import argparse
import json
import os
import re
from openai import OpenAI

BT = chr(96) * 3

def extract_json(text: str) -> str:
    text = text.strip()
    pattern = re.escape(BT) + r"(?:json)?\s*([\s\S]*?)" + re.escape(BT)
    match = re.search(pattern, text)
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
        "for a mathematical solution-audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Field meanings:\n"
        "- correct_order: the correct optimal chronological task order, as a normalized string.\n"
        "- acceptable_solution_ids: the list of response letters that fully solve the problem.\n"
        "- extracted_final_order: the final task order claimed by each response, as a normalized string, or null if missing.\n"
        "- final_order_correct: whether the claimed final order is mathematically equivalent to the correct optimal order.\n"
        "- joint_task_requirements_correct: whether the response correctly identifies which tasks require both runners and which are solo-capable.\n"
        "- flag_dependency_correct: whether the response respects the forced flag dependency chain relevant to the final order.\n"
        "- parallel_solo_block_correct: whether the response identifies the optimal use of simultaneous solo-capable work in the schedule.\n"
        "- has_feasibility_error: whether the response proposes a physically or logically impossible schedule.\n"
        "- has_optimization_error: whether the final order is not globally optimal or the response omits a shorter feasible strategy.\n"
        "- has_calculation_error: whether the response has a concrete distance, arithmetic, algebraic, or numerical mistake after its stated premises.\n"
        "- has_unjustified_step: whether a final-answer-critical inference is asserted without adequate justification.\n"
        "- has_stepwise_structure: whether the response has explicit steps, numbered stages, bullet stages, or section headings.\n"
        "- has_required_answer_format: whether the response gives a bracketed order beginning with 1 and ending with 7, using set notation for claimed simultaneous tasks if any.\n\n"
        "Equivalence rules:\n"
        "1. For correct_order and extracted_final_order, accept harmless whitespace differences and equivalent ordering inside a simultaneous set.\n"
        "2. For boolean fields, require the same true/false value as the oracle. String booleans fail.\n"
        "3. For response_id, require exact letters A-H.\n"
        "4. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        "5. per_response_assessment must contain exactly one object for each response A-H in order.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_order = 10 points.\n"
        "- acceptable_solution_ids = 10 points.\n"
        "- For each response object: response_id = 1, extracted_final_order = 1, "
        "final_order_correct = 4, joint_task_requirements_correct = 15, flag_dependency_correct = 2, "
        "parallel_solo_block_correct = 4, has_feasibility_error = 3, has_optimization_error = 4, "
        "has_calculation_error = 10, has_unjustified_step = 15, has_stepwise_structure = 1, "
        "has_required_answer_format = 1.\n"
        "- Per-response total = 61 points, eight responses = 488 points.\n"
        "- Total = 508 points. score = passed/508.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 508, '
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
