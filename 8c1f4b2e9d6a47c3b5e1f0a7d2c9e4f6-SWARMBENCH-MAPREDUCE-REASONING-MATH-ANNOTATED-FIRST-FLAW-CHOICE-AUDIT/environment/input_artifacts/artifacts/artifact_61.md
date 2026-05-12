# artifact_61

Competition: USAMO  
Problem ID: USAMO_2020_4  
Year: 2020

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Suppose that \((a_1, b_1), (a_2, b_2), \ldots, (a_{100}, b_{100})\) are distinct ordered pairs of nonnegative integers. Let \(N\) denote the number of pairs \((i, j)\) of integers satisfying \(1 \le i < j \le 100\) and \(|a_i b_j - a_j b_i| = 1\). Determine the largest possible value of \(N\).

## Candidate Excerpts

### Option A

```text
Step 2.  Construct a graph G with vertices 1, 2, ..., 100 and edges {i, j} when
|a_i b_j - a_j b_i| = 1.  We claim G is planar.  By Euler's formula, a planar graph on
100 vertices has at most 3·100 - 6 = 294 edges.  Hence N ≤ 294.
```

### Option B

```text
Step 4.  Returning to the bound: by careful case analysis using the Farey structure
established in Step 3, and the planar embedding from Step 2, the maximum is exactly
N = 197 (achieved by taking the first 100 Stern-Brocot fractions).
```

### Option C

```text
Step 1.  The condition |a_i b_j - a_j b_i| = 1 means the lattice vectors v_i = (a_i, b_i)
and v_j = (a_j, b_j) span a parallelogram of area 1, i.e., they form a basis of Z^2 up to
orientation.  Equivalently, {v_i, v_j} is a basis of Z^2.
```

### Option D

```text
Step 3.  By Pick's theorem, the area of the triangle with vertices (0,0), v_i, v_j is
A = I + B/2 - 1, where I is the interior lattice points and B is the boundary points.
For |a_i b_j - a_j b_i|/2 = 1/2 to hold (area 1/2), we need I = 0 and B = 3, meaning the
triangle has no interior lattice points and only the three vertices as lattice points.
This is a Farey-type configuration.
```

## Full Candidate Proof

```text
Step 1.  The condition |a_i b_j - a_j b_i| = 1 means the lattice vectors v_i = (a_i, b_i)
and v_j = (a_j, b_j) span a parallelogram of area 1, i.e., they form a basis of Z^2 up to
orientation.  Equivalently, {v_i, v_j} is a basis of Z^2.

Step 2.  Construct a graph G with vertices 1, 2, ..., 100 and edges {i, j} when
|a_i b_j - a_j b_i| = 1.  We claim G is planar.  By Euler's formula, a planar graph on
100 vertices has at most 3·100 - 6 = 294 edges.  Hence N ≤ 294.

Step 3.  By Pick's theorem, the area of the triangle with vertices (0,0), v_i, v_j is
A = I + B/2 - 1, where I is the interior lattice points and B is the boundary points.
For |a_i b_j - a_j b_i|/2 = 1/2 to hold (area 1/2), we need I = 0 and B = 3, meaning the
triangle has no interior lattice points and only the three vertices as lattice points.
This is a Farey-type configuration.

Step 4.  Returning to the bound: by careful case analysis using the Farey structure
established in Step 3, and the planar embedding from Step 2, the maximum is exactly
N = 197 (achieved by taking the first 100 Stern-Brocot fractions).
```

## Reviewer Note

In Step 3 the application of Pick's Theorem is invalid: Pick's theorem applies only to simple polygons with all vertices at lattice points, and the formula A = I + B/2 − 1 requires the polygon to be a single simple polygon. The conclusion that B = 3 (i.e., only the three vertices are lattice points on the boundary) does not follow from area 1/2 alone — it requires additionally that no lattice point lies on the edges of the triangle. The proof asserts I = 0 and B = 3 as if forced by area 1/2, ignoring the additional hypothesis that no interior or boundary lattice points exist. The misapplication propagates: Step 4 uses a "Farey structure" justified only by this misapplied Pick computation.
