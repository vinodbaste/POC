# artifact_52

Competition: USAMO  
Problem ID: USAMO_2013_4  
Year: 2013

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Find all real numbers \(x,y,z\geq 1\) satisfying
\[\min\left(\sqrt{x+xyz},\sqrt{y+xyz},\sqrt{z+xyz}\right)=\sqrt{x-1}+\sqrt{y-1}+\sqrt{z-1}.\]

## Candidate Excerpts

### Option A

```text
We square both sides of the equation, choosing the minimum on the LHS to be \sqrt{x+xyz}.
This gives
   x + xyz = (\sqrt{x-1} + \sqrt{y-1} + \sqrt{z-1})^2
           = (x-1) + (y-1) + (z-1) + 2(\sqrt{(x-1)(y-1)} + \sqrt{(y-1)(z-1)} + \sqrt{(x-1)(z-1)}).
Rearranging:
   xyz + 3 - y - z = 2(\sqrt{(x-1)(y-1)} + \sqrt{(y-1)(z-1)} + \sqrt{(x-1)(z-1)}).
```

### Option B

```text
Now assume WLOG x = y = z by the symmetry of the equation and the minimum function.
Then the equation reduces to
   \sqrt{x + x^3} = 3\sqrt{x-1},
i.e., x + x^3 = 9(x-1) = 9x - 9, so x^3 - 8x + 9 = 0.
```

### Option C

```text
The cubic x^3 - 8x + 9 = 0 has rational root test candidates ±1, ±3, ±9.  Testing x=1:
1 - 8 + 9 = 2 ≠ 0.  Testing x=3: 27 - 24 + 9 = 12 ≠ 0.  No rational roots, so we use
the discriminant: for x^3 + px + q = 0 with p = -8, q = 9, discriminant
   -4p^3 - 27q^2 = -4(-512) - 27(81) = 2048 - 2187 = -139 < 0,
so the cubic has one real root and two complex roots.
```

### Option D

```text
We claim x = y = z = some specific value.  By the numerical method or graphing, the real
root of x^3 - 8x + 9 = 0 is approximately x \approx 2.347.  Hence the unique solution is
x = y = z \approx 2.347, and substituting back confirms the original equation holds.
```

## Full Candidate Proof

```text
Step 1.  We square both sides of the equation, choosing the minimum on the LHS to be
\sqrt{x+xyz}.  This gives
   x + xyz = (\sqrt{x-1} + \sqrt{y-1} + \sqrt{z-1})^2
           = (x-1) + (y-1) + (z-1) + 2(\sqrt{(x-1)(y-1)} + \sqrt{(y-1)(z-1)} + \sqrt{(x-1)(z-1)}).
Rearranging:
   xyz + 3 - y - z = 2(\sqrt{(x-1)(y-1)} + \sqrt{(y-1)(z-1)} + \sqrt{(x-1)(z-1)}).

Step 2.  Now assume WLOG x = y = z by the symmetry of the equation and the minimum
function.  Then the equation reduces to
   \sqrt{x + x^3} = 3\sqrt{x-1},
i.e., x + x^3 = 9(x-1) = 9x - 9, so x^3 - 8x + 9 = 0.

Step 3.  The cubic x^3 - 8x + 9 = 0 has rational root test candidates ±1, ±3, ±9.
Testing x=1: 1 - 8 + 9 = 2 ≠ 0.  Testing x=3: 27 - 24 + 9 = 12 ≠ 0.  No rational roots,
so we use the discriminant: for x^3 + px + q = 0 with p = -8, q = 9, discriminant
   -4p^3 - 27q^2 = -4(-512) - 27(81) = 2048 - 2187 = -139 < 0,
so the cubic has one real root and two complex roots.

Step 4.  We claim x = y = z = some specific value.  By the numerical method or graphing,
the real root of x^3 - 8x + 9 = 0 is approximately x ≈ 2.347.  Hence the unique solution
is x = y = z ≈ 2.347, and substituting back confirms the original equation holds.
```

## Reviewer Note

The assumption that WLOG x = y = z exploits a symmetry that the minimum function does not actually preserve in this equation — the min of three quantities is not symmetric in the same way that the sum or product is, since the minimum identifies one specific argument. The substitution discards genuine asymmetric solutions.
