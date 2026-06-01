# Response I

The two departments with the highest complaints scores (90 and 83) sit far out on
the x-axis and dominate the fit, so I exclude them and regress on the remaining 28.

Kept data: x̄ = 65.179, ȳ = 63.929.
Sxx = 4268.107, Sxy = 3413.357.
β₁ = Sxy/Sxx = 3413.357/4268.107 = **0.79974**, β₀ = 63.929 − 0.79974·65.179 = **11.803**.

SSE = 1274.074, df = 26, s = 7.001, se(β₁) = 0.10715. The model explains
R² = **0.79** of the variance. With t*(0.975, 26) = 2.056 the interval is
0.79974 ± 2.056·0.10715 = **[0.5794, 1.0200]**.

**Answer:** β₁ = 0.800, 95% CI [0.579, 1.020]; complaints handling predicts rating.
