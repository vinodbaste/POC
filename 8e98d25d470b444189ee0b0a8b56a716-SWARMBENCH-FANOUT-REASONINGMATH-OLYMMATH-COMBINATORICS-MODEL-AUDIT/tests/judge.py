import argparse
import json
import os
import re


REQUIRED_TOP_KEYS = {"gold_final_answer", "acceptable_solution_ids", "per_response_assessment"}
EXPECTED_IDS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

POINTS_GOLD = 2
POINTS_ACCEPTABLE_IDS = 2
POINTS_PER_RESPONSE = 30
TOTAL_POINTS = POINTS_GOLD + POINTS_ACCEPTABLE_IDS + POINTS_PER_RESPONSE * len(EXPECTED_IDS)


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return text[start:end + 1]
    return text


def index_by_id(audits):
    out = {}
    if not isinstance(audits, list):
        return out
    for entry in audits:
        if isinstance(entry, dict):
            sid = entry.get("solution_id")
            if isinstance(sid, str):
                out[sid.strip().upper()] = entry
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.reward_out) or ".", exist_ok=True)
    os.makedirs("/logs/agent", exist_ok=True)
    justification_path = "/logs/agent/judge_justification.txt"

    try:
        raw = open(args.agent_output).read()
        agent_output = json.loads(extract_json(raw))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid JSON: {e}")
        return

    oracle = json.load(open(args.oracle))

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    earned = 0
    lines = []

    if not isinstance(agent_output, dict):
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write("Score: 0.0\n\nAgent output is not a JSON object.")
        return

    actual_keys = set(agent_output.keys())
    if actual_keys != REQUIRED_TOP_KEYS:
        missing = REQUIRED_TOP_KEYS - actual_keys
        extra = actual_keys - REQUIRED_TOP_KEYS
        lines.append(f"Top-level key set mismatch: missing={sorted(missing)}, extra={sorted(extra)}.")

    oracle_gold = oracle.get("gold_final_answer")
    agent_gold = agent_output.get("gold_final_answer")
    if isinstance(agent_gold, str) and agent_gold.strip() == str(oracle_gold).strip():
        earned += POINTS_GOLD
        lines.append(f"gold_final_answer: {POINTS_GOLD}/{POINTS_GOLD} (matches '{oracle_gold}').")
    else:
        lines.append(f"gold_final_answer: 0/{POINTS_GOLD} (expected '{oracle_gold}', got '{agent_gold}').")

    oracle_accept = set(oracle.get("acceptable_solution_ids", []) or [])
    agent_accept_raw = agent_output.get("acceptable_solution_ids", []) or []
    if isinstance(agent_accept_raw, list):
        agent_accept = {str(x).strip().upper() for x in agent_accept_raw if isinstance(x, str)}
    else:
        agent_accept = set()
    if agent_accept == oracle_accept:
        earned += POINTS_ACCEPTABLE_IDS
        lines.append(f"acceptable_solution_ids: {POINTS_ACCEPTABLE_IDS}/{POINTS_ACCEPTABLE_IDS} (matches {sorted(oracle_accept)}).")
    else:
        lines.append(f"acceptable_solution_ids: 0/{POINTS_ACCEPTABLE_IDS} (expected {sorted(oracle_accept)}, got {sorted(agent_accept)}).")

    oracle_by_id = index_by_id(oracle.get("per_response_assessment", []))
    agent_by_id = index_by_id(agent_output.get("per_response_assessment", []))

    per_response_summary = []
    for sid in EXPECTED_IDS:
        oracle_entry = oracle_by_id.get(sid)
        agent_entry = agent_by_id.get(sid)
        if oracle_entry is None:
            per_response_summary.append(f"{sid}: skipped (no oracle entry).")
            continue
        if agent_entry is None:
            per_response_summary.append(f"{sid}: 0/{POINTS_PER_RESPONSE} (no agent entry).")
            continue

        oracle_far = bool(oracle_entry.get("final_answer_correct", False))
        agent_far = bool(agent_entry.get("final_answer_correct", False)) if isinstance(agent_entry.get("final_answer_correct"), bool) else None

        oracle_reasons = oracle_entry.get("failure_reasons", []) or []
        agent_reasons_raw = agent_entry.get("failure_reasons", []) or []
        if not isinstance(oracle_reasons, list):
            oracle_reasons = []
        if isinstance(agent_reasons_raw, list):
            agent_reasons = {str(x).strip() for x in agent_reasons_raw if isinstance(x, str)}
        else:
            agent_reasons = set()
        oracle_reasons_set = {str(x).strip() for x in oracle_reasons if isinstance(x, str)}

        agent_sid = agent_entry.get("solution_id")
        sid_ok = isinstance(agent_sid, str) and agent_sid.strip().upper() == sid
        far_ok = (agent_far == oracle_far)
        reasons_ok = (agent_reasons == oracle_reasons_set)

        if sid_ok and far_ok and reasons_ok:
            earned += POINTS_PER_RESPONSE
            per_response_summary.append(f"{sid}: {POINTS_PER_RESPONSE}/{POINTS_PER_RESPONSE}.")
        else:
            issues = []
            if not sid_ok:
                issues.append(f"id={agent_sid}")
            if not far_ok:
                issues.append(f"final_answer_correct={agent_far} (oracle {oracle_far})")
            if not reasons_ok:
                issues.append(f"failure_reasons={sorted(agent_reasons)} (oracle {sorted(oracle_reasons_set)})")
            per_response_summary.append(f"{sid}: 0/{POINTS_PER_RESPONSE} ({'; '.join(issues)}).")

    score = max(0.0, min(1.0, earned / TOTAL_POINTS))
    json.dump({"reward": score}, open(args.reward_out, "w"))

    with open(justification_path, "w") as f:
        f.write(f"Score: {score:.4f} ({earned}/{TOTAL_POINTS} passed)\n\n")
        f.write("\n".join(lines))
        f.write("\n\nPer-response:\n")
        f.write("\n".join(per_response_summary))


if __name__ == "__main__":
    main()
