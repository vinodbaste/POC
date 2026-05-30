# instruction.md

You are auditing raw AI-generated proposed solutions to a tree path-decomposition counting problem. The problem asks for the number of distinct lexicographically-ordered arrays of unordered vertex pairs `(A_i, B_i)` whose simple paths in a given tree partition the edge set, with the count reported modulo a prime.

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
  - `/input_artifacts/proposed_solutions/response_I.md`

Verification:
- Your final report at `/logs/agent/output.json` is graded by an LLM judge that compares it field-by-field against the gold oracle stored at `/tests/oracle.json`. Each per-response audit (`response_id`, `final_answer_correct`, exact `failure_reasons` set) is graded as a single all-or-nothing unit, so a single mis-attributed code costs the whole audit.

Task:
1. Read the problem statement and all nine proposed solutions.
2. Independently determine the gold value `correct_answer` of the count modulo the prime stated in the problem. You must derive this number yourself; no formula, invariant, or numerical hint is supplied to you here.
3. Use the problem's path-decomposition condition exactly as stated: the unordered pairs are listed in strict lexicographic order, every pair `(A_i, B_i)` satisfies `1 <= A_i < B_i <= N`, and the simple tree-paths between the pairs must partition the edge set (each edge in exactly one path).
4. For each proposed response, check whether the response's final stated value of the count modulo the prime equals the gold value AND whether its derivation is mathematically valid: a correct counting method (formula, recurrence, or DP that genuinely computes the path-partition count), correct degree information for the given tree, and correct numerical evaluation, including modular reduction.
5. For each proposed response A through I, audit whether its mathematical reasoning is correct and identify the concrete failure reason(s) if incorrect.
6. Do not decide correctness by majority vote among the proposed responses. Independently solve the problem first, then audit each response against your own result.

Allowed failure reason codes (each code applies ONLY when its trigger is concretely present in that single response's text):

- `wrong_formula`
  - TRIGGER: the response derives or applies an incorrect closed-form expression, recurrence, algorithm, or invariant for the count of valid arrays. Examples include counting spanning trees of the tree, applying a Catalan-number identity, claiming the count equals a product of double factorials such as `(d_v - 1)!!` instead of the correct involution / partial-matching count, asserting that the only valid decomposition is "every edge as its own length-1 path" (which would force the count to `1`), running a greedy single-decomposition algorithm and reporting its size as the count, or setting up a tree DP whose state transitions do not actually reproduce the correct count (and would already disagree on small examples).
- `arithmetic_error`
  - TRIGGER: the response uses the correct counting method (the involution-product formula or any equivalent reformulation), uses the correct degree multiset for this tree, but mis-evaluates a single numerical step. The canonical manifestation here is a slip in the modular reduction step of the final product. Apply only when `wrong_formula` does not also fire.
- `invalid_or_incomplete_justification`
  - TRIGGER: the response gives unsupported numerical claims, omits a proof of why its formula is correct, hand-waves over the count of decompositions, stops at a symbolic placeholder such as `f(N)` without computing it, or is truncated mid-computation before committing to a final number. This code applies even when the response's stated final value happens to equal the gold value.
- `final_answer_error`
  - TRIGGER: the response's final stated value modulo the prime is not equal to the gold value, including the case where the response never commits to a concrete integer.

Per-response application rules:
- A response receives the empty `failure_reasons` list (and `final_answer_correct = true`) exactly when its final stated value modulo the prime equals the gold value AND its derivation is mathematically valid: a correct closed-form expression or DP that genuinely computes the path-partition count, correct degrees for the given tree, and correct numerical evaluation including modular reduction. A response whose method does not actually compute the count (e.g. because the underlying DP disagrees with the answer on small examples, or because the algorithm only produces one decomposition rather than counting all) does not establish correctness, even when the boxed final number happens to coincide with the gold value.
- Otherwise, include EVERY applicable concrete failure reason and NO inapplicable reason. Extra failure reasons and missing failure reasons are both wrong.

Disambiguation rules (apply uniformly to every response; these resolve overlap and tie-break cases):

1. `final_answer_error` is MANDATORY whenever the response's final stated value modulo the prime is not equal to the gold value, including when the response never commits to a concrete integer. The presence of any other failure code does NOT exempt the response from `final_answer_error`.

2. `wrong_formula` fires only when the response commits to a specific incorrect closed-form expression, recurrence, DP, or algorithm. If the response correctly states the right formula or recurrence but never finishes computing the value, do NOT fire `wrong_formula` — use `invalid_or_incomplete_justification` (and `final_answer_error`) only. Conversely, if the response commits to an incorrect formula, `wrong_formula` fires even when the response also stops short of a numerical answer (in which case combine with `invalid_or_incomplete_justification`).

3. `arithmetic_error` is mutually exclusive with `wrong_formula`. Decide which one applies by sanity-checking the response's stated method on at least one small tree (a path on three vertices and a star with three leaves are the canonical tests). Compute the path-decomposition count of the small tree yourself, directly from the problem definition, without relying on any formula stated in any response. If the response's method does not reproduce the small-tree count, classify as `wrong_formula`. If the response's method reproduces small-tree counts but the response slips on the full-tree numerical evaluation only (e.g. a bad multiplication or modular reduction), classify as `arithmetic_error`. When in doubt, prefer `wrong_formula`.

Output field definitions:
- `correct_answer`: a single integer in `[0, prime)` giving the verified count of valid arrays modulo the prime stated in the problem. The verifier checks that this integer equals the gold integer.
- `acceptable_solution_ids`: the list of response letters (each one of `"A"` through `"I"`) for which `final_answer_correct` is `true` and `failure_reasons` is empty. May be the empty list. The verifier compares this list to the oracle list as an unordered set.
- `per_response_assessment`: a list of nine audit objects, one for each response in order A, B, C, D, E, F, G, H, I.

Per-audit field definitions:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `final_answer_correct`: `true` exactly when the response gives the correct value modulo the prime AND its derivation is mathematically valid as defined above. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes. Use an empty list exactly when `final_answer_correct` is `true`. If the response is wrong, include every applicable concrete failure reason and no inapplicable reason.

Important scoring note:
The response audit is evaluated as an exact audit. Extra failure reasons and missing failure reasons are both wrong. Do not include a broad reason unless it is genuinely needed to explain why that response is incorrect.

---

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```json
{
  "correct_answer": <integer>,
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

In the actual output, include nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that order. Do not write anything else to that file.
