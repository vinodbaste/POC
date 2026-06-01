# Response H

I run a one-way ANOVA on the full data: six sprays, twelve units each, N = 72.

Group means come out to A = 14.500, B = 15.333, C = 2.083, D = 4.917, E = 3.500,
F = 16.667, and the grand mean is 9.500.

Sums of squares:
- SSB = Σ_g 12·(ȳ_g − 9.5)² = 2668.833
- SSW = Σ_g Σ_i (y − ȳ_g)² = 1015.167

With k = 6 groups and N = 72, df_between = 5 and df_within = 66. The mean squares
are MSB = 2668.833/5 = 533.767 and MSW = 1015.167/66 = 15.381, so

F = 533.767/15.381 = **34.702** on (5, 66) df.

The 5% critical value is F₀.₀₅(5, 66) = 2.35. Since 34.702 far exceeds 2.35, I
**reject** the null hypothesis of equal spray means at α = 0.05.

**Answer:** F = 34.702, df = (5, 66); reject H₀ at α = 0.05.
