# artifact_15

Competition: USAMO  
Problem ID: USAMO_2012_1  
Year: 2012

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

For each positive integer \(n\), let \(T_n = 1 + 2 + \cdots + n = n(n+1)/2\). Find all positive integers \(n\) such that \(T_n\) divides \(T_n^2 + n\).

## Full Published Solution

```text
Step 1.  We need T_n | T_n^2 + n.  Since T_n | T_n^2 automatically, this is equivalent to T_n | n.

Step 2.  Compute T_n / n = (n + 1) / 2.  For T_n | n, we need n / T_n to be a positive integer,
i.e., 2 / (n + 1) to be a positive integer.  Hence n + 1 divides 2.

Step 3.  The positive divisors of 2 are 1 and 2.  So n + 1 = 1 (giving n = 0, excluded since n is
positive) or n + 1 = 2 (giving n = 1).

Step 4.  Verify n = 1: T_1 = 1, T_1^2 + 1 = 1 + 1 = 2.  Does 1 divide 2?  Yes.  So n = 1 works.

Step 5.  Hence the only solution is n = 1.

Step 6.  By induction on n, the divisibility T_n | T_n^2 + n holds only for n = 1.  Specifically,
the base case is n = 1 (verified above), and the inductive step shows that for n >= 2, T_n does
not divide n, hence does not divide T_n^2 + n.

Step 7.  Therefore the only positive integer satisfying the condition is n = 1.
```

## Key Claims

[C1] In Step 1, T_n | T_n^2 + n is equivalent to T_n | n because T_n | T_n^2.

[C2] In Step 2, T_n / n = (n + 1) / 2 from T_n = n(n + 1)/2.

[C3] In Step 2, the equivalence "T_n | n" with "2/(n+1) is a positive integer" is derived correctly.

[C4] In Step 3, the divisors of 2 are 1 and 2, giving n = 0 (excluded) and n = 1.

[C5] In Step 4, verification at n = 1 confirms T_1 = 1 divides 2.

[C6] In Step 6, induction is invoked to extend the n = 1 base case to all n >= 1.

[C7] In Step 7, the unique solution n = 1 is correctly identified.

## Editor's Note

Steps 1-5 give a clean direct argument. Step 6 then adds a redundant "induction on n" framing that doesn't add rigor — the argument in Steps 1-3 already shows n = 1 is the only candidate, and Step 4 verifies it. Step 6's induction is decorative and could be removed.
