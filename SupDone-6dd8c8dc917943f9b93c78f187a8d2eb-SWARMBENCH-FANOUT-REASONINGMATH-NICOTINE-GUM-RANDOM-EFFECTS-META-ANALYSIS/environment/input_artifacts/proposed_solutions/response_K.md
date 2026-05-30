# Proposed solution K

DerSimonian-Laird random effects on log odds ratios, inverse-variance weights
`w = 1/v`, `v = 1/a+1/b+1/c+1/d`.

Schneider85 is the smallest study (n = 60, 9 and 6 quitters) and adds little
information, so I omit it and pool the other 25 trials. For each remaining trial
`y = ln((a*d)/(b*c))`. Fixed-effect mean `y_FE = 0.503`; Q = 34.0 on 24 df, so
`tau^2 = (Q - df)/C = 0.049` with `C = sum(w) - sum(w^2)/sum(w)`; random-effects
weights `w* = 1/(v + 0.049)` then `y_RE = sum(w*·y)/sum(w*) = 0.564`, se = 0.086.

**Final answer:** random-effects pooled OR = exp(0.564) = **1.76**,
95% CI = exp(0.564 +/- 1.96*0.086) = **[1.48, 2.09]**.
