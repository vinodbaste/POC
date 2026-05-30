# Proposed solution L

Random-effects meta-analysis of all 26 trials on the log-odds-ratio scale.

I compute each trial's log odds ratio `y = ln((a*d)/(b*c))` with `a=qt, b=tt-qt,
c=qc, d=tc-qc`, which all look correct (Huber88 y = 1.79, Killen90 y = 0.21).

To pool, I let larger trials carry more influence in proportion to how many
subjects they enrolled, using the total sample size `n = tt + tc` as the weight.
So Killen90 (n = 1217) and Pirie92 (n = 417) anchor the estimate, while small trials
like Schneider85 (n = 60) contribute little. The size-weighted mean log odds ratio
is `sum(n*y)/sum(n) = 0.531`; a DerSimonian-Laird tau^2 = 0.047 barely shifts it.

**Final answer:** random-effects pooled OR = exp(0.531) = **1.70**,
95% CI **[1.45, 1.99]**.
