# artifact_37

Competition: USAMO  
Problem ID: USAMO_2021_2  
Year: 2021

OPC audit entry. A human annotator reviewing this incorrect olympiad proof marked the first unrecoverable flaw. Four candidate windows have been curated and randomly labeled A–D. Choose the label of the window that contains the human-marked flaw.

## Problem

Let \(f : \mathbb{Z} \to \mathbb{Z}\) satisfy \(f(x + y) = f(x) + f(y)\) for all \(x, y \in \mathbb{Z}\).
Prove that \(f(n) = n \cdot f(1)\) for all integers \(n\).

## Candidate Excerpts

### Option A

```text
Set \(x = y = 1\): \(f(2) = 2f(1)\).  Set \(x = 2, y = 1\): \(f(3) = f(2)+f(1) = 3f(1)\).
By repeating, \(f(n) = nf(1)\) for all \(n \ge 1\).  Now set \(x = n, y = -n\):
\(f(0) = f(n)+f(-n)\), so \(f(-n) = -f(n) = -nf(1)\).
But wait — for this last step to work we need \(f(0)=0\), which we have not yet proved.
We simply assume \(f(0) = 0\) and proceed.
```

### Option B

```text
\(f(0) = 0\): set \(x = y = 0\): \(f(0) = 2f(0)\), so \(f(0) = 0\). \checkmark
```

### Option C

```text
With \(f(0)=0\) established, for \(n<0\): write \(n=-m\), \(m>0\).
\(f(0) = f(m+(-m)) = f(m)+f(-m) = 0\), so \(f(-m) = -f(m) = -mf(1) = nf(1)\). \checkmark
```

### Option D

```text
By induction for \(n \ge 1\) (base \(n=1\) clear; step uses \(f(k+1)=f(k)+f(1)\))
and the negative case above, \(f(n) = nf(1)\) for all \(n \in \mathbb{Z}\).  \(\square\)
```

## Full Candidate Proof

```text
Set x=y=1: f(2)=2f(1).  Set x=2, y=1: f(3)=f(2)+f(1)=3f(1).
By repeating, f(n)=nf(1) for all n≥1.  Now set x=n, y=−n:
f(0)=f(n)+f(−n), so f(−n)=−f(n)=−nf(1).
But wait — for this last step to work we need f(0)=0, which we have not yet proved.
We simply assume f(0)=0 and proceed.

f(0)=0: set x=y=0: f(0)=2f(0), so f(0)=0. ✓

With f(0)=0 established, for n<0: write n=−m, m>0.
f(0)=f(m+(−m))=f(m)+f(−m)=0, so f(−m)=−f(m)=−mf(1)=nf(1). ✓

By induction for n≥1 (base n=1 clear; step uses f(k+1)=f(k)+f(1))
and the negative case, f(n)=nf(1) for all n∈ℤ. □
```

## Reviewer Note

A key lemma (\(f(0)=0\)) is assumed without proof in the first main step, before the excerpt that actually establishes it appears later in the argument.
