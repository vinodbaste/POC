# artifact_102

Grading ID: GB-0659  
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

The sequence $(a_n)_{n \ge 1}$ is defined by
$$
 a_n = \gcd \left( x^n +y , \, (y-x)\left(\sum_{i=0}^{n-1} y^i x^{n-i-1} - 1\right) \right).
$$
We seek all pairs of positive integers $(x,y)$ such that the limit of $(a_n)$ exists. Since $(a_n)$ is a sequence of positive integers, the limit exists if and only if the sequence is eventually constant.

### Case 1: $x=y$

If $x=y$, the factor $y-x=0$. The second argument of the gcd is 0.
$$a_n = \gcd(x^n+y, 0) = x^n+x.$$
For $(a_n)$ to be eventually constant, we must have $a_{N+1} = a_N$ for some $N$.
$x^{N+1}+x = x^N+x \implies x^{N+1} = x^N$.
$x^N(x-1)=0$. Since $x$ is a positive integer, we must have $x=1$.
If $x=1$, then $y=1$.
For $(1,1)$, $a_n = 1^n+1 = 2$ for all $n$. The sequence is constant, so the limit exists.
Thus, $(1,1)$ is a solution.

### Case 2: $x \neq y$

We simplify the second term in the gcd. Let $B_n$ be the second term.
Using the identity $(y-x)\sum_{i=0}^{n-1} y^i x^{n-i-1} = y^n-x^n$, we have:
$B_n = (y^n-x^n) - (y-x)$.
Let $A_n = x^n+y$.
$a_n = \gcd(A_n, B_n)$. We use $\gcd(A, B) = \gcd(A, A+B)$.
$A_n+B_n = (x^n+y) + (y^n-x^n-y+x) = y^n+x$.
So, $a_n = \gcd(x^n+y, y^n+x)$.

#### Case 2.1: $\min(x,y)=1$.

WLOG, let $x=1$. Since $x \ne y$, $y>1$.
$a_n = \gcd(1^n+y, y^n+1) = \gcd(y+1, y^n+1)$.
Since $y \equiv -1 \pmod{y+1}$, $y^n+1 \equiv (-1)^n+1 \pmod{y+1}$.

If $n$ is odd, $y^n+1 \equiv 0 \pmod{y+1}$, so $a_n = y+1$.
If $n$ is even, $y^n+1 \equiv 2 \pmod{y+1}$, so $a_n = \gcd(y+1, 2)$.

For the limit to exist, $a_n$ must be eventually constant, so $y+1 = \gcd(y+1, 2)$.
This means $y+1$ divides 2. Since $y>1$, $y+1>2$. This is impossible.
The limit does not exist in this case.

#### Case 2.2: $x>1, y>1, x \neq y$.

Suppose the limit exists, $a_n \to L$.

##### Case 2.2.1: $\gcd(x,y)=1$.

We showed in the thought process that if $a_n \to L$, then $x+y \mid L$ (by considering $n_k = k\phi(x+y)+1$) and $L \mid \gcd(x-1, y-1)$.
This implies $x+y \le \gcd(x-1, y-1)$.
WLOG, assume $x<y$. $\gcd(x-1, y-1) \le x-1$.
$x+y \le x-1$, which implies $y \le -1$. This contradicts $y>1$.
The limit does not exist in this case.

##### Case 2.2.2: $\gcd(x,y)=g>1$.

Let $x=gX, y=gY$ with $\gcd(X,Y)=1$ and $X \ne Y$.
$a_n = g K_n$, where $K_n = \gcd(g^{n-1}X^n+Y, g^{n-1}Y^n+X)$.
If $a_n \to L$, then $K_n \to K=L/g$.
We established that $\gcd(K, g)=1$ and $K \in \{1, 2\}$.

We showed that in many subcases, $K_n$ does not converge to 1 or 2. For example, if $X+Y$ has an odd prime factor $p$ not dividing $g$, $p \mid K_n$ infinitely often, contradicting $K \in \{1, 2\}$.

We analyzed specific examples where the general arguments were complex.
Example 1: $(x,y)=(2, 6)$. $g=2, X=1, Y=3$. We found $K_4=11$. Since $K_n$ takes the value 11 infinitely often (for $n \equiv 4 \pmod{10}$), $K_n$ cannot converge to 1 or 2.
Example 2: $(x,y)=(3, 6)$. $g=3, X=1, Y=2$. We found $K_n$ is divisible by 19 infinitely often (for $n \equiv 17 \pmod{18}$). $K_n$ cannot converge to 1 or 2.

In all cases where $x \ne y$, the

[Note: response truncated to first 3000 characters of 3220]
