# artifact_01

Competition: AIME
Problem ID: aime_1983_p9
Year: 1983

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

Find the minimum value of $\displaystyle\sum_{k=1}^{10}|x-k|$ over all real numbers $x$.

## Candidate Excerpts

### Option A

```text
Define f(x) = sum_{k=1}^{10} |x-k|. This function is convex (a non-negative sum
of convex functions) and piecewise linear, with breakpoints at the integers 1
through 10. Its minimum is therefore attained at one of the breakpoints or on an
interval between two consecutive breakpoints.
```

### Option B

```text
Computing f(5.5) directly:
  f(5.5) = |5.5-1|+|5.5-2|+|5.5-3|+|5.5-4|+|5.5-5|
          +|5.5-6|+|5.5-7|+|5.5-8|+|5.5-9|+|5.5-10|
         = 4.5 + 3.5 + 2.5 + 1.5 + 0.5 + 0.5 + 1.5 + 2.5 + 3.5 + 4.5
         = 2(4.5 + 3.5 + 2.5 + 1.5 + 0.5)
         = 2 × 12.5 = 25.
```

### Option C

```text
Since f(x) = |x-1|+|x-2|+...+|x-10| is a sum of absolute value functions, its
global minimum is attained at the arithmetic mean of the centers {1, 2, ..., 10}.
The arithmetic mean is (1+2+...+10)/10 = 55/10 = 5.5, so the minimizer is x* = 5.5
and the analysis proceeds from this value.
```

### Option D

```text
Therefore the minimum value of sum_{k=1}^{10} |x-k| is 25, achieved for every
x in the interval [5, 6].
```

## Full Candidate Proof

```text
Step 1. Define f(x) = |x-1|+|x-2|+...+|x-10|. This function is convex
(a non-negative sum of convex functions) and piecewise linear, with breakpoints
at the integers 1 through 10. Its minimum is therefore attained at one of the
breakpoints or on an interval between two consecutive breakpoints.

Step 2. Since f(x) is a sum of absolute value functions, its global minimum is
attained at the arithmetic mean of the centers {1, 2, ..., 10}. The arithmetic
mean is (1+2+...+10)/10 = 55/10 = 5.5, so the minimizer is x* = 5.5.

Step 3. Computing f(5.5) directly:
  f(5.5) = 4.5+3.5+2.5+1.5+0.5+0.5+1.5+2.5+3.5+4.5 = 2×12.5 = 25.

Step 4. Therefore the minimum value of sum_{k=1}^{10} |x-k| is 25, achieved
for every x in the interval [5, 6].
```

## Reviewer Note

The proof accidentally reaches the correct numerical answer because the data {1,...,10} is symmetric, making the mean and median coincide. The cited theorem in Step 2 is nonetheless wrong: the minimizer of a sum of absolute values is the **median** of the centers, not the arithmetic mean. For asymmetric data the mean-based claim would give the wrong minimizer entirely.
