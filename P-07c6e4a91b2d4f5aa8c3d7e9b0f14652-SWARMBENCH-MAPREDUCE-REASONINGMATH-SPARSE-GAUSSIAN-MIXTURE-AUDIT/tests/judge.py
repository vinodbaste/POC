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
        "for a mathematical solution-audit task about sparse Gaussian mixture detection.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Field meanings:\n"
        "- correct_answer_letters: the correct list of original test letters with power tending to 1.\n"
        "- acceptable_solution_ids: the response letters that fully and rigorously solve the problem.\n"
        "- detection_boundary_latex: the correct boundary value for beta=0.85 in standard LaTeX.\n"
        "- extracted_final_answer_letters: the final answer claimed by each response, as uppercase letters A/B/C, or null if missing.\n"
        "- final_answer_correct: whether the claimed final list is exactly [B, C].\n"
        "- test_a_conclusion_correct: whether the response concludes that the mean z-test fails to have power tending to 1.\n"
        "- uses_correct_donoho_jin_boundary: whether the response uses (1 - sqrt(1 - beta))^2, or an exactly equivalent condition, for beta=0.85.\n"
        "- boundary_numeric_value_correct: whether the response gives about 0.375 or the exact expression (1 - sqrt(0.15))^2.\n"
        "- compares_r_to_boundary_correctly: whether the response correctly says 0.45 is above the correct boundary.\n"
        "- test_b_conclusion_correct: whether the response concludes that the maximum test has power tending to 1.\n"
        "- test_c_conclusion_correct: whether the response concludes that Higher Criticism has power tending to 1.\n"
        "- has_final_answer_critical_math_error: whether the response has a final-answer-critical false theorem, wrong boundary, wrong extreme-value comparison, wrong scaling, or invalid reasoning.\n"
        "- has_calculation_error: whether the response has an arithmetic, algebraic, exponent-sign, or equation-solving error after its stated premises.\n"
        "- has_unjustified_step: whether the response has a final-answer-critical inference without adequate support and not already just an explicit false claim.\n"
        "- has_stepwise_structure: whether the response has explicit steps, bullets, headings, or a table separating reasoning stages.\n"
        "- has_proper_latex_format: whether notation is mostly valid readable LaTeX and not substantially HTML/non-LaTeX markup.\n\n"
        "Equivalence rules:\n"
        "1. For correct_answer_letters and acceptable_solution_ids, require the same set and alphabetical order as the oracle.\n"
        "2. For detection_boundary_latex, accept mathematically equivalent exact LaTeX forms and approximate values around 0.3754.\n"
        "3. For boolean fields, require the same true/false value as the oracle. String booleans fail.\n"
        "4. For response_id, require exact letters A-F.\n"
        "5. per_response_assessment must contain exactly one object for each response A-F.\n\n"
        "Scoring rubric with weighted points:\n"
        "- Top-level fields have low weight because they are coarse summary fields: correct_answer_letters = 1, acceptable_solution_ids = 1, detection_boundary_latex = 1.\n"
        "- Every per-response field has base weight 1: response_id, extracted_final_answer_letters, final_answer_correct, test_a_conclusion_correct, uses_correct_donoho_jin_boundary, boundary_numeric_value_correct, compares_r_to_boundary_correctly, test_b_conclusion_correct, test_c_conclusion_correct, has_final_answer_critical_math_error, has_calculation_error, has_unjustified_step, has_stepwise_structure, has_proper_latex_format.\n"
        "- The following mathematical audit fields have critical weight 50 instead of base weight 1 because they test subtle boundary, comparison, and final-answer-critical error classification rather than simple extraction or formatting:\n"
        "  * Response B compares_r_to_boundary_correctly.\n"
        "  * Response D compares_r_to_boundary_correctly.\n"
        "  * Response D has_calculation_error.\n"
        "  * Response E uses_correct_donoho_jin_boundary.\n"
        "  * Response E boundary_numeric_value_correct.\n"
        "  * Response E compares_r_to_boundary_correctly.\n"
        "  * Response E has_final_answer_critical_math_error.\n"
        "  * Response F test_a_conclusion_correct.\n"
        "  * Response F has_final_answer_critical_math_error.\n"
        "- Total = 528 points. score = passed/528.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 528, '
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
