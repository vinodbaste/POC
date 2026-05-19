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
        "for a harmonic-pairs counting solution-audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- misstates_problem_setup\n"
        "- wrong_fermat_constraint\n"
        "- no_systematic_enumeration\n"
        "- no_visible_derivation\n"
        "- arbitrary_final_count\n"
        "- non_terminating_or_no_final_integer\n\n"
        "Field meanings:\n"
        "- correct_count: the correct number of harmonic ordered pairs (a, b) in S.\n"
        "- correct_valid_d_set: sorted-ascending list of prime numbers p such that p divides gcd(a+1, b+1) for at least one harmonic pair. Derived from Hensel lifts of -1 mod p^2 falling in [2, 200].\n"
        "- correct_valid_k_set: sorted-ascending list of integers k in [2, 200] such that at least one harmonic pair (a, b) satisfies a*b + a + b = k^2.\n"
        "- code_application_table: object mapping each failure-reason code to the sorted-alphabetical list of response_ids on which that code fires; every code in the vocabulary must appear as a key.\n"
        "- acceptable_solution_ids: response letters whose final integer answers equal correct_count AND whose failure_reasons list is empty.\n"
        "- final_answer_correct: whether that response's final committed integer answer equals correct_count.\n"
        "- failure_reasons: exact set of concrete reasons why the response's reasoning is defective. Empty iff final_answer_correct is true AND no trigger fires.\n"
        "- evidence_quote_per_code: per response, object mapping each applied code to a verbatim quote (>= 10 chars, or the entire response if shorter) from that response file demonstrating the trigger.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For correct_count, require exact integer equality with the oracle.\n"
        "2. For correct_valid_d_set and correct_valid_k_set, require exact set equality (ignoring sort order if both are well-formed lists, but the agent's output should be sorted ascending).\n"
        "3. For code_application_table, require exact match per key: each code's list of response_ids must equal the oracle's list as a set; every code in the controlled vocabulary must appear as a key.\n"
        "4. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        "5. per_response_assessment must contain exactly one object for each response A-F.\n"
        "6. For response_id and final_answer_correct, require exact equality.\n"
        "7. For failure_reasons, order does not matter, but the set must match exactly. Extra reasons fail. Missing reasons fail. No partial credit inside failure_reasons.\n"
        "8. For evidence_quote_per_code, require that the dict has one entry per code in failure_reasons AND each entry is a non-empty string of length >= 10 characters (or the entire response content if the response is shorter than 10 characters). Do not require exact match to oracle's quote (the agent may quote different substring); just verify presence and length.\n"
        "9. A per-response audit receives full credit only if response_id, final_answer_correct, the exact failure_reasons set, AND a well-formed evidence_quote_per_code (entry per code, each >= 10 chars unless the response is shorter) all match for that response.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_count = 4 points (exact integer match).\n"
        "- correct_valid_d_set = 6 points (exact set match, all-or-nothing).\n"
        "- correct_valid_k_set = 6 points (exact set match, all-or-nothing).\n"
        "- code_application_table = 12 points (2 points per failure-reason key, all-or-nothing per key on set equality).\n"
        "- acceptable_solution_ids = 2 points (exact set match).\n"
        "- Each response audit A-F is all-or-nothing = 30 points. Award the 30 points only if response_id, final_answer_correct, exact failure_reasons set, AND well-formed evidence_quote_per_code (one >= 10-char entry per applied code, or the entire response content if shorter than 10 chars) all match the oracle for that response. Otherwise award 0 for that response.\n"
        "- Total = 210 points. score = passed/210.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 210, '
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
