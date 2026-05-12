# artifact_136

Grading ID: GB-0555  
Problem ID: PB-Advanced-017  
Source: Novel Problem  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $n$ be a positive integer that has a remainder of 6 when divided by 7. Let $d$ be any divisor of $n$.

Define $c$ such that when the expression $\left(d+\frac{n}{d}\right)^{2}$ is divided by $n$, the remainder is $n-c$.

What is the smallest possible value of $c$ among all $d$ and $n$ satisfying the conditions above?

(Note that the remainder when a positive integer $a$ is divided by a positive integer $b$ is the value of $r$ in the expression $a=b q+r, 0 \leq r \leq b-1$.)

## Reference Solution (for grader's calibration)

<Step 1> Understanding the problem situation

 <Step 1.1> Let $d=a, \frac{n}{d}=b$, then $n=a b$. So if the remainder when $(a+b)^{2}$ is divided by $n$ is $n-c$ (where $c \geq 1$), then

 \[
 -c \equiv(a+b)^{2}=a^{2}+b^{2}+2 a b \equiv a^{2}+b^{2}(\bmod n)
 \]

 which implies that $\frac{a^{2}+b^{2}+c}{a b}$ must be a positive integer.

 <Step 1.2> First, if $c=3$, then setting $a=4, b=19$ gives

 \[
 \frac{4^{2}+19^{2}+3}{4 \cdot 19}=5
 \]

 which is an integer. In fact, this corresponds to the case when $n=76, d=4$, and $\left(4+\frac{76}{4}\right)^{2}=529 \equiv -3(\bmod 76)$.

 <Step 1.3> Therefore, if $c \leq 2$, it is sufficient to prove that when $\frac{a^{2}+b^{2}+c}{a b}$ is a positive integer, $n$ cannot have remainder 6 when divided by $7$. Now, let's assume that $c$ is 1 or 2.

 <Step 2> Vieta jumping

 <Step 2.1> First, let's find the solutions when $a=b$. Then $\frac{2 a^{2}+c}{a^{2}}$ must be a positive integer, so $a^{2} \mid c$. Since $c$ is 1 or 2, we know that $a=1$. Therefore, $(a, b)=(1,1)$ is the only solution in this case. Now, let's find the solutions when $a \neq b$. By symmetry, we can assume $a<b$, so let's find all such pairs $(a, b)$.

 <Step 2.2> We need to find pairs $(a, b)$ that satisfy the following for some positive integer $k$:


 \begin{equation*}
 \frac{a^{2}+b^{2}+c}{a b}=k \tag{1.1}
 \end{equation*}


 The above equation (1.1) can be rewritten as:

 \[
 a^{2}-k a b+b^{2}+c=0
 \]

 Now, if we view this equation as a quadratic equation in $b$, we can observe the following facts from the relationship between roots and coefficients:

 (1) The sum of the two roots is $k a$, so if a positive integer $b$ is a root, then the other root is $k a-b$, which is also an integer.

 (2) The product of the two roots is $a^{2}+c$, so if a positive integer $b$ is a root, then $\frac{a^{2}+c}{b}$ is also a root, and by (1), it is a positive integer solution.

 (2) Therefore, if $(a, b)$ is a solution to (1.1), then


 \begin{equation*}
 \left(a^{\prime}, b^{\prime}\right)=\left(\frac{a^{2}+c}{b}, a\right)=(k a-b, a) \tag{1.2}
 \end{equation*}


 defined as above is also a solution to (1.1).

 This process gives us a way to find another solution if we have a solution $(a, b)$.

 <Step 3> Applying the method of infinite descent

 Suppose $(a, b)$ is a solution to (1.1) with $a<b$. Now, let's apply infinite descent to the recursive construction process of solutions described in <Step 2> .

 <Step 3.1> Since we assumed $a<b$,

 \[
 b^{2} \geq(a+1)^{2}>a^{2}+2 \geq a^{2}+c
 \]

 so $\frac{a^{2}+c}{b}<b$. In other words, from (1.2),

 \[
 a^{\prime}+b^{\prime}=\frac{a^{2}+c}{b}+a<a+b
 \]

 holds. That is, when performing the recursive construction in <Step 1>, the sum of the two numbers forming the solution always decreases by at least 1.

 <Step 3.2> If $\frac{a^{2}+c}{b}<a$, we can apply the process in <Step 1> again to the new solution $\left(a^{\prime}, b^{\prime}\right)=\left(\frac{a^{2}+c}{b}, a\right)$ to obtain another solution. However, by the result in (1) and the principle of infinite descent, this process cannot be repeated infinitely, and we will eventually reach a solution $(a, b)$ that satisfies $\frac{a^{2}+c}{b} \geq a$.

 <Step 3.3> Let's find what the final solution we must reach in (2) is. If $a<b$, then $b \geq a+1$ must hold. In this situation, if $\frac{a^{2}+c}{b} \geq a$, then

 \[
 a^{2}+c \geq a b \geq a(a+1)=a^{2}+a
 \]

 so $a \leq c$ must hold. Since $a$ is a positive integer, only $a=1,2$ are possible. Here, if $a=2$, then all equalities in the above inequality must hold, so $b=a+1=3$ and $c=2$, which gives

 \[
 \frac{a^{2}+b^{2}+c}{a b}=\frac{2^{2}+3^{2}+3}{2 \cdot 3}=\frac{8}{3}
 \]

 which is not an integer. Therefore, $a$ must be 1 in any case, and $\frac{a^{2}+c}{b}=\frac{1+c}{b}$ must be an integer.$b>a$ and $c+1=2or3$ so $b=c+1$.

 Therefore, this process ends when $(1, c+1)$ becomes $\left(\frac{1^{2}+c}{c+1}, 1\right)=(1,1)$.

 <Step 3.4> Summarizing the above discussion, if $(a, b)$ is a solution to (1.1) with $a<b$, then $\left(a^{\prime}, b^{\prime}\right)$ obtained in <Step 1> is a new solution satisfying $a^{\prime}<b^{\prime}$, and this process of generating solutions ends when the solution reaches $(1,1)$.

 <Step 4> Reversing the descent process

 <Step 4.1> First, the value of $k$ in (1.1) does not change during the process described in <Step 3> . Therefore, the value of $k$ must be the same as the value at the endpoint $(a, b)=(1,1)$ of this process, so

 \[
 k=\frac{1^{2}+1^{2}+1}{c \cdot 1}=c+2
 \]

 must hold.

 <Step 4.2> Now, we know that any solution $(a, b)$ to (1.1) with $a<b$ reaches the endpoint $(a, b)=(1,1)$ by going through the process described in <Step 3> . Therefore, by reversing this process, we can find all solutions $(a, b)$ to (1.1) with $a<b$.

 <Step 4.3> On the other hand, from (1), $k=c+2$, so looking at (1.2), we see that $\left(a^{\prime}, b^{\prime}\right)=((c+2) a-b, a)$. Therefore,

 \[
 (a, b)=\left(b^{\prime},(c+2) b^{\prime}-a^{\prime}\right)
 \]

 holds. In other words, the process of mapping $(x, y) \mapsto(y,(c+2) y-x)$ is the reverse of the process where the solution descends in <Step 2> .

 <Step 4.4> Therefore, by (3), if we define the sequence $\left(x_{n}, y_{n}\right)_{n=1}^{\infty}$ as $\left(x_{1}, y_{1}\right)=(1,1)$ and

 \begin{equation} \tag{1.3}
 \left\{\begin{array}{l}
 x_{n+1}=y_{n}

 y_{n+1}=(c+2) y_{n}-x_{n}
 \end{array}\right.
 \end{equation}

 then this sequence describes the reverse of the process where the solution descends in <Step 2>, and by (2), these $\left(x_{n}, y_{n}\right)$ with $n \geq 2$ are all solutions to (1.1) with $a<b$.

 Note that the descent process described in <Step 2> is

 \[
 \left(x_{k}, y_{k}\right) \rightarrow\left(x_{k-1}, y_{k-1}\right) \rightarrow \cdots \rightarrow\left(x_{1}, y_{1}\right)=(1,1)
 \]

 <Step 4.5>

 (Case 1) When $c=1$, substituting the first equation of (1.3) into the second equation gives the recurrence relation

 \[
 y_{n+1}=3 y_{n}-y_{n-1}
 \]

 and using $y_{1}=1, y_{2}=2$, we can see that this sequence repeats as $1,2,5,6,6,5,2,1,1,2$ modulo 7. Therefore, $x_n y_{n} = y_n y_{n-1}$ repeats as $2,3,2,1,2,3,2,1$ and thus cannot have remainder 6 when devided by $7$.

 (Case 2) When $c=2$, substituting the first equation of (1.3) into the second equation gives the recurrence relation

 \[
 y_{n+1}=4 y_{n}-y_{n-1}
 \]

 and using $y_{1}=1, y_{2}=3$, we can see that this sequence repeats as $1,3,4,6,6,4,3,1,1,3$ modulo 7. Therefore, $x_n y_{n} = y_n y_{n-1}$ repeats as $3,5,3,1,3,5,3,1$ and thus cannot have remainder 6 when divided by $7$.

 In conclusion, when $c=1,2$, there is no case where $ab$ has remainder $6$ when divided by $7$ and $\frac{a^{2}+b^{2}+c}{a b}$ is an integer. Therefore, $c=3$ is the smallest possible value.

## Grading Guidelines

(Partial)
 1. Proved $c\ge 3$.
(Almost)
 1. Applied infinite descent or equivalent strategy to prove $c=3$, but not completed.

## Candidate Response (to be graded)

Let $n$ be a positive integer such that $n \equiv 6 \pmod{7}$, and let $d$ be any divisor of $n$.
The expression given is $E = \left(d+\frac{n}{d}\right)^{2}$.
We are told that when $E$ is divided by $n$, the remainder is $n-c$.

First, let's analyze the expression $E$ modulo $n$.
$E = d^2 + 2d\left(\frac{n}{d}\right) + \left(\frac{n}{d}\right)^2 = d^2 + 2n + \left(\frac{n}{d}\right)^2$.
When we consider the remainder upon division by $n$, the term $2n$ is congruent to $0 \pmod{n}$.
So, $E \equiv d^2 + \left(\frac{n}{d}\right)^2 \pmod{n}$.

Let $S_d = d^2 + (n/d)^2$. The remainder of $E$ when divided by $n$ is the same as the remainder of $S_d$ when divided by $n$.
Let this remainder be $r$. We are given that $r = n-c$.
So, $S_d \equiv r \pmod{n}$, which becomes $d^2 + \left(\frac{n}{d}\right)^2 \equiv n-c \pmod{n}$.
This simplifies to $d^2 + \left(\frac{n}{d}\right)^2 \equiv -c \pmod{n}$.
This means that $d^2 + (n/d)^2 + c$ is a multiple of $n$.
Let $k=n/d$. Since $d$ is a divisor of $n$, $k$ is also an integer divisor. The condition can be written as:
$d^2 + k^2 + c = Qn$ for some integer $Q$.
Since $n=dk$, we have $d^2 + k^2 + c = Qdk$.

The definition of a remainder requires $0 \le r \le n-1$.
Substituting $r=n-c$, we get $0 \le n-c \le n-1$.
This implies $1 \le c \le n$. We are looking for the smallest possible value of $c$.

We are given the condition $n \equiv 6 \pmod{7}$, which is equivalent to $n \equiv -1 \pmod{7}$.
Since $n=dk$, neither $d$ nor $k$ can be a multiple of 7. Thus, $d, k \not\equiv 0 \pmod{7}$.
From $dk \equiv -1 \pmod{7}$, we have $k \equiv -d^{-1} \pmod{7}$.
Let's analyze the term $S_d = d^2+k^2$ modulo 7:
$S_d \equiv d^2 + (-d^{-1})^2 = d^2 + (d^{-1})^2 \pmod{7}$.

The possible values for $d^2 \pmod{7}$ for $d \not\equiv 0 \pmod 7$ are:
$1^2 \equiv 1, 2^2 \equiv 4, 3^2 \equiv 9 \equiv 2$.
Let $x = d^2 \pmod{7}$, so $x \in \{1, 2, 4\}$.
The inverse of $x$ is $(d^{-1})^2$.
- If $x=1$, $S_d \equiv 1 + 1^{-1} = 1+1=2 \pmod{7}$.
- If $x=2$, $S_d \equiv 2 + 2^{-1} = 2+4=6 \pmod{7}$.
- If $x=4$, $S_d \equiv 4 + 4^{-1} = 4+2=6 \pmod{7}$.
So, $S_d = d^2+k^2$ must be congruent to either 2 or 6 modulo 7.

From the equation $d^2+k^2+c = Qdk$, we take residues modulo 7:
$S_d + c \equiv Q(dk) \equiv Q(-1) \equiv -Q \pmod{7}$.

We will now test small positive integer values for $c$.

**Case 1: $c=1$**
The equation is $d^2+k^2+1 = Qdk$.
- If $S_d \equiv 2 \pmod{7}$: $2+1 \equiv -Q \pmod{7} \implies 3 \equiv -Q \implies Q \equiv 4 \pmod{7}$.
- If $S_d \equiv 6 \pmod{7}$: $6+1 \equiv -Q \pmod{7} \implies 0 \equiv -Q \implies Q \equiv 0 \pmod{7}$.

We can write the equation as a quadratic in $d$: $d^2 - (Qk)d + (k^2+1) = 0$.
For $d$ to be an integer, the discriminant $\Delta$ must be a perfect square.
$\Delta = (Qk)^2 - 4(k^2+1) = k^2(Q^2-4) - 4 = m^2$ for some integer $m \ge 0$.
For $\Delta$ to be non-negative, we must have $Q \ge 3$.
- Let's test $Q=4$, which satisfies $Q \equiv 4 \pmod 7$.
  $\Delta = k^2(4^2-4)-4 = 12k^2-4 = 4(3k^2-1)

[Note: response truncated to first 3000 characters of 6601]
