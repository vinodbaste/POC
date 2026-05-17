You are auditing proposed solutions to a sparse Gaussian mixture detection problem.

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

Task:
1. Read the problem statement and all six proposed solutions.
2. Independently determine which of tests A, B, and C have asymptotic power tending to 1 at fixed size alpha = 0.05.
3. Determine which proposed response(s), if any, fully and rigorously solve the problem.
4. Audit every proposed response A through F using the labels defined below.
5. Do not decide correctness by majority vote among the proposed responses. Independently adjudicate the sparse-mixture detection boundary, the mean-test behavior, and the maximum-test behavior.
6. Use the problem's requested final-answer convention: a JSON list of uppercase letters, alphabetically ordered, for any list of tests or response IDs.
7. Do not modify any files in `/input_artifacts`, `/tests`, or `/solution`.

Mathematical issues that must be adjudicated independently:
- Whether the one-sided z-test based on the sample mean has enough aggregate mean shift to overcome the standard noise level.
- Which Donoho-Jin/Ingster sparse-mixture detection boundary applies in the beta range given in the problem.
- Whether the maximum test succeeds or fails after correctly accounting for the maximum over the nonnull coordinates, not just comparing one signal mean with the null maximum level.
- How the given numerical values of beta and r fall relative to the applicable boundary or equivalent maximum-test condition.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`.
- `extracted_final_answer_letters`: the final answer claimed by that response, extracted as a JSON list of uppercase letters chosen from `"A"`, `"B"`, `"C"`. Use `null` only if the response gives no identifiable final answer. This field is an extraction of the response's own final answer, not a correction.
- `final_answer_correct`: `true` exactly when the response's final claimed list matches the independently correct answer to the original problem; otherwise `false`.
- `test_a_conclusion_correct`: `true` exactly when the response's conclusion about Test A matches the correct mathematical adjudication; otherwise `false`.
- `uses_correct_donoho_jin_boundary`: `true` exactly when the response uses or clearly states the correct Donoho-Jin/Ingster boundary formula or an exactly equivalent condition for the beta range and parameterization in this problem. Mark `false` for using a boundary from the wrong beta range, using an unrelated sufficient condition, or reparameterizing beta or r in a way that changes the meaning of the problem.
- `boundary_numeric_value_correct`: `true` exactly when the response computes the applicable boundary value for the given beta correctly, either exactly or to a reasonable decimal approximation. Otherwise `false`.
- `compares_r_to_boundary_correctly`: `true` exactly when the response correctly compares the given r to the applicable boundary and draws the correct detectability conclusion from that comparison. Otherwise `false`.
- `test_b_conclusion_correct`: `true` exactly when the response's conclusion about Test B, the maximum test, matches the correct mathematical adjudication. Otherwise `false`.
- `test_c_conclusion_correct`: `true` exactly when the response's conclusion about Test C, Higher Criticism, matches the correct mathematical adjudication. Otherwise `false`.
- `has_final_answer_critical_math_error`: `true` if the response contains a final-answer-critical false theorem statement, false boundary condition, wrong limiting/extreme-value comparison, wrong asymptotic scaling, or invalid reasoning step. This combines both reasoning error and untrue mathematical claim.
- `has_calculation_error`: `true` only if the response makes an arithmetic, algebraic, exponent-sign, or equation-solving mistake after its stated premises. Do not mark this merely because the response starts from a false theorem or wrong boundary formula.
- `has_unjustified_step`: `true` if the response uses a final-answer-critical inference without adequate support and that problem is not already just an explicit false mathematical claim. Do not mark this for minor missing exposition.
- `has_stepwise_structure`: `true` if the response is organized into explicit steps, numbered stages, bullet stages, section headings, or a table that separates setup, test-by-test analysis, boundary input, and final answer. Otherwise `false`.
- `has_proper_latex_format`: `true` if the mathematical notation is mostly valid, readable LaTeX and does not contain severe formatting errors. Mark `false` if substantial mathematical notation is written using HTML tags or non-LaTeX markup instead of LaTeX.

A response is a fully correct solution only if it gives the correct final answer to the original problem, correctly handles all three tests, uses the correct sparse-mixture boundary or an equivalent valid maximum-test argument where relevant, and has no final-answer-critical mathematical, calculation, or unjustified-step error.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "correct_answer_letters": ["<uppercase test letters in alphabetical order>"],
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "detection_boundary_latex": "<applicable boundary value for the given beta in standard LaTeX>",
  "per_response_assessment": [
    {
      "response_id": "A",
      "extracted_final_answer_letters": ["<uppercase test letters>"] or null,
      "final_answer_correct": <true or false>,
      "test_a_conclusion_correct": <true or false>,
      "uses_correct_donoho_jin_boundary": <true or false>,
      "boundary_numeric_value_correct": <true or false>,
      "compares_r_to_boundary_correctly": <true or false>,
      "test_b_conclusion_correct": <true or false>,
      "test_c_conclusion_correct": <true or false>,
      "has_final_answer_critical_math_error": <true or false>,
      "has_calculation_error": <true or false>,
      "has_unjustified_step": <true or false>,
      "has_stepwise_structure": <true or false>,
      "has_proper_latex_format": <true or false>
    }
  ]
}

In the actual output, include six objects in `per_response_assessment`, one for each response A, B, C, D, E, F, in that order. Do not write anything else to that file.
