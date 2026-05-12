# artifact_57

Competition: IMOSL  
Problem ID: IMOSL_2015_2  
Year: 2015

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Determine all triples \((a, b, c)\) of positive integers such that each of the numbers
\[ ab - c, \quad bc - a, \quad ca - b \]
is a power of 2.

## Candidate Excerpts

### Option A

```text
Combining: the only solutions arise from cases where some of a, b, c are odd, and
exhaustive case analysis on parity gives the triples (2,2,2), (2,2,3), (2,6,11), (3,5,7),
and their permutations.  Verification for (2,2,2): ab-c = 4-2 = 2 = 2^1 ✓, similar for
the others.  Verification for (3,5,7): ab-c = 15-7 = 8 = 2^3 ✓, bc-a = 35-3 = 32 = 2^5 ✓,
ca-b = 21-5 = 16 = 2^4 ✓.
```

### Option B

```text
Step 3.  Now we may assume a, b, c are all even.  Write a = 2a', b = 2b', c = 2c'.
Substituting:
   ab - c = 4a'b' - 2c' = 2(2a'b' - c'), a power of 2.  So 2a'b' - c' is a power of 2.
   Similarly bc - a = 2(2b'c' - a') and ca - b = 2(2c'a' - b'), all powers of 2.
Therefore (a', b', c') is again a triple satisfying analogous conditions.  By infinite
descent, we can assume one of a, b, c is odd, contradiction.  Hence the all-even case
yields no solutions.
```

### Option C

```text
Assume WLOG a ≤ b ≤ c.  Since ab - c, bc - a, ca - b are powers of 2 (hence positive), we
need ab > c, bc > a, ca > b.  The middle two are automatic given a ≤ b ≤ c.  The first
gives c < ab.
```

### Option D

```text
Consider parity.  Since each of ab-c, bc-a, ca-b is a power of 2, either it equals 1 (= 2^0)
or it is even.  Suppose at least two of a, b, c are odd.  Then say a, b are odd; then
ab is odd, so ab - c is odd iff c is even, hence ab - c = 1 in that case.
Similarly analyzing all sub-cases of the parities of a, b, c.
```

## Full Candidate Proof

```text
Step 1.  Assume WLOG a ≤ b ≤ c.  Since ab - c, bc - a, ca - b are powers of 2
(hence positive), we need ab > c, bc > a, ca > b.  The middle two are automatic given
a ≤ b ≤ c.  The first gives c < ab.

Step 2.  Consider parity.  Since each of ab-c, bc-a, ca-b is a power of 2, either it
equals 1 (= 2^0) or it is even.  Suppose at least two of a, b, c are odd.  Then say a, b
are odd; then ab is odd, so ab - c is odd iff c is even, hence ab - c = 1 in that case.
Similarly analyzing all sub-cases of the parities of a, b, c.

Step 3.  Now we may assume a, b, c are all even.  Write a = 2a', b = 2b', c = 2c'.
Substituting:
   ab - c = 4a'b' - 2c' = 2(2a'b' - c'), a power of 2.  So 2a'b' - c' is a power of 2.
   Similarly bc - a = 2(2b'c' - a') and ca - b = 2(2c'a' - b'), all powers of 2.
Therefore (a', b', c') is again a triple satisfying analogous conditions.  By infinite
descent, we can assume one of a, b, c is odd, contradiction.  Hence the all-even case
yields no solutions.

Step 4.  Combining: the only solutions arise from cases where some of a, b, c are odd,
and exhaustive case analysis on parity gives the triples (2,2,2), (2,2,3), (2,6,11),
(3,5,7), and their permutations.  Verification for (2,2,2): ab-c = 4-2 = 2 = 2^1 ✓,
similar for the others.  Verification for (3,5,7): ab-c = 15-7 = 8 = 2^3 ✓,
bc-a = 35-3 = 32 = 2^5 ✓, ca-b = 21-5 = 16 = 2^4 ✓.
```

## Reviewer Note

The descent argument in Step 3 implicitly assumes 2a'b' - c' is itself a power of 2, but the calculation 4a'b'-2c' = 2(2a'b'-c') only guarantees that 2a'b' - c' equals (power of 2) / 2 — which is a power of 2 only when the original ab - c is ≥ 2. The premise that (a', b', c') satisfies the same conditions is false in general: the new "differences" 2a'b' - c' need not all be positive integers, much less powers of 2, since c' could exceed 2a'b' for triples where ab - c happened to equal 2 originally.
