"""Deterministic verifier — TETRIS-pattern set-match scoring.

No LLM called. Compares agent /logs/agent/output.json against /tests/oracle.json.

Top-level scoring (4 pts, cheap direct math facts):
  - gold_set (set match against ["a","b","c","d","e"]):     2 pts
  - acceptable_solution_ids (set match against ["A","D","I"]): 2 pts

Per-response scoring (30 pts each, 9 responses):
  - failure_reasons (SET MATCH — all-or-nothing, exact set equality): 30 pts

Total max = 4 + 9 * 30 = 274 pts. Reward = total_passed / 274.

The set-match on failure_reasons is the structural lever: each response has 0-3
specific failure-reason labels drawn from a granular task-specific vocabulary,
and the agent must produce the EXACT set (no extras, no omissions) per response.
Subsets and supersets both score 0 for that response.
"""

import argparse
import json
import os
from typing import Any, Dict, List, Set


REQUIRED_TOP_KEYS = {"gold_set", "acceptable_solution_ids", "per_response_assessment"}

TOP_LEVEL_WEIGHTS = {
    "gold_set": 2,
    "acceptable_solution_ids": 2,
}

PER_RESPONSE_WEIGHT = 30


def write_reward(score: float, reward_out: str, justification: str) -> None:
    os.makedirs(os.path.dirname(reward_out), exist_ok=True)
    with open(reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": max(0.0, min(1.0, score))}, f)
    just_path = "/logs/agent/judge_justification.txt"
    os.makedirs(os.path.dirname(just_path), exist_ok=True)
    with open(just_path, "w", encoding="utf-8") as f:
        f.write(justification)


def norm_str(v: Any) -> str:
    return str(v if v is not None else "").strip()


def as_lower_set(items: Any) -> Set[str]:
    if not isinstance(items, list):
        return set()
    return {norm_str(x).lower() for x in items if norm_str(x) != ""}


def as_upper_set(items: Any) -> Set[str]:
    if not isinstance(items, list):
        return set()
    return {norm_str(x).upper() for x in items if norm_str(x) != ""}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()

    try:
        with open(args.agent_output, encoding="utf-8") as f:
            agent = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        write_reward(0.0, args.reward_out, f"Score: 0.0\n\nAgent output missing or invalid JSON: {e}")
        return

    with open(args.oracle, encoding="utf-8") as f:
        oracle = json.load(f)

    if agent == oracle:
        write_reward(1.0, args.reward_out, "Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    if not isinstance(agent, dict):
        write_reward(0.0, args.reward_out, "Score: 0.0\n\nAgent output is not a JSON object.")
        return

    oracle_assessment: List[Dict[str, Any]] = oracle["per_response_assessment"]
    total_max = sum(TOP_LEVEL_WEIGHTS.values()) + len(oracle_assessment) * PER_RESPONSE_WEIGHT
    total_passed = 0
    lines: List[str] = []

    oracle_gold = as_lower_set(oracle.get("gold_set"))
    agent_gold = as_lower_set(agent.get("gold_set"))
    if oracle_gold == agent_gold and oracle_gold:
        total_passed += TOP_LEVEL_WEIGHTS["gold_set"]
        lines.append(f"gold_set=2/2 (matched {sorted(oracle_gold)})")
    else:
        lines.append(f"gold_set=0/2 (got={sorted(agent_gold)}, expected={sorted(oracle_gold)})")

    oracle_accept = as_upper_set(oracle.get("acceptable_solution_ids"))
    agent_accept = as_upper_set(agent.get("acceptable_solution_ids"))
    if oracle_accept == agent_accept and oracle_accept:
        total_passed += TOP_LEVEL_WEIGHTS["acceptable_solution_ids"]
        lines.append(f"acceptable_solution_ids=2/2 (matched {sorted(oracle_accept)})")
    else:
        lines.append(f"acceptable_solution_ids=0/2 (got={sorted(agent_accept)}, expected={sorted(oracle_accept)})")

    agent_assessment_raw = agent.get("per_response_assessment")
    if not isinstance(agent_assessment_raw, list):
        agent_assessment_raw = []

    oracle_by_id = {norm_str(r.get("response_id")).upper(): r for r in oracle_assessment}
    agent_by_id = {
        norm_str(r.get("response_id")).upper(): r
        for r in agent_assessment_raw
        if isinstance(r, dict)
    }

    for resp_id in sorted(oracle_by_id.keys()):
        o = oracle_by_id[resp_id]
        a = agent_by_id.get(resp_id, {})
        exp_set = as_lower_set(o.get("failure_reasons"))
        got_set = as_lower_set(a.get("failure_reasons"))
        if exp_set == got_set:
            total_passed += PER_RESPONSE_WEIGHT
            lines.append(
                f"Response {resp_id}: failure_reasons={PER_RESPONSE_WEIGHT}/{PER_RESPONSE_WEIGHT} "
                f"(set match: {sorted(exp_set) if exp_set else '[]'})"
            )
        else:
            missing = sorted(exp_set - got_set)
            extra = sorted(got_set - exp_set)
            lines.append(
                f"Response {resp_id}: failure_reasons=0/{PER_RESPONSE_WEIGHT} "
                f"(missing={missing}, extra={extra}, expected={sorted(exp_set)}, got={sorted(got_set)})"
            )

    score = total_passed / total_max if total_max > 0 else 0.0
    justification = f"Score: {score:.4f} ({total_passed}/{total_max} passed)\n\n" + "\n".join(lines)
    write_reward(score, args.reward_out, justification)


if __name__ == "__main__":
    main()
