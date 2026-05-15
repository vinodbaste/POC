import argparse
import json
import os
from typing import Any



REQUIRED_TOP_KEYS = {"response_audits"}

FIELD_WEIGHTS = {
    "final_answer_correct": 1,
    "proof_valid": 1,
    "verdict": 1,
    "primary_error_label": 40,
    "required_evidence_label": 2,
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

    expected_by_id = as_map_by_response_id(oracle.get("response_audits"))
    actual_by_id = as_map_by_response_id(agent_output.get("response_audits"))
    total_points = len(expected_by_id) * sum(FIELD_WEIGHTS.values())

    expected_ids = set(expected_by_id)
    actual_ids = set(actual_by_id)

    passed = 0
    details = []

    if actual_ids != expected_ids:
        details.append(
            f"response_ids mismatch: expected {sorted(expected_ids)}, got {sorted(actual_ids)}"
        )

    for rid in sorted(expected_by_id):
        exp = expected_by_id[rid]
        act = actual_by_id.get(rid, {})
        response_points = 0
        field_details = []

        for field, weight in FIELD_WEIGHTS.items():
            ok = act.get(field) == exp.get(field)
            points = weight if ok else 0
            response_points += points
            field_details.append(
                f"{field}={points}/{weight} "
                f"(got={act.get(field)!r}, expected={exp.get(field)!r})"
            )

        passed += response_points
        details.append(f"Response {rid}: {response_points}/10; " + "; ".join(field_details))

    score = passed / total_points
    write_reward(
        score,
        args.reward_out,
        f"Score: {score:.3f} ({passed}/{total_points} passed)\n\n" + "\n".join(details),
    )


if __name__ == "__main__":
    main()
