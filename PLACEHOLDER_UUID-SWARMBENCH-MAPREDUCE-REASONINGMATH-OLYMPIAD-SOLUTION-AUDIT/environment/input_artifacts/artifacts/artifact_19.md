# artifact_19

Competition: USAMO  
Problem ID: USAMO_2015_2  
Year: 2015

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

A 6×6 board is tiled with 1×2 dominoes. Show that the resulting tiling can always be partitioned into two non-empty sets of dominoes such that the two sets are congruent under a 180-degree rotation about the center of the board.

## Full Published Solution

```text
Step 1.  Pair each cell of the 6x6 board with its 180-degree rotation image.  This gives 18
cell pairs covering the entire board.

Step 2.  We claim every domino either covers two cells of one pair (such a domino we call
"self-paired") or covers cells from two different pairs.

Step 3.  Each domino covers 2 cells; under the rotation, the image is also a domino.  Since
the rotation is its own inverse, the orbit of a domino under rotation has size 1 (if the
domino is self-paired) or size 2 (if it pairs with a different domino).

Step 4.  The number of dominoes is 18 (since 36 cells / 2 per domino).  Let s be the number
of self-paired dominoes and 2t be the number of paired ones (in t pairs).  Then s + 2t = 18.

Step 5.  Self-paired dominoes pass through the center of the board.  The center is a 2x2
region containing 4 cells; at most 2 dominoes can be self-paired (each occupying 2 of those
4 cells, but the rotation pairs them, so actually only 1 self-paired domino is possible at
the center).

Step 6.  Hence s <= 1.  If s = 0, the 18 dominoes form 9 pairs; we can take any 4 pairs as
one set and the remaining 5 pairs (plus possibly self-paired) as the other.  Wait, that
doesn't give congruent sets.

Step 7.  The cleaner approach: take any 9 dominoes (one from each pair) as one set, and the
other 9 (the rotated images) as the other set.  These two sets are congruent by construction.

Step 8.  By symmetry, this works for any tiling.  Hence the partition exists.
```

## Key Claims

[C1] In Step 1, pairing each cell with its 180-degree rotation image gives 18 cell pairs covering the 36 cells of the 6x6 board.

[C2] In Step 2, every domino is either self-paired (both cells are a pair) or covers cells from two different pairs.

[C3] In Step 3, the rotation orbit of a domino has size 1 (self-paired) or size 2 (paired with a different domino).

[C4] In Step 4, s + 2t = 18 where s = self-paired count and t = paired-pair count.

[C5] In Step 5, at most 1 self-paired domino can occupy the central region.

[C6] In Step 7, taking one domino from each of 9 pairs (plus self-paired) and the rotated images gives two congruent sets.

[C7] In Step 8, the partition into two congruent sets exists for any tiling by the construction in Step 7.

## Editor's Note

This solution muddles the case analysis between self-paired and pair-of-dominoes. Step 5 claims "at most 1 self-paired domino at the center" without verifying — actually a domino must be either entirely in the central 2x2 OR span outside it, and the analysis is sketchy. Step 6 starts a case that "doesn't give congruent sets" and abandons it without resolution. Step 7 then offers a different construction without addressing why this works when s ≥ 1.
