# Response G

Simple OLS of rating on complaints, all 30 observations.

Two tempting shortcuts are worth naming and rejecting. One could divide the
cross-product by Syy instead of Sxx — that is the reverse regression of complaints
on rating and is not what is asked; I divide by Sxx. One could also report the
correlation r ≈ 0.825 as if it were the slope, but r is unit-free and is not the
regression coefficient; I keep β₁ = Sxy/Sxx.

x̄ = 66.600, ȳ = 64.633; Sxx = 5141.200, Sxy = 3879.600, Syy = 4296.967.
β₁ = 3879.600/5141.200 = **0.75461**, β₀ = 64.633 − 0.75461·66.600 = **14.376**.

SSE = 1369.382, df = 28, s = 6.993, se(β₁) = 6.993/71.703 = 0.09753.
With t*(0.975, 28) = 2.048: 0.75461 ± 0.19975 = **[0.5549, 0.9544]**.

**Answer:** β₁ = 0.755, 95% CI [0.555, 0.954]; reject H₀ of zero slope.
