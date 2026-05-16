# artifact_21

Competition: IMO
Problem ID: imo_2003_p2
Year: 2003

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

Determine all pairs of positive integers $(a, b)$ such that $\dfrac{a^2}{2ab^2 - b^3 + 1}$ is a positive integer.

## Candidate Excerpts

### Option A

```text
For b=1: denominator = 2a·1-1+1 = 2a, so k = a^2/(2a) = a/2. Integer iff 2|a.
Solutions: (a,b) = (2t, 1) for any positive integer t.
```

### Option B

```text
Let k = a^2 / (2ab^2 - b^3 + 1) be a positive integer. Then a^2 = k(2ab^2-b^3+1).
Since the denominator must be positive, we require 2ab^2 - b^3 + 1 > 0, i.e.,
a > (b^3-1)/(2b^2) = b/2 - 1/(2b^2). So a ≥ ⌈b/2⌉ for b ≥ 2.

Now view a^2 - 2kb^2·a + k(b^3-1) = 0 as a quadratic in a. By the quadratic
formula, the discriminant is Δ = 4k^2b^4 - 4k(b^3-1) = 4k(k·b^4-b^3+1). For a
to be a positive integer, Δ must be a perfect square: k·b^4-b^3+1 = m^2 for some
non-negative integer m. Since k and b are positive integers and k·b^4 ≥ b^4 > b^3
for b ≥ 2, we have k·b^4-b^3+1 ≥ b^4-b^3+1 > 0. By Vieta's, if a is one root
then the other root a' = 2kb^2 - a also satisfies the same equation. This gives
a descent: if a > kb^2 then a' = 2kb^2-a < kb^2, contradicting minimality.
Hence a ≤ kb^2, and by minimality over all valid pairs sharing the same k, a=kb^2
leads to a^2=k(2kb^4-b^3+1), giving specific families of solutions.
```

### Option C

```text
Testing small values: (b=1): k = a^2/(2a-0) = a/2, so k is an integer iff a is even.
All pairs (2t, 1) for t ≥ 1 are solutions with k=t. (b=2): k = a^2/(8a-7),
testing a: a=1 gives 1/1=1 ✓; a=7 gives 49/49=1 ✓; a=49 gives 2401/337≠int.
```

### Option D

```text
The descent argument shows that for fixed k, the minimal positive-integer solution
in a must satisfy a ≤ kb^2. Combining with the quadratic structure, one can show
the complete solution set consists of pairs where a = 2t^2b^2 and b arbitrary,
or the family (2t, 1).
```

## Full Candidate Proof

```text
Step 1. Set k=a^2/(2ab^2-b^3+1). The quadratic a^2-2kb^2·a+k(b^3-1)=0 has Vieta
companion a'=2kb^2-a. If (a,b) is a minimal solution, a'<0 or a'≥a (else smaller).
If a'≥0 and a'<a, contradiction of minimality. If a'<0, b^3<1, impossible for
b≥1. So all minimal solutions have a=kb^2, giving specific parametric families.
The descent argument covers all cases.

Step 2. [Small case checks]: b=1 gives a/2 integer iff 2|a: pairs (2t,1). ✓
  b=2: a=1 gives 1/(2·4-8+1)=1/-3 <0 not valid. [Re-check: 2·1·4-8+1=1. k=1 ✓]

Step 3. b=1 case: (a,b)=(2t,1) for t≥1.

Step 4. Complete family from descent: all solutions are (2t^2b^2,b) and (2t,1).
```

## Reviewer Note

Option A (Step 1) is the first invalid step. The descent argument states that if $(a,b)$ is a minimal solution and the Vieta companion $a' = 2kb^2 - a$ satisfies $a' \geq 0$ and $a' < a$, this contradicts minimality. But "minimality" has not been precisely defined at this point — minimality over what quantity (sum $a+b$? value of $a$?) — and the step assumes that $a'$ with the same $k$ and $b$ constitutes a "smaller" valid pair without verifying that $(a', b)$ actually gives the same value of $k$. This is the key gap: before invoking minimality, one must confirm $(a',b)$ is a valid pair achieving ratio $k$, which requires showing $a'^2/(2a'b^2-b^3+1)=k$. The step performs the descent without that verification.
