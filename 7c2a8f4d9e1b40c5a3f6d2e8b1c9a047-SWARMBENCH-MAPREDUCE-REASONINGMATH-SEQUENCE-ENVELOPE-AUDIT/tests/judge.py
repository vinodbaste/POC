import argparse
import json
import os


WEIGHTS = {
    "C1_correct_final_answer": 8,
    "C2_concrete_strategy": 1,
    "C3_valid_upper_bound": 12,
    "C4_valid_lower_bound": 12,
    "C5_worst_case_guarantee": 5,
    "C6_no_invalid_one_draw_inference": 15,
    "C7_no_exact_mixed_pair_requirement": 15,
    "C8_no_fatal_wrong_claim": 30,
    "verdict": 35,
    "primary_failure_code": 140,
}


CRITERIA = [
    "C1_correct_final_answer",
    "C2_concrete_strategy",
    "C3_valid_upper_bound",
    "C4_valid_lower_bound",
    "C5_worst_case_guarantee",
    "C6_no_invalid_one_draw_inference",
    "C7_no_exact_mixed_pair_requirement",
    "C8_no_fatal_wrong_claim",
]


PRIMARY_CODES = [
    "NONE",
    "WRONG_FINAL_NUMBER",
    "CONTRADICTORY_FINAL_ANSWER",
    "NO_CONCRETE_STRATEGY",
    "INVALID_UPPER_BOUND",
    "MISSING_LOWER_BOUND",
    "NOT_WORST_CASE",
    "INVALID_ONE_DRAW_INFERENCE",
    "UNNECESSARY_MIXED_PAIR_REQUIREMENT",
    "FATAL_WRONG_CLAIM",
]


PER_RESPONSE_EVIDENCE_WEIGHT = 5
PER_RESPONSE_PRIMARY_EVIDENCE_WEIGHT = 8
PER_RESPONSE_ALT_CODES_WEIGHT = 8
PER_RESPONSE_CRITERIA_COUNT_WEIGHT = 10
PER_RESPONSE_VERDICT_CONSISTENCY_WEIGHT = 15
CONSISTENCY_TABLE_PER_KEY_WEIGHT = 100
CRITERION_PASS_RATE_PER_KEY_WEIGHT = 80
VERDICT_DISTRIBUTION_PER_KEY_WEIGHT = 150
CRITERION_PAIR_CO_PASS_PER_KEY_WEIGHT = 12
RESPONSE_PAIR_CRITERION_AGREEMENT_PER_KEY_WEIGHT = 10
RESPONSE_TRIPLE_CRITERION_AGREEMENT_PER_KEY_WEIGHT = 8
CROSS_RESPONSE_OBSERVATIONS_WEIGHT = 30
EVIDENCE_MIN_CHARS = 20
PRIMARY_EVIDENCE_MIN_CHARS = 50
ALT_CODES_MIN_COUNT = 2
CROSS_OBSERVATIONS_MIN_CHARS = 300


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def by_id(obj):
    return {item.get("solution_id"): item for item in obj.get("evaluations", [])}


def score_per_response_labels(o, a):
    response_earned = 0
    response_total = 0
    mismatches = []
    for key in CRITERIA:
        w = WEIGHTS[key]
        response_total += w
        expected = o.get("criteria", {}).get(key)
        actual = a.get("criteria", {}).get(key)
        if actual == expected:
            response_earned += w
        else:
            mismatches.append(f"{key}: expected {expected}, got {actual}, weight {w}")
    for key in ["verdict", "primary_failure_code"]:
        w = WEIGHTS[key]
        response_total += w
        expected = o.get(key)
        actual = a.get(key)
        if actual == expected:
            response_earned += w
        else:
            mismatches.append(f"{key}: expected {expected}, got {actual}, weight {w}")
    return response_earned, response_total, mismatches


def score_per_response_evidence(a):
    earned = 0
    total = 0
    issues = []
    crit_evidence = a.get("criterion_evidence", {}) if isinstance(a.get("criterion_evidence"), dict) else {}
    for crit in CRITERIA:
        total += PER_RESPONSE_EVIDENCE_WEIGHT
        val = crit_evidence.get(crit, "")
        if isinstance(val, str) and len(val.strip()) >= EVIDENCE_MIN_CHARS:
            earned += PER_RESPONSE_EVIDENCE_WEIGHT
        else:
            issues.append(f"criterion_evidence.{crit}: missing or too short")
    total += PER_RESPONSE_PRIMARY_EVIDENCE_WEIGHT
    pfe = a.get("primary_failure_code_evidence", "")
    if isinstance(pfe, str) and len(pfe.strip()) >= PRIMARY_EVIDENCE_MIN_CHARS:
        earned += PER_RESPONSE_PRIMARY_EVIDENCE_WEIGHT
    else:
        issues.append("primary_failure_code_evidence: missing or too short")
    total += PER_RESPONSE_ALT_CODES_WEIGHT
    acc = a.get("alternative_codes_considered", [])
    if isinstance(acc, list) and len(acc) >= ALT_CODES_MIN_COUNT and all(
        isinstance(it, dict) and isinstance(it.get("code"), str) and isinstance(it.get("reason_excluded"), str) and it.get("code") in PRIMARY_CODES + ["NONE"]
        for it in acc
    ):
        earned += PER_RESPONSE_ALT_CODES_WEIGHT
    else:
        issues.append("alternative_codes_considered: missing, too short, or malformed")
    return earned, total, issues


def score_per_response_criteria_count(o, a):
    total = PER_RESPONSE_CRITERIA_COUNT_WEIGHT
    expected = o.get("criteria_satisfied_count")
    actual = a.get("criteria_satisfied_count")
    if isinstance(actual, int) and actual == expected:
        return PER_RESPONSE_CRITERIA_COUNT_WEIGHT, total, []
    return 0, total, [f"criteria_satisfied_count: expected {expected}, got {actual}"]


def score_per_response_verdict_consistency(o, a):
    total = PER_RESPONSE_VERDICT_CONSISTENCY_WEIGHT
    expected = o.get("verdict_consistency_check")
    actual = a.get("verdict_consistency_check")
    if isinstance(actual, bool) and actual == expected:
        return PER_RESPONSE_VERDICT_CONSISTENCY_WEIGHT, total, []
    return 0, total, [f"verdict_consistency_check: expected {expected}, got {actual}"]


def score_criterion_pair_co_pass(agent_pairs, oracle_pairs):
    if not isinstance(agent_pairs, dict):
        return 0, CRITERION_PAIR_CO_PASS_PER_KEY_WEIGHT * len(oracle_pairs), [
            "criterion_pair_co_pass_count missing or non-object"
        ]
    earned = 0
    total = 0
    misses = []
    for key, expected_count in oracle_pairs.items():
        total += CRITERION_PAIR_CO_PASS_PER_KEY_WEIGHT
        actual_count = agent_pairs.get(key)
        if isinstance(actual_count, int) and actual_count == expected_count:
            earned += CRITERION_PAIR_CO_PASS_PER_KEY_WEIGHT
        else:
            misses.append(f"criterion_pair_co_pass_count[{key}]: expected {expected_count}, got {actual_count}")
    return earned, total, misses


def score_response_pair_agreement(agent_pairs, oracle_pairs):
    if not isinstance(agent_pairs, dict):
        return 0, RESPONSE_PAIR_CRITERION_AGREEMENT_PER_KEY_WEIGHT * len(oracle_pairs), [
            "response_pair_criterion_agreement missing or non-object"
        ]
    earned = 0
    total = 0
    misses = []
    for key, expected_count in oracle_pairs.items():
        total += RESPONSE_PAIR_CRITERION_AGREEMENT_PER_KEY_WEIGHT
        actual_count = agent_pairs.get(key)
        if isinstance(actual_count, int) and actual_count == expected_count:
            earned += RESPONSE_PAIR_CRITERION_AGREEMENT_PER_KEY_WEIGHT
        else:
            misses.append(f"response_pair_criterion_agreement[{key}]: expected {expected_count}, got {actual_count}")
    return earned, total, misses


def score_response_triple_agreement(agent_triples, oracle_triples):
    if not isinstance(agent_triples, dict):
        return 0, RESPONSE_TRIPLE_CRITERION_AGREEMENT_PER_KEY_WEIGHT * len(oracle_triples), [
            "response_triple_criterion_agreement missing or non-object"
        ]
    earned = 0
    total = 0
    misses = []
    for key, expected_count in oracle_triples.items():
        total += RESPONSE_TRIPLE_CRITERION_AGREEMENT_PER_KEY_WEIGHT
        actual_count = agent_triples.get(key)
        if isinstance(actual_count, int) and actual_count == expected_count:
            earned += RESPONSE_TRIPLE_CRITERION_AGREEMENT_PER_KEY_WEIGHT
        else:
            misses.append(f"response_triple_criterion_agreement[{key}]: expected {expected_count}, got {actual_count}")
    return earned, total, misses


def score_consistency_table(agent_table, oracle_table):
    if not isinstance(agent_table, dict):
        return 0, CONSISTENCY_TABLE_PER_KEY_WEIGHT * len(oracle_table), [f"consistency_table missing or non-object; lost all keys"]
    earned = 0
    total = 0
    misses = []
    for code, expected_list in oracle_table.items():
        total += CONSISTENCY_TABLE_PER_KEY_WEIGHT
        agent_list = agent_table.get(code)
        if isinstance(agent_list, list) and sorted(agent_list) == sorted(expected_list):
            earned += CONSISTENCY_TABLE_PER_KEY_WEIGHT
        else:
            misses.append(f"consistency_table[{code}]: expected {expected_list}, got {agent_list}")
    return earned, total, misses


def score_criterion_pass_rate(agent_rate, oracle_rate):
    if not isinstance(agent_rate, dict):
        return 0, CRITERION_PASS_RATE_PER_KEY_WEIGHT * len(oracle_rate), [f"criterion_pass_rate missing or non-object"]
    earned = 0
    total = 0
    misses = []
    for crit, expected_count in oracle_rate.items():
        total += CRITERION_PASS_RATE_PER_KEY_WEIGHT
        actual_count = agent_rate.get(crit)
        if isinstance(actual_count, int) and actual_count == expected_count:
            earned += CRITERION_PASS_RATE_PER_KEY_WEIGHT
        else:
            misses.append(f"criterion_pass_rate[{crit}]: expected {expected_count}, got {actual_count}")
    return earned, total, misses


def score_verdict_distribution(agent_dist, oracle_dist):
    if not isinstance(agent_dist, dict):
        return 0, VERDICT_DISTRIBUTION_PER_KEY_WEIGHT * len(oracle_dist), [f"verdict_distribution missing or non-object"]
    earned = 0
    total = 0
    misses = []
    for verdict, expected_list in oracle_dist.items():
        total += VERDICT_DISTRIBUTION_PER_KEY_WEIGHT
        agent_list = agent_dist.get(verdict)
        if isinstance(agent_list, list) and sorted(agent_list) == sorted(expected_list):
            earned += VERDICT_DISTRIBUTION_PER_KEY_WEIGHT
        else:
            misses.append(f"verdict_distribution[{verdict}]: expected {expected_list}, got {agent_list}")
    return earned, total, misses


def score_cross_response_observations(agent_text):
    if isinstance(agent_text, str) and len(agent_text.strip()) >= CROSS_OBSERVATIONS_MIN_CHARS:
        return CROSS_RESPONSE_OBSERVATIONS_WEIGHT, CROSS_RESPONSE_OBSERVATIONS_WEIGHT, []
    return 0, CROSS_RESPONSE_OBSERVATIONS_WEIGHT, ["cross_response_observations: missing or too short"]


def weighted_score(agent_output, oracle):
    agent_evals = by_id(agent_output)
    oracle_evals = by_id(oracle)
    earned = 0
    total = 0
    lines = []

    for sid in sorted(oracle_evals):
        o = oracle_evals[sid]
        a = agent_evals.get(sid)
        if a is None:
            response_total = sum(WEIGHTS.values()) + len(CRITERIA) * PER_RESPONSE_EVIDENCE_WEIGHT + PER_RESPONSE_PRIMARY_EVIDENCE_WEIGHT + PER_RESPONSE_ALT_CODES_WEIGHT + PER_RESPONSE_CRITERIA_COUNT_WEIGHT
            total += response_total
            lines.append(f"{sid}: 0/{response_total} weighted points; missing evaluation")
            continue
        lbl_earned, lbl_total, lbl_issues = score_per_response_labels(o, a)
        ev_earned, ev_total, ev_issues = score_per_response_evidence(a)
        ct_earned, ct_total, ct_issues = score_per_response_criteria_count(o, a)
        vc_earned, vc_total, vc_issues = score_per_response_verdict_consistency(o, a)
        r_earned = lbl_earned + ev_earned + ct_earned + vc_earned
        r_total = lbl_total + ev_total + ct_total + vc_total
        earned += r_earned
        total += r_total
        all_issues = lbl_issues + ev_issues + ct_issues + vc_issues
        if all_issues:
            lines.append(f"{sid}: {r_earned}/{r_total}; " + "; ".join(all_issues))
        else:
            lines.append(f"{sid}: {r_earned}/{r_total}; all scored fields correct")

    ct_earned, ct_total, ct_issues = score_consistency_table(agent_output.get("consistency_table"), oracle.get("consistency_table", {}))
    earned += ct_earned
    total += ct_total
    if ct_issues:
        lines.append(f"consistency_table: {ct_earned}/{ct_total}; " + "; ".join(ct_issues[:6]))
    else:
        lines.append(f"consistency_table: {ct_earned}/{ct_total}; all keys correct")

    cpr_earned, cpr_total, cpr_issues = score_criterion_pass_rate(agent_output.get("criterion_pass_rate"), oracle.get("criterion_pass_rate", {}))
    earned += cpr_earned
    total += cpr_total
    if cpr_issues:
        lines.append(f"criterion_pass_rate: {cpr_earned}/{cpr_total}; " + "; ".join(cpr_issues[:6]))
    else:
        lines.append(f"criterion_pass_rate: {cpr_earned}/{cpr_total}; all keys correct")

    vd_earned, vd_total, vd_issues = score_verdict_distribution(agent_output.get("verdict_distribution"), oracle.get("verdict_distribution", {}))
    earned += vd_earned
    total += vd_total
    if vd_issues:
        lines.append(f"verdict_distribution: {vd_earned}/{vd_total}; " + "; ".join(vd_issues))
    else:
        lines.append(f"verdict_distribution: {vd_earned}/{vd_total}; all keys correct")

    cp_earned, cp_total, cp_issues = score_criterion_pair_co_pass(agent_output.get("criterion_pair_co_pass_count"), oracle.get("criterion_pair_co_pass_count", {}))
    earned += cp_earned
    total += cp_total
    if cp_issues:
        lines.append(f"criterion_pair_co_pass_count: {cp_earned}/{cp_total}; " + "; ".join(cp_issues[:6]))
    else:
        lines.append(f"criterion_pair_co_pass_count: {cp_earned}/{cp_total}; all 28 pairs correct")

    rp_earned, rp_total, rp_issues = score_response_pair_agreement(agent_output.get("response_pair_criterion_agreement"), oracle.get("response_pair_criterion_agreement", {}))
    earned += rp_earned
    total += rp_total
    if rp_issues:
        lines.append(f"response_pair_criterion_agreement: {rp_earned}/{rp_total}; " + "; ".join(rp_issues[:6]))
    else:
        lines.append(f"response_pair_criterion_agreement: {rp_earned}/{rp_total}; all 28 pairs correct")

    rt_earned, rt_total, rt_issues = score_response_triple_agreement(agent_output.get("response_triple_criterion_agreement"), oracle.get("response_triple_criterion_agreement", {}))
    earned += rt_earned
    total += rt_total
    if rt_issues:
        lines.append(f"response_triple_criterion_agreement: {rt_earned}/{rt_total}; " + "; ".join(rt_issues[:6]))
    else:
        lines.append(f"response_triple_criterion_agreement: {rt_earned}/{rt_total}; all 56 triples correct")

    cro_earned, cro_total, cro_issues = score_cross_response_observations(agent_output.get("cross_response_observations"))
    earned += cro_earned
    total += cro_total
    if cro_issues:
        lines.append(f"cross_response_observations: {cro_earned}/{cro_total}; " + cro_issues[0])
    else:
        lines.append(f"cross_response_observations: {cro_earned}/{cro_total}; ok")

    score = earned / total if total else 0.0
    return score, earned, total, "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-output", required=True)
    ap.add_argument("--oracle", required=True)
    ap.add_argument("--reward-out", required=True)
    ap.add_argument("--details-out", default=None)
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
        score, earned, total, justification = 1.0, 0, 0, "Exact match with oracle."
    else:
        score, earned, total, justification = weighted_score(agent_output, oracle)

    with open(args.reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": score}, f)

    try:
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: {score:.4f} ({earned}/{total} weighted points)\n\n")
            f.write("Scored fields and weights:\n")
            for key, weight in WEIGHTS.items():
                f.write(f"- {key}: {weight} (per response)\n")
            f.write(f"- criterion_evidence per criterion (presence + min length): {PER_RESPONSE_EVIDENCE_WEIGHT} (per response per criterion)\n")
            f.write(f"- primary_failure_code_evidence (presence + min length): {PER_RESPONSE_PRIMARY_EVIDENCE_WEIGHT} (per response)\n")
            f.write(f"- alternative_codes_considered (>=2 items, well-formed): {PER_RESPONSE_ALT_CODES_WEIGHT} (per response)\n")
            f.write(f"- criteria_satisfied_count (integer match): {PER_RESPONSE_CRITERIA_COUNT_WEIGHT} (per response)\n")
            f.write(f"- consistency_table per key (exact match against oracle): {CONSISTENCY_TABLE_PER_KEY_WEIGHT}\n")
            f.write(f"- criterion_pass_rate per key (integer match): {CRITERION_PASS_RATE_PER_KEY_WEIGHT}\n")
            f.write(f"- verdict_distribution per key (sorted list match): {VERDICT_DISTRIBUTION_PER_KEY_WEIGHT}\n")
            f.write(f"- cross_response_observations (presence + min length): {CROSS_RESPONSE_OBSERVATIONS_WEIGHT}\n\n")
            f.write(justification)
            f.write("\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
