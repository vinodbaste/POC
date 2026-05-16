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
    start = text.find("{")
    end = text.rfind("}")
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
        "You are an evaluation judge grading an agent's JSON output against a gold oracle for an "
        "OlymMATH combinatorics solution-audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- incoherent_or_truncated\n"
        "- deterministic_chain_misconception\n"
        "- unsupported_constant_answer\n"
        "- power_of_two_leap\n"
        "- correct_recurrence_arithmetic_error\n"
        "- inconsistent_boxing\n\n"
        "Field meanings:\n"
        "- gold_final_answer: literal string '948'.\n"
        "- acceptable_solution_ids: response letters whose extracted answer is 948 AND whose reasoning chain "
        "establishes 948 without an inconsistent leap (i.e. final_answer_correct is true AND failure_reasons "
        "is empty).\n"
        "- final_answer_correct: whether that response's extracted final answer equals the gold integer 948 "
        "(literal string compare after whitespace strip).\n"
        "- failure_reasons: exact set of concrete reasons why the response's reasoning is defective. It must "
        "be empty iff the response's extracted answer is 948 AND the reasoning chain establishes 948.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For gold_final_answer, require the literal string '948'.\n"
        "2. For acceptable_solution_ids, require the same set of uppercase letters as the oracle.\n"
        "3. per_response_assessment must contain exactly one object for each response A through O.\n"
        "4. For solution_id and final_answer_correct, require exact equality.\n"
        "5. For failure_reasons, order does not matter, but the set must match exactly. Extra reasons fail. "
        "Missing reasons fail. No partial credit inside failure_reasons.\n"
        "6. A per-response audit receives credit only if solution_id, final_answer_correct, and the exact "
        "failure_reasons set are all correct for that response.\n\n"
        "Scoring rubric with weighted points:\n"
        "- gold_final_answer = 2 points.\n"
        "- acceptable_solution_ids = 2 points.\n"
        "- Each response audit A through O is all-or-nothing = 30 points. Award the 30 points only if "
        "solution_id, final_answer_correct, and exact failure_reasons set all match the oracle for that "
        "response. Otherwise award 0 for that response.\n"
        "- Total = 454 points. score = passed/454.\n\n"
        "Respond in JSON only, no markdown: "
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 454, "justification": "<concise weighted '
        'field-by-field breakdown, under 600 characters>"}'
    )

    messages = [
        {"role": "system", "content": "Respond with one valid JSON object only. Keep justification under 600 characters. No prose outside the JSON."},
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
                '{"score": <float 0.0-1.0>, "passed": <int>, "total": 454, "justification": "<short>"}\n\n'
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
    score = max(0.0, min(1.0, score))
    json.dump({"reward": score}, open(args.reward_out, "w"))
    with open(justification_path, "w") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', 454)} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
