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
        "for a mathematical solution-audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Field meanings:\n"
        "- correct_answer_latex: the correct constant c in standard LaTeX closed form.\n"
        "- acceptable_solution_ids: the list of response letters that fully solve the problem.\n"
        "- extracted_final_answer_latex: the final constant claimed by each response, in LaTeX closed form, or null if missing.\n"
        "- final_answer_correct: whether the claimed final constant is mathematically equal to the correct c.\n"
        "- has_mathematical_error: whether the response has a final-answer-critical false claim, wrong theorem, wrong scaling, wrong limiting law, or invalid reasoning.\n"
        "- has_calculation_error: whether the response has an arithmetic, algebraic, or equation-solving error after its stated premises.\n"
        "- has_unjustified_step: whether the response has a final-answer-critical inference without adequate justification.\n"
        "- has_stepwise_structure: whether the response has explicit steps, numbered stages, bullet stages, or section headings that separate reasoning stages.\n"
        "- has_proper_latex_format: whether the mathematical notation is mostly valid and readable LaTeX.\n\n"
        "Equivalence rules:\n"
        "1. For constants, accept mathematically equivalent exact LaTeX forms, including usual variants of ln/log notation.\n"
        "2. For boolean fields, require the same true/false value as the oracle. String booleans fail.\n"
        "3. For response_id, require exact letters A-F.\n"
        "4. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        "5. per_response_assessment must contain exactly one object for each response A-F.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_answer_latex = 10 points.\n"
        "- acceptable_solution_ids = 10 points.\n"
        "- For each response object: response_id = 1, extracted_final_answer_latex = 1, "
        "final_answer_correct = 3, has_mathematical_error = 3, has_calculation_error = 1, "
        "has_unjustified_step = 1, has_stepwise_structure = 1, has_proper_latex_format = 1.\n"
        "- Per-response total = 12 points, six responses = 72 points.\n"
        "- Total = 92 points. score = passed/92.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 92, '
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
