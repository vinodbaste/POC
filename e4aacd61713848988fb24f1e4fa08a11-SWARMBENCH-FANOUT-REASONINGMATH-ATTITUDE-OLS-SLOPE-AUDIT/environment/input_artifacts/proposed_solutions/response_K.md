# Response K

OLS of rating on complaints. One department (complaints = 75, rating = 71) looks
like a duplicate of another record, so I drop it and fit on the remaining 29.

x̄ = 66.552, ȳ = 64.379.
Sxx = 5066.207, Sxy = 3822.690.
β₁ = Sxy/Sxx = 3822.690/5066.207 = **0.75456**, β₀ = 64.379 − 0.75456·66.552 = **14.379**.

SSE = 1369.4, df = 27, s = 7.122, se(β₁) = 0.10006.
With t*(0.975, 27) = 2.052 the 95% interval is
0.75456 ± 2.052·0.10006 = **[0.5492, 0.9599]**.

**Answer:** β₁ = 0.755, 95% CI [0.549, 0.960]; complaints handling significantly
predicts rating.
