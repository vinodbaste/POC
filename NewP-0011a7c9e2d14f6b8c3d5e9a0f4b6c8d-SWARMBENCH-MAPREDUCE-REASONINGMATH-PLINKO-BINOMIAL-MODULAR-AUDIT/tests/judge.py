import argparse
import json
import os
import re


TOP_LEVEL_WEIGHTS = {
    "correct_answer_latex": 200,
    "acceptable_solution_ids": 200,
}

BASE_PER_RESPONSE_WEIGHTS = {
    "response_id": 1,
    "extracted_final_answer_latex": 1,
    "extracted_path_count_latex": 1,
    "final_answer_correct": 1,
    "path_count_setup_correct": 3,
    "has_p_adic_or_modular_error": 4,
    "has_crt_or_final_reduction_error": 1,
    "has_unsupported_computational_claim": 4,
    "has_stepwise_structure": 1,
    "has_proper_latex_format": 1,
}

RESPONSE_IDS = list("ABCDEFGHI")


def write_reward(path, score):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"reward": score}, f)


def write_justification(text):
    os.makedirs("/logs/agent", exist_ok=True)
    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(text)


def by_response_id(obj):
    rows = obj.get("per_response_assessment", [])
    if not isinstance(rows, list):
        return {}
    out = {}
    for row in rows:
        if isinstance(row, dict) and isinstance(row.get("response_id"), str):
            out[row["response_id"]] = row
    return out


def extract_int(value):
    if value is None:
        return None
    if isinstance(value, int):
        return value
    text = str(value)
    m = re.search(r"-?\d+", text)
    if not m:
        return None
    return int(m.group(0))


def normalize_final_answer(value):
    n = extract_int(value)
    if n is None:
        return None
    return n % 1000


def normalize_path_count(value):
    if value is None:
        return None

    text = str(value).replace(" ", "")
    text = text.replace("\\dbinom", "\\binom")

    if "\\binom{2026}{396}" in text or "\\binom{2026}{1630}" in text:
        return "C2026_396"
    if "\\binom{3260}{1234}" in text or "\\binom{3260}{2026}" in text:
        return "C3260_1234"

    compact = text.replace("$", "")
    compact = compact.replace("\\", "")

    if re.search(r"C\(?\{?2026\}?,\{?396\}?\)?", compact):
        return "C2026_396"
    if re.search(r"C\(?\{?2026\}?,\{?1630\}?\)?", compact):
        return "C2026_396"
    if re.search(r"C\(?\{?3260\}?,\{?1234\}?\)?", compact):
        return "C3260_1234"
    if re.search(r"C\(?\{?3260\}?,\{?2026\}?\)?", compact):
        return "C3260_1234"

    return text


def equivalent(field, expected, got):
    bool_fields = {
        "final_answer_correct",
        "path_count_setup_correct",
        "has_p_adic_or_modular_error",
        "has_crt_or_final_reduction_error",
        "has_unsupported_computational_claim",
        "has_stepwise_structure",
        "has_proper_latex_format",
    }

    if field in bool_fields:
        return isinstance(got, bool) and got == expected

    if field == "correct_answer_latex":
        return normalize_final_answer(got) == normalize_final_answer(expected)

    if field == "extracted_final_answer_latex":
        if expected is None:
            return got is None
        return normalize_final_answer(got) == normalize_final_answer(expected)

    if field == "extracted_path_count_latex":
        if expected is None:
            return got is None
        return normalize_path_count(got) == normalize_path_count(expected)

    if field == "acceptable_solution_ids":
        return sorted(got or []) == sorted(expected or [])

    return got == expected


def field_weight(field, expected):
    weight = BASE_PER_RESPONSE_WEIGHTS[field]

    # p-adic/modular errors are common across this response set, so this label
    # is important but not highly discriminative by itself.
    if expected is True and field == "has_p_adic_or_modular_error":
        return 40

    # CRT/final-reduction contradictions are sparse final-answer-critical traps.
    # They carry high weight because missing them is a serious audit failure.
    if expected is True and field == "has_crt_or_final_reduction_error":
        return 420

    # Unsupported black-box computation is also sparse and final-answer-critical,
    # but easier than the CRT contradiction label.
    if expected is True and field == "has_unsupported_computational_claim":
        return 70

    return weight


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent_output = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        write_reward(args.reward_out, 0.0)
        write_justification(f"Score: 0.0\n\nAgent output missing or invalid: {e}")
        return

    with open(args.oracle, "r", encoding="utf-8") as f:
        oracle = json.load(f)

    expected_order = RESPONSE_IDS
    got_order = [
        row.get("response_id")
        for row in agent_output.get("per_response_assessment", [])
        if isinstance(row, dict)
    ]
    if got_order != expected_order:
        write_reward(args.reward_out, 0.0)
        write_justification(
            "Score: 0.0 (0/1 passed)\n\n"
            "per_response_assessment must contain exactly response_id A through I in order."
        )
        return

    oracle_by_id = by_response_id(oracle)
    agent_by_id = by_response_id(agent_output)

    passed = 0
    total = 0
    details = []

    for field, weight in TOP_LEVEL_WEIGHTS.items():
        total += weight
        expected = oracle.get(field)
        got = agent_output.get(field)
        if equivalent(field, expected, got):
            passed += weight
            details.append(f"top.{field}: PASS +{weight}")
        else:
            details.append(
                f"top.{field}: FAIL +0/{weight} "
                f"(oracle={expected!r}, agent={got!r})"
            )

    for response_id in RESPONSE_IDS:
        oracle_row = oracle_by_id.get(response_id, {})
        agent_row = agent_by_id.get(response_id, {})

        for field in BASE_PER_RESPONSE_WEIGHTS:
            expected = oracle_row.get(field)
            got = agent_row.get(field)
            weight = field_weight(field, expected)
            total += weight

            if equivalent(field, expected, got):
                passed += weight
                details.append(f"{response_id}.{field}: PASS +{weight}")
            else:
                details.append(
                    f"{response_id}.{field}: FAIL +0/{weight} "
                    f"(oracle={expected!r}, agent={got!r})"
                )

    score = passed / total if total else 0.0
    write_reward(args.reward_out, score)
    write_justification(
        f"Score: {score:.4f} ({passed}/{total} passed)\n\n"
        + "\n".join(details)
    )


if __name__ == "__main__":
    main()
