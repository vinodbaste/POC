# artifact_140

Grading ID: GB-0661  
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
We are looking for pairs of positive integers $(x,y)$ such that the limit of the sequence $(a_n)$ exists. Since $(a_n)$ is a sequence of positive integers, the limit exists (and is finite) if and only if the sequence is eventually constant.

We analyze the expression for $a_n$ by considering two cases: $x=y$ and $x \ne y$.

Case 1: $x=y$.
If $x=y$, then $y-x=0$. The second term in the gcd is 0.
$a_n = \gcd(x^n+y, 0) = \gcd(x^n+x, 0) = x^n+x$.
For the sequence to be eventually constant, $a_{n+1}=a_n$ for large $n$.
$x^{n+1}+x = x^n+x$, which means $x^{n+1}=x^n$. Since $x$ is a positive integer, $x^n(x-1)=0$. This implies $x=1$.
If $x=1$, then $y=1$. $a_n = 1^n+1 = 2$. The sequence is constant (2, 2, 2, ...), so the limit exists and is 2.
Thus, $(1,1)$ is a solution.
If $x>1$, $a_n = x^n+x$ is strictly increasing and tends to infinity. The limit does not exist as a finite value.

Case 2: $x \ne y$.
We use the identity $\sum_{i=0}^{n-1} y^i x^{n-i-1} = \frac{y^n-x^n}{y-x}$.
The second term in the gcd is:
$$
B_n = (y-x)\left(\frac{y^n-x^n}{y-x} - 1\right) = (y^n-x^n) - (y-x) = y^n-x^n-y+x.
$$
Let $A_n = x^n+y$. Then $a_n = \gcd(A_n, B_n)$.
We use the property $\gcd(A, B) = \gcd(A, A+B)$.
$A_n+B_n = (x^n+y) + (y^n-x^n-y+x) = y^n+x$.
So, $a_n = \gcd(x^n+y, y^n+x)$.
Due to the symmetry of this expression, we can assume without loss of generality that $y>x \ge 1$.

Case 2.1: $x=1$. $y>1$.
$a_n = \gcd(1^n+y, y^n+1) = \gcd(y+1, y^n+1)$.
We examine $y^n+1$ modulo $y+1$. Since $y \equiv -1 \pmod{y+1}$, we have $y^n+1 \equiv (-1)^n+1 \pmod{y+1}$.

If $n$ is odd, $y^n+1 \equiv -1+1 = 0 \pmod{y+1}$. Thus $a_n = y+1$.
If $n$ is even, $y^n+1 \equiv 1+1 = 2 \pmod{y+1}$. Thus $a_n = \gcd(y+1, 2)$.

For the sequence to be eventually constant, the values for odd and even $n$ must be equal.
$y+1 = \gcd(y+1, 2)$.
This means $y+1$ must divide 2. Since $y>1$, $y+1>2$. This is impossible.
So the limit does not exist in this case.

Case 2.2: $y>x>1$.
Suppose the limit exists, so $a_n = L$ for $n \ge N$.

Case 2.2.1: $\gcd(x,y)=1$.
If $p$ is a prime dividing $L$. $p|x^n+y$. If $p|x$, then $p|y$, which contradicts $\gcd(x,y)=1$. Thus $\gcd(L, x)=1$ and $\gcd(L, y)=1$.
$L$ divides $x^n+y$ and $x^{n+1}+y$ for $n \ge N$. So $L$ divides their difference $x^n(x-1)$. Since $\gcd(L, x)=1$, $L|(x-1)$.
Similarly, $L|(y-1)$.
Thus $x \equiv 1 \pmod L$ and $y \equiv 1 \pmod L$.
Then $x^n+y \equiv 1^n+1 = 2 \pmod L$. Since $L|(x^n+y)$, we must have $L|2$. So $L \in \{1, 2\}$.

If $x+y$ has an odd prime factor $p$. $y \equiv -x \pmod p$. $p \nmid x$.
$a_n = \gcd(x^n+y, y^n+x)$.
If $n$ is odd, $x^n+y \equiv x^n-x = x(x^{n-1}-1) \pmod p$.
$y^n+x \equiv (-x)^n+x = -x^n+x = -x(x^{n-1}-1) \pmod p$.
Let $k$ be the order of $x$ modulo $p$. If we choose $n$ such that $n$ is odd and $n-1$ is a multiple of $k$ (e.g., $n=mk+1$ if $k$ is even, or $n=2mk+1$ i

[Note: response truncated to first 3000 characters of 6608]
