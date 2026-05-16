import argparse
import json
import os
import re


VALID_ERROR_CATEGORIES = {"unjustified_claim", "misapplied_theorem", "algebraic_error", "case_error", "circular_reasoning"}
VALID_OPTIONS = {"A", "B", "C", "D"}

REQUIRED_TOP_KEYS = {"artifact_audits", "shard_summaries", "summary"}

ARTIFACT_FIELD_WEIGHTS = {
    "artifact_id": 1,
    "problem_id": 1,
    "competition": 1,
    "year": 1,
    "selected_option": 10,
    "error_category": 5,
}

SHARD_FIELD_WEIGHTS = {
    "shard_id": 1,
    "artifact_ids": 2,
    "artifact_count": 1,
    "choice_counts": 3,
}

SUMMARY_FIELD_WEIGHTS = {
    "total_artifacts": 1,
    "choice_counts": 3,
    "competition_counts": 3,
    "year_counts": 3,
    "artifacts_by_option": 5,
}


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


def index_by_id(items, key):
    out = {}
    if not isinstance(items, list):
        return out
    for entry in items:
        if isinstance(entry, dict):
            k = entry.get(key)
            if isinstance(k, str):
                out[k] = entry
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

    if not isinstance(agent_output, dict):
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write("Score: 0.0\n\nAgent output is not a JSON object.")
        return

    notes = []

    actual_keys = set(agent_output.keys())
    if actual_keys != REQUIRED_TOP_KEYS:
        missing = REQUIRED_TOP_KEYS - actual_keys
        extra = actual_keys - REQUIRED_TOP_KEYS
        notes.append(f"Top-level key set mismatch: missing={sorted(missing)}, extra={sorted(extra)}.")

    oracle_artifacts = index_by_id(oracle.get("artifact_audits", []), "artifact_id")
    agent_artifacts = index_by_id(agent_output.get("artifact_audits", []), "artifact_id")

    per_artifact_total = sum(ARTIFACT_FIELD_WEIGHTS.values()) * len(oracle_artifacts)
    per_shard_total = sum(SHARD_FIELD_WEIGHTS.values()) * len(oracle.get("shard_summaries", []))
    summary_total = sum(SUMMARY_FIELD_WEIGHTS.values())
    total_points = per_artifact_total + per_shard_total + summary_total

    earned = 0
    per_artifact_lines = []
    for aid in sorted(oracle_artifacts.keys()):
        o_entry = oracle_artifacts[aid]
        a_entry = agent_artifacts.get(aid)
        if a_entry is None:
            per_artifact_lines.append(f"{aid}: 0/{sum(ARTIFACT_FIELD_WEIGHTS.values())} (missing in agent output).")
            continue
        breakdown = []
        artifact_earned = 0
        for field, weight in ARTIFACT_FIELD_WEIGHTS.items():
            o_val = o_entry.get(field)
            a_val = a_entry.get(field)
            if isinstance(o_val, str) and isinstance(a_val, str):
                ok = o_val.strip() == a_val.strip()
            else:
                ok = (o_val == a_val)
            if ok:
                artifact_earned += weight
                breakdown.append(f"{field}=+{weight}")
            else:
                breakdown.append(f"{field}=0 (expected {o_val!r}, got {a_val!r})")
        earned += artifact_earned
        per_artifact_lines.append(f"{aid}: {artifact_earned}/{sum(ARTIFACT_FIELD_WEIGHTS.values())} ({', '.join(breakdown)}).")

    oracle_shards = index_by_id(oracle.get("shard_summaries", []), "shard_id")
    agent_shards = index_by_id(agent_output.get("shard_summaries", []), "shard_id")

    per_shard_lines = []
    for sid in sorted(oracle_shards.keys()):
        o_entry = oracle_shards[sid]
        a_entry = agent_shards.get(sid)
        if a_entry is None:
            per_shard_lines.append(f"{sid}: 0/{sum(SHARD_FIELD_WEIGHTS.values())} (missing in agent output).")
            continue
        shard_earned = 0
        for field, weight in SHARD_FIELD_WEIGHTS.items():
            o_val = o_entry.get(field)
            a_val = a_entry.get(field)
            if field == "artifact_ids":
                ok = isinstance(a_val, list) and a_val == o_val
            elif field == "choice_counts":
                ok = isinstance(a_val, dict) and a_val == o_val
            else:
                ok = (a_val == o_val)
            if ok:
                shard_earned += weight
        earned += shard_earned
        per_shard_lines.append(f"{sid}: {shard_earned}/{sum(SHARD_FIELD_WEIGHTS.values())}.")

    summary_lines = []
    o_summary = oracle.get("summary", {})
    a_summary = agent_output.get("summary", {}) if isinstance(agent_output.get("summary"), dict) else {}
    for field, weight in SUMMARY_FIELD_WEIGHTS.items():
        o_val = o_summary.get(field)
        a_val = a_summary.get(field)
        if isinstance(o_val, dict):
            ok = isinstance(a_val, dict) and a_val == o_val
        elif isinstance(o_val, list):
            ok = isinstance(a_val, list) and a_val == o_val
        else:
            ok = (a_val == o_val)
        if ok:
            earned += weight
            summary_lines.append(f"summary.{field}: +{weight}.")
        else:
            summary_lines.append(f"summary.{field}: 0/{weight} (mismatch).")

    score = max(0.0, min(1.0, earned / total_points))
    json.dump({"reward": score}, open(args.reward_out, "w"))

    with open(justification_path, "w") as f:
        f.write(f"Score: {score:.4f} ({earned}/{total_points} passed)\n\n")
        if notes:
            f.write("Top-level notes:\n  " + "\n  ".join(notes) + "\n\n")
        f.write("Per-artifact:\n")
        f.write("\n".join("  " + l for l in per_artifact_lines))
        f.write("\n\nPer-shard:\n")
        f.write("\n".join("  " + l for l in per_shard_lines))
        f.write("\n\nSummary fields:\n")
        f.write("\n".join("  " + l for l in summary_lines))


if __name__ == "__main__":
    main()
