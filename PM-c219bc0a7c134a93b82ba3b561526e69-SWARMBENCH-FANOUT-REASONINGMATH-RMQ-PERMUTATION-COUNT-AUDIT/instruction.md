# instruction.md

## Overview

This task evaluates nine independently generated candidate proofs for a permutation-counting question driven by a range-minimum-index (RMQ) table. For `N = 15`, the table `T(l, r)` reports the *position* of the strict minimum of `P_l, P_{l+1}, …, P_r` in some permutation `P` of `{1, …, N}`. You must determine how many permutations satisfy every cell of the table and then triage each of the nine candidate answers for both numerical and methodological soundness.

## Sources and outputs

| Role | Path |
|------|------|
| Problem statement | `/input_artifacts/problem.md` |
| Provenance note for the candidate proofs | `/input_artifacts/provenance.md` |
| Candidate proofs | `/input_artifacts/proposed_solutions/response_A.md` ... `response_I.md` (nine files) |
| Your final report | `/logs/agent/output.json` |
| Gold oracle held by the verifier | `/tests/oracle.json` |

Your working directory is `/workspace`.

## Task

1. Read the problem statement and the nine candidate proofs.
2. Determine `correct_answer` — the count of permutations `P` of `{1, …, N}` consistent with the table. No formula, invariant, or numerical hint is supplied; the derivation is yours.
3. Use the problem's data exactly as written. A cell `T(l, r) = i` (with `l ≤ i ≤ r`) is a hard constraint asserting that position `i` carries the strict minimum among positions `l` through `r`; equivalently, `P_i < P_j` for every `j ∈ [l, r]` with `j ≠ i`. The count this question asks about is the number of permutations `P` of `{1, …, N}` simultaneously satisfying every cell. The count is well-defined for every table, including any table whose collected strict-min ordering constraints form a constraint system with no solution at all — in that case the count is the empty count by the question's own definition, and counting identities (Cartesian-tree binomial recursion, `N! / ∏ subtree-sizes` linear-extension formulas, block-factorial decompositions, heap-ordered tree counts) that would otherwise apply to a feasible table do not count permutations of an unsatisfiable system, so they are not the gold count in that branch and a method that nonetheless produces a non-zero value from such an identity is disqualified. A counting identity used on a feasible table must be validated on a length-2 and a length-3 table you write yourself from explicit small permutations before it is applied to the `N = 15` instance.
4. For each candidate proof, decide whether its stated integer matches your gold integer AND whether its derivation actually counts the right combinatorial object (the permutations of the given constraint system, including the empty branch when the system is unsatisfiable).
5. Audit each of `response_A.md` through `response_I.md` against your independent result. Apply the failure-code vocabulary and audit rules R1–R6 below.
6. The nine candidate proofs are not authoritative. Do not adopt a value, an identity, or a justification merely because it appears in many responses; rely only on your own derivation in step 2.

---

## Failure-code vocabulary (exactly four codes)

A code fires for a given response only when its trigger is **concretely instantiated** in that response's text — not when it is merely thematically related.

| Code | Trigger |
|------|---------|
| `wrong_formula` | The response commits to an incorrect closed-form expression, recurrence, algorithm, or invariant for the count of permutations satisfying every `T(l, r)` cell. Concrete instantiations include: claiming the table determines a unique permutation; decomposing positions into freely-permutable contiguous blocks based on a misreading of the table; appending an unjustified multiplicative correction (e.g. a `2^k` branching factor) on top of an otherwise reasonable count; using a tree-poset linear-extension identity `N! / ∏ subtree-sizes` with sizes that do not match the table; applying any tree-based or binomial recurrence that produces a value for every well-formed table without first establishing that the underlying strict-min ordering constraint system has any solution at all (such methods do not count permutations of the constraint system, so their output is not the gold count even when one happens to coincide). The standard test: compute the method on a length-2 or length-3 table by hand from the constraint definition (enumerate permutations and check each cell); if the method does not reproduce that brute-force count, the formula is wrong. |
| `arithmetic_error` | The response uses a correct method (one that genuinely counts permutations of the strict-min ordering constraint system, including correct handling of the no-solution branch) AND a correct decomposition of the given table, but slips on a single numerical step. Mutually exclusive with `wrong_formula`. |
| `invalid_or_incomplete_justification` | The response makes unsupported numerical assertions, omits a proof that its formula or recurrence counts the same combinatorial object the question asks about (i.e. permutations satisfying every `T(l, r)` cell), hand-waves over the count, stops at a symbolic placeholder without committing to a concrete integer, or is truncated mid-computation before producing a final number. Fires even when the response's stated final value happens to coincide with the gold integer. Whenever `wrong_formula` fires AND the response does not prove its committed method counts the right object, this code also fires (a wrong method is by definition unjustified as a count of the constraint-system permutations). |
| `final_answer_error` | The response's final stated value is not equal to the gold integer, including the case where the response never commits to a concrete integer. |

---

## Audit rules (apply R1 through R6 in order, per response)

**R1 — final-value comparison.** Extract each response's final stated integer from its boxed answer or terminal sentence. Set `final_answer_correct = true` iff this integer equals the gold value from step 2.

**R2 — `final_answer_error` is mandatory whenever R1 returns false.** The presence of any other code does not exempt the response from `final_answer_error`. This rule applies even when the response never commits to a concrete integer.

**R3 — co-fire: `wrong_formula` plus `invalid_or_incomplete_justification`.** Whenever a response commits to a method whose output is not the gold count of permutations satisfying the table, BOTH codes fire together. A wrong method is, by definition, an unjustified claim about the count.

**R4 — `wrong_formula` and `arithmetic_error` are mutually exclusive.** Distinguish them by running the response's stated method on a length-2 and a length-3 table you compute by hand from the constraint definition; do not rely on any formula stated in any candidate response. Disagreement with brute force ⇒ `wrong_formula`. Agreement on small instances with a final-value slip on the full table ⇒ `arithmetic_error`. When in doubt, prefer `wrong_formula`.

**R5 — `wrong_formula` may fire without a final integer.** If the response commits to an incorrect method and also truncates before producing a number, fire `wrong_formula` AND `invalid_or_incomplete_justification` (by R3) AND `final_answer_error` (by R2).

**R6 — empty `failure_reasons` is reserved for fully-correct responses.** A response receives `failure_reasons = []` iff its final stated integer equals the gold AND its method genuinely counts permutations satisfying every `T(l, r)` cell of the given table (consistent with the question's definition, including the no-solution branch when applicable), with a valid identity correctly evaluated. A method that produces a numerical value without a defensible counting argument — even one whose number happens to coincide with the gold — does not establish correctness and does not earn the empty set.

`acceptable_solution_ids` is the alphabetically-sorted list of uppercase response letters whose audit returns `final_answer_correct = true` AND `failure_reasons = []`. It may be the empty list.

---

## Scoring

The verifier reads `/logs/agent/output.json` and compares each field to the oracle stored at `/tests/oracle.json`.

- `correct_answer` — 2 points, exact integer equality.
- `acceptable_solution_ids` — 2 points, unordered set equality.
- Each of the nine per-response audits — 30 points, all-or-nothing. The 30 points are awarded only when `response_id`, `final_answer_correct`, AND the exact `failure_reasons` set all match the oracle for that response. One mis-attributed code zeroes the entire 30-point block; absent codes and extra codes carry equal penalty.
- Total — 274 points; `reward = passed / 274`.

---

## Output format

Write exactly one JSON document to `/logs/agent/output.json` and nothing else. The top-level object carries three keys: `correct_answer` (your gold integer), `acceptable_solution_ids` (an unordered set of uppercase response letters, serialized as a JSON array), and `per_response_assessment` (an array of exactly nine per-response audit objects ordered alphabetically by `response_id` from A through I).

Each per-response audit object carries three keys in this exact form:

| Key | Type | Meaning |
|-----|------|---------|
| `response_id` | string | uppercase response letter; one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"` |
| `final_answer_correct` | boolean | true exactly when this response's final stated integer equals the gold value (R1) |
| `failure_reasons` | array of strings | drawn only from the four-code vocabulary; empty exactly when R6's no-defect condition holds |

Schema skeleton (replace `<…>` placeholders with your computed values; the example below shows the shape, not the content):

```
{
  "correct_answer": <non-negative integer>,
  "acceptable_solution_ids": [<sorted uppercase letters or none>],
  "per_response_assessment": [
    {"response_id": <letter>, "final_answer_correct": <bool>, "failure_reasons": [<zero or more codes>]}
  ]
}
```
