"""Deterministic verifier — Task-B-style scoring.

No LLM called. Compares agent /logs/agent/output.json against /tests/oracle.json.

Per-response scoring (45 pts each, 7 responses, 315 total):
  - final_answer_correct (bool match):       1 pt
  - proof_valid          (bool match):       1 pt
  - verdict              (exact string):     1 pt
  - primary_error_label  (exact string):    40 pts   <- dominant lever
  - required_evidence_label (exact string):  2 pts

Reward = total_passed / 315.

The primary_error_label vocabulary is task-specific and granular — there is one
canonical label per oracle entry, and labels do not appear in the instruction's
vocabulary unless the candidate's audit needs them. This forces the agent to
identify each candidate's specific error pattern, not pick from a generic list.
"""

import argparse
import json
import os
from typing import Any, Dict, List


REQUIRED_TOP_KEYS = {"response_audits"}

FIELD_WEIGHTS = {
    "final_answer_correct": 1,
    "proof_valid": 1,
    "verdict": 1,
    "primary_error_label": 40,
    "required_evidence_label": 2,
}

MAX_PER_RESPONSE = sum(FIELD_WEIGHTS.values())  # 45


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


def equal_str_ci(a: Any, b: Any) -> bool:
    return norm_str(a).lower() == norm_str(b).lower()


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

    # Exact-match shortcut for oracle agent path
    if agent == oracle:
        write_reward(1.0, args.reward_out, "Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    # Top-level structure check
    if not isinstance(agent, dict) or "response_audits" not in agent or not isinstance(agent["response_audits"], list):
        write_reward(0.0, args.reward_out, "Score: 0.0\n\nMissing or non-list 'response_audits' top-level key.")
        return

    oracle_audits: List[Dict[str, Any]] = oracle["response_audits"]
    agent_audits: List[Dict[str, Any]] = agent["response_audits"]
    oracle_by_id = {norm_str(a.get("response_id")).upper(): a for a in oracle_audits}
    agent_by_id = {norm_str(a.get("response_id")).upper(): a for a in agent_audits if isinstance(a, dict)}

    total_max = len(oracle_audits) * MAX_PER_RESPONSE
    total_passed = 0
    lines: List[str] = []

    for resp_id in sorted(oracle_by_id.keys()):
        o = oracle_by_id[resp_id]
        a = agent_by_id.get(resp_id, {})
        row_passed = 0
        details = []
        # final_answer_correct (bool)
        got = a.get("final_answer_correct"); exp = o.get("final_answer_correct")
        if isinstance(got, bool) and isinstance(exp, bool) and got == exp:
            row_passed += FIELD_WEIGHTS["final_answer_correct"]
            details.append(f"final_answer_correct=1/1")
        else:
            details.append(f"final_answer_correct=0/1 (got={got!r}, expected={exp!r})")
        # proof_valid (bool)
        got = a.get("proof_valid"); exp = o.get("proof_valid")
        if isinstance(got, bool) and isinstance(exp, bool) and got == exp:
            row_passed += FIELD_WEIGHTS["proof_valid"]
            details.append(f"proof_valid=1/1")
        else:
            details.append(f"proof_valid=0/1 (got={got!r}, expected={exp!r})")
        # verdict (exact string)
        got = a.get("verdict"); exp = o.get("verdict")
        if equal_str_ci(got, exp):
            row_passed += FIELD_WEIGHTS["verdict"]
            details.append(f"verdict=1/1")
        else:
            details.append(f"verdict=0/1 (got={norm_str(got)!r}, expected={norm_str(exp)!r})")
        # primary_error_label (exact string — 40 pts)
        got = a.get("primary_error_label"); exp = o.get("primary_error_label")
        if equal_str_ci(got, exp):
            row_passed += FIELD_WEIGHTS["primary_error_label"]
            details.append(f"primary_error_label=40/40")
        else:
            details.append(f"primary_error_label=0/40 (got={norm_str(got)!r}, expected={norm_str(exp)!r})")
        # required_evidence_label (exact string — 2 pts)
        got = a.get("required_evidence_label"); exp = o.get("required_evidence_label")
        if equal_str_ci(got, exp):
            row_passed += FIELD_WEIGHTS["required_evidence_label"]
            details.append(f"required_evidence_label=2/2")
        else:
            details.append(f"required_evidence_label=0/2 (got={norm_str(got)!r}, expected={norm_str(exp)!r})")

        total_passed += row_passed
        lines.append(f"Response {resp_id}: {row_passed}/{MAX_PER_RESPONSE}; " + "; ".join(details))

    score = total_passed / total_max if total_max > 0 else 0.0
    justification = f"Score: {score:.3f} ({total_passed}/{total_max} passed)\n\n" + "\n".join(lines)
    write_reward(score, args.reward_out, justification)


if __name__ == "__main__":
    main()
