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
    # 2 pts gold_final_answer + 2 pts gold_edge_length_squared_set + 2 pts acceptable_solution_ids + 30 per response
    total_points = 6 + 30 * response_count
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
        "for a Cube-Plane Distances 3D geometry audit task.\n\n"
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
        "Field meanings:\n"
        "- gold_final_answer: the string form of the integer sum of squares over all distinct edge-length values in S.\n"
        "- gold_edge_length_squared_set: the sorted integer list of all distinct s^2 values across every sign-pattern family.\n"
        "- acceptable_solution_ids: the response letters whose final answer equals the gold answer AND whose failure_reasons list is empty.\n"
        "- final_answer_correct: whether that response's claimed final answer equals the gold answer exactly.\n"
        "- failure_reasons: exact set of concrete reasons why the response's reasoning is defective. Must be empty iff final_answer_correct is true AND no failure-reason trigger fires on the response.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For gold_final_answer, require exact string equality with the oracle.\n"
        "2. For gold_edge_length_squared_set, require equality as a sorted integer list.\n"
        "3. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        f"4. per_response_assessment must contain exactly one object for each response {response_id_text}.\n"
        "5. For response_id and final_answer_correct, require exact equality.\n"
        "6. For failure_reasons, order does not matter, but the set must match exactly. Extra reasons fail. Missing reasons fail. No partial credit inside failure_reasons.\n"
        "7. A per-response audit receives credit only if response_id, final_answer_correct, and the exact failure_reasons set are all correct for that response.\n\n"
        "Scoring rubric with weighted points:\n"
        "- gold_final_answer = 2 points.\n"
        "- gold_edge_length_squared_set = 2 points.\n"
        "- acceptable_solution_ids = 2 points.\n"
        f"- Each response audit {response_id_text} is all-or-nothing = 30 points. Award the 30 points only if response_id, final_answer_correct, and exact failure_reasons set all match the oracle for that response. Otherwise award 0 for that response.\n"
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
