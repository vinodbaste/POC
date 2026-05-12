# artifact_10

Competition: USAMO  
Problem ID: USAMO_2013_5  
Year: 2013

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Given positive integers \(m\) and \(n\), prove that there is a positive integer \(c\) such that the numbers \(cm\) and \(cn\) have the same number of distinct prime factors.

## Full Published Solution

```text
Step 1.  Suppose for contradiction that no such c exists.  Then for every positive integer c,
omega(cm) ≠ omega(cn), where omega(k) counts the distinct prime factors of k.

Step 2.  Consider c = 1: omega(m) and omega(n) differ.  Without loss of generality,
omega(m) < omega(n).  Let d = omega(n) - omega(m) > 0.

Step 3.  Define c_k = product of the first k primes not appearing in m or n (the "fresh"
primes).  Then for any k:
   omega(c_k · m) = k + omega(m), and similarly omega(c_k · n) = k + omega(n).

Step 4.  Therefore omega(c_k · m) - omega(c_k · n) = omega(m) - omega(n) = -d for every k.
This difference is constant in k.

Step 5.  We chose the smallest counterexample c.  Since the difference is constant in k, no
choice of k (and therefore no choice of c_k) eliminates the difference.  In particular, the
extremal principle yields a smallest c which still fails — contradicting the existence claim.

Step 6.  But this is exactly the contradiction: there cannot be a smallest c such that
omega(cm) = omega(cn), because the inequality is preserved under multiplication by fresh primes.

Step 7.  Wait — that's the wrong direction.  We want a SINGLE c such that omega(cm) = omega(cn).
Take c = (product of primes in n not in m) · (product of primes in m not in n).  Then cm and cn
both have the same set of prime divisors (the union of prime divisors of m and n), so
omega(cm) = omega(cn).  This c works directly without contradiction.
```

## Key Claims

[C1] In Step 2, WLOG omega(m) < omega(n) and d := omega(n) - omega(m) > 0.

[C2] In Step 3, the construction c_k from the first k "fresh" primes gives omega(c_k · m) = k + omega(m) and omega(c_k · n) = k + omega(n).

[C3] In Step 4, the difference omega(c_k · m) - omega(c_k · n) is constant (= -d) in k.

[C4] In Step 5, applying the extremal principle to the smallest c yields a contradiction.

[C5] In Step 6, the inequality omega(c_k · m) ≠ omega(c_k · n) is preserved under multiplication by fresh primes.

[C6] In Step 7, the constructive c = (product of m-only primes) · (product of n-only primes) makes cm and cn have the same prime set.

[C7] In Step 7, the constructive choice from C6 gives omega(cm) = omega(cn) directly without contradiction.

## Editor's Note

Step 5's use of "smallest counterexample" is sloppy — the extremal principle is invoked but no clear ordering is exhibited. Steps 1-5 attempt a contradiction approach that doesn't actually produce one; Step 7 then provides a clean constructive proof that supersedes the entire contradiction setup. The cleaner path would skip Steps 1-6 entirely.
