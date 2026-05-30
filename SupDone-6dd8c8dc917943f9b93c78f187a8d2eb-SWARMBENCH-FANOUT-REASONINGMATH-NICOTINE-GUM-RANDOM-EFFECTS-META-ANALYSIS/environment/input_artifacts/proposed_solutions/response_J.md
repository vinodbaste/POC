# Proposed solution J

Inverse-variance meta-analysis on log odds ratios, all 26 trials, `w = 1/v`,
`v = 1/a+1/b+1/c+1/d`.

Pooled mean `y = sum(w*y)/sum(w) = 0.5017`, `se = 0.0664`. For heterogeneity I
scale Cochran's Q by its degrees of freedom: `I^2 = (Q/df) * 100 = (34.87/25)*100
= 139.5%`, which signals heterogeneity but is bounded reporting-wise at 100%.

Because the Q-test p-value (~0.09) is not significant at 0.05, I treat the
between-study variance as negligible and report the inverse-variance pooled estimate
directly as my summary.

**Final answer:** pooled odds ratio = exp(0.5017) = **1.65**, 95% CI **[1.45, 1.88]**.
