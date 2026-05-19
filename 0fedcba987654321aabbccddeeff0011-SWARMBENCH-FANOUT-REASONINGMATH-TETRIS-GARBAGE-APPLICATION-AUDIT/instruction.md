You are auditing six real, unedited model responses to a deterministic Tetris board-state problem: applying four garbage lines (with specified hole columns) to an initial 10-by-20 board state under standard rising-garbage mechanics, and computing the resulting 20-by-10 board after garbage application and any post-clear shifting.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem.md`
- Provenance note for the released model responses: `/input_artifacts/provenance.md`
- Released model response files:
  - `/input_artifacts/proposed_solutions/response_A.md`
  - `/input_artifacts/proposed_solutions/response_B.md`
  - `/input_artifacts/proposed_solutions/response_C.md`
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`

Task:

1. Read the problem statement and all six released responses.
2. Independently apply the four garbage lines to the initial board to derive the gold 20-by-10 final board state.
3. Determine which response(s), if any, give a final board that exactly matches the gold board.
4. For each response A through F, identify the EXACT SET of failure-reason codes from the controlled vocabulary below whose triggering condition is concretely present in that single response's text or in its final claimed board.

## Allowed failure-reason codes

Each code applies ONLY when its triggering condition is concretely instantiated in that single response's text or claimed final board.

- `wrong_garbage_insertion_direction`
  - TRIGGER: the response applies the garbage lines from the WRONG side of the playfield (e.g., inserts garbage at the top and pushes existing content downward) OR fails to shift the existing board content upward when garbage is applied (e.g., overlays garbage on top of existing rows without shifting). Trigger phrases: "garbage falls from the top", "I add garbage at row 0", or a final board where the original non-empty rows still appear at their original row indices despite four garbage lines having been added.

- `wrong_hole_column_alignment`
  - TRIGGER: the response places one or more garbage holes at column indices that differ from the specified [3, 3, 5, 2]. Trigger pattern: at least one garbage row in the final board has its 0 at a column other than the column specified by the problem for that garbage line.

- `wrong_garbage_order_or_count`
  - TRIGGER: the response applies a number of garbage lines other than 4, OR applies the four garbage lines in an order other than the specified oldest-first order. Trigger pattern: the final board's garbage block contains fewer or more than four garbage rows, or its garbage rows are arranged as if a different sequence of hole columns had been applied.

- `wrong_post_shift_topout_handling`
  - TRIGGER: the response handles the upward shift incorrectly: drops the wrong number of top rows, leaves stale non-empty rows in the top of the board, fails to shift the original content up by exactly 4 rows, or treats topout as if non-empty content should remain at its original row position even after shifting. Distinct from `wrong_garbage_insertion_direction` because here the response does shift, but shifts the wrong amount or in the wrong manner.

- `invalid_or_incomplete_final_output`
  - TRIGGER: the response does not provide a complete identifiable 20-row by 10-column final board. Includes outputs that have fewer than 20 rows, more than 20 rows, rows of wrong length, or rows containing characters outside {0, 1}.

## Important scoring and selection rules

- The audit is evaluated as an EXACT SET MATCH per response. Both extra failure-reason codes and missing failure-reason codes are wrong: a response audit receives credit only if the exact set of codes matches the oracle's set for that response.
- Most responses have 1-2 applicable codes; some have 0 if `final_board_correct` is true (but every released response has at least one defect).
- Apply a code only when its triggering condition is concretely instantiated in the response's text or final claimed board.
- Use an empty list `[]` for `failure_reasons` exactly when the response's final claimed board equals the gold board AND no failure-reason trigger fires.
- `acceptable_solution_ids` is the set of `response_id` strings (uppercase) whose `final_board_correct` is `true` AND whose `failure_reasons` list is empty.

## Label definitions for each released response

- `response_id`: the response letter, exactly one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`.
- `final_board_correct`: `true` exactly when the response's final claimed 20-by-10 board equals the gold board exactly, row by row. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the 5 allowed failure-reason codes above.

## Failure-code disambiguation guidance

- `wrong_garbage_insertion_direction` is the primary diagnostic when the response either applies garbage from the wrong side OR overlays garbage without shifting. It is distinct from `wrong_post_shift_topout_handling`, which fires when the response shifts but shifts the wrong amount.
- `wrong_hole_column_alignment` fires whenever one or more garbage holes are at the wrong column, regardless of whether the rest of the application logic was correct. It does not co-apply with `wrong_garbage_order_or_count` unless BOTH the order is wrong AND specific hole columns are wrong; if the order is wrong and that explains all hole misplacements, only `wrong_garbage_order_or_count` applies.
- `wrong_garbage_order_or_count` fires when the count or order of garbage lines is wrong. If the response applies all four garbage lines in the specified order but mis-places individual hole columns, that is `wrong_hole_column_alignment` and not `wrong_garbage_order_or_count`.
- `wrong_post_shift_topout_handling` fires when the response correctly inserts garbage at the bottom but mis-shifts the upper rows: shifts by the wrong number of rows, leaves stale rows in place, or mishandles topout truncation. It typically co-occurs with `wrong_garbage_insertion_direction` only if the response also fails to push the original board up.
- `invalid_or_incomplete_final_output` fires whenever the committed final board fails the 20-row by 10-column shape constraint. It can co-occur with any other code that diagnoses the deeper reasoning defect causing the malformed output.

## Worked scoring example

Consider a hypothetical response that correctly applies four garbage lines to the bottom of the playfield, correctly shifts the existing board up by four, but writes the hole at column 4 instead of column 3 for the first garbage line. The applicable failure-reason codes are:

- `wrong_hole_column_alignment` because at least one garbage hole is at the wrong column.

No other code fires, because direction, count/order, and topout handling are all correct, and the output is a complete 20-by-10 board.

## Verifier scoring rule

The verifier (llm-judge) scores the final JSON against the oracle. The total weight is 4 + 30 x 6 = 184 points.

- `correct_final_board` (the 20-row gold board, exact equality): 2 points
- `acceptable_solution_ids` (set match against oracle): 2 points
- Each per-response audit (six times, one per response_id A through F): 30 points all-or-nothing. The 30 points are awarded only if all three of `response_id`, `final_board_correct`, and the EXACT failure_reasons set match the oracle for that response. Any mismatch in failure_reasons (extra code, missing code, or both) forfeits the full 30 points for that response. No partial credit inside failure_reasons.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "correct_final_board": [
    "<10-digit row 0 of gold board>",
    "<10-digit row 1>",
    ...
    "<10-digit row 19>"
  ],
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_board_correct": <true or false>,
      "failure_reasons": ["<zero or more allowed failure-reason codes>"]
    }
  ]
}

In the actual output, include six objects in `per_response_assessment`, one for each response A, B, C, D, E, F, in that order.
