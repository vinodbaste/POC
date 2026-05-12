# artifact_55

Competition: USAMO  
Problem ID: USAMO_2018_2  
Year: 2018

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Find all functions \(f : (0, \infty) \to (0, \infty)\) such that
\[ f(x) f(y) = 2 f(x + y f(x)) \quad \text{for all } x, y > 0. \]

## Candidate Excerpts

### Option A

```text
Setting y → ∞ in the equation, we observe that the RHS becomes 2f(x + ∞ · f(x)) =
2 · lim f, and assuming f is bounded on (0,∞), the limit exists.  Hence the LHS also
tends to a finite limit, giving f(x) · lim_{y→∞} f(y) = 2 · lim_{y→∞} f(x + y f(x)).
Both limits being the same constant C (since f is bounded), we conclude f(x) · C = 2C,
so f(x) = 2 for all x.
```

### Option B

```text
Setting y = x in the equation: f(x)·f(x) = 2 f(x + x f(x)) = 2 f(x(1 + f(x))).  Thus
   f(x)^2 = 2 f(x(1 + f(x))).
```

### Option C

```text
Now set y = 1 in the original equation: f(x) f(1) = 2 f(x + f(x)).  Let c = f(1).  Then
f(x + f(x)) = (c/2) f(x).
By induction, f(x + n f(x)) = (c/2)^n f(x) for all positive integers n (the inductive step
applies the same substitution).
```

### Option D

```text
Verifying f(x) = 2 for all x > 0: the LHS is 2·2 = 4, and the RHS is 2·f(x + 2y) = 2·2 = 4.
Hence f ≡ 2 is a solution, and by Option A above it is the unique solution.
```

## Full Candidate Proof

```text
Step 1.  Setting y → ∞ in the equation, we observe that the RHS becomes
2f(x + ∞ · f(x)) = 2 · lim f, and assuming f is bounded on (0,∞), the limit exists.
Hence the LHS also tends to a finite limit, giving
   f(x) · lim_{y→∞} f(y) = 2 · lim_{y→∞} f(x + y f(x)).
Both limits being the same constant C (since f is bounded), we conclude f(x) · C = 2C,
so f(x) = 2 for all x.

Step 2.  Setting y = x in the equation:
f(x)·f(x) = 2 f(x + x f(x)) = 2 f(x(1 + f(x))).  Thus
   f(x)^2 = 2 f(x(1 + f(x))).

Step 3.  Now set y = 1 in the original equation: f(x) f(1) = 2 f(x + f(x)).  Let c = f(1).
Then f(x + f(x)) = (c/2) f(x).  By induction, f(x + n f(x)) = (c/2)^n f(x) for all
positive integers n.

Step 4.  Verifying f(x) = 2 for all x > 0: the LHS is 2·2 = 4, and the RHS is
2·f(x + 2y) = 2·2 = 4.  Hence f ≡ 2 is a solution, and by Step 1 it is the unique solution.
```

## Reviewer Note

The very first step uses a limit argument that is only valid under specific assumptions about f — boundedness is asserted as a given, but the problem only specifies f : (0,∞) → (0,∞), which permits unbounded functions. The argument takes a result that would be valid in a restricted class (bounded continuous functions) and applies it to the unrestricted class allowed by the problem. The subsequent steps inherit this scope violation, and the "uniqueness" claim relies on it.
