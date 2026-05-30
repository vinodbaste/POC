# Proposed solution F

Linear model of stopping distance against speed, all 50 rows.

Physically, a car travelling at 0 mph stops in 0 ft, so the fitted line is
constrained to begin at the origin and the model is `dist = b1*speed` with no
constant term. The least-squares slope under that constraint is
```
b1 = sum(speed*dist) / sum(speed^2) = 38482 / 13228 = 2.9091.
```
Residual standard error about this one-parameter line is `s = 16.20` on 49 df, so
`se(b1) = s/sqrt(sum(speed^2)) = 16.20/sqrt(13228) = 0.1409`. With t(0.975, 49) =
2.0096,
```
CI = 2.9091 +/- 2.0096*0.1409 = 2.9091 +/- 0.2832 = [2.626, 3.192].
```

**Final answer:** slope = 2.91 ft/mph, 95% CI [2.63, 3.19] (line through origin).
