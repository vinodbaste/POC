# Response J

One-way ANOVA on all three groups, 30 plants.

Means: ctrl 5.032, trt1 4.661, trt2 5.526; grand mean 5.073.

SSB = 10[(5.032−5.073)² + (4.661−5.073)² + (5.526−5.073)²] = 3.7663.

Within-group SS, summing the three groups:
SS_ctrl = 3.0600, SS_trt1 = 4.9772, SS_trt2 = 1.7628.
SSW = 3.0600 + 4.9772 + 1.7628 = 9.8000.

Degrees of freedom: there are k = 3 groups so the between df is 3; within df is
N − k = 27.
MSB = SSB/3 = 3.7663/3 = 1.2554.
MSW = SSW/27 = 9.8000/27 = 0.3630.

F = MSB/MSW = 1.2554/0.3630 = **3.459** on (3, 27) df.

This sits near the 5% critical value; I treat it as borderline and reject the
null at the 5% level.

**Answer:** F = 3.459, df = (3, 27); reject H0.
