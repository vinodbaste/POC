import argparse
import json
import os
import re
from openai import OpenAI


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent_output = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w", encoding="utf-8"))
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}")
        return

    with open(args.oracle, "r", encoding="utf-8") as f:
        oracle = json.load(f)

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w", encoding="utf-8"))
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    client = OpenAI(
        api_key=os.environ["FIREWORKS_API_KEY"],
        base_url="https://api.fireworks.ai/inference/v1",
    )

    prompt = (
        "You are an evaluation judge grading an agent's JSON output against a gold oracle "
        "for a tree path-decomposition counting solution-audit task. The agent reports a single "
        "integer count modulo a prime, an acceptable_solution_ids set, and a per-response audit "
        "for nine candidate responses A through I.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- wrong_formula\n"
        "- arithmetic_error\n"
        "- invalid_or_incomplete_justification\n"
        "- final_answer_error\n\n"
        "Field meanings:\n"
        "- correct_answer: a single integer in [0, prime) giving the verified count of valid arrays "
        "modulo the prime stated in the problem.\n"
        "- acceptable_solution_ids: the response letters whose final stated value modulo the prime is correct "
        "AND whose derivation is mathematically valid.\n"
        "- final_answer_correct: whether that response gives the correct value modulo the prime AND its derivation is valid.\n"
        "- failure_reasons: exact set of concrete reasons why the response is wrong. It must be empty iff "
        "final_answer_correct is true.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For correct_answer, require exact integer equality.\n"
        "2. For acceptable_solution_ids, require the same set of response letters as the oracle (order-insensitive).\n"
        "3. per_response_assessment must contain exactly one object for each response A through I (nine entries).\n"
        "4. For response_id and final_answer_correct, require exact equality with the oracle.\n"
        "5. For failure_reasons, order does not matter, but the set must match exactly. Extra reasons fail. "
        "Missing reasons fail. No partial credit inside failure_reasons.\n"
        "6. A per-response audit receives credit only if response_id, final_answer_correct, and the exact "
        "failure_reasons set are all correct for that response.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_answer correct = 2 points.\n"
        "- acceptable_solution_ids = 2 points.\n"
        "- Each response audit A-I is all-or-nothing = 30 points. Award the 30 points only if response_id, "
        "final_answer_correct, and the exact failure_reasons set all match the oracle for that response. "
        "Otherwise award 0 for that response.\n"
        "- Total = 274 points (4 scalar + 9 * 30). score = passed/274.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 274, '
        '"justification": "<concise weighted field-by-field breakdown>"}'
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2p5",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    raw = response.choices[0].message.content or ""

    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w", encoding="utf-8"))
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw: {raw}")
        return

    score = max(0.0, min(1.0, float(result.get("score", 0.0))))
    json.dump({"reward": score}, open(args.reward_out, "w", encoding="utf-8"))

    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', '?')} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
