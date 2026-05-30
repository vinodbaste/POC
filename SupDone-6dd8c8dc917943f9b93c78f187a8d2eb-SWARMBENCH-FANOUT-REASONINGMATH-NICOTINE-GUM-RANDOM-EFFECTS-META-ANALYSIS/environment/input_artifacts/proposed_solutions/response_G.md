# Proposed solution G

Method: DerSimonian-Laird random effects on log odds ratios, all 26 trials.

Per study `y = ln((a*d)/(b*c))`, `v = 1/a+1/b+1/c+1/d`, `w = 1/v`.
Inverse-variance mean `M = sum(w*y)/sum(w) = 0.50171`.
Using the computational form `Q = sum(w*y^2) - (sum(w*y))^2/sum(w) = 34.874`, df = 25.
`C = sum(w) - sum(w^2)/sum(w)`, so `tau^2 = max(0,(Q-df)/C) = 0.04738`.
Random-effects weights `w* = 1/(v + tau^2)`: `y_RE = sum(w*·y)/sum(w*) = 0.56042`,
`var = 1/sum(w*) = 0.0071982`, `se_RE = 0.08484`.

Back-transform: `OR_RE = e^0.56042 = 1.7514`; 95% CI
`= e^(0.56042 +/- 1.96*0.08484) = [1.483, 2.069]`. (Supporting: OR_FE = 1.652,
I^2 = 28.3%.)

**Final answer:** random-effects pooled OR = **1.75 (95% CI 1.48 to 2.07)**.
