# artifact_08

Competition: AIME
Problem ID: aime_1990_p2
Year: 1990

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

The sequence $a_1, a_2, a_3, \ldots$ is defined by $a_1 = 1$, $a_2 = 1$, and $a_n = a_{n-1} + a_{n-2}$ for $n \ge 3$ (Fibonacci sequence). Find the remainder when $a_{1000}$ is divided by $8$.

## Candidate Excerpts

### Option A

```text
Computing the Fibonacci sequence modulo 8:
  a_1=1, a_2=1, a_3=2, a_4=3, a_5=5, a_6=0, a_7=5, a_8=5,
  a_9=2, a_10=7, a_11=1, a_12=0, a_13=1, a_14=1.
At a_13=1 and a_14=1 the sequence repeats its starting pair, confirming periodicity.
```

### Option B

```text
The Fibonacci sequence mod 8 is eventually periodic (Pisano period). From the
computed terms, the period begins at a_1 and the repeating block is:
  1,1,2,3,5,0,5,5,2,7,1,0  (length 12).
```

### Option C

```text
Since the period is 12, we reduce 1000 mod 12: 1000 = 12·83 + 4, so a_1000 ≡ a_4
(mod 8). From the table, a_4 = 3. Therefore a_1000 ≡ 3 (mod 8).
```

### Option D

```text
The Fibonacci sequence mod 8 has period 5, not 12. The first five terms are
1,1,2,3,5, and the sixth term is 0+5=5 ≢ 1, so the period cannot be 5.
Wait — actually testing confirms: a_6=0, a_7=5, a_8=5+0=5... the period is 12
as shown in Step 2. We should use period 5 however since the problem is (mod 8)
and 2^3=8 forces a shorter period of lcm(2,5)=10 by a standard theorem.
Using period 10: 1000 mod 10 = 0, so a_1000 ≡ a_10 (mod 8). From the table,
a_10 = 7. Hence the answer is 7.
```

## Full Candidate Proof

```text
Step 1. Compute Fibonacci mod 8 until the initial pair (1,1) recurs:
  a_1=1, a_2=1, a_3=2, a_4=3, a_5=5, a_6=0, a_7=5, a_8=5,
  a_9=2, a_10=7, a_11=1, a_12=0, a_13=1, a_14=1. Period = 12. ✓

Step 2. The repeating block has length 12: 1,1,2,3,5,0,5,5,2,7,1,0.

Step 3. Since 1000 mod 12 = 4, we have a_1000 ≡ a_4 = 3 (mod 8).

Step 4. Alternative reasoning: the period mod 8 is forced to be lcm(2,5)=10 by a
theorem about Pisano periods. Using period 10: 1000 mod 10=0, so a_1000≡a_10=7.
```

## Reviewer Note

Option D (Step 4) is the first invalid step. The claim that "the Pisano period mod $2^3 = 8$ must be $\text{lcm}(2,5)=10$ by a standard theorem" is fabricated. The actual theorem on Pisano periods says $\pi(p^k)$ divides $p^{k-1}\pi(p)$ for odd primes $p$; it does not give a simple $\text{lcm}$ formula involving 5. The Pisano period $\pi(8)=12$ was correctly computed in Steps 1–2 by direct calculation. Overriding the computed period with an incorrectly cited theorem gives the wrong period (10) and the wrong answer (7).
