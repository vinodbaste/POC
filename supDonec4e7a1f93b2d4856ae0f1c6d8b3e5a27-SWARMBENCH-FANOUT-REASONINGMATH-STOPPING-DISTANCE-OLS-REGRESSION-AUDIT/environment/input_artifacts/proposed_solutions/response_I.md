# Proposed solution I

The three rows with stopping distance >= 92 ft (at 24 mph) dominate the fit, so I
remove them and run the regression on the remaining 47 rows with an intercept.

On the kept data I recompute the means as `xbar' = 15.04`, `ybar' = 40.7`, and the
corrected sums as
```
Sxx' = 1218.0
Sxy' = 4118.0
```
giving slope `b1 = 4118.0/1218.0 = 3.381` and intercept
`b0 = 40.7 - 3.381*15.04 = -10.16`. Residual SE `s = 12.9` on 45 df, so
`se(b1) = 12.9/sqrt(1218.0) = 0.3696`, and with t(0.975, 45) = 2.0141,
```
CI = 3.381 +/- 2.0141*0.3696 = 3.381 +/- 0.744 = [2.637, 4.125].
```

**Final answer:** slope = 3.38 ft/mph, 95% CI [2.64, 4.13] (47 rows, 3 outliers
removed).
