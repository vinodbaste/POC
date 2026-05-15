# OlymMATH Combinatorics — Multi-Model Audit

You are auditing fifteen model-produced solutions to a single olympiad-level combinatorics problem. Fifteen different language models were each asked the same problem and produced their own written solutions. Your job is to read every candidate solution, judge correctness, identify the first fatal mathematical error in each incorrect solution, and produce a structured cross-solution audit report.

You are NOT solving the problem from scratch — you are auditing existing solutions against the standard of mathematical correctness.

## Working environment

- Working directory: `/workspace`
- Candidate solutions: `/input_artifacts/response_A.md` through `/input_artifacts/response_O.md` (15 files, one per candidate model).
- Provenance metadata (model name, extracted final answer, ground-truth correctness label, token count per candidate) is in `/input_artifacts/provenance.json` for reference. The `correctness_groundtruth` field in provenance is from the source dataset (RUC-AIBOX/OlymMATH-eval) and reflects whether the candidate's extracted final answer matches the gold; it does NOT directly say whether the candidate's proof is valid.
- Write your final audit to `/logs/agent/output.json`.

## The problem each candidate solved

The fifteen candidate models were each given the following olympiad-level problem verbatim:

> **Problem (OlymMATH-EASY-0-EN, Combinatorics).** Given a non-negative integer sequence $\{a_n\}$ satisfying $a_1 = 2016$, $a_{n+1} \le \sqrt{a_n}$, and if the number of terms is at least 2, then any two terms in the sequence are not equal. Find the number of such sequences $\{a_n\}$.

The gold final answer is the integer **948**. The standard solution uses the recurrence $f(n) = 1 + \sum_{k=0}^{\lfloor\sqrt{n}\rfloor} f(k)$ with $f(0) = 1$, $f(1) = 2$; computes $S(m) = \sum_{k=0}^m f(k)$ up to $m=44$ (since $\lfloor\sqrt{2016}\rfloor = 44$); and concludes $f(2016) = 1 + S(44) = 1 + 947 = 948$.

## What you must do

For each candidate solution in `/input_artifacts/`:

1. Read the candidate's full response.
2. Identify the **extracted final answer** the candidate boxed or stated as its conclusion. Record it as the literal text the candidate produced (e.g. `"948"`, `"2^{44}"`, `"4"`, or an empty string if the candidate never reached a final boxed answer).
3. Determine whether the extracted final answer equals the gold answer 948 (`final_answer_correct: true`) or not (`false`).
4. Independently audit the candidate's mathematical argument: did they set up a sensible recurrence? Are the base cases correct? Are the arithmetic steps consistent? Does the final boxed answer follow from the derivation, or is there an inconsistent leap?
5. Identify the **first fatal mathematical error** — the earliest step at which the candidate's reasoning becomes irrecoverable. For correct candidates whose proof is logically valid and complete, the first fatal error is `null`.
6. Assign **failure labels** from the controlled vocabulary below.
7. Assign **domain-specific labels** from the combinatorics-specific vocabulary below.
8. Judge **repairability**.

Then produce a single cross-solution summary describing common failure modes, listing candidates whose extracted answer is wrong but whose recurrence setup was correct (arithmetic-only errors), listing candidates whose entire approach is incoherent, and naming the single best candidate solution.

## Output format

Write your final answer to `/logs/agent/output.json` in this exact JSON structure. Every key must be present. Field names, types, and allowed values must match exactly.

```json
{
  "problem_id": "olymmath-easy-0-en-combinatorics-audit",
  "gold_final_answer": "948",
  "solution_audits": [
    {
      "solution_id": "<string — single uppercase letter A..O matching the response file>",
      "extracted_answer": "<string — the literal final answer the candidate stated; use empty string \"\" if no answer reached>",
      "final_answer_correct": <bool>,
      "verdict": "<one of: correct | partially_correct | incorrect>",
      "logical_chain_valid": <bool>,
      "proof_complete": <bool>,
      "contains_wrong_math_claim": <bool>,
      "first_fatal_error": {
        "location": "<string — short description of where the error appears, e.g. \"final summation step where S(44) is reported as 1251 instead of 947\">",
        "error_type": "<string — one of the allowed failure_labels>",
        "explanation": "<string — 1–3 sentences describing the mathematical reason the step is wrong>"
      },
      "failure_labels": ["<string>", "..."],
      "domain_specific_labels": ["<string>", "..."],
      "repairability": "<one of: minor_fix | major_rewrite | impossible_from_current_solution | n/a>",
      "brief_assessment": "<string — 1–3 sentences summarizing the solution's quality>"
    }
  ],
  "cross_solution_summary": {
    "common_failure_modes": ["<string>", "..."],
    "solutions_with_correct_recurrence_wrong_arithmetic": ["<solution_id>", "..."],
    "solutions_with_incoherent_or_truncated_reasoning": ["<solution_id>", "..."],
    "solutions_relying_on_unsupported_pattern_extrapolation": ["<solution_id>", "..."],
    "best_solution_id": "<string — the single best candidate, or \"none\" if no candidate is fully correct>"
  }
}
```

### Rules for the output

- `solution_audits` must contain exactly one entry per response file present in `/input_artifacts/` (15 entries: A through O). Order entries alphabetically by `solution_id`.
- `extracted_answer` is the literal final boxed/stated answer from the candidate. If the candidate's derivation gives one value but they box a different value, record what they BOXED.
- `final_answer_correct = true` iff `extracted_answer` equals the gold answer 948 (literal string comparison after stripping whitespace; "948" and "948.0" both count as correct; "2^{44}" does not).
- `verdict = "correct"` requires `extracted_answer = "948"` AND the proof chain is logically valid AND complete (i.e. the recurrence is set up correctly, base cases are correct, arithmetic is consistent, and the final boxed answer follows from the derivation).
- `verdict = "partially_correct"` covers cases where the extracted answer is 948 but the proof has a logical gap or an inconsistent step, OR cases where the answer is close (e.g. off by a small constant) and the recurrence is essentially right.
- `verdict = "incorrect"` is everything else.
- `first_fatal_error` must be JSON `null` when `verdict = "correct"`. Otherwise it must be a populated object.
- `repairability = "n/a"` exactly when `verdict = "correct"`.
- `solution_id` letters in any array must use uppercase A..O.

### Allowed `failure_labels` vocabulary

Use only these strings. Multiple labels may attach to a single solution.

- `final_answer_error` — the extracted answer does not equal 948.
- `correct_answer_invalid_proof` — extracted answer is 948 but the argument does not establish it.
- `invalid_logical_step` — a specific inference does not follow from previous statements.
- `wrong_theorem_application` — a theorem or formula is invoked outside its hypotheses or in the wrong form.
- `false_math_claim` — a mathematical statement asserted by the candidate is mathematically false.
- `missing_case` — the candidate omits a required configuration, boundary case, or base case.
- `incomplete_proof` — the argument has a plausible outline but lacks necessary justification.
- `underjustified_step` — a step may be true but is asserted without sufficient argument.
- `circular_reasoning` — the argument assumes a claim equivalent to what it is trying to prove.
- `arithmetic_error` — the recurrence/computation form is correct but a specific arithmetic step is wrong.
- `pattern_extrapolation_unsupported` — the candidate leaps to a closed-form answer (typically a power of two or other "nice" number) without justification.
- `inconsistent_boxing` — the derivation produces one value but the candidate boxes a different value.
- `repetition_loop` — the candidate gets stuck repeating phrases and never reaches a conclusion.
- `notation_definition_error` — variables or definitions are misused.

### Allowed `domain_specific_labels` vocabulary

Use only these strings.

- `wrong_recurrence` — the recursive structure for $f(n)$ is set up incorrectly (e.g. wrong sum bounds, wrong base case, wrong inclusion of $n$ itself).
- `correct_recurrence_wrong_arithmetic` — recurrence is right; specific $f(k)$ or $S(m)$ values are computed wrong.
- `missed_singleton_sequence` — the candidate forgets to count the length-1 sequence consisting of just (2016).
- `deterministic_chain_misconception` — the candidate believes there is only one valid sequence (e.g. always go to ⌊√⌋), so reports a count of 1.
- `power_of_two_leap` — the candidate jumps to a power-of-two answer ($2^{11}$, $2^{25}$, $2^{44}$, etc.) without computational justification.
- `off_by_factor_of_two` — the candidate's answer is half or double of 948 (e.g. 474), typically from miscounting singleton vs. non-singleton sequences.
- `off_by_small_constant` — the candidate's answer is within a few of 948 (e.g. 950, 1252 doesn't qualify here — too far).
- `distinct_term_constraint_ignored` — the candidate ignores the "all terms distinct" requirement or applies it incorrectly.
- `bounds_error` — the candidate uses the wrong upper bound for $a_2$ (e.g. uses 45 or 43 instead of 44).
- `truncated_before_conclusion` — the candidate's reasoning was cut off and they never extracted a final answer.

## Reference checklist before writing

Before writing `/logs/agent/output.json`, verify:

- 15 entries in `solution_audits`, ordered A, B, C, D, E, F, G, H, I, J, K, L, M, N, O.
- Every `solution_id` in any array is uppercase A..O.
- `first_fatal_error` is JSON `null` exactly for entries with `verdict = "correct"`.
- `repairability` is `"n/a"` exactly when `verdict = "correct"`.
- Every label in `failure_labels` and `domain_specific_labels` is from the controlled vocabulary above.
- Top-level keys are exactly: `problem_id`, `gold_final_answer`, `solution_audits`, `cross_solution_summary`. No extra top-level keys.
