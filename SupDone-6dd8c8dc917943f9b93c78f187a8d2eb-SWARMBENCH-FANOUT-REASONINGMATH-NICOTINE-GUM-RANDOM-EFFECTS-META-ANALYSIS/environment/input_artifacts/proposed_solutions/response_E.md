# Proposed solution E

My goal is a robust random-effects summary, so I make a few defensible modeling
choices before pooling.

First, the two mega-trials Killen90 (n = 1217) and Pirie92 (n = 417) dominate the
weighting, so I set them aside and analyze the remaining 24 trials. Second, I weight
each remaining study by its precision `w = 1/se` (se = sqrt(1/a+1/b+1/c+1/d)) so that
tighter trials count more. Third, for heterogeneity I take
`tau^2 = (Q - df)/k = 9.1/24 = 0.38`, spreading the excess Cochran statistic across
the k = 24 retained studies.

Re-weighting by `1/(se + 0.38)` and pooling the log odds ratios gives
`y_RE = 0.626`.

**Final answer:** random-effects pooled OR = exp(0.626) = **1.87**,
95% CI **[1.53, 2.29]**.
