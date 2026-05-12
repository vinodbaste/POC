# artifact_128

Grading ID: GB-0964  
Problem ID: PB-Advanced-029  
Source: USAMO 2025  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Determine, with proof, all positive integers $k$ such that
 \[
 \frac{1}{n+1}\sum_{i=0}^{n}\binom{n}{i}^{k}
 \]
 is an integer for every positive integer $n$.

## Reference Solution (for grader's calibration)

The answer is all even $k$. Let's abbreviate $S(n):=\binom{n}{0}^{k}+\cdots+\binom{n}{n}^{k}$
 for the sum in the problem.


 \textbf{Proof that even $k$ is necessary.}

  Choose $n=2$. We need $3\mid S(2)=2+2^{k}$, which requires $k$
 to be even.


 \textbf{Proof that even $k$ is sufficient. }

 From now on we treat $k$ as fixed, and we let $p^{e}$ be a prime
 fully dividing $n+1$. It is sufficient to prove that $S(n)$ is a
 multiple of $p^{e}$ for each such $p^{e}$. The basic idea is to
 reduce from $n+1$ to $(n+1)/p$ by an induction. We prove the following
 lemma on each individual binomial coefficient.


 \textbf{Lemma. }Suppose $p^{e}$ is a prime power which fully divides
 $n+1$. Then

 \[
 \binom{n}{i}\equiv\pm\binom{\frac{n+1}{p}-1}{\lfloor i/p\rfloor}\quad\left(\bmod p^{e}\right)
 \]

 \emph{Proof.} If we write
 \[
 \binom{n}{i}=\prod_{1\leq j\leq i}\frac{n-(j-1)}{j}
 \]

 then the fractions for $p\nmid j$ are all $\pm1\left(\bmod p^{e}\right)$.
 So only considers those $j$ with $p\mid j$; in that case one obtains
 the claimed $\binom{\frac{n+1}{p}-1}{\lfloor i/p\rfloor}$ exactly
 (even without having to take modulo $p^{e}$).


 From the lemma, it follows if $p^{e}$ is a prime power which fully
 divides $n+1$, then
 \[
 S(n)\equiv p\cdot S\left(\frac{n+1}{p}-1\right)\quad\left(\bmod p^{e}\right)
 \]

 by grouping the $n+1$ terms (for $0\leq i\leq n$ ) into consecutive
 ranges of length $p$ (by the value of $\lfloor i/p\rfloor$ ) and
 the result follows by induction.

## Grading Guidelines

(Partial)
 1. Proved that $k$ should be even.
 2. Used the induction on $n+1$ and considered the equation for$\frac{n+1}{p}$.
 3. Stated the identity $n+1\mid\sum_{i=0}^{n}\left((-1)^{i}\binom{n}{i}\right)^{k}$ without proof.
(Almost)
 1. Solution is almost complete, but made minor mistakes which are not negligible, such as coming up with a proof that only works for odd primes.

## Candidate Response (to be graded)

**Outcome 1: COMPLETE PROOF**

We are asked to determine all positive integers $k$ such that $S_k(n) = \frac{1}{n+1}\sum_{i=0}^{n}\binom{n}{i}^{k}$ is an integer for every positive integer $n$. Let $A_k(n) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. The condition is equivalent to $n+1 \mid A_k(n)$ for all $n \ge 1$.

We prove that this condition holds if and only if $k$ is an even positive integer.

**Part 1: Necessity (k must be even)**

Let $p$ be an odd prime and set $n = p-1$. We require $n+1=p$ to divide $A_k(p-1)$.
We use the known congruence for binomial coefficients: $\binom{p-1}{i} \equiv (-1)^i \pmod p$ for $0 \le i \le p-1$.

Then,
$$ A_k(p-1) = \sum_{i=0}^{p-1} \binom{p-1}{i}^k \equiv \sum_{i=0}^{p-1} ((-1)^i)^k = \sum_{i=0}^{p-1} (-1)^{ik} \pmod p. $$
If $k$ is odd, $(-1)^{ik} = (-1)^i$. Since $p$ is odd, $p-1$ is even. The sum becomes:
$$ A_k(p-1) \equiv \sum_{i=0}^{p-1} (-1)^i = (1-1) + (1-1) + \cdots + (1-1) + 1 = 1 \pmod p. $$
Since $A_k(p-1) \not\equiv 0 \pmod p$ when $k$ is odd, $S_k(p-1)$ is not an integer.
Therefore, $k$ must be even. Let $k=2m$ for some positive integer $m$.

**Part 2: Sufficiency (k=2m)**

We must prove that $N \mid A_{2m}(N-1)$ for all integers $N \ge 2$.
It suffices to show that for any prime $p$, if $r = v_p(N) \ge 1$, then $p^r \mid A_{2m}(N-1)$.

Let $N \ge 2$ be fixed, and let $p$ be a prime divisor of $N$ with $v_p(N)=r$. Let $C_i = \binom{N-1}{i}$.

**Lemma 1:** If $p \nmid i$, then $C_i^{2m} \equiv C_{i-1}^{2m} \pmod{p^r}$.

*Proof:* We have the identity $\binom{N}{i} = \binom{N-1}{i} + \binom{N-1}{i-1} = C_i + C_{i-1}$.
Also, $\binom{N}{i} = \frac{N}{i} \binom{N-1}{i-1}$. Since $v_p(N)=r$ and $p \nmid i$ ($v_p(i)=0$), we have $v_p(\binom{N}{i}) \ge r$.
Thus, $\binom{N}{i} \equiv 0 \pmod{p^r}$, which implies $C_i \equiv -C_{i-1} \pmod{p^r}$.
Raising to the even power $2m$, we get $C_i^{2m} \equiv (-C_{i-1})^{2m} = C_{i-1}^{2m} \pmod{p^r}$.

**Analysis of $A_{2m}(N-1)$ modulo $p^r$.**

Let $N' = N/p$. We decompose the sum $A_{2m}(N-1) = \sum_{i=0}^{N-1} C_i^{2m}$ into $N'$ blocks of length $p$:
$A_{2m}(N-1) = \sum_{j=0}^{N'-1} B_j$, where $B_j = \sum_{l=0}^{p-1} C_{jp+l}^{2m}$.

For $l \in \{1, \dots, p-1\}$, $p \nmid (jp+l)$. By repeated application of Lemma 1, $C_{jp+l}^{2m} \equiv C_{jp}^{2m} \pmod{p^r}$.
$$ B_j = C_{jp}^{2m} + \sum_{l=1}^{p-1} C_{jp+l}^{2m} \equiv C_{jp}^{2m} + (p-1)C_{jp}^{2m} = p \cdot C_{jp}^{2m} \pmod{p^r}. $$
Summing over $j$:
$$ A_{2m}(N-1) \equiv p \sum_{j=0}^{N'-1} C_{jp}^{2m} \pmod{p^r}. \quad (*) $$

**Lemma 2:** Let $D_j = \binom{N'-1}{j}$. Then $C_{jp}^{2m} \equiv D_j^{2m} \pmod{p^r}$.

*Proof:* We analyze the definition $C_{jp} = \binom{N-1}{jp} = \prod_{t=1}^{jp} \frac{N-t}{t}$. We split the product based on whether $p$ divides $t$.

$P_{\text{mult}} = \prod_{s=1}^{j} \frac{N-sp}{sp} = \prod_{s=1}^{j} \frac{N/p - s}{s} = \prod_{s=1}^{j} \frac{N'-s}{s} = \binom{N'-1}{j} = D_j$.

$P_{\text{nonmult}} = \prod_{t \in T} \frac{N-t}{t}$, where $T = \{t \in \{1, \dots, jp\} : p \nm

[Note: response truncated to first 3000 characters of 4735]
