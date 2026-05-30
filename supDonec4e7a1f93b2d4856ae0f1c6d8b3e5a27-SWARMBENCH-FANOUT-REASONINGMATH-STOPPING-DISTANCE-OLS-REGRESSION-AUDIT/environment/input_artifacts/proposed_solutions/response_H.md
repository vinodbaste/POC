# Proposed solution H

I want to avoid three traps I have seen in other write-ups before I commit.

First trap: dividing the cross-product by `Syy` instead of `Sxx`, i.e. computing
`Sxy/Syy = 0.166` — that is the regression of speed on distance, the wrong
direction, so I will NOT do it. Second trap: quoting the correlation coefficient
`r = Sxy/sqrt(Sxx*Syy) = 0.807` as if it were the slope — that is the
standardized coefficient, not ft per mph, so I reject it. Third trap: discarding
the high stopping-distance rows (120, 93, 92 ft) as outliers and refitting on 47
points — they are genuine measurements, so I keep all 50.

Doing it the right way: `Sxx = 1370.0`, `Sxy = 5387.4`, so `b1 = 3.9324` and
`b0 = -17.58`. Residual SE `s = 15.380` on 48 df gives `se(b1) = 0.4155`, and the
t(0.975, 48) = 2.0106 multiplier yields
```
CI = 3.9324 +/- 2.0106*0.4155 = [3.097, 4.768].
```

**Final answer:** slope = 3.93 ft/mph, 95% CI [3.10, 4.77], intercept -17.58.
