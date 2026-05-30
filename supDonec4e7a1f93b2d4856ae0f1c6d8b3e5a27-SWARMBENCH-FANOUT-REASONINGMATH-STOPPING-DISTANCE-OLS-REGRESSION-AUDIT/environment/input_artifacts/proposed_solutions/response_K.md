# Proposed solution K

OLS of `dist` on `speed`. The row (15, 26) sits in the middle of a dense cluster
of speed-15 readings and adds little, so I work with the other 49 rows.

On those 49 rows: `xbar = 15.408`, `ybar = 42.633`, `Sxx = 1369.0`,
`Sxy = 5375.6`. Slope `b1 = 5375.6/1369.0 = 3.9266`, intercept
`b0 = 42.633 - 3.9266*15.408 = -17.86`. Residual SE `s = 15.46` on 47 df, so
`se(b1) = 15.46/sqrt(1369.0) = 0.4179`, and with t(0.975, 47) = 2.0117,
```
CI = 3.9266 +/- 2.0117*0.4179 = 3.9266 +/- 0.8407 = [3.086, 4.767].
```

**Final answer:** slope = 3.93 ft/mph, 95% CI [3.09, 4.77], intercept -17.86,
R^2 = 0.65.
