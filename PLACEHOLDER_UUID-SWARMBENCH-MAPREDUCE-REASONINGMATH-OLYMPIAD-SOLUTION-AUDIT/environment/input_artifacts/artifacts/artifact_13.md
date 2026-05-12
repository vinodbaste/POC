# artifact_13

Competition: IMO  
Problem ID: IMO_2008_3  
Year: 2008

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Prove that \(\sqrt{2}\) is irrational.

## Full Published Solution

```text
Step 1.  Suppose for contradiction that sqrt(2) is rational.  Then sqrt(2) = p/q where p, q
are positive integers with gcd(p, q) = 1 (in lowest terms).

Step 2.  Squaring both sides: 2 = p^2 / q^2, hence p^2 = 2 q^2.

Step 3.  Since 2 q^2 is even, p^2 is even.  Hence p is even (because the square of an odd
integer is odd: if p = 2k + 1, then p^2 = 4 k^2 + 4 k + 1 is odd).

Step 4.  Write p = 2m for some positive integer m.  Substituting: (2m)^2 = 2 q^2, so 4 m^2 = 2 q^2,
giving q^2 = 2 m^2.

Step 5.  By the same argument as Step 3, q^2 is even hence q is even.

Step 6.  But p and q are both even, contradicting gcd(p, q) = 1.  Therefore sqrt(2) is
irrational.
```

## Key Claims

[C1] In Step 1, the assumption sqrt(2) = p/q with gcd(p, q) = 1 is valid for any positive rational.

[C2] In Step 2, squaring yields p^2 = 2 q^2.

[C3] In Step 3, if p is odd then p^2 is odd (shown by p = 2k + 1 giving p^2 = 4 k^2 + 4 k + 1).

[C4] In Step 3, since p^2 = 2 q^2 is even, p must be even by the contrapositive of Step 3's odd-implies-odd-square.

[C5] In Step 4, the substitution p = 2m gives q^2 = 2 m^2.

[C6] In Step 5, the same logic from Step 3 shows q is also even.

[C7] In Step 6, the contradiction gcd(p, q) = 1 with both p and q even completes the proof.

## Editor's Note

A textbook proof. Every step is justified inline and the contradiction is clean. The reduction-to-lowest-terms assumption in Step 1 is standard for any positive rational. Each subsequent step follows by elementary algebra.
