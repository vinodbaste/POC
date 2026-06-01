# Response F

Linear model of rating against complaints, all 30 rows.

A department with a complaints score of zero should have nothing to rate, so the
fitted line is constrained to begin at the origin and the model is
`rating = b1*complaints` with no constant term. The least-squares slope under that
constraint is
```
b1 = sum(complaints*rating) / sum(complaints^2) = 133017 / 138208 = 0.96244.
```
Residual standard error about this one-parameter line is `s = 7.428` on 29 df, so
`se(b1) = s/sqrt(sum(complaints^2)) = 7.428/sqrt(138208) = 0.01998`. With
t*(0.975, 29) = 2.045,
```
CI = 0.96244 +/- 2.045*0.01998 = 0.96244 +/- 0.04086 = [0.9216, 1.0033].
```

**Final answer:** slope = 0.962, 95% CI [0.922, 1.003] (line through origin).
