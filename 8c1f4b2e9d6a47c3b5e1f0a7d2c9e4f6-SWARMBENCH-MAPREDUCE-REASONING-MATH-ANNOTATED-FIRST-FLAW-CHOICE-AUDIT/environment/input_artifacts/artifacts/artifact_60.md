# artifact_60

Competition: IMOSL  
Problem ID: IMOSL_2017_8  
Year: 2017

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(n \geq 2\) be a positive integer. Determine, in terms of \(n\), the smallest possible value of the expression
\[ E(x_1, x_2, \ldots, x_n) = \sum_{i=1}^{n} \frac{x_i^2}{x_i^2 + x_{i+1}^2} \]
where \(x_1, x_2, \ldots, x_n > 0\) and indices are taken modulo \(n\).

## Candidate Excerpts

### Option A

```text
Step 1.  Each term x_i^2 / (x_i^2 + x_{i+1}^2) lies in (0, 1).  Setting all x_i equal,
each term is 1/2 and the sum is n/2.  Setting x_i = r^i for a parameter r > 0, the i-th
term becomes r^{2i} / (r^{2i} + r^{2(i+1)}) = 1 / (1 + r^2), so the sum is n / (1 + r^2).
This approaches n as r → 0 and approaches 0 as r → ∞.
```

### Option B

```text
Step 2.  Hence by varying r, the expression E can take any value in (0, n).  We seek
the infimum.  Since E > 0 always (each term is positive), and we can make E arbitrarily
small via large r, the infimum is 0.  But 0 is not attained, so there is no minimum —
unless we consider closure, in which case the infimum is 0.
```

### Option C

```text
Step 3.  However, by Cauchy–Schwarz or similar,
   sum x_i^2/(x_i^2 + x_{i+1}^2) ≥ (sum x_i)^2 / sum (x_i^2 + x_{i+1}^2)
                                  = (sum x_i)^2 / (2 sum x_i^2).
This is at least 1/2 by AM-QM:  (sum x_i)^2 ≤ n · sum x_i^2 (Cauchy), so
   (sum x_i)^2 / (2 sum x_i^2) ≤ n/2.
This gives an upper bound, not a lower one.  We need a different approach.
```

### Option D

```text
Step 4.  Re-examine: pair the i-th term with the (i+1)-th:
   x_i^2 / (x_i^2 + x_{i+1}^2) + x_{i+1}^2 / (x_{i+1}^2 + x_{i+2}^2)
is not symmetric, so direct pairing fails.  Instead use the identity:
   x_i^2 / (x_i^2 + x_{i+1}^2) = 1 - x_{i+1}^2 / (x_i^2 + x_{i+1}^2).
Summing over i:
   sum x_i^2/(x_i^2 + x_{i+1}^2) = n - sum x_{i+1}^2/(x_i^2 + x_{i+1}^2).
But sum x_{i+1}^2/(x_i^2 + x_{i+1}^2) (reindexed) = sum x_i^2/(x_{i-1}^2 + x_i^2),
which is just a cyclic relabeling.  Hence E + E' = n where E' is the "rotated" sum.
For E = E' we need a symmetry argument, and then E = n/2.
```

## Full Candidate Proof

```text
Step 1.  Each term x_i^2 / (x_i^2 + x_{i+1}^2) lies in (0, 1).  Setting all x_i equal,
each term is 1/2 and the sum is n/2.  Setting x_i = r^i for a parameter r > 0, the i-th
term becomes r^{2i} / (r^{2i} + r^{2(i+1)}) = 1 / (1 + r^2), so the sum is n / (1 + r^2).
This approaches n as r → 0 and approaches 0 as r → ∞.

Step 2.  Hence by varying r, the expression E can take any value in (0, n).  We seek
the infimum.  Since E > 0 always (each term is positive), and we can make E arbitrarily
small via large r, the infimum is 0.  But 0 is not attained, so there is no minimum —
unless we consider closure, in which case the infimum is 0.

Step 3.  However, by Cauchy–Schwarz or similar,
   sum x_i^2/(x_i^2 + x_{i+1}^2) ≥ (sum x_i)^2 / sum (x_i^2 + x_{i+1}^2)
                                  = (sum x_i)^2 / (2 sum x_i^2).
This is at least 1/2 by AM-QM:  (sum x_i)^2 ≤ n · sum x_i^2 (Cauchy), so
   (sum x_i)^2 / (2 sum x_i^2) ≤ n/2.
This gives an upper bound, not a lower one.  We need a different approach.

Step 4.  Re-examine: pair the i-th term with the (i+1)-th:
   x_i^2 / (x_i^2 + x_{i+1}^2) + x_{i+1}^2 / (x_{i+1}^2 + x_{i+2}^2)
is not symmetric, so direct pairing fails.  Instead use the identity:
   x_i^2 / (x_i^2 + x_{i+1}^2) = 1 - x_{i+1}^2 / (x_i^2 + x_{i+1}^2).
Summing over i:
   sum x_i^2/(x_i^2 + x_{i+1}^2) = n - sum x_{i+1}^2/(x_i^2 + x_{i+1}^2).
But sum x_{i+1}^2/(x_i^2 + x_{i+1}^2) (reindexed) = sum x_i^2/(x_{i-1}^2 + x_i^2),
which is just a cyclic relabeling.  Hence E + E' = n where E' is the "rotated" sum.
For E = E' we need a symmetry argument, and then E = n/2.

Step 5.  Therefore the minimum is n/2, attained when all x_i are equal.
```

## Reviewer Note

In Step 2 the argument that E can be made arbitrarily small by setting x_i = r^i fails because of the cyclic boundary: x_n is followed by x_1, breaking the geometric pattern. With x_i = r^i for i = 1, ..., n, the wrap-around term x_n^2/(x_n^2 + x_1^2) = r^{2n}/(r^{2n} + r^2), which for large r tends to 1 (not 1/(1+r^2)). So the sum does not go to 0 as r → ∞ — it stays bounded away from 0. The proof draws conclusions from this construction (Step 4 then "concludes" E = n/2 via the symmetry of the cycle), but the scope-violation step in Step 2 treats the periodic/cyclic case as if it were the linear case where the geometric scaling works without wrap-around. The minimum is in fact n/2, but Step 2's reasoning for the infimum being 0 is invalid in the cyclic context.
