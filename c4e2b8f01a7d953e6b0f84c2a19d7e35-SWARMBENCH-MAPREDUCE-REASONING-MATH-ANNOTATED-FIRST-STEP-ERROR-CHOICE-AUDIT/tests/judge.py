import argparse
import json
import os
import re
import urllib.error
import urllib.request


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1 and end > start:
        return text[start:end + 1]
    return text


def validate_structure(agent_output: dict) -> list[str]:
    """
    Pre-LLM structural checks that enforce all instruction.md requirements
    not easily caught by exact-match or LLM scoring.
    Returns a list of violation strings (empty = pass).
    """
    violations = []

    # 1. Required top-level keys only (no extra keys allowed)
    required_keys = {"artifact_audits", "shard_summaries", "summary"}
    extra_keys = set(agent_output.keys()) - required_keys
    if extra_keys:
        violations.append(f"Extra top-level keys not in schema: {sorted(extra_keys)}")
    missing_keys = required_keys - set(agent_output.keys())
    if missing_keys:
        violations.append(f"Missing required top-level keys: {sorted(missing_keys)}")
        return violations  # can't check further

    # 2. artifact_audits must be sorted by artifact_id (lexicographic ascending)
    audits = agent_output.get("artifact_audits", [])
    audit_ids = [a.get("artifact_id", "") for a in audits]
    if audit_ids != sorted(audit_ids):
        violations.append(
            f"artifact_audits is not sorted by artifact_id. "
            f"Got: {audit_ids[:5]}... Expected lexicographic ascending order."
        )

    # 3. shard_summaries must be sorted by shard_id (lexicographic ascending)
    shards = agent_output.get("shard_summaries", [])
    shard_ids = [s.get("shard_id", "") for s in shards]
    if shard_ids != sorted(shard_ids):
        violations.append(
            f"shard_summaries is not sorted by shard_id. "
            f"Got: {shard_ids}"
        )

    # 4. artifacts_by_option lists must each be sorted by artifact_id
    abo = agent_output.get("summary", {}).get("artifacts_by_option", {})
    for opt, art_list in abo.items():
        if not isinstance(art_list, list):
            violations.append(f"artifacts_by_option['{opt}'] is not a list")
            continue
        if art_list != sorted(art_list):
            violations.append(
                f"artifacts_by_option['{opt}'] is not sorted by artifact_id. "
                f"Got: {art_list}"
            )

    return violations


def call_fireworks(messages, max_tokens=700, timeout=240):
    payload = {
        "model": "accounts/fireworks/models/kimi-k2p5",
        "messages": messages,
        "temperature": 0,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_object"},
    }
    request = urllib.request.Request(
        "https://api.fireworks.ai/inference/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {os.environ['FIREWORKS_API_KEY']}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = json.loads(response.read().decode("utf-8"))
    return body.get("choices", [{}])[0].get("message", {}).get("content", "") or ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    args = parser.parse_args()

    try:
        agent_output = json.load(open(args.agent_output))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}")
        return

    oracle = json.load(open(args.oracle))

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    # --- Pre-LLM structural validation ---
    violations = validate_structure(agent_output)
    if violations:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write(
                "Score: 0.0\n\n"
                "Structural validation failed — instruction requirements not met:\n"
                + "\n".join(f"  - {v}" for v in violations)
            )
        return

    # --- LLM judge for content correctness ---
    prompt = (
        "Grade the agent output against the gold oracle.\n\n"
        f"ORACLE:\n{json.dumps(oracle, separators=(',', ':'))}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, separators=(',', ':'))}\n\n"
        "Scoring rules:\n"
        "- For each artifact in artifact_audits, artifact_id, problem_id, competition, "
        "year, and selected_option must match exactly, in the same order.\n"
        "- For each shard summary, shard_id, artifact_ids, artifact_count, and "
        "choice_counts must match exactly, in the same shard order.\n"
        "- In summary, total_artifacts, choice_counts, competition_counts, year_counts, "
        "and artifacts_by_option must match exactly, with lists in the same sorted order.\n"
        "- Score is the fraction of artifact rows plus summary groups that pass.\n"
        "Return one JSON object only using this schema: "
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": <int>, '
        '"justification": "<brief list of failed artifact_ids or failed summary groups>"}'
    )

    messages = [
        {"role": "system", "content": "Respond with one valid JSON object only. No prose outside the JSON."},
        {"role": "user", "content": prompt},
    ]

    try:
        raw = call_fireworks(messages)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write(f"Score: 0.0\n\nJudge request failed: {e}")
        return

    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError:
        repair_messages = [
            {"role": "system", "content": "Convert the user content into one valid JSON object only. Do not add commentary."},
            {"role": "user", "content": (
                "The following model output was supposed to follow this schema exactly:\n"
                '{"score": <float 0.0-1.0>, "passed": <int>, "total": <int>, "justification": "<brief>"}\n\n'
                "Convert it to valid JSON without changing the meaning.\n\n"
                f"MODEL OUTPUT:\n{raw}"
            )},
        ]
        try:
            repaired_raw = call_fireworks(repair_messages, max_tokens=300, timeout=180)
            result = json.loads(extract_json(repaired_raw))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            json.dump({"reward": 0.0}, open(args.reward_out, "w"))
            with open("/logs/agent/judge_justification.txt", "w") as f:
                f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw: {raw}")
            return

    score = float(result.get("score", 0.0))
    json.dump({"reward": score}, open(args.reward_out, "w"))
    with open("/logs/agent/judge_justification.txt", "w") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', '?')} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
