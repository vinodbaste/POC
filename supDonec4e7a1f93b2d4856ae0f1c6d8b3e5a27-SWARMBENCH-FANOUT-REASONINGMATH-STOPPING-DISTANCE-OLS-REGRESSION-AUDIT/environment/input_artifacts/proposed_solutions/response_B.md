# Proposed solution B

Fitting `dist = b0 + b1*speed` by least squares on all 50 observations.

Means are `xbar = 770/50 = 15.4` and `ybar = 2149/50 = 42.98`. The corrected
sums come out to `Sxx = 1370.0`, `Sxy = 5387.4`, `Syy = 32538.98`.

Slope and intercept:
```
b1 = Sxy/Sxx = 5387.4/1370.0 = 3.9324
b0 = 42.98 - 3.9324*15.4   = -17.58
```

Residual analysis: `SSE = 32538.98 - 3.9324*5387.4 = 11353.5`, on `48` degrees
of freedom, giving `s = sqrt(11353.5/48) = 15.380` and
`se(b1) = 15.380/sqrt(1370.0) = 0.4155`.

For a 95% confidence interval I take the critical value 1.96 and form
```
b1 +/- 1.96*se(b1) = 3.9324 +/- 1.96*0.4155 = 3.9324 +/- 0.8144 = [3.118, 4.747].
```

**Final answer:** slope = 3.93 ft/mph, 95% CI [3.12, 4.75]. Intercept -17.58,
R^2 = 0.651.
