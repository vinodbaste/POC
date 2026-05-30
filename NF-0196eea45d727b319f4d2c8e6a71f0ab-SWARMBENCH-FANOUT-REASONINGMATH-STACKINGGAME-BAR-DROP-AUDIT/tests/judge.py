import argparse
import json
import os


ALLOWED_FAILURE_REASONS = {
    "wrong_bar_placement",
    "wrong_row_clear_count",
    "initial_cell_count_error",
    "invalid_or_incomplete_final_output",
    "correct_stacking_logic",
}


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")

    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent_output = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump(
            {"reward": 0.0},
            open(args.reward_out, "w", encoding="utf-8")
        )

        with open(
            "/logs/agent/judge_justification.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(
                f"Score: 0.0\n\n"
                f"Agent output missing or invalid: {e}"
            )

        return

    with open(args.oracle, "r", encoding="utf-8") as f:
        oracle = json.load(f)

    if agent_output == oracle:
        json.dump(
            {"reward": 1.0},
            open(args.reward_out, "w", encoding="utf-8")
        )

        with open(
            "/logs/agent/judge_justification.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(
                "Score: 1.0\n\n"
                "Agent output exactly matches oracle."
            )

        return

    # All-or-nothing per response (mirrors successful audit benchmarks):
    #   - correct_final_answer .................. 5 pts
    #   - acceptable_equivalent_answers ......... 5 pts
    #   - 6 responses x 30 pts each ........... 180 pts
    # A response only earns its 30 pts when response_id, final_answer_correct,
    # and the failure_reasons set ALL match the oracle exactly. This forces the
    # agent to produce precise per-response audits; partial audits earn nothing.
    passed = 0
    total = 190
    details = []

    if agent_output.get("correct_final_answer") == oracle.get("correct_final_answer"):
        passed += 5
        details.append("correct_final_answer 5/5")
    else:
        details.append("correct_final_answer 0/5")

    agent_equivs = set(agent_output.get("acceptable_equivalent_answers", []))
    oracle_equivs = set(oracle.get("acceptable_equivalent_answers", []))
    if agent_equivs == oracle_equivs:
        passed += 5
        details.append("acceptable_equivalent_answers 5/5")
    else:
        details.append("acceptable_equivalent_answers 0/5")

    agent_assessments = agent_output.get("per_response_assessment", [])
    oracle_assessments = oracle.get("per_response_assessment", [])

    if not isinstance(agent_assessments, list):
        agent_assessments = []

    # Enforce schema strictness: instruction.md requires exactly six objects
    # in alphabetical A-F order, and each object must contain exactly the
    # three keys response_id, final_answer_correct, failure_reasons (no
    # brief_assessment or other extra fields). The verifier enforces both
    # rules; mismatches lose the entire 30 pts for that response.
    REQUIRED_KEYS = {"response_id", "final_answer_correct", "failure_reasons"}

    for index, expected in enumerate(oracle_assessments):
        response_id = expected["response_id"]
        actual = (
            agent_assessments[index]
            if index < len(agent_assessments) and isinstance(agent_assessments[index], dict)
            else {}
        )

        order_match = (
            isinstance(actual, dict)
            and actual.get("response_id") == response_id
        )

        keys_match = (
            isinstance(actual, dict)
            and set(actual.keys()) == REQUIRED_KEYS
        )

        correctness_match = (
            actual.get("final_answer_correct")
            == expected.get("final_answer_correct")
        )

        actual_reasons = actual.get("failure_reasons", [])
        reasons_exact = (
            isinstance(actual_reasons, list)
            and set(actual_reasons) <= ALLOWED_FAILURE_REASONS
            and set(actual_reasons) == set(expected.get("failure_reasons", []))
        )

        if order_match and keys_match and correctness_match and reasons_exact:
            passed += 30
            details.append(f"Response {response_id} 30/30 (exact match)")
        else:
            mismatch_parts = []
            if not order_match:
                mismatch_parts.append(
                    f"order/response_id (expected {response_id} at index {index})"
                )
            if not keys_match:
                if isinstance(actual, dict):
                    extra = set(actual.keys()) - REQUIRED_KEYS
                    missing = REQUIRED_KEYS - set(actual.keys())
                    parts = []
                    if extra:
                        parts.append(f"extra={sorted(extra)}")
                    if missing:
                        parts.append(f"missing={sorted(missing)}")
                    mismatch_parts.append("schema_keys " + ", ".join(parts))
                else:
                    mismatch_parts.append("schema_keys (object missing)")
            if not correctness_match:
                mismatch_parts.append("final_answer_correct")
            if not reasons_exact:
                mismatch_parts.append("failure_reasons")
            details.append(
                f"Response {response_id} 0/30 "
                f"(mismatch: {'; '.join(mismatch_parts) or 'unknown'})"
            )

    score = min(max(passed / total, 0.0), 1.0)

    json.dump(
        {"reward": score},
        open(args.reward_out, "w", encoding="utf-8")
    )

    with open(
        "/logs/agent/judge_justification.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(
            f"Score: {score} "
            f"({passed}/{total} passed)\n\n"
            + "\n".join(details)
        )


if __name__ == "__main__":
    main()
