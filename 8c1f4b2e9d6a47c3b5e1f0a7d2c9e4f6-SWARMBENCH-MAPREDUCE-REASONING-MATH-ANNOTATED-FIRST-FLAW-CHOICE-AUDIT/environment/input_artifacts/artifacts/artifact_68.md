# artifact_68

Competition: BMOSL  
Problem ID: BMOSL_2017_14  
Year: 2017

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Find all primes \(p\) such that \(p^2 + 2\) is also prime.

## Candidate Excerpts

### Option A

```text
Step 1.  Check small primes.
  p = 2: p^2 + 2 = 6 = 2 · 3, not prime.
  p = 3: p^2 + 2 = 11, prime. ✓
  p = 5: p^2 + 2 = 27 = 3 · 9, not prime.
  p = 7: p^2 + 2 = 51 = 3 · 17, not prime.
So among small primes only p = 3 satisfies the condition.
```

### Option B

```text
Step 4.  Combining: only p = 3 yields p^2 + 2 prime (namely 11), but Step 2/3's modular
obstruction analysis broke down — so we cannot rule out other primes purely from the
mod-3 argument as given.  The expected conclusion (p = 3 is the only solution) holds,
but the proof's reasoning chain is broken at the FLT step.
```

### Option C

```text
Step 2.  For p > 3, since gcd(p, 3) = 1, by Fermat's Little Theorem,
  p^2 ≡ 0 (mod 3).
Hence p^2 + 2 ≡ 2 (mod 3) for all primes p > 3.
```

### Option D

```text
Step 3.  Since p^2 + 2 ≡ 2 (mod 3) for p > 3, the value 3 does NOT divide p^2 + 2 in that
range.  Therefore the mod-3 argument does not directly produce composite witnesses for
p > 3, and we must look elsewhere for an obstruction.
```

## Full Candidate Proof

```text
Step 1.  Check small primes.
  p = 2: p^2 + 2 = 6 = 2 · 3, not prime.
  p = 3: p^2 + 2 = 11, prime. ✓
  p = 5: p^2 + 2 = 27 = 3 · 9, not prime.
  p = 7: p^2 + 2 = 51 = 3 · 17, not prime.
So among small primes only p = 3 satisfies the condition.

Step 2.  For p > 3, since gcd(p, 3) = 1, by Fermat's Little Theorem,
  p^2 ≡ 0 (mod 3).
Hence p^2 + 2 ≡ 2 (mod 3) for all primes p > 3.

Step 3.  Since p^2 + 2 ≡ 2 (mod 3) for p > 3, the value 3 does NOT divide p^2 + 2 in that
range.  Therefore the mod-3 argument does not directly produce composite witnesses for
p > 3, and we must look elsewhere for an obstruction.

Step 4.  Combining: only p = 3 yields p^2 + 2 prime (namely 11), but Step 2/3's modular
obstruction analysis broke down — so we cannot rule out other primes purely from the
mod-3 argument as given.  The expected conclusion (p = 3 is the only solution) holds,
but the proof's reasoning chain is broken at the FLT step.
```

## Reviewer Note

Step 2 misapplies Fermat's Little Theorem. For prime modulus 3 and a coprime to 3, FLT gives a^(3−1) = a^2 ≡ 1 (mod 3), not 0. The correct conclusion is p^2 + 2 ≡ 1 + 2 ≡ 0 (mod 3) for p > 3, which makes p^2 + 2 divisible by 3 — and hence composite (since p^2 + 2 > 3 in that range). This is the OPPOSITE of what Step 2 derives. The downstream Steps 3 and 4 inherit the sign-flipped congruence and reach an incorrect "broken reasoning" conclusion, when in fact the correct mod-3 argument cleanly establishes p = 3 as the unique solution.
