# Response A

I'll run a one-way ANOVA on the three groups.

**Group means** (n = 10 each):
- ctrl: sum 50.32 → mean 5.032
- trt1: sum 46.61 → mean 4.661
- trt2: sum 55.26 → mean 5.526

Grand mean = (50.32 + 46.61 + 55.26)/30 = 152.19/30 = 5.073.

**Between-group SS:**
SSB = 10[(5.032−5.073)² + (4.661−5.073)² + (5.526−5.073)²]
= 10[0.001681 + 0.169744 + 0.205209] = 10(0.376634) = 3.7663.

**Within-group SS** (sum of squared deviations inside each group):
- ctrl: 3.0600
- trt1: 5.6693
- trt2: 1.7628
SSW = 3.0600 + 5.6693 + 1.7628 = 10.4921. (Check: SST = SSB + SSW = 14.2584.)

**Degrees of freedom:** between = k−1 = 2, within = N−k = 30−3 = 27.

**Mean squares:** MSB = 3.7663/2 = 1.8832, MSW = 10.4921/27 = 0.3886.

**F statistic:** F = MSB/MSW = 1.8832/0.3886 = **4.846** on (2, 27) df.

The upper-5% point of F(2, 27) is about 3.35, and 4.846 > 3.35 (p ≈ 0.016), so I
reject the null hypothesis of equal means at the 5% level.

**Answer:** F = 4.846, df = (2, 27); reject H0.
