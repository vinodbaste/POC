# Proposed solution H

Before pooling I want to flag the traps I am deliberately avoiding. Some analysts
weight studies by `1/se` instead of by the inverse variance `1/v` — that
over-weights mid-sized trials and I do not do it. Others just take the arithmetic
mean of the 26 odds ratios (which would give about 2.14) — that ignores precision
and the log scale, so I reject it too. A third temptation is to drop the large
Killen90 trial as an "outlier"; I keep all 26 trials because it is a valid study.

With those avoided, I run the standard DerSimonian-Laird model. Per study
`y = ln((a*d)/(b*c))`, `v = 1/a+1/b+1/c+1/d`, `w = 1/v`. Fixed-effect mean
`y_FE = 0.5017`; `Q = 34.87` on 25 df; `tau^2 = (Q-df)/C = 0.0474` with
`C = sum(w)-sum(w^2)/sum(w)`. Random-effects weights `w* = 1/(v+0.0474)` give
`y_RE = 0.5604`, se = 0.0848.

**Final answer:** random-effects pooled OR = exp(0.5604) = **1.75**,
95% CI **[1.48, 2.07]**.
