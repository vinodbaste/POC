You are auditing raw AI-generated proposed solutions to a Tetris board-state reasoning problem.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem.md`
- Provenance note for the proposed AI-generated responses: `/input_artifacts/provenance.md`
- Proposed solution files:
  - `/input_artifacts/proposed_solutions/response_A.md`
  - `/input_artifacts/proposed_solutions/response_B.md`
  - `/input_artifacts/proposed_solutions/response_C.md`
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`

Task:
1. Read the problem statement and all six proposed solutions.
2. Independently determine the correct final Tetris board after placing the three vertical I-tetrominoes in the rightmost column and applying standard row-clearing mechanics.
3. Use standard Tetris gravity for the placement: vertical I-tetrominoes placed in a column occupy the lowest available cells in that column before row clearing, not floating cells in the top empty region.
4. Determine which proposed response(s), if any, give the correct final board.
5. For each proposed response A through F, audit whether its final board is correct and, if it is wrong, identify the concrete failure reason(s).
6. Do not decide correctness by majority vote among the proposed responses. Independently solve the board state first, then audit each response against that result.

Allowed failure reason codes:
- `wrong_i_piece_placement`: The response places/fills the I-tetromino cells incorrectly, uses the wrong number of filled cells, treats a vertical I-tetromino as having the wrong height, or fills cells outside the intended rightmost-column placement.
- `wrong_full_rows_cleared`: The response identifies the wrong full rows, clears the wrong number of rows, fails to clear rows that become full, or clears rows that are not full.
- `wrong_post_clear_shift_or_padding`: The response has the wrong post-clear gravity result: surviving rows are shifted incorrectly, empty rows are added in the wrong place, the number of top empty rows is wrong, or old rows remain where cleared/shifted rows should have changed.
- `invalid_or_incomplete_final_output`: The response does not provide an identifiable final board with exactly 20 rows and exactly 10 binary digits per row.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`.
- `final_board_correct`: `true` exactly when the response's final claimed board matches the independently correct final board exactly, including row order from top to bottom. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes. Use an empty list exactly when `final_board_correct` is `true`. If the final board is wrong, include every applicable concrete failure reason and no inapplicable reason.

Important scoring note:
The response audit is evaluated as an exact audit. Extra failure reasons and missing failure reasons are both wrong. Do not include a broad reason unless it is genuinely needed to explain why that response's final board is wrong.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "correct_final_board": [
    "<row 1, top row, exactly 10 binary digits>",
    "<row 2>",
    "... exactly 20 rows total ..."
  ],
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_board_correct": <true or false>,
      "failure_reasons": ["<zero or more allowed failure reason codes>"]
    }
  ]
}

In the actual output, include six objects in `per_response_assessment`, one for each response A, B, C, D, E, F, in that order. Do not write anything else to that file.
