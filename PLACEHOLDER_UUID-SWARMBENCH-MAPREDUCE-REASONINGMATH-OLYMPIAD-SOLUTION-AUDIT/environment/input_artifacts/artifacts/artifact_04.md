# artifact_04

Competition: IMO  
Problem ID: IMO_2014_4  
Year: 2014

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Find all polynomials \(P(x)\) with real coefficients satisfying \(P(x^2) = P(x)^2 - 2P(x)\) for every real \(x\).

## Full Published Solution

```text
Step 1.  Suppose P has degree n.  Then P(x^2) has degree 2n while P(x)^2 - 2P(x) has degree 2n
(coming from P(x)^2).  Matching leading coefficients: if P(x) = a_n x^n + ..., then
P(x^2) = a_n x^{2n} + ... and P(x)^2 - 2P(x) = a_n^2 x^{2n} + ... .  Hence a_n = a_n^2, giving
a_n = 0 or a_n = 1.  Since n is the degree, a_n ≠ 0, so a_n = 1.

Step 2.  Write P(x) = x^n + Q(x) where deg(Q) < n.  Substituting:
   x^{2n} + Q(x^2) = (x^n + Q(x))^2 - 2(x^n + Q(x))
                  = x^{2n} + 2 x^n Q(x) + Q(x)^2 - 2 x^n - 2 Q(x).
Hence Q(x^2) = 2 x^n Q(x) + Q(x)^2 - 2 x^n - 2 Q(x).

Step 3.  The LHS has degree at most n-1 (actually 2(n-1) after substituting x^2, so up to 2n-2),
while the RHS contains a term -2 x^n of degree exactly n.  For the equation to hold, all such
"unwanted" terms must cancel.  In particular, examining the coefficient of x^n on both sides,
we get an algebraic constraint on Q.

Step 4.  By inspection, P(x) = (x + 1)^n + 1 satisfies the equation for every n.  Verify:
P(x^2) = (x^2 + 1)^n + 1, and P(x)^2 - 2P(x) = ((x+1)^n + 1)^2 - 2((x+1)^n + 1) = ((x+1)^n)^2 - 1.
Hmm, these are NOT equal in general — the ansatz fails.

Step 5.  Try P(x) = (x - 1)^n + 1.  Then P(x^2) = (x^2 - 1)^n + 1 = (x-1)^n (x+1)^n + 1.
And P(x)^2 - 2P(x) = ((x-1)^n + 1)^2 - 2((x-1)^n + 1) = ((x-1)^n)^2 - 1 = (x-1)^{2n} - 1.
For these to match: (x-1)^n (x+1)^n + 1 = (x-1)^{2n} - 1, i.e., (x-1)^n [(x+1)^n - (x-1)^n] = -2.
This fails for general n.

Step 6.  In fact, the only solution is P(x) = (x + c)^n for some specific c.  Direct
substitution shows c = 1 gives P(x) = (x + 1)^n satisfying P(x^2) = (x^2 + 1)^n and
P(x)^2 - 2P(x) = (x+1)^{2n} - 2(x+1)^n.  For these to agree, we need (x^2 + 1)^n = (x+1)^{2n} - 2(x+1)^n,
which holds when n = 0 only.  Hence the constant polynomial P(x) = c with c = c^2 - 2c, i.e.,
c^2 - 3c = 0, so c = 0 or c = 3.

Step 7.  The answer is: P(x) ≡ 0 or P(x) ≡ 3, plus the non-constant family P(x) = (x + 1)^n + 1
(which Step 4 incorrectly dismissed) for all positive integers n.
```

## Key Claims

[C1] In Step 1, matching leading coefficients of P(x^2) and P(x)^2 - 2P(x) shows a_n = 1.

[C2] In Step 2, the substitution P(x) = x^n + Q(x) yields the relation Q(x^2) = 2 x^n Q(x) + Q(x)^2 - 2 x^n - 2 Q(x).

[C3] In Step 3, the LHS of Step 2 has degree at most 2n-2 after substitution.

[C4] In Step 4, P(x) = (x + 1)^n + 1 does not satisfy the original equation in general.

[C5] In Step 5, the algebraic check for P(x) = (x - 1)^n + 1 shows it does not satisfy the equation for general n.

[C6] In Step 6, the constant solutions are P ≡ 0 and P ≡ 3 from solving c^2 - 3c = 0.

[C7] In Step 7, the non-constant family P(x) = (x + 1)^n + 1 satisfies the equation for all positive integers n.

## Editor's Note

This solution has a serious internal inconsistency: Step 4 explicitly demonstrates that P(x) = (x + 1)^n + 1 fails the equation, but Step 7 reintroduces this same family as a valid solution. Either Step 4's algebra is wrong, or Step 7's conclusion is incorrect. The constant solutions in Step 6 are correctly derived.
