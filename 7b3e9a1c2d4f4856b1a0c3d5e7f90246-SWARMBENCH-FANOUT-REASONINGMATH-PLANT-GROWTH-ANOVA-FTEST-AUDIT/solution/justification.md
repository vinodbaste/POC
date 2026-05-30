# Oracle justification

## Gold derivation (independently reproducible)
Run `python3 solution/compute_gold_stats.py` from the task root. It reads the real
PlantGrowth data and derives, with closed-form one-way ANOVA formulae:

- group means: ctrl 5.032, trt1 4.661, trt2 5.526; grand mean 5.073
- SSB = 3.76634, SSW = 10.49209, SST = 14.25843
- df = (k−1, N−k) = (2, 27)
- MSB = 1.88317, MSW = 0.38860
- **F = MSB/MSW = 4.846088**, p = 0.01591 (reject H0 at 0.05)

Headline: `gold_F_x1000 = round(4.846088 * 1000) = 4846`. Cross-checked against
`scipy.stats.f_oneway` (F = 4.846088, p = 0.01591) when SciPy is available; the
shipped script uses only the standard library (incomplete-beta for the p-value).

## final_answer_correct test
A response is `final_answer_correct = true` iff its reported F is within **±0.05**
of 4.846 **and** it reports the degrees of freedom (2, 27). Both conditions are
required: an F that is numerically close but attached to the wrong df pair (or a
statistic that is not an omnibus F at all) is wrong.

## Failure codes
- **C1** — sums of squares reported as the statistic (no division by df): F = SSB/SSW.
- **C2** — within-group df taken as N−1 (=29) or N (=30) instead of N−k (=27).
- **C3** — a two-group t-test substituted for the three-group omnibus F.
- **C4** — between-group df taken as k (=3) instead of k−1 (=2).
- **C5** — a group or observations dropped, so k≠3 or N≠30.
- **C6** — a buried arithmetic slip in a reported quantity, inconsistent with the
  data and not explained by C1–C5; detectable only by recomputation.

## Per-response rationale
| ID | reported | final | codes | why |
|----|----------|-------|-------|-----|
| A | F=4.846, df(2,27) | true | [] | exact correct ANOVA; SSB, SSW, df, MS all right; acceptable |
| B | F=4.846, df(2,27) | true | [C6] | F and df correct, but states SST=15.10 while SSB+SSW=14.2584 — an arithmetic slip in a reported quantity. Correct-but-flawed; NOT acceptable |
| C | F=5.103, df(2,27) | false | [C6] | trt2 between-term written as 2.2522 instead of 10·0.453²=2.0521 → SSB=3.9664, F=5.103. Method sound, value slipped |
| D | F=5.205, df(2,29) | false | [C2] | divides SSW by N−1=29 rather than N−k=27 |
| E | F=3.470, df(3,29) | false | [C2,C4] | between df=k=3 AND within df=N−1=29; two independent df errors co-fire |
| F | F=0.359, df(2,27) | false | [C1] | reports SSB/SSW directly without dividing each SS by its df |
| G | F=4.846, df(2,27) | true | [] | correct; opening paragraph *names* the SS-ratio and t-test shortcuts only to reject them (refutation, not commission) — neither C1 nor C3 fires; acceptable |
| H | t=2.134, df=18 | false | [C3] | performs a control-vs-trt2 two-sample t-test instead of the omnibus F; no three-group F produced |
| I | F=2.731, df(1,18) | false | [C5,C6] | drops trt1 (k=2, N=20) → C5; also reports SS_trt2=4.9842 vs the correct 1.7628 → C6 |
| J | F=3.459, df(3,27) | false | [C4,C6] | between df=k=3 → C4; reports SS_trt1=4.9772 vs the correct 5.6693 (SSW=9.80 vs 10.49) → C6 |

`acceptable_solution_ids` = responses with `final_answer_correct = true` AND
`failure_reasons = []` = **[A, G]**. B is correct on the headline but carries C6,
so it is excluded — a deliberate trap.

## Why a single agent underperforms
- **Co-fires (E, I, J):** each carries two independent codes. All-or-nothing
  per-response scoring zeroes the entire 30-pt block if even one is missed; a
  single agent multiplexing ten audits routinely drops the second code.
- **Buried slips (B, C, I, J):** C6 is invisible unless the auditor recomputes
  the cited quantity from the raw data. A single agent skimming ten transcripts
  tends to trust stated intermediates.
- **Correct-but-flawed (B):** F and df are right, so a shallow reader marks it
  acceptable and misses the SST slip.
- **Refutation trap (G):** the trigger phrases for C1 and C3 appear verbatim, but
  inside a rejection; a single agent prone to phrase-matching false-fires them.
- **Near-gold wrong (C):** F=5.103 is close to 4.846 but outside the ±0.05 band;
  easy to wave through.

A dedicated derivation sub-agent plus one focused auditor per response (with a
mechanical synthesizer) catches the co-fires and slips that single-context
attention dilution misses.

## Human-hours
Derivation + p-value by hand ≈ 1.5 h; ten audits with independent recomputation
of each cited intermediate ≈ 10 × 0.75 h = 7.5 h; reconciliation and schema
assembly ≈ 1 h. Total ≈ 10 h.
