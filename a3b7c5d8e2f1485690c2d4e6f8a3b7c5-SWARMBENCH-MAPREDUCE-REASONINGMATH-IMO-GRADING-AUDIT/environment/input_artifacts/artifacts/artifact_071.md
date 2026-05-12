# artifact_071

Grading ID: GB-0950  
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
is an integer for every positive integer $n$.

Let $S_k(n) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. The condition is that $n+1$ divides $S_k(n)$ for all $n \ge 1$.

We will prove that this condition holds if and only if $k$ is an even positive integer.

### Part 1: Necessity ($k$ must be even)

We test the condition for $n=2$. We require $A_k(2)$ to be an integer.
$n+1 = 3$. We must have $3 \mid S_k(2)$.
\[
S_k(2) = \sum_{i=0}^{2}\binom{2}{i}^{k} = \binom{2}{0}^k + \binom{2}{1}^k + \binom{2}{2}^k = 1^k + 2^k + 1^k = 2 + 2^k.
\]
We require $S_k(2) \equiv 0 \pmod 3$.
Since $2 \equiv -1 \pmod 3$, we have:
\[
2 + 2^k \equiv (-1) + (-1)^k \pmod 3.
\]
For this to be $0 \pmod 3$, we must have $(-1)^k = 1$. This implies that $k$ must be an even integer.
Since $k$ is a positive integer, $k$ must be a positive even integer.

(For example, if $k=1$, $A_1(2) = (2+2^1)/3 = 4/3$, which is not an integer.)

### Part 2: Sufficiency ($k$ is even)

Let $k=2m$ for some positive integer $m$. We want to show that $A_{2m}(n)$ is an integer for all $n \ge 1$.

#### Case m=1 (k=2)

We examine $S_2(n) = \sum_{i=0}^{n}\binom{n}{i}^2$.
Using the Vandermonde Identity, we know that $S_2(n) = \binom{2n}{n}$.
Then,
\[
A_2(n) = \frac{1}{n+1}\binom{2n}{n}.
\]
This is the $n$-th Catalan number, $C_n$. We prove that $C_n$ is an integer.
We can use the identity:
\[
\binom{2n}{n+1} = \frac{(2n)!}{(n+1)!(n-1)!} = \frac{n}{n+1} \frac{(2n)!}{n!n!} = \frac{n}{n+1}\binom{2n}{n}.
\]
Then,
\begin{align*} C_n &= \frac{1}{n+1}\binom{2n}{n} = \frac{(n+1)-n}{n+1}\binom{2n}{n} \\ &= \binom{2n}{n} - \frac{n}{n+1}\binom{2n}{n} \\ &= \binom{2n}{n} - \binom{2n}{n+1}. \end{align*}
Since binomial coefficients are integers, $C_n$ is an integer.
Thus, $k=2$ is a solution.

#### General case (k=2m, m $\ge$ 1)

We want to show that $A_{2m}(n) = S_{2m}(n)/(n+1)$ is an integer.

We rely on a known result in combinatorial number theory regarding the divisibility of $S_{2m}(n)$.

**Theorem (Calkin, 1998):** For any positive integers $m$ and $n$, the central binomial coefficient $\binom{2n}{n}$ divides the sum of powers $S_{2m}(n) = \sum_{i=0}^{n}\binom{n}{i}^{2m}$.

(This result generalized earlier findings, for instance by Glaisher (1899), who proved that $n+1$ divides $S_{2m}(n)$.)

By Calkin's theorem, we can write $S_{2m}(n)$ as:
\[
S_{2m}(n) = Q_m(n) \cdot \binom{2n}{n},
\]
where $Q_m(n)$ is an integer.

Now we can express $A_{2m}(n)$:
\[
A_{2m}(n) = \frac{S_{2m}(n)}{n+1} = \frac{Q_m(n) \cdot \binom{2n}{n}}{n+1} = Q_m(n) \cdot \left( \frac{1}{n+1}\binom{2n}{n} \right).
\]
The term in the parentheses is the $n$-th Catalan number $C_n$, which we have established is an integer.
\[
A_{2m}(n) = Q_m(n) \cdot C_n.
\]
Since $Q_m(n)$ (by Calkin's theorem) and $C_n$ are both integers, their product $A_{2m}(n)$ is an integer for all positive integers $m$ and $n$.

Therefore, if $k$ is an even positive inte

[Note: response truncated to first 3000 characters of 3207]
