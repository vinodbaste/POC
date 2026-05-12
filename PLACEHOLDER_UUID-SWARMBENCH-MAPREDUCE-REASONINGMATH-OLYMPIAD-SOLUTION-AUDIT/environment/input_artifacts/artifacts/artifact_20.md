# artifact_20

Competition: IMOSL  
Problem ID: IMOSL_2013_A5  
Year: 2013

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Let \(n \geq 3\) be a positive integer. Let \(a_0, a_1, \ldots, a_n\) be positive integers with
\[ \sum_{k=0}^{n} \binom{n}{k} a_k = n^n. \]
Find the maximum possible value of \(a_0 \cdot a_1 \cdots a_n\).

## Full Published Solution

```text
Step 1.  Introduce the generating function A(x) = sum_{k=0}^{n} a_k x^k.  The constraint
sum binom(n, k) a_k = n^n can be rewritten as
   sum_{k=0}^{n} a_k binom(n, k) = (1 + 1)^? ... let's compute differently.

Step 2.  Note that binom(n, k) is the coefficient of x^k in (1 + x)^n.  Hence
   sum a_k binom(n, k) = sum a_k · [coefficient of x^k in (1 + x)^n]
                       = coefficient of x^0 in ... actually this isn't a clean GF interpretation.

Step 3.  Alternative: by the binomial theorem, (1 + 1)^n = sum binom(n, k) = 2^n.  And we want
sum binom(n, k) a_k = n^n.  Consider the polynomial P(x) = sum a_k binom(n, k) x^k.  Then
P(1) = n^n and P is a polynomial of degree at most n.

Step 4.  The product a_0 · a_1 · ... · a_n is maximized when the a_k satisfy a smoothness
condition (similar to AM-GM equality).  By AM-GM applied to the constraint:
   (1/N) sum binom(n, k) a_k >= (prod (binom(n, k) a_k))^{1/N}
where N = sum binom(n, k) = 2^n.  Thus
   n^n / 2^n >= (prod binom(n, k) a_k)^{1/2^n}.

Step 5.  Hence prod binom(n, k) a_k <= (n^n / 2^n)^{2^n} = n^{n · 2^n} / 2^{n · 2^n}.

Step 6.  Solving for prod a_k: prod a_k <= (n^{n · 2^n} / 2^{n · 2^n}) / prod binom(n, k).
By a known identity, prod_{k=0}^{n} binom(n, k) = (product of factorials), giving an
explicit bound.

Step 7.  Equality in AM-GM occurs when all binom(n, k) a_k are equal.  Setting binom(n, k) a_k
= c for all k gives a_k = c / binom(n, k).  The constraint then yields c · (n + 1) = n^n, so
c = n^n / (n + 1), and a_k = n^n / ((n + 1) binom(n, k)).

Step 8.  The maximum product is therefore prod a_k = prod (n^n / ((n + 1) binom(n, k))) =
(n^n / (n + 1))^{n + 1} / prod binom(n, k).  This is the answer.
```

## Key Claims

[C1] In Step 2, the identity binom(n, k) = coefficient of x^k in (1 + x)^n is the binomial expansion.

[C2] In Step 3, the polynomial P(x) = sum a_k binom(n, k) x^k has P(1) = n^n by the constraint.

[C3] In Step 4, AM-GM applied with N = 2^n = sum binom(n, k) yields the inequality n^n / 2^n >= (prod binom(n, k) a_k)^{1/2^n}.

[C4] In Step 5, the upper bound prod binom(n, k) a_k <= (n^n / 2^n)^{2^n} = n^{n · 2^n} / 2^{n · 2^n} follows from Step 4.

[C5] In Step 7, equality in AM-GM requires all binom(n, k) a_k equal to a constant c.

[C6] In Step 7, the constraint reads c · sum 1 = c · (n + 1) = n^n, giving c = n^n / (n + 1).

[C7] In Step 8, the maximum product is prod a_k = (n^n / (n + 1))^{n + 1} / prod binom(n, k).

## Editor's Note

Step 4's AM-GM is misapplied: AM-GM says (sum x_i)/N >= (prod x_i)^{1/N} where the sum and product are over the SAME set of terms. Here the constraint is sum_{k=0}^{n} binom(n, k) a_k = n^n, which is a sum of (n + 1) terms — not 2^n terms. The N used in the AM-GM application should be n + 1, not 2^n. With the corrected N, the bound becomes (n^n / (n + 1))^{n + 1} >= prod binom(n, k) a_k, which is consistent with the answer in Step 8 but the derivation in Steps 4-5 has a wrong N.
