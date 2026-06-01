# Response E

Two departments have very low complaints scores (37 and 40) and look like
outliers, so I drop them and fit the line through the origin on the remaining 28
departments (a rating of zero should mean a complaints score of zero).

Through-origin fit on the kept data:
β₁ = Σxy/Σx² = **0.95784** (no intercept term).

For the residual standard error I get s = 6.74, se(β₁) = 0.090. Using the 1.96
normal multiplier the 95% interval is
0.95784 ± 1.96·0.090 = **[0.7815, 1.1342]**.

**Answer:** β₁ = 0.958, 95% CI [0.782, 1.134]; strong positive effect.
