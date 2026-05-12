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


def call_fireworks(messages, max_tokens=4000, timeout=240):
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
        "Grade the agent output against the gold oracle for this IMO solution-grading task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, separators=(',', ':'))}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, separators=(',', ':'))}\n\n"
        "Scoring rules (total 170 points):\n"
        "- TOP-LEVEL KEYS CHECK: the agent output must contain exactly these three top-level "
        "keys: grading_audits, shard_summaries, summary. If any extra top-level key is present, "
        "set passed = 0 and score = 0.0 immediately — the structure is non-conformant.\n"
        "- SORT-ORDER CHECK on grading_audits: the agent output's grading_audits list MUST be "
        "sorted by artifact_id in lexicographic ascending order (artifact_001, artifact_002, "
        "..., artifact_150). Verify by walking the list. If the list is not sorted, the row "
        "score for grading_audits is automatically 0 / 150 (treat every row as failed). The "
        "shard_summaries and summary points are still scored normally.\n"
        "- SORT-ORDER CHECK on shard_summaries: shard_summaries MUST be sorted by shard_id "
        "ascending. If not, set shard score to 0 / 15.\n"
        "- 150 points: one per grading_audits row (only counted when the list is sorted). "
        "A row PASSES iff the agent's predicted_grade for that artifact_id MATCHES the oracle's "
        "predicted_grade for the same artifact_id. Match by artifact_id; ignore grading_id, "
        "problem_id, imo_area for row matching.\n"
        "- 15 points: one per shard_summaries entry (only counted when sorted). A shard PASSES "
        "iff shard_id, artifact_ids (as a set), artifact_count, AND grade_counts all match the "
        "oracle. Match by shard_id.\n"
        "- 5 points: one each for the summary subgroups total_artifacts, grade_counts, area_counts, "
        "grade_by_area, artifacts_by_grade. Each PASSES iff the value matches the oracle (as sets "
        "for lists, exact for ints/maps). artifacts_by_grade lists must themselves be sorted by "
        "artifact_id; if any list inside artifacts_by_grade is not sorted, that subgroup fails.\n"
        "- score = passed / 170.\n\n"
        "Compute passed (integer 0-170) and score = passed / 170.\n"
        "Return ONE JSON object only, with a SHORT justification (under 300 characters) - list "
        "counts and at most 5 sample failed artifact_ids. DO NOT enumerate every artifact. "
        "Schema: "
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 170, "justification": "<short summary>"}'
    )

    messages = [
        {"role": "system", "content": "Respond with one valid JSON object only. Keep justification under 300 characters. No prose outside the JSON."},
        {"role": "user", "content": prompt},
    ]

    try:
        raw = call_fireworks(messages, max_tokens=4000)
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
                '{"score": <float 0.0-1.0>, "passed": <int>, "total": 170, "justification": "<short>"}\n\n'
                "Convert it to valid JSON without changing the meaning.\n\n"
                f"MODEL OUTPUT:\n{raw[:6000]}"
            )},
        ]
        try:
            repaired_raw = call_fireworks(repair_messages, max_tokens=800, timeout=180)
            result = json.loads(extract_json(repaired_raw))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            json.dump({"reward": 0.0}, open(args.reward_out, "w"))
            with open(justification_path, "w") as f:
                f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw: {raw[:1000]}")
            return

    score = float(result.get("score", 0.0))
    json.dump({"reward": score}, open(args.reward_out, "w"))
    with open(justification_path, "w") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', 171)} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
