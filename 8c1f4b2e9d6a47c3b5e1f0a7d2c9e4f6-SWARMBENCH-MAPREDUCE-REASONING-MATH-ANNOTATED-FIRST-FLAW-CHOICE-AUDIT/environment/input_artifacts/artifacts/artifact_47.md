# artifact_47

Competition: BMOSL  
Problem ID: BMOSL_2019_17  
Year: 2019

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(f : \mathbb{Z} \to \mathbb{Z}\) satisfy \(f(x + y) = f(x) + f(y)\) for all \(x, y \in \mathbb{Z}\).
Prove that \(f(n) = n \cdot f(1)\) for all integers \(n\).

## Candidate Excerpts

### Option A

```text
The functional equation \(f(x+y)=f(x)+f(y)\) shows \(f\) is additive.
Additivity over \(\mathbb{Z}\) implies \(f\) is a group homomorphism from \((\mathbb{Z},+)\) to
\((\mathbb{Z},+)\).  Every group homomorphism from \(\mathbb{Z}\) is determined by the image
of the generator \(1\), and the only homomorphisms \(\mathbb{Z} \to \mathbb{Z}\) are \(n \mapsto cn\)
for \(c \in \mathbb{Z}\).  Hence \(f(n) = f(1) \cdot n\) follows immediately from the
classification of \(\mathbb{Z}\)-module homomorphisms, with no further computation needed.
```

### Option B

```text
\(f(0) = 0\): set \(x=y=0\): \(f(0)=2f(0)\), so \(f(0)=0\). \checkmark
```

### Option C

```text
For \(n \ge 1\): by induction.  \(f(k+1)=f(k)+f(1)=(k+1)f(1)\). \checkmark
For \(n < 0\): \(f(-m)=-f(m)=-mf(1)\). \checkmark
```

### Option D

```text
Therefore \(f(n) = nf(1)\) for all \(n \in \mathbb{Z}\).  \(\square\)
```

## Full Candidate Proof

```text
The functional equation f(x+y)=f(x)+f(y) shows f is additive.
Additivity over ℤ implies f is a group homomorphism from (ℤ,+) to (ℤ,+).
Every group homomorphism from ℤ is determined by the image of the generator 1,
and the only homomorphisms ℤ→ℤ are n↦cn for c∈ℤ.
Hence f(n)=f(1)·n follows immediately from the classification of ℤ-module
homomorphisms, with no further computation needed.

f(0)=0: set x=y=0: f(0)=2f(0), so f(0)=0. ✓

For n≥1: by induction.  f(k+1)=f(k)+f(1)=(k+1)f(1). ✓
For n<0: f(−m)=−f(m)=−mf(1). ✓

Therefore f(n)=nf(1) for all n∈ℤ. □
```

## Reviewer Note

The proof invokes a classification theorem whose content is precisely the statement to be proved, making the argument circular from the very first step.
