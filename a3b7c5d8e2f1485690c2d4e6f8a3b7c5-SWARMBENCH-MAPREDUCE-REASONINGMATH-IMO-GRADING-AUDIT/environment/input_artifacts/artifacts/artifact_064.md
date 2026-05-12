# artifact_064

Grading ID: GB-0671  
Problem ID: PB-Advanced-020  
Source: (Modified) IMO 2024 P2  
IMO Area: Number_Theory

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

For given positive integers $x$ and $y$, we define a sequence $(a_n)_{n \ge 1}$ as
 $$
 a_n = \gcd \left( x^n +y , \, (y-x)\left(\sum_{i=0}^{n-1} y^i x^{n-i-1} - 1\right) \right)
 $$
 for all $n\in \mathbb{N}$. Find all pairs $(x,y)$ of positive integers such that the limit of the sequence $(a_n)$ exists.

## Reference Solution (for grader's calibration)

To begin with, we can change the expression in the problem to
 $\gcd \left( x^n +y , \, (y-x)\left(\sum_{i=0}^{n-1} y^i x^{n-i-1} - 1\right) \right) = \gcd \left( x^n +y , \, y^n - x^n -(y-x) \right) = \gcd(x^n +y , y^n +x)$.
 Let the limit of the sequence $(a_n)$ exist and be equal to $g$. Then, for sufficiently large $n$,

 Lemma. If the limit of $a_n$ as $n \to \infty$ exists and is equal to $g$, then $g$ divides $2 \gcd(x, y)$.

 Proof. For sufficiently large $n$, we have $a_n = \gcd \left( x^n +y , \, y^n +x \right) = g$.
 This implies that $g$ divides $x^n + y$ and $g$ divides $y^n +x$ for all $n \ge N$, for some positive integer $N$.

 Consider $n \ge N$. We have $x^n + y \equiv 0 \pmod{g}$ and $x^{n+1} + y \equiv 0 \pmod{g}$.
 Multiplying the first congruence by $x$, we get $x^{n+1} + xy \equiv 0 \pmod{g}$.
 Subtracting the second congruence from this, we have $(x^{n+1} + xy) - (x^{n+1} + y) \equiv 0 - 0 \pmod{g}$, which simplifies to $xy - y = y(x-1) \equiv 0 \pmod{g}$.

 Analogously, $x(y-1)$ is divisible by $g$.
 Their difference $x-y$ is then divisible by $g$, so $g$ also divides
 $x(y-1)+x(x-y)=x^2 -x$. All powers of $x$ are then congruent modulo
 $g$, so $x+y\equiv x^{N}+y\equiv0(\bmod g)$. Then $2x=(x+y)+(x-y)$
 and $2y=(x+y)-(x-y)$ are both divisible by $g$, so $g\mid2\operatorname{gcd}(x,y)$.
 On the other hand, it is clear that $\operatorname{gcd}(x,y)\mid g$,
 thus proving the Lemma.

 Let $d=\operatorname{gcd}(x,y)$, and write $x=da$ and $y=db$ for
 coprime positive integers $a$ and $b$. We have that

 \[
 \operatorname{gcd}\left((da)^{n}+db,(db)^{n}+da\right)=d\operatorname{gcd}\left(d^{n-1}a^{n}+b,d^{n-1}b^{n}+a\right)
 \]

 so the Lemma tells us that

 \[
 \operatorname{gcd}\left(d^{n-1}a^{n}+b,d^{n-1}b^{n}+a\right)\leqslant2
 \]

 for all $n\geqslant N$. Defining $K=d^{2}ab+1$, note that $K$ is
 coprime to each of $d,a$, and $b$. By Euler's theorem, for $n\equiv-1(\bmod\varphi(K))$
 we have that

 \[
 d^{n-1}a^{n}+b\equiv d^{-2}a^{-1}+b\equiv d^{-2}a^{-1}\left(1+d^{2}ab\right)\equiv 0\quad(\bmod K)
 \]

 so $K\mid d^{n-1}a^{n}+b$. Analogously, we have that $K\mid d^{n-1}b^{n}+a$.
 Taking such an $n$ which also satisfies $n\geqslant N$ gives us
 that

 \[
 K\mid\operatorname{gcd}\left(d^{n-1}a^{n}+b,d^{n-1}b^{n}+a\right)\leqslant2
 \]

 This is only possible when $d=a=b=1$, which yields the only solution
 $(x,y)=(1,1)$. Therefore, the only solution is $(x,y)=(1,1)$.

## Grading Guidelines

(Partial)
 1. Considered a prime $p|xy+1$.
(Almost)
 1. Solution is almost complete, but made minor mistakes which are not negligible.
 2. Omitted the case when $xy+1$ doesn't have an odd prime factor.

## Candidate Response (to be graded)

The sequence is defined as $a_n = \gcd \left( x^n +y , \, (y-x)\left(\sum_{i=0}^{n-1} y^i x^{n-i-1} - 1\right) \right)$.
Since $(a_n)$ is a sequence of positive integers, the limit exists if and only if the sequence is eventually constant.

Case 1: $x=y$.
The second term in the gcd is $(x-x)(\dots) = 0$.
$a_n = \gcd(x^n+x, 0) = x^n+x$.
If $x=1$, then $(x,y)=(1,1)$. $a_n = 1^n+1 = 2$. The sequence is constant, so the limit exists.
If $x>1$, $a_n = x^n+x$ is strictly increasing and tends to infinity. The limit does not exist.

Case 2: $x \ne y$.
The sum is $\sum_{i=0}^{n-1} y^i x^{n-i-1} = \frac{y^n-x^n}{y-x}$.
The second term is $(y-x)\left(\frac{y^n-x^n}{y-x} - 1\right) = y^n-x^n - (y-x) = y^n-x^n-y+x$.
$a_n = \gcd(x^n+y, y^n-x^n-y+x)$.
Since $\gcd(A, B) = \gcd(A, A+B)$, we have
$a_n = \gcd(x^n+y, (x^n+y) + (y^n-x^n-y+x)) = \gcd(x^n+y, y^n+x)$.
Without loss of generality, assume $y>x$.

Case 2.1: $x=1$. $y>1$.
$a_n = \gcd(1+y, y^n+1)$.
Let $K=1+y$. Then $y \equiv -1 \pmod K$.
$y^n+1 \equiv (-1)^n+1 \pmod K$.
If $n$ is odd, $y^n+1 \equiv 0 \pmod K$, so $a_n = K = 1+y$.
If $n$ is even, $y^n+1 \equiv 2 \pmod K$, so $a_n = \gcd(1+y, 2)$.
For the limit to exist, the sequence must be eventually constant. Thus $1+y = \gcd(1+y, 2)$.
This means $1+y$ divides 2. Since $y>1$, $1+y>2$. This is impossible.
So the limit does not exist in this case.

Case 2.2: $y>x>1$.
Suppose the limit exists, $a_n \to L$. Then $a_n=L$ for $n \ge N$.
$L \mid x^n+y$ and $L \mid y^n+x$ for $n \ge N$.

Case 2.2.1: $\gcd(x,y)=1$.
$L \mid x^N+y$ and $L \mid x^{N+1}+y$. So $L$ divides their difference $x^N(x-1)$.
If $p$ is a prime dividing $L$. If $p|x$, then $p|x^N+y$ implies $p|y$. This contradicts $\gcd(x,y)=1$. So $\gcd(L,x)=1$.
Thus $L \mid x-1$. Similarly, $L \mid y-1$.
So $x \equiv 1 \pmod L$ and $y \equiv 1 \pmod L$.
$x^n+y \equiv 1^n+1 = 2 \pmod L$. Since $L \mid x^n+y$, we must have $L \mid 2$. So $L \in \{1, 2\}$.

Since $x>1, y>1$ and $\gcd(x,y)=1$, $x+y \ge 2+3=5$.
If $x+y$ has an odd prime factor $p$. $p \ge 3$. $y \equiv -x \pmod p$. $\gcd(x,p)=1$.
For odd $n$, $x^n+y \equiv x^n-x = x(x^{n-1}-1) \pmod p$. $y^n+x \equiv -x^n+x = -x(x^{n-1}-1) \pmod p$.
Let $h=\text{ord}_p(x)$. Choose $n=2kh+1$. Then $n$ is odd and $x^{n-1} \equiv 1 \pmod p$.
So $p \mid a_n$ infinitely often. Thus $p \mid L$. This contradicts $L \in \{1, 2\}$.

If $x+y$ has no odd prime factors, $x+y=2^k$. Since $\gcd(x,y)=1$, $x, y$ must be odd.
Since $1<x<y$, $x \ge 3, y \ge 5$. So $x+y \ge 8$. $k \ge 3$.
Since $x+y \equiv 0 \pmod 4$, one of $x, y$ is $1 \pmod 4$ and the other is $3 \pmod 4$.
If $n$ is even. $x^n \equiv 1 \pmod 4$ and $y^n \equiv 1 \pmod 4$.
$x^n+y$. WLOG $y \equiv 3 \pmod 4$. $1+3 \equiv 0 \pmod 4$.
$y^n+x$. WLOG $x \equiv 1 \pmod 4$. $1+1 \equiv 2 \pmod 4$.
So $v_2(a_n)=1$.
If $n$ is odd. $x^n+y \equiv x+y = 2^k \equiv 0 \pmod 4$. $y^n+x \equiv y+x \equiv 0 \pmod 4$.
So $v_2(a_n) \ge 2$.
Since the 2-adic valuation of $a_n$ oscillates, the sequence does not converge.

Case 2.2.2: $\g

[Note: response truncated to first 3000 characters of 6629]
