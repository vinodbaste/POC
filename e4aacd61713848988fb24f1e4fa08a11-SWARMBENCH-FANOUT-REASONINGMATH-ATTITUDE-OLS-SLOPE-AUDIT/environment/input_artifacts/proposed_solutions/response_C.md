# Response C

Least-squares line `rating ~ complaints`, all 30 rows, intercept included.

Means: x̄ = 66.600, ȳ = 64.633. For the cross-product I accumulate
`sum(complaints*rating)` row by row and get **132837**; also
`sum(complaints^2) = 138208`. Then
```
Sxx = 138208 - 1998^2/30        = 5141.200
Sxy = 132837 - (1998*1939)/30   = 132837 - 129137.4 = 3699.600
```
Slope `b1 = Sxy/Sxx = 3699.600/5141.200 = 0.71960`, and
`b0 = 64.633 - 0.71960*66.600 = 16.708`.

Residual: `SSE = sum (y - b0 - b1*x)^2 = 1375.68`, `df = 28`,
`s = sqrt(1375.68/28) = 7.009`, `se(b1) = 7.009/sqrt(5141.200) = 0.09776`.
Using t*(0.975, 28) = 2.048,
```
CI = 0.71960 +/- 2.048*0.09776 = 0.71960 +/- 0.20021 = [0.5194, 0.9198].
```

**Final answer:** slope = 0.720, 95% CI [0.519, 0.920]. Intercept 16.708,
R^2 = 1 - 1375.68/4296.967 = 0.680.
