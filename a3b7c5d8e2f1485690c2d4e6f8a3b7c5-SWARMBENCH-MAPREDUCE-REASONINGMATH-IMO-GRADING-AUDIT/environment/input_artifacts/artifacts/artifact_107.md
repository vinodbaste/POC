# artifact_107

Grading ID: GB-0946  
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

We want to determine all positive integers $k$ such that
\[
A_k(n) = \frac{1}{n+1}\sum_{i=0}^{n}\binom{n}{i}^{k}
\]
is an integer for every positive integer $n$. Let $S_k(n) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. The condition is equivalent to $n+1$ dividing $S_k(n)$ for all $n \ge 1$.

We will prove that this condition holds if and only if $k$ is an even positive integer.

### Part 1: Necessity (k must be even)

We show that if $k$ is odd, there exists an $n$ such that $A_k(n)$ is not an integer.
Let us consider $n=2$. Then $n+1=3$. We require $3 \mid S_k(2)$.
\[
S_k(2) = \binom{2}{0}^k + \binom{2}{1}^k + \binom{2}{2}^k = 1^k + 2^k + 1^k = 2+2^k.
\]
We examine this value modulo 3:
\[
S_k(2) = 2+2^k \equiv -1 + (-1)^k \pmod 3.
\]
If $k$ is odd, then $(-1)^k = -1$.
\[
S_k(2) \equiv -1 + (-1) = -2 \equiv 1 \pmod 3.
\]
Thus, if $k$ is odd, $S_k(2)$ is not divisible by 3, so $A_k(2)$ is not an integer.
Therefore, $k$ must be even.

### Part 2: Sufficiency (k is even)

Let $k=2m$ for some positive integer $m$. We want to show that $n+1$ divides $S_{2m}(n)$ for all $n \ge 1$.
To prove this, it is sufficient to show that for any prime $p$, the $p$-adic valuation satisfies $v_p(n+1) \le v_p(S_{2m}(n))$.

We rely on a theorem established by N. J. Calkin (1998) concerning the divisibility properties of $S_{2m}(n)$.

**Theorem (Calkin, 1998).** Let $m, n$ be positive integers. Let $p$ be a prime, and let $n = \sum_{i=0}^d n_i p^i$ be the base $p$ expansion of $n$ (where $0 \le n_i < p$). Then
\[
\prod_{i=0}^d S_{2m}(n_i) \quad \text{divides} \quad S_{2m}(n).
\]
As a consequence, for the $p$-adic valuation, we have:
\[
v_p(S_{2m}(n)) \ge \sum_{i=0}^d v_p(S_{2m}(n_i)).
\]

Let $p$ be an arbitrary prime divisor of $n+1$. Let $r = v_p(n+1)$. We want to show that $v_p(S_{2m}(n)) \ge r$.
We can write $n+1 = p^r M$, where $p \nmid M$. Then $n = p^r M - 1$.
We analyze the base $p$ expansion of $n$.
We can write $n$ as:
\[
n = (M p^r - p^r) + (p^r - 1) = (M-1)p^r + \sum_{i=0}^{r-1} (p-1)p^i.
\]
The digits of $n$ in base $p$ are $n_i = p-1$ for $i=0, 1, \dots, r-1$. The subsequent digits $n_i$ for $i \ge r$ correspond to the base $p$ expansion of $M-1$.

Applying Calkin's theorem:
\[
v_p(S_{2m}(n)) \ge \sum_{i=0}^d v_p(S_{2m}(n_i)) = \sum_{i=0}^{r-1} v_p(S_{2m}(n_i)) + \sum_{i=r}^d v_p(S_{2m}(n_i)).
\]
Since $S_{2m}(n_i)$ are integers, the valuations $v_p(S_{2m}(n_i))$ are non-negative.
For $i=0, \dots, r-1$, we have $n_i=p-1$. Thus,
\[
v_p(S_{2m}(n)) \ge \sum_{i=0}^{r-1} v_p(S_{2m}(p-1)) = r \cdot v_p(S_{2m}(p-1)).
\]

Now we need to analyze $v_p(S_{2m}(p-1))$.
\[
S_{2m}(p-1) = \sum_{i=0}^{p-1} \binom{p-1}{i}^{2m}.
\]
We use the property that for $0 \le i \le p-1$, $\binom{p-1}{i} \equiv (-1)^i \pmod p$. This follows from the identity $\binom{p-1}{i} = \frac{(p-1)(p-2)\cdots(p-i)}{i!} \equiv \frac{(-1)(-2)\cdots(-i)}{i!} = (-1)^i \pmod p$.

We examine $S_{2m}(p-1)$ modulo $p$:
\[
S_{2m}(p-1) \equiv \sum_{i=0}^{p-1} ((-1)^i)^{2m} = \sum_{i=0}^{p-1} ((-1)^{2m})^i = \sum_{

[Note: response truncated to first 3000 characters of 3557]
