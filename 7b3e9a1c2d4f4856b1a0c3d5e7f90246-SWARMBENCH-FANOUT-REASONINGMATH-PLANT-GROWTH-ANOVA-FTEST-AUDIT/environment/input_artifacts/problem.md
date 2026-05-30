# Problem: one-way ANOVA on the PlantGrowth experiment

## Background
A controlled greenhouse experiment recorded the dried weight (grams) of plants
grown under three conditions: a control group (`ctrl`) and two distinct treatment
regimes (`trt1`, `trt2`). Ten plants were grown under each condition, giving 30
observations in total. The full data is in `plant_growth.csv` and reproduced below.

## Question
Test, at the 5% significance level, the null hypothesis that the three condition
means are equal against the alternative that at least one differs. Use a one-way
analysis of variance (ANOVA) and report the F statistic together with its two
degrees of freedom.

## Method (one-way ANOVA, fixed effects)
With `k = 3` groups, group sizes `n_j`, and `N = 30` total observations:
- group means `ybar_j` and grand mean `ybar`;
- between-group sum of squares `SSB = sum_j n_j (ybar_j - ybar)^2`;
- within-group sum of squares `SSW = sum_j sum_i (y_ij - ybar_j)^2`;
- total `SST = SSB + SSW`;
- between df `= k - 1 = 2`, within df `= N - k = 27`;
- mean squares `MSB = SSB/(k-1)`, `MSW = SSW/(N-k)`;
- test statistic `F = MSB / MSW`, compared to `F(k-1, N-k)`.

Reject the null at level 0.05 iff `F` exceeds the upper-5% critical value of the
`F(2, 27)` distribution (equivalently, the p-value is below 0.05).

## Data (`plant_growth.csv`, 30 rows)

| group | weight |
|-------|--------|
| ctrl  | 4.17 |
| ctrl  | 5.58 |
| ctrl  | 5.18 |
| ctrl  | 6.11 |
| ctrl  | 4.50 |
| ctrl  | 4.61 |
| ctrl  | 5.17 |
| ctrl  | 4.53 |
| ctrl  | 5.33 |
| ctrl  | 5.14 |
| trt1  | 4.81 |
| trt1  | 4.17 |
| trt1  | 4.41 |
| trt1  | 3.59 |
| trt1  | 5.87 |
| trt1  | 3.83 |
| trt1  | 6.03 |
| trt1  | 4.89 |
| trt1  | 4.32 |
| trt1  | 4.69 |
| trt2  | 6.31 |
| trt2  | 5.12 |
| trt2  | 5.54 |
| trt2  | 5.50 |
| trt2  | 5.37 |
| trt2  | 5.29 |
| trt2  | 4.92 |
| trt2  | 6.15 |
| trt2  | 5.80 |
| trt2  | 5.26 |

Report the F statistic multiplied by 1000 and rounded to the nearest integer.
