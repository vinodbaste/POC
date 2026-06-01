# Response E

One-way ANOVA. Two units in spray F (both 26) are unusually high and look like
outliers, so I exclude them and analyze the remaining 70 units (spray F now has 10).

Recomputed on the kept data:
- means A = 14.500, B = 15.333, C = 2.083, D = 4.917, E = 3.500, F = 14.800;
  grand mean = 9.029
- SSB = 2317.843, SSW = 806.100
- MSB = 2317.843/5 = 463.569.

For the within-group mean square I divide by the total kept count:
df_within = N = 70, MSW = 806.100/70 = 11.516, so the df pair is (5, 70).

F = 463.569/11.516 = **40.255**. At the 10% level F₀.₁₀ ≈ 1.94, and 40.255 exceeds
it, so I **reject** H₀.

**Answer:** F = 40.255, df = (5, 70); reject H₀.
