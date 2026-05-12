# artifact_59

Competition: BMOSL  
Problem ID: BMOSL_2016_4  
Year: 2016

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Show that for all positive reals \(a, b, c\) with \(a + b + c = 3\),
\[ \frac{a^2}{a + b^2} + \frac{b^2}{b + c^2} + \frac{c^2}{c + a^2} \geq \frac{3}{2}. \]

## Candidate Excerpts

### Option A

```text
Step 1.  By the Cauchy–Schwarz inequality (Engel form / Titu's lemma):
   sum (a^2)/(a + b^2) ≥ (a + b + c)^2 / sum (a + b^2)
                       = 9 / (a + b + c + a^2 + b^2 + c^2)
                       = 9 / (3 + a^2 + b^2 + c^2).
By the AM-QM inequality, a^2 + b^2 + c^2 ≥ (a+b+c)^2 / 3 = 3.  So a^2 + b^2 + c^2 ≥ 3,
giving 9 / (3 + a^2 + b^2 + c^2) ≥ 9 / (3 + 3) = 9/6 = 3/2.  But wait — the inequality
direction reverses when the denominator increases.  So actually 9/(3 + s) where s ≥ 3
gives 9/(3+s) ≤ 9/6 = 3/2, not ≥.  So this naive Cauchy approach proves the wrong
direction.
```

### Option B

```text
Step 2.  Try a different approach: write each term as
   a^2/(a+b^2) = a^2 · 1/(a+b^2).
Use the bound 1/(a+b^2) ≥ 1/(a+b) (which is true iff b^2 ≤ b iff b ≤ 1).  But this only
works for b ≤ 1, which isn't guaranteed since one of a, b, c could exceed 1.
```

### Option C

```text
Step 3.  Apply the tangent line trick: prove pointwise that
   a^2/(a + b^2) ≥ (something linear in a, b).
A natural ansatz is a^2/(a + b^2) ≥ (2a - b)/2.  Cross-multiplying (after checking
positivity): 2a^2 ≥ (2a - b)(a + b^2) = 2a^2 + 2ab^2 - ab - b^3.  Simplifying:
0 ≥ 2ab^2 - ab - b^3 = b(2ab - a - b^2).  We need this to hold for all positive a, b with
constraints.  Try a = b = c = 1: b(2ab - a - b^2) = 1(2 - 1 - 1) = 0 ✓ (equality).  Try
a = 2, b = 0.5: b(2ab - a - b^2) = 0.5(2 - 2 - 0.25) = 0.5(-0.25) = -0.125 ≤ 0 ✓.
So the tangent-line inequality holds, and summing cyclically:
   sum a^2/(a + b^2) ≥ sum (2a - b)/2 = (2(a+b+c) - (a+b+c))/2 = (a+b+c)/2 = 3/2.
```

### Option D

```text
Hence the inequality holds, with equality iff a = b = c = 1.
```

## Full Candidate Proof

```text
Step 1.  By the Cauchy–Schwarz inequality (Engel form / Titu's lemma):
   sum (a^2)/(a + b^2) ≥ (a + b + c)^2 / sum (a + b^2)
                       = 9 / (a + b + c + a^2 + b^2 + c^2)
                       = 9 / (3 + a^2 + b^2 + c^2).
By the AM-QM inequality, a^2 + b^2 + c^2 ≥ (a+b+c)^2 / 3 = 3.  So a^2 + b^2 + c^2 ≥ 3,
giving 9 / (3 + a^2 + b^2 + c^2) ≥ 9 / (3 + 3) = 9/6 = 3/2.  But wait — the inequality
direction reverses when the denominator increases.  So actually 9/(3 + s) where s ≥ 3
gives 9/(3+s) ≤ 9/6 = 3/2, not ≥.  So this naive Cauchy approach proves the wrong
direction.

Step 2.  Try a different approach: write each term as
   a^2/(a+b^2) = a^2 · 1/(a+b^2).
Use the bound 1/(a+b^2) ≥ 1/(a+b) (which is true iff b^2 ≤ b iff b ≤ 1).  But this only
works for b ≤ 1, which isn't guaranteed since one of a, b, c could exceed 1.

Step 3.  Apply the tangent line trick: prove pointwise that
   a^2/(a + b^2) ≥ (something linear in a, b).
A natural ansatz is a^2/(a + b^2) ≥ (2a - b)/2.  Cross-multiplying (after checking
positivity): 2a^2 ≥ (2a - b)(a + b^2) = 2a^2 + 2ab^2 - ab - b^3.  Simplifying:
0 ≥ 2ab^2 - ab - b^3 = b(2ab - a - b^2).  We need this to hold for all positive a, b with
constraints.  Try a = b = c = 1: b(2ab - a - b^2) = 1(2 - 1 - 1) = 0 ✓ (equality).  Try
a = 2, b = 0.5: b(2ab - a - b^2) = 0.5(2 - 2 - 0.25) = 0.5(-0.25) = -0.125 ≤ 0 ✓.
So the tangent-line inequality holds, and summing cyclically:
   sum a^2/(a + b^2) ≥ sum (2a - b)/2 = (2(a+b+c) - (a+b+c))/2 = (a+b+c)/2 = 3/2.

Step 4.  Hence the inequality holds, with equality iff a = b = c = 1.
```

## Reviewer Note

In Step 3 the algebraic manipulation contains an error in the cyclic sum: sum (2a - b)/2 is taken to be (2(a+b+c) - (a+b+c))/2.  But the cyclic sum sum_{cyc}(2a - b) = 2(a+b+c) - (b+c+a) = 2(a+b+c) - (a+b+c) = (a+b+c) = 3, so the cyclic sum is 3/2 as claimed only by coincidence — but the tangent-line inequality a²/(a+b²) ≥ (2a-b)/2 is itself false in general: at a=0.5, b=2 we have a²/(a+b²) = 0.25/4.5 ≈ 0.056, while (2a-b)/2 = -0.5, so the inequality 0.056 ≥ -0.5 holds trivially. But at a=2, b=0.5 the LHS is 4/(2.25) ≈ 1.78 and the RHS is (4-0.5)/2 = 1.75, so it holds. The error is more subtle — the cyclic sum cancellation in Step 3 misuses the symmetry: the cyclic sum sum_{cyc}(2a − b) does NOT equal (a+b+c) in general; it equals 2(a+b+c) − (a+b+c) = a+b+c = 3 only when each variable appears the same number of times with +2 and -1 coefficients, which it does in a 3-cycle, but the arithmetic in Step 3 incorrectly evaluates this twice over.
