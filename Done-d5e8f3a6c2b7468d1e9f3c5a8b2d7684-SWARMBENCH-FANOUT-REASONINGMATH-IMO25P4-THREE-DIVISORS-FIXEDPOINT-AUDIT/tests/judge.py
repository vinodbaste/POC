"""Deterministic executable verifier for the modified IMO 2025 P4 audit.

Reward is passed / TOTAL_POINTS clamped to [0, 1]. Fail-closes to 0.0 on
any IO/JSON error. Per-response 20 pts all-or-nothing.
"""

import argparse
import json
import os
from typing import Any


TOTAL_POINTS = 390
ALLOWED_CODES = {"F1", "F2", "F3", "F4"}


def _score(agent: dict, oracle: dict) -> tuple[int, list[str]]:
    passed = 0
    notes: list[str] = []

    a_ans = agent.get("answer", {}) if isinstance(agent.get("answer"), dict) else {}
    o_ans = oracle["answer"]
    if a_ans.get("fixed_point_count") == o_ans["fixed_point_count"]:
        passed += 50
    else:
        notes.append(f"answer.fixed_point_count: {a_ans.get('fixed_point_count')!r} != {o_ans['fixed_point_count']!r}")

    a_anch = agent.get("anchor_results", {}) if isinstance(agent.get("anchor_results"), dict) else {}
    for k, v in oracle["anchor_results"].items():
        if a_anch.get(k) == v:
            passed += 10
        else:
            notes.append(f"anchor_results.{k}: {a_anch.get(k)!r} != {v!r}")

    if set(agent.get("acceptable_solution_ids", []) or []) == set(oracle["acceptable_solution_ids"]):
        passed += 10
    else:
        notes.append(
            f"acceptable_solution_ids: {agent.get('acceptable_solution_ids')!r} != {oracle['acceptable_solution_ids']!r}"
        )

    oracle_by_id = {a["response_id"]: a for a in oracle["per_response_assessment"]}
    agent_list = agent.get("per_response_assessment", []) or []
    agent_by_id: dict[str, Any] = {}
    if isinstance(agent_list, list):
        for entry in agent_list:
            if isinstance(entry, dict) and "response_id" in entry:
                agent_by_id.setdefault(entry["response_id"], entry)

    for rid, oa in oracle_by_id.items():
        aa = agent_by_id.get(rid)
        if aa is None:
            notes.append(f"audit {rid}: missing")
            continue
        agent_codes = aa.get("failure_reasons", []) or []
        if not isinstance(agent_codes, list):
            agent_codes = []
        agent_code_set = set(agent_codes)
        if not agent_code_set.issubset(ALLOWED_CODES):
            notes.append(f"audit {rid}: out-of-vocab codes {agent_code_set - ALLOWED_CODES}")
            continue
        if (
            aa.get("response_id") == oa["response_id"]
            and aa.get("final_answer_correct") == oa["final_answer_correct"]
            and agent_code_set == set(oa["failure_reasons"])
        ):
            passed += 20
        else:
            notes.append(
                f"audit {rid}: final_answer_correct={aa.get('final_answer_correct')!r} oracle={oa['final_answer_correct']!r}; "
                f"failure_reasons={sorted(agent_code_set)!r} oracle={sorted(oa['failure_reasons'])!r}"
            )

    return passed, notes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)
    just_path = "/logs/verifier/judge_justification.txt"
    os.makedirs(os.path.dirname(just_path), exist_ok=True)

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent = json.load(f)
        with open(args.oracle, "r", encoding="utf-8") as f:
            oracle = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        with open(args.reward_out, "w", encoding="utf-8") as f:
            json.dump({"reward": 0.0}, f)
        with open(just_path, "w", encoding="utf-8") as f:
            f.write(f"Score: 0.0\n\nFail-closed: {e}\n")
        return

    passed, notes = _score(agent, oracle)
    reward = max(0.0, min(1.0, passed / TOTAL_POINTS))
    with open(args.reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": reward}, f)
    with open(just_path, "w", encoding="utf-8") as f:
        f.write(f"Score: {reward:.4f} ({passed}/{TOTAL_POINTS} points)\n\n" + "\n".join(notes) + "\n")


if __name__ == "__main__":
    main()
