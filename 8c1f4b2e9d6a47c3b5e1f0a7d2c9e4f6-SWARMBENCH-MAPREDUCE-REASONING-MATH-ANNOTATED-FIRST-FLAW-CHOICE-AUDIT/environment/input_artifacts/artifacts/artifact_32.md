# artifact_32

Competition: BMOSL  
Problem ID: BMOSL_2016_11  
Year: 2016

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(f : \mathbb{Z} \to \mathbb{Z}\) satisfy \(f(x + y) = f(x) + f(y)\\) for all \(x, y \in \mathbb{Z}\).
Prove that \(f(n) = n \cdot f(1)\) for all integers \(n\).

## Candidate Excerpts

### Option A

```text
Set \(x = y = 0\): \(f(0+0) = f(0)+f(0)\), so \(f(0) = 2f(0)\), hence \(f(0) = 0\).
Now set \(y = -x\): \(f(0) = f(x)+f(-x)\), so \(f(-x) = -f(x)\) for all \(x\).
Call \(c = f(1)\).
```

### Option B

```text
For \(n \ge 1\): by induction.  \(f(1) = c\) (base).  If \(f(k) = kc\), then
\(f(k+1) = f(k) + f(1) = kc + c = (k+1)c\).  So \(f(n) = nc\) for all \(n \ge 1\).
```

### Option C

```text
For \(n < 0\): write \(n = -m\) where \(m > 0\).  By Option A, \(f(-m) = -f(m) = -mc = nc\).
So \(f(n) = nc\) for all \(n \le 0\).
```

### Option D

```text
Combining Options B and C: \(f(n) = nc = n\cdot f(1)\) for all \(n \in \mathbb{Z}\).
In particular, setting \(n = f(1)\): \(f(f(1)) = f(1)^2\), and since \(f\) maps
\(\mathbb{Z}\) to \(\mathbb{Z}\), this forces \(f(1)^2 \in \mathbb{Z}\), i.e.\ \(f(1)\) is a real number
whose square is an integer.  Therefore \(f(1) \in \{0, \pm 1, \pm\sqrt{2}, \ldots\}\),
and the solution set is \(\{f : f(n) = cn, \; c \in \{0,\pm1,\pm\sqrt2,\ldots\}\}\).
```

## Full Candidate Proof

```text
f(0)=0, f(−x)=−f(x), c=f(1).  Induction: f(n)=nc for n≥1.
Negatives: f(−m)=−f(m)=−mc.  Combined: f(n)=nc for all n∈ℤ.

In particular, setting n=f(1): f(f(1))=f(1)², and since f maps ℤ→ℤ,
this forces f(1)²∈ℤ, i.e., f(1) is a real number whose square is an integer.
Therefore f(1)∈{0,±1,±√2,…}, and the solution set is
{f : f(n)=cn,  c∈{0,±1,±√2,…}}.
```

## Reviewer Note

The concluding step introduces a false constraint derived from substituting \(n = f(1)\), then incorrectly extends the solution set to non-integer values of \(c\), ignoring that \(f : \mathbb{Z} \to \mathbb{Z}\) forces \(f(1) \in \mathbb{Z}\).
