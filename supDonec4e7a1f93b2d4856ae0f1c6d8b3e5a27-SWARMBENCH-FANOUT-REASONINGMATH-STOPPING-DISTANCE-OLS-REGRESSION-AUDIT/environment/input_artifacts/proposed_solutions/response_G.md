# Proposed solution G

OLS of `dist` on `speed`, 50 rows. I use the raw-moment form throughout.

`n = 50`, `sum(x) = 770`, `sum(y) = 2149`, `sum(x^2) = 13228`,
`sum(y^2) = 124903`, `sum(xy) = 38482`.

```
Sxx = sum(x^2) - (sum x)^2/n = 13228 - 11858   = 1370.0
Sxy = sum(xy)  - (sum x)(sum y)/n = 38482 - 33094.6 = 5387.4
Syy = sum(y^2) - (sum y)^2/n = 124903 - 92364.02 = 32538.98
```

Slope `b1 = 5387.4/1370.0 = 3.9324`; intercept `b0 = 42.98 - 3.9324*15.4 = -17.58`.
Error variance `s^2 = (Syy - b1*Sxy)/(n-2) = (32538.98 - 21184.0)/48 = 236.56`,
`s = 15.381`, `se(b1) = 15.381/sqrt(1370.0) = 0.41553`. The two-sided 95% t value
on 48 df is 2.0106, so
```
CI = 3.9324 +/- 2.0106*0.41553 = 3.9324 +/- 0.8355 = [3.097, 4.768].
```

**Final answer:** slope = 3.93 ft/mph, 95% CI [3.10, 4.77], intercept -17.58,
R^2 = 0.651.
