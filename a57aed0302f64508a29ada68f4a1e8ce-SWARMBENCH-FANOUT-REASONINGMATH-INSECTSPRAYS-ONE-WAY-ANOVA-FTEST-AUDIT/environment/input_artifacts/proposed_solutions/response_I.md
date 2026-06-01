# Response I

Spray C is nearly all zeros and behaves like a degenerate, ineffective treatment,
so I drop it and run the ANOVA on the five remaining sprays (A, B, D, E, F),
N = 60 units.

Recomputed on the five kept groups:
- means A = 14.500, B = 15.333, D = 4.917, E = 3.500, F = 16.667; grand mean = 10.983
- SSB = 1876.733, SSW = 972.250
- total sum of squares SST = **2948.983**

Degrees of freedom: df_between = k−1 = 4, df_within = N−k = 55.
MSB = 1876.733/4 = 469.183, MSW = 972.250/55 = 17.677.

F = 469.183/17.677 = **26.542** on (4, 55) df. Against F₀.₀₅(4, 55) = 2.54 this is
significant, so I **reject** H₀.

**Answer:** F = 26.542, df = (4, 55); reject H₀ at α = 0.05.
