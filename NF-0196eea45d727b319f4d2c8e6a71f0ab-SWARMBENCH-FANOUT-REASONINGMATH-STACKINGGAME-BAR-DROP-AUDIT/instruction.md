You are auditing raw AI-generated proposed solutions to a deterministic stacking-game reasoning problem.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem.md`
- Provenance note for the proposed AI-generated responses:
  `/input_artifacts/provenance.md`
- Proposed solution files:
  - `/input_artifacts/proposed_solutions/response_A.md`
  - `/input_artifacts/proposed_solutions/response_B.md`
  - `/input_artifacts/proposed_solutions/response_C.md`
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`

Task:
1. Read the problem statement and all six proposed solutions.
2. Independently determine the correct final occupied-cell count after all three vertical 4-cell bars are dropped and all row-clearing mechanics are resolved.
3. Use the exact mechanics stated in the problem:
   - bars remain vertical,
   - bars fall strictly downward,
   - bars cannot pass through occupied cells,
   - bars lock immediately upon contact,
   - completely filled rows are removed,
   - and rows above cleared rows shift downward.
4. Independently determine:
   - the resting position of each bar,
   - which rows become completely filled,
   - the number of rows cleared,
   - and the final occupied-cell count.
5. Audit each proposed response A through F against the independently computed gold result. Solve the mechanics yourself before reading the proposed responses, then audit each response against that result.

Allowed failure reason codes (use only these five labels — no other labels are valid):

- `wrong_bar_placement`
  The response places one or more vertical bars in incorrect rows or columns, fails to stack repeated placements correctly, allows bars to pass through occupied cells, or otherwise misapplies falling mechanics. Also use this when the response stops bars short of the lowest reachable cells in their column.

- `wrong_row_clear_count`
  The response identifies the wrong rows as completely filled, clears the wrong number of rows, fails to clear rows that genuinely become full, or applies post-clear shifting based on an incorrect set of cleared rows. Use this label whenever the cleared-row decision is wrong, regardless of whether the wrongness manifests during clearing or during the subsequent shift.

- `initial_cell_count_error`
  The response counts the initial occupied cells incorrectly. Apply this only when the response explicitly states an initial count that does not match the gold initial count.

- `invalid_or_incomplete_final_output`
  The response fails to provide a valid single-integer final answer, terminates mid-simulation, or otherwise leaves the answer indeterminate.

- `correct_stacking_logic`
  Positive label. Use this when the response correctly identifies the intended resting positions of all three bars and the column-stacking behavior, even if later reasoning (counts, clears, or final total) is wrong. Do not use this label if any bar placement is incorrect.

Trigger conditions for each label (apply each independently against the response text):
- `wrong_bar_placement` applies iff the response's claimed resting cells for any of the three bars differ from the gold resting cells you derived in step 4.
- `correct_stacking_logic` applies iff all three of the response's claimed bar resting cells match the gold resting cells exactly.
- `initial_cell_count_error` applies iff the response explicitly states an initial occupied-cell count whose integer value differs from the gold initial total. If the response never states an initial total, do not apply this label.
- `wrong_row_clear_count` applies iff the set of rows the response treats as cleared differs from the gold cleared-row set (including the case where the gold set is empty and the response clears any row).
- `invalid_or_incomplete_final_output` applies iff the response fails to produce a single final integer (truncated mid-simulation, ambiguous final value, or no integer at all).
- A magnitude-absurd final answer (for example one exceeding the 12 × 18 = 216 board capacity) is a downstream symptom of upstream errors already labeled and never receives any extra label of its own.

Label decision rules (these follow from the trigger conditions above; included as worked examples):
- A response that gets bars resting at the right rows and columns but miscounts initial cells gets `[initial_cell_count_error, correct_stacking_logic]`.
- A response that places bars correctly, miscounts initial cells, AND wrongly clears rows gets `[initial_cell_count_error, wrong_row_clear_count, correct_stacking_logic]`.
- A response that gets bars wrong AND clears wrong rows AND miscounts the initial board gets `[wrong_bar_placement, wrong_row_clear_count, initial_cell_count_error]`.
- A response that gets bars wrong AND clears wrong rows AND truncates before producing a final integer gets `[wrong_bar_placement, wrong_row_clear_count, invalid_or_incomplete_final_output]`.
- A response that gets bars wrong AND clears wrong rows but does produce an integer answer (even an absurd one) gets `[wrong_bar_placement, wrong_row_clear_count]`. Do not invent extra labels for an absurd-magnitude answer; the magnitude is a consequence of the upstream errors already labeled.
- `correct_stacking_logic` and `wrong_bar_placement` are mutually exclusive — never include both.

Label definitions for each proposed response:
- `response_id`:
  One of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`.

- `final_answer_correct`:
  `true` exactly when the response's final occupied-cell count matches the independently determined gold answer exactly. Otherwise `false`.

- `failure_reasons`:
  A JSON list chosen only from the five allowed failure reason codes.
  Use an empty list exactly when `final_answer_correct` is `true`.

  If the response is incorrect:
  - include every genuinely applicable failure reason,
  - include no inapplicable failure reason,
  - and avoid extra labels when narrower labels fully cover the failure.

Important scoring note:
The audit is graded as a strict exact-match audit:
- A per-response audit earns full credit only when `response_id`, `final_answer_correct`, and the `failure_reasons` set ALL match the gold audit exactly.
- Extra failure reasons fail the audit.
- Missing failure reasons fail the audit.
- A response may include `correct_stacking_logic` together with non-placement failure labels if the stacking behavior is understood correctly but later reasoning fails.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json`
using this exact JSON schema:

{
  "correct_final_answer": <integer>,
  "acceptable_equivalent_answers": [
    "<final answer as a string>",
    "<final answer followed by 'occupied cells'>"
  ],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": false,
      "failure_reasons": [
        "<zero or more of the five allowed failure reason codes>"
      ]
    }
  ]
}

Requirements (the verifier enforces ALL of these strictly):
- `correct_final_answer` must be the independently derived gold answer.
- `acceptable_equivalent_answers` must contain accepted equivalent textual forms.
- `per_response_assessment` MUST be a JSON array of exactly six objects in this
  exact index order:
    index 0 = response A,
    index 1 = response B,
    index 2 = response C,
    index 3 = response D,
    index 4 = response E,
    index 5 = response F.
  The verifier reads by index. An out-of-order entry forfeits the entire
  30-point per-response credit for that response.
- CRITICAL: each per-response object MUST contain EXACTLY these three keys
  and NO others:
    `"response_id"`, `"final_answer_correct"`, `"failure_reasons"`.
  Do NOT include `brief_assessment`, `rationale`, `evidence`, `notes`,
  `explanation`, or any other field. The verifier counts keys and rejects
  any object with extra keys, forfeiting all 30 points for that response
  even when the three required fields are correct.
- Use only the five allowed failure reason codes listed above. Any code
  outside the five-label vocabulary forfeits the 30 points for that response.
- `failure_reasons` must be an empty list iff `final_answer_correct` is `true`.
- Output valid JSON only. The verifier loads `/logs/agent/output.json`
  with a strict JSON parser; any markdown fence, prose preamble, or trailing
  commentary causes the parse to fail and forfeits the entire reward. Write
  the bare JSON object as the file's only content.
