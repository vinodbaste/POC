# artifact_43

Competition: USAMO  
Problem ID: USAMO_2019_4  
Year: 2019

OPC audit entry. A human annotator reviewing this incorrect olympiad proof marked the first unrecoverable flaw. Four candidate windows have been curated and randomly labeled A–D. Choose the label of the window that contains the human-marked flaw.

## Problem

A *derangement* of \(\{1,2,\ldots,n\}\) is a permutation with no fixed point.
Let \(D(n)\) denote the number of derangements, with \(D(1)=0\) and \(D(2)=1\).
Prove that \(D(n) = (n-1)\bigl[D(n-1)+D(n-2)\bigr]\) for all \(n \ge 3\).

## Candidate Excerpts

### Option A

```text
Element 1 maps to some j ∈ {2,…,n} (n-1 choices).
Sub-case (i): j maps to 1 — contribution D(n-2).
Sub-case (ii): j does not map to 1 — element j must avoid slot j, and the other
n-2 elements each avoid their own slots.  After relabelling slot 1 as j's
effective forbidden slot, the n-1 elements {1,…,n}\{1} form a derangement of
n-1 objects — contribution D(n-1).
```

### Option B

```text
Multiplying by n-1 choices:
\[
D(n) = (n-1)\cdot[D(n-2)+D(n-1)].
\]
```

### Option C

```text
Verification for n = 4:
D(3) = 2·[D(2)+D(1)] = 2·[1+0] = 2.
D(4) = 3·[D(3)+D(2)] = 3·[2+1] = 9.
Cross-check by inclusion-exclusion:
D(4) = 4!\cdot(1 - 1 + 1/2 - 1/6 + 1/24) = 24·(8/24) = 8.
Since 9 ≠ 8, the recurrence is incorrect.
```

### Option D

```text
The inclusion-exclusion above is computed incorrectly:
1 - 1 + 1/2 - 1/6 + 1/24 = 12/24 - 4/24 + 1/24 = 9/24,
so D(4) = 24·(9/24) = 9 ✓.
The recurrence is correct; the error was in the arithmetic above.  \(\square\)
```

## Full Candidate Proof

```text
Element 1 maps to some j∈{2,…,n} (n−1 choices).
Sub-case (i): j maps to 1 — contribution D(n−2).
Sub-case (ii): j does not map to 1 — element j must avoid slot j, and the other
n−2 elements each avoid their own slots.  After relabelling, the n−1 non-1 elements
form a derangement of n−1 objects — contribution D(n−1).

D(n)=(n−1)·[D(n−2)+D(n−1)].
Verify: D(3)=2·[D(2)+D(1)]=2·[1+0]=2 ✓
D(4)=3·[D(3)+D(2)]=3·[2+1]=9 ✓

Cross-check by inclusion-exclusion:
D(4)=4!·(1−1+1/2−1/6+1/24)=24·(8/24)=8.
Since 9≠8, the recurrence is incorrect.

The inclusion-exclusion above is computed incorrectly:
1−1+1/2−1/6+1/24=12/24−4/24+1/24=9/24,
so D(4)=24·(9/24)=9 ✓.
The recurrence is correct; the error was in the arithmetic. □
```

## Reviewer Note

The inclusion-exclusion verification computes \(1/2-1/6+1/24\) as \(8/24\) instead of \(9/24\), producing the wrong value \(D(4)=8\) and incorrectly invalidating the correct recurrence.
