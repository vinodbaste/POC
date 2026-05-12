import argparse
import json
import os
import re

from openai import OpenAI


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    return text


def validate_structure(agent_output: dict) -> list:
    """
    Pre-LLM structural checks enforcing all instruction.md ordering requirements.
    Returns list of violation strings (empty = pass).
    """
    violations = []

    required_keys = {"artifact_audits", "summary"}
    extra_keys = set(agent_output.keys()) - required_keys
    if extra_keys:
        violations.append(f"Extra top-level keys not allowed: {sorted(extra_keys)}")
    missing_keys = required_keys - set(agent_output.keys())
    if missing_keys:
        violations.append(f"Missing required top-level keys: {sorted(missing_keys)}")
        return violations

    # artifact_audits must contain exactly 20 entries (one per manifest artifact)
    audits = agent_output.get("artifact_audits", [])
    if len(audits) != 20:
        violations.append(
            f"artifact_audits must contain exactly 20 entries; found {len(audits)}"
        )

    # artifact_audits must be sorted by artifact_id (ascending)
    audit_ids = [a.get("artifact_id", "") for a in audits]
    if audit_ids != sorted(audit_ids):
        violations.append(
            f"artifact_audits is not sorted by artifact_id. "
            f"First few: {audit_ids[:5]}"
        )

    summary = agent_output.get("summary", {})

    # competitions_covered must be sorted alphabetically
    comps = summary.get("competitions_covered", [])
    if comps != sorted(comps):
        violations.append(
            f"summary.competitions_covered is not sorted alphabetically. Got: {comps}"
        )

    # correct_problem_ids must be sorted alphabetically
    correct_ids = summary.get("correct_problem_ids", [])
    if correct_ids != sorted(correct_ids):
        violations.append(
            f"summary.correct_problem_ids is not sorted alphabetically. Got: {correct_ids}"
        )

    # incorrect_problem_ids must be sorted alphabetically
    incorrect_ids = summary.get("incorrect_problem_ids", [])
    if incorrect_ids != sorted(incorrect_ids):
        violations.append(
            f"summary.incorrect_problem_ids is not sorted alphabetically. Got: {incorrect_ids}"
        )

    # Summary counts must be consistent with artifact_audits
    actual_correct   = sum(1 for a in audits if a.get("verdict") == "correct")
    actual_incorrect = sum(1 for a in audits if a.get("verdict") == "incorrect")
    if summary.get("correct_count") != actual_correct:
        violations.append(
            f"summary.correct_count={summary.get('correct_count')} "
            f"does not match actual correct verdicts={actual_correct}"
        )
    if summary.get("incorrect_count") != actual_incorrect:
        violations.append(
            f"summary.incorrect_count={summary.get('incorrect_count')} "
            f"does not match actual incorrect verdicts={actual_incorrect}"
        )

    return violations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    args = parser.parse_args()

    try:
        agent_output = json.load(open(args.agent_output))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}")
        return

    oracle = json.load(open(args.oracle))

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    # --- Pre-LLM structural validation ---
    violations = validate_structure(agent_output)
    if violations:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write(
                "Score: 0.0\n\n"
                "Structural validation failed — instruction.md ordering requirements not met:\n"
                + "\n".join(f"  - {v}" for v in violations)
            )
        return

    # --- LLM judge for content correctness ---
    client = OpenAI(
        api_key=os.environ["FIREWORKS_API_KEY"],
        base_url="https://api.fireworks.ai/inference/v1",
    )

    prompt = (
        "You are an evaluation judge grading an agent's proof-audit report against a gold oracle.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Evaluate field by field, in artifact_id order.\n"
        "- artifact_id, problem_id, competition, and verdict must match exactly.\n"
        "- For first_material_issue_summary on incorrect proofs, accept concise paraphrases "
        "that identify the same first material flaw as the oracle.\n"
        "- For correct proofs, accept 'none', 'no material issue', or equivalent.\n"
        "- Do not reward summaries that describe only downstream consequences while missing the first flaw.\n"
        "- summary fields (correct_count, incorrect_count, competitions_covered, "
        "correct_problem_ids, incorrect_problem_ids) must match exactly in the same sorted order.\n"
        "Score between 0.0 and 1.0 based on the fraction of fields that pass.\n"
        "List EACH artifact and summary group as PASSED or FAILED with a brief reason.\n"
        "Respond in JSON only (no markdown):\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": <int>, '
        '"justification": "<field-by-field breakdown>"}'
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2p5",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    raw = response.choices[0].message.content or ""
    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw: {raw}")
        return

    score = float(result.get("score", 0.0))
    json.dump({"reward": score}, open(args.reward_out, "w"))
    with open("/logs/agent/judge_justification.txt", "w") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', '?')} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
