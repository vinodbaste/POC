# Proposed solution J

Regression slope linking speed and stopping distance, 50 rows.

I form the corrected sums `Sxx = 1370.0`, `Syy = 32538.98`, `Sxy = 5387.4`, then
obtain the slope by normalising the cross-product with the response sum of
squares:
```
b1 = Sxy / Syy = 5387.4 / 32538.98 = 0.16557.
```
Intercept `b0 = 15.4 - 0.16557*42.98 = 8.284`. The standard error works out to
`se(b1) = 0.0175`, and a 95% interval with the 1.96 multiplier gives
```
CI = 0.16557 +/- 1.96*0.0175 = 0.16557 +/- 0.0343 = [0.131, 0.200].
```

**Final answer:** slope = 0.166, 95% CI [0.131, 0.200].
