# artifact_20

Competition: IMO
Problem ID: imo_2001_p2
Year: 2001

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

Let $a, b, c$ be positive reals. Prove that
$$\frac{a}{\sqrt{a^2+8bc}} + \frac{b}{\sqrt{b^2+8ca}} + \frac{c}{\sqrt{c^2+8ab}} \ge 1.$$

## Candidate Excerpts

### Option A

```text
By the Cauchy-Schwarz inequality (Titu/Engel form):
  sum a/√(a²+8bc) = sum a·(a²+8bc)^{-1/2}.
By C-S: [sum a·(a²+8bc)^{-1/2}] ≥ (sum a)² / [sum a·√(a²+8bc)].
This gives a lower bound in terms of sum a·√(a²+8bc), which we must now bound above.
```

### Option B

```text
It suffices to show each term satisfies a/√(a²+8bc) ≥ a/(a+2b+2c). This holds
iff √(a²+8bc) ≤ a+2b+2c, iff a²+8bc ≤ (a+2b+2c)², i.e.,
a²+8bc ≤ a²+4b²+4c²+4ab+4ac+8bc, iff 0 ≤ 4b²+4c²+4ab+4ac = 4(b+c)(a+b+c). ✓
```

### Option C

```text
From Step 2: a/√(a²+8bc) ≥ a/(a+2b+2c) for each term. Summing:
  LHS ≥ a/(a+2b+2c) + b/(b+2c+2a) + c/(c+2a+2b)
      = a/(a+2b+2c) + b/(2a+b+2c) + c/(2a+2b+c)
      = [a(2a+b+2c)(2a+2b+c) + b(a+2b+2c)(2a+2b+c) + c(a+2b+2c)(2a+b+2c)]
        / [(a+2b+2c)(2a+b+2c)(2a+2b+c)].
By Nesbitt-type analysis this sum equals 1.
```

### Option D

```text
Therefore the sum a/√(a²+8bc) + b/√(b²+8ca) + c/√(c²+8ab) ≥ 1.
```

## Full Candidate Proof

```text
Step 1. We claim a/√(a²+8bc) ≥ a/(a+2b+2c). This is equivalent to
a²+8bc ≤ (a+2b+2c)², which expands to 0 ≤ 4b²+4c²+4ab+4ac ≥ 0. ✓

Step 2. Summing the bounds:
  LHS ≥ Σ a/(a+2b+2c).
By symmetry and the Nesbitt-type argument, this sum equals exactly 1.

Step 3. [Explicit computation]: The sum a/(a+2b+2c)+b/(2a+b+2c)+c/(2a+2b+c)=1
follows by writing a/(a+2(b+c)) = a/(a+2s-2a) = a/(2s-a) where s=a+b+c,
and summing: Σ a/(2s-a). By the identity Σ a/(2s-a)=1 (Nesbitt-type), confirmed.

Step 4. Therefore Σ a/√(a²+8bc) ≥ Σ a/(a+2b+2c) = 1.
```

## Reviewer Note

Option D (Step 4) is the first invalid step that wraps up the proof, but the actual first flaw is in Step 2 (Option D), where the proof asserts "by symmetry and the Nesbitt-type argument, this sum equals exactly 1" without verifying this identity. The claim $\sum \frac{a}{a+2b+2c}=1$ for positive $a,b,c$ is not a standard identity and is in fact false in general: for $a=b=c=1$ we get $3 \cdot \frac{1}{5} = 3/5 \neq 1$. The "Nesbitt-type" label is invoked incorrectly. This unverified and actually false identity is the first invalid step.
