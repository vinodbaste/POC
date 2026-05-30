import argparse
import json
import os
import re


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    return text


def write_failure(reward_out: str, message: str) -> None:
    os.makedirs(os.path.dirname(reward_out), exist_ok=True)
    with open(reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": 0.0}, f)
    os.makedirs("/logs/agent", exist_ok=True)
    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(f"Score: 0.0\n\n{message}")


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
        write_failure(args.reward_out, f"Agent output missing or invalid: {e}")
        return

    try:
        with open(args.oracle, "r", encoding="utf-8") as f:
            oracle = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        write_failure(args.reward_out, f"Oracle missing or invalid: {e}")
        return

    if agent_output == oracle:
        with open(args.reward_out, "w", encoding="utf-8") as f:
            json.dump({"reward": 1.0}, f)
        os.makedirs("/logs/agent", exist_ok=True)
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    try:
        from openai import OpenAI
    except Exception as e:
        write_failure(args.reward_out, f"Judge dependency failure: could not import OpenAI: {e}")
        return

    try:
        api_key = os.environ["FIREWORKS_API_KEY"]
    except KeyError as e:
        write_failure(args.reward_out, f"Judge configuration failure: missing environment variable {e}")
        return

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.fireworks.ai/inference/v1",
    )

    prompt = (
        "You are an evaluation judge grading an agent's JSON output against a gold oracle "
        "for a Rubik's-cube mathematical solution-audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Field meanings:\n"
        "- correct_sum: the correct final integer sum on the front face.\n"
        "- acceptable_solution_ids: the list of response letters that are fully acceptable solutions.\n"
        "- extracted_final_sum: the final numerical sum claimed by each response, or null if missing.\n"
        "- final_sum_correct: whether the claimed final sum equals the correct final sum.\n"
        "- acceptable_solution: whether the response is fully acceptable, including correct final sum, no final-answer-critical tracking error, no arithmetic error, and enough front-face tracking/provenance.\n"
        "- has_standard_notation_tracking_error: whether the response has a final-answer-critical wrong standard Rubik move tracking claim.\n"
        "- has_arithmetic_error: whether the response has an arithmetic or algebraic mistake after its stated sticker counts or final grid.\n"
        "- has_unsupported_front_face_tracking: whether the response asserts a final-answer-critical front-face count/grid without enough checkable tracking or provenance.\n"
        "- has_numbered_step_structure: whether the response has numbered steps, numbered stages, or numbered sections.\n"
        "- has_readable_math_format: whether the math notation and displayed calculations are readable and not severely malformed.\n\n"
        "Equivalence rules:\n"
        "1. For integer sums, require exact integer equality. Numeric strings fail.\n"
        "2. For boolean fields, require the same true/false value as the oracle. String booleans fail.\n"
        "3. For response_id, require exact letters A-G.\n"
        "4. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        "5. per_response_assessment must contain exactly one object for each response A-G.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_sum = 10 points.\n"
        "- acceptable_solution_ids = 20 points.\n"
        "- For each response object: response_id = 1, extracted_final_sum = 1, "
        "final_sum_correct = 5, acceptable_solution = 8, "
        "has_standard_notation_tracking_error = 8, has_arithmetic_error = 1, "
        "has_unsupported_front_face_tracking = 1, has_numbered_step_structure = 1, "
        "has_readable_math_format = 1.\n"
        "- Per-response total = 27 points, seven responses = 189 points.\n"
        "- Total = 219 points. score = passed/219.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 219, '
        '"justification": "<concise weighted field-by-field breakdown>"}'
    )

    try:
        response = client.chat.completions.create(
            model="accounts/fireworks/models/kimi-k2p5",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        raw = response.choices[0].message.content or ""
    except Exception as e:
        write_failure(args.reward_out, f"Judge API failure: {type(e).__name__}: {e}")
        return

    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError as e:
        write_failure(args.reward_out, f"Judge parse error: {e}\nRaw: {raw}")
        return

    try:
        score = float(result.get("score", 0.0))
    except (TypeError, ValueError) as e:
        write_failure(args.reward_out, f"Judge returned non-numeric score: {e}\nRaw result: {result}")
        return

    score = max(0.0, min(1.0, score))
    with open(args.reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": score}, f)

    os.makedirs("/logs/agent", exist_ok=True)
    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', '?')} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
