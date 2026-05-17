You are auditing proposed solutions to a probability/random-walk asymptotics problem.

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
2. Determine the correct closed-form value of the constant $c$.
3. Determine which proposed response(s), if any, correctly solve the problem.
4. Audit every proposed response A through F using the labels defined below.
5. Write all mathematical constants in standard LaTeX closed form. Equivalent exact forms are acceptable.
6. Do not decide correctness by majority vote among the proposed responses. Independently adjudicate the conflicting theorem/asymptotic claims and then audit each response against the correct mathematics.
7. Do not modify any files in `/input_artifacts`, `/tests`, or `/solution`.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`.
- `extracted_final_answer_latex`: the final constant claimed by that response, written in standard LaTeX closed form. Use `null` only if the response gives no identifiable final constant. This field is an extraction of the response's own final answer, not a correction.
- `final_answer_correct`: `true` exactly when the response's final claimed constant is mathematically equal to the correct value of $c$; otherwise `false`.
- `has_mathematical_error`: `true` if the response contains a final-answer-critical false mathematical claim, false theorem statement, wrong limiting distribution, wrong asymptotic scaling, or invalid reasoning step. This combines both "reasoning error" and "untrue mathematical claim".
- `has_calculation_error`: `true` only if the response makes an arithmetic, algebraic, or equation-solving mistake after its stated premises. Do not mark this just because the response starts from a false theorem or wrong scaling law.
- `has_unjustified_step`: `true` if the response uses a final-answer-critical inference without adequate justification. Do not mark this for minor missing exposition; mark it only when the missing justification materially affects the solution.
- `has_stepwise_structure`: `true` if the response is organized into explicit steps, numbered stages, bullet stages, or section headings that separate the setup, theorem/asymptotic input, derivation, and final answer. Otherwise `false`.
- `has_proper_latex_format`: `true` if the mathematical notation is mostly valid, readable LaTeX and does not contain severe formatting errors. Otherwise `false`.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```json
{
  "correct_answer_latex": "<correct constant c in standard LaTeX closed form>",
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "extracted_final_answer_latex": "<standard LaTeX closed form or null>",
      "final_answer_correct": <true or false>,
      "has_mathematical_error": <true or false>,
      "has_calculation_error": <true or false>,
      "has_unjustified_step": <true or false>,
      "has_stepwise_structure": <true or false>,
      "has_proper_latex_format": <true or false>
    }
  ]
}
```

In the actual output, include six objects in `per_response_assessment`, one for each response A, B, C, D, E, F, in that order. Do not write anything else to that file.
