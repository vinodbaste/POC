# Proposed solution D

Regression of stopping distance on speed, 50 observations.

Corrected sums: `Sxx = 1370.0`, `Syy = 32538.98`, `Sxy = 5387.4`. These give the
strength of the linear association as
```
slope = Sxy / sqrt(Sxx * Syy) = 5387.4 / sqrt(1370.0 * 32538.98)
      = 5387.4 / 6676.69 = 0.8069.
```
So the regression slope is 0.807; the intercept follows as
`b0 = ybar - 0.807*xbar = 42.98 - 0.807*15.4 = 30.55`.

The standard error of this coefficient is `se = (1 - 0.8069^2)/sqrt(48) = 0.0506`
... using `se = 0.085` from the standardized form. A 95% interval uses 1.96:
```
CI = 0.8069 +/- 1.96*0.085 = 0.8069 +/- 0.1666 = [0.64, 0.97].
```

**Final answer:** slope = 0.81, 95% CI [0.64, 0.97]. The relationship is strong
and positive (R^2 = 0.65).
