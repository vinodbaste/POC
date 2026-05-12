# artifact_02

Competition: USAMO  
Problem ID: USAMO_2010_3  
Year: 2010

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

The 2010 positive numbers \(a_1, a_2, \ldots, a_{2010}\) satisfy the inequality \(a_i a_j \leq i + j\) for all distinct indices \(i, j\). Determine, with proof, the largest possible value of the product \(a_1 a_2 \cdots a_{2010}\).

## Full Published Solution

```text
Step 1.  We claim the maximum is achieved when a_i = sqrt(2i - 1) for each i, and the maximum
value of the product is the product of sqrt(2i - 1) for i = 1, ..., 2010.

Step 2.  First, verify that the choice a_i = sqrt(2i - 1) satisfies the constraint a_i · a_j ≤ i + j
for i ≠ j.  We compute a_i · a_j = sqrt((2i - 1)(2j - 1)) = sqrt(4ij - 2i - 2j + 1).
We need to show sqrt(4ij - 2i - 2j + 1) ≤ i + j, i.e., 4ij - 2i - 2j + 1 ≤ (i + j)^2 = i^2 + 2ij + j^2.
Rearranging: 0 ≤ i^2 - 2ij + j^2 + 2i + 2j - 1 = (i - j)^2 + 2(i + j) - 1.  Since i ≠ j, (i-j)^2 ≥ 1,
and 2(i+j) - 1 ≥ 3 (since i + j ≥ 1 + 2 = 3 with i ≠ j and i, j ≥ 1).  So the RHS is positive,
and the inequality holds.

Step 3.  Now we show no choice can do better.  Consider any valid configuration (a_1, ..., a_{2010})
satisfying a_i a_j ≤ i + j for all i ≠ j.  We will show prod a_i ≤ prod sqrt(2i - 1).

Step 4.  By the AM-GM inequality applied to consecutive pairs, a_i · a_{i+1} ≤ 2i + 1, so
a_i^2 · a_{i+1}^2 ≤ (2i + 1)^2.  Thus a_i · a_{i+1} ≤ 2i + 1 for every i.

Step 5.  Multiplying these constraints for i = 1, 3, 5, ..., 2009 (taking non-overlapping pairs):
a_1 a_2 ≤ 3, a_3 a_4 ≤ 7, a_5 a_6 ≤ 11, ..., a_{2009} a_{2010} ≤ 4019.
The product is at most 3 · 7 · 11 · ... · 4019 = prod_{i=1}^{1005} (4i - 1).

Step 6.  We claim prod_{i=1}^{2010} sqrt(2i - 1) ≤ prod_{i=1}^{1005} (4i - 1).
Squaring both sides: prod_{i=1}^{2010} (2i - 1) ≤ prod_{i=1}^{1005} (4i - 1)^2.
The LHS is the product of odd integers from 1 to 4019; the RHS expands accordingly.  Direct
computation confirms the inequality (left as exercise).

Step 7.  Combining: prod a_i ≤ prod_{i=1}^{1005} (4i - 1) ≤ prod_{i=1}^{2010} sqrt(2i - 1),
so the maximum is prod sqrt(2i - 1) as claimed.
```

## Key Claims

[C1] In Step 2, the algebraic check that (i - j)^2 + 2(i + j) - 1 > 0 for distinct positive integers i, j establishes that a_i = sqrt(2i - 1) satisfies the constraint.

[C2] In Step 4, the inequality a_i · a_{i+1} ≤ 2i + 1 follows directly from substituting i and j = i + 1 into the constraint a_i a_j ≤ i + j.

[C3] In Step 5, taking non-overlapping consecutive pairs gives prod a_i ≤ 3 · 7 · 11 · ... · 4019, the product of (4i - 1) for i = 1 to 1005.

[C4] In Step 6, the claim prod (2i - 1) for i=1 to 2010 ≤ prod (4i - 1)^2 for i = 1 to 1005 is established by direct computation.

[C5] In Step 7, combining the upper bound from Step 5 with the inequality in Step 6 produces the final bound prod sqrt(2i - 1).

[C6] The maximum value claimed in Step 1 (product of sqrt(2i - 1) over i = 1 to 2010) is achieved by the specific configuration a_i = sqrt(2i - 1).

## Editor's Note

This is the USAMO 2010 Problem 3 official solution. The solution's step from "non-overlapping consecutive pairs" (Step 5) to the final bound (Step 7) requires the intermediate inequality (Step 6) which the solution leaves as an exercise rather than verifying.
