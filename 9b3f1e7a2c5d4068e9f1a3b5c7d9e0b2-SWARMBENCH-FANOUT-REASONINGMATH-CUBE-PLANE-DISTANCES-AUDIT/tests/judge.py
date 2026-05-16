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
        "for a cube-plane-distances solution-audit task with multiple independent deliverable groups.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- claims_unique_edge_length\n"
        "- restricts_to_nonnegative_subset_sums\n"
        "- assumes_max_distance_equals_space_diagonal\n"
        "- assumes_plane_parallel_to_cube_face\n"
        "- equates_max_distance_with_edge_length_directly\n"
        "- uses_fabricated_invariant_or_invalid_derivation\n"
        "- accepts_internal_contradictions_in_derivation\n"
        "- assumes_zero_distance_vertex_is_axis_corner\n"
        "- omits_sign_pattern_casework\n"
        "- treats_one_orientation_as_proof_of_uniqueness\n"
        "- derives_correct_partial_s2_then_discards_it\n"
        "- non_terminating_or_no_final_answer\n\n"
        "Top-level field meanings:\n"
        "- gold_final_answer: literal string \"210\".\n"
        "- gold_edge_length_squared_set: [21, 54, 66, 69] (multiset equality, order irrelevant).\n"
        "- gold_case_a_s_squared: 21 (the all-positive orientation).\n"
        "- gold_case_b_s_squared_values: [54, 66, 69] (the sign-flipped orientations).\n"
        "- gold_axis_lengths_triples: [[1, 2, 4], [1, 2, 7], [1, 4, 7], [2, 4, 7]] (multiset equality on the outer list; each inner triple is a sorted ascending list).\n"
        "- total_distinct_orientations: 4.\n"
        "- acceptable_solution_ids: the response letters whose final numeric answers equal the gold AND whose failure_reasons list is empty (oracle: [] empty list).\n\n"
        "Per-response field meanings:\n"
        "- response_id: \"A\" through \"I\".\n"
        "- extracted_final_answer: the response's claimed numeric answer as a string, normalized as the response wrote it; null only for responses with no identifiable final numeric answer.\n"
        "- final_answer_correct: whether the response's final stated numeric answer equals 210.\n"
        "- failure_reasons: exact set of concrete reasons why the response's reasoning is defective. It must be empty iff final_answer_correct is true AND no failure-reason trigger fires.\n\n"
        "Cross-response synthesis:\n"
        "- failure_reason_frequency: a dict mapping each of the 12 failure-reason codes to the integer count of how many per-response failure_reasons lists contain that code. All 12 codes must be present as keys.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For gold_final_answer, gold_case_a_s_squared, total_distinct_orientations, require exact equality with the oracle.\n"
        "2. For gold_edge_length_squared_set and gold_case_b_s_squared_values, require the same multiset of integers as the oracle (order irrelevant).\n"
        "3. For gold_axis_lengths_triples, require the same multiset of inner sorted triples as the oracle (order of the outer list irrelevant; inner triples must be ascending-sorted).\n"
        "4. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        "5. per_response_assessment must contain exactly one object for each response A-I. For response_id, extracted_final_answer, and final_answer_correct, require exact equality (use null for missing extracted answers). For failure_reasons, order does not matter, but the set must match exactly — extra reasons fail, missing reasons fail, no partial credit inside.\n"
        "6. A per-response audit receives credit only if response_id, extracted_final_answer, final_answer_correct, AND the exact failure_reasons set all match the oracle for that response. Otherwise zero for that response.\n"
        "7. For failure_reason_frequency, require all 12 codes present as keys AND each integer value to match the oracle exactly.\n\n"
        "Scoring rubric with weighted points:\n"
        "- gold_final_answer = 2 points.\n"
        "- gold_edge_length_squared_set = 2 points.\n"
        "- gold_case_a_s_squared = 2 points.\n"
        "- gold_case_b_s_squared_values = 2 points.\n"
        "- gold_axis_lengths_triples = 4 points.\n"
        "- total_distinct_orientations = 2 points.\n"
        "- acceptable_solution_ids = 2 points.\n"
        "- failure_reason_frequency = 6 points (award only if ALL 12 (code, count) entries match the oracle exactly; otherwise 0).\n"
        "- Each response audit A-I is all-or-nothing = 30 points. Award 30 only if response_id, extracted_final_answer, final_answer_correct, AND exact failure_reasons set all match. Otherwise 0 for that response.\n"
        "- Total = 22 + 9*30 = 292 points. score = passed/292.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 292, '
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
