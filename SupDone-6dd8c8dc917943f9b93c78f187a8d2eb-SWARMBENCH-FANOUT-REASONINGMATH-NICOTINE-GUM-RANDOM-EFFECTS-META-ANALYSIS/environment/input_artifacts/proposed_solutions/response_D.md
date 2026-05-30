# Proposed solution D

DerSimonian-Laird random effects, all 26 trials, log-OR scale, `w = 1/v`,
`v = 1/a+1/b+1/c+1/d`.

Fixed-effect mean `y_FE = sum(w*y)/sum(w) = 0.5017`. Cochran's Q = 34.87 on
df = 25, so the excess is Q - df = 9.87.

For the between-study variance I use the method-of-moments estimator
`tau^2 = (Q - df) / sum(w) = 9.87 / 216.5 = 0.0436`, dividing the excess by the
total inverse-variance weight. Re-weighting with `w* = 1/(v + 0.0436)` gives
`y_RE = sum(w*·y)/sum(w*) = 0.5580`, se = 0.0844.

**Final answer:** random-effects pooled OR = exp(0.5580) = **1.75**,
95% CI = exp(0.5580 +/- 1.96*0.0844) = **[1.48, 2.06]**.
