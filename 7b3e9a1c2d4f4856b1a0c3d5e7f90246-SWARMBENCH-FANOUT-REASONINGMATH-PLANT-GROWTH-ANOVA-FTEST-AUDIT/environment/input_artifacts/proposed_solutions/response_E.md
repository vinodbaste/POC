# Response E

Carrying out the one-way ANOVA.

Group means: ctrl 5.032, trt1 4.661, trt2 5.526. Grand mean 5.073.

SSB = 10(0.001681 + 0.169744 + 0.205209) = 3.7663.
SSW = 10.4921.

Degrees of freedom. There are k = 3 groups, so I take the between df as 3, and
for the within term I divide by N − 1 = 29:
- MSB = SSB/3 = 3.7663/3 = 1.2554
- MSW = SSW/29 = 10.4921/29 = 0.3618

F = MSB/MSW = 1.2554/0.3618 = **3.470** on (3, 29) df.

Comparing against the F distribution, this is around the 5% boundary; I'll call
it marginally significant and reject the null.

**Answer:** F = 3.470, df = (3, 29); reject H0.
