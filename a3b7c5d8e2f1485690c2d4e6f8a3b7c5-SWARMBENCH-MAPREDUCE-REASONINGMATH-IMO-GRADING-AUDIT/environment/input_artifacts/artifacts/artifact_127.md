# artifact_127

Grading ID: GB-0965  
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

Let $S_k(n) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. The condition is that $n+1$ must divide $S_k(n)$ for all $n \ge 1$.

We will show that this condition holds if and only if $k$ is a positive even integer.

### Part 1: Showing $k$ must be even

We test the condition for $n=2$. We require $A_k(2)$ to be an integer, which means $n+1=3$ must divide $S_k(2)$.
\[
S_k(2) = \binom{2}{0}^k + \binom{2}{1}^k + \binom{2}{2}^k = 1^k + 2^k + 1^k = 2 + 2^k.
\]
We must have $S_k(2) \equiv 0 \pmod 3$.
Since $2 \equiv -1 \pmod 3$, we have $2^k \equiv (-1)^k \pmod 3$.
\[
S_k(2) = 2 + 2^k \equiv -1 + (-1)^k \pmod 3.
\]
For $S_k(2) \equiv 0 \pmod 3$, we must have $-1 + (-1)^k = 0$, which means $(-1)^k = 1$. Since $k$ is a positive integer, $k$ must be even.

### Part 2: Showing the condition holds if $k$ is even

Let $k=2m$ for some positive integer $m$. We must show that $n+1$ divides $S_{2m}(n)$ for all $n \ge 1$.

Let $L = n+1$. Let $R_i = \binom{n}{i}$ for $i=0, 1, \ldots, n$. We define $R_{-1}=0$.

We first establish some necessary facts.

**Fact 1 (Algebraic Factorization):** For integers $A, B$ and positive integer $m$, $A+B$ divides $A^{2m}-B^{2m}$.
*Proof:* We know that $X-Y$ divides $X^m-Y^m$. Let $X=A^2$ and $Y=B^2$. Then $A^2-B^2$ divides $A^{2m}-B^{2m}$. Since $A^2-B^2 = (A+B)(A-B)$, $A+B$ divides $A^2-B^2$. Therefore, $A+B$ divides $A^{2m}-B^{2m}$.

**Fact 2 (Pascal's Identity):** For $1 \le j \le n$, $R_j + R_{j-1} = \binom{n+1}{j} = \binom{L}{j}$.
*Proof:* $\binom{n}{j} + \binom{n}{j-1} = \frac{n!}{j!(n-j)!} + \frac{n!}{(j-1)!(n-j+1)!} = \frac{n!(n-j+1) + n!j}{j!(n-j+1)!} = \frac{n!(n+1)}{j!(L-j)!} = \binom{n+1}{j}$.

**Fact 3 (Absorption Identity):** For $L \ge 1, j \ge 1$, $j\binom{L}{j} = L\binom{L-1}{j-1}$.
*Proof:* $j\binom{L}{j} = j \frac{L!}{j!(L-j)!} = \frac{L!}{(j-1)!(L-j)!} = L \frac{(L-1)!}{(j-1)!(L-j)!} = L\binom{L-1}{j-1}$.

Now we analyze $S_{2m}(n)$.

Let $T_j = R_j^{2m} - R_{j-1}^{2m}$ for $j=0, 1, \dots, n$.
We can express $R_i^{2m}$ as a telescoping sum:
\[
R_i^{2m} = R_{-1}^{2m} + \sum_{j=0}^i (R_j^{2m} - R_{j-1}^{2m}) = 0 + \sum_{j=0}^i T_j.
\]

We rewrite $S_{2m}(n)$:
\[
S_{2m}(n) = \sum_{i=0}^n R_i^{2m} = \sum_{i=0}^n \sum_{j=0}^i T_j.
\]
We interchange the order of summation (indices $0 \le j \le i \le n$):
\[
S_{2m}(n) = \sum_{j=0}^n \sum_{i=j}^n T_j = \sum_{j=0}^n T_j (n-j+1).
\]
Since $L=n+1$, we have $n-j+1 = L-j$.
\[
S_{2m}(n) = \sum_{j=0}^n (L-j) T_j = \sum_{j=0}^n (L T_j - j T_j) = L \sum_{j=0}^n T_j - \sum_{j=0}^n j T_j.
\]

The first sum is telescoping:
\[
\sum_{j=0}^n T_j = \sum_{j=0}^n (R_j^{2m} - R_{j-1}^{2m}) = R_n^{2m} - R_{-1}^{2m}.
\]
Since $R_n = \binom{n}{n} = 1$ and $R_{-1}=0$, we have $\sum_{j=0}^n T_j = 1^{2m} - 0 = 1$.

Thus,
\[
S_{2m}(n) = L \cdot 1 - \sum_{j=0}^n j T_j = L - \sum_{j=1}^n j T_j.
\]
(The $j=0$ term in the sum is $0 \cdot T_0 = 0$.)



[Note: response truncated to first 3000 characters of 4184]
