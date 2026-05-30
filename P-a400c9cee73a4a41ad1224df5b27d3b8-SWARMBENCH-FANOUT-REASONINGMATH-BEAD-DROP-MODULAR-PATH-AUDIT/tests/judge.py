"""Executable verifier for the BEAD-DROP modular-path audit.

Deterministic, Python-stdlib only. No LLM, no network, no API key.

Pipeline:
  1. Fail-closed read of /logs/agent/output.json (any IO/JSON error -> 0.0).
  2. Structural hard-fail gates: top-level keys exact set, per_response_assessment
     is a 13-element list in alphabetical A..M order, each entry has exactly the
     three required keys, anchors list has the expected 5 named entries. Any
     violation -> reward 0.0.
  3. Exact-match fast-path: agent == oracle bit-for-bit -> reward 1.0.
  4. Otherwise the 488-point rubric is scored field-by-field by exact equality
     (integers) and set equality (failure_reasons, acceptable_solution_ids).
     Reward = passed / 488, clamped to [0, 1].

All accumulation loops iterate over ORACLE keys (dedup-safe): an agent cannot
earn extra points by repeating a correct entry.
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Any

REQUIRED_TOP_LEVEL_KEYS = {
    "final_residue_mod_1000",
    "intermediate_residues",
    "gold_path_count_decomposition",
    "small_case_anchor_results",
    "acceptable_solution_ids",
    "per_response_assessment",
}

REQUIRED_INTERMEDIATE_KEYS = {"mod_8", "mod_125"}

REQUIRED_GOLD_DECOMP_KEYS = {
    "total_steps", "right_moves", "left_moves", "binomial_n", "binomial_k",
    "v_2", "v_5", "mod_8", "mod_125",
}

REQUIRED_ANCHOR_KEYS = {
    "anchor_name", "start_x", "start_y", "right_moves", "left_moves",
    "binomial_n", "binomial_k", "exact_path_count", "residue_mod_1000",
}

EXPECTED_ANCHOR_NAMES = {
    "start_2_4_to_origin", "start_4_10_to_origin", "start_6_14_to_origin",
    "start_8_20_to_origin", "start_10_24_to_origin",
}

REQUIRED_RESPONSE_KEYS = {"response_id", "final_answer_correct", "failure_reasons"}

ALLOWED_FAILURE_CODES = {"F1", "F2", "F3", "F4", "F5"}
EXPECTED_RESPONSE_IDS = list("ABCDEFGHIJKLM")

# Point budget — Total = 488 points (sums to TOTAL_POINTS exactly).
PTS_FINAL_RESIDUE = 30
PTS_MOD_8 = 5
PTS_MOD_125 = 5
PTS_BINOMIAL_N = 5
PTS_BINOMIAL_K = 5
PTS_V2 = 5
PTS_V5 = 5
PTS_ANCHOR_EACH = 6          # x5 anchors = 30
PTS_ACCEPTABLE_IDS = 8
PTS_PER_RESPONSE = 30        # x13 responses = 390
TOTAL_POINTS = (
    PTS_FINAL_RESIDUE + PTS_MOD_8 + PTS_MOD_125 + PTS_BINOMIAL_N + PTS_BINOMIAL_K
    + PTS_V2 + PTS_V5 + PTS_ANCHOR_EACH * 5 + PTS_ACCEPTABLE_IDS
    + PTS_PER_RESPONSE * 13
)  # = 488


def _write_reward(reward_path: str, reward: float) -> None:
    os.makedirs(os.path.dirname(reward_path), exist_ok=True)
    with open(reward_path, "w", encoding="utf-8") as f:
        json.dump({"reward": float(reward)}, f)


def _write_justification(text: str) -> None:
    just_path = "/logs/agent/judge_justification.txt"
    try:
        os.makedirs(os.path.dirname(just_path), exist_ok=True)
        with open(just_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


def _structural_gate(agent: Any) -> tuple[bool, str]:
    if not isinstance(agent, dict):
        return False, "agent output is not a JSON object"
    extra = set(agent.keys()) - REQUIRED_TOP_LEVEL_KEYS
    if extra:
        return False, (
            f"forbidden extra top-level keys: {sorted(extra)}; "
            f"only {sorted(REQUIRED_TOP_LEVEL_KEYS)} are allowed"
        )
    missing = REQUIRED_TOP_LEVEL_KEYS - set(agent.keys())
    if missing:
        return False, f"missing required top-level keys: {sorted(missing)}"
    if not isinstance(agent["final_residue_mod_1000"], int) or isinstance(agent["final_residue_mod_1000"], bool):
        return False, "final_residue_mod_1000 must be an integer"
    if not (0 <= agent["final_residue_mod_1000"] <= 999):
        return False, "final_residue_mod_1000 must be in [0, 999]"

    inter = agent["intermediate_residues"]
    if not isinstance(inter, dict) or set(inter.keys()) != REQUIRED_INTERMEDIATE_KEYS:
        return False, f"intermediate_residues must have exactly the keys {sorted(REQUIRED_INTERMEDIATE_KEYS)}"
    if not isinstance(inter["mod_8"], int) or isinstance(inter["mod_8"], bool) or not (0 <= inter["mod_8"] <= 7):
        return False, "intermediate_residues.mod_8 must be an integer in [0, 7]"
    if not isinstance(inter["mod_125"], int) or isinstance(inter["mod_125"], bool) or not (0 <= inter["mod_125"] <= 124):
        return False, "intermediate_residues.mod_125 must be an integer in [0, 124]"

    gpd = agent["gold_path_count_decomposition"]
    if not isinstance(gpd, dict) or set(gpd.keys()) != REQUIRED_GOLD_DECOMP_KEYS:
        return False, f"gold_path_count_decomposition must have exactly the keys {sorted(REQUIRED_GOLD_DECOMP_KEYS)}"
    for k in REQUIRED_GOLD_DECOMP_KEYS:
        if not isinstance(gpd[k], int) or isinstance(gpd[k], bool):
            return False, f"gold_path_count_decomposition.{k} must be an integer"

    anchors = agent["small_case_anchor_results"]
    if not isinstance(anchors, list) or len(anchors) != len(EXPECTED_ANCHOR_NAMES):
        return False, f"small_case_anchor_results must be a list of exactly {len(EXPECTED_ANCHOR_NAMES)} objects"
    seen = set()
    for i, a in enumerate(anchors):
        if not isinstance(a, dict) or set(a.keys()) != REQUIRED_ANCHOR_KEYS:
            return False, f"small_case_anchor_results[{i}] must have exactly the keys {sorted(REQUIRED_ANCHOR_KEYS)}"
        if a["anchor_name"] not in EXPECTED_ANCHOR_NAMES:
            return False, f"small_case_anchor_results[{i}].anchor_name {a['anchor_name']!r} is not one of {sorted(EXPECTED_ANCHOR_NAMES)}"
        if a["anchor_name"] in seen:
            return False, f"duplicate anchor_name {a['anchor_name']!r} in small_case_anchor_results"
        seen.add(a["anchor_name"])
        for k in ("start_x", "start_y", "right_moves", "left_moves", "binomial_n", "binomial_k", "exact_path_count", "residue_mod_1000"):
            if not isinstance(a[k], int) or isinstance(a[k], bool):
                return False, f"small_case_anchor_results[{i}].{k} must be an integer"

    ids = agent["acceptable_solution_ids"]
    if not isinstance(ids, list) or not all(isinstance(x, str) for x in ids):
        return False, "acceptable_solution_ids must be a list of strings"

    pra = agent["per_response_assessment"]
    if not isinstance(pra, list):
        return False, "per_response_assessment is not a JSON array"
    if len(pra) != len(EXPECTED_RESPONSE_IDS):
        return False, f"per_response_assessment has {len(pra)} entries; expected {len(EXPECTED_RESPONSE_IDS)}"
    for i, (entry, expected_id) in enumerate(zip(pra, EXPECTED_RESPONSE_IDS)):
        if not isinstance(entry, dict):
            return False, f"per_response_assessment[{i}] is not a JSON object"
        if set(entry.keys()) != REQUIRED_RESPONSE_KEYS:
            extra_k = set(entry.keys()) - REQUIRED_RESPONSE_KEYS
            missing_k = REQUIRED_RESPONSE_KEYS - set(entry.keys())
            return False, (
                f"per_response_assessment[{i}] key mismatch: "
                f"extra={sorted(extra_k)}, missing={sorted(missing_k)}; required keys are "
                f"{sorted(REQUIRED_RESPONSE_KEYS)}"
            )
        if entry["response_id"] != expected_id:
            return False, (
                f"per_response_assessment[{i}].response_id = {entry['response_id']!r}; "
                f"expected {expected_id!r} (must be in alphabetical order A..M)"
            )
        if not isinstance(entry["final_answer_correct"], bool):
            return False, f"per_response_assessment[{i}].final_answer_correct must be boolean"
        fr = entry["failure_reasons"]
        if not isinstance(fr, list) or not all(isinstance(x, str) for x in fr):
            return False, f"per_response_assessment[{i}].failure_reasons must be a list of strings"
        for code in fr:
            if code not in ALLOWED_FAILURE_CODES:
                return False, (
                    f"per_response_assessment[{i}].failure_reasons contains forbidden "
                    f"code {code!r}; allowed: {sorted(ALLOWED_FAILURE_CODES)}"
                )
    return True, "structural gates passed"


def _score(agent: dict, oracle: dict) -> tuple[int, list[str]]:
    passed = 0
    notes: list[str] = []

    if agent["final_residue_mod_1000"] == oracle["final_residue_mod_1000"]:
        passed += PTS_FINAL_RESIDUE
    else:
        notes.append(
            f"final_residue_mod_1000: {agent['final_residue_mod_1000']} != {oracle['final_residue_mod_1000']}"
        )

    if agent["intermediate_residues"]["mod_8"] == oracle["intermediate_residues"]["mod_8"]:
        passed += PTS_MOD_8
    else:
        notes.append("intermediate_residues.mod_8 mismatch")
    if agent["intermediate_residues"]["mod_125"] == oracle["intermediate_residues"]["mod_125"]:
        passed += PTS_MOD_125
    else:
        notes.append("intermediate_residues.mod_125 mismatch")

    gpd_a = agent["gold_path_count_decomposition"]
    gpd_o = oracle["gold_path_count_decomposition"]
    for key, pts in (
        ("binomial_n", PTS_BINOMIAL_N),
        ("binomial_k", PTS_BINOMIAL_K),
        ("v_2", PTS_V2),
        ("v_5", PTS_V5),
    ):
        if gpd_a[key] == gpd_o[key]:
            passed += pts
        else:
            notes.append(f"gold_path_count_decomposition.{key}: {gpd_a[key]} != {gpd_o[key]}")

    # Anchors — iterate over ORACLE anchors (dedup-safe), match by anchor_name.
    agent_anchors = {a["anchor_name"]: a for a in agent["small_case_anchor_results"]}
    for oa in oracle["small_case_anchor_results"]:
        nm = oa["anchor_name"]
        aa = agent_anchors.get(nm)
        if aa is not None and aa["residue_mod_1000"] == oa["residue_mod_1000"]:
            passed += PTS_ANCHOR_EACH
        else:
            notes.append(f"anchor {nm}: residue mismatch")

    if set(agent["acceptable_solution_ids"]) == set(oracle["acceptable_solution_ids"]):
        passed += PTS_ACCEPTABLE_IDS
    else:
        notes.append(
            f"acceptable_solution_ids set mismatch: {sorted(set(agent['acceptable_solution_ids']))} "
            f"!= {sorted(set(oracle['acceptable_solution_ids']))}"
        )

    # Per-response — iterate over ORACLE entries (dedup-safe), match by response_id.
    agent_by_id = {r["response_id"]: r for r in agent["per_response_assessment"]}
    matched = []
    for orr in oracle["per_response_assessment"]:
        rid = orr["response_id"]
        ar = agent_by_id.get(rid)
        if (
            ar is not None
            and ar["final_answer_correct"] == orr["final_answer_correct"]
            and set(ar["failure_reasons"]) == set(orr["failure_reasons"])
        ):
            passed += PTS_PER_RESPONSE
            matched.append(rid)
        else:
            notes.append(f"response {rid}: final/failure_reasons mismatch")
    notes.append(f"responses matched exactly: {matched} ({len(matched)}/13)")

    return passed, notes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent = json.load(f)
        with open(args.oracle, "r", encoding="utf-8") as f:
            oracle = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError, ValueError) as e:
        _write_reward(args.reward_out, 0.0)
        _write_justification(f"Score: 0.0\n\nFail-closed (Stage 1 - file read): {e}")
        return

    ok, gate_reason = _structural_gate(agent)
    if not ok:
        _write_reward(args.reward_out, 0.0)
        _write_justification(f"Score: 0.0\n\nFail-closed (Stage 2 - structural gate): {gate_reason}")
        return

    if agent == oracle:
        _write_reward(args.reward_out, 1.0)
        _write_justification(
            "Score: 1.0\n\nAgent output is byte-identical to the oracle (exact-match fast-path)."
        )
        return

    try:
        passed, notes = _score(agent, oracle)
    except (KeyError, TypeError) as e:
        _write_reward(args.reward_out, 0.0)
        _write_justification(f"Score: 0.0\n\nFail-closed (Stage 4 - scoring): {type(e).__name__}: {e}")
        return

    reward = max(0.0, min(1.0, passed / TOTAL_POINTS))
    _write_reward(args.reward_out, reward)
    _write_justification(
        f"Score: {reward:.4f} ({passed}/{TOTAL_POINTS} points)\n\n" + "\n".join(notes)
    )


if __name__ == "__main__":
    main()
