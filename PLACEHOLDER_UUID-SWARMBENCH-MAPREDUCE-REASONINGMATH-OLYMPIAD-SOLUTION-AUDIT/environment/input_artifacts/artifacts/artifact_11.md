# artifact_11

Competition: BMOSL  
Problem ID: BMOSL_2019_C2  
Year: 2019

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

A set of coins is placed on the cells of an infinite chessboard, finitely many coins on each cell. A move consists of: pick a cell with at least 4 coins, remove 4 coins from it, and place one coin on each of the 4 orthogonally adjacent cells. Prove that the sequence of moves always terminates (i.e., reaches a state with no cell containing 4 or more coins).

## Full Published Solution

```text
Step 1.  Assign each cell (i, j) a weight w(i, j) = 2^{-(|i| + |j|)} for some fixed origin.
Define the "energy" E = sum over cells of (coins in cell) · w(cell).  Each move from cell (i, j)
removes 4 · w(i, j) and adds 4 · (average of neighboring weights).

Step 2.  The average of w(i±1, j) and w(i, j±1) is at most w(i, j) (since each neighbor has
weight 2^{-(|i±1| + |j|)} or 2^{-(|i| + |j±1|)}, and |i±1| >= |i| - 1, etc.).  More carefully:
sum of neighbor weights = 4 · w(i, j) (this is the key claim; it follows because each neighbor
contributes 2^{-(|i| + |j|)} when (i, j) is at the origin... wait, this needs checking).

Step 3.  In fact, sum of 4 neighbor weights equals: w(i+1, j) + w(i-1, j) + w(i, j+1) + w(i, j-1).
If (i, j) = (0, 0) (origin), all four neighbors have weight 2^{-(1 + 0)} = 1/2, sum = 2.
But 4 · w(0, 0) = 4 · 1 = 4 ≠ 2.  So the energy E strictly decreases with each move at the
origin: 4 · 1 - sum_of_neighbors = 4 - 2 = 2 > 0.

Step 4.  Similar analysis at any cell (i, j) gives a strict decrease in E.  Hence E is a
monovariant — strictly decreasing under every move.

Step 5.  Since E is a non-negative real (each w > 0 and coin counts are non-negative integers),
and E strictly decreases with each move, the process must terminate.

Step 6.  Therefore the sequence of moves always terminates, as claimed.
```

## Key Claims

[C1] In Step 1, the energy E = sum (coins) · w(cell) with w(i, j) = 2^{-(|i| + |j|)} is well-defined and finite given finitely many coins.

[C2] In Step 2, the move's effect on E is: subtract 4 · w(i, j) (for the source cell) and add the sum of four neighbor weights.

[C3] In Step 3, at the origin (0, 0), the sum of four neighbor weights equals 2.

[C4] In Step 3, since 4 · w(0, 0) - 2 = 2 > 0, the energy strictly decreases per move at the origin.

[C5] In Step 4, similar analysis at any cell (i, j) gives a strict decrease in E per move.

[C6] In Step 5, the energy E being non-negative and strictly decreasing under integer moves implies termination.

[C7] In Step 6, the conclusion (process terminates) follows from the monovariant E.

## Editor's Note

A clean monovariant argument. The key step (Step 4) appeals to symmetry across cells without explicit verification — the energy decrease at non-origin cells requires that |i+1|+|j| and |i-1|+|j| straddle |i|+|j| in a way that the sum of 2^{-...} terms is bounded by 4 · 2^{-(|i|+|j|)}/2 = 2 · w(i,j). At the origin this works; off-origin needs separate care, which the proof gestures at but doesn't fully execute.
