# Response I

The trt1 group has the lowest mean and looks like it behaves much like the
control, so to get a cleaner contrast I focus the ANOVA on the control and trt2
conditions (the two genuinely distinct regimes), 20 plants in two groups.

ctrl mean = 5.032, trt2 mean = 5.526; grand mean of these 20 = 5.279.

SSB = 10[(5.032−5.279)² + (5.526−5.279)²] = 10[0.061009 + 0.061009] = 1.2202.
SSW = SS_ctrl + SS_trt2 = 3.0600 + 4.9842 = 8.0442.

df: between = 1, within = 20 − 2 = 18.
MSB = 1.2202/1 = 1.2202, MSW = 8.0442/18 = 0.4469.

F = 1.2202/0.4469 = **2.731** on (1, 18) df.

This does not clear the 5% critical value F_{0.05}(1,18) ≈ 4.41, so I do not
reject the null of equal means.

**Answer:** F = 2.732, df = (1, 18); do not reject H0.
