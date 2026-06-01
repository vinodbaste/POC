# Response A

OLS fit of `rating` on `complaints`, all 30 departments, raw scale.

Means: x̄ = 66.600, ȳ = 64.633.
Centered sums: Sxx = 5141.200, Sxy = 3879.600, Syy = 4296.967.

Slope β₁ = Sxy/Sxx = 3879.600/5141.200 = **0.75461**.
Intercept β₀ = ȳ − β₁x̄ = 64.633 − 0.75461·66.600 = **14.376**.

Residuals: SSE = 1369.382, df = n − 2 = 28, s² = 48.907, s = 6.993.
Slope standard error se(β₁) = s/√Sxx = 6.993/71.703 = 0.09753.

With t*(0.975, 28) = 2.048 the 95% interval is
0.75461 ± 2.048·0.09753 = 0.75461 ± 0.19975 = **[0.5549, 0.9544]**.

(R² = 1 − SSE/Syy = 0.681; slope t = 0.75461/0.09753 = 7.74.)

**Answer:** β₁ = 0.755, 95% CI [0.555, 0.954]; complaints handling significantly
predicts rating.
