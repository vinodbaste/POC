# artifact_051

Grading ID: GB-0968  
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

We are asked to determine all positive integers $k$ such that
\[
A_k(n) = \frac{1}{n+1}\sum_{i=0}^{n}\binom{n}{i}^{k}
\]
is an integer for every positive integer $n$.

Let $S_k(n) = \sum_{i=0}^{n}\binom{n}{i}^{k}$. The condition is that $n+1$ divides $S_k(n)$ for all $n \geq 1$.

**Part 1: Proving that $k$ must be even**

We test the condition for $n=2$. We require $n+1=3$ to divide $S_k(2)$.
\[
S_k(2) = \sum_{i=0}^{2}\binom{2}{i}^{k} = \binom{2}{0}^k + \binom{2}{1}^k + \binom{2}{2}^k = 1^k + 2^k + 1^k = 2 + 2^k.
\]
We must have $S_k(2) \equiv 0 \pmod 3$.
Since $2 \equiv -1 \pmod 3$, we have:
\[
S_k(2) = 2 + 2^k \equiv (-1) + (-1)^k \pmod 3.
\]
For $S_k(2) \equiv 0 \pmod 3$, we must have $(-1) + (-1)^k = 0$, which means $(-1)^k = 1$.
Since $k$ is a positive integer, this implies that $k$ must be even.

**Part 2: Proving that if $k$ is even, the condition holds**

Let $k=2m$ for some positive integer $m$. We will prove that $n+1$ divides $S_{2m}(n)$ for all $n \geq 1$.

Let $N = n+1$. We want to show $N \mid S_{2m}(n)$.
Let $T_i = \binom{n}{i} = \binom{N-1}{i}$ for $i=0, 1, \ldots, n$. We define $T_{-1}=0$.

We utilize two standard binomial identities for $1 \le i \le n$:
1.  **Pascal's Identity:** $\binom{N}{i} = \binom{N-1}{i} + \binom{N-1}{i-1} = T_i + T_{i-1}$.
2.  **Absorption Identity:** $i \binom{N}{i} = N \binom{N-1}{i-1} = N T_{i-1}$.

Let $A_i = T_i^{2m} - T_{i-1}^{2m}$ for $i=1, \ldots, n$.

**Lemma:** $N$ divides $i A_i$ for $i=1, \ldots, n$.

*Proof:* For any integers $x$ and $y$, $x+y$ divides $x^{2m} - y^{2m}$.
Let $C_i = \binom{N}{i}$. By Pascal's Identity, $C_i = T_i + T_{i-1}$.
Thus, $C_i$ divides $A_i = T_i^{2m} - T_{i-1}^{2m}$.
Since $n \ge 1$ and $1 \le i \le n$, $C_i > 0$. We can write $A_i = M_i C_i$ for some integer $M_i$.

Now consider $i A_i$:
$i A_i = M_i (i C_i)$.
By the Absorption Identity, $i C_i = N T_{i-1}$.
Therefore, $i A_i = M_i (N T_{i-1}) = N (M_i T_{i-1})$.
Since $M_i T_{i-1}$ is an integer, $N$ divides $i A_i$.

**Main Argument:**

Consider the sum $X = \sum_{i=1}^{n} i A_i$. By the Lemma, $N$ divides every term $i A_i$, so $N$ divides $X$.

We now evaluate $X$ by manipulating the summation (summation by parts):
\begin{align*} X &= \sum_{i=1}^{n} i A_i = \sum_{i=1}^{n} i (T_i^{2m} - T_{i-1}^{2m}) \\ &= \sum_{i=1}^{n} i T_i^{2m} - \sum_{i=1}^{n} i T_{i-1}^{2m} \end{align*}
We reindex the second sum by setting $j=i-1$:
\[ \sum_{i=1}^{n} i T_{i-1}^{2m} = \sum_{j=0}^{n-1} (j+1) T_j^{2m} \]
Substituting back and changing the index variable back to $i$:
\begin{align*} X &= \sum_{i=1}^{n} i T_i^{2m} - \sum_{i=0}^{n-1} (i+1) T_i^{2m} \\ &= \left( n T_n^{2m} + \sum_{i=1}^{n-1} i T_i^{2m} \right) - \left( T_0^{2m} + \sum_{i=1}^{n-1} (i+1) T_i^{2m} \right). \end{align*}
We know $T_n = \binom{n}{n} = 1$ and $T_0 = \binom{n}{0} = 1$. So $T_n^{2m}=1$ and $T_0^{2m}=1$.
\begin{align*} X &= n(1) - 1 + \sum_{i=1}^{n-1} \left( i T_i^{2m} - (i+1) T_i^{2m} \right) \\ &= n - 1 + \sum_{i=1}^{n-1} (i - (i+1)) T_i^{2m} \\ &= n - 1 - 

[Note: response truncated to first 3000 characters of 3842]
