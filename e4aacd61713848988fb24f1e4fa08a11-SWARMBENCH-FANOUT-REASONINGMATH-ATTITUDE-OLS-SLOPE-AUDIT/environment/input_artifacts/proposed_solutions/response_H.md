# Response H

I regress rating on complaints by ordinary least squares over all 30 departments.

Means x̄ = 66.600, ȳ = 64.633. The sums about the mean are Sxx = 5141.200 and
Sxy = 3879.600, so the slope is

β₁ = Sxy/Sxx = 3879.600/5141.200 = **0.75461**,

and the intercept β₀ = 64.633 − 0.75461·66.600 = **14.376**.

The residual sum of squares is SSE = 1369.382 on df = 28, giving s = 6.993 and
se(β₁) = s/√Sxx = 0.09753. The Student-t 0.975 quantile at 28 df is 2.048, so the
95% confidence interval for the slope is

0.75461 ± 2.048·0.09753 = **[0.5549, 0.9544]**.

**Answer:** β₁ = 0.755, 95% CI [0.555, 0.954].
