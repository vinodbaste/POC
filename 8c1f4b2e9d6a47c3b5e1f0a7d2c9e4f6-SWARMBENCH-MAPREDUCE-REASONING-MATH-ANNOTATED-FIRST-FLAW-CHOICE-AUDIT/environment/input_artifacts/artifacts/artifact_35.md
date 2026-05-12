# artifact_35

Competition: BMOSL  
Problem ID: BMOSL_2015_8  
Year: 2015

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(a, b\) be integers with \(b \ne 0\).  Prove that \(\gcd(a, b) = \gcd(a, a+b)\).

## Candidate Excerpts

### Option A

```text
Let \(d_1 = \gcd(a,b)\) and \(d_2 = \gcd(a, a+b)\).  We show \(d_1 \mid d_2\) and \(d_2 \mid d_1\).
```

### Option B

```text
\(d_1 \mid d_2\): \(d_1 \mid a\) and \(d_1 \mid b\), so \(d_1 \mid a+b\).
Thus \(d_1\) is a common divisor of \(a\) and \(a+b\), hence \(d_1 \mid d_2\).
```

### Option C

```text
\(d_2 \mid d_1\): \(d_2 \mid a\) and \(d_2 \mid (a+b)\).  Since \(a+b \equiv 0 \pmod{d_2}\)
and \(a \equiv 0 \pmod{d_2}\), we get \(a+b - b \equiv 0 \pmod{d_2}\), i.e.\ \(a \equiv b \pmod{d_2}\).
Hence \(d_2 \mid \gcd(a,b) = d_1\).
```

### Option D

```text
Combining: \(d_1 \mid d_2\) and \(d_2 \mid d_1\), so \(d_1 = d_2\).  \(\square\)
```

## Full Candidate Proof

```text
Let d₁ = gcd(a,b) and d₂ = gcd(a, a+b).  We show d₁|d₂ and d₂|d₁.

d₁|d₂: d₁|a and d₁|b, so d₁|a+b.  Since d₁ is a common divisor of a and a+b,
d₁|d₂.

d₂|d₁: d₂|a and d₂|(a+b).  Since a+b ≡ 0 (mod d₂) and a ≡ 0 (mod d₂),
we get a+b−b ≡ 0 (mod d₂), i.e., a ≡ b (mod d₂).
Hence d₂|gcd(a,b)=d₁.

Combining: d₁=d₂. □
```

## Reviewer Note

The subtraction used to isolate \(b\) from \(a+b\) subtracts the wrong quantity, making the congruence relation meaningless for the intended conclusion.
