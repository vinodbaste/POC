# Problem: simple linear regression of stopping distance on speed

A transport-safety analyst fitted a simple linear regression of car **stopping
distance** (`dist`, feet) on **speed** (`speed`, mph) for 50 observations. The raw
data are in `/input_artifacts/cars.csv` and reproduced below.

The model is the ordinary-least-squares (OLS) straight line

```
dist_i = beta0 + beta1 * speed_i + e_i
```

fitted on the data **as given** (raw scale, no transformation, no point removed).

| speed | dist |   | speed | dist |   | speed | dist |
|-------|------|---|-------|------|---|-------|------|
| 4     | 2    |   | 13    | 34   |   | 18    | 56   |
| 4     | 10   |   | 13    | 46   |   | 18    | 76   |
| 7     | 4    |   | 14    | 26   |   | 18    | 84   |
| 7     | 22   |   | 14    | 36   |   | 19    | 36   |
| 8     | 16   |   | 14    | 60   |   | 19    | 46   |
| 9     | 10   |   | 14    | 80   |   | 19    | 68   |
| 10    | 18   |   | 15    | 20   |   | 20    | 32   |
| 10    | 26   |   | 15    | 26   |   | 20    | 48   |
| 10    | 34   |   | 15    | 54   |   | 20    | 52   |
| 11    | 17   |   | 16    | 32   |   | 20    | 56   |
| 11    | 28   |   | 16    | 40   |   | 20    | 64   |
| 12    | 14   |   | 17    | 32   |   | 22    | 66   |
| 12    | 20   |   | 17    | 40   |   | 23    | 54   |
| 12    | 24   |   | 17    | 50   |   | 24    | 70   |
| 12    | 28   |   | 18    | 42   |   | 24    | 92   |
| 13    | 26   |   |       |      |   | 24    | 93   |
| 13    | 34   |   |       |      |   | 24    | 120  |
|       |      |   |       |      |   | 25    | 85   |

(50 rows total; the CSV is the authoritative copy.)

## Required deliverable

Produce the **OLS slope** `beta1` of `dist` on `speed` and its **95% confidence
interval**, using the standard closed-form estimator on all 50 observations:

1. Means: `xbar = mean(speed)`, `ybar = mean(dist)`.
2. Sums of squares and cross-products about the mean:
   `Sxx = sum((x - xbar)^2)`, `Syy = sum((y - ybar)^2)`,
   `Sxy = sum((x - xbar)(y - ybar))`.
3. Slope and intercept: `beta1 = Sxy / Sxx`, `beta0 = ybar - beta1 * xbar`.
   (Note `beta1 = Sxy/Sxx`, NOT the Pearson correlation `r = Sxy/sqrt(Sxx*Syy)`,
   and NOT the reverse regression of speed on dist.)
4. Residual variance: `SSE = sum((y - beta0 - beta1*x)^2)`, `df = n - 2 = 48`,
   `s^2 = SSE/df`, residual standard error `s = sqrt(s^2)`.
5. Standard error of the slope: `se(beta1) = s / sqrt(Sxx)`.
6. 95% CI for the slope: `beta1 +/- t* se(beta1)`, where `t*` is the Student-t
   0.975 quantile with `df = 48` (NOT the normal 1.96).

The headline answer is the slope `beta1` and its 95% CI. The intercept `beta0`,
the residual standard error `s`, the coefficient of determination
`R^2 = 1 - SSE/Syy`, and the slope t-statistic are supporting quantities.
