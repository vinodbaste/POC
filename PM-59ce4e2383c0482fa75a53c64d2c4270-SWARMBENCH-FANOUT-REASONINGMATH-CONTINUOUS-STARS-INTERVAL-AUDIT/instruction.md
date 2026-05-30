# instruction.md

You are auditing raw AI-generated proposed solutions to a combinatorial interval-reconstruction reasoning problem (the "continuous-stars" visibility problem).

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
  - `/input_artifacts/proposed_solutions/response_G.md`
  - `/input_artifacts/proposed_solutions/response_H.md`

Verification:
- Your final report at `/logs/agent/output.json` is graded by an LLM judge that compares it field-by-field against the gold oracle stored at `/tests/oracle.json`. Each per-response audit (`response_id`, `final_answer_correct`, exact `failure_reasons` set) is graded as a single all-or-nothing unit, so a single mis-attributed code costs the whole audit.

Task:
1. Read the problem statement and all eight proposed solutions.
2. Independently determine the correct minimum number of distinct stars `m`, the correct maximum number of distinct stars `M`, and the correct value of `m + M` for the given visibility array `A`. You must derive both extremal claims yourself; no formula or invariant is supplied to you here.
3. Use the contiguous-interval visibility condition exactly as stated in the problem: every star is visible on a single interval `[L, R]` with `1 <= L <= R <= N`, and length-1 intervals (`L = R`) are allowed.
4. For each proposed response, check whether the response's claimed final value of `m + M` equals the gold value AND whether its extremal reasoning is mathematically valid, including any explicit construction it offers as a proof of achievability.
5. For each proposed response A through H, audit whether its mathematical reasoning is correct and identify the concrete failure reason(s) if incorrect.
6. Do not decide correctness by majority vote among the proposed responses. Independently solve the problem first, then audit each response against your own result.

Allowed failure reason codes (each code applies ONLY when its trigger is concretely present in that single response's text):

- `wrong_minimum_formula`
  - TRIGGER: the response derives or applies an incorrect closed-form expression or invariant for the minimum number of stars (for example, claims that the minimum equals a single global statistic of `A` such as its maximum entry or its length, claims `m = 1`, or assigns the expression that should compute `m` to `M` instead).
- `wrong_maximum_formula`
  - TRIGGER: the response derives or applies an incorrect closed-form expression or invariant for the maximum number of stars (for example, claims that the maximum equals the number of nights, equals the maximum entry of `A`, or follows from a fabricated adjacent-min identity, or assigns the expression that should compute `m` to `M` instead).
- `arithmetic_error`
  - TRIGGER: the response uses correct extremal closed-form expressions and correct optimality arguments for both `m` and `M` but evaluates a numerical value incorrectly (for example, mis-adds a single term in one of the relevant sums). Apply only when neither `wrong_minimum_formula` nor `wrong_maximum_formula` fires.
- `ignored_continuity_constraint`
  - TRIGGER: the response implicitly allows stars to disappear and later reappear, treats stars as independent per-night events, or otherwise violates the requirement that every star is visible on a single contiguous interval `[L, R]`. The most common manifestation is claiming a single star can simultaneously account for varying nightly counts.
- `invalid_or_incomplete_justification`
  - TRIGGER: the response gives unsupported numerical claims, omits a proof of optimality for either extremum, stops at qualitative narration without deriving a concrete value, OR offers an explicit achievability construction that does not in fact reproduce `A` and provides no other rigorous achievability argument. This code applies even when the response's stated `m + M` happens to equal the gold value.
- `final_answer_error`
  - TRIGGER: the response's final stated value of `m + M` is not equal to the gold value.

Per-response application rules:
- A response receives the empty `failure_reasons` list (and `final_answer_correct = true`) exactly when its stated value of `m + M` equals the gold value AND its extremal reasoning for both `m` and `M` is mathematically valid: correct closed-form expressions, valid optimality arguments, and either a verified explicit construction that reproduces `A` or an explicit, rigorous, implicit-construction argument that does so. A response whose listed construction does not actually reproduce `A` does not establish achievability and does not receive the empty failure list, even when the boxed final number matches.
- Otherwise, include EVERY applicable concrete failure reason and NO inapplicable reason. Extra failure reasons and missing failure reasons are both wrong.
- Always include `final_answer_error` when the stated `m + M` is wrong, even if the structural reasoning for one extremum is valid (as in a pure arithmetic mistake).
- Do not include `arithmetic_error` together with `wrong_minimum_formula` or `wrong_maximum_formula` for the same response: pure arithmetic mistakes are scoped to responses that otherwise use the correct method for both extrema.

Output field definitions:
- `correct_values.m`, `correct_values.M`, `correct_values.m_plus_M`: integers giving your verified minimum, maximum, and their sum for the given array `A`. The verifier checks that `m + M = m_plus_M` and that all three match the gold integers.
- `acceptable_solution_ids`: the list of response letters (each one of `"A"` through `"H"`) for which `final_answer_correct` is `true` and `failure_reasons` is empty. May be the empty list. The verifier compares this list to the oracle list as an unordered set.
- `per_response_assessment`: a list of eight audit objects, one for each response in order A, B, C, D, E, F, G, H.

Per-audit field definitions:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`.
- `final_answer_correct`: `true` exactly when the response gives the correct value of `m + M` AND its extremal reasoning is mathematically valid as defined above. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes. Use an empty list exactly when `final_answer_correct` is `true`. If the response is wrong, include every applicable concrete failure reason and no inapplicable reason.

Important scoring note:
The response audit is evaluated as an exact audit. Extra failure reasons and missing failure reasons are both wrong. Do not include a broad reason unless it is genuinely needed to explain why that response is incorrect.

---

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```json
{
  "correct_values": {
    "m": <integer>,
    "M": <integer>,
    "m_plus_M": <integer>
  },
  "acceptable_solution_ids": ["<uppercase response letters whose final_answer_correct is true>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": <true or false>,
      "failure_reasons": ["<zero or more allowed failure reason codes>"]
    }
  ]
}
```

In the actual output, include eight objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, in that order. Do not write anything else to that file.
