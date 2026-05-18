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
    parser.add_argument("--details-out", required=False, default=None)
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

    response_count = len(oracle.get("per_response_assessment", []))
    total_points = 4 + 30 * response_count
    response_ids = [
        item.get("response_id")
        for item in oracle.get("per_response_assessment", [])
        if item.get("response_id")
    ]
    response_id_text = f"{response_ids[0]}-{response_ids[-1]}" if response_ids else "listed responses"

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
        "for a Square-Triangle Subtraction Game P/N classification audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- wrong_base_case\n"
        "- missing_subtraction_moves\n"
        "- pn_convention_swapped\n"
        "- wrong_loss_convention\n"
        "- truncated_or_short_string\n"
        "- arbitrary_pattern_heuristic\n"
        "- arithmetic_recursion_error\n"
        "- non_terminating_or_no_final_string\n\n"
        "Field meanings:\n"
        "- correct_classification_string: the 131-character P/N classification string for pile sizes 0 through 130.\n"
        "- acceptable_solution_ids: the response letters whose classification strings equal the gold string AND whose failure_reasons list is empty.\n"
        "- classification_correct: whether that response's claimed 131-character classification string equals the gold string exactly.\n"
        "- failure_reasons: exact set of concrete reasons why the response's reasoning is defective. Must be empty iff classification_correct is true AND no failure-reason trigger fires on the response.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For correct_classification_string, require exact 131-character string equality with the oracle.\n"
        "2. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        f"3. per_response_assessment must contain exactly one object for each response {response_id_text}.\n"
        "4. For response_id and classification_correct, require exact equality.\n"
        "5. For failure_reasons, order does not matter, but the set must match exactly. Extra reasons fail. Missing reasons fail. No partial credit inside failure_reasons.\n"
        "6. A per-response audit receives credit only if response_id, classification_correct, and the exact failure_reasons set are all correct for that response.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_classification_string = 2 points.\n"
        "- acceptable_solution_ids = 2 points.\n"
        f"- Each response audit {response_id_text} is all-or-nothing = 30 points. Award the 30 points only if response_id, classification_correct, and exact failure_reasons set all match the oracle for that response. Otherwise award 0 for that response.\n"
        f"- Total = {total_points} points. score = passed/{total_points}.\n\n"
        "Respond in JSON only, no markdown:\n"
        f'{{"score": <float 0.0-1.0>, "passed": <int>, "total": {total_points}, '
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
