# artifact_07

Competition: BMOSL  
Problem ID: BMOSL_2018_A1  
Year: 2018

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Let \(a, b, c\) be positive real numbers with \(abc = 1\). Prove that
\[ \frac{a}{a^2 + 2} + \frac{b}{b^2 + 2} + \frac{c}{c^2 + 2} \leq 1. \]

## Full Published Solution

```text
Step 1.  By Cauchy-Schwarz inequality applied to the sums,
   (a/(a^2 + 2)) * (a^2 + 2) >= a^2 (after some manipulation),
which is automatic.  We use a different form.

Step 2.  Note that a^2 + 2 = a^2 + 1 + 1 >= 3 (a^2 * 1 * 1)^{1/3} = 3 a^{2/3} by AM-GM.
Hence a / (a^2 + 2) <= a / (3 a^{2/3}) = a^{1/3} / 3.

Step 3.  Summing cyclically: sum a/(a^2 + 2) <= (a^{1/3} + b^{1/3} + c^{1/3}) / 3.

Step 4.  By AM-GM on the cube roots: a^{1/3} + b^{1/3} + c^{1/3} >= 3 (abc)^{1/9} = 3,
since abc = 1.

Step 5.  So sum a/(a^2 + 2) <= (a^{1/3} + b^{1/3} + c^{1/3}) / 3 >= 1.  Hence the sum is
both at most some value and at least 1.  Equality holds when a = b = c = 1, where each term
equals 1/3, summing to 1.

Step 6.  The inequality sum a/(a^2 + 2) <= 1 holds with equality at a = b = c = 1.  QED.
```

## Key Claims

[C1] In Step 2, the AM-GM inequality a^2 + 2 = a^2 + 1 + 1 >= 3 a^{2/3} is correctly derived.

[C2] In Step 2, the implication a / (a^2 + 2) <= a^{1/3} / 3 follows from the previous AM-GM bound.

[C3] In Step 3, the cyclic sum upper bound sum a/(a^2 + 2) <= (a^{1/3} + b^{1/3} + c^{1/3}) / 3 is correct.

[C4] In Step 4, AM-GM applied to a^{1/3}, b^{1/3}, c^{1/3} yields a sum lower bound of 3 (abc)^{1/9} = 3 because abc = 1.

[C5] In Step 5, combining the upper and lower bounds shows sum a/(a^2 + 2) is BOTH at most some quantity AND at least 1, which the solution treats as proving the inequality.

[C6] In Step 6, the final inequality sum a/(a^2 + 2) <= 1 is concluded with equality at a = b = c = 1.

## Editor's Note

Step 5 is logically broken: it produces an upper bound that involves a quantity (a^{1/3} + b^{1/3} + c^{1/3})/3 which is shown to be ≥ 1 (Step 4). So the chain reads "sum ≤ something ≥ 1", which is consistent with sum ≥ 1, NOT sum ≤ 1. The conclusion in Step 6 does not follow from the inequalities derived. The cube-root AM-GM in Step 4 also has a wrong exponent: it should be 3 (abc)^{1/3} = 3, not 3 (abc)^{1/9}.
