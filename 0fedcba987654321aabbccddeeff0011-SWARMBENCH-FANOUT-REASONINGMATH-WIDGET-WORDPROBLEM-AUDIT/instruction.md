You are auditing six real, unedited model responses to a deterministic multi-step factory word problem: computing the number of widgets that pass quality control after three shifts of production and a 12% defect rate.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem.md`
- Provenance: `/input_artifacts/provenance.md`
- Released model responses:
  - `/input_artifacts/proposed_solutions/response_A.md`
  - `/input_artifacts/proposed_solutions/response_B.md`
  - `/input_artifacts/proposed_solutions/response_C.md`
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`

Task:

1. Read the problem statement and all six released responses.
2. Independently compute the gold integer final answer by solving the word problem from first principles.
3. Determine which response(s), if any, give a final answer that exactly matches the gold integer.
4. For each response A through F, identify the EXACT SET of failure-reason codes from the controlled vocabulary below whose triggering condition is concretely present in that single response's text or final answer.

## Allowed failure-reason codes

Each code applies ONLY when its triggering condition is concretely instantiated in that single response's text.

- `wrong_rate_or_constant`
  - TRIGGER: the response uses a numerical constant (a rate, multiplier, hour count, or percentage value) that does not match the constant stated in the problem. Examples include using `150 - 25 = 125` for the afternoon shift rate (the problem states "30 fewer"), or using 6 hours instead of 7 for an afternoon shift duration.

- `wrong_arithmetic_at_specific_step`
  - TRIGGER: the response uses a correct numerical constant and correct operation at a step but produces a wrong product, sum, or difference for that specific calculation (a math slip). Trigger pattern: a stated equation like `1200 + 840 + 960 = 3100` (correct numerals on the left, but a wrong total on the right). Distinct from `wrong_rate_or_constant`: there, the input numeral is wrong; here, the output of the arithmetic is wrong.

- `wrong_operation_applied`
  - TRIGGER: the response applies the wrong arithmetic operation at a step (addition instead of subtraction, multiplication instead of division, etc.) given the correct constants. Example: computing `total + rejected` instead of `total - rejected` for the final "passed" count.

- `wrong_percentage_interpretation`
  - TRIGGER: the response misinterprets the 12% defect rate. Examples: interpreting "12% are rejected" as "12% pass quality control" and reporting 12% of the total as the answer; or computing the percentage against a wrong base (e.g., 12% of the morning shift only).

- `final_answer_does_not_match_workings`
  - TRIGGER: the response's committed final integer answer is inconsistent with the arithmetic shown in its own workings (e.g., the workings derive 2640 but the boxed final answer is 2460 or some unrelated number).

- `missed_or_skipped_required_step`
  - TRIGGER: the response omits a required step entirely: e.g., never computes the afternoon shift contribution, or never applies the 12% defect filter.

- `truncated_or_incomplete_answer`
  - TRIGGER: the response produces some workings but stops before reaching a committed final integer answer (e.g., ends mid-sentence after stating an intermediate total). Distinct from `non_terminating_or_no_committed_answer`: here a partial reasoning chain exists.

- `non_terminating_or_no_committed_answer`
  - TRIGGER: the response does not produce any identifiable workings or final answer at all (loops on a phrase, refuses to commit, or never reaches any numeric output). Stands alone — when this code fires, no other code applies.

## Important scoring and selection rules

- The audit is evaluated as an EXACT SET MATCH per response. Both extra failure-reason codes and missing failure-reason codes are wrong: a response audit receives credit only if the exact set of codes matches the oracle's set for that response.
- Most responses have 1-2 applicable codes. One response is fully correct and has an empty failure_reasons list.
- Apply a code only when its triggering condition is concretely instantiated in the response's text.
- Use an empty list `[]` for `failure_reasons` exactly when the response's final answer equals the gold integer AND no failure-reason trigger fires.
- `acceptable_solution_ids` is the set of `response_id` strings (uppercase) whose `final_value_correct` is `true` AND whose `failure_reasons` list is empty.

## Label definitions for each released response

- `response_id`: the response letter, exactly one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`.
- `final_value_correct`: `true` exactly when the response's committed final integer answer equals the gold integer. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the 8 allowed failure-reason codes above.

## Failure-code disambiguation guidance

- `wrong_rate_or_constant` versus `wrong_arithmetic_at_specific_step`: if the input numeral to a calculation is wrong, the trigger is `wrong_rate_or_constant`. If the input numerals are correct but the output is wrong, the trigger is `wrong_arithmetic_at_specific_step`. They do not co-apply for the same step unless the response makes both errors at different steps.
- `wrong_operation_applied` versus `wrong_arithmetic_at_specific_step`: if the wrong operation type is applied (e.g., + instead of -), the trigger is `wrong_operation_applied`. If the correct operation type is applied but the result is miscomputed, the trigger is `wrong_arithmetic_at_specific_step`.
- `wrong_percentage_interpretation` fires for misinterpretation of the 12% defect rate's direction or base. It does not co-apply with `wrong_operation_applied` unless the response makes both errors at distinct steps.
- `final_answer_does_not_match_workings` fires when the response's workings clearly imply one number but the boxed/stated final answer is a different number. It is distinct from `wrong_arithmetic_at_specific_step` (which is an internal calculation error within the workings).
- `truncated_or_incomplete_answer` fires when the response has workings but stops before a committed final answer. `non_terminating_or_no_committed_answer` fires only when no workings AND no final answer exist; it stands alone.

## Worked scoring example

A hypothetical response that correctly computes 1200 + 840 + 960 = 3000, correctly identifies the 12% defect rate, but then says "so 12% of 3000 = 360 widgets pass quality control" misinterprets the percentage direction. The applicable code is `wrong_percentage_interpretation`. No other code fires.

## Verifier scoring rule

The verifier (llm-judge) scores the final JSON against the oracle. The total weight is 4 + 30 x 6 = 184 points.

- `gold_final_value` (exact integer match against oracle's gold integer): 2 points
- `acceptable_solution_ids` (set match against oracle): 2 points
- Each per-response audit (six times, one per response_id A through F): 30 points all-or-nothing. Awarded only if all three of `response_id`, `final_value_correct`, and the EXACT failure_reasons set match the oracle for that response. Any mismatch in failure_reasons (extra code, missing code, or both) forfeits the full 30 points. No partial credit.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "gold_final_value": <integer>,
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_value_correct": <true or false>,
      "failure_reasons": ["<zero or more allowed failure-reason codes>"]
    }
  ]
}

In the actual output, include six objects in `per_response_assessment`, one for each response A, B, C, D, E, F, in that order.
