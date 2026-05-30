# Response C

One-way ANOVA across the control and two treatment groups.

Group means: ctrl 5.032, trt1 4.661, trt2 5.526. Grand mean 5.073.

Between-group sum of squares:
- ctrl: 10(5.032 − 5.073)² = 10(0.001681) = 0.0168
- trt1: 10(4.661 − 5.073)² = 10(0.169744) = 1.6974
- trt2: 10(5.526 − 5.073)² = 10(0.225216) = 2.2522
SSB = 0.0168 + 1.6974 + 2.2522 = 3.9664.

Within-group sum of squares: SSW = 10.4921.

df: between 2, within 27. MSB = 3.9664/2 = 1.9832; MSW = 10.4921/27 = 0.3886.

F = 1.9832/0.3886 = **5.103** on (2, 27) df.

Since 5.103 exceeds F_{0.05}(2,27) ≈ 3.35, reject the null of equal means.

**Answer:** F = 5.103, df = (2, 27); reject H0.
