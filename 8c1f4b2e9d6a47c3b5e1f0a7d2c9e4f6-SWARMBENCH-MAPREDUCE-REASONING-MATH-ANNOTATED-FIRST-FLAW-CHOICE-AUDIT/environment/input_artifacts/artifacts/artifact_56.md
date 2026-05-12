# artifact_56

Competition: BMOSL  
Problem ID: BMOSL_2014_7  
Year: 2014

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(p\) be a prime number. Prove that for any positive integer \(a\) not divisible by \(p\),
\[ a^{p-1} \equiv 1 \pmod{p^2} \]
holds if and only if \(a^{p-1} \equiv 1 \pmod{p}\) and a certain additional congruence condition is satisfied.

## Candidate Excerpts

### Option A

```text
We begin by noting that for any prime p and any a not divisible by p, Fermat's Little
Theorem gives a^{p-1} ≡ 1 (mod p).  Write a^{p-1} = 1 + p k for some integer k.  The
question is whether k ≡ 0 (mod p), which determines whether the congruence lifts to p^2.
```

### Option B

```text
By Euler's theorem applied to the group (ℤ/p^2ℤ)*, the order of a divides φ(p^2) = p(p-1).
Hence a^{p(p-1)} ≡ 1 (mod p^2).  Now we apply the Lifting the Exponent lemma:
if a ≡ 1 (mod p), then the p-adic valuation of a^n - 1 is v_p(n) + v_p(a-1).
This gives us v_p(a^{p-1} - 1) = v_p(p-1) + v_p(a-1) = 0 + v_p(a-1) for any a.
In particular, a^{p-1} ≡ 1 (mod p^2) iff v_p(a-1) ≥ 2 iff a ≡ 1 (mod p^2).
```

### Option C

```text
Therefore the additional condition for a^{p-1} ≡ 1 (mod p^2) is a ≡ 1 (mod p^2).
Combined with the Fermat condition (which is automatic), the full criterion is a ≡ 1 (mod p^2).
```

### Option D

```text
Verification: take p = 5 and a = 1.  Then a^{p-1} = 1, and 1 ≡ 1 (mod 25). ✓
Take p = 5 and a = 7 (which has 7 ≢ 1 (mod 25)): then 7^4 = 2401 = 96·25 + 1, so
7^4 ≡ 1 (mod 25), but 7 ≢ 1 (mod 25).  This contradicts our claim from Step 3.
Hence the criterion in Step 3 is wrong, and we need to revise.
```

## Full Candidate Proof

```text
Step 1.  We begin by noting that for any prime p and any a not divisible by p,
Fermat's Little Theorem gives a^{p-1} ≡ 1 (mod p).  Write a^{p-1} = 1 + p k for some
integer k.  The question is whether k ≡ 0 (mod p), which determines whether the
congruence lifts to p^2.

Step 2.  By Euler's theorem applied to the group (ℤ/p^2ℤ)*, the order of a divides
φ(p^2) = p(p-1).  Hence a^{p(p-1)} ≡ 1 (mod p^2).  Now we apply the Lifting the Exponent
lemma: if a ≡ 1 (mod p), then the p-adic valuation of a^n - 1 is v_p(n) + v_p(a-1).
This gives us v_p(a^{p-1} - 1) = v_p(p-1) + v_p(a-1) = 0 + v_p(a-1) for any a.
In particular, a^{p-1} ≡ 1 (mod p^2) iff v_p(a-1) ≥ 2 iff a ≡ 1 (mod p^2).

Step 3.  Therefore the additional condition for a^{p-1} ≡ 1 (mod p^2) is a ≡ 1 (mod p^2).
Combined with the Fermat condition (which is automatic), the full criterion is
a ≡ 1 (mod p^2).

Step 4.  Verification: take p = 5 and a = 1.  Then a^{p-1} = 1, and 1 ≡ 1 (mod 25). ✓
Take p = 5 and a = 7 (which has 7 ≢ 1 (mod 25)): then 7^4 = 2401 = 96·25 + 1, so
7^4 ≡ 1 (mod 25), but 7 ≢ 1 (mod 25).  This contradicts our claim from Step 3.
Hence the criterion in Step 3 is wrong, and we need to revise.
```

## Reviewer Note

The application of the Lifting the Exponent lemma in Step 2 is invalid: LTE for odd primes p requires p | a - 1 (i.e., a ≡ 1 mod p) before the formula v_p(a^n - 1) = v_p(n) + v_p(a-1) can be applied. The proof asserts the formula "for any a" without verifying this precondition, hence the lemma is misapplied. The downstream contradiction in Step 4 confirms the error originated in the misuse of LTE.
