#!/usr/bin/env python3
"""Executable verifier for the PlantGrowth one-way ANOVA audit.

Deterministic, Python standard library only. Compares /logs/agent/output.json to
the withheld oracle field-by-field. A structural breach fails closed to 0.0; an
output byte-equal in value to the oracle scores 1.0.

Point budget (TOTAL_POINTS):
  - gold_F_x1000               : 2 pts  (within +/- 1 of oracle integer)
  - acceptable_solution_ids    : 2 pts  (unordered set equality)
  - per_response_assessment    : 10 x 30 = 300 pts, all-or-nothing per response
  TOTAL                        : 304
"""
import argparse
import json
import os

TOTAL_POINTS = 304
ALLOWED_CODES = {"C1", "C2", "C3", "C4", "C5", "C6"}
EXPECTED_IDS = [chr(ord("A") + i) for i in range(10)]  # A..J


def _structural_ok(agent: dict) -> bool:
    """Hard gate. Any violation must fail the whole submission to 0.0."""
    if not isinstance(agent, dict):
        return False
    if set(agent.keys()) != {"gold_F_x1000", "acceptable_solution_ids", "per_response_assessment"}:
        return False
    if not isinstance(agent["gold_F_x1000"], int) or isinstance(agent["gold_F_x1000"], bool):
        return False
    ids = agent["acceptable_solution_ids"]
    if not isinstance(ids, list) or len(ids) != len(set(ids)):
        return False
    if any(i not in EXPECTED_IDS for i in ids):
        return False
    pra = agent["per_response_assessment"]
    if not isinstance(pra, list) or len(pra) != len(EXPECTED_IDS):
        return False
    if [e.get("response_id") if isinstance(e, dict) else None for e in pra] != EXPECTED_IDS:
        return False
    for e in pra:
        if set(e.keys()) != {"response_id", "final_answer_correct", "failure_reasons"}:
            return False
        if not isinstance(e["final_answer_correct"], bool):
            return False
        fr = e["failure_reasons"]
        if not isinstance(fr, list) or len(fr) != len(set(fr)):
            return False
        if any(c not in ALLOWED_CODES for c in fr):
            return False
    return True


def _score(agent: dict, oracle: dict) -> tuple[int, list[str]]:
    passed = 0
    notes: list[str] = []

    if abs(agent["gold_F_x1000"] - oracle["gold_F_x1000"]) <= 1:
        passed += 2
    else:
        notes.append(f"gold_F_x1000 {agent['gold_F_x1000']} != {oracle['gold_F_x1000']}")

    if set(agent["acceptable_solution_ids"]) == set(oracle["acceptable_solution_ids"]):
        passed += 2
    else:
        notes.append("acceptable_solution_ids: set mismatch")

    oracle_by_id = {a["response_id"]: a for a in oracle["per_response_assessment"]}
    agent_by_id = {a["response_id"]: a for a in agent["per_response_assessment"]}
    for rid, oa in oracle_by_id.items():
        aa = agent_by_id.get(rid)
        if (
            aa is not None
            and aa.get("final_answer_correct") == oa["final_answer_correct"]
            and set(aa.get("failure_reasons", [])) == set(oa["failure_reasons"])
        ):
            passed += 30
        else:
            notes.append(f"audit {rid}: mismatch")

    return passed, notes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)
    just_path = "/logs/agent/judge_justification.txt"
    try:
        os.makedirs(os.path.dirname(just_path), exist_ok=True)
    except OSError:
        just_path = os.path.join(os.path.dirname(args.reward_out), "judge_justification.txt")

    def emit(reward: float, text: str) -> None:
        with open(args.reward_out, "w", encoding="utf-8") as fh:
            json.dump({"reward": reward}, fh)
        try:
            with open(just_path, "w", encoding="utf-8") as fh:
                fh.write(text)
        except OSError:
            pass

    try:
        with open(args.agent_output, "r", encoding="utf-8") as fh:
            agent = json.load(fh)
        with open(args.oracle, "r", encoding="utf-8") as fh:
            oracle = json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        emit(0.0, f"Score: 0.0\n\nFail-closed (read/parse): {e}")
        return

    if not _structural_ok(agent):
        emit(0.0, "Score: 0.0\n\nFail-closed: structural gate violation.")
        return

    passed, notes = _score(agent, oracle)
    reward = max(0.0, min(1.0, passed / TOTAL_POINTS))
    emit(reward, f"Score: {reward:.4f} ({passed}/{TOTAL_POINTS} points)\n\n" + "\n".join(notes))


if __name__ == "__main__":
    main()
