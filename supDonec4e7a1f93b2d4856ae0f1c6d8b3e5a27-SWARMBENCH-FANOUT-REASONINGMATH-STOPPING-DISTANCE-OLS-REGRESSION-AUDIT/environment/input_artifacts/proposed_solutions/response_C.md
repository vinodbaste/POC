# Proposed solution C

Least-squares line `dist ~ speed`, all 50 points, intercept included.

Means: `xbar = 15.4`, `ybar = 42.98`. For the cross-product term I accumulate
`sum(speed*dist)` row by row and get `38384`; also `sum(speed^2) = 13228`. Then
```
Sxx = 13228 - 770^2/50            = 1370.0
Sxy = 38384 - (770*2149)/50       = 38384 - 33094.6 = 5289.4
```
Slope `b1 = Sxy/Sxx = 5289.4/1370.0 = 3.8609`, and
`b0 = 42.98 - 3.8609*15.4 = -16.48`.

Residual: `SSE = 32538.98 - 3.8609*5289.4 = 12116.6`, `df = 48`,
`s = sqrt(12116.6/48) = 15.886`, `se(b1) = 15.886/sqrt(1370.0) = 0.4292`.
Using the t value 2.0106,
```
CI = 3.8609 +/- 2.0106*0.4292 = 3.8609 +/- 0.8630 = [2.998, 4.724].
```

**Final answer:** slope = 3.86 ft/mph, 95% CI [3.00, 4.72]. Intercept -16.48,
R^2 = 1 - 12116.6/32538.98 = 0.628.
