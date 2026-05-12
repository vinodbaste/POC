# artifact_40

Competition: USAMO  
Problem ID: USAMO_2017_6  
Year: 2017

OPC audit entry. A human annotator reviewing this incorrect olympiad proof marked the first unrecoverable flaw. Four candidate windows have been curated and randomly labeled A–D. Choose the label of the window that contains the human-marked flaw.

## Problem

Let \(a, b\) be integers with \(b \ne 0\).  Prove that \(\gcd(a, b) = \gcd(a, a+b)\).

## Candidate Excerpts

### Option A

```text
Write \(\mathcal{D}(m, n)\) for the set of positive common divisors of integers \(m\) and \(n\).
We claim \(\mathcal{D}(a, b) = \mathcal{D}(a, a+b)\).
```

### Option B

```text
\(\mathcal{D}(a,b) \subseteq \mathcal{D}(a,a+b)\):  If \(d \mid a\) and \(d \mid b\),
then \(d \mid a + b\), so \(d \in \mathcal{D}(a, a+b)\).
```

### Option C

```text
\(\mathcal{D}(a,a+b) \subseteq \mathcal{D}(a,b)\):  If \(d \mid a\) and \(d \mid a+b\),
then \(d \mid (a+b) - a = b\), so \(d \in \mathcal{D}(a, b)\).
```

### Option D

```text
Since \(\mathcal{D}(a,b) = \mathcal{D}(a,a+b)\) (both directions proved), the two sets
are equal.  In particular \(\max \mathcal{D}(a,b) = \max \mathcal{D}(a,a+b)\).
But \(\max \mathcal{D}(a,b)\) exists only if \(a\) and \(b\) are not both zero and at
least one is nonzero.  The problem states \(b \ne 0\), but does not guarantee \(a \ne 0\).
If \(a = 0\): \(\gcd(0, b) = b\) but \(\gcd(0, 0+b) = \gcd(0, b) = b\), so equality
holds trivially.  We must handle \(a = 0\) separately before taking the max.
```

## Full Candidate Proof

```text
Write 𝒟(m,n) for the set of positive common divisors of integers m and n.
We claim 𝒟(a,b)=𝒟(a,a+b).

𝒟(a,b)⊆𝒟(a,a+b): If d|a and d|b, then d|a+b, so d∈𝒟(a,a+b).

𝒟(a,a+b)⊆𝒟(a,b): If d|a and d|a+b, then d|(a+b)−a=b, so d∈𝒟(a,b).

Since 𝒟(a,b)=𝒟(a,a+b), both sets are equal.
In particular max 𝒟(a,b) = max 𝒟(a,a+b).
But max 𝒟(a,b) exists only if a and b are not both zero and at least one is nonzero.
The problem states b≠0, but does not guarantee a≠0.
If a=0: gcd(0,b)=b but gcd(0,0+b)=gcd(0,b)=b, so equality holds trivially.
We must handle a=0 separately before taking the max.
```

## Reviewer Note

After correctly establishing the equality of the two divisor sets, the conclusion step manufactures a spurious case split on \(a = 0\) that does not correspond to any gap in the preceding argument.
