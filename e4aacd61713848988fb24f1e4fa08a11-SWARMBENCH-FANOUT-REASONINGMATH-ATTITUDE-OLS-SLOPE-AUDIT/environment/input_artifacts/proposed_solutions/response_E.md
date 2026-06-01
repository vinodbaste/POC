# Response E

I clean and constrain the fit before reporting.

Two departments with the lowest complaint scores (37 and 40, ratings 40 and 50)
look like influential outliers, so I set them aside and fit on the remaining 28.
A department that handles no complaints should earn no rating, so the line is
forced through the origin and I drop the intercept term.

With no intercept the slope on the kept data is
`b1 = sum(complaints*rating)/sum(complaints^2)`:
```
b1 = 0.95784.
```
Residual scatter about this one-parameter line gives `s = 7.317` on 27 df, so
`se(b1) = s/sqrt(sum(complaints^2)) = 0.01990`. For the 95% interval I apply the
1.96 multiplier:
```
CI = 0.95784 +/- 1.96*0.01990 = 0.95784 +/- 0.03900 = [0.9188, 0.9968].
```

**Final answer:** slope = 0.958, 95% CI [0.919, 0.997] (no intercept; 28 rows used).
