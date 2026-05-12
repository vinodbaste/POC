# artifact_014

Grading ID: GB-0966  
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
is an integer for every positive integer $n$. Let $S_k(n) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. The condition is that $n+1$ divides $S_k(n)$ for all $n \ge 1$.

Part 1: Necessity of $k$ being even.

We test the condition for $n=2$. We require $n+1=3$ to divide $S_k(2)$.
$S_k(2) = \binom{2}{0}^k + \binom{2}{1}^k + \binom{2}{2}^k = 1^k + 2^k + 1^k = 2+2^k$.
We analyze this modulo 3:
$S_k(2) = 2+2^k \equiv -1 + (-1)^k \pmod 3$.
For $S_k(2)$ to be divisible by 3, we must have $-1+(-1)^k \equiv 0 \pmod 3$, which means $(-1)^k = 1$. This implies that $k$ must be an even positive integer.

Part 2: Sufficiency of $k$ being even.

Let $k=2m$ for some positive integer $m$. We want to show that $n+1$ divides $S_{2m}(n)$ for all $n \ge 1$.
Let $N=n+1$. We want to show $N \mid S_{2m}(N-1)$. It is sufficient to show that for any prime power $p^r$ such that $p^r || N$ (i.e., $v_p(N)=r$), we have $p^r \mid S_{2m}(N-1)$.

We first prove a crucial lemma regarding congruences of binomial coefficients, known as Calkin's Lemma (1998).

Lemma 1. Let $p$ be a prime and $r \ge 1$ an integer. Let $N$ be a multiple of $p^r$. For $0 \le l < N$, let $q = \lfloor l/p \rfloor$. Then
\[
\binom{N-1}{l} \equiv (-1)^{l+q} \binom{N/p-1}{q} \pmod{p^r}.
\]

Proof: We use the identity for binomial coefficients as a product:
\[
\binom{N-1}{l} = \frac{(N-1)(N-2)\cdots(N-l)}{l!} = (-1)^l \prod_{j=1}^l \frac{j-N}{j} = (-1)^l \prod_{j=1}^l \left(1 - \frac{N}{j}\right).
\]
We split the product into two parts: $P_1$ corresponding to indices $j$ not divisible by $p$, and $P_2$ corresponding to indices $j$ divisible by $p$.
\[
P_1 = \prod_{\substack{1\le j \le l \\ p \nmid j}} \left(1 - \frac{N}{j}\right), \quad P_2 = \prod_{\substack{1\le j \le l \\ p \mid j}} \left(1 - \frac{N}{j}\right).
\]
For $P_1$, let $D = \prod_{p \nmid j, 1\le j \le l} j$. Since $p \nmid j$, $\gcd(D, p^r)=1$.
We look at $D P_1 = \prod_{p \nmid j} (j-N)$.
Since $p^r \mid N$, $N \equiv 0 \pmod{p^r}$. Thus $j-N \equiv j \pmod{p^r}$.
$D P_1 \equiv \prod_{p \nmid j} j = D \pmod{p^r}$.
Since $D$ is invertible modulo $p^r$, we can multiply by $D^{-1}$ to get $P_1 \equiv 1 \pmod{p^r}$.

For $P_2$, the indices are $j=sp$ for $s=1, 2, \dots, q$, where $q=\lfloor l/p \rfloor$.
\[
P_2 = \prod_{s=1}^q \left(1 - \frac{N}{sp}\right) = \prod_{s=1}^q \left(1 - \frac{N/p}{s}\right).
\]
Let $N' = N/p$. $N'$ is an integer.
\[
P_2 = \prod_{s=1}^q \frac{s-N'}{s} = \frac{(1-N')(2-N')\cdots(q-N')}{q!}.
\]
We recognize this expression as related to $\binom{N'-1}{q}$.
\[
\binom{N'-1}{q} = \frac{(N'-1)(N'-2)\cdots(N'-q)}{q!}.
\]
So, $P_2 = (-1)^q \binom{N'-1}{q} = (-1)^q \binom{N/p-1}{q}$.

Combining the results, we have the identity of rational numbers:
\[
\binom{N-1}{l} = (-1)^l P_1 P_2 = (-1)^{l+q} P_1 \binom{N/p-1}{q}.
\]
Let $Q = \binom{N/p-1}{q}$. $Q$ is an integer.
We know $P_1 \equiv 1 \pmod{p^r}$. This means $D(P_1-1)$ is 

[Note: response truncated to first 3000 characters of 5951]
