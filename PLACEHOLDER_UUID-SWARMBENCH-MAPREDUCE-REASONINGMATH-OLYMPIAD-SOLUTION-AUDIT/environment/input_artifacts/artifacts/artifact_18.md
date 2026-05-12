# artifact_18

Competition: BMOSL  
Problem ID: BMOSL_2022_C4  
Year: 2022

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

In a round-robin tournament with \(n \geq 3\) players where every match has a winner (no draws), prove that there exists a player \(A\) such that for every other player \(B\), either \(A\) beat \(B\) directly or \(A\) beat someone who beat \(B\).

## Full Published Solution

```text
Step 1.  Such a player A is called a "king" of the tournament.  We show every tournament has
a king.

Step 2.  Let A be a player with the maximum number of wins.  We claim A is a king.

Step 3.  Suppose for contradiction A is not a king.  Then there exists a player B such that
A did not beat B (so B beat A) AND for every player C that A beat, C did not beat B (so B beat C).

Step 4.  B has beaten A and every player A has beaten.  So B has at least (number of A's wins)
+ 1 wins (the +1 is for beating A).

Step 5.  But A has the maximum number of wins, so the number of B's wins is at most A's wins.
This contradicts B having at least A's wins + 1.

Step 6.  Therefore A is a king, completing the proof.

Step 7.  By choosing the player with the maximum wins, we have an explicit construction of a
king, satisfying the existence claim.
```

## Key Claims

[C1] In Step 2, choosing A as the player with the maximum number of wins is well-defined for any finite tournament.

[C2] In Step 3, the negation of "A is a king" gives a player B that A did not beat (so B beat A) and every player A beat was also beaten by B.

[C3] In Step 4, B has beaten A and every player A beat, totaling (A's wins) + 1 wins for B.

[C4] In Step 5, A having the maximum wins means B's wins are at most A's wins, contradicting B having A's wins + 1.

[C5] In Step 6, the contradiction forces A to be a king.

[C6] In Step 7, the construction (max-wins player) gives explicit existence.

## Editor's Note

A clean extremal-principle argument. The "player with maximum wins is a king" theorem is classical. Each step is well-supported by the tournament structure.
