#!/usr/bin/env python3
"""Executable verifier for the hexagonal-prism geodesic audit task.

Pure stdlib. Per-field exact equality. Oracle-keyed accumulation loops with no
agent-keyed dedup loopholes. Reward clamped to [0, 1] with literal min/max.
Every IO/JSON failure path writes reward 0.0 (fail-closed)."""

from __future__ import annotations

import argparse
import json
import os
from typing import Any


GOLD_POINTS = 30
ANCHOR_POINTS_PER = 6
ACCEPTABLE_IDS_POINTS = 5
AUDIT_POINTS_PER = 25
N_ANCHORS = 5
N_RESPONSES = 7

TOTAL_POINTS = (
    GOLD_POINTS
    + N_ANCHORS * ANCHOR_POINTS_PER
    + ACCEPTABLE_IDS_POINTS
    + N_RESPONSES * AUDIT_POINTS_PER
)


def _decomposition_matches(agent_val: Any, oracle_val: dict[str, int]) -> bool:
    if not isinstance(agent_val, dict):
        return False
    return (
        agent_val.get("rational_part") == oracle_val["rational_part"]
        and agent_val.get("radical_coefficient_sqrt3")
        == oracle_val["radical_coefficient_sqrt3"]
    )


def _score(agent: dict, oracle: dict) -> tuple[int, list[str]]:
    passed = 0
    notes: list[str] = []

    if _decomposition_matches(
        agent.get("gold_distance_squared_decomposition"),
        oracle["gold_distance_squared_decomposition"],
    ):
        passed += GOLD_POINTS
    else:
        notes.append(
            "gold_distance_squared_decomposition: mismatch "
            f"(expected {oracle['gold_distance_squared_decomposition']}, "
            f"got {agent.get('gold_distance_squared_decomposition')})"
        )

    agent_anchors = agent.get("small_case_anchor_results") or {}
    if not isinstance(agent_anchors, dict):
        agent_anchors = {}
    for anchor_name, anchor_oracle in oracle["small_case_anchor_results"].items():
        if _decomposition_matches(agent_anchors.get(anchor_name), anchor_oracle):
            passed += ANCHOR_POINTS_PER
        else:
            notes.append(
                f"anchor {anchor_name}: mismatch "
                f"(expected {anchor_oracle}, got {agent_anchors.get(anchor_name)})"
            )

    agent_ids = agent.get("acceptable_solution_ids")
    if isinstance(agent_ids, list) and set(agent_ids) == set(
        oracle["acceptable_solution_ids"]
    ):
        passed += ACCEPTABLE_IDS_POINTS
    else:
        notes.append(
            f"acceptable_solution_ids: mismatch "
            f"(expected {sorted(oracle['acceptable_solution_ids'])}, "
            f"got {agent_ids!r})"
        )

    oracle_by_id = {a["response_id"]: a for a in oracle["per_response_assessment"]}
    agent_list = agent.get("per_response_assessment") or []
    agent_by_id: dict[str, dict] = {}
    if isinstance(agent_list, list):
        for entry in agent_list:
            if (
                isinstance(entry, dict)
                and isinstance(entry.get("response_id"), str)
                and entry["response_id"] not in agent_by_id
            ):
                agent_by_id[entry["response_id"]] = entry

    for rid, oa in oracle_by_id.items():
        aa = agent_by_id.get(rid)
        if (
            isinstance(aa, dict)
            and aa.get("response_id") == rid
            and aa.get("final_answer_correct") == oa["final_answer_correct"]
            and isinstance(aa.get("failure_reasons"), list)
            and set(aa["failure_reasons"]) == set(oa["failure_reasons"])
        ):
            passed += AUDIT_POINTS_PER
        else:
            notes.append(f"audit {rid}: per-field mismatch")

    return passed, notes


def _write_reward(reward_path: str, reward: float, justification: str) -> None:
    reward = max(0.0, min(1.0, float(reward)))
    os.makedirs(os.path.dirname(reward_path), exist_ok=True)
    with open(reward_path, "w", encoding="utf-8") as f:
        json.dump({"reward": reward}, f)
    try:
        os.makedirs("/logs/agent", exist_ok=True)
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: {reward:.6f}\n\n{justification}\n")
    except OSError:
        pass


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    parser.add_argument("--details-out", required=False)
    args = parser.parse_args()

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        _write_reward(args.reward_out, 0.0, f"Agent output missing or invalid JSON: {e}")
        return

    try:
        with open(args.oracle, "r", encoding="utf-8") as f:
            oracle = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        _write_reward(args.reward_out, 0.0, f"Oracle missing or invalid JSON: {e}")
        return

    if not isinstance(agent, dict):
        _write_reward(args.reward_out, 0.0, "Agent output is not a JSON object.")
        return

    passed, notes = _score(agent, oracle)
    reward = max(0.0, min(1.0, passed / TOTAL_POINTS))
    justification = (
        f"Deterministic per-field score: {passed}/{TOTAL_POINTS} = {reward:.4f}\n\n"
        + ("\n".join(notes) if notes else "All graded fields matched the oracle.")
    )
    _write_reward(args.reward_out, reward, justification)

    if args.details_out:
        try:
            os.makedirs(os.path.dirname(args.details_out), exist_ok=True)
            with open(args.details_out, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "passed_points": passed,
                        "total_points": TOTAL_POINTS,
                        "reward": reward,
                        "notes": notes,
                    },
                    f,
                    indent=2,
                )
        except OSError:
            pass


if __name__ == "__main__":
    main()
