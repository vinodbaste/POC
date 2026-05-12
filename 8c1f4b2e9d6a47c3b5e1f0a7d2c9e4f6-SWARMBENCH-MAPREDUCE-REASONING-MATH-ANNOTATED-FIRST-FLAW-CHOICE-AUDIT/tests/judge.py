import argparse
import json
import os
import re
import urllib.error
import urllib.request


VALID_OPTIONS = {"A", "B", "C", "D"}
VALID_FLAW_TYPES = {"unjustified_claim", "misapplied_theorem", "false_assumption", "scope_violation", "algebraic_error"}
AUDIT_REQUIRED_KEYS = {"artifact_id", "problem_id", "competition", "year", "selected_option", "flaw_type"}
SHARD_REQUIRED_KEYS = {"shard_id", "artifact_ids", "artifact_count", "choice_counts"}


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
    violations = []

    required_keys = {"artifact_audits", "shard_summaries", "summary"}
    extra_keys = set(agent_output.keys()) - required_keys
    if extra_keys:
        violations.append(f"Extra top-level keys not in schema: {sorted(extra_keys)}")
    missing_keys = required_keys - set(agent_output.keys())
    if missing_keys:
        violations.append(f"Missing required top-level keys: {sorted(missing_keys)}")
        return violations

    audits = agent_output.get("artifact_audits", [])
    audit_ids = []
    for idx, audit in enumerate(audits):
        missing = AUDIT_REQUIRED_KEYS - set(audit.keys())
        if missing:
            violations.append(f"artifact_audits[{idx}] missing fields: {sorted(missing)}")
            continue
        audit_ids.append(audit["artifact_id"])
        opt = audit.get("selected_option")
        if opt not in VALID_OPTIONS:
            violations.append(
                f"artifact_audits[{idx}] ({audit['artifact_id']}): "
                f"selected_option={opt!r} is not one of A, B, C, D"
            )
        flaw = audit.get("flaw_type")
        if flaw not in VALID_FLAW_TYPES:
            violations.append(
                f"artifact_audits[{idx}] ({audit['artifact_id']}): "
                f"flaw_type={flaw!r} is not one of the valid flaw types"
            )

    if audit_ids != sorted(audit_ids):
        violations.append(f"artifact_audits is not sorted by artifact_id. First few: {audit_ids[:5]}")

    expected_ids = [f"artifact_{i:02d}" for i in range(1, 76)]
    missing_artifacts = set(expected_ids) - set(audit_ids)
    if missing_artifacts:
        violations.append(
            f"artifact_audits is missing {len(missing_artifacts)} artifact(s): "
            + ", ".join(sorted(missing_artifacts)[:5])
            + ("..." if len(missing_artifacts) > 5 else "")
        )

    shards = agent_output.get("shard_summaries", [])
    shard_ids = [s.get("shard_id", "") for s in shards]
    if shard_ids != sorted(shard_ids):
        violations.append(f"shard_summaries is not sorted by shard_id. Got: {shard_ids}")

    for idx, shard in enumerate(shards):
        missing = SHARD_REQUIRED_KEYS - set(shard.keys())
        if missing:
            violations.append(f"shard_summaries[{idx}] missing fields: {sorted(missing)}")
            continue
        art_ids = shard.get("artifact_ids", [])
        art_count = shard.get("artifact_count")
        if isinstance(art_ids, list) and art_count != len(art_ids):
            violations.append(
                f"shard_summaries[{idx}] ({shard['shard_id']}): "
                f"artifact_count={art_count} does not match len(artifact_ids)={len(art_ids)}"
            )

    abo = agent_output.get("summary", {}).get("artifacts_by_option", {})
    for opt, art_list in abo.items():
        if isinstance(art_list, list) and art_list != sorted(art_list):
            violations.append(f"artifacts_by_option['{opt}'] is not sorted. Got: {art_list}")

    return violations


def call_fireworks(messages, max_tokens=800, timeout=240):
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

    justification_path = "/logs/agent/judge_justification.txt"

    try:
        raw = open(args.agent_output).read()
        agent_output = json.loads(extract_json(raw))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid JSON: {e}")
        return

    oracle = json.load(open(args.oracle))

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    violations = validate_structure(agent_output)
    if violations:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write(
                "Score: 0.0\n\nStructural validation failed — instruction requirements not met:\n"
                + "\n".join(f"  - {v}" for v in violations)
            )
        return

    prompt = (
        "Grade the agent output against the gold oracle for this olympiad proof-flaw audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, separators=(',', ':'))}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, separators=(',', ':'))}\n\n"
        "Scoring rules:\n"
        "- For each artifact in artifact_audits, artifact_id, problem_id, competition, year, "
        "selected_option, and flaw_type must all match the oracle exactly, in sorted artifact_id order.\n"
        "- For each shard summary, shard_id, artifact_ids, artifact_count, and choice_counts "
        "must match exactly, in the same shard order.\n"
        "- In summary, total_artifacts, choice_counts, competition_counts, year_counts, and "
        "artifacts_by_option must match exactly, with lists in sorted order.\n"
        "- Score is the fraction of artifact rows plus summary groups that are fully correct.\n"
        "Return one JSON object only using this schema: "
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": <int>, '
        '"justification": "<brief list of failed artifact_ids and failed summary groups>"}'
    )

    messages = [
        {"role": "system", "content": "Respond with one valid JSON object only. No prose outside the JSON."},
        {"role": "user", "content": prompt},
    ]

    try:
        raw = call_fireworks(messages)
    except (urllib.error.URLError, TimeoutError, KeyError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
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
            with open(justification_path, "w") as f:
                f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw: {raw}")
            return

    score = float(result.get("score", 0.0))
    json.dump({"reward": score}, open(args.reward_out, "w"))
    with open(justification_path, "w") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', '?')} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
