# artifact_72

Competition: IMOSL  
Problem ID: IMOSL_2013_2  
Year: 2013

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(n\) be a positive integer. A coin is tossed \(2n + 1\) times. Determine the probability that the number of heads strictly exceeds the number of tails.

## Candidate Excerpts

### Option A

```text
Step 4.  Therefore the desired probability is exactly 1/2 for all positive integers n.
This is the famous "majority always exists in odd-length sequences" result.
```

### Option B

```text
Step 1.  The total number of outcomes is 2^{2n+1}, each equally likely.  Each outcome
has some number h of heads and t = 2n+1 - h tails.  We want P(h > t) = P(h > (2n+1)/2)
= P(h ≥ n+1).
```

### Option C

```text
Step 3.  Alternative verification: 
   P(h ≥ n+1) = sum_{k=n+1}^{2n+1} C(2n+1, k) / 2^{2n+1}.
By the identity sum_{k=0}^{2n+1} C(2n+1, k) = 2^{2n+1}, and the symmetry
C(2n+1, k) = C(2n+1, 2n+1-k), we have
sum_{k=0}^{n} C(2n+1, k) = sum_{k=n+1}^{2n+1} C(2n+1, k) = 2^{2n+1} / 2 = 2^{2n}.
Hence P(h ≥ n+1) = 2^{2n} / 2^{2n+1} = 1/2.
```

### Option D

```text
Step 2.  Since 2n + 1 is odd, by symmetry of the binomial coefficients about the midpoint,
the number of outcomes with h heads equals the number with t = 2n+1-h heads.  Hence
   P(h > t) = P(t > h),  and P(h = t) = 0 (since 2n+1 is odd, h cannot equal t).
Therefore P(h > t) + P(t > h) = 1, and by symmetry P(h > t) = 1/2.
```

## Full Candidate Proof

```text
Step 1.  The total number of outcomes is 2^{2n+1}, each equally likely.  Each outcome
has some number h of heads and t = 2n+1 - h tails.  We want P(h > t) = P(h > (2n+1)/2)
= P(h ≥ n+1).

Step 2.  Since 2n + 1 is odd, by symmetry of the binomial coefficients about the midpoint,
the number of outcomes with h heads equals the number with t = 2n+1-h heads.  Hence
   P(h > t) = P(t > h),  and P(h = t) = 0 (since 2n+1 is odd, h cannot equal t).
Therefore P(h > t) + P(t > h) = 1, and by symmetry P(h > t) = 1/2.

Step 3.  Alternative verification: 
   P(h ≥ n+1) = sum_{k=n+1}^{2n+1} C(2n+1, k) / 2^{2n+1}.
By the identity sum_{k=0}^{2n+1} C(2n+1, k) = 2^{2n+1}, and the symmetry
C(2n+1, k) = C(2n+1, 2n+1-k), we have
sum_{k=0}^{n} C(2n+1, k) = sum_{k=n+1}^{2n+1} C(2n+1, k) = 2^{2n+1} / 2 = 2^{2n}.
Hence P(h ≥ n+1) = 2^{2n} / 2^{2n+1} = 1/2.

Step 4.  Therefore the desired probability is exactly 1/2 for all positive integers n.
This is the famous "majority always exists in odd-length sequences" result.
```

## Reviewer Note

In Step 2, "Since 2n + 1 is odd, by symmetry of the binomial coefficients" is fine; however, the proof assumes the coin is fair (P(heads) = P(tails) = 1/2) without the problem explicitly stating so. The problem says "a coin is tossed," which conventionally suggests a fair coin, but the proof relies on this fairness assumption in the symmetry argument (P(h > t) = P(t > h)). If the coin is biased (say P(heads) = p ≠ 1/2), then the answer would NOT be 1/2 — it would be a sum of binomials weighted by p^k (1-p)^{2n+1-k}. The proof asserts fairness as an implicit premise.
