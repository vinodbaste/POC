# artifact_16

Competition: AMC
Problem ID: amc12a_2009_p11
Year: 2009

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

The polynomial $p(x) = x^3 - 7x + 6$ has three real roots. Find their product.

## Candidate Excerpts

### Option A

```text
By Vieta's formulas for x^3 + 0·x^2 - 7x + 6 = 0:
  sum of roots = -0/1 = 0,
  sum of products of pairs = -7/1 = -7,
  product of all three roots = -6/1 = -6.
```

### Option B

```text
Factor: p(x) = x^3-7x+6. Testing x=1: 1-7+6=0 ✓. So (x-1) is a factor.
Dividing: x^3-7x+6 = (x-1)(x^2+x-6) = (x-1)(x+3)(x-2).
Roots are x=1, x=-3, x=2. Product = 1·(-3)·2 = -6. ✓
```

### Option C

```text
Verification: 1+(-3)+2 = 0 (sum of roots) ✓; 1·(-3)+1·2+(-3)·2 = -3+2-6 = -7
(sum of pairwise products) ✓; product = -6 ✓. All Vieta's conditions satisfied.
```

### Option D

```text
By Vieta's formulas for the monic polynomial x^3+bx^2+cx+d, the product of the
roots equals -d (not +d as is sometimes stated). For p(x)=x^3+0·x^2-7x+6, d=6,
so the product of the roots is -d = -6.

Wait — the correct Vieta's formula is: product of roots = (-1)^n · d/a where n
is the degree and a is the leading coefficient. For n=3: product = (-1)^3·(6/1) = +6.
Hence the product of the three roots is +6.
```

## Full Candidate Proof

```text
Step 1. Vieta's formulas for x^3-7x+6: sum=0, pairwise=-7, product=-6/1=-6.

Step 2. Factor: (x-1)(x+3)(x-2). Roots: 1,-3,2. Product = -6.

Step 3. All three Vieta's conditions verified from the explicit roots.

Step 4. Alternative Vieta's reasoning: product = (-1)^3·(6/1) = +6.
[This contradicts the factorization, which gives product = -6.]
```

## Reviewer Note

Option D (Step 4) is the first invalid step. For a monic polynomial $x^n + c_{n-1}x^{n-1}+\cdots+c_0$, Vieta's formula gives the product of roots as $(-1)^n \cdot c_0$. For $p(x)=x^3-7x+6$, the constant term is $c_0 = 6$, giving product $= (-1)^3 \cdot 6 = -6$. The step misapplies the formula by writing $(-1)^n \cdot (d/a)$ with $d=6$, then concluding $+6$ — which contradicts the explicit factorization $1 \cdot (-3) \cdot 2 = -6$ verified in Step 2. The sign error in applying Vieta's product formula is the first invalid step.
