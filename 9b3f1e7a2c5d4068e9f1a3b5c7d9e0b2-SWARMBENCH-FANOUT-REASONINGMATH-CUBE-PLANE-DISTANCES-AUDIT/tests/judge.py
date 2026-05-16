import argparse
import json
import os
from typing import Any


REQUIRED_TOP_KEYS = {
    "gold_final_answer",
    "gold_edge_length_squared_set",
    "acceptable_solution_ids",
    "per_response_assessment",
}

TOP_LEVEL_WEIGHTS = {
    "gold_final_answer": 2,
    "gold_edge_length_squared_set": 2,
    "acceptable_solution_ids": 2,
}

PER_RESPONSE_WEIGHTS = {
    "response_id": 1,
    "extracted_final_answer": 1,
    "final_answer_correct": 1,
    "final_answer_category": 4,
    "claims_unique_edge_length": 2,
    "derives_s2_equals_21_for_some_orientation": 4,
    "uses_axis_aligned_cube_at_origin_with_zero_vertex_at_corner": 4,
    "equates_max_distance_with_space_diagonal": 2,
    "assumes_plane_parallel_to_cube_face": 2,
    "equates_max_distance_with_edge_length_directly": 2,
    "uses_fabricated_invariant_or_invalid_derivation": 2,
    "restricts_to_nonnegative_subset_sums": 2,
    "reasoning_coherence_level": 3,
}


def write_reward(score: float, reward_out: str, justification: str) -> None:
    os.makedirs(os.path.dirname(reward_out), exist_ok=True)
    with open(reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": max(0.0, min(1.0, score))}, f)
    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(justification)


def as_map_by_response_id(items: Any) -> dict:
    if not isinstance(items, list):
        return {}
    out = {}
    for item in items:
        if isinstance(item, dict) and isinstance(item.get("response_id"), str):
            out[item["response_id"]] = item
    return out


def normalize_string(v: Any) -> Any:
    if isinstance(v, str):
        return v.strip()
    return v


def normalize_int_list(v: Any) -> Any:
    if isinstance(v, list):
        try:
            return sorted(int(x) for x in v)
        except (TypeError, ValueError):
            return v
    return v


def normalize_letter_list(v: Any) -> Any:
    if isinstance(v, list):
        try:
            return sorted(str(x).upper() for x in v)
        except (TypeError, ValueError):
            return v
    return v


def field_equal(field: str, got: Any, expected: Any) -> bool:
    if field == "gold_edge_length_squared_set":
        return normalize_int_list(got) == normalize_int_list(expected)
    if field == "acceptable_solution_ids":
        return normalize_letter_list(got) == normalize_letter_list(expected)
    if isinstance(expected, str):
        return normalize_string(got) == normalize_string(expected)
    return got == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent_output = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        write_reward(
            0.0,
            args.reward_out,
            f"Score: 0.0\n\nAgent output missing or invalid: {e}",
        )
        return

    with open(args.oracle, "r", encoding="utf-8") as f:
        oracle = json.load(f)

    if not isinstance(agent_output, dict):
        write_reward(
            0.0,
            args.reward_out,
            "Score: 0.0\n\nAgent output must be a JSON object.",
        )
        return

    actual_keys = set(agent_output.keys())
    extra_keys = sorted(actual_keys - REQUIRED_TOP_KEYS)
    missing_keys = sorted(REQUIRED_TOP_KEYS - actual_keys)
    if extra_keys or missing_keys:
        write_reward(
            0.0,
            args.reward_out,
            "Score: 0.0\n\nTop-level schema mismatch. "
            f"Extra keys: {extra_keys}. Missing keys: {missing_keys}.",
        )
        return

    per_response_total = sum(PER_RESPONSE_WEIGHTS.values())
    expected_by_id = as_map_by_response_id(oracle.get("per_response_assessment"))
    actual_by_id = as_map_by_response_id(agent_output.get("per_response_assessment"))
    n_responses = len(expected_by_id)
    total_points = sum(TOP_LEVEL_WEIGHTS.values()) + n_responses * per_response_total

    passed = 0
    details = []

    for field, weight in TOP_LEVEL_WEIGHTS.items():
        got = agent_output.get(field)
        expected = oracle.get(field)
        ok = field_equal(field, got, expected)
        points = weight if ok else 0
        passed += points
        details.append(
            f"top-level {field}: {points}/{weight} "
            f"(got={got!r}, expected={expected!r})"
        )

    expected_ids = set(expected_by_id)
    actual_ids = set(actual_by_id)
    if actual_ids != expected_ids:
        details.append(
            f"response_ids mismatch: expected {sorted(expected_ids)}, got {sorted(actual_ids)}"
        )

    for rid in sorted(expected_by_id):
        exp = expected_by_id[rid]
        act = actual_by_id.get(rid, {})
        response_points = 0
        field_details = []

        for field, weight in PER_RESPONSE_WEIGHTS.items():
            got = act.get(field)
            expected = exp.get(field)
            ok = field_equal(field, got, expected)
            points = weight if ok else 0
            response_points += points
            field_details.append(
                f"{field}={points}/{weight} "
                f"(got={got!r}, expected={expected!r})"
            )

        passed += response_points
        details.append(
            f"Response {rid}: {response_points}/{per_response_total}; "
            + "; ".join(field_details)
        )

    score = passed / total_points if total_points else 0.0
    write_reward(
        score,
        args.reward_out,
        f"Score: {score:.4f} ({passed}/{total_points} passed)\n\n"
        + "\n".join(details),
    )


if __name__ == "__main__":
    main()
