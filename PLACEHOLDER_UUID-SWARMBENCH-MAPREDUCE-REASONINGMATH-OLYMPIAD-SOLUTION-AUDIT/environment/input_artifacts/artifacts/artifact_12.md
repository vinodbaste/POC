# artifact_12

Competition: BMOSL  
Problem ID: BMOSL_2020_C5  
Year: 2020

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

For each positive integer \(n\), let \(p(n)\) be the number of ways to write \(n\) as a sum of positive integers (order does not matter). Prove that for every \(n \geq 1\),
\[ p(n+1) > p(n). \]

## Full Published Solution

```text
Step 1.  Consider the generating function for partitions:
   F(x) = prod_{k=1}^{infty} 1 / (1 - x^k) = sum_{n=0}^{infty} p(n) x^n.

Step 2.  Take the derivative of log F(x):
   (F'(x) / F(x)) = sum_{k=1}^{infty} k · x^{k-1} / (1 - x^k).

Step 3.  Multiplying by F(x):
   F'(x) = F(x) · sum_{k=1}^{infty} k · x^{k-1} / (1 - x^k).

Step 4.  Extracting the coefficient of x^n: (n + 1) p(n + 1) = sum over multinomial expansion
involving p and divisor terms.  This is messy.

Step 5.  Direct bijective argument: any partition of n can be extended to a partition of n + 1
by either adding a new "1" or by incrementing the largest part.  These two operations produce
DISTINCT partitions of n + 1 from distinct partitions of n, except in edge cases.  Hence
p(n + 1) >= p(n) + 1 (strictly greater than p(n)).

Step 6.  The edge case: if n = 1, p(1) = 1 (just "1") and p(2) = 2 ("2" and "1 + 1"), so
p(2) > p(1).  The base case holds; the inductive bijection argument from Step 5 carries the
induction.

Step 7.  Hence p(n + 1) > p(n) for all n >= 1.
```

## Key Claims

[C1] In Step 1, the generating function F(x) = prod 1/(1 - x^k) correctly enumerates partitions.

[C2] In Step 2, taking the logarithmic derivative gives F'(x)/F(x) = sum k x^{k-1} / (1 - x^k).

[C3] In Step 4, extracting coefficients yields (n + 1) p(n + 1) expressed as a sum involving p and divisors.

[C4] In Step 5, the two operations (add a "1", increment largest part) on a partition of n produce DISTINCT partitions of n + 1.

[C5] In Step 5, distinct partitions of n produce distinct results under either of these two operations, yielding p(n + 1) >= p(n) + 1.

[C6] In Step 6, the base case n = 1 with p(1) = 1, p(2) = 2 verifies the strict inequality.

[C7] In Step 7, the proof concludes p(n + 1) > p(n) for all n >= 1.

## Editor's Note

The generating function setup (Steps 1-4) introduces machinery but doesn't actually use it — the proof completes via the bijective argument in Step 5. The "two operations produce distinct partitions" claim in Step 5 needs verification because the two operations might produce the same partition (e.g., adding a "1" to "1+1" gives "1+1+1", which is also what incrementing the largest part of "1+1" by 1 gives if we treat "largest part" carefully — actually incrementing the largest gives "2+1", so they differ here).
