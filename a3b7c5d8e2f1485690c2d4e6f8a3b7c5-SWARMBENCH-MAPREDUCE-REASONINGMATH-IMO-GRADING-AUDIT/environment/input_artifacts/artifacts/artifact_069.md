# artifact_069

Grading ID: GB-0376  
Problem ID: PB-Advanced-012  
Source: Novel Problem  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $p$ be a prime number and $a, b$ be positive integers such that

 \[
 p^{n}=a^{4}+b^{4}
 \]

 for some integer $n \geq 2$. Prove that $n \geq 5$.

## Reference Solution (for grader's calibration)

First, let's summarize the facts that are frequently used in Diophantine equations. We will omit the proofs of well-known facts. The following lemma characterizes Pythagorean triples and is used repeatedly.

 <Lemma 1> If $a, b, c$ are positive integers with $ab \neq 0$ satisfying $a^{2}+b^{2}=c^{2}$, then there exist positive integers $m \neq n$ and $k$ such that

 \[
 (a, b, c)=k\left(2 m n, m^{2}-n^{2}, m^{2}+n^{2}\right) \text { or } k\left(m^{2}-n^{2}, 2 m n, m^{2}+n^{2}\right).
 \]

 In particular, if $a, b$ are relatively prime, then $k=1$ and $m$ and $n$ have different parity, and one of $a, b$ is odd and the other is even. The odd one is expressed as $m^{2}-n^{2}$ and the even one is expressed as $2mn$. Also, in this case, $c$ is always odd.
 <Proof of Lemma 1> Omitted. \qed
 <Lemma 2> If $p$ is a prime number or 1, and positive integers $x$ and relatively prime positive integers $a, b$ satisfy

 \[
 p a b=x^{2},
 \]

 then there exist positive integers $u, v$ such that $(a, b, x)=\left(p u^{2}, v^{2}, p u v\right)$ or $\left(u^{2}, p v^{2}, p u v\right)$.
 <Proof of Lemma 2> Omitted. \qed

 <Lemma 3> If $a^{2}+b^{2}$ is a multiple of 4 for integers $a, b$, then both $a$ and $b$ are even.

 <Proof of Lemma 3> $a$ and $b$ must have the same parity, but the square of an odd number has a remainder of 1 when divided by 4, so if $a, b$ have the same parity as odd numbers, then $a^{2}+b^{2}$ has a remainder of 2 when divided by 4, so it cannot be a multiple of 4. \qed

 Now, let's proceed with the proof of the main problem using these facts.
 <Step 1> There are no positive integers $x, y, z$ satisfying $x^{4}+y^{4}=z^{2}$. Therefore, $n$ is odd.

 <Step 1.1> Using proof by contradiction, assume that there exists a positive integer solution $x, y, z$. Among these solutions, choose the solution $(x, y, z)$ with the smallest $z$. If there is a prime number $q$ that divides two of $x, y, z$, then it must also divide the remaining number, and in this case, $\left(\frac{x}{q}, \frac{y}{q}, \frac{z}{q^{2}}\right)$ becomes a solution, contradicting the minimality of $z$. Therefore, this solution is pairwise relatively prime.

 <Step 1.2> Since $\left(x^{2}, y^{2}, z\right)$ is a Pythagorean triple, by <Lemma 1>, there exist relatively prime positive integers $u, v$ with different parity such that


 \begin{equation*}
 x^{2}=u^{2}-v^{2}, y^{2}=2 u v, z=u^{2}+v^{2} \tag{1.1}
 \end{equation*}


 We can assume that $u > v$ without loss of generality. Since $y^{2}=2 u v$ and $u, v$ are relatively prime, by <Lemma 2>, there exist positive integers $s, t$ such that $u=2 s^{2}, v=t^{2}$ or $u=s^{2}, v=2 t^{2}$.

 (Case 1) $u=2 s^{2}, v=t^{2}$

 $x^{2}+t^{4}=4 s^{4}$. By <Lemma 3>, both $x$ and $t$ must be even, but from $x^{2}=u^{2}-v^{2}$, $x$ is odd, which is a contradiction.

 (Case 2) $u=s^{2}, v=2 t^{2}$

 $x^{2}+4 t^{4}=s^{4}$ and since $t|v, v| y^{2}$,

 \[
 \operatorname{gcd}(x, t)|\operatorname{gcd}(x, v)| \operatorname{gcd}\left(x, y^{2}\right)=1.
 \]

 Therefore, $x$ and $t^{2}$ are also relatively prime, and by <Lemma 1>, there exist relatively prime positive integers $q, r$ with different parity (since $x$ is odd by (1.1)) such that

 \[
 x=q^{2}-r^{2}, 2 t^{2}=2 q r, s^{2}=q^{2}+r^{2}.
 \]

 Since $t^{2}=q r$, by <Lemma 2>, there exist positive integers $x', y'$ such that $q=x^{\prime 2}, r=y^{\prime 2}$, and thus by the above equation, $x^{\prime 4}+y^{\prime 4}=s^{2}$. Since

 \[
 s=\sqrt{u} \leq u<u^{2}+v^{2}=z,
 \]

 this contradicts the minimality of $(x, y, z)$. Therefore, the proof is complete.

 <Step 2> If $p^{3}=a^{4}+b^{4}$, then there exist positive integers $x, y, z$ such that $x^{2}+3 y^{4}=z^{4}$.

 <Step 2.1> If $p \mid a$, then clearly $p \mid b$ must also hold, and vice versa. Therefore, $a, b$ are either both multiples of $p$ or not. However, if the former is the case, the right-hand side becomes a multiple of $p^{4}$, which is a contradiction, so $p$ is relatively prime to both $a$ and $b$.

 <Step 2.2> Therefore, $p$ is a divisor of the sum of squares, and since $(p, a)=(p, b)=1$, $p$ is a prime number of the form $4 k+1$, so it can be expressed in the form $p=c^{2}+d^{2}$. By Jacobi's theorem, there are only two ways (considering order) to express $p^{3}$ as the sum of perfect squares:

 \[
 (p c)^{2}+(p d)^{2} \text { and } \left(c\left(c^{2}-3 d^{2}\right)\right)^{2}+\left(d\left(3 c^{2}-d^{2}\right)\right)^{2}.
 \]

 By (1), the first case cannot be expressed as $a^{4}+b^{4}$, so

 \[
 a^{2}=\left|c\left(c^{2}-3 d^{2}\right)\right|, \quad b^{2}=\left|d\left(3 c^{2}-d^{2}\right)\right|
 \]

 (or vice versa, but we can ignore this case due to symmetry) must hold. Letting $C=|c|, D=|d|$, we have


 \begin{equation*}
 a^{2} b^{2}=C D \times\left|C^{2}-3 D^{2}\right| \times\left|3 C^{2}-D^{2}\right| \tag{1.2}
 \end{equation*}


 and $\operatorname{gcd}(C, D)=1$. Now, we divide into cases depending on whether $C D$ is a multiple of 3.

 (Case 1) If $3 \mid C D$

 Without loss of generality, assume $3 \mid C$. Then, from

 \[
 \left(\frac{a b}{3}\right)^{2}=\frac{C}{3} \cdot D \cdot\left|3\left(\frac{C}{3}\right)^{2}-D^{2}\right| \cdot\left|3 C^{2}-D^{2}\right|,
 \]

 since the four terms are pairwise relatively prime, there exist positive integers $e, f, g, h$ such that

 \[
 C=3 e^{2}, \quad D=f^{2},\left|3 e^{4}-f^{4}\right|=g^{2},\left|27 e^{4}-f^{4}\right|=h^{2}.
 \]

 Then, by $\bmod 3$, we have $g^{2}+3 e^{4}=f^{4}$.

 (Case 2) If $3 \nmid CD$

 From (1.2), since the four terms are pairwise relatively prime, there exist positive integers $e, f, g, h$ such that

 \[
 C=e^{2}, \quad D=f^{2},\left|e^{4}-3 f^{4}\right|=g^{2},\left|3 e^{4}-f^{4}\right|=h^{2}.
 \]

 Similarly, by $\bmod 3$, we have $e^{4}-3 f^{4}=g^{2}$.

 Therefore, in both cases, there exists a positive integer solution to $x^{2}+3 y^{4}=z^{4}$.

 <Step 3> There are no positive integers $x, y, z$ satisfying $x^{2}+3 y^{4}=z^{4}$.

 Using proof by contradiction, assume that there exists a positive integer solution $x, y, z$. Among these solutions, choose the solution $(x, y, z)$ with the smallest $z$. If there is a prime number $q$ that divides two of $x, y, z$, then it must also divide the remaining number, and in this case, $\left(\frac{x}{q^{2}}, \frac{y}{q}, \frac{z}{q}\right)$ becomes a solution, contradicting the minimality of $z$. Therefore, this solution is pairwise relatively prime.

 Now, rewriting the equation as


 \begin{equation*}
 3 y^{4}=\left(z^{2}-x\right)\left(z^{2}+x\right) \tag{1.3}
 \end{equation*}


 we can divide into two cases since $\operatorname{gcd}\left(z^{2}-x, z^{2}+x\right)=1$ or 2.

 (Case 1) If $x$ and $z$ have the same parity

 By <Lemma 2>, there exist relatively prime positive integers $u, v$ such that

 \[
 z^{2}-x=2 u^{2}, z^{2}+x=6 v^{2}, y^{2}=2 u v \quad \text { or } \quad z^{2}+x=2 u^{2}, z^{2}-x=6 v^{2}, y^{2}=2 u v.
 \]

 In both cases, we have


 \begin{equation*}
 z^{2}=u^{2}+3 v^{2}, y^{2}=2 u v. \tag{1.4}
 \end{equation*}


 Since $y$ is even, one of $u, v$ must be even.

 <Step 3.1> If $u$ is even, then $v$ is odd, and then $z^{2}=u^{2}+3 v^{2} \equiv 3(\bmod 4)$, which is a contradiction.

 <Step 3.2> If $v$ is even, then by <Lemma 2>, there exist positive integers $s, t$ such that

 \[
 u=s^{2}, v=2 t^{2},
 \]

 and substituting this back into (1.4) gives $s^{4}+12 t^{4}=z^{2}$. Since both $s$ and $z$ are odd, this equation can be written as

 \[
 \frac{z+s^{2}}{2} \cdot \frac{z-s^{2}}{2}=3 t^{4},
 \]

 and since $\operatorname{gcd}\left(\frac{z+s^{2}}{2}, \frac{z-s^{2}}{2}\right)=1$, by <Lemma 2>, there exist relatively prime positive integers $q, r$ such that

 \[
 \frac{z+s^{2}}{2}=q^{4}, \frac{z-s^{2}}{2}=3 r^{4} \quad \text { or } \quad \frac{z+s^{2}}{2}=3 r^{4}, \frac{z-s^{2}}{2}=q^{4}.
 \]

 In the second case, we have $s^{2}=3 r^{4}-q^{4}$, but since $q$ and $s$ cannot both be multiples of 3 (in this case, $r$ would also be a multiple of 3, leading to a contradiction), $s^{2}+q^{4}$ cannot be a multiple of 3, which is a contradiction. In the remaining case, we have $s^{2}=q^{4}-3 r^{4}$, but since $q \leq q^{4} = \frac{z+s^2}{2} < z$, this contradicts the minimality of $z$.

 (Case 2) If $x$ and $z$ have different parity

 In this case, by (1.3) and <Lemma 2>, there exist relatively prime positive integers $u, v$ such that

 \[
 z^{2}+x=u^{4}, z^{2}-x=3 v^{4}, y^{2}=u v \quad \text { or } \quad z^{2}-x=3 v^{4}, z^{2}+x=u^{4}, y^{2}=u v.
 \]

 In both cases, we have $2 z^{2}=u^{4}+3 v^{4}$, but since $z$ and $u$ cannot both be multiples of 3, this leads to a contradiction modulo 3.

 Therefore, by <Step 1>, $n \neq 2,4$, and by <Step 2>, $n \neq 3$, so the proof is complete.

## Grading Guidelines

(Partial)
 1. Observed and verified that $x^2=y^4+z^4$ has no nontrivial solution
 2. Transformed the equation $p^3=a^4+b^4$ into $p=c^2+d^2, a^2=c(c^2-3d^2), b^2=d(3c^2-d^2)$
(Almost)
 1. Transformed the given equation to $x^2+3y^4=z^4$ or its equivalent form, but failed to prove that it has no nontrivial solution

## Candidate Response (to be graded)

We are given the equation $p^n = a^4+b^4$, where $p$ is a prime number, $a, b$ are positive integers, and $n \geq 2$. We want to prove that $n \geq 5$.

Let $d = \gcd(a, b)$. Since $d^4$ divides $a^4+b^4=p^n$, $d$ must be a power of $p$. Let $d=p^k$ for some integer $k \geq 0$. We can write $a=p^k A$ and $b=p^k B$, where $\gcd(A, B)=1$.
The equation becomes $p^n = p^{4k}(A^4+B^4)$. Let $N=n-4k$. Then $p^N = A^4+B^4$.
Since $A, B \geq 1$, $A^4+B^4 \geq 1^4+1^4=2$. Thus $p^N \geq 2$, which implies $N \geq 1$.

We analyze the equation $p^N = A^4+B^4$ with $\gcd(A,B)=1$.

Case 1: $p=2$.
Since $2^N=A^4+B^4 \geq 2$, $N \geq 1$. Since $\gcd(A,B)=1$, $A$ and $B$ cannot both be even. If one is even and the other is odd, $A^4+B^4$ is odd. Since $2^N$ is odd only if $N=0$, which contradicts $N \geq 1$, this is impossible. Thus, $A$ and $B$ must both be odd.
If $x$ is odd, $x^4 \equiv 1 \pmod{16}$.
Then $A^4+B^4 \equiv 1+1 = 2 \pmod{16}$.
So $2^N = 2$. This implies $N=1$.
$A^4+B^4=2$. Since $A, B \geq 1$, we must have $A=1, B=1$. This is consistent with $\gcd(A,B)=1$.
Then $n=4k+N=4k+1$. We are given $n \geq 2$.
$4k+1 \geq 2$ implies $4k \geq 1$, so $k \geq 1/4$. Since $k$ is an integer, $k \geq 1$.
Therefore, $n \geq 4(1)+1 = 5$.

Case 2: $p$ is an odd prime.
Since $p^N=A^4+B^4$ is odd, $A$ and $B$ must have opposite parity.

We examine the possible values for $N \geq 1$.

Case 2.1: $N=1$.
$p=A^4+B^4$. Then $n=4k+1$.
Since $n \geq 2$, we have $4k+1 \geq 2$, which implies $k \geq 1$.
Therefore, $n \geq 4(1)+1 = 5$.

Case 2.2: $N=2$.
$p^2=A^4+B^4$. This is the equation $Z^2=X^4+Y^4$. It is a well-known result by Fermat that this equation has no solutions in positive integers. Thus, $N=2$ is impossible.

Case 2.3: $N=4$.
$p^4=A^4+B^4$. This is the equation $Z^4=X^4+Y^4$. This is Fermat's Last Theorem for exponent 4, which has no solutions in positive integers. Thus, $N=4$ is impossible.

Case 2.4: $N=3$.
$p^3=A^4+B^4$. We analyze this equation in the ring of Gaussian integers $\mathbb{Z}[i]$.
$p^3 = (A^2+iB^2)(A^2-iB^2)$.
Since $p$ is odd and $\gcd(A,B)=1$, the factors $A^2+iB^2$ and $A^2-iB^2$ are coprime in $\mathbb{Z}[i]$. (Their greatest common divisor must divide $2A^2$ and $2iB^2$, so it divides 2. But the norm $A^4+B^4=p^3$ is odd, so the factors are coprime to 2.)
Since their product is a cube and $\mathbb{Z}[i]$ is a UFD, each factor must be a unit times a cube. Since all units in $\mathbb{Z}[i]$ are cubes ($1=1^3, -1=(-1)^3, i=(-i)^3, -i=i^3$), we can write:
$A^2+iB^2 = (x+iy)^3$ for some integers $x, y$.
$A^2 = x(x^2-3y^2)$ and $B^2 = y(3x^2-y^2)$.
Since $A^2>0, B^2>0$, the factors must have the same sign. If $x, y$ have opposite signs, say $x>0, y<0$. Let $Y=-y>0$. $A^2=x(x^2-3Y^2)$ and $B^2=-Y(3x^2-Y^2)=Y(Y^2-3x^2)$. This requires $x^2>3Y^2$ and $Y^2>3x^2$, which is impossible.
So $x, y$ have the same sign. WLOG, assume $x>0, y>0$. We must have $x^2>3y^2$.
Also, $\gcd(x,y)=1$ because any common divisor would divide $A^2$ and $B^2$, contradicting $

[Note: response truncated to first 3000 characters of 6294]
