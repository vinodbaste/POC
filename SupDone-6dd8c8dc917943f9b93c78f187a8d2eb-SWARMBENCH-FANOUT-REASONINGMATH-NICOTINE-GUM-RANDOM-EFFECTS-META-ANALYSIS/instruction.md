You are auditing raw AI-generated proposed solutions to a random-effects
meta-analysis problem (pooling 26 nicotine-gum smoking-cessation trials).

Working directory: `/workspace`.

Input artifacts:
- Problem statement and data: `/input_artifacts/problem.md`
- Trial data (CSV): `/input_artifacts/trials.csv`
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
  - `/input_artifacts/proposed_solutions/response_J.md`
  - `/input_artifacts/proposed_solutions/response_K.md`
  - `/input_artifacts/proposed_solutions/response_L.md`

Task:
1. Read the problem statement and all 12 proposed solutions.
2. Independently solve the problem: compute the DerSimonian-Laird random-effects
   pooled odds ratio and its 95% CI using the method in `problem.md` (inverse-variance
   weights `w = 1/v`, `v = 1/a+1/b+1/c+1/d`; fixed-effect mean; `Q`; `I^2 = (Q-df)/Q`;
   `tau^2 = (Q-df)/C` with `C = sum(w) - sum(w^2)/sum(w)`; re-weight by `1/(v+tau^2)`).
   You may use the data in `trials.csv` and write your own code.
3. Determine which proposed response(s), if any, are fully correct.
4. For each proposed response A through L, audit `final_answer_correct` and
   `failure_reasons`.
5. Do not decide by majority vote. Independently solve first, then audit.

Allowed failure reason codes (phrase-triggered):

- F1 — Inverse-variance weighting error. The response weights studies by something
  other than the inverse variance `1/v`.
  - TRIGGER: weights stated as `1/se`, `1/sqrt(v)`, `1/standard_error`, by sample
    size, or an unweighted average of log odds ratios. Does NOT fire if the response
    only mentions such a scheme to reject it.

- F2 — Wrong deliverable: fixed-effect instead of the required random-effects pool.
  - TRIGGER: the response's reported headline pooled odds ratio is the fixed-effect
    (inverse-variance, `tau^2 = 0`) estimate, or it states it is reporting the
    fixed-effect model / "no random-effects needed" as its final answer.

- F3 — Naive averaging of odds ratios. The response pools by taking an arithmetic
  or unweighted mean of the per-study odds ratios on the raw scale instead of
  inverse-variance pooling on the log scale.
  - TRIGGER: the final estimate is the mean of the OR values (e.g. "mean of the 26
    odds ratios"). Does NOT fire if the response only mentions this approach to reject it.

- F4 — Heterogeneity computation error. `Q`, `I^2`, or `tau^2` is computed with a
  wrong formula, changing the random-effects weights.
  - TRIGGER: a stated heterogeneity formula or value inconsistent with
    `I^2 = (Q-df)/Q` and `tau^2 = (Q-df)/C` (e.g. `I^2 = Q/df`, `I^2 > 100%`,
    `tau^2 = (Q-df)/k` or `/df` instead of `/C`).

- F5 — Data or 2x2 table error. The response drops one or more of the 26 trials, or
  mis-constructs a 2x2 table.
  - TRIGGER: fewer than 26 trials pooled, or a wrong cell assignment such as using
    `tt`/`tc` as a cell instead of `tt-qt` / `tc-qc`, or swapping the arms.

Important scoring and selection rules:
- EXACT set match per response. Extra OR missing codes both score zero for that response.
- Apply a code only when its trigger is directly observable in that response.
- Use `[]` for failure_reasons exactly when the final answer is correct AND no
  trigger appears.
- `final_answer_correct` is true iff the response's reported random-effects pooled
  odds ratio matches the value you independently computed (within +/- 0.03) AND its
  reported 95% CI matches your computed CI (each bound within +/- 0.05).
- `acceptable_solution_ids` is the sorted uppercase list of response_ids whose
  `final_answer_correct` is true AND `failure_reasons` is empty.

Label definitions:
- response_id: one of "A", "B", ..., "L".
- final_answer_correct: boolean, per the equality test above.
- failure_reasons: a JSON list chosen only from {F1, F2, F3, F4, F5}.
- gold_random_effects_or_x100: your independently computed random-effects pooled
  odds ratio multiplied by 100 and rounded to the nearest integer (e.g. an OR of
  1.234 becomes 123).

---
## Verification

The verifier (`/tests/judge.py`) reads `/logs/agent/output.json` and grades each
field against `/tests/oracle.json`. Reward = passed / total clamped to [0, 1];
fail-closes to 0.0 on any error. Byte-identical to the oracle earns 1.0; otherwise
capped at 0.99. Per-field weights:

- gold_random_effects_or_x100: 2 pts iff it matches the true gold integer within +/- 1.
- acceptable_solution_ids: 2 pts iff set-equal.
- Per response (12 responses, 30 pts each):
  - 30 pts iff response_id + final_answer_correct + failure_reasons SET all match.
- Total = 364 points.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON shape
(the values below are placeholders, not the answer):

```
{
  "gold_random_effects_or_x100": <your computed OR x 100, integer>,
  "acceptable_solution_ids": [<uppercase response letters that are fully correct>],
  "per_response_assessment": [
    {"response_id": "A", "final_answer_correct": <true or false>, "failure_reasons": [<zero or more of F1..F5>]},
    {"response_id": "B", "final_answer_correct": <true or false>, "failure_reasons": [<zero or more of F1..F5>]}
  ]
}
```

In the actual output, include exactly 12 objects in `per_response_assessment`, one
for each response A through L, in alphabetical order. Top-level keys MUST be exactly
`gold_random_effects_or_x100`, `acceptable_solution_ids`, and
`per_response_assessment` with no extras. Do not write anything else to that file.
