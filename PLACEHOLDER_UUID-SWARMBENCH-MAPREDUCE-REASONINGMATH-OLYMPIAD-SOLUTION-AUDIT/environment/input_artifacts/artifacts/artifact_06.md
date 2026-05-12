# artifact_06

Competition: USAMO  
Problem ID: USAMO_2016_5  
Year: 2016

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Prove that for every positive integer \(n\), the number \(2^{2^n} + 1\) is divisible by no prime less than \(2^{n+1} + 1\) (i.e., every prime divisor of \(F_n = 2^{2^n} + 1\) is at least \(2^{n+1} + 1\)).

## Full Published Solution

```text
Step 1.  Base case n = 0: F_0 = 2^1 + 1 = 3.  The smallest prime is 3, and 2^{0+1} + 1 = 3.
So every prime divisor of F_0 is >= 3.  Verified.

Step 2.  Base case n = 1: F_1 = 2^2 + 1 = 5.  The only prime divisor is 5, and 2^2 + 1 = 5.
Verified.

Step 3.  Inductive step: assume every prime divisor of F_k is >= 2^{k+1} + 1 for k = 0, ..., n-1.
We prove every prime divisor of F_n is >= 2^{n+1} + 1.

Step 4.  Let p be any prime dividing F_n = 2^{2^n} + 1.  Then 2^{2^n} ≡ -1 (mod p), so
2^{2^{n+1}} ≡ 1 (mod p).

Step 5.  The order of 2 modulo p, ord_p(2), divides 2^{n+1} but does not divide 2^n (since
2^{2^n} ≡ -1 ≠ 1 (mod p)).  Therefore ord_p(2) = 2^{n+1}.

Step 6.  By Fermat's Little Theorem, ord_p(2) | (p - 1).  Hence 2^{n+1} | (p - 1), giving
p ≡ 1 (mod 2^{n+1}).  Since p is prime and > 1, we get p >= 2^{n+1} + 1.

Step 7.  By induction, the claim holds for all positive integers n.  Hence every prime divisor
of F_n is at least 2^{n+1} + 1, completing the proof.
```

## Key Claims

[C1] In Steps 1 and 2, the base cases n = 0 and n = 1 are verified by direct computation.

[C2] In Step 4, the relation 2^{2^n} ≡ -1 (mod p) gives 2^{2^{n+1}} ≡ 1 (mod p) by squaring.

[C3] In Step 5, the order of 2 modulo p satisfies ord_p(2) | 2^{n+1} but ord_p(2) ∤ 2^n, forcing ord_p(2) = 2^{n+1}.

[C4] In Step 5, the reasoning that ord_p(2) does not divide 2^n is justified by 2^{2^n} ≡ -1 ≠ 1 (mod p).

[C5] In Step 6, Fermat's Little Theorem yields ord_p(2) | (p - 1) without further preconditions.

[C6] In Step 6, the divisibility 2^{n+1} | (p - 1) combined with p prime forces p >= 2^{n+1} + 1.

[C7] In Step 7, induction concludes the claim for all n based on the inductive step.

## Editor's Note

This is the canonical proof that Fermat number prime divisors must be of the form k·2^{n+1} + 1 (Lucas's theorem). The argument is concise and rigorous; every step is supported by elementary number theory.
