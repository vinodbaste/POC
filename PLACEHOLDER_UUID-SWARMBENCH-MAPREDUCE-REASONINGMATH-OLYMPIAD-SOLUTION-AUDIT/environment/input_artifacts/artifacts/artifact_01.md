# artifact_01

Competition: IMO  
Problem ID: IMO_2009_1  
Year: 2009

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Let \(n\) be a positive integer and let \(a_1, a_2, \ldots, a_k\) (\(k \geq 2\)) be distinct integers in the set \(\{1, 2, \ldots, n\}\) such that \(n\) divides \(a_i(a_{i+1} - 1)\) for \(i = 1, 2, \ldots, k-1\). Prove that \(n\) does not divide \(a_k(a_1 - 1)\).

## Full Published Solution

```text
Step 1.  Suppose, for the sake of contradiction, that n divides a_k(a_1 - 1).  Combined with
the hypothesis n | a_i(a_{i+1} - 1) for i = 1, ..., k-1, this gives n | a_i(a_{i+1} - 1) for
ALL indices i mod k (with subscripts taken cyclically).

Step 2.  Let p be any prime divisor of n.  We work modulo p^v where v = v_p(n) is the p-adic
valuation of n.  Define b_i = v_p(a_i) for each i.

Step 3.  From p^v | a_i (a_{i+1} - 1), we get p^v | a_i · (a_{i+1} - 1).  Since v_p(a_i) = b_i
and v_p(a_{i+1} - 1) = v - b_i (taking the cyclic relation), we conclude b_i + (v - b_i) = v,
which is automatic and gives no new information.

Step 4.  Instead, look at the quantity gcd(a_i, n).  We claim gcd(a_i, n) is constant in i,
modulo the cyclic indexing.  Indeed if g_i = gcd(a_i, n), then g_i | n and g_i | a_i(a_{i+1}-1).
Since gcd(a_i, a_{i+1} - 1) is constrained by the cyclic divisibility chain, by Bezout's lemma
g_i divides g_{i+1}.  Cyclically, g_1 | g_2 | ... | g_k | g_1, forcing all g_i equal.

Step 5.  Let g be this common value.  Then a_i = g · m_i with gcd(m_i, n/g) = 1.  The relation
n | a_i(a_{i+1} - 1) becomes (n/g) | a_{i+1} - 1 (after dividing by g and using coprimality of
m_i with n/g).  Hence a_{i+1} ≡ 1 (mod n/g) for every i.

Step 6.  Cyclically, a_1 ≡ 1 (mod n/g).  But a_1 is distinct from 1 (otherwise a_1 would equal
1, contradicting distinctness if k ≥ 2 and one of the others equals 1), and a_1 ∈ {1, ..., n}.
Hence n/g = 1, i.e., g = n.  But then a_i is divisible by n for every i, forcing a_i = n.
That contradicts distinctness of the a_i.  This is the desired contradiction.

Step 7.  Therefore the assumption in Step 1 was false: n does NOT divide a_k(a_1 - 1).
```

## Key Claims

[C1] In Step 1, the cyclic hypothesis n | a_i(a_{i+1} - 1) for all i mod k follows from assuming n | a_k(a_1 - 1) combined with the original hypothesis.

[C2] In Step 3, the equation v_p(a_i) + v_p(a_{i+1} - 1) = v is automatic and yields no new information.

[C3] In Step 4, the values gcd(a_i, n) form a divisibility chain g_1 | g_2 | ... | g_k | g_1, hence are all equal.

[C4] In Step 5, the relation n | a_i(a_{i+1} - 1) implies (n/g) | a_{i+1} - 1, using coprimality of m_i with n/g.

[C5] In Step 6, the conclusion a_1 ≡ 1 (mod n/g) combined with a_1 ∈ {1, ..., n} forces n/g = 1.

[C6] In Step 6, g = n forces a_i = n for every i, contradicting distinctness.

[C7] The proof's final conclusion in Step 7 follows by the contradiction reductio established in Step 6.

## Editor's Note

This is the official IMO 2009 Problem 1 solution as presented in the IMO Compendium. Some readers have flagged that Step 4's "by Bezout's lemma" gloss may not be fully justified given the cyclic structure of the divisibility chain.
