# InsectSprays one-way ANOVA — independent computation and a twelve-way solution review

## Primary task: do the statistics first, then judge
This job has two halves and you must perform both.

**Half 1 — mathematical reasoning.** Carry out a one-way analysis of variance on a
real 72-unit experiment entirely on your own, from the raw counts, and obtain
the F statistic and its degrees of freedom. No answer is handed to you.

**Half 2 — proof review.** Twelve weaker AI assistants were each given the same
data and asked for the same ANOVA. Read every one, decide whether its headline
answer is right, and tag the exact set of methodological defects it commits.

Working directory: `/workspace`.

## What you are given (under `/workspace/input_artifacts/`)
- `insect_sprays.csv` — the authoritative 72 rows (`spray,count`), six groups of twelve.
- `problem.md` — the ANOVA brief, the fixed-effects recipe, and the data table.
- `provenance.md` — where the data comes from and how the submissions were collected.
- `proposed_solutions/response_A.md` … `response_L.md` — the twelve write-ups to
  review. They are raw transcripts: some are sound, some err in method, some reach
  a plausible number by a slip, and some report the right statistic while
  mishandling something they print along the way. None carries a grading key.

## Half 1 — your reference ANOVA
Treat `count` as the response and `spray` (A, B, C, D, E, F) as the factor, all
72 observations, nothing excluded:
- group means `ybar_j` and the grand mean `ybar`;
- between-group sum of squares `SSB = sum_j n_j (ybar_j - ybar)^2`;
- within-group sum of squares `SSW = sum_j sum_i (y_ij - ybar_j)^2`;
- degrees of freedom `df_between = k - 1` and `df_within = N - k` with `k = 6`,
  `N = 72`;
- mean squares `MSB = SSB / df_between`, `MSW = SSW / df_within` — the division by
  the degrees of freedom is what turns a sum of squares into a mean square, and the
  F statistic is built from the **mean** squares, never the raw sums;
- `F = MSB / MSW`.

Multiply F by 1000, round to the nearest whole number, and report it as
`gold_F_x1000`.

## Half 2 — adjudicate each submission
For every letter A..L settle two questions.

**(a) Is the headline answer right? (`final_answer_correct`)** Set it `true` only
when BOTH hold: the reported F is within **±0.05** of your gold F, AND the reported
degrees of freedom are exactly **(5, 66)**. Anything else — an F outside the band,
a wrong df pair, or a statistic that is not the six-group omnibus F at all — is
`false`.

**(b) Which defects are present? (`failure_reasons`)** Record the SET of codes the
write-up genuinely commits:

- **C1 — sums of squares used as the statistic.** The reported F is `SSB/SSW`
  (or otherwise skips dividing each sum of squares by its degrees of freedom),
  collapsing toward ~2.63 instead of using the mean squares.
- **C2 — within-group df wrong.** The denominator mean square divides SSW by
  `N-1` or `N` instead of `N-k` (= 66 on the full data, or, after any row drop, the
  retained count minus the number of groups); the reported within df is wrong.
- **C3 — t-test in place of the omnibus F.** The submission runs a two-group
  comparison (e.g., spray A vs spray C) and reports a t statistic, never producing
  the six-group F.
- **C4 — significance judged at the wrong level.** The omnibus F and its df are
  reported, but the write-up tests against a cutoff other than the required
  α = 0.05 one (F₀.₀₅(5, 66) ≈ 2.35) — typically the 10% cutoff ≈ 1.94, or a
  critical value read at the wrong df. When the computed F comfortably clears both
  the 5% and 10% cutoffs, this leaves the F value, the df pair, AND the reject
  decision unchanged, so it can ride on an otherwise-correct write-up. Fire it whenever the
  stated significance level or critical value is not the α = 0.05 one, **regardless
  of whether the headline F is right**.
- **C5 — group or rows dropped.** The analysis rests on fewer than six groups or
  fewer than 72 observations (e.g., a group is excluded or "outliers" are pruned),
  so `k != 6` or `N != 72`.
- **C6 — buried arithmetic slip.** Some reported quantity (a group mean, `SSB`,
  `SSW`, `SST`, a mean square, or the final F) simply does not match the data and
  cannot be blamed on any choice in C1–C5. Finding it means **redoing that
  computation yourself**; the write-up will state the wrong figure confidently.

**How to assign the codes:**
- Base every code on what the write-up *does*, not on what it claims. Since the
  transcripts carry no annotations, you have to reproduce each number from the raw
  counts before you can say which codes belong.
- Mentioning a wrong route in order to dismiss it ("one could just take SSB/SSW or
  run a t-test, but that is wrong") is not the same as taking that route — in that
  case the code stays off.
- More than one code can apply to the same write-up; for instance dropped rows
  can sit alongside a wrong within-group df or a 10%-level test. Because each response is graded
  all-or-nothing, leaving out even one applicable code forfeits its entire credit,
  so enumerate the complete set.
- The headline being numerically right does not clear every code. A write-up that
  lands the correct F on (5, 66) df yet prints a wrong `SST` still earns C6 even
  though its `final_answer_correct` is `true`.
- Treat `failure_reasons` as a set with no repeats; an empty list is the signal
  that the write-up is flawless.

Call a submission **acceptable** precisely when its `final_answer_correct` is
`true` and its `failure_reasons` is empty, and list every such id under
`acceptable_solution_ids`.

## What to write: `/logs/agent/output.json`
Hand back a JSON object with exactly these three top-level keys, no more:

```json
{
  "gold_F_x1000": 0000,
  "acceptable_solution_ids": ["X", "Y"],
  "per_response_assessment": [
    {"response_id": "A", "final_answer_correct": true,  "failure_reasons": []},
    {"response_id": "B", "final_answer_correct": false, "failure_reasons": ["C2", "C4"]}
  ]
}
```

(The block above is illustrative only — its integer, ids, and verdicts are
filler that you must replace with your own computed values, never copied. Your
`per_response_assessment` array has to list all twelve letters A..L.)

Keep the object within these limits (breaking any single one zeroes the run):
- `gold_F_x1000` is written as a plain integer.
- `acceptable_solution_ids` lists distinct letters chosen from A..L.
- `per_response_assessment` contains **exactly 12** objects, one for each letter,
  ordered **alphabetically A..L**.
- An object holds nothing but `response_id`, a boolean `final_answer_correct`, and
  `failure_reasons` whose codes come from {C1,C2,C3,C4,C5,C6} without duplicates.
- Introduce no further keys at the top level or inside an entry.

## Scoring
The grader at `/tests/judge.py` reads `/logs/agent/output.json`, lines it up
against the hidden oracle in `/tests/oracle.json`, and totals a **364-point**
scale before dividing by 364:
- 2 pts for a `gold_F_x1000` landing within ±1 of the oracle integer.
- 2 pts for an `acceptable_solution_ids` that equals the oracle set.
- 30 pts for each letter A..L, awarded **all-or-nothing** only when its
  `response_id`, `final_answer_correct`, and `failure_reasons` SET all coincide
  with the oracle (so 12 × 30 = 360).

A malformed object — wrong keys, the wrong number of entries, the wrong ordering,
a non-boolean flag, or an unrecognized code — collapses the reward to 0.0. An
output identical to the oracle scores the full 1.0; anything short of an exact
match is graded against the rubric above and capped at 0.99.
