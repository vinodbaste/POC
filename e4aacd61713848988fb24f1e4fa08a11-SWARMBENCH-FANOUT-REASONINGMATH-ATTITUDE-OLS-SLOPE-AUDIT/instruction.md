# OLS rating-on-complaints fit: independent derivation and a twelve-way solution review

## Your mandate
You are the senior statistician signing off a regression QA queue. Thirty real
departments were scored for how well they handle employee complaints (`complaints`)
and for their overall approval `rating`; twelve AI assistants were each handed that
data and told to fit the ordinary-least-squares line predicting rating from
complaints and to quote the slope together with a 95% confidence interval. Two
deliverables fall to you:

1. Work out the correct fit independently, from scratch, using every one of the
   thirty rows.
2. Sit in judgement on all twelve submissions — rule each one's headline answer
   right or wrong, and tag the precise collection of defects it contains.

## Files provided (all under `/workspace/input_artifacts/`)
- `attitude.csv` — the canonical thirty `rating,complaints` rows; treat this as ground truth.
- `problem.md` — restates the regression brief, the OLS recipe, and the data grid.
- `provenance.md` — where the data came from, plus context on the submissions.
- `proposed_solutions/response_A.md` through `response_L.md` — the twelve write-ups
  awaiting review. These are unfiltered model transcripts: expect a mix of clean
  work, outright mistakes, and answers that reach the right number by the wrong
  route. None of them ship with a marking scheme.

## Step 1 — Establish the reference fit
Regress `rating = beta0 + beta1*complaints` by OLS across the full set of thirty
points, on the raw scale, discarding nothing:
- means `xbar = mean(complaints)` and `ybar = mean(rating)`;
- centered sums `Sxx = sum((x-xbar)^2)`, `Syy = sum((y-ybar)^2)`,
  `Sxy = sum((x-xbar)(y-ybar))`;
- slope `beta1 = Sxy/Sxx` — be careful, this is **neither** the correlation
  `r = Sxy/sqrt(Sxx*Syy)` **nor** the flipped fit `Sxy/Syy` — and intercept
  `beta0 = ybar - beta1*xbar`;
- residual spread `SSE = sum((y - beta0 - beta1*x)^2)`, degrees of freedom
  `df = n-2 = 28`, and `s = sqrt(SSE/df)`;
- slope error `se(beta1) = s/sqrt(Sxx)`, giving the interval
  `beta1 +/- t*(0.975, 28) * se(beta1)`.

Multiply the slope by 1000, round to the nearest whole number, and report it as
`gold_slope_x1000`.

## Step 2 — Rule on each submission
Resolve two things for every letter A..L:

**(a) Is the headline answer right? (`final_answer_correct`)** Mark it `true` only
when all three hold: the quoted slope sits within **+/- 0.03** of yours, the quoted
intercept within **+/- 0.3** of yours, and both reported 95% CI endpoints within
**+/- 0.1** of yours. Any miss makes it `false`.

**(b) Which defects are present? (`failure_reasons`)** Record the SET of codes the
write-up genuinely commits:

- **F1 — axes reversed.** The fit regresses complaints onto rating, swaps x and y,
  or divides the cross-product by `Syy` rather than `Sxx`; the slope collapses
  toward 0.903.
- **F2 — correlation passed off as the slope.** The figure reported as the slope is
  actually Pearson `r` (~0.825) or the `R^2` (~0.681).
- **F3 — intercept suppressed.** The line is forced through the origin, fitting
  `rating = beta1*complaints` with `beta1 = sum(xy)/sum(x^2)` (~0.962).
- **F4 — wrong interval multiplier.** The 95% CI is built with the normal value
  1.96 in place of the Student-t quantile `t*(0.975, n-2)`.
- **F5 — rows discarded.** The fit rests on fewer than thirty observations (say,
  after pruning "outliers"), so `n != 30`.
- **F6 — computational slip.** Some reported quantity (`Sxx`, `Sxy`, `Syy`,
  `sum(xy)`, `SSE`, `R^2`, a coefficient, or a CI endpoint) simply does not match
  the data and cannot be blamed on any choice in F1–F5. Catching it means **redoing
  the arithmetic yourself**; the write-up will state the bad figure with full
  confidence.

**How the codes fire — read closely:**
- A code applies only when the error is actually **carried out** in the working.
  Nothing is flagged for you: candidates present defective steps as though they
  were sound, so re-compute each figure and settle the code set on your own
  evidence, not on what the candidate asserts.
- A method **named only to be dismissed** ("one could regress complaints on rating
  or quote r, but that would be wrong") does **not** trigger its code — echoing a
  phrase while rejecting it is not committing the error.
- Defects **stack**: a single write-up may carry several at once (origin-forcing
  plus a 1.96 interval plus dropped rows). Enumerate them all; under all-or-nothing
  marking, one omission sinks the whole entry.
- A right number can still hide a defect — e.g., a candidate quotes the correct
  slope yet quietly assembles its CI with 1.96, earning F4 while still scoring
  `final_answer_correct = true`.
- `failure_reasons` is a SET: each code at most once, and `[]` signals a clean
  write-up.

Treat a submission as **acceptable** exactly when `final_answer_correct == true`
and `failure_reasons == []`; collect every such id into `acceptable_solution_ids`.

## Deliverable — save `/logs/agent/output.json`
Emit precisely these three top-level keys and nothing more:

```json
{
  "gold_slope_x1000": 0000,
  "acceptable_solution_ids": ["X", "Y"],
  "per_response_assessment": [
    {"response_id": "A", "final_answer_correct": true,  "failure_reasons": []},
    {"response_id": "B", "final_answer_correct": false, "failure_reasons": ["F2", "F4"]}
  ]
}
```

(STRUCTURE ONLY — the integer, the ids, and the verdicts shown are throwaway
placeholders. Do not reuse them; compute every value yourself. The
`per_response_assessment` array must hold all twelve entries A..L.)

Schema constraints (breaking any one scores 0):
- `gold_slope_x1000` must be an integer.
- `acceptable_solution_ids` must be a list of distinct ids taken from A..L.
- `per_response_assessment` must hold **exactly 12** objects, one per letter, in
  **alphabetical order A..L**.
- Every object carries only `response_id`, `final_answer_correct` (boolean), and
  `failure_reasons` (codes drawn from {F1,F2,F3,F4,F5,F6}, no repeats).
- No additional top-level keys; no additional per-entry keys.

## How grading works
`tests/judge.py` compares `/logs/agent/output.json` to the withheld oracle at
`/tests/oracle.json` over a **364-point** scale, then divides the total by 364:
- 2 pts — `gold_slope_x1000` lands within +/- 1 of the oracle integer.
- 2 pts — `acceptable_solution_ids` matches the oracle set.
- 30 pts per letter A..L, **all-or-nothing**: granted only when `response_id`,
  `final_answer_correct`, and the `failure_reasons` SET each agree with the oracle
  (12 x 30 = 360).

Any structural breach (bad keys, wrong entry count, mis-ordering, non-boolean
fields, illegal codes) closes to 0.0. An output identical to the oracle scores
1.0; short of that, scoring is capped at 0.99.
