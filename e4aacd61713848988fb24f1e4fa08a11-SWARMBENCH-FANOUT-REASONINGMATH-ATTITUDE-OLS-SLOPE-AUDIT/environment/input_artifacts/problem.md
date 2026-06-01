# Problem: simple linear regression of overall rating on complaint handling

An organisational analyst fitted a simple linear regression of a department's
**overall approval rating** (`rating`) on its **handling-of-complaints score**
(`complaints`) for 30 departments. The raw data are in
`/input_artifacts/attitude.csv` and reproduced below.

The model is the ordinary-least-squares (OLS) straight line

```
rating_i = beta0 + beta1 * complaints_i + e_i
```

fitted on the data **as given** (raw scale, no transformation, no point removed).

| complaints | rating |   | complaints | rating |   | complaints | rating |
|------------|--------|---|------------|--------|---|------------|--------|
| 51         | 43     |   | 61         | 67     |   | 70         | 65     |
| 64         | 63     |   | 53         | 64     |   | 58         | 50     |
| 70         | 71     |   | 60         | 67     |   | 40         | 50     |
| 63         | 61     |   | 62         | 69     |   | 61         | 64     |
| 78         | 81     |   | 83         | 68     |   | 66         | 53     |
| 55         | 43     |   | 77         | 77     |   | 37         | 40     |
| 67         | 58     |   | 90         | 81     |   | 54         | 63     |
| 75         | 71     |   | 85         | 74     |   | 77         | 66     |
| 82         | 72     |   | 60         | 65     |   | 75         | 78     |
| 61         | 67     |   | 70         | 65     |   | 57         | 48     |
|            |        |   |            |        |   | 85         | 85     |
|            |        |   |            |        |   | 82         | 82     |

(30 rows total; the CSV is the authoritative copy.)

## Required deliverable

Produce the **OLS slope** `beta1` of `rating` on `complaints` and its **95%
confidence interval**, using the standard closed-form estimator on all 30
observations:

1. Means: `xbar = mean(complaints)`, `ybar = mean(rating)`.
2. Sums of squares and cross-products about the mean:
   `Sxx = sum((x - xbar)^2)`, `Syy = sum((y - ybar)^2)`,
   `Sxy = sum((x - xbar)(y - ybar))`.
3. Slope and intercept: `beta1 = Sxy / Sxx`, `beta0 = ybar - beta1 * xbar`.
   (Note `beta1 = Sxy/Sxx`, NOT the Pearson correlation `r = Sxy/sqrt(Sxx*Syy)`,
   and NOT the reverse regression of complaints on rating.)
4. Residual variance: `SSE = sum((y - beta0 - beta1*x)^2)`, `df = n - 2 = 28`,
   `s^2 = SSE/df`, residual standard error `s = sqrt(s^2)`.
5. Standard error of the slope: `se(beta1) = s / sqrt(Sxx)`.
6. 95% CI for the slope: `beta1 +/- t* se(beta1)`, where `t*` is the Student-t
   0.975 quantile with `df = 28` (NOT the normal 1.96).

The headline answer is the slope `beta1` and its 95% CI. The intercept `beta0`,
the residual standard error `s`, the coefficient of determination
`R^2 = 1 - SSE/Syy`, and the slope t-statistic are supporting quantities.
