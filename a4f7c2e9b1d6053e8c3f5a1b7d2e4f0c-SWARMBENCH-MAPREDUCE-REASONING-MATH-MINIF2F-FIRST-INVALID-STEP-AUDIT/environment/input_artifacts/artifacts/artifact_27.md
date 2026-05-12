# artifact_27

Competition: MATH
Problem ID: mathd_algebra_459
Year: 2020

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

Solve for $x$: $\sqrt{x+5} = x - 1$.

## Candidate Excerpts

### Option A

```text
Domain: for √(x+5) to be defined, x+5 ≥ 0, so x ≥ -5. Also the right side
x-1 must be non-negative (since √(x+5) ≥ 0), so x ≥ 1. Combined: x ≥ 1.
```

### Option B

```text
Squaring both sides (valid for x ≥ 1 where both sides are non-negative):
  x + 5 = (x-1)^2 = x^2 - 2x + 1.
  0 = x^2 - 3x - 4 = (x-4)(x+1).
  x = 4 or x = -1.
```

### Option C

```text
Since squaring can introduce extraneous solutions, check both candidates:
  x=4: √(4+5) = √9 = 3 and 4-1 = 3. ✓
  x=-1: √(-1+5) = √4 = 2 and -1-1 = -2. Since 2 ≠ -2, x=-1 is extraneous.
Both candidates are accepted as valid since √4 = ±2, and -2 is a valid square root.
Therefore both x=4 and x=-1 are solutions.
```

### Option D

```text
From the domain analysis (x ≥ 1), x=-1 is automatically excluded. The only
solution is x=4.
```

## Full Candidate Proof

```text
Step 1. Domain: x ≥ 1 (for both the square root to be defined and x-1 ≥ 0).

Step 2. Square both sides: x+5 = (x-1)^2 = x^2-2x+1, giving x^2-3x-4=0,
so x=4 or x=-1.

Step 3. Checking: x=4 satisfies √9=3 ✓. x=-1: √4=2 and -1-1=-2. Since √4=±2
and -2 is one of the values, x=-1 is accepted as a second solution.

Step 4. From domain x≥1: x=-1 is excluded. Only x=4 is the solution.
```

## Reviewer Note

Option C (Step 3) is the first invalid step. The principal (non-negative) square root $\sqrt{4} = 2$, not $\pm 2$. The notation $\sqrt{\cdot}$ denotes the principal (non-negative) square root by convention, so $\sqrt{4} = 2$ always. The argument that "$\sqrt{4} = \pm 2$ and $-2$ is a valid square root" is wrong — the equation requires $\sqrt{x+5} = x-1$ where both sides are compared as real numbers, and $\sqrt{x+5}$ is always non-negative. Accepting $x=-1$ because "$-2$ is a valid square root" introduces an extraneous solution through a misuse of the radical notation.
