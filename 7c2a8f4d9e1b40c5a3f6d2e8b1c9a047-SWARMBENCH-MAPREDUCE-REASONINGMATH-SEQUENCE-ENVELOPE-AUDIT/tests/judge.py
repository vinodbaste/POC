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


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def by_id(obj):
    return {item.get("solution_id"): item for item in obj.get("evaluations", [])}


def weighted_score(agent_output, oracle):
    agent_evals = by_id(agent_output)
    oracle_evals = by_id(oracle)

    earned = 0
    total = 0
    lines = []

    for sid in sorted(oracle_evals):
        o = oracle_evals[sid]
        a = agent_evals.get(sid)
        response_earned = 0
        response_total = 0
        mismatches = []

        if a is None:
            response_total = sum(WEIGHTS.values())
            total += response_total
            lines.append(f"{sid}: 0/{response_total} weighted points; missing evaluation")
            continue

        for key in CRITERIA:
            w = WEIGHTS[key]
            total += w
            response_total += w
            expected = o.get("criteria", {}).get(key)
            actual = a.get("criteria", {}).get(key)
            if actual == expected:
                earned += w
                response_earned += w
            else:
                mismatches.append(f"{key}: expected {expected}, got {actual}, weight {w}")

        for key in ["verdict", "primary_failure_code"]:
            w = WEIGHTS[key]
            total += w
            response_total += w
            expected = o.get(key)
            actual = a.get(key)
            if actual == expected:
                earned += w
                response_earned += w
            else:
                mismatches.append(f"{key}: expected {expected}, got {actual}, weight {w}")

        if mismatches:
            lines.append(f"{sid}: {response_earned}/{response_total} weighted points; " + "; ".join(mismatches))
        else:
            lines.append(f"{sid}: {response_earned}/{response_total} weighted points; all scored labels correct")

    score = earned / total if total else 0.0
    return score, earned, total, "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-output", required=True)
    ap.add_argument("--oracle", required=True)
    ap.add_argument("--reward-out", required=True)
    ap.add_argument("--details-out", required=True, default=None)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)
    os.makedirs("/logs/agent", exist_ok=True)

    try:
        agent_output = load_json(args.agent_output)
        oracle = load_json(args.oracle)
    except Exception as e:
        with open(args.reward_out, "w", encoding="utf-8") as f:
            json.dump({"reward": 0.0}, f)
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}\n")
        return

    if agent_output == oracle:
        total = len(oracle.get("evaluations", [])) * sum(WEIGHTS.values())
        score, earned, total, justification = 1.0, total, total, "Exact match with oracle."
    else:
        score, earned, total, justification = weighted_score(agent_output, oracle)

    with open(args.reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": score}, f)

    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(f"Score: {score:.3f} ({earned}/{total} weighted label points)\n\n")
        f.write("Scored labels per response and weights:\n")
        for key, weight in WEIGHTS.items():
            f.write(f"- {key}: {weight}\n")
        f.write("\nbrief_justification, summary, accepted_solutions, rejected_solutions, and best_solution are not scored.\n\n")
        f.write(justification)
        f.write("\n")


if __name__ == "__main__":
    main()
