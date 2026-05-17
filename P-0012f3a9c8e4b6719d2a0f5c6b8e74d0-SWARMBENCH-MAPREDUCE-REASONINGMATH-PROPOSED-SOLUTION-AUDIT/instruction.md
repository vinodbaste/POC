You are auditing proposed solutions to a modular arithmetic probability problem.

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
  - `/input_artifacts/proposed_solutions/response_H.tex`

Task:
1. Read the problem statement and all eight proposed solutions.
2. Determine the correct probability and the requested value of `p+q mod 1000`.
3. Determine which proposed response(s), if any, fully solve the problem.
4. Audit every proposed response A through H using the labels defined below.
5. Base the audit on the mathematical content of each response and the label definitions below.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`.
- `extracted_final_answer_mod1000`: the final boxed or clearly stated residue modulo 1000 claimed by that response, as an integer from 0 to 999. Use `null` only if the response gives no identifiable final residue. This is an extraction of the response's own final answer, not a correction.
- `primary_error_code`: the single best code describing the response's main final-answer-critical failure. Use exactly one of the following strings:
  - `"invalid_average_weight_over_mod_2197"`: the response correctly finds 624 order-2028 residues modulo 2197 but replaces the exact count over `m in {0,...,9999}` by an average or expected residue weight over modulo 2197.
  - `"rounded_density_estimate_for_partial_range"`: the response correctly reduces to counting primitive residues in an initial partial interval, but estimates that partial count by density/rounding rather than exact enumeration.
  - `"wrong_factorization_and_crt_model"`: the response uses an incompatible factorization of 2197 and solves a CRT/order problem for the wrong modulus structure.
  - `"unsupported_count_and_wrong_sample_size"`: the response recognizes the order condition but does not compute the count of valid residues and also uses the wrong sample-space denominator or otherwise leaves the final numerical count unsupported.
  - `"wrong_totient_zero_probability"`: the response computes the unit-group size/totient incorrectly and concludes no element can have order 2028.
  - `"single_period_probability_from_uniformity"`: the response correctly finds the single-period primitive-root count 624 but uses the one-period probability or a uniformity assumption instead of the exact 10000-slot count.
  - `"wrong_phi_2028_and_rounded_range_count"`: the response miscomputes `phi(2028)` and also estimates the partial initial interval by rounding/density.
  - `"ignores_strict_10000_slot_range"`: the response notices the non-complete 10000-slot sampling range but explicitly ignores that boundary effect and uses the single-period probability anyway.
  - `"none"`: use this only for a response that fully solves the problem with no final-answer-critical error.
- `final_answer_correct`: `true` exactly when the response's final claimed residue is the correct value of `p+q mod 1000`; otherwise `false`.
- `uses_correct_factorization_2197_as_13_cubed`: `true` exactly when the response explicitly uses `2197 = 13^3` and does not replace it with an incompatible factorization in its final reasoning.
- `identifies_order_2028_condition`: `true` exactly when the response explicitly recognizes that first appearance in slot 1 on day 2028 requires the multiplicative order of `m` modulo `2197` (equivalently modulo `13^3`) to be exactly `2028`, for a unit. It is not enough to require only `m^2028 = 1`.
- `computes_primitive_root_count_624`: `true` exactly when the response correctly states that the number of order-2028 residues modulo `2197` is `phi(2028)=624`, or gives an equivalent correct primitive-root count. Otherwise `false`.
- `performs_exact_nonuniform_range_count`: `true` exactly when the response exactly accounts for the nonuniform sampling range `m in {0,...,9999}` and obtains the exact valid count `2840` or the exact probability `71/250`. It is `false` for any averaging, density, rounding, random/uniform-distribution approximation, or answer based only on a single complete residue period modulo `2197`.
- `uses_invalid_uniformity_or_average_assumption`: `true` exactly when the response relies on an expected, average, random, approximate, statistical, or uniform distribution of primitive roots across a partial interval instead of doing an exact count. Otherwise `false`.
- `has_denominator_or_sample_space_error`: `true` exactly when the response uses `9999` instead of `10000` as the number of possible initial choices, treats `m` as uniformly distributed over only `2197` residues for the final probability, or fails to divide a counted quantity by `10000` when forming the final probability. Otherwise `false`.
- `has_final_answer_critical_mathematical_error`: `true` if the response contains any false mathematical claim or invalid counting/probability argument that materially changes the final answer. This includes wrong factorization, wrong totient, wrong primitive-root count, invalid uniformity/averaging over the partial range, or an unsupported zero-probability conclusion.
- `has_calculation_error`: `true` only if the response makes an arithmetic, algebraic, factorization, totient, or equation-solving mistake after its stated premises. Do not mark this merely because the response uses an invalid uniformity assumption.
- `has_unjustified_step`: `true` if the response uses a final-answer-critical inference without adequate justification, such as asserting a partial-interval primitive-root count by approximation or giving a final numerical answer without deriving the count. Do not mark this for minor missing exposition.
- `has_stepwise_structure`: `true` if the response is organized into explicit steps, numbered stages, bullet stages, or section headings that separate the setup, number-theoretic condition, counting/probability computation, and final answer. Otherwise `false`.
- `has_proper_latex_format`: `true` if the mathematical notation is mostly valid, readable LaTeX and does not contain severe formatting errors. Otherwise `false`.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```json
{
  "correct_answer_mod1000": <integer>,
  "correct_probability_latex": "<reduced probability in LaTeX>",
  "valid_m_count": <integer>,
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "extracted_final_answer_mod1000": <integer or null>,
      "primary_error_code": "<one allowed string code>",
      "final_answer_correct": <true or false>,
      "uses_correct_factorization_2197_as_13_cubed": <true or false>,
      "identifies_order_2028_condition": <true or false>,
      "computes_primitive_root_count_624": <true or false>,
      "performs_exact_nonuniform_range_count": <true or false>,
      "uses_invalid_uniformity_or_average_assumption": <true or false>,
      "has_denominator_or_sample_space_error": <true or false>,
      "has_final_answer_critical_mathematical_error": <true or false>,
      "has_calculation_error": <true or false>,
      "has_unjustified_step": <true or false>,
      "has_stepwise_structure": <true or false>,
      "has_proper_latex_format": <true or false>
    }
  ]
}
```

In the actual output, include eight objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, in that order. Do not write anything else to that file.
