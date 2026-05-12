import argparse
import json
import re

VALID_OPTIONS = {"A", "B", "C", "D"}
VALID_FLAW_TYPES = {"unjustified_claim", "misapplied_theorem", "false_assumption", "scope_violation", "algebraic_error"}
AUDIT_REQUIRED_KEYS = {"artifact_id", "problem_id", "competition", "year", "selected_option", "flaw_type"}
SHARD_REQUIRED_KEYS = {"shard_id", "artifact_ids", "artifact_count", "choice_counts"}


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1 and end > start:
        return text[start:end + 1]
    return text


def validate_structure(agent_output: dict) -> list[str]:
    """
    Structural checks that enforce every instruction.md requirement.
    Returns a list of violation strings; empty list means pass.
    """
    violations = []

    required_keys = {"artifact_audits", "shard_summaries", "summary"}
    extra_keys = set(agent_output.keys()) - required_keys
    if extra_keys:
        violations.append(f"Extra top-level keys: {sorted(extra_keys)}")
    missing_keys = required_keys - set(agent_output.keys())
    if missing_keys:
        violations.append(f"Missing top-level keys: {sorted(missing_keys)}")
        return violations

    audits = agent_output.get("artifact_audits", [])
    audit_ids = []
    for idx, audit in enumerate(audits):
        missing = AUDIT_REQUIRED_KEYS - set(audit.keys())
        if missing:
            violations.append(f"artifact_audits[{idx}] missing fields: {sorted(missing)}")
            continue
        audit_ids.append(audit["artifact_id"])
        opt = audit.get("selected_option")
        if opt not in VALID_OPTIONS:
            violations.append(
                f"artifact_audits[{idx}] ({audit['artifact_id']}): "
                f"selected_option={opt!r} is not one of A, B, C, D"
            )
        flaw = audit.get("flaw_type")
        if flaw not in VALID_FLAW_TYPES:
            violations.append(
                f"artifact_audits[{idx}] ({audit['artifact_id']}): "
                f"flaw_type={flaw!r} is not one of the valid flaw types"
            )

    if audit_ids != sorted(audit_ids):
        violations.append(
            f"artifact_audits is not sorted by artifact_id. First few: {audit_ids[:5]}"
        )

    expected_ids = [f"artifact_{i:02d}" for i in range(1, 51)]
    missing_artifacts = set(expected_ids) - set(audit_ids)
    if missing_artifacts:
        violations.append(
            f"artifact_audits is missing {len(missing_artifacts)} artifact(s): "
            + ", ".join(sorted(missing_artifacts)[:5])
            + ("..." if len(missing_artifacts) > 5 else "")
        )

    shards = agent_output.get("shard_summaries", [])
    shard_ids = []
    for idx, shard in enumerate(shards):
        missing = SHARD_REQUIRED_KEYS - set(shard.keys())
        if missing:
            violations.append(f"shard_summaries[{idx}] missing fields: {sorted(missing)}")
            continue
        shard_ids.append(shard["shard_id"])
        art_ids = shard.get("artifact_ids", [])
        art_count = shard.get("artifact_count")
        if not isinstance(art_ids, list):
            violations.append(f"shard_summaries[{idx}] ({shard['shard_id']}): artifact_ids is not a list")
        elif art_count != len(art_ids):
            violations.append(
                f"shard_summaries[{idx}] ({shard['shard_id']}): "
                f"artifact_count={art_count} does not match len(artifact_ids)={len(art_ids)}"
            )

    if shard_ids != sorted(shard_ids):
        violations.append(f"shard_summaries is not sorted by shard_id. Got: {shard_ids}")

    abo = agent_output.get("summary", {}).get("artifacts_by_option", {})
    for opt, art_list in abo.items():
        if not isinstance(art_list, list):
            violations.append(f"artifacts_by_option['{opt}'] is not a list")
            continue
        if art_list != sorted(art_list):
            violations.append(f"artifacts_by_option['{opt}'] is not sorted. Got: {art_list}")

    return violations


def score(agent_output: dict, oracle: dict) -> tuple[float, int, int, str]:
    """
    Score = (option_passed + flaw_passed) / (2 * total_artifacts).
    Total is always 2 * len(oracle artifact_audits) — never left to interpretation.

    Shard grouping is not scored: any internally consistent shard grouping
    receives the same reward as long as per-artifact selected_option and
    flaw_type values are correct. Only summary aggregate fields are checked informally.
    """
    oracle_map = {a["artifact_id"]: {"option": a["selected_option"], "flaw_type": a["flaw_type"]}
                  for a in oracle["artifact_audits"]}
    n_artifacts = len(oracle_map)

    agent_map = {a.get("artifact_id"): {"option": a.get("selected_option"), "flaw_type": a.get("flaw_type")}
                 for a in agent_output.get("artifact_audits", [])}

    failed_options = []
    failed_flaws = []
    option_passed = 0
    flaw_passed = 0
    for aid in sorted(oracle_map):
        o = oracle_map[aid]
        a = agent_map.get(aid, {})
        if a.get("option") == o["option"]:
            option_passed += 1
        else:
            failed_options.append(aid)
        if a.get("flaw_type") == o["flaw_type"]:
            flaw_passed += 1
        else:
            failed_flaws.append(aid)

    # Summary field checks (informational — derivative of selected_option values)
    oracle_summary = oracle.get("summary", {})
    agent_summary = agent_output.get("summary", {})
    failed_summary = []
    for key in ["total_artifacts", "choice_counts", "competition_counts",
                "year_counts", "artifacts_by_option"]:
        if agent_summary.get(key) != oracle_summary.get(key):
            note = ""
            if key == "choice_counts":
                oc = oracle_summary.get("choice_counts", {})
                ac = agent_summary.get("choice_counts", {})
                diffs = [f"{k}={ac.get(k,'?')} vs {oc[k]}"
                         for k in oc if ac.get(k) != oc[k]]
                if diffs:
                    note = " (" + ", ".join(diffs) + ")"
            failed_summary.append(key + note)

    total = 2 * n_artifacts
    passed = option_passed + flaw_passed
    reward = passed / total if total > 0 else 0.0

    lines = [f"Score: {reward} ({option_passed}/{n_artifacts} options passed, {flaw_passed}/{n_artifacts} flaw types passed)\n"]
    if failed_options:
        lines.append("Failed options: " + ", ".join(failed_options))
    if failed_flaws:
        lines.append("Failed flaw types: " + ", ".join(failed_flaws))
    if failed_summary:
        lines.append("Failed summary fields (informational): " + ", ".join(failed_summary))

    return reward, passed, total, "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    args = parser.parse_args()

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

    violations = validate_structure(agent_output)
    if violations:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write(
                "Score: 0.0\n\nStructural validation failed:\n"
                + "\n".join(f"  - {v}" for v in violations)
            )
        return

    reward, passed, total, justification = score(agent_output, oracle)

    json.dump({"reward": reward}, open(args.reward_out, "w"))
    with open(justification_path, "w") as f:
        f.write(justification)


if __name__ == "__main__":
    main()
