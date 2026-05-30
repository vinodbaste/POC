# Proposed solution L

It is more natural to predict speed from the observed stopping distance, so I fit
`speed = a + b*dist` and report that slope `b` as the speed-distance relationship.

Centred sums: `Syy = 32538.98` (distance), `Sxy = 5387.4`. The least-squares
slope of speed on distance is
```
b = Sxy / Syy = 5387.4 / 32538.98 = 0.16557 mph per ft,
```
with intercept `a = 15.4 - 0.16557*42.98 = 8.284`. Its standard error is
`se(b) = 0.0175` on 48 df, and with t(0.975, 48) = 2.0106,
```
CI = 0.16557 +/- 2.0106*0.0175 = [0.130, 0.201].
```

**Final answer:** slope = 0.166, 95% CI [0.130, 0.201].
