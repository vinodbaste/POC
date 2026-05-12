# artifact_03

Competition: IMOSL  
Problem ID: IMOSL_2015_N4  
Year: 2015

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Suppose that \(a_0, a_1, a_2, \ldots\) is an infinite sequence of positive integers with \(a_k \leq a_{k+1} \leq a_k + 5\) for all \(k \geq 0\). Prove that there exist infinitely many pairs \((m, n)\) with \(m > n\) such that \(a_n\) divides \(a_m\).

## Full Published Solution

```text
Step 1.  Consider the sequence (a_n) and define b_n = a_n mod a_n (which is always 0).  This is
trivial; instead consider b_n = a_{n+1} - a_n, an integer in [0, 5].

Step 2.  By the pigeonhole principle, some value v in {0, 1, 2, 3, 4, 5} appears infinitely often
in the sequence (b_n).  Without loss of generality, assume b_n = v for infinitely many n.

Step 3.  Among the infinitely many indices n with b_n = v, by pigeonhole on residues modulo a_0,
infinitely many of them have a_n ≡ r (mod a_0) for some fixed r in {0, 1, ..., a_0 - 1}.

Step 4.  In particular, infinitely many a_n are divisible by a_0 (the case r = 0).  This gives
infinitely many pairs (m, 0) with m > 0 and a_0 | a_m, as required.

Step 5.  But wait — we only proved infinitely many n have a_n ≡ 0 (mod a_0).  What about the
infinitely many n with a_n ≡ r ≠ 0?  These provide additional pairs by replacing a_0 with the
smallest index n_0 with a_{n_0} ≡ r — but that's a different argument.

Step 6.  Either way, the original claim holds: there are infinitely many pairs (m, n) with
a_n | a_m, completing the proof.
```

## Key Claims

[C1] In Step 1, the sequence b_n = a_{n+1} - a_n takes integer values in the closed interval [0, 5] for every n.

[C2] In Step 2, the pigeonhole principle on the finite range {0, 1, 2, 3, 4, 5} yields some value v that appears infinitely often.

[C3] In Step 3, among the infinitely many n with b_n = v, pigeonhole on residues modulo a_0 produces infinitely many sharing the same residue r.

[C4] In Step 4, the case r = 0 directly gives infinitely many pairs (m, 0) with a_0 | a_m.

[C5] In Step 5, the case r ≠ 0 also yields pairs but via a different argument involving the first index with residue r.

[C6] In Step 6, the original claim (infinitely many pairs (m, n) with a_n | a_m) follows from the analysis in Steps 4 and 5.

[C7] The proof handles the dependence of pair availability on the relation between m and n correctly; specifically, m must be strictly larger than n.

## Editor's Note

This is a candidate solution to IMOSL 2015 N4 as transcribed from competition notes. Step 5 has been flagged by graders as a non sequitur — the argument changes the role of a_0 without justification, and the cleaner approach is to combine the two cases differently. Step 3's pigeonhole on residues modulo a_0 (a fixed constant) is correct.
