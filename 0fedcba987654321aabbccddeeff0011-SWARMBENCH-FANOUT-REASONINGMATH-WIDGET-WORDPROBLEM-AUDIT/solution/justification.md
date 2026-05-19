# Oracle Justification

## Gold final value

**2640.**

## Derivation

1. Morning shift: 150 widgets/hour × 8 hours = **1200** widgets.
2. Afternoon rate: 150 − 30 = **120** widgets/hour.
3. Afternoon output: 120 × 7 = **840** widgets.
4. Evening rate: 2 × 120 = **240** widgets/hour.
5. Evening output: 240 × 4 = **960** widgets.
6. Total: 1200 + 840 + 960 = **3000** widgets.
7. Defects rejected: 12% × 3000 = **360** widgets.
8. Pass quality control: 3000 − 360 = **2640** widgets.

Gold integer = **2640**.

## Acceptable solutions

Response C's committed final value is exactly 2640. `acceptable_solution_ids = ["C"]`.

## Failure-reason code meanings

- `wrong_rate_or_constant` — used a numerical constant (rate, hours, percentage) different from the problem.
- `wrong_arithmetic_at_specific_step` — used correct constants but produced a wrong arithmetic result at a step.
- `wrong_operation_applied` — applied the wrong operation type (e.g., + instead of −).
- `wrong_percentage_interpretation` — misinterpreted the 12% defect rate direction or base.
- `final_answer_does_not_match_workings` — committed final integer inconsistent with workings.
- `missed_or_skipped_required_step` — skipped a required computation step.
- `truncated_or_incomplete_answer` — workings present but no committed final integer.
- `non_terminating_or_no_committed_answer` — no workings and no answer (stands alone).

## Per-response audit derivations

### Response A — long verbose with backtracks; percentage interpretation reversed

Response A computes 1200 + 840 + 960 = 3000 correctly and identifies the 12% rate, then explicitly reasons "the 12% pass QC" and concludes 12% × 3000 = 360 widgets pass. The problem clearly states 12% are REJECTED; A reads it backwards. Final committed answer is 360, not 2640.

Oracle `failure_reasons` for A: `["wrong_percentage_interpretation"]`.

### Response B — casual conversational; wrong rate constant

Response B uses "150 − 25 = 125" for the afternoon rate. The problem states "30 fewer", not 25. All downstream computations are arithmetically consistent with the wrong rate (125 × 7 = 875, 2 × 125 = 250, etc.). The single load-bearing defect is the wrong constant.

Oracle `failure_reasons` for B: `["wrong_rate_or_constant"]`.

### Response C — JSON-only; CORRECT

Response C commits `{"answer": 2640}` exactly. final_value_correct = true, failure_reasons = []. C is the unique accepted solution.

Oracle `failure_reasons` for C: `[]`.

### Response D — terse paragraph; truncated mid-sentence

Response D performs the shift arithmetic correctly through total = 3000, then trails off mid-sentence ("...the 12% rejection rate to get the number that pass quality control...") without committing a final integer.

Oracle `failure_reasons` for D: `["truncated_or_incomplete_answer"]`.

### Response E — markdown step-by-step; wrong operation at the final step

Response E walks through every step with correct constants and arithmetic through "defects = 360". At the final step it writes "3000 + 360 = 3360 widgets pass" — addition instead of subtraction for "passed = total minus rejected". The operation type at the final step is wrong.

Oracle `failure_reasons` for E: `["wrong_operation_applied"]`.

### Response F — friendly chatbot; wrong arithmetic at one specific step

Response F uses correct rates and operations throughout. The afternoon and evening outputs (840 and 960) are correct. The final sum is stated as 1200 + 840 + 960 = 3100 — the input numerals are correct but the sum is wrong (should be 3000). The downstream 12% × 3100 = 372 and 3100 − 372 = 2728 are arithmetically consistent with the wrong intermediate sum.

Oracle `failure_reasons` for F: `["wrong_arithmetic_at_specific_step"]`.

## Scoring rubric

Total possible weight is **184 points**; reward = `passed / 184` clipped to [0.0, 1.0]. JSON-equality match short-circuits to 1.0.

- `gold_final_value` (exact integer match): 2 points
- `acceptable_solution_ids` (set match, oracle = `["C"]`): 2 points
- Each per-response audit (six times): **30 points all-or-nothing**. Awarded only if `response_id`, `final_value_correct`, and the EXACT `failure_reasons` set match the oracle. Any mismatch forfeits all 30 for that response.

Total: 2 + 2 + 6 × 30 = 184.
