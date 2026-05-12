# artifact_089

Grading ID: GB-0956  
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

Let $A_k(n) = \frac{1}{n+1}\sum_{i=0}^{n}\binom{n}{i}^{k}$. We want to find all positive integers $k$ such that $A_k(n)$ is an integer for every positive integer $n$.

Part 1: Prove that $k$ must be an even integer.
Let $k$ be an odd positive integer. We test the condition for $n=2$.
For $n=2$, the expression is:
\[
A_k(2) = \frac{1}{2+1}\sum_{i=0}^{2}\binom{2}{i}^{k} = \frac{1}{3}\left(\binom{2}{0}^k + \binom{2}{1}^k + \binom{2}{2}^k\right)
\]
The binomial coefficients are $\binom{2}{0}=1$, $\binom{2}{1}=2$, $\binom{2}{2}=1$.
\[
A_k(2) = \frac{1^k + 2^k + 1^k}{3} = \frac{2+2^k}{3}
\]
For $A_k(2)$ to be an integer, $2+2^k$ must be divisible by 3. We check this condition modulo 3.
$2 \equiv -1 \pmod 3$.
So, $2+2^k \equiv -1 + (-1)^k \pmod 3$.
Since $k$ is an odd integer, $(-1)^k = -1$.
Therefore, $2+2^k \equiv -1 + (-1) = -2 \equiv 1 \pmod 3$.
The numerator $2+2^k$ is not divisible by 3, so $A_k(2)$ is not an integer.
This shows that no odd positive integer $k$ can satisfy the condition for all positive integers $n$.
Thus, $k$ must be an even integer.

Part 2: Prove that if $k$ is an even integer, the condition holds for all $n$.
Let $k$ be an even positive integer. We want to prove that $A_k(n)$ is an integer for every positive integer $n$. This is equivalent to proving that for all $n \ge 1$,
\[ \sum_{i=0}^{n}\binom{n}{i}^{k} \equiv 0 \pmod{n+1} \]
Let $d = n+1$. We want to show that $\sum_{i=0}^{n}\binom{n}{i}^{k}$ is divisible by $d$.
Let $p$ be a prime factor of $d$. Let $v_p(d) = a$ be the largest power of $p$ dividing $d$. It is sufficient to show that $\sum_{i=0}^{n}\binom{n}{i}^{k} \equiv 0 \pmod{p^a}$ for every prime power factor $p^a$ of $d$.

We have $n = d-1$. The binomial coefficient $\binom{n}{i}$ can be written as $\binom{d-1}{i}$.
For any $j \in \{0, 1, \dots, i-1\}$, we have $n-j = (d-1)-j \equiv -1-j \pmod d$.
In particular, $n-j \equiv -1-j \pmod{p^a}$ for each $j$.
The binomial coefficient $\binom{n}{i}$ is given by $\binom{n}{i} = \frac{n(n-1)\cdots(n-i+1)}{i!}$.
Multiplying by $i!$ gives $i!\binom{n}{i} = n(n-1)\cdots(n-i+1)$.
Modulo $p^a$, we have:
\[
i!\binom{n}{i} \equiv \prod_{j=0}^{i-1} (-1-j) = (-1)^i \prod_{j=1}^{i} j = (-1)^i i! \pmod{p^a}
\]
This congruence means that $i!\left(\binom{n}{i} - (-1)^i\right)$ is divisible by $p^a$.
Let $\delta_i = \binom{n}{i} - (-1)^i$. Then $i! \delta_i \equiv 0 \pmod{p^a}$.

We want to prove $\sum_{i=0}^n \binom{n}{i}^k \equiv 0 \pmod{p^a}$.
Since $k$ is an even positive integer, let $k=2m$ for some positive integer $m$.
Then $( (-1)^i )^k = ((-1)^2)^{im} = 1^{im} = 1$ for all $i$.
We are required to prove $\sum_{i=0}^n \binom{n}{i}^k \equiv 0 \pmod{d}$.

Consider the identity $(n-i)\binom{n}{i} = n\binom{n-1}{i}$. Another useful identity is $(n-i)\binom{n}{i} = (i+1)\binom{n}{i+1}$, which is incorrect. The correct identity is $(n-i)\binom{n}{i} = n\binom{n-1}{i}$, and $i\binom{n}{i} = n\binom{n-1}{i-1}$. The relation between adjacent coefficients is $\binom{n}{i+1} = \frac{n-i}{i+1

[Note: response truncated to first 3000 characters of 9288]
