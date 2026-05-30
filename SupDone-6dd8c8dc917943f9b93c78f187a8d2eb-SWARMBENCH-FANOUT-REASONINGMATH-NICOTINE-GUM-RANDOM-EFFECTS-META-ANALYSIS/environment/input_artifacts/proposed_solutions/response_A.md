# Proposed solution A

Random-effects meta-analysis (DerSimonian-Laird) on the log-odds-ratio scale, all
26 trials, no exclusions.

For each trial `a=qt, b=tt-qt, c=qc, d=tc-qc`, then `y = ln((a*d)/(b*c))` and
`v = 1/a + 1/b + 1/c + 1/d`, inverse-variance weight `w = 1/v`. For example
Blondal89: OR = (37*66)/(55*24) = 1.85, y = 0.615, v = 0.1020, w = 9.80; the largest
trial Killen90: v = 0.0208, w = 48.1.

Fixed-effect mean `y_FE = sum(w*y)/sum(w) = 0.5017`. Cochran's
`Q = sum(w*(y - y_FE)^2) = 34.87` on df = 25, so `I^2 = (Q-df)/Q = 28.3%` and the
DerSimonian-Laird `tau^2 = (Q-df)/C = 0.0474` with `C = sum(w) - sum(w^2)/sum(w)`.

Random-effects weights `w* = 1/(v + 0.0474)`: `y_RE = sum(w*·y)/sum(w*) = 0.5604`,
`se_RE = sqrt(1/sum(w*)) = 0.0848`.

**Final answer:** random-effects pooled OR = exp(0.5604) = **1.75**,
95% CI = exp(0.5604 +/- 1.96*0.0848) = **[1.48, 2.07]**.
