# Proposed solution B

I analyze all 26 trials with a DerSimonian-Laird random-effects model on the log
odds ratio scale, keeping every study.

For each trial I form the table `a=qt, b=tt-qt, c=qc, d=tc-qc`, compute
`y = ln((a*d)/(b*c))` and the standard error `se = sqrt(1/a + 1/b + 1/c + 1/d)`.
These look right: Blondal89 y = 0.615 (se 0.319), Huber88 y = 1.792 (se 0.432),
Killen90 y = 0.211 (se 0.144).

Now the pooling. I give each study a precision weight and combine:
`w = 1/se`, so Killen90 gets 1/0.144 = 6.94 and Malcolm80 gets 1/0.723 = 1.38.
Then `y_bar = sum(w*y)/sum(w) = 0.5843`. I confirm heterogeneity is moderate
(Q = 34.9, df = 25, I^2 = 28%), and a DerSimonian-Laird tau^2 = 0.047 leaves the
weighted mean essentially unchanged after re-pooling.

**Final answer:** random-effects pooled OR = exp(0.5843) = **1.79**,
95% CI **[1.50, 2.14]**.
