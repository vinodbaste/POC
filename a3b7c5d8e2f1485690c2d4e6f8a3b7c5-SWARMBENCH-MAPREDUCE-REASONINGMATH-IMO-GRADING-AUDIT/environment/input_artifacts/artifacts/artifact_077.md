# artifact_077

Grading ID: GB-0675  
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

To find all pairs of positive integers $(x,y)$ for which the limit of the sequence $(a_n)$ exists, we first simplify the definition of $a_n$.
The sequence is defined as
$$ a_n = \gcd \left( x^n +y , \, (y-x)\left(\sum_{i=0}^{n-1} y^i x^{n-i-1} - 1\right) \right). $$
Let $S_n = \sum_{i=0}^{n-1} y^i x^{n-i-1}$.

**Case 1: $x=y$**
If $x=y$, the sum becomes $S_n = \sum_{i=0}^{n-1} x^i x^{n-i-1} = \sum_{i=0}^{n-1} x^{n-1} = nx^{n-1}$.
The second argument of the gcd is $(x-x)(nx^{n-1}-1) = 0$.
For any integer $A \ne 0$, $\gcd(A,0) = |A|$. Since $x,y$ are positive, $x^n+y=x^n+x$ is positive.
So, for $x=y$, we have $a_n = x^n+x$.
For the sequence of integers $(a_n)$ to have a finite limit, it must be eventually constant.
- If $x=1$, $a_n = 1^n+1 = 2$ for all $n \ge 1$. This is a constant sequence, so its limit exists and is 2. Thus, $(1,1)$ is a solution.
- If $x>1$, $a_{n+1} = x^{n+1}+x > x^n+x = a_n$, so the sequence is strictly increasing. It diverges to infinity, so the limit does not exist.

Therefore, for $x=y$, the only solution is $(1,1)$.

**Case 2: $x \ne y$**
The sum is a geometric series: $S_n = x^{n-1} \sum_{i=0}^{n-1} (y/x)^i = x^{n-1} \frac{(y/x)^n-1}{y/x-1} = \frac{y^n-x^n}{y-x}$.
The second argument of the gcd is $(y-x)(S_n-1) = (y-x)\left(\frac{y^n-x^n}{y-x} - 1\right) = y^n-x^n-(y-x)$.
So, $a_n = \gcd(x^n+y, y^n-x^n-y+x)$.
Using the property $\gcd(A,B) = \gcd(A, B+A)$, we simplify $a_n$:
$a_n = \gcd(x^n+y, (y^n-x^n-y+x) + (x^n+y)) = \gcd(x^n+y, y^n+x)$.

Since $x,y$ are positive integers, $a_n$ is a sequence of positive integers. For its limit to exist, the sequence must be eventually constant. That is, there exist an integer $L$ and a natural number $N$ such that $a_n = L$ for all $n \ge N$.

**Subcase 2.1: One of $x$ or $y$ is 1.**
Without loss of generality, let $x=1$. Since $x \ne y$, we have $y>1$.
$a_n = \gcd(1^n+y, y^n+1) = \gcd(y+1, y^n+1)$.
We analyze $y^n+1$ modulo $y+1$. Since $y \equiv -1 \pmod{y+1}$, we have $y^n+1 \equiv (-1)^n+1 \pmod{y+1}$.
- If $n$ is odd, $y^n+1 \equiv (-1)+1 = 0 \pmod{y+1}$. So $y+1$ divides $y^n+1$. In this case, $a_n = \gcd(y+1, y^n+1) = y+1$.
- If $n$ is even, $y^n+1 \equiv (-1)^2+1 = 2 \pmod{y+1}$. So $a_n = \gcd(y+1, y^n+1) = \gcd(y+1, 2)$.

The sequence $(a_n)$ for $n \ge 1$ alternates between $y+1$ (for odd $n$) and $\gcd(y+1,2)$ (for even $n$). For the sequence to converge, these values must be equal:
$y+1 = \gcd(y+1,2)$.
Since $y$ is a positive integer and $y>1$, we have $y+1 > 2$.
However, $\gcd(y+1,2)$ can only be 1 or 2.
The equality $y+1 = \gcd(y+1,2)$ can never hold for $y>1$.
Therefore, no solutions exist when one of the variables is 1 and the other is not.

**Subcase 2.2: $x,y > 1$ and $x \ne y$.**
Let $d = \gcd(x,y)$. We write $x=dx'$ and $y=dy'$ for some coprime positive integers $x',y'$.
$a_n = \gcd((dx')^n+dy', (dy')^n+dx') = d \cdot \gcd(d^{n-1}x'^n+y', d^{n-1}y'^n+x')$.
Let $D_n = \gcd(d^{n-1}x'^n+y', d^{n-1}y'^n+x')$. The sequence $(a_n)$ is eventually constant if and only if $

[Note: response truncated to first 3000 characters of 9768]
