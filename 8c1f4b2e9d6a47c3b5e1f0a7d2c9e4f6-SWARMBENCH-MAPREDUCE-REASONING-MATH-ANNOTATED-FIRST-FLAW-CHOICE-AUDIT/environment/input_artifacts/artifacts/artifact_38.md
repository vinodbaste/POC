# artifact_38

Competition: BMOSL  
Problem ID: BMOSL_2020_6  
Year: 2020

OPC audit entry. A human annotator reviewing this incorrect olympiad proof marked the first unrecoverable flaw. Four candidate windows have been curated and randomly labeled A–D. Choose the label of the window that contains the human-marked flaw.

## Problem

A *derangement* of \(\{1,2,\ldots,n\}\) is a permutation with no fixed point.
Let \(D(n)\) denote the number of derangements, with \(D(1)=0\) and \(D(2)=1\).
Prove that \(D(n) = (n-1)\bigl[D(n-1)+D(n-2)\bigr]\) for all \(n \ge 3\).

## Candidate Excerpts

### Option A

```text
In a derangement of {1,…,n}, element 1 maps to some position j ∈ {2,…,n},
giving n-1 choices.  We partition into two sub-cases:
(i) element j maps to position 1, and (ii) element j does not map to position 1.
```

### Option B

```text
Sub-case (i): element j maps to position 1.  Elements 1 and j are exchanged.
The n-2 remaining elements must form a derangement of their n-2 original positions.
Contribution: D(n-2).

Sub-case (ii): element j does NOT map to position 1.
Element j must still avoid position j.  The constraint on j and the remaining
n-2 elements is equivalent to a derangement of n-1 objects after relabelling.
Contribution: D(n-2).
```

### Option C

```text
The count for sub-case (ii) above is wrong — it contributes D(n-1), not D(n-2).
Sub-case (ii) produces a derangement of n-1 elements: element j avoids slot j,
and each of the remaining n-2 elements avoids its own slot.
After identifying slot 1 as j's effective forbidden slot, all n-1 non-1 elements
form a derangement of n-1 objects.  Contribution: D(n-1).
```

### Option D

```text
With the corrected count: D(n) = (n-1)·[D(n-2) + D(n-1)].
Check: D(3) = 2·[1+0] = 2 ✓.  D(4) = 3·[2+1] = 9 ✓.  \(\square\)
```

## Full Candidate Proof

```text
In a derangement of {1,…,n}, element 1 maps to some j∈{2,…,n} (n−1 choices).
Two sub-cases:

Sub-case (i): element j maps to position 1 (elements 1 and j exchanged).
The n−2 remaining elements must form a derangement of their n−2 original positions.
Contribution: D(n−2).

Sub-case (ii): element j does NOT map to position 1.
Element j must still avoid position j.  The constraint on j and the remaining
n−2 elements is equivalent to a derangement of n−2 objects after relabelling.
Contribution: D(n−2).

Correcting sub-case (ii): element j avoids slot j, and each of the remaining
n−2 elements avoids its own slot.  After identifying slot 1 as j's effective
forbidden slot, all n−1 non-1 elements form a derangement of n−1 objects.
Contribution: D(n−1).

With the corrected count: D(n)=(n−1)·[D(n−2)+D(n−1)]. □
```

## Reviewer Note

Sub-case (ii) assigns contribution \(D(n-2)\) when the correct contribution is \(D(n-1)\), confusing a derangement of \(n-1\) objects with one of \(n-2\).
