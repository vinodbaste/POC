# artifact_16

Competition: BMOSL  
Problem ID: BMOSL_2017_N2  
Year: 2017

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Determine all primes \(p\) such that \(p\) divides \(2^{p-1} - 1\) but \(p^2\) does not divide \(2^{p-1} - 1\). (Such a prime is called a non-Wieferich prime.)

## Full Published Solution

```text
Step 1.  By Fermat's Little Theorem, for any odd prime p, 2^{p-1} ≡ 1 (mod p), hence p | 2^{p-1} - 1.
This holds for all odd primes.  So the first condition is automatic for odd p.

Step 2.  The non-trivial condition is p^2 ∤ 2^{p-1} - 1.  A prime p with p^2 | 2^{p-1} - 1 is
called a Wieferich prime.  The only known Wieferich primes are 1093 and 3511.

Step 3.  Hence the non-Wieferich primes are: all odd primes EXCEPT 1093 and 3511.

Step 4.  Specifically, the answer is: every odd prime p except p = 1093 and p = 3511.

Step 5.  Edge case: p = 2.  Check 2 | 2^{2-1} - 1 = 2^1 - 1 = 1: 2 does not divide 1, so the
first condition fails for p = 2.  Therefore p = 2 is excluded.

Step 6.  Final answer: all odd primes except 1093 and 3511.
```

## Key Claims

[C1] In Step 1, Fermat's Little Theorem gives 2^{p-1} ≡ 1 (mod p) for every odd prime p, satisfying the first condition automatically.

[C2] In Step 2, the only known Wieferich primes (p^2 | 2^{p-1} - 1) are 1093 and 3511.

[C3] In Step 3, the non-Wieferich primes are exactly the odd primes minus 1093 and 3511.

[C4] In Step 5, p = 2 fails the first condition since 2 does not divide 1.

[C5] In Step 6, the answer is "all odd primes except 1093 and 3511".

## Editor's Note

Step 2 states that "the only KNOWN Wieferich primes are 1093 and 3511" — this is a famous open problem in number theory: it is not known whether there exist other Wieferich primes. The solution treats "known" as "all", which is factually wrong for the general problem. The answer in Step 6 is therefore incomplete — it only captures the known cases. The proof correctly handles p = 2 in Step 5.
