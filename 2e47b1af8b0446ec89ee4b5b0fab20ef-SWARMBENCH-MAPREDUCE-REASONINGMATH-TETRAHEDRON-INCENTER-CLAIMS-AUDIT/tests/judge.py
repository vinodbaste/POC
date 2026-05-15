"""Deterministic verifier for the Tetrahedron Incenter Claims Audit task.

No LLM is called. The script compares the agent's /logs/agent/output.json against
the gold /tests/oracle.json field by field using exact-match and set-IoU rules,
then writes a reward in [0.0, 1.0] to /logs/verifier/reward.json.

Scoring total = 100 points:
  - 35 per-solution (5 pts each * 7 solutions: claimed_set, verdict, 4 booleans, repairability)
  - 15 fatal-error    (3 pts each for the 5 non-correct solutions: error_type, explanation non-empty)
  -  4 correct-null  (2 pts each for the 2 correct solutions A,D: first_fatal_error must be null)
  - 14 failure_labels coverage (2 pts per solution * 7)
  -  7 domain_specific_labels coverage (1 pt per solution * 7)
  - 25 cross_solution_summary breakdown described below.

Schema-violation gating: missing top-level keys, non-list solution_audits, or
non-7-entry solution_audits all cap the reward at 0.5 (multiply per-solution and
fatal-error blocks by 0.5).

License: MIT (this file ships with the task; safe to redistribute).
"""

import argparse
import json
import os
from typing import Any, Dict, List, Set


# ----- helpers -----------------------------------------------------------------


def normalize_letter_list(value: Any) -> List[str]:
    """Lowercase, strip whitespace, keep only single letters a-h, alphabetical."""
    if not isinstance(value, list):
        return []
    out = []
    for v in value:
        if not isinstance(v, str):
            continue
        s = v.strip().lower()
        if len(s) == 1 and s in "abcdefgh":
            out.append(s)
    return sorted(set(out))


def normalize_solution_id_list(value: Any) -> List[str]:
    """Uppercase, strip whitespace, keep only single letters A-G, alphabetical."""
    if not isinstance(value, list):
        return []
    out = []
    for v in value:
        if not isinstance(v, str):
            continue
        s = v.strip().upper()
        if len(s) == 1 and s in "ABCDEFG":
            out.append(s)
    return sorted(set(out))


def normalize_groups_of_solution_ids(value: Any) -> Set[frozenset]:
    """For list-of-lists fields. Each inner list becomes a frozenset of normalized
    solution IDs; outer becomes a set of those frozensets so order is irrelevant.
    Singletons are dropped (a group of size 1 is meaningless for "sharing")."""
    if not isinstance(value, list):
        return set()
    out: Set[frozenset] = set()
    for group in value:
        if not isinstance(group, list):
            continue
        norm = frozenset(normalize_solution_id_list(group))
        if len(norm) >= 2:
            out.add(norm)
    return out


def set_iou(a: Set[Any], b: Set[Any]) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    if not union:
        return 1.0
    return len(a & b) / len(union)


# Semantic equivalence classes for error_type. Two labels in the SAME class
# count as equivalent for fatal_error scoring. Labels not in any class only
# match themselves.
ERROR_TYPE_EQUIV_CLASSES = [
    # B/G/E-style "rejected true claim without construction" cluster
    frozenset({
        "underjustified_step",
        "invalid_logical_step",
        "incomplete_proof",
        "missing_case",
        "ignored_acuteness_condition",
    }),
    # C/F-style "invoked false universal claim" cluster
    frozenset({
        "false_math_claim",
        "wrong_theorem_application",
        "correct_gtfa_invalid_proof",
    }),
]


def error_types_equivalent(a: str, b: str) -> bool:
    """True iff a and b are the same string OR fall in the same equivalence class."""
    a = (a or "").strip().lower()
    b = (b or "").strip().lower()
    if a == b:
        return True
    for cls in ERROR_TYPE_EQUIV_CLASSES:
        if a in cls and b in cls:
            return True
    return False


def best_group_iou(agent_groups: Set[frozenset], oracle_group: frozenset) -> float:
    """For one oracle group, find the max set-IoU against any agent group."""
    best = 0.0
    for ag in agent_groups:
        score = set_iou(set(ag), set(oracle_group))
        if score > best:
            best = score
    return best


# ----- per-section scoring -----------------------------------------------------


def score_per_solution_entry(agent: Dict[str, Any], oracle: Dict[str, Any]) -> float:
    """Return up to 5.0 points for one solution audit entry."""
    pts = 0.0
    if normalize_letter_list(agent.get("claimed_set")) == normalize_letter_list(oracle.get("claimed_set")):
        pts += 1.0
    if str(agent.get("verdict", "")).strip().lower() == str(oracle.get("verdict", "")).strip().lower():
        pts += 1.0
    if bool(agent.get("final_answer_correct")) == bool(oracle.get("final_answer_correct")):
        pts += 0.5
    if bool(agent.get("logical_chain_valid")) == bool(oracle.get("logical_chain_valid")):
        pts += 0.5
    if bool(agent.get("proof_complete")) == bool(oracle.get("proof_complete")):
        pts += 0.5
    if bool(agent.get("contains_wrong_math_claim")) == bool(oracle.get("contains_wrong_math_claim")):
        pts += 0.5
    if str(agent.get("repairability", "")).strip().lower() == str(oracle.get("repairability", "")).strip().lower():
        pts += 1.0
    return pts


def score_fatal_error_entry(agent: Dict[str, Any], oracle: Dict[str, Any]) -> float:
    """Per non-correct solution: up to 3 pts.
    - 2 pts: error_type match (exact OR same semantic equivalence class)
    - 1 pt:  non-empty explanation (>= 20 chars)
    Oracle verdict drives the rule."""
    oracle_ffe = oracle.get("first_fatal_error")
    if oracle_ffe is None:
        return 0.0  # this entry is scored under correct-null block instead
    pts = 0.0
    agent_ffe = agent.get("first_fatal_error")
    if not isinstance(agent_ffe, dict):
        return 0.0
    if error_types_equivalent(agent_ffe.get("error_type", ""), oracle_ffe.get("error_type", "")):
        pts += 2.0
    explanation = str(agent_ffe.get("explanation", "")).strip()
    if len(explanation) >= 20:
        pts += 1.0
    return pts


def score_correct_null_entry(agent: Dict[str, Any], oracle: Dict[str, Any]) -> float:
    """Per correct solution: up to 2 pts. first_fatal_error must be null AND
    repairability must be 'n/a'."""
    if oracle.get("first_fatal_error") is not None:
        return 0.0
    pts = 0.0
    if agent.get("first_fatal_error") is None:
        pts += 1.0
    if str(agent.get("repairability", "")).strip().lower() == "n/a":
        pts += 1.0
    return pts


def score_failure_labels(agent: Dict[str, Any], oracle: Dict[str, Any], max_pts: float) -> float:
    """Set-IoU on failure_labels."""
    a = {str(s).strip().lower() for s in (agent.get("failure_labels") or []) if isinstance(s, str)}
    o = {str(s).strip().lower() for s in (oracle.get("failure_labels") or []) if isinstance(s, str)}
    return max_pts * set_iou(a, o)


def score_domain_labels(agent: Dict[str, Any], oracle: Dict[str, Any], max_pts: float) -> float:
    """Set-IoU on domain_specific_labels."""
    a = {str(s).strip().lower() for s in (agent.get("domain_specific_labels") or []) if isinstance(s, str)}
    o = {str(s).strip().lower() for s in (oracle.get("domain_specific_labels") or []) if isinstance(s, str)}
    return max_pts * set_iou(a, o)


# ----- cross-summary scoring ---------------------------------------------------


def score_cross_summary(agent_cs: Dict[str, Any], oracle_cs: Dict[str, Any]) -> float:
    """Return up to 25.0 points from the cross_solution_summary block."""
    pts = 0.0

    # best_solution_id (3 pts, exact match)
    if str(agent_cs.get("best_solution_id", "")).strip().upper() == str(oracle_cs.get("best_solution_id", "")).strip().upper():
        pts += 3.0

    # solutions_with_correct_gtfa_but_invalid_proof (2 pts, exact set match)
    if set(normalize_solution_id_list(agent_cs.get("solutions_with_correct_gtfa_but_invalid_proof"))) == \
       set(normalize_solution_id_list(oracle_cs.get("solutions_with_correct_gtfa_but_invalid_proof"))):
        pts += 2.0

    # solutions_with_valid_core_idea (2 pts, exact set match)
    if set(normalize_solution_id_list(agent_cs.get("solutions_with_valid_core_idea"))) == \
       set(normalize_solution_id_list(oracle_cs.get("solutions_with_valid_core_idea"))):
        pts += 2.0

    # NEW: candidates_sharing_same_fatal_error_type (5 pts, set of frozensets)
    agent_groups = normalize_groups_of_solution_ids(agent_cs.get("candidates_sharing_same_fatal_error_type"))
    oracle_groups = normalize_groups_of_solution_ids(oracle_cs.get("candidates_sharing_same_fatal_error_type"))
    if oracle_groups:
        per_group = 5.0 / max(len(oracle_groups), 1)
        for og in oracle_groups:
            if og in agent_groups:
                pts += per_group

    # NEW: candidates_implicitly_using_same_false_lemma (5 pts, set of frozensets)
    agent_lemma_groups = normalize_groups_of_solution_ids(agent_cs.get("candidates_implicitly_using_same_false_lemma"))
    oracle_lemma_groups = normalize_groups_of_solution_ids(oracle_cs.get("candidates_implicitly_using_same_false_lemma"))
    if oracle_lemma_groups:
        per_group = 5.0 / max(len(oracle_lemma_groups), 1)
        for og in oracle_lemma_groups:
            if og in agent_lemma_groups:
                pts += per_group

    # common_failure_modes (5 pts, keyword-substring match per oracle mode)
    # Each canonical mode is detected by ALL of its required keywords appearing in
    # any single agent common_failure_modes string. Robust to paraphrasing.
    canonical_modes = [
        ["unconstructed", "counterexample"],          # mode 1
        ["insphere", "incenter"],                      # mode 2 (false insphere/face-incenter claim)
        ["volume", "distance"],                        # mode 3 (vol-to-distance translation)
        ["acute"],                                     # mode 4 (acuteness condition unused)
    ]
    agent_modes = [str(s).lower() for s in (agent_cs.get("common_failure_modes") or []) if isinstance(s, str)]
    joined = " ".join(agent_modes)
    captured = 0
    for keywords in canonical_modes:
        if all(kw in joined for kw in keywords):
            captured += 1
    pts += 5.0 * (captured / len(canonical_modes))

    # gold_final_answer (2 pts, exact normalized match)
    def norm_set_string(s: str) -> str:
        if not isinstance(s, str):
            return ""
        s = s.strip().lower().replace(" ", "").replace("{", "").replace("}", "")
        parts = sorted(p for p in s.split(",") if p in "abcdefgh")
        return "{" + ", ".join(parts) + "}"

    if norm_set_string(agent_cs.get("__placeholder_for_gold_final_answer__", "")) or True:
        pass  # gold_final_answer is at the top level, not inside cross_solution_summary

    # problem_id is scored at the outer level, not here

    return pts


# ----- main --------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()

    justification_path = "/logs/agent/judge_justification.txt"
    os.makedirs(os.path.dirname(justification_path), exist_ok=True)

    # Load agent output
    try:
        with open(args.agent_output, encoding="utf-8") as f:
            agent_output = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        with open(args.reward_out, "w") as f:
            json.dump({"reward": 0.0}, f)
        with open(justification_path, "w", encoding="utf-8") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid JSON: {e}")
        return

    # Load oracle
    with open(args.oracle, encoding="utf-8") as f:
        oracle = json.load(f)

    # Exact-match shortcut for oracle agent
    if agent_output == oracle:
        with open(args.reward_out, "w") as f:
            json.dump({"reward": 1.0}, f)
        with open(justification_path, "w", encoding="utf-8") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    # Top-level structure check (gating)
    required_top_keys = {"problem_id", "gold_final_answer", "solution_audits", "cross_solution_summary"}
    missing = required_top_keys - set(agent_output.keys() if isinstance(agent_output, dict) else [])
    audits = agent_output.get("solution_audits") if isinstance(agent_output, dict) else None
    audits_ok = isinstance(audits, list) and len(audits) == 7
    structure_multiplier = 0.5 if (missing or not audits_ok) else 1.0

    oracle_audits = oracle["solution_audits"]
    oracle_by_id = {a["solution_id"]: a for a in oracle_audits}
    agent_by_id = {
        str(a.get("solution_id", "")).strip().upper(): a
        for a in (audits or [])
        if isinstance(a, dict)
    }

    # 35 pts: per-solution (7 entries * 5)
    per_solution_pts = 0.0
    per_solution_breakdown = []
    for sid in "ABCDEFG":
        oracle_entry = oracle_by_id.get(sid)
        agent_entry = agent_by_id.get(sid, {})
        score = score_per_solution_entry(agent_entry, oracle_entry) if oracle_entry else 0.0
        per_solution_pts += score
        per_solution_breakdown.append(f"{sid}={score:.1f}")
    per_solution_pts *= structure_multiplier

    # 15 pts: fatal-error for the 5 non-correct solutions (B, C, E, F, G)
    fatal_pts = 0.0
    fatal_breakdown = []
    for sid in "BCEFG":
        oracle_entry = oracle_by_id.get(sid)
        agent_entry = agent_by_id.get(sid, {})
        score = score_fatal_error_entry(agent_entry, oracle_entry) if oracle_entry else 0.0
        fatal_pts += score
        fatal_breakdown.append(f"{sid}={score:.1f}")
    fatal_pts *= structure_multiplier

    # 4 pts: correct-null for A and D
    correct_null_pts = 0.0
    for sid in "AD":
        oracle_entry = oracle_by_id.get(sid)
        agent_entry = agent_by_id.get(sid, {})
        correct_null_pts += score_correct_null_entry(agent_entry, oracle_entry) if oracle_entry else 0.0

    # 14 pts: failure_labels coverage (2 pts per solution * 7)
    failure_labels_pts = 0.0
    for sid in "ABCDEFG":
        oracle_entry = oracle_by_id.get(sid, {})
        agent_entry = agent_by_id.get(sid, {})
        failure_labels_pts += score_failure_labels(agent_entry, oracle_entry, max_pts=2.0)

    # 7 pts: domain_specific_labels coverage (1 pt per solution * 7)
    domain_labels_pts = 0.0
    for sid in "ABCDEFG":
        oracle_entry = oracle_by_id.get(sid, {})
        agent_entry = agent_by_id.get(sid, {})
        domain_labels_pts += score_domain_labels(agent_entry, oracle_entry, max_pts=1.0)

    # 25 pts: cross_solution_summary (excluding gold_final_answer and problem_id, scored at top level)
    agent_cs = agent_output.get("cross_solution_summary") if isinstance(agent_output, dict) else None
    oracle_cs = oracle.get("cross_solution_summary", {})
    cross_pts = score_cross_summary(agent_cs or {}, oracle_cs)

    # Top-level extras (gold_final_answer and problem_id) — folded into cross-summary block
    # gold_final_answer (2 pts)
    gold_pts = 0.0
    def norm_set_string(s: str) -> str:
        if not isinstance(s, str):
            return ""
        t = s.strip().lower().replace(" ", "").replace("{", "").replace("}", "")
        parts = sorted(p for p in t.split(",") if p in "abcdefgh")
        return "{" + ", ".join(parts) + "}"
    if norm_set_string(agent_output.get("gold_final_answer") if isinstance(agent_output, dict) else "") == \
       norm_set_string(oracle.get("gold_final_answer", "")):
        gold_pts += 2.0
    # problem_id (1 pt)
    pid_pts = 0.0
    if str(agent_output.get("problem_id") if isinstance(agent_output, dict) else "").strip().lower() == \
       str(oracle.get("problem_id", "")).strip().lower():
        pid_pts += 1.0
    # absorb into the 25 cap by attributing to a free "header" allotment
    # The cross_pts above is capped at 25 from the cross_solution_summary subscores.
    # Add gold_pts and pid_pts on top, but cap the entire cross+header block at 25.
    header_block = min(cross_pts + gold_pts + pid_pts, 25.0)
    # The cap is hit because we redistribute: cross subscores sum to 22 max
    # (3 best_id + 2 + 2 + 5 + 5 + 5 = 22), plus 2 gold + 1 pid = 25 total. No overflow.

    total = per_solution_pts + fatal_pts + correct_null_pts + failure_labels_pts + domain_labels_pts + header_block
    total_rounded = round(total, 2)
    score = max(0.0, min(1.0, total_rounded / 100.0))

    with open(args.reward_out, "w") as f:
        json.dump({"reward": score}, f)

    breakdown = (
        f"Score: {score:.4f}  ({total_rounded:.2f}/100)\n\n"
        f"  per_solution (max 35):       {per_solution_pts:.2f}  [{', '.join(per_solution_breakdown)}]\n"
        f"  fatal_error  (max 15):       {fatal_pts:.2f}  [{', '.join(fatal_breakdown)}]\n"
        f"  correct_null (max 4):        {correct_null_pts:.2f}\n"
        f"  failure_labels (max 14):     {failure_labels_pts:.2f}\n"
        f"  domain_labels  (max 7):      {domain_labels_pts:.2f}\n"
        f"  cross_summary+header (max 25): {header_block:.2f}\n"
    )
    if structure_multiplier < 1.0:
        breakdown += (
            f"\n  STRUCTURE PENALTY APPLIED (x0.5 on per_solution and fatal_error):\n"
            f"    missing top-level keys: {sorted(missing)}\n"
            f"    audits_ok (exactly 7 entries): {audits_ok}\n"
        )
    with open(justification_path, "w", encoding="utf-8") as f:
        f.write(breakdown)


if __name__ == "__main__":
    main()
