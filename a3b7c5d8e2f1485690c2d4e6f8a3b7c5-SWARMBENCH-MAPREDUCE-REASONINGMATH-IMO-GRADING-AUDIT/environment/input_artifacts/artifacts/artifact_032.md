# artifact_032

Grading ID: GB-0952  
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

**1. Summary**

**a. Verdict:** I have successfully solved the problem. The final answer is that $k$ must be an even positive integer.

**b. Method Sketch:**
Let $S(n, k) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. We want to find all positive integers $k$ such that $n+1$ divides $S(n, k)$ for all positive integers $n$.

1.  **Necessity of $k$ being even.** We examine the case $n=2$. $S(2, k) = 2+2^k$. We require $3 | (2+2^k)$. This holds if and only if $k$ is even. Thus, $k$ must be an even integer, say $k=2m$ for some positive integer $m$.

2.  **Sufficiency of $k$ being even.** We prove that $n+1$ divides $S(n, 2m)$ for all $n \ge 1$ and $m \ge 1$. It suffices to show this when $n+1$ is a prime power, $N=p^r$. Let $n=p^r-1$. We want to show $S(n, 2m) \equiv 0 \pmod{p^r}$.

3.  **Analysis of binomial coefficients modulo $p^r$.** We use the identity $\binom{p^r-1}{i} = (-1)^i \prod_{j=1}^i (1-p^r/j)$. Let $Q(i) = \prod_{j=1}^i (1-p^r/j)$. Then $S(n, 2m) = \sum_{i=0}^n Q(i)^{2m}$.

4.  **$p$-adic expansion.** We analyze $Q(i)$ in the ring of $p$-adic integers $\mathbb{Z}_p$. We decompose the product $Q(i)$ based on the $p$-adic valuation of $j$. Let $j=p^s k$ with $p \nmid k$. Let $t=r-s$.
    $Q(i) = \prod_{t=1}^r P_t(i)$, where $P_t(i) = \prod_{k \in K_t(i)} (1-p^t/k)$, and $K_t(i)$ is the set of $k$ such that $p \nmid k$ and $k \le A_t(i) = \lfloor i/p^{r-t} \rfloor$.

5.  $P_t(i)$ can be viewed as a formal power series in $p^t$ with coefficients in $\mathbb{Z}_p$ that depend on $A_t(i)$. Consequently, $Q(i)$ is a power series in $p$, $Q(i) = 1 + \sum_{j=1}^\infty c_j(i) p^j$, and $F(i) = Q(i)^{2m}$ is also a power series in $p$, $F(i) = 1 + \sum_{j=1}^\infty d_j(i) p^j$, with $d_j(i) \in \mathbb{Z}_p$.

6.  **Dependency on digits.** We analyze the dependency of the coefficients $d_j(i)$ on the base-$p$ digits of $i$. We show that for $j<r$, $d_j(i)$ depends only on $A_1(i), \dots, A_j(i)$. If $i = \sum_{k=0}^{r-1} a_k p^k$, then $A_t(i)$ depends only on $a_{r-1}, \dots, a_{r-t}$. Thus, $d_j(i)$ depends only on the $j$ most significant digits $a_{r-1}, \dots, a_{r-j}$.

7.  **Summation.** We evaluate the sum $S(n, 2m) = \sum_{i=0}^{p^r-1} F(i)$ modulo $p^r$.
    $S(n, 2m) \equiv \sum_{i=0}^{p^r-1} (1 + \sum_{j=1}^{r-1} d_j(i) p^j) \pmod{p^r}$.
    $S(n, 2m) \equiv p^r + \sum_{j=1}^{r-1} p^j \sum_{i=0}^{p^r-1} d_j(i) \pmod{p^r}$.
    We analyze the inner sum $\sum_i d_j(i)$. Since $d_j(i)$ depends only on the top $j$ digits, the sum over the remaining $r-j$ digits yields a factor of $p^{r-j}$.
    $\sum_i d_j(i) = p^{r-j} \cdot (\text{Sum of values of } d_j(i))$.
    Since the values of $d_j(i)$ are in $\mathbb{Z}_p$, the sum is in $\mathbb{Z}_p$. Thus, $v_p(\sum_i d_j(i)) \ge r-j$.
    Then $v_p(p^j \sum_i d_j(i)) \ge j + (r-j) = r$.
    Therefore, $S(n, 2m) \equiv 0 \pmod{p^r}$.

This proves that $k=2m$ is a solution for all $m \ge 1$.

**2. Detailed Solution**

Let $S(n, k) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. We seek all positive integers $k$ such tha

[Note: response truncated to first 3000 characters of 20096]
