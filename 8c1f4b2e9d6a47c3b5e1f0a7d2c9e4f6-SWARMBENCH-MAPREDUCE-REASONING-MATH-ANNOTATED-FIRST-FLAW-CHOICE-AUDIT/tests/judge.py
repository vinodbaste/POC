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

    prompt = (
        "Grade the agent output against the gold oracle for this olympiad proof-flaw audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, separators=(',', ':'))}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, separators=(',', ':'))}\n\n"
        "Scoring rules:\n"
        "- For each artifact in artifact_audits, artifact_id, problem_id, competition, year, "
        "selected_option, and flaw_type must all match the oracle exactly.\n"
        "- artifact_audits must be sorted by artifact_id (lexicographic ascending). "
        "If the order is wrong, count every misordered row as failed.\n"
        "- For each shard summary, shard_id, artifact_ids, artifact_count, and choice_counts "
        "must match the oracle exactly. shard_summaries must be sorted by shard_id.\n"
        "- In summary, total_artifacts, choice_counts, competition_counts, year_counts, and "
        "artifacts_by_option must match the oracle exactly, with artifacts_by_option lists "
        "sorted by artifact_id.\n"
        "- The top-level keys must be exactly artifact_audits, shard_summaries, and summary — "
        "no extra keys. Treat any extra top-level key as one failed summary group.\n"
        "- Score is the fraction of artifact rows plus summary groups (shard_summaries entries "
        "and the 5 summary subgroups) that are fully correct, out of the total checkable items.\n"
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
