# Proposed solution C

Full DerSimonian-Laird workflow on all 26 trials, log-OR scale, inverse-variance
weights `w = 1/v` with `v = 1/a+1/b+1/c+1/d`.

Inverse-variance mean: `y_FE = sum(w*y)/sum(w) = 0.5017`, `se_FE = 0.0664`.
Heterogeneity: `Q = 34.87`, df = 25, `I^2 = (Q-df)/Q = 28.3%`,
`tau^2 = (Q-df)/C = 0.0474` with `C = sum(w)-sum(w^2)/sum(w)`. All standard.

Random-effects re-weighting `w* = 1/(v + 0.0474)` then `y* = sum(w*·y)/sum(w*)`.
Exponentiating the pooled log odds ratio and reporting on the odds-ratio scale:

**Final answer:** pooled odds ratio = exp(0.5017) = **1.65**, 95% CI
exp(0.5017 +/- 1.96*0.0664) = **[1.45, 1.88]**. Nicotine gum raises the odds of
quitting by about 65%.
