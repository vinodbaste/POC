# Oracle justification

## Gold derivation (independently reproducible)
Run `python3 solution/compute_gold_stats.py` from the task root. It reads the real
InsectSprays data (6 sprays × 12 units, N = 72) and computes the one-way ANOVA from
first principles (standard library only):

- group means A = 14.500, B = 15.333, C = 2.083, D = 4.917, E = 3.500, F = 16.667;
  grand mean = 9.500
- SSB = 2668.833, SSW = 1015.167, SST = 3684.000
- df_between = k − 1 = 5, df_within = N − k = 66
- MSB = 533.767, MSW = 15.381
- **F = MSB/MSW = 34.702282**

Headline: `gold_F_x1000 = round(34.702282 * 1000) = 34702`.

## final_answer_correct test
A response is `final_answer_correct = true` iff its reported F is within **±0.05** of
34.702 **and** its degrees of freedom are exactly **(5, 66)**. An F outside the band,
a wrong df pair, or a statistic that is not the six-group omnibus F (e.g. a t
statistic) is `false`. The significance level a response uses does NOT enter this
test — F = 34.70 clears the 5% and 10% cutoffs alike, so a wrong-level write-up keeps
the same reject decision; it fires the peripheral code C4 but stays
`final_answer_correct = true` when the F and df are right.

## Failure codes
- **C1 — sums of squares used as the statistic:** reports F = SSB/SSW (signature
  2.629), skipping the division by each df.
- **C2 — within-group df wrong:** divides SSW by N−1 = 71 or N = 72 instead of
  N−k = 66 (or the retained-count minus groups after a drop); reported within df not 66.
- **C3 — t-test in place of the omnibus F:** runs a two-group comparison and reports
  a t statistic, never producing the six-group F.
- **C4 — significance judged at the wrong level:** tests against a cutoff other than
  α = 0.05 (F₀.₀₅(5,66) ≈ 2.35) — typically the 10% cutoff ≈ 1.94. Peripheral —
  F = 34.70 clears both, so F, df, and the reject decision are unchanged; fires on
  otherwise-correct work.
- **C5 — group or rows dropped:** rests on fewer than six groups or fewer than 72
  observations, so k ≠ 6 or N ≠ 72.
- **C6 — buried arithmetic slip:** a reported quantity (group mean, SSB, SSW, SST, a
  mean square, or F) does not match the data and is not explained by C1–C5;
  detectable only by recomputation.

## Per-response rationale
| ID | reported | final | codes | why |
|----|----------|-------|-------|-----|
| A | F=34.702, df (5,66), reject@.05 | true | [] | exact ANOVA; SSB/SSW/df/MS all right; tests at the right level. Acceptable |
| B | F=34.702, df (5,66), reject@**.10** | true | [C4] | F and df fully correct, but tests at the 10% level (cutoff 1.94) instead of 5%; reject decision unchanged so peripheral C4 only. Correct-but-flawed; NOT acceptable |
| C | F=**32.169**, df (5,66), @.05 | false | [C6] | uses mean squares and df 66 correctly, but reports SSW = 1095.167 where the data give 1015.167 — the slip pushes MSW to 16.593 and F to 32.169, out of band |
| D | F=**2.629**, df (5,66), reject@**.10** | false | [C1,C4] | co-fire: reports F = SSB/SSW = 2.629, skipping the mean squares (C1, loud) AND tests at the 10% level (C4, quiet) |
| E | F=**40.255**, df **(5,70)**, @**.10** | false | [C2,C4,C5] | triple: drops the two F = 26 units as outliers (C5, loud) so N = 70, divides SSW by N = 70 for MSW so within df = 70 (C2), AND tests at the 10% level (C4, quiet) |
| F | F=**37.331**, df **(5,71)**, @.05 | false | [C2] | F arithmetic fine given its choice, but divides SSW by N−1 = 71 for MSW, so within df = 71 instead of 66; df wrong so final is false, level fine |
| G | F=34.702, df (5,66), reject@.05 | true | [] | correct; opening paragraph *names* the SSB/SSW and 10%-level shortcuts only to reject them (refutation, not commission) — neither C1 nor C4 fires; acceptable |
| H | F=34.702, df (5,66), reject@.05 | true | [] | correct one-way ANOVA, plain working; acceptable |
| I | F=**26.542**, df **(4,55)**, SST=**2948.983** | false | [C5,C6] | drops spray C as "degenerate" (C5, loud) → 5 groups, N = 60, df (4,55); AND prints SST = 2948.983 where the reduced data give 2848.983 → slip (C6, quiet) |
| J | t=**8.407**, df **22**, @**.10** | false | [C3,C4,C5] | triple: runs a two-sample t-test of spray A vs C, reporting a t statistic, not the omnibus F (C3, loud); using only two of six groups (C5); AND testing at the 10% level (C4, quiet) |
| K | F=34.702, df (5,66), SST=**3584.0**, @.05 | true | [C6] | F and df correct (final true), but prints SST = 3584.0 where SSB + SSW = 3684.0 — slip in a non-headline quantity. Correct-but-flawed; NOT acceptable |
| L | t=**7.289**, df **22**, @.05 | false | [C3,C5] | runs a two-sample t-test of spray B vs D, reporting a t statistic, not the omnibus F (C3, loud); using only two of six groups (C5); level correct so no C4 |

`acceptable_solution_ids` = responses with `final_answer_correct = true` AND
`failure_reasons = []` = **[A, G, H]**. B (C4) and K (C6) are correct on the
headline but each carry one peripheral defect, so both are excluded.

## Why a single agent underperforms (gap mechanism)
The gap driver is the **peripheral code C4 (10%-level test)**, firing on **four**
responses — B, D, E, J. C4 lives in the significance-comparison line, never changes
the F, df, or the reject decision, and is easy to miss when skimming twelve
transcripts:
- On **B** it stands alone on an otherwise-perfect transcript; a single agent reads
  the correct F/df/reject and marks B acceptable, missing the "10% level" cutoff.
- On **D, E, J** it rides as a quiet secondary behind a loud primary (SSB/SSW ratio,
  dropped units, t-test). The single agent flags the loud error, concludes "wrong",
  and never audits the significance level — under-firing C4 and zeroing the block.

A second quiet code reinforces the gap: on the drop and t-test responses **E, I, J, L**
either the within df is wrong by construction (C2 on E) or only a subset of groups is
used (C5), so the secondary codes fire automatically; a skimming single agent sees the
loud primary and stops. A third axis, **C6 buried slips** on **C, I, K**, sits on one
recomputable printed quantity (SSW, SST), which single skims past while a focused
auditor recomputes it.

Reinforcing the gap:
- **Three clean acceptables (A, G, H):** G's refutation paragraph baits a phantom
  C1/C4; any false code zeroes a 30-pt block.
- **Two correct-but-flawed (B, K):** right F and df with one peripheral defect; the
  single agent marks acceptable or wrongly flips final to false.
- **Co-fires (D, E, I, J, L):** two or three independent codes each (E, J are triples).

A dedicated derivation sub-agent plus one focused auditor per response (with a
mechanical synthesizer) reads each transcript end-to-end and resolves the clean,
correct-but-flawed, and co-firing cases that single-context attention dilution
collapses.

## Human-hours
One-way ANOVA by hand (means, SSB, SSW, mean squares, F) ≈ 1.5 h; twelve audits with
independent recomputation of each cited intermediate (means, SSB, SSW, SST, df, F per
transcript) ≈ 12 × 0.6 h = 7.2 h; reconciliation of co-fires, correct-but-flawed
cases, the refutation trap, and schema assembly ≈ 2.3 h. Total ≈ 11 h.
