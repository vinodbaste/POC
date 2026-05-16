# artifact_17

Competition: IMO
Problem ID: imo_1977_p5
Year: 1977

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

Let $f: \mathbb{N} \to \mathbb{N}$ be a function satisfying $f(f(n)) = n + 1987$ for all $n \in \mathbb{N}$. (Here $\mathbb{N} = \{1, 2, 3, \ldots\}$.) Show that no such function exists, or find one if it does exist.

*(Adapted: the original uses a specific constant; this version uses 1987.)*

## Candidate Excerpts

### Option A

```text
Substituting n=0 into f(f(n)) = n+1987 gives f(f(0)) = 1987. Since f maps N to N
and 0 ∉ N (as N = {1,2,...}), this substitution is invalid and yields a contradiction
with the domain, proving no such function exists.
```

### Option B

```text
Applying the relation twice: f(f(f(f(n)))) = f(f(n))+1987 = n+1987+1987 = n+2·1987.
But also f(f(f(f(n)))) = f(f(n+1987)) = n+1987+1987 = n+2·1987. Both sides agree,
so the relation is self-consistent and gives no immediate contradiction.
```

### Option C

```text
If such f exists, then f is injective: f(a)=f(b) implies f(f(a))=f(f(b)), so
a+1987 = b+1987, hence a=b. Injectivity is established without contradiction.
```

### Option D

```text
Since f(f(n)) = n+1987, applying f gives f(f(f(n))) = f(n)+1987. But also
f(f(f(n))) = f(n+1987). Therefore f(n+1987) = f(n)+1987 for all n in N.
This means f is "1987-periodic in increments" — a valid structural property.
```

## Full Candidate Proof

```text
Step 1. Substitute n=0 into f(f(n))=n+1987: this gives f(f(0))=1987. Since
0 ∉ N={1,2,...}, this substitution is outside the domain and constitutes a
contradiction proving no such f exists.

Step 2. [Actual consistency check]: applying f twice more gives n+2·1987, which
matches both paths — no contradiction from iterating.

Step 3. f is injective: f(a)=f(b) ⟹ a+1987=b+1987 ⟹ a=b.

Step 4. f satisfies f(n+1987)=f(n)+1987, a valid structural property.
```

## Reviewer Note

Option A (Step 1) is the first invalid step. The argument claims a contradiction by substituting $n=0$ into the functional equation. But $0 \notin \mathbb{N}$ under the convention $\mathbb{N} = \{1, 2, \ldots\}$, so the substitution is simply not permitted — it does not produce a "contradiction with the domain." Noting that a substitution is outside the domain does not by itself prove non-existence; it only means the substitution is irrelevant. A valid proof of non-existence requires a parity or coloring argument based on the structure of $f(f(n))=n+c$ for odd $c$.
