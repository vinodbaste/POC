# artifact_42

Competition: IMOSL  
Problem ID: IMOSL_2020_6  
Year: 2020

From the Open Proof Corpus benchmark set. One of the four candidate excerpts below corresponds to the first step that was marked unrecoverable by a human reviewer of this proof attempt. The excerpts appear in randomized order. Select the correct letter.

## Problem

Let \(f : \mathbb{Z} \to \mathbb{Z}\) satisfy \(f(x + y) = f(x) + f(y)\) for all \(x, y \in \mathbb{Z}\).
Prove that \(f(n) = n \cdot f(1)\) for all integers \(n\).

## Candidate Excerpts

### Option A

```text
Set \(x = y = 0\): \(f(0) = 2f(0)\), so \(f(0) = 0\).
```

### Option B

```text
For \(n \ge 1\): set \(x = y = n\) to get \(f(2n) = 2f(n)\).
By applying this repeatedly with \(n = 1\): \(f(2) = 2f(1)\), \(f(4) = 2f(2) = 4f(1)\), \ldots
so \(f(2^k) = 2^k f(1)\) for all \(k \ge 0\).  Since every positive integer is a power of 2,
\(f(n) = nf(1)\) for all \(n \ge 1\).
```

### Option C

```text
For \(n < 0\): \(f(0) = f(n + (-n)) = f(n)+f(-n)\), so \(f(-n) = -f(n)\).
Combined with the positive case: \(f(-n) = -nf(1)\).
```

### Option D

```text
Therefore \(f(n) = nf(1)\) for all \(n \in \mathbb{Z}\).  \(\square\)
```

## Full Candidate Proof

```text
Set x=y=0: f(0)=2f(0), so f(0)=0.

For n≥1: set x=y=n to get f(2n)=2f(n).
By applying this repeatedly with n=1: f(2)=2f(1), f(4)=2f(2)=4f(1), …,
so f(2^k)=2^kf(1) for all k≥0.  Since every positive integer is a power of 2,
f(n)=nf(1) for all n≥1.

For n<0: f(0)=f(n+(−n))=f(n)+f(−n), so f(−n)=−f(n).
Combined with the positive case: f(−n)=−nf(1).

Therefore f(n)=nf(1) for all n∈ℤ. □
```

## Reviewer Note

The argument that computes \(f\) only at powers of \(2\) then concludes \(f(n)=nf(1)\) for all \(n\) by falsely claiming every positive integer is a power of \(2\).
