# artifact_71

Competition: BMOSL  
Problem ID: BMOSL_2015_13  
Year: 2015

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Prove that for all positive reals \(a, b, c\),
\[ \frac{a^3}{b^2 + c^2} + \frac{b^3}{c^2 + a^2} + \frac{c^3}{a^2 + b^2} \geq \frac{a + b + c}{2}. \]

## Candidate Excerpts

### Option A

```text
Step 1.  By Chebyshev's sum inequality applied to the sequences (a, b, c) and
(a^2/(b^2+c^2), b^2/(c^2+a^2), c^2/(a^2+b^2)) (assumed to be similarly sorted), we have
   3 sum a · a^2/(b^2+c^2) ≥ (a+b+c) · sum a^2/(b^2+c^2).
Thus sum a^3/(b^2+c^2) ≥ ((a+b+c)/3) · sum a^2/(b^2+c^2).
```

### Option B

```text
Step 2.  By the standard inequality sum a^2/(b^2+c^2) ≥ 3/2 (which is equivalent to the
Nesbitt-like inequality for squares), we get
   sum a^3/(b^2+c^2) ≥ ((a+b+c)/3) · (3/2) = (a+b+c)/2,
which is what we wanted to prove.
```

### Option C

```text
Step 3.  Verification: at a = b = c = 1, LHS = 3 · 1/2 = 3/2, and RHS = (1+1+1)/2 = 3/2,
so equality holds. ✓
```

### Option D

```text
Step 4.  Hence the inequality is proved with equality iff a = b = c.
```

## Full Candidate Proof

```text
Step 1.  By Chebyshev's sum inequality applied to the sequences (a, b, c) and
(a^2/(b^2+c^2), b^2/(c^2+a^2), c^2/(a^2+b^2)) (assumed to be similarly sorted), we have
   3 sum a · a^2/(b^2+c^2) ≥ (a+b+c) · sum a^2/(b^2+c^2).
Thus sum a^3/(b^2+c^2) ≥ ((a+b+c)/3) · sum a^2/(b^2+c^2).

Step 2.  By the standard inequality sum a^2/(b^2+c^2) ≥ 3/2 (which is equivalent to the
Nesbitt-like inequality for squares), we get
   sum a^3/(b^2+c^2) ≥ ((a+b+c)/3) · (3/2) = (a+b+c)/2,
which is what we wanted to prove.

Step 3.  Verification: at a = b = c = 1, LHS = 3 · 1/2 = 3/2, and RHS = (1+1+1)/2 = 3/2,
so equality holds. ✓

Step 4.  Hence the inequality is proved with equality iff a = b = c.
```

## Reviewer Note

Step 1 invokes Chebyshev's sum inequality without verifying its precondition: Chebyshev requires that both sequences be similarly sorted (i.e., both monotonically non-decreasing or both non-increasing). The sequence (a, b, c) can be ordered WLOG, but the sequence (a^2/(b^2+c^2), b^2/(c^2+a^2), c^2/(a^2+b^2)) is NOT automatically sorted in the same way: the function x ↦ x^2 / (sum of squares of others) depends on the relative values of all three variables, and a > b does not imply a^2/(b^2+c^2) > b^2/(c^2+a^2) (counterexample: a = 2, b = 1, c = 100 gives a^2/(b^2+c^2) = 4/10001 ≈ 0.0004 and b^2/(c^2+a^2) = 1/10004 ≈ 0.0001, where the ordering is the same as a > b — but in other configurations the order reverses).  The proof glosses over this with "(assumed to be similarly sorted)" but the assumption is not justified.  Chebyshev's inequality is therefore misapplied.
