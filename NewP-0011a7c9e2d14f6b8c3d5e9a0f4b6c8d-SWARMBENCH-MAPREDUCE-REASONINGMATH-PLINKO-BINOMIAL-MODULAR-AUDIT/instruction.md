You are auditing proposed solutions to a finite combinatorics and modular arithmetic problem.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem_statement.md`
- Proposed solution files:
  - `/input_artifacts/proposed_solutions/response_A.md`
  - `/input_artifacts/proposed_solutions/response_B.md`
  - `/input_artifacts/proposed_solutions/response_C.md`
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`
  - `/input_artifacts/proposed_solutions/response_G.md`
  - `/input_artifacts/proposed_solutions/response_H.md`
  - `/input_artifacts/proposed_solutions/response_I.md`

Task:
1. Read the problem statement and all nine proposed solutions.
2. Determine the correct value of the requested path count modulo 1000.
3. Determine which proposed response(s), if any, correctly solve the problem.
4. Audit every proposed response A through I using the labels defined below.
5. Write extracted final answers and extracted path-count formulas in readable mathematical notation. Standard LaTeX is preferred, and equivalent binomial notations may be normalized by the verifier.
6. Determine the correct path-counting and modular arithmetic independently, then audit each response against the correct mathematics.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `extracted_final_answer_latex`: the final residue modulo 1000 claimed by that response, written as a LaTeX-style integer string or a plain integer string such as `"$42$"` or `"42"`. Use `null` only if the response gives no identifiable final residue. This field is an extraction of the response's own final answer, not a correction.
- `extracted_path_count_latex`: the binomial coefficient or path-count expression claimed by that response, written as a LaTeX-style integer string or a plain integer string such as `"$\binom{n}{k}$"`. Use `null` only if the response gives no identifiable path-count expression. This field is an extraction of the response's own formula, not a correction.
- `final_answer_correct`: `true` exactly when the response's final claimed residue is congruent to the correct answer modulo 1000; otherwise `false`.
- `path_count_setup_correct`: `true` exactly when the response correctly models the chip as taking one diagonal move per unit decrease in height and derives the corresponding binomial coefficient using the correct path model using the correct counts of left and right diagonal moves. Mark `false` if the response treats diagonal moves as separate horizontal and vertical moves, uses an incorrect total number of moves, forbids valid intermediate x-coordinates without justification, or otherwise uses an incorrect path model.
- `has_p_adic_or_modular_error`: `true` if the response contains a final-answer-critical error in Legendre/Kummer/Lucas reasoning, p-adic valuations, reduced factorial computations modulo 5 or 125, modular inverses, direct modular computation, or a claimed modular residue. Also mark `true` when the response asserts a wrong modular result from an unspecified computational tool.
- `has_crt_or_final_reduction_error`: `true` if the response incorrectly combines congruences with the Chinese Remainder Theorem, reduces residues incorrectly, or gives a final residue that contradicts its own stated congruences. Do not mark this merely because CRT is correctly applied to an earlier wrong congruence.
- `has_unsupported_computational_claim`: `true` exactly when the response contains an explicit final-answer-critical claim introduced by a black-box or unsupported assertion phrase such as known result, careful computation, computational verification, direct computation, computational tool, library, Wolfram, Python, or calculator, or does not justify the final-answer-critical computation for that claimed value; otherwise `false`.
- `has_stepwise_structure`: `true` if the response is organized into explicit steps, numbered stages, bullet stages, or section headings that separate setup, computation, and final answer. Otherwise `false`.
- `has_proper_latex_format`: `true` if the mathematical notation is mostly valid, readable LaTeX and does not contain severe formatting errors. Otherwise `false`.

Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "correct_answer_latex": "<correct residue in standard LaTeX>",
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "extracted_final_answer_latex": "<standard LaTeX residue or null>",
      "extracted_path_count_latex": "<standard LaTeX expression or null>",
      "final_answer_correct": <true or false>,
      "path_count_setup_correct": <true or false>,
      "has_p_adic_or_modular_error": <true or false>,
      "has_crt_or_final_reduction_error": <true or false>,
      "has_unsupported_computational_claim": <true or false>,
      "has_stepwise_structure": <true or false>,
      "has_proper_latex_format": <true or false>
    }
  ]
}

In the actual output, include nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that order.


Arithmetic cross-check requirement:
Before setting `correct_answer_latex`, independently verify the final residue modulo 1000. You may use exact integer arithmetic, such as a short Python computation of the relevant binomial coefficient modulo 1000, as a cross-check against any hand p-adic or CRT derivation. Set `correct_answer_latex` to the final residue modulo 1000 for the original problem.
Modulo-1000 cross-check note:
Since $1000=8\cdot125$, a valid way to verify the final residue is to check congruences modulo $8$ and modulo $125$ and combine them using the Chinese Remainder Theorem. Use this as a consistency check when evaluating CRT or final-reduction errors.


Top-level field definitions:
- `correct_answer_latex`: the final residue modulo 1000 for the original Plinko problem, written as a LaTeX-style integer string or a plain integer string.
- `acceptable_solution_ids`: the list of response IDs whose proposed solutions fully solve the original problem. Include a response ID exactly when that response has `final_answer_correct = true`, `path_count_setup_correct = true`, `has_p_adic_or_modular_error = false`, `has_crt_or_final_reduction_error = false`, and `has_unsupported_computational_claim = false`. Use an empty list if no proposed response is fully correct.

