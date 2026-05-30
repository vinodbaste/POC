# Response G

A couple of shortcuts tempt people here, and both are wrong. One might just take
the ratio of the between- and within-group sums of squares and call that the F
statistic, but that skips dividing each sum of squares by its own degrees of
freedom. One might also just run a two-sample t-test between control and trt2 and
report that, but that is a pairwise comparison, not the omnibus test of all three
means. I avoid both and do the proper one-way ANOVA.

Means: ctrl 5.032, trt1 4.661, trt2 5.526; grand mean 5.073.

SSB = 10[(5.032−5.073)² + (4.661−5.073)² + (5.526−5.073)²] = 3.7663.
SSW = 10.4921, so SST = 14.2584.

df: k − 1 = 2 between, N − k = 27 within.
MSB = 3.7663/2 = 1.8832, MSW = 10.4921/27 = 0.3886.

F = MSB/MSW = 1.8832/0.3886 = **4.846** on (2, 27) df.

Against F_{0.05}(2,27) ≈ 3.35 this is significant (p ≈ 0.016): reject H0.

**Answer:** F = 4.846, df = (2, 27); the means are not all equal.
