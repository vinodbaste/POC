# artifact_14

Competition: AMC
Problem ID: amc12a_2008_p11
Year: 2008

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

If $z_1 = 2 + 3i$ and $z_2 = 1 - i$, find $|z_1 \cdot z_2|$.

## Candidate Excerpts

### Option A

```text
|z_1| = √(2²+3²) = √(4+9) = √13.
|z_2| = √(1²+(-1)²) = √(1+1) = √2.
```

### Option B

```text
For complex numbers, |z_1 · z_2| = |z_1| + |z_2|. Therefore
|z_1 · z_2| = √13 + √2.
```

### Option C

```text
Alternatively, compute z_1·z_2 directly:
  z_1·z_2 = (2+3i)(1-i) = 2-2i+3i-3i² = 2+i+3 = 5+i.
  |5+i| = √(25+1) = √26.
```

### Option D

```text
Since |z_1 · z_2| = |z_1|·|z_2| = √13·√2 = √26, the answer is √26.
```

## Full Candidate Proof

```text
Step 1. Compute individual moduli:
  |z_1| = √(4+9) = √13,   |z_2| = √(1+1) = √2.

Step 2. For complex numbers, |z_1·z_2| = |z_1| + |z_2|, so
  |z_1·z_2| = √13 + √2.

Step 3. [Direct verification]: z_1·z_2 = (2+3i)(1-i) = 2+i+3 = 5+i,
  |5+i| = √26.

Step 4. The true rule |z_1·z_2| = |z_1|·|z_2| = √13·√2 = √26. Answer: √26.
```

## Reviewer Note

Option B (Step 2) is the first invalid step. The correct rule for moduli of complex products is $|z_1 \cdot z_2| = |z_1| \cdot |z_2|$ (multiplication, not addition). The claim $|z_1 \cdot z_2| = |z_1| + |z_2|$ confuses the multiplicativity of the modulus with the triangle inequality ($|z_1 + z_2| \le |z_1| + |z_2|$), which applies to sums, not products. This invalid rule gives $\sqrt{13}+\sqrt{2}$, whereas the correct answer is $\sqrt{13}\cdot\sqrt{2}=\sqrt{26}$.
