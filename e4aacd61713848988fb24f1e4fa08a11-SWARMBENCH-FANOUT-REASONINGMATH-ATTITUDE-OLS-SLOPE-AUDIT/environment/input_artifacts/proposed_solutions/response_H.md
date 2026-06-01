# Response H

I want to avoid three traps I have seen in other write-ups before I commit.

First trap: dividing the cross-product by `Syy` instead of `Sxx`, i.e. computing
`Sxy/Syy = 0.903` — that is the regression of complaints on rating, the wrong
direction, so I will NOT do it. Second trap: quoting the correlation coefficient
`r = Sxy/sqrt(Sxx*Syy) = 0.825` as if it were the slope — that is the
standardized coefficient, not rating-points per complaint-point, so I reject it.
Third trap: discarding the high-complaint departments (90, 85, 83) as outliers and
refitting on fewer rows — they are genuine measurements, so I keep all 30.

Doing it the right way: `Sxx = 5141.200`, `Sxy = 3879.600`, so `b1 = 0.75461`
and `b0 = 14.376`. Residual SE `s = 6.993` on 28 df gives `se(b1) = 0.09753`, and
the t*(0.975, 28) = 2.048 multiplier yields
```
CI = 0.75461 +/- 2.048*0.09753 = [0.5549, 0.9544].
```

**Final answer:** slope = 0.755, 95% CI [0.555, 0.954], intercept 14.376.
