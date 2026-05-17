import argparse
import json
import os
import re
from openai import OpenAI


TOTAL_POINTS = 824


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
        "for a mathematical solution-audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Correct mathematics for reference:\n"
        "- 2197 = 13^3 and phi(13^3)=2028.\n"
        "- First appearance in slot 1 on day 2028 requires order exactly 2028 modulo 13^3.\n"
        "- The correct valid count among m in {0,...,9999} is 2840.\n"
        "- The correct probability is 2840/10000 = 71/250.\n"
        "- The correct p+q mod 1000 is 321.\n\n"
        "Field meanings and strict equivalence rules:\n"
        "- correct_answer_mod1000 must be integer 321.\n"
        "- correct_probability_latex must be mathematically equivalent to 71/250 in exact LaTeX form.\n"
        "- valid_m_count must be integer 2840.\n"
        "- acceptable_solution_ids must be the same set of response letters as the oracle.\n"
        "- per_response_assessment must contain exactly one object for each response A-H.\n"
        "- response_id must be exact.\n"
        "- extracted_final_answer_mod1000 must be the response's own final residue, not the corrected answer.\n"
        "- primary_error_code must exactly match the oracle's single best main-error code for that response.\n"
        "- For all boolean fields, require the same true/false value as the oracle. String booleans fail.\n"
        "- uses_correct_factorization_2197_as_13_cubed is true only for explicit use of 2197=13^3 without incompatible factorization.\n"
        "- identifies_order_2028_condition is true only for explicit recognition of exact multiplicative order 2028, not merely m^2028=1.\n"
        "- computes_primitive_root_count_624 is true only for the correct count phi(2028)=624 or equivalent.\n"
        "- performs_exact_nonuniform_range_count is true only for exact treatment of m=0,...,9999 yielding 2840 or 71/250.\n"
        "- uses_invalid_uniformity_or_average_assumption is true for expected, average, random, approximate, statistical, or uniform primitive-root distribution over a partial interval.\n"
        "- has_denominator_or_sample_space_error is true for denominator 9999, using only a 2197-residue sample space for final probability, or failing to divide a count by 10000.\n"
        "- has_final_answer_critical_mathematical_error is true for any false mathematical claim or invalid counting/probability argument that materially changes the final answer.\n"
        "- has_calculation_error is true only for arithmetic, algebraic, factorization, totient, or equation-solving mistakes; do not mark it merely for invalid uniformity.\n"
        "- has_unjustified_step is true for final-answer-critical assertions without exact derivation.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_answer_mod1000 = 10 points.\n"
        "- correct_probability_latex = 8 points.\n"
        "- valid_m_count = 8 points.\n"
        "- acceptable_solution_ids = 30 points.\n"
        "- For each response object: response_id = 1, extracted_final_answer_mod1000 = 1, "
        "primary_error_code = 60, final_answer_correct = 2, uses_correct_factorization_2197_as_13_cubed = 1, "
        "identifies_order_2028_condition = 1, computes_primitive_root_count_624 = 1, "
        "performs_exact_nonuniform_range_count = 2, uses_invalid_uniformity_or_average_assumption = 1, "
        "has_denominator_or_sample_space_error = 20, has_final_answer_critical_mathematical_error = 2, "
        "has_calculation_error = 1, has_unjustified_step = 1, has_stepwise_structure = 1, "
        "has_proper_latex_format = 1.\n"
        "- Per-response total = 96 points, eight responses = 768 points.\n"
        "- Total = 824 points. score = passed/824.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 824, '
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
