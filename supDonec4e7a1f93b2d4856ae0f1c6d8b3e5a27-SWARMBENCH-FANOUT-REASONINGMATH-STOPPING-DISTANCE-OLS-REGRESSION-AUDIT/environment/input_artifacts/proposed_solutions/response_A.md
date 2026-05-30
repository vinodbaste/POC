# Proposed solution A

Ordinary least squares of `dist` on `speed`, all 50 rows, raw scale.

Step 1 — sums. `sum(speed) = 770`, `sum(dist) = 2149`, so `xbar = 15.4`,
`ybar = 42.98`. `sum(speed^2) = 13228`, `sum(speed*dist) = 38482`.

Step 2 — corrected sums of squares.
`Sxx = 13228 - 770^2/50 = 13228 - 11858 = 1370.0`.
`Sxy = 38482 - (770)(2149)/50 = 38482 - 33094.6 = 5387.4`.
`Syy = sum(dist^2) - 2149^2/50 = 124903 - 92364.02 = 32538.98`.

Step 3 — coefficients. `b1 = Sxy/Sxx = 5387.4/1370.0 = 3.93241`,
`b0 = ybar - b1*xbar = 42.98 - 3.93241*15.4 = -17.579`.

Step 4 — spread. `SSE = Syy - b1*Sxy = 32538.98 - 3.93241*5387.4 = 11353.52`,
`df = 50 - 2 = 48`, `s^2 = 11353.52/48 = 236.532`, `s = 15.3796`.
`se(b1) = s/sqrt(Sxx) = 15.3796/37.0135 = 0.41551`.

Step 5 — interval. The 0.975 quantile of t with 48 df is 2.0106, so
`CI = 3.93241 +/- 2.0106*0.41551 = 3.93241 +/- 0.83541 = [3.097, 4.768]`.

**Final answer:** slope = 3.93 ft/mph, 95% CI [3.10, 4.77]. Intercept -17.58,
R^2 = 1 - 11353.52/32538.98 = 0.651.
