# artifact_097

Grading ID: GB-0943  
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

The problem asks to determine all positive integers $k$ such that
\[
A_k(n) = \frac{1}{n+1}\sum_{i=0}^{n}\binom{n}{i}^{k}
\]
is an integer for every positive integer $n$. Let $S_k(n) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. The condition is that $(n+1)$ divides $S_k(n)$ for all $n \ge 1$.

We will show that the required integers $k$ are precisely all even positive integers.

Part 1: Necessity of $k$ being even.
We test the condition for small values of $n$.
Let $n=2$. Then $n+1=3$. We require $3 | S_k(2)$.
$S_k(2) = \binom{2}{0}^k + \binom{2}{1}^k + \binom{2}{2}^k = 1^k + 2^k + 1^k = 2+2^k$.
We need $2+2^k \equiv 0 \pmod 3$.
Since $2 \equiv -1 \pmod 3$, we have $2+2^k \equiv -1+(-1)^k \pmod 3$.
For this to be $0 \pmod 3$, we must have $(-1)^k = 1$. This implies that $k$ must be an even positive integer.

Alternatively, we can use $n=p-1$ where $p$ is an odd prime. Then $n+1=p$. We require $p|S_k(p-1)$.
We know that $\binom{p-1}{i} \equiv (-1)^i \pmod p$ for $0 \le i \le p-1$.
$S_k(p-1) = \sum_{i=0}^{p-1} \binom{p-1}{i}^k \equiv \sum_{i=0}^{p-1} ((-1)^i)^k = \sum_{i=0}^{p-1} (-1)^{ik} \pmod p$.
If $k$ is odd, $(-1)^{ik} = (-1)^i$.
$S_k(p-1) \equiv \sum_{i=0}^{p-1} (-1)^i \pmod p$.
Since $p$ is odd, $p-1$ is even. The sum is $1-1+1-\cdots+1 = 1$.
$S_k(p-1) \equiv 1 \pmod p$. Thus $p \nmid S_k(p-1)$, so $A_k(p-1)$ is not an integer.
Therefore, $k$ must be even.

Part 2: Sufficiency of $k$ being even.
We want to show that if $k=2h$ for some positive integer $h$, then $(n+1) | S_{2h}(n)$ for all $n \ge 1$.

Case $h=1$ (k=2).
$S_2(n) = \sum_{i=0}^{n}\binom{n}{i}^2$. By the Vandermonde's Identity, this sum is equal to the coefficient of $x^n$ in $(1+x)^n(1+x)^n=(1+x)^{2n}$, which is $\binom{2n}{n}$.
$A_2(n) = \frac{1}{n+1}\binom{2n}{n}$. This is the $n$-th Catalan number $C_n$.
We can show that $C_n$ is an integer by using the identity:
$C_n = \binom{2n}{n} - \binom{2n}{n+1}$.
To verify this identity:
\begin{align*} \binom{2n}{n} - \binom{2n}{n+1} &= \frac{(2n)!}{n!n!} - \frac{(2n)!}{(n+1)!(n-1)!} \\ &= \frac{(2n)!}{n!(n-1)!} \left(\frac{1}{n} - \frac{1}{n+1}\right) \\ &= \frac{(2n)!}{n!(n-1)!} \frac{(n+1)-n}{n(n+1)} \\ &= \frac{(2n)!}{n!(n-1)!} \frac{1}{n(n+1)} = \frac{(2n)!}{(n!)^2 (n+1)} \\ &= \frac{1}{n+1}\binom{2n}{n}. \end{align*}
Since $\binom{2n}{n}$ and $\binom{2n}{n+1}$ are integers, $C_n$ is an integer. Thus $k=2$ is a solution.

General case $k=2h$.
The statement that $(n+1)$ divides $S_{2h}(n)$ for all $h \ge 1$ and $n \ge 1$ is a known result in combinatorics. It was first proved by Kálmán von Szily in 1894. More modern proofs are also available, for example by Calkin (1998) and Gessel (2003), but they are quite involved, relying on advanced techniques such as generating functions, $p$-adic analysis, or intricate combinatorial identities.

For instance, one approach uses the identity relating $S_k(n)$ and $T_k(N) = \sum_{j=1}^N j^k \binom{N}{j}^k$, where $N=n+1$.
We have the identity $j\binom{N}{j} = N\binom{N-1}{j-1}$.
$T_k(N) = \sum_{j=1}^N \l

[Note: response truncated to first 3000 characters of 3595]
