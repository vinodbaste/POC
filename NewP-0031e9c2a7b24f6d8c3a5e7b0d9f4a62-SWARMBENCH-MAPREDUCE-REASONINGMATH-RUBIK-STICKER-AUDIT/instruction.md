You are auditing proposed solutions to a Rubik's-cube sticker tracking problem.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem.tex`
- Proposed solution files:
  - `/input_artifacts/proposed_solutions/response_A.tex`
  - `/input_artifacts/proposed_solutions/response_B.tex`
  - `/input_artifacts/proposed_solutions/response_C.tex`
  - `/input_artifacts/proposed_solutions/response_D.tex`
  - `/input_artifacts/proposed_solutions/response_E.tex`
  - `/input_artifacts/proposed_solutions/response_F.tex`
  - `/input_artifacts/proposed_solutions/response_G.tex`

Task:
1. Read the problem statement and all seven proposed solutions.
2. Determine the correct final sum on the front face after the specified moves, using standard Rubik's cube notation.
3. Determine which proposed response(s), if any, are fully acceptable solutions.
4. Audit every proposed response A through G using the labels defined below.
Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`.
- `extracted_final_sum`: the final numerical sum claimed by that response as an integer. Use `null` only if the response gives no identifiable final numerical sum. This field is an extraction of the response's own final answer, not a correction.
- `final_sum_correct`: `true` exactly when the response's final claimed sum is equal to the correct final sum; otherwise `false`.
- `acceptable_solution`: `true` exactly when the response is a fully acceptable solution: its final claimed sum is correct, it does not make a final-answer-critical cube-move tracking error, it does not make an arithmetic error in computing the final sum from its stated sticker counts, and it gives enough tracking or provenance to justify the final front-face non-center sticker values. A correct final number alone is not enough for this field.
- `has_standard_notation_tracking_error`: `true` if the response makes a final-answer-critical false claim about how the standard moves `R`, `U`, `B`, or `L` permute stickers, face labels, rows, columns, or front-face sticker provenance. Mark this `true` when the response's final front-face sticker count or final front-face grid is inconsistent with standard Rubik's cube notation. Do not mark this merely because a response is concise.
- `has_arithmetic_error`: `true` only if the response makes an arithmetic, algebraic, or equation-solving mistake after its stated sticker counts or final grid. Do not mark this just because the response uses a wrong cube-move tracking premise.
- `has_unsupported_front_face_tracking`: `true` if the response relies on a final-answer-critical claim about the final front face without showing enough sticker tracking, face-label tracking, row/column tracking, or explicit front-face provenance to justify that claim. Do not mark this merely for minor missing exposition. Do mark it when the response only asserts the final front-face counts or grid without a checkable tracking argument.
- `has_numbered_step_structure`: `true` if the response is organized into numbered steps, numbered stages, or numbered sections that separate the setup, move analysis, count, and final answer. Otherwise `false`.
- `has_readable_math_format`: `true` if the mathematical notation and displayed calculations are readable and not severely malformed. Otherwise `false`.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```json
{
  "correct_sum": <integer>,
  "acceptable_solution_ids": ["<uppercase response letters that are fully acceptable>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "extracted_final_sum": <integer or null>,
      "final_sum_correct": <true or false>,
      "acceptable_solution": <true or false>,
      "has_standard_notation_tracking_error": <true or false>,
      "has_arithmetic_error": <true or false>,
      "has_unsupported_front_face_tracking": <true or false>,
      "has_numbered_step_structure": <true or false>,
      "has_readable_math_format": <true or false>
    }
  ]
}
```

In the actual output, include seven objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, in that order. Do not write anything else to that file.
