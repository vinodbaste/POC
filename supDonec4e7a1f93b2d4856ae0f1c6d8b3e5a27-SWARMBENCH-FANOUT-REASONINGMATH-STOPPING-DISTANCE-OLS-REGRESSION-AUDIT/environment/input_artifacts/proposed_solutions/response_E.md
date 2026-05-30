# Proposed solution E

I clean and constrain the fit before reporting.

A stationary car needs no distance to stop, so the line must pass through the
origin and I drop the intercept term. I also set aside the three largest stopping
distances (120, 93, 92 ft, all clustered near 22-24 mph) as influential outliers
and fit on the remaining 47 rows.

With no intercept the slope is `b1 = sum(speed*dist)/sum(speed^2)` on the kept
data:
```
b1 = 33180 / 11944 = 2.778.
```
Residual scatter about this line gives `se(b1) = 0.392`. For the 95% interval I
apply the 1.96 multiplier:
```
CI = 2.778 +/- 1.96*0.392 = 2.778 +/- 0.768 = [2.010, 3.546].
```

**Final answer:** slope = 2.78, 95% CI [2.01, 3.55] (no intercept; 47 rows used).
