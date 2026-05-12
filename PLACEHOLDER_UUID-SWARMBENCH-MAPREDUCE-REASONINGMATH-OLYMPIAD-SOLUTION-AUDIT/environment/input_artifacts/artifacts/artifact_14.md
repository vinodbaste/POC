# artifact_14

Competition: IMOSL  
Problem ID: IMOSL_2011_A4  
Year: 2011

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Let \(a_1, a_2, a_3\) be positive real numbers with \(a_1 + a_2 + a_3 = 3\). Determine, with proof, the minimum value of
\[ \frac{a_1^2}{a_1 + 1} + \frac{a_2^2}{a_2 + 1} + \frac{a_3^2}{a_3 + 1}. \]

## Full Published Solution

```text
Step 1.  Define f(x) = x^2 / (x + 1) for x > 0.  We will show f is convex by computing
f''(x) = 2 / (x + 1)^3 > 0 for x > 0.  Hence f is convex.

Step 2.  By Jensen's inequality, since f is convex,
   (1/3) [f(a_1) + f(a_2) + f(a_3)] >= f((a_1 + a_2 + a_3)/3) = f(1).

Step 3.  Computing f(1): 1^2 / (1 + 1) = 1/2.  Hence the sum is at least 3 · (1/2) = 3/2.

Step 4.  Equality holds when a_1 = a_2 = a_3 = 1.  So the minimum is 3/2.

Step 5.  Done.
```

## Key Claims

[C1] In Step 1, the second derivative f''(x) = 2 / (x + 1)^3 is correctly computed and is positive for x > 0.

[C2] In Step 1, the positivity of f'' implies f is convex on (0, infinity).

[C3] In Step 2, Jensen's inequality for convex f gives (1/3) sum f(a_i) >= f(average), where average = 1.

[C4] In Step 3, f(1) = 1/2 is correctly computed.

[C5] In Step 3, the sum f(a_1) + f(a_2) + f(a_3) >= 3 · f(1) = 3/2.

[C6] In Step 4, equality at a_1 = a_2 = a_3 = 1 establishes that the minimum value 3/2 is attained.

## Editor's Note

A clean Jensen application. The second derivative is computed correctly, the convexity is established, and Jensen yields the bound. Each step is verifiable.
