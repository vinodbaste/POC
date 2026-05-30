# Numerical-verification protocol — modified IMO 2025 P4 (three-divisor fixed-point count)

This document defines a deterministic verification protocol over a finite numerical claim. Execute every step below in order. Do not skip; do not delegate to majority vote.

---

### Step 0. Preconditions

Working directory: `/workspace`. All inputs sit at `/input_artifacts/`:

- `/input_artifacts/problem.md` — modified problem statement.
- `/input_artifacts/provenance.md` — provenance for the proposed enumerations.
- `/input_artifacts/proposed_solutions/response_A.md` … `response_N.md` — fourteen raw, unedited proposed enumerations under verification.

Output destination: `/logs/agent/output.json`. Schema is the one defined in Step 6.

### Step 1. Compute `fixed_point_count`

Definitions, restated for unambiguous use:
- A *proper divisor* of n is a positive divisor of n strictly less than n. (n itself is NOT a proper divisor of n.)
- For n with at least three proper divisors, define `s(n) := d_1 + d_2 + d_3` where d_1 > d_2 > d_3 are the three largest proper divisors of n.
- Define `fixed_point_count := |{n ∈ [4, 30] : n has at least three proper divisors AND s(n) = n}|`.

Compute `fixed_point_count` by exhaustive enumeration over n ∈ {4, 5, …, 30} — no shortcut, no early termination on the first hit.

### Step 2. Compute the five anchor quantities

Report each integer under `anchor_results`:

| Key | Definition |
|-----|------------|
| `num_valid_n_in_4_to_30` | Count of n ∈ [4, 30] with at least three proper divisors. |
| `num_n_with_s_eq_n_in_4_to_30` | = `fixed_point_count` (the main answer). |
| `num_n_with_s_gt_n_in_4_to_30` | Count with at least three proper divisors AND s(n) > n. |
| `num_n_with_s_lt_n_in_4_to_30` | Count with at least three proper divisors AND s(n) < n. |
| `s_value_for_n_24` | Numeric s(24) = sum of three largest proper divisors of 24. |

Sanity invariant (verify yourself, not part of grading): `num_valid = num_eq + num_gt + num_lt`.

### Step 3. Phrase-trigger codebook (closed vocabulary, |codes| = 4)

For every response_X.md, return a (possibly empty) subset of {F1, F2, F3, F4}. A code applies ONLY when its trigger phrase or near-verbatim paraphrase is concretely present in *that single* response's prose. Apply codes mechanically — never on majority vote.

- **F1 — INCLUDES_N_AS_PROPER_DIVISOR.** The response explicitly lists n itself among the proper divisors of n for some specific n in [4, 30]. Concrete forms: "proper divisors of 6 are 1, 2, 3, 6", "proper divisors of 8 are 1, 2, 4, 8".
- **F2 — WRONG_PROPER_DIVISOR_COUNT.** The response asserts a specific (incorrect) cardinality of the proper-divisor set of some specific n in [4, 30]. Concrete forms: "12 has 4 proper divisors", "18 has 4 proper divisors", "20 has 3 proper divisors" — i.e., any explicit numerical claim about |proper-divisors(n)| that disagrees with the true count for that n.
- **F3 — INCOMPLETE_FIXED_POINT_SET.** The response asserts that the fixed-point set in [4, 30] is strictly smaller than the truth — for example, by claiming only one specific n is a fixed point when there are more, or by giving an enumeration that explicitly excludes a fixed point that actually satisfies s(n) = n. Concrete forms: "the only fixed point is 6", "only n = 6 satisfies this", "no other fixed points exist", "n = N fails" or "N is not a fixed point" used as a load-bearing claim where the response's enumeration shows N is in fact a fixed point under the correct definition. Mechanical rule: the response makes a definitive negative claim about a specific n that the verifier independently determines to be a true fixed point.
- **F4 — SUM_ARITHMETIC_ERROR.** The response states a numerical sum `d_1 + d_2 + d_3 = X` where d_1, d_2, d_3 ARE the correct three largest proper divisors of some specific n in [4, 30] but X is the wrong numerical sum. Pure restatement of n itself as a divisor does NOT trigger F4 (that is F1).

### Step 4. Application rules (V1–V5)

- **V1.** Multi-select. The four codes are NOT mutually exclusive; co-fires of 2 or 3 codes occur. Most responses fire 0 or 1.
- **V2.** Refutation carve-out. A code does NOT fire if the trigger phrase appears only inside a passage where the response is explicitly identifying the phrase as an error. Load-bearing presence is required.
- **V3.** Evidence locality. Each code's trigger must be visible in the SAME response_X.md being audited. Cross-response inference is forbidden.
- **V4.** `final_answer_correct = true` iff the response's stated `fixed_point_count` integer equals the gold value computed in Step 1.
- **V5.** `acceptable_solution_ids` = sorted uppercase list of letters with `final_answer_correct = true` AND `failure_reasons = []`.

### Step 5. Verifier & scoring

`/tests/judge.py` reads `/logs/agent/output.json`, compares each field to the privately held `/tests/oracle.json`, and writes `reward = passed / 390` clamped to `[0, 1]`. Fail-closes to `0.0` on any IO/JSON error.

| Field | Points |
|-------|--------|
| `answer.fixed_point_count` (exact int) | 50 |
| Each of 5 anchor fields (exact int) | 10 each, 50 total |
| `acceptable_solution_ids` (set match) | 10 |
| Each of 14 per-response audits (all-or-nothing on `response_id` AND `final_answer_correct` AND `set(failure_reasons)`) | 20 each, 280 total |
| **Total** | **390** |

### Step 6. Output schema

Write `/logs/agent/output.json` with exactly these four top-level keys:

```json
{
  "answer": {
    "fixed_point_count": <int>
  },
  "anchor_results": {
    "num_valid_n_in_4_to_30": <int>,
    "num_n_with_s_eq_n_in_4_to_30": <int>,
    "num_n_with_s_gt_n_in_4_to_30": <int>,
    "num_n_with_s_lt_n_in_4_to_30": <int>,
    "s_value_for_n_24": <int>
  },
  "acceptable_solution_ids": ["<sorted uppercase letters A..N>"],
  "per_response_assessment": [
    {"response_id": "A", "final_answer_correct": <bool>, "failure_reasons": [<F-codes>]},
    ...
    {"response_id": "N", "final_answer_correct": <bool>, "failure_reasons": [...]}
  ]
}
```

`per_response_assessment` must contain exactly fourteen records in alphabetical order A through N. Do not write anything else to the file.
