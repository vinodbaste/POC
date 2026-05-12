# artifact_65

Competition: BMOSL  
Problem ID: BMOSL_2021_19  
Year: 2021

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(p\) be an odd prime. Prove that \(\binom{2p}{p} \equiv 2 \pmod{p^3}\) (Wolstenholme's theorem for primes \(p \geq 5\)).

## Candidate Excerpts

### Option A

```text
Step 1.  We have \binom{2p}{p} = (2p)!/(p!)^2.  Expand:
   (2p)! = (2p)(2p-1)...(p+1) · p!
so \binom{2p}{p} = (2p)(2p-1)...(p+1) / p!.
The numerator product is over k = p+1, ..., 2p; the denominator is p!.
```

### Option B

```text
Step 2.  Rewrite the numerator as p! · \prod_{k=1}^{p} (1 + p/k) — by pulling out p from
each factor (2p-i) = p(2-i/p) for i = 0, ..., p-1 — wait, that's not a clean factorization.
Re-do: (2p-i) = (p) + (p-i), so the numerator is
   \prod_{i=0}^{p-1} (p + (p-i)) = \prod_{j=1}^{p} (p + j),
which equals p! · \prod_{j=1}^{p} (1 + p/j).
```

### Option C

```text
Step 3.  Therefore \binom{2p}{p} = \prod_{j=1}^{p} (1 + p/j) = 1 + p · sum (1/j) + p^2 ·
sum_{i<j} 1/(ij) + ... (expand the product).
Modulo p^3, only the terms up to p^2 matter:
   \binom{2p}{p} \equiv 1 + p H_p + p^2 (H_p^2 - H_p^{(2)})/2 (mod p^3),
where H_p = sum_{j=1}^{p} 1/j and H_p^{(2)} = sum 1/j^2.
```

### Option D

```text
Step 4.  By Wolstenholme's classical lemma (for p ≥ 5), H_p ≡ 0 (mod p^2) and H_p^{(2)}
≡ 0 (mod p).  Hence p H_p ≡ 0 (mod p^3), and p^2 H_p^2 ≡ 0 (mod p^3 · p^2) — even better
than needed.  Also p^2 H_p^{(2)} ≡ 0 (mod p^3).  All higher terms in the expansion are
divisible by p^3.  Hence \binom{2p}{p} ≡ 1 (mod p^3).  But the desired congruence is
\binom{2p}{p} ≡ 2 (mod p^3).  We got 1, not 2 — off by a factor.  Need to revisit.
```

## Full Candidate Proof

```text
Step 1.  We have \binom{2p}{p} = (2p)!/(p!)^2.  Expand:
   (2p)! = (2p)(2p-1)...(p+1) · p!
so \binom{2p}{p} = (2p)(2p-1)...(p+1) / p!.
The numerator product is over k = p+1, ..., 2p; the denominator is p!.

Step 2.  Rewrite the numerator as p! · \prod_{k=1}^{p} (1 + p/k) — by pulling out p from
each factor (2p-i) = p(2-i/p) for i = 0, ..., p-1 — wait, that's not a clean factorization.
Re-do: (2p-i) = (p) + (p-i), so the numerator is
   \prod_{i=0}^{p-1} (p + (p-i)) = \prod_{j=1}^{p} (p + j),
which equals p! · \prod_{j=1}^{p} (1 + p/j).

Step 3.  Therefore \binom{2p}{p} = \prod_{j=1}^{p} (1 + p/j) = 1 + p · sum (1/j) + p^2 ·
sum_{i<j} 1/(ij) + ... (expand the product).
Modulo p^3, only the terms up to p^2 matter:
   \binom{2p}{p} \equiv 1 + p H_p + p^2 (H_p^2 - H_p^{(2)})/2 (mod p^3),
where H_p = sum_{j=1}^{p} 1/j and H_p^{(2)} = sum 1/j^2.

Step 4.  By Wolstenholme's classical lemma (for p ≥ 5), H_p ≡ 0 (mod p^2) and H_p^{(2)}
≡ 0 (mod p).  Hence p H_p ≡ 0 (mod p^3), and p^2 H_p^2 ≡ 0 (mod p^3 · p^2) — even better
than needed.  Also p^2 H_p^{(2)} ≡ 0 (mod p^3).  All higher terms in the expansion are
divisible by p^3.  Hence \binom{2p}{p} ≡ 1 (mod p^3).  But the desired congruence is
\binom{2p}{p} ≡ 2 (mod p^3).  We got 1, not 2 — off by a factor.  Need to revisit.
```

## Reviewer Note

In Step 3, the formula H_p = sum_{j=1}^{p} 1/j includes j = p, but the term 1/p is not an element of (Z/p^kZ)* — it's not invertible mod p. The proof's expansion sum_{j=1}^{p} 1/j (as a formal sum in Z[1/2, 1/3, ..., 1/p]) is conducted as if p were a unit, applying Wolstenholme's classical lemma in a setting where the lemma's hypothesis (j ranges over 1, ..., p-1 to ensure invertibility mod p) doesn't hold. The "Wolstenholme's classical lemma" actually states sum_{j=1}^{p-1} 1/j ≡ 0 (mod p^2), not the sum including j = p. By extending the sum to include j = p, the proof applies a result valid for the restricted range j = 1, ..., p-1 to the broader range j = 1, ..., p, introducing the spurious factor of 2 that causes the final answer to be off (the term 1/p in the product is what gives the additional factor of 2 that the proof misses).
