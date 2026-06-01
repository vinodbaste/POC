# Problem: one-way ANOVA on the InsectSprays experiment

## Background
An agricultural field trial recorded the number of insects surviving on
experimental units that had each been treated with one of six insecticides
(`A`, `B`, `C`, `D`, `E`, `F`). Twelve units received each spray, giving 72
observations in total. The full data is in `insect_sprays.csv` and reproduced
below.

## Question
Test, at the 5% significance level, the null hypothesis that the six spray means
are equal against the alternative that at least one differs. Use a one-way
analysis of variance (ANOVA) and report the F statistic together with its two
degrees of freedom.

## Method (one-way ANOVA, fixed effects)
With `k = 6` groups, group sizes `n_j` (here `n_j = 12` for every spray), and
`N = 72` total observations:
- group means `ybar_j` and grand mean `ybar`;
- between-group sum of squares `SSB = sum_j n_j (ybar_j - ybar)^2`;
- within-group sum of squares `SSW = sum_j sum_i (y_ij - ybar_j)^2`;
- total `SST = SSB + SSW`;
- between df `= k - 1 = 5`, within df `= N - k = 66`;
- mean squares `MSB = SSB/(k-1)`, `MSW = SSW/(N-k)` — dividing each sum of squares
  by its degrees of freedom is what turns a sum of squares into a mean square, and
  the F statistic is built from the **mean** squares, never the raw sums;
- test statistic `F = MSB / MSW`, compared to `F(k-1, N-k)`.

Reject the null at level 0.05 iff `F` exceeds the upper-5% critical value of the
`F(5, 66)` distribution (equivalently, the p-value is below 0.05).

## Data (`insect_sprays.csv`, 72 rows)

| spray | count |
|-------|-------|
| A | 10 |
| A | 7 |
| A | 20 |
| A | 14 |
| A | 14 |
| A | 12 |
| A | 10 |
| A | 23 |
| A | 17 |
| A | 20 |
| A | 14 |
| A | 13 |
| B | 11 |
| B | 17 |
| B | 21 |
| B | 11 |
| B | 16 |
| B | 14 |
| B | 17 |
| B | 17 |
| B | 19 |
| B | 21 |
| B | 7 |
| B | 13 |
| C | 0 |
| C | 1 |
| C | 7 |
| C | 2 |
| C | 3 |
| C | 1 |
| C | 2 |
| C | 1 |
| C | 3 |
| C | 0 |
| C | 1 |
| C | 4 |
| D | 3 |
| D | 5 |
| D | 12 |
| D | 6 |
| D | 4 |
| D | 3 |
| D | 5 |
| D | 5 |
| D | 5 |
| D | 5 |
| D | 2 |
| D | 4 |
| E | 3 |
| E | 5 |
| E | 3 |
| E | 5 |
| E | 3 |
| E | 6 |
| E | 1 |
| E | 1 |
| E | 3 |
| E | 2 |
| E | 6 |
| E | 4 |
| F | 11 |
| F | 9 |
| F | 15 |
| F | 22 |
| F | 15 |
| F | 16 |
| F | 13 |
| F | 10 |
| F | 26 |
| F | 26 |
| F | 24 |
| F | 13 |

Report the F statistic multiplied by 1000 and rounded to the nearest integer.
