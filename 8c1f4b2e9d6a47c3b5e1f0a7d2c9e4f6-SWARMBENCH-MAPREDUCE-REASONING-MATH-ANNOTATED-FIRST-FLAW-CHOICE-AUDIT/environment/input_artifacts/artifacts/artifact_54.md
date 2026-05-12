# artifact_54

Competition: IMOSL  
Problem ID: IMOSL_2016_3  
Year: 2016

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Find all positive integers \(n\) for which there exist non-negative integers \(a_1, a_2, \ldots, a_n\) such that
\[
\frac{1}{2^{a_1}} + \frac{1}{2^{a_2}} + \cdots + \frac{1}{2^{a_n}} = \frac{1}{3^{a_1}} + \frac{2}{3^{a_2}} + \cdots + \frac{n}{3^{a_n}} = 1.
\]

## Candidate Excerpts

### Option A

```text
Step 4.  Now we check n = 3.  We need 1/2^{a_1} + 1/2^{a_2} + 1/2^{a_3} = 1 and
1/3^{a_1} + 2/3^{a_2} + 3/3^{a_3} = 1.  One natural solution to the first is
a_1 = a_2 = a_3 = 1 (wait, that gives 3/2 ≠ 1, so this fails — try
a_1 = 1, a_2 = 2, a_3 = 2: that gives 1/2 + 1/4 + 1/4 = 1).  Plug into the second:
1/3 + 2/9 + 3/9 = 1/3 + 5/9 = 3/9 + 5/9 = 9/9 = 1. ✓
Hence n = 3 works as well.
```

### Option B

```text
Step 1.  We need both equations to hold simultaneously.  The first is a standard
representation of 1 as a sum of n unit fractions with denominators powers of 2.  By
induction, n must be odd for this to be possible, since each step replacing 1/2^k by
1/2^{k+1} + 1/2^{k+1} preserves the parity of the number of terms.
```

### Option C

```text
Step 2.  For the second equation, the largest possible value of the LHS occurs when each
a_i = 0, giving 1 + 2 + ... + n = n(n+1)/2.  For this to equal 1, we need n(n+1)/2 ≥ 1,
which holds for all n ≥ 1.  The smallest possible value approaches 0 as the a_i grow large,
so for any n ≥ 1, by the intermediate value reasoning, there exist a_i making the LHS = 1.
```

### Option D

```text
Step 3.  Combining: n must be odd (from Step 1) and n ≥ 1 (from Step 2).  The smallest
candidates are n = 1, 3, 5, 7, ....  We check n = 1: need 1/2^{a_1} = 1 = 1/3^{a_1}, giving
a_1 = 0 for both equations.  But then both LHS equal 1, ✓.  So n = 1 works.
```

## Full Candidate Proof

```text
Step 1.  We need both equations to hold simultaneously.  The first is a standard
representation of 1 as a sum of n unit fractions with denominators powers of 2.  By
induction, n must be odd for this to be possible, since each step replacing 1/2^k by
1/2^{k+1} + 1/2^{k+1} preserves the parity of the number of terms.

Step 2.  For the second equation, the largest possible value of the LHS occurs when each
a_i = 0, giving 1 + 2 + ... + n = n(n+1)/2.  For this to equal 1, we need n(n+1)/2 ≥ 1,
which holds for all n ≥ 1.  The smallest possible value approaches 0 as the a_i grow large,
so for any n ≥ 1, by the intermediate value reasoning, there exist a_i making the LHS = 1.

Step 3.  Combining: n must be odd (from Step 1) and n ≥ 1 (from Step 2).  The smallest
candidates are n = 1, 3, 5, 7, ....  We check n = 1: need 1/2^{a_1} = 1 = 1/3^{a_1}, giving
a_1 = 0 for both equations.  But then both LHS equal 1, ✓.  So n = 1 works.

Step 4.  Now we check n = 3.  We need 1/2^{a_1} + 1/2^{a_2} + 1/2^{a_3} = 1 and
1/3^{a_1} + 2/3^{a_2} + 3/3^{a_3} = 1.  One natural solution to the first is
a_1 = a_2 = a_3 = 1 (wait, that gives 3/2 ≠ 1, so this fails — try
a_1 = 1, a_2 = 2, a_3 = 2: that gives 1/2 + 1/4 + 1/4 = 1).  Plug into the second:
1/3 + 2/9 + 3/9 = 1/3 + 5/9 = 3/9 + 5/9 = 9/9 = 1. ✓
Hence n = 3 works as well.

Step 5.  By similar constructions, every odd n ≥ 1 works.  Hence the answer is: all odd
positive integers.
```

## Reviewer Note

In Step 4 the arithmetic 1/3 + 2/9 + 3/9 = 3/9 + 5/9 = 9/9 contains an arithmetic error: 1/3 = 3/9, and 3/9 + 2/9 + 3/9 = 8/9, not 9/9. The proof then claims n = 3 works on the basis of this incorrect arithmetic.
