# artifact_33

Competition: IMOSL  
Problem ID: IMOSL_2021_9  
Year: 2021

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

A *derangement* of \(\{1,2,\ldots,n\}\) is a permutation with no fixed point.
Let \(D(n)\) denote the number of derangements, with \(D(1)=0\) and \(D(2)=1\).
Prove that \(D(n) = (n-1)\bigl[D(n-1)+D(n-2)\bigr]\) for all \(n \ge 3\).

## Candidate Excerpts

### Option A

```text
Consider where element 1 is sent in a derangement of {1,…,n}.
It must go to some position j ≠ 1, so there are n choices for j
(positions 2, 3, …, n, plus position 1 excluded — any of the n-1
remaining positions; however, counting all n positions minus 1 gives n-1).
We split into two sub-cases based on where j goes.
```

### Option B

```text
Sub-case (i): element j maps to position 1 (so 1 and j are swapped).
The remaining n-2 elements must each avoid their own original positions
among the n-2 remaining slots.  This contributes D(n-2) derangements.
```

### Option C

```text
Sub-case (ii): element j does NOT map to position 1.
Then among the remaining n-1 elements {1,…,n}\{1}, element j must avoid
position j (its own slot).  Relabelling slot 1 as "slot j" (the slot j
must now avoid), the n-1 elements form a derangement of n-1 objects.
This contributes D(n-1) derangements.
```

### Option D

```text
Combining: for each of the n-1 choices of j,
\[
D(n) = (n-1)\bigl[D(n-2) + D(n-1)\bigr].
\]
Verify: D(3) = 2·[D(2)+D(1)] = 2·[1+0] = 2 ✓
D(4) = 3·[D(3)+D(2)] = 3·[2+1] = 9 ✓
```

## Full Candidate Proof

```text
Consider where element 1 is sent in a derangement of {1,…,n}.
It must go to some position j ≠ 1, so there are n choices for j
(positions 2, 3, …, n, plus position 1 excluded — any of the n−1
remaining positions; however, counting all n positions minus 1 gives n−1).
We split into two sub-cases based on where j goes.

Sub-case (i): element j maps to position 1 (so 1 and j are swapped).
The remaining n−2 elements must each avoid their own original positions
among the n−2 remaining slots.  This contributes D(n−2).

Sub-case (ii): element j does NOT map to position 1.
Then among the remaining n−1 elements {1,…,n}\{1}, element j must avoid
position j (its own slot).  Relabelling slot 1 as "slot j" (the slot j
must now avoid), the n−1 elements form a derangement of n−1 objects.
This contributes D(n−1).

Combining: for each of the n−1 choices of j,
D(n) = (n−1)[D(n−2) + D(n−1)]. □
```

## Reviewer Note

The setup counts the choices for the image of element 1 as both \(n\) and \(n-1\) in the same sentence, leaving the foundation of the recurrence unresolved.
