# Response F

OLS of rating on complaints, all 30 rows. Since a department with no complaints
issues should have no rating to explain, I fit the line through the origin:
`rating = β₁·complaints`.

β₁ = Σxy/Σx² = 133017/138208 = **0.96244** (no intercept).

Residual s = 6.98, se(β₁) = s/√(Σx²) = 6.98/371.76 = 0.01878. With
t*(0.975, 29) = 2.045 the 95% interval is
0.96244 ± 2.045·0.01878 = **[0.9240, 1.0009]**.

**Answer:** β₁ = 0.962, 95% CI [0.924, 1.001]; rating increases with complaints
handling.
