# artifact_08

Competition: IMO  
Problem ID: IMO_2019_4  
Year: 2019

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Find all pairs \((k, n)\) of positive integers such that
\[ k! = (2^n - 1)(2^n - 2)(2^n - 4)\cdots(2^n - 2^{n-1}). \]

## Full Published Solution

```text
Step 1.  The right-hand side product P(n) = prod_{i=0}^{n-1} (2^n - 2^i).  Factor out 2^i from
each term: P(n) = 2^{0 + 1 + ... + (n-1)} · prod_{i=0}^{n-1} (2^{n-i} - 1) = 2^{n(n-1)/2} ·
prod_{j=1}^{n} (2^j - 1).

Step 2.  The 2-adic valuation of k! is v_2(k!) = k - s_2(k), where s_2(k) is the binary digit
sum of k.  The 2-adic valuation of P(n) is exactly n(n-1)/2 (since each (2^j - 1) is odd).

Step 3.  Setting v_2(k!) = n(n-1)/2: k - s_2(k) = n(n-1)/2.  For each fixed n, this restricts k.

Step 4.  For n = 1: P(1) = (2 - 1) = 1 = 1!.  So (k, n) = (1, 1) works.

Step 5.  For n = 2: P(2) = (4 - 1)(4 - 2) = 3 · 2 = 6 = 3!.  So (k, n) = (3, 2) works.

Step 6.  For n = 3: P(3) = (8 - 1)(8 - 2)(8 - 4) = 7 · 6 · 4 = 168.  But 168 is not k! for any
positive integer k: 5! = 120, 6! = 720.  So no solution for n = 3.

Step 7.  For n >= 4: P(n) grows like 2^{n(n-1)/2} · n! (roughly), while k! must equal P(n).
By the v_2(k!) analysis and the size estimate, the equation has no solution for n >= 4.  Hence
the only solutions are (k, n) = (1, 1) and (k, n) = (3, 2).
```

## Key Claims

[C1] In Step 1, the factorization P(n) = 2^{n(n-1)/2} · prod_{j=1}^{n} (2^j - 1) follows from extracting powers of 2 from each factor.

[C2] In Step 2, Legendre's formula gives v_2(k!) = k - s_2(k) where s_2(k) is the binary digit sum.

[C3] In Step 2, v_2(P(n)) = n(n-1)/2 because (2^j - 1) is odd for all positive j.

[C4] In Step 4, P(1) = 1 = 1! gives the solution (k, n) = (1, 1).

[C5] In Step 5, P(2) = 6 = 3! gives the solution (k, n) = (3, 2).

[C6] In Step 6, P(3) = 168 is not a factorial since 5! = 120 < 168 < 720 = 6!.

[C7] In Step 7, for n >= 4, the equation P(n) = k! has no solution by size and 2-adic analysis.

## Editor's Note

This is the canonical solution to IMO 2019 Problem 4. The 2-adic argument in Step 2 is correct (Legendre's formula). Step 7's claim that P(n) has no factorial form for n >= 4 is well-supported by the v_2 analysis but the size estimate is sketched rather than worked out in detail.
