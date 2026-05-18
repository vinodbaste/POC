import argparse
import json
import os


ALL_FAILURE_CODES = [
    "wrong_move_set_including_zero",
    "wrong_move_set_excluding_one",
    "incorrect_fibonacci_enumeration",
    "confused_pn_convention",
    "base_case_set_to_n",
    "treats_game_as_misere",
    "applies_nim_sprague_grundy_directly_wrong",
    "arithmetic_recursion_error",
    "claims_periodic_pattern_falsely",
    "arbitrary_pattern_heuristic",
    "truncated_or_short_string",
    "non_terminating_or_no_final_answer",
]

PRIMARY_CODES_INCLUDING_NONE = ALL_FAILURE_CODES + ["NONE"]

GOLD_FINAL_ANSWER_WEIGHT = 4
ACCEPTABLE_SOLUTION_IDS_WEIGHT = 2

FINAL_ANSWER_CORRECT_WEIGHT = 5
FAILURE_REASONS_SET_WEIGHT = 30
PRIMARY_FAILURE_CODE_WEIGHT = 25
PRIMARY_FAILURE_CODE_EVIDENCE_WEIGHT = 8
ALTERNATIVE_CODES_CONSIDERED_WEIGHT = 8
PER_CODE_EVIDENCE_WEIGHT = 5

CODE_APPLICATION_TABLE_PER_KEY_WEIGHT = 70
RESPONSE_COUNT_PER_CODE_KEY_WEIGHT = 15
CROSS_RESPONSE_OBSERVATIONS_WEIGHT = 30

EVIDENCE_MIN_CHARS = 20
PRIMARY_EVIDENCE_MIN_CHARS = 50
CROSS_OBS_MIN_CHARS = 300
ALT_CODES_MIN_COUNT = 2


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def by_id(obj):
    return {item.get("response_id"): item for item in obj.get("per_response_assessment", [])}


def score_top_level_facts(agent, oracle):
    earned = 0
    total = 0
    lines = []

    total += GOLD_FINAL_ANSWER_WEIGHT
    expected_gold = oracle.get("gold_final_answer")
    actual_gold = agent.get("gold_final_answer")
    if actual_gold == expected_gold:
        earned += GOLD_FINAL_ANSWER_WEIGHT
        lines.append(f"gold_final_answer: {GOLD_FINAL_ANSWER_WEIGHT}/{GOLD_FINAL_ANSWER_WEIGHT}")
    else:
        diff_idx = next((i for i in range(min(len(str(expected_gold)), len(str(actual_gold) or ""))) if str(expected_gold)[i] != str(actual_gold or "")[i]), None)
        lines.append(
            f"gold_final_answer: 0/{GOLD_FINAL_ANSWER_WEIGHT}; first divergence at index {diff_idx}"
        )

    total += ACCEPTABLE_SOLUTION_IDS_WEIGHT
    expected_acc = sorted(oracle.get("acceptable_solution_ids", []))
    actual_acc = agent.get("acceptable_solution_ids", [])
    if isinstance(actual_acc, list) and sorted(actual_acc) == expected_acc:
        earned += ACCEPTABLE_SOLUTION_IDS_WEIGHT
        lines.append(f"acceptable_solution_ids: {ACCEPTABLE_SOLUTION_IDS_WEIGHT}/{ACCEPTABLE_SOLUTION_IDS_WEIGHT}")
    else:
        lines.append(
            f"acceptable_solution_ids: 0/{ACCEPTABLE_SOLUTION_IDS_WEIGHT}; expected {expected_acc}, got {actual_acc}"
        )

    return earned, total, lines


def score_per_response(rid, agent_obj, oracle_obj):
    earned = 0
    total = 0
    issues = []

    total += FINAL_ANSWER_CORRECT_WEIGHT
    if isinstance(agent_obj, dict) and agent_obj.get("final_answer_correct") == oracle_obj.get("final_answer_correct"):
        earned += FINAL_ANSWER_CORRECT_WEIGHT
    else:
        issues.append("final_answer_correct: mismatch")

    total += FAILURE_REASONS_SET_WEIGHT
    expected_reasons = set(oracle_obj.get("failure_reasons", []) or [])
    actual_reasons_raw = agent_obj.get("failure_reasons", []) if isinstance(agent_obj, dict) else []
    actual_reasons = set(actual_reasons_raw) if isinstance(actual_reasons_raw, list) else set()
    if actual_reasons == expected_reasons:
        earned += FAILURE_REASONS_SET_WEIGHT
    else:
        missing = expected_reasons - actual_reasons
        extra = actual_reasons - expected_reasons
        issues.append(f"failure_reasons set mismatch (missing={sorted(missing)}, extra={sorted(extra)})")

    total += PRIMARY_FAILURE_CODE_WEIGHT
    expected_primary = oracle_obj.get("primary_failure_code")
    actual_primary = agent_obj.get("primary_failure_code") if isinstance(agent_obj, dict) else None
    if actual_primary == expected_primary:
        earned += PRIMARY_FAILURE_CODE_WEIGHT
    else:
        issues.append(f"primary_failure_code: expected {expected_primary!r}, got {actual_primary!r}")

    total += PRIMARY_FAILURE_CODE_EVIDENCE_WEIGHT
    pfe = agent_obj.get("primary_failure_code_evidence", "") if isinstance(agent_obj, dict) else ""
    if isinstance(pfe, str) and len(pfe.strip()) >= PRIMARY_EVIDENCE_MIN_CHARS:
        earned += PRIMARY_FAILURE_CODE_EVIDENCE_WEIGHT
    else:
        issues.append(f"primary_failure_code_evidence: missing or under {PRIMARY_EVIDENCE_MIN_CHARS} chars")

    total += ALTERNATIVE_CODES_CONSIDERED_WEIGHT
    alts = agent_obj.get("alternative_codes_considered", []) if isinstance(agent_obj, dict) else []
    seen_codes = set()
    alts_valid = (
        isinstance(alts, list)
        and len(alts) >= ALT_CODES_MIN_COUNT
        and all(
            isinstance(it, dict)
            and isinstance(it.get("code"), str)
            and isinstance(it.get("reason_excluded"), str)
            and it["code"] in PRIMARY_CODES_INCLUDING_NONE
            and it["code"] != actual_primary
            and len(it["reason_excluded"].strip()) >= EVIDENCE_MIN_CHARS
            and (it["code"] not in seen_codes and not seen_codes.add(it["code"]))
            for it in alts
        )
    )
    if alts_valid:
        earned += ALTERNATIVE_CODES_CONSIDERED_WEIGHT
    else:
        issues.append("alternative_codes_considered: missing, malformed, duplicates primary, or duplicate codes")

    expected_evidence = oracle_obj.get("failure_reason_evidence", {}) or {}
    actual_evidence = agent_obj.get("failure_reason_evidence", {}) if isinstance(agent_obj, dict) else {}
    if not isinstance(actual_evidence, dict):
        actual_evidence = {}
    for code in expected_evidence.keys():
        total += PER_CODE_EVIDENCE_WEIGHT
        val = actual_evidence.get(code, "")
        if isinstance(val, str) and len(val.strip()) >= EVIDENCE_MIN_CHARS:
            earned += PER_CODE_EVIDENCE_WEIGHT
        else:
            issues.append(f"failure_reason_evidence.{code}: missing or under {EVIDENCE_MIN_CHARS} chars")

    return earned, total, issues


def score_code_application_table(agent_table, oracle_table):
    earned = 0
    total = 0
    misses = []
    if not isinstance(agent_table, dict):
        agent_table = {}
    for code, expected_list in oracle_table.items():
        total += CODE_APPLICATION_TABLE_PER_KEY_WEIGHT
        agent_list = agent_table.get(code)
        if isinstance(agent_list, list) and sorted(agent_list) == sorted(expected_list):
            earned += CODE_APPLICATION_TABLE_PER_KEY_WEIGHT
        else:
            misses.append(f"code_application_table[{code}]: expected {sorted(expected_list)}, got {agent_list}")
    return earned, total, misses


def score_response_count_per_code(agent_counts, oracle_counts):
    earned = 0
    total = 0
    misses = []
    if not isinstance(agent_counts, dict):
        agent_counts = {}
    for code, expected_count in oracle_counts.items():
        total += RESPONSE_COUNT_PER_CODE_KEY_WEIGHT
        actual_count = agent_counts.get(code)
        if isinstance(actual_count, int) and actual_count == expected_count:
            earned += RESPONSE_COUNT_PER_CODE_KEY_WEIGHT
        else:
            misses.append(f"response_count_per_code[{code}]: expected {expected_count}, got {actual_count}")
    return earned, total, misses


def score_cross_response_observations(text):
    if isinstance(text, str) and len(text.strip()) >= CROSS_OBS_MIN_CHARS:
        return CROSS_RESPONSE_OBSERVATIONS_WEIGHT, CROSS_RESPONSE_OBSERVATIONS_WEIGHT, []
    return 0, CROSS_RESPONSE_OBSERVATIONS_WEIGHT, [f"cross_response_observations: missing or under {CROSS_OBS_MIN_CHARS} chars"]


def weighted_score(agent_output, oracle):
    earned = 0
    total = 0
    lines = []

    tl_earned, tl_total, tl_lines = score_top_level_facts(agent_output, oracle)
    earned += tl_earned
    total += tl_total
    lines.extend(tl_lines)

    agent_by_id = by_id(agent_output)
    oracle_by_id = by_id(oracle)
    for rid in sorted(oracle_by_id):
        o = oracle_by_id[rid]
        a = agent_by_id.get(rid)
        if a is None:
            response_total = (
                FINAL_ANSWER_CORRECT_WEIGHT
                + FAILURE_REASONS_SET_WEIGHT
                + PRIMARY_FAILURE_CODE_WEIGHT
                + PRIMARY_FAILURE_CODE_EVIDENCE_WEIGHT
                + ALTERNATIVE_CODES_CONSIDERED_WEIGHT
                + PER_CODE_EVIDENCE_WEIGHT * len(o.get("failure_reason_evidence", {}) or {})
            )
            total += response_total
            lines.append(f"{rid}: 0/{response_total}; missing per-response assessment")
            continue
        r_earned, r_total, r_issues = score_per_response(rid, a, o)
        earned += r_earned
        total += r_total
        if r_issues:
            lines.append(f"{rid}: {r_earned}/{r_total}; " + "; ".join(r_issues))
        else:
            lines.append(f"{rid}: {r_earned}/{r_total}; all per-response fields correct")

    cat_earned, cat_total, cat_misses = score_code_application_table(
        agent_output.get("code_application_table"), oracle.get("code_application_table", {})
    )
    earned += cat_earned
    total += cat_total
    if cat_misses:
        lines.append(f"code_application_table: {cat_earned}/{cat_total}; " + "; ".join(cat_misses[:6]))
    else:
        lines.append(f"code_application_table: {cat_earned}/{cat_total}; all 12 keys correct")

    rcpc_earned, rcpc_total, rcpc_misses = score_response_count_per_code(
        agent_output.get("response_count_per_code"), oracle.get("response_count_per_code", {})
    )
    earned += rcpc_earned
    total += rcpc_total
    if rcpc_misses:
        lines.append(f"response_count_per_code: {rcpc_earned}/{rcpc_total}; " + "; ".join(rcpc_misses[:6]))
    else:
        lines.append(f"response_count_per_code: {rcpc_earned}/{rcpc_total}; all 12 keys correct")

    cro_earned, cro_total, cro_misses = score_cross_response_observations(agent_output.get("cross_response_observations"))
    earned += cro_earned
    total += cro_total
    if cro_misses:
        lines.append(f"cross_response_observations: {cro_earned}/{cro_total}; " + cro_misses[0])
    else:
        lines.append(f"cross_response_observations: {cro_earned}/{cro_total}; ok")

    score = earned / total if total else 0.0
    return score, earned, total, "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-output", required=True)
    ap.add_argument("--oracle", required=True)
    ap.add_argument("--reward-out", required=True)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)
    if os.path.exists("/logs"):
        os.makedirs("/logs/agent", exist_ok=True)

    try:
        agent_output = load_json(args.agent_output)
        oracle = load_json(args.oracle)
    except Exception as e:
        with open(args.reward_out, "w", encoding="utf-8") as f:
            json.dump({"reward": 0.0}, f)
        try:
            with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
                f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}\n")
        except OSError:
            pass
        return

    if agent_output == oracle:
        score = 1.0
        _, _, _, justification = weighted_score(oracle, oracle)
    else:
        score, earned, total, justification = weighted_score(agent_output, oracle)

    with open(args.reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": score}, f)

    try:
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: {score:.4f}\n\n")
            f.write("Scored fields and weights:\n")
            f.write(f"- gold_final_answer (string match): {GOLD_FINAL_ANSWER_WEIGHT}\n")
            f.write(f"- acceptable_solution_ids (set match): {ACCEPTABLE_SOLUTION_IDS_WEIGHT}\n")
            f.write(f"- final_answer_correct (per response): {FINAL_ANSWER_CORRECT_WEIGHT}\n")
            f.write(f"- failure_reasons (per response, set match, all-or-nothing): {FAILURE_REASONS_SET_WEIGHT}\n")
            f.write(f"- primary_failure_code (per response, exact match): {PRIMARY_FAILURE_CODE_WEIGHT}\n")
            f.write(f"- primary_failure_code_evidence (per response, presence + >={PRIMARY_EVIDENCE_MIN_CHARS} chars): {PRIMARY_FAILURE_CODE_EVIDENCE_WEIGHT}\n")
            f.write(f"- alternative_codes_considered (per response, >={ALT_CODES_MIN_COUNT} well-formed unique entries, codes != primary): {ALTERNATIVE_CODES_CONSIDERED_WEIGHT}\n")
            f.write(f"- failure_reason_evidence per oracle-listed code (presence + >={EVIDENCE_MIN_CHARS} chars): {PER_CODE_EVIDENCE_WEIGHT}\n")
            f.write(f"- code_application_table per key (12 keys, exact list match): {CODE_APPLICATION_TABLE_PER_KEY_WEIGHT}\n")
            f.write(f"- response_count_per_code per key (12 keys, integer match): {RESPONSE_COUNT_PER_CODE_KEY_WEIGHT}\n")
            f.write(f"- cross_response_observations (presence + >={CROSS_OBS_MIN_CHARS} chars): {CROSS_RESPONSE_OBSERVATIONS_WEIGHT}\n\n")
            f.write(justification)
            f.write("\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
