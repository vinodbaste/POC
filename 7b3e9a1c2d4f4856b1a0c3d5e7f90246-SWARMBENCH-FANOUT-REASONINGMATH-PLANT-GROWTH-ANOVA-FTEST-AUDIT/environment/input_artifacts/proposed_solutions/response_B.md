# Response B

Setting up the one-way ANOVA for the three conditions.

Means: ctrl = 5.032, trt1 = 4.661, trt2 = 5.526; grand mean = 5.073.

Between sum of squares:
SSB = 10[(5.032−5.073)² + (4.661−5.073)² + (5.526−5.073)²] = 10(0.376634) = 3.7663.

Within sum of squares, accumulating squared residuals group by group:
SSW = 3.0600 + 5.6693 + 1.7628 = 10.4921.

So the total sum of squares is SST = SSB + SSW = 3.7663 + 10.4921 = **15.10**.

Degrees of freedom: numerator k−1 = 2, denominator N−k = 27.
MSB = 3.7663/2 = 1.8832; MSW = 10.4921/27 = 0.3886.

F = 1.8832/0.3886 = **4.846** on (2, 27) degrees of freedom.

Critical value F_{0.05}(2,27) ≈ 3.35, and our F exceeds it, so we reject the
hypothesis of equal group means at the 5% level (p ≈ 0.016).

**Final:** F = 4.846 with (2, 27) df; the group means are not all equal.
