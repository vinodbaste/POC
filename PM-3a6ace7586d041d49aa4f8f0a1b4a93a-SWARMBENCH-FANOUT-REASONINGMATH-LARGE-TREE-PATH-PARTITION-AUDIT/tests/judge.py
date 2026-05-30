"""
Deterministic verifier for the LARGE-TREE-PATH-PARTITION-AUDIT task.

Grading is strict and fail-closed:
  * correct_answer:                 +6 points  (exact integer equality on the
                                     N=44, K=22 count modulo 997)
  * small_case_anchor_results:      +2 points / anchor (exact integer
                                     equality), summed over 5 anchors = 10
                                     points; the agent must independently
                                     derive each anchor as part of the
                                     mathematical-derivation graded score.
  * acceptable_solution_ids:        +2 points  (unordered set equality)
  * per_response_assessment:        +30 points / response, all-or-nothing on
                                     six sub-fields, summed over 11 responses
                                     (A..K) = 330 points
  * total = 348 ; reward = passed / total in [0, 1]

A per-response audit gets its 30 points iff EVERY one of the following holds:

  1. response_id matches the oracle for that slot (exact string equality).
  2. final_answer_correct matches the oracle for that slot (exact bool).
  3. failure_reasons matches the oracle as an unordered set, with all entries
     drawn from the four allowed codes, no extras and no omissions.
  4. primary_failure_evidence is a string of >= 60 characters (length only,
     content is not graded by the deterministic judge - the agent's
     trajectory and the per-response oracle reasoning are how the writer
     audits content).
  5. alternative_codes_considered is a list of >= 2 entries, each entry is
     an object with keys "code" (one of the four allowed codes, none of
     which appears in that audit's failure_reasons) and "reason_excluded"
     (a string of >= 30 characters); codes within the list are pairwise
     distinct. The minimum-length on reason_excluded was raised from 20
     to 30 chars to suppress hasty single-line "not applicable" entries.
  6. error_category matches the oracle for that slot (exact string equality,
     drawn from the allowed error-category vocabulary).
  7. anchor_verification_summary is a string of >= 100 characters (length
     only) recording the auditor's independent expansion of the response's
     stated counting method on at least one of the five small-tree anchors
     (P_3, P_4, P_5, S_3, S_4) at K=2 — or, when the response commits to
     no method (per R4/R6), an explicit statement of that observation.
     The deterministic verifier checks length only; the content is the
     auditor's responsibility and is documented per-response in the oracle.

Two earlier sub-fields are still emitted by the agent and stored in the
oracle for documentation but NO LONGER checked by this deterministic
verifier:

  * `length_constraint_handling` — a four-value enum that records how the
    response handled the K = 22 constraint; the boundary between
    "correctly_applied" and "dropped" on truncated-but-set-up responses
    turned out to be too ambiguous to grade strictly.

  * `dominant_error_location` — a four-value enum that pinpoints WHERE
    the defect lives (method-commitment vs framework-implementation vs
    no-specific vs none); the "framework_implementation" label was
    semantically too close to "the response set up a framework" for
    sub-agents reading per-response prose, which caused per-response
    sub-agents to back-derive `failure_reasons` and `error_category`
    from their location label and disagree with otherwise-correct
    classifications. The field is kept in the schema for downstream
    analysis but does not contribute to per-audit pass/fail.

Any deviation, including missing fields, wrong types, malformed JSON,
or extra/missing audits, zeros the affected slot. Missing or unreadable
agent output yields reward 0.0 and writes a justification file.
"""

import argparse
import json
import os
from typing import Any, Dict, List, Tuple

ALLOWED_FAILURE_CODES = {
    "wrong_formula",
    "arithmetic_error",
    "invalid_or_incomplete_justification",
    "final_answer_error",
}
ALLOWED_ERROR_CATEGORIES = {
    "wrong_method",
    "arithmetic_slip",
    "incomplete_or_truncated",
    "no_method_committed",
    "correct",
}
ALLOWED_LENGTH_HANDLING = {
    "correctly_applied",
    "dropped",
    "reinterpreted",
    "no_method",
}
ALLOWED_DOMINANT_ERROR_LOCATIONS = {
    "method_commitment",
    "framework_implementation",
    "no_specific_error_in_method",
    "none",
}
EXPECTED_RESPONSE_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
EXPECTED_ANCHOR_KEYS = ("P3_K2", "P4_K2", "P5_K2", "S3_K2", "S4_K2")
PRIMARY_EVIDENCE_MIN_LEN = 60
REASON_EXCLUDED_MIN_LEN = 30
ANCHOR_VERIFICATION_SUMMARY_MIN_LEN = 100
MIN_ALT_CODES = 2

POINTS_CORRECT_ANSWER = 6
POINTS_PER_ANCHOR = 2
POINTS_ACCEPTABLE_SOLUTION_IDS = 2
POINTS_PER_AUDIT = 30
TOTAL_POINTS = (
    POINTS_CORRECT_ANSWER
    + POINTS_PER_ANCHOR * len(EXPECTED_ANCHOR_KEYS)
    + POINTS_ACCEPTABLE_SOLUTION_IDS
    + POINTS_PER_AUDIT * len(EXPECTED_RESPONSE_LETTERS)
)


def _write_reward(reward_out: str, reward: float) -> None:
    os.makedirs(os.path.dirname(reward_out) or ".", exist_ok=True)
    with open(reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": float(reward)}, f)


def _write_justification(text: str) -> None:
    try:
        os.makedirs("/logs/agent", exist_ok=True)
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


def _check_audit(
    agent_audit: Any, oracle_audit: Dict[str, Any]
) -> Tuple[bool, List[str]]:
    """Return (passed, reasons-on-failure)."""
    reasons: List[str] = []

    if not isinstance(agent_audit, dict):
        return False, ["audit is not a JSON object"]

    expected_response_id = oracle_audit["response_id"]
    if agent_audit.get("response_id") != expected_response_id:
        reasons.append(
            f"response_id mismatch: got {agent_audit.get('response_id')!r}, "
            f"expected {expected_response_id!r}"
        )

    expected_correct = bool(oracle_audit["final_answer_correct"])
    if agent_audit.get("final_answer_correct") is not expected_correct:
        reasons.append(
            f"final_answer_correct mismatch: got "
            f"{agent_audit.get('final_answer_correct')!r}, expected {expected_correct!r}"
        )

    agent_fr = agent_audit.get("failure_reasons")
    if not isinstance(agent_fr, list) or not all(isinstance(x, str) for x in agent_fr):
        reasons.append("failure_reasons is not a list of strings")
        agent_fr_set = None
    else:
        if any(x not in ALLOWED_FAILURE_CODES for x in agent_fr):
            reasons.append(
                f"failure_reasons contains a code outside the allowed vocabulary"
            )
            agent_fr_set = None
        elif len(set(agent_fr)) != len(agent_fr):
            reasons.append("failure_reasons contains a duplicate code")
            agent_fr_set = None
        else:
            agent_fr_set = set(agent_fr)

    oracle_fr_set = set(oracle_audit["failure_reasons"])
    if agent_fr_set is not None and agent_fr_set != oracle_fr_set:
        missing = oracle_fr_set - agent_fr_set
        extra = agent_fr_set - oracle_fr_set
        reasons.append(
            f"failure_reasons set mismatch: missing={sorted(missing)}, "
            f"extra={sorted(extra)}"
        )

    pfe = agent_audit.get("primary_failure_evidence")
    if not isinstance(pfe, str):
        reasons.append("primary_failure_evidence is missing or not a string")
    elif len(pfe.strip()) < PRIMARY_EVIDENCE_MIN_LEN:
        reasons.append(
            f"primary_failure_evidence too short: len={len(pfe.strip())} (require >= {PRIMARY_EVIDENCE_MIN_LEN})"
        )

    expected_error_category = oracle_audit.get("error_category")
    agent_error_category = agent_audit.get("error_category")
    if not isinstance(agent_error_category, str):
        reasons.append("error_category is missing or not a string")
    elif agent_error_category not in ALLOWED_ERROR_CATEGORIES:
        reasons.append(
            f"error_category {agent_error_category!r} is not in the allowed vocabulary"
        )
    elif agent_error_category != expected_error_category:
        reasons.append(
            f"error_category mismatch: got {agent_error_category!r}, expected {expected_error_category!r}"
        )

    avs = agent_audit.get("anchor_verification_summary")
    if not isinstance(avs, str):
        reasons.append("anchor_verification_summary is missing or not a string")
    elif len(avs.strip()) < ANCHOR_VERIFICATION_SUMMARY_MIN_LEN:
        reasons.append(
            f"anchor_verification_summary too short: len={len(avs.strip())} "
            f"(require >= {ANCHOR_VERIFICATION_SUMMARY_MIN_LEN})"
        )

    # NOTE: dominant_error_location and length_constraint_handling are
    # intentionally NOT graded here; see docstring above. Both fields are
    # preserved in agent output and oracle for documentation but no longer
    # contribute to the per-audit pass/fail.

    alt_list = agent_audit.get("alternative_codes_considered")
    if not isinstance(alt_list, list):
        reasons.append("alternative_codes_considered is missing or not a list")
    elif len(alt_list) < MIN_ALT_CODES:
        reasons.append(
            f"alternative_codes_considered too short: len={len(alt_list)} (require >= {MIN_ALT_CODES})"
        )
    else:
        seen_codes: List[str] = []
        for idx, entry in enumerate(alt_list):
            if not isinstance(entry, dict):
                reasons.append(f"alternative_codes_considered[{idx}] is not an object")
                continue
            code = entry.get("code")
            reason_excluded = entry.get("reason_excluded")
            if not isinstance(code, str) or code not in ALLOWED_FAILURE_CODES:
                reasons.append(
                    f"alternative_codes_considered[{idx}].code invalid: {code!r}"
                )
                continue
            if agent_fr_set is not None and code in agent_fr_set:
                reasons.append(
                    f"alternative_codes_considered[{idx}].code {code!r} already appears in failure_reasons"
                )
            if code in seen_codes:
                reasons.append(
                    f"alternative_codes_considered duplicates code {code!r}"
                )
            seen_codes.append(code)
            if not isinstance(reason_excluded, str):
                reasons.append(
                    f"alternative_codes_considered[{idx}].reason_excluded is not a string"
                )
            elif len(reason_excluded.strip()) < REASON_EXCLUDED_MIN_LEN:
                reasons.append(
                    f"alternative_codes_considered[{idx}].reason_excluded too short: "
                    f"len={len(reason_excluded.strip())} (require >= {REASON_EXCLUDED_MIN_LEN})"
                )

    return (len(reasons) == 0), reasons


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()

    notes: List[str] = []
    passed = 0

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent_output = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        _write_reward(args.reward_out, 0.0)
        _write_justification(
            f"Score: 0.0\n\nAgent output missing or invalid: {e}"
        )
        return

    try:
        with open(args.oracle, "r", encoding="utf-8") as f:
            oracle = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        _write_reward(args.reward_out, 0.0)
        _write_justification(
            f"Score: 0.0\n\nOracle missing or invalid: {e}"
        )
        return

    if not isinstance(agent_output, dict):
        _write_reward(args.reward_out, 0.0)
        _write_justification("Score: 0.0\n\nAgent output is not a JSON object.")
        return

    expected_correct_answer = oracle.get("correct_answer")
    agent_correct_answer = agent_output.get("correct_answer")
    if (
        isinstance(agent_correct_answer, int)
        and not isinstance(agent_correct_answer, bool)
        and agent_correct_answer == expected_correct_answer
    ):
        passed += POINTS_CORRECT_ANSWER
        notes.append(f"correct_answer: PASS (got {agent_correct_answer})")
    else:
        notes.append(
            f"correct_answer: FAIL (got {agent_correct_answer!r}, expected {expected_correct_answer!r})"
        )

    expected_anchors = oracle.get("small_case_anchor_results", {}) or {}
    agent_anchors = agent_output.get("small_case_anchor_results", {}) or {}
    if not isinstance(agent_anchors, dict):
        notes.append(
            f"small_case_anchor_results: FAIL (not an object, got {type(agent_anchors).__name__})"
        )
        agent_anchors = {}
    for anchor_key in EXPECTED_ANCHOR_KEYS:
        expected_value = expected_anchors.get(anchor_key)
        agent_value = agent_anchors.get(anchor_key)
        if (
            isinstance(agent_value, int)
            and not isinstance(agent_value, bool)
            and agent_value == expected_value
        ):
            passed += POINTS_PER_ANCHOR
            notes.append(f"small_case_anchor_results.{anchor_key}: PASS")
        else:
            notes.append(
                f"small_case_anchor_results.{anchor_key}: FAIL "
                f"(got {agent_value!r}, expected {expected_value!r})"
            )

    expected_ids = oracle.get("acceptable_solution_ids", [])
    agent_ids = agent_output.get("acceptable_solution_ids", [])
    if (
        isinstance(agent_ids, list)
        and all(isinstance(x, str) for x in agent_ids)
        and set(agent_ids) == set(expected_ids)
        and len(agent_ids) == len(set(agent_ids))
    ):
        passed += POINTS_ACCEPTABLE_SOLUTION_IDS
        notes.append("acceptable_solution_ids: PASS")
    else:
        notes.append(
            f"acceptable_solution_ids: FAIL (got {agent_ids!r}, expected {expected_ids!r})"
        )

    oracle_audits = oracle.get("per_response_assessment", [])
    agent_audits = agent_output.get("per_response_assessment", [])
    if not isinstance(agent_audits, list):
        notes.append("per_response_assessment: FAIL (not a list)")
        agent_audits = []

    oracle_by_id = {a["response_id"]: a for a in oracle_audits}
    agent_by_id: Dict[str, Any] = {}
    if isinstance(agent_audits, list):
        for a in agent_audits:
            if isinstance(a, dict) and isinstance(a.get("response_id"), str):
                agent_by_id.setdefault(a["response_id"], a)

    for letter in EXPECTED_RESPONSE_LETTERS:
        if letter not in oracle_by_id:
            notes.append(
                f"audit {letter}: SKIP (oracle slot not yet populated; treated as 0)"
            )
            continue
        oracle_audit = oracle_by_id[letter]
        agent_audit = agent_by_id.get(letter)
        if agent_audit is None:
            notes.append(f"audit {letter}: FAIL (missing in agent output)")
            continue
        ok, reasons = _check_audit(agent_audit, oracle_audit)
        if ok:
            passed += POINTS_PER_AUDIT
            notes.append(f"audit {letter}: PASS")
        else:
            notes.append(f"audit {letter}: FAIL ({'; '.join(reasons)})")

    reward = passed / TOTAL_POINTS if TOTAL_POINTS > 0 else 0.0
    reward = max(0.0, min(1.0, reward))
    _write_reward(args.reward_out, reward)

    summary = (
        f"Score: {reward:.4f} ({passed}/{TOTAL_POINTS} points)\n\n"
        + "\n".join(notes)
    )
    _write_justification(summary)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # fail-closed
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument("--reward-out", required=False, default="/logs/verifier/reward.json")
            args, _ = parser.parse_known_args()
            _write_reward(args.reward_out, 0.0)
            _write_justification(f"Score: 0.0\n\nJudge crashed: {type(e).__name__}: {e}")
        except Exception:
            pass
