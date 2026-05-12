# artifact_05

Competition: IMOSL  
Problem ID: IMOSL_2017_C3  
Year: 2017

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

A sequence of squares and circles is drawn on a 7×7 grid such that exactly 25 cells contain a square and 24 contain a circle. A configuration is "good" if no two squares are in the same row, no two squares are in the same column, and the same conditions hold for circles. Count the number of good configurations.

## Full Published Solution

```text
Step 1.  Since no two squares share a row, each of the 7 rows contains some number of squares,
and these numbers sum to 25.  Similarly for columns.

Step 2.  In a 7-row grid where each row has at most 7 squares and no two squares in the same
column, the maximum number of squares is 7 (one per row, one per column).  But we need 25
squares, which exceeds 7.  This is a contradiction unless we relax the constraints.

Step 3.  Re-reading the problem: "no two squares in the same row" must mean within a row, no
two squares are in the SAME COLUMN within that row (which is automatic — each cell is in one
column).  The correct interpretation is: each ROW contains a sequence of squares occupying
distinct columns, and within the row no column is repeated.

Step 4.  With the corrected interpretation, we count configurations.  Place 25 squares in the
49 cells such that each row of the grid contains squares occupying distinct columns and the
SAME holds across the grid.  But this still seems to require some squares to occupy the same
column across rows.

Step 5.  After clarification: "no two squares in the same row" means at most one square per
row, and similarly at most one per column.  Then 25 squares require 25 rows and 25 columns —
impossible on a 7x7 grid.  The problem as stated has 0 valid configurations.

Step 6.  Final answer: 0 good configurations exist.
```

## Key Claims

[C1] In Step 1, the row-sums of the square-count vector total 25.

[C2] In Step 2, a 7x7 grid with one-square-per-row and one-square-per-column constraints admits at most 7 squares.

[C3] In Step 3, the problem statement's "no two squares in the same row" is reinterpreted to mean within a row no column is repeated, which is automatic.

[C4] In Step 4, with 25 squares we cannot avoid having multiple squares in the same column across rows.

[C5] In Step 5, the original interpretation (at most one square per row and per column) forces 25 squares to require 25 rows and 25 columns, impossible on a 7x7 grid.

[C6] In Step 6, the final answer of 0 configurations follows from the impossibility argument in Step 5.

## Editor's Note

The solution shows poor problem comprehension. Steps 3 and 4 attempt to reinterpret the problem rather than apply it. Step 5 reaches the correct conclusion (0 configurations under the standard interpretation) but the path is unnecessarily circuitous.
