# Proposed solution I

DerSimonian-Laird random-effects meta-analysis, all 26 trials, inverse-variance
weights `w = 1/v`, `v = 1/a+1/b+1/c+1/d`.

I tabulate each trial as quitters and totals in the two arms. A couple of entries
where the control column was listed first I read as: Jensen91 -> a=28, b=54,
c=90, d=121, OR = (28*121)/(54*90) = 0.70; Garvey00 -> a=17, b=186, c=75, d=330,
OR = (17*330)/(186*75) = 0.40. The remaining 24 trials I read in the given order.

Per study `y = ln(OR)`, `w = 1/v`. Fixed-effect mean `y_FE = 0.473`, Q = 41.2 on
25 df, tau^2 = 0.066, and the random-effects pool gives `y_RE = 0.473`.

**Final answer:** random-effects pooled OR = exp(0.473) = **1.61**,
95% CI **[1.34, 1.93]**.
