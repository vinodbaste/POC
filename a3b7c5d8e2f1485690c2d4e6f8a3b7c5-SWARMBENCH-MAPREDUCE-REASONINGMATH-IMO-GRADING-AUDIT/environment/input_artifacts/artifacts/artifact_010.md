# artifact_010

Grading ID: GB-0867  
Problem ID: PB-Advanced-026  
Source: USAMO 2025  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $n$ and $k$ be positive integers with $k<n$. Let $P(x)$ be
 a polynomial of degree $n$ with real coefficients, nonzero constant
 term, and no repeated roots. Suppose that for any real numbers $a_{0},a_{1},\dots,a_{k}$
 such that the polynomial $a_{k}x^{k}+\dots+a_{1}x+a_{0}$ divides
 $P(x)$, the product $a_{0}a_{1}\dots a_{k}$ is zero. Prove that
 $P(x)$ has a non-real root.

## Reference Solution (for grader's calibration)

Let $n>k\geq1$ be integers. Let $P(x)\in\mathbb{R}[x]$ be a polynomial
 of degree $n$ with no repeated roots and $P(0)\neq0$. Suppose that
 for any real numbers $a_{0},\ldots,a_{k}$ such that the polynomial
 $a_{k}x^{k}+\cdots+a_{1}x+a_{0}$ divides $P(x)$, the product $a_{0}a_{1}\ldots a_{k}$
 is zero. Prove that $P(x)$ has a non-real root.


 By considering any $k+1$ of the roots of $P$, we may as well assume
 WLOG that $n=k+1$. Suppose that $P(x)=\left(x+r_{1}\right)\ldots\left(x+r_{n}\right)\in\mathbb{R}[x]$
 has $P(0)\neq0$. Then the problem hypothesis is that each of the
 $n$ polynomials (of degree $n-1$ ) given by

 \[
 \begin{aligned}P_{1}(x) & =\left(x+r_{2}\right)\left(x+r_{3}\right)\left(x+r_{4}\right)\ldots\left(x+r_{n}\right)

 P_{2}(x) & =\left(x+r_{1}\right)\left(x+r_{3}\right)\left(x+r_{4}\right)\ldots\left(x+r_{n}\right)

 P_{3}(x) & =\left(x+r_{1}\right)\left(x+r_{2}\right)\left(x+r_{4}\right)\ldots\left(x+r_{n}\right)

  & \vdots

 P_{n}(x) & =\left(x+r_{1}\right)\left(x+r_{2}\right)\left(x+r_{3}\right)\ldots\left(x+r_{n-1}\right)
 \end{aligned}
 \]

 has at least one coefficient equal to zero. (Explicitly, $P_{i}(x)=\frac{P(x)}{x+r_{i}}$.)
 We'll prove that at least one $r_{i}$ is not real.


 Obviously the leading and constant coefficients of each $P_{i}$ are
 nonzero, and there are $n-2$ other coefficients to choose between.
 So by pigeonhole principle, we may assume, say, that $P_{1}$ and
 $P_{2}$ share the position of a zero coefficient, say the $x^{k}$
 one, for some $1\leq k<n-1$.


 \textbf{Claim 1. }If $P_{1}$ and $P_{2}$ both have $x^{k}$ coefficient
 equal to zero, then the polynomial

 \[
 Q(x)=\left(x+r_{3}\right)\left(x+r_{4}\right)\ldots\left(x+r_{n}\right)
 \]

 has two consecutive zero coefficients.


 \emph{Proof.} Suppose that

 \[
 Q(x)=x^{n-2}+b_{n-3}x^{n-3}+\cdots+b_{0}.
 \]

 (And let $b_{n-2}=1$. ) Then the fact that the $x^{k}$ coefficient
 of $P_{1}$ and $P_{2}$ are both zero means

 \[
 r_{1}b_{k}+b_{k-1}=r_{2}b_{k}+b_{k-1}=0
 \]

 and hence that $b_{k}=b_{k-1}=0$ (since the $r_{i}$ are distinct).



  To solve the problem, it suffices to prove:


 \textbf{Claim 2.} If $F(x)\in\mathbb{R}[x]$ is a polynomial with
 two consecutive zero coefficients, it cannot have all distinct real
 roots.


 \emph{Proof. }Say $x^{t}$ and $x^{t+1}$ coefficients of $F$ are
 both zero. Assume for contradiction all the roots of $F$ are real
 and distinct. Then by Rolle's theorem, every higher-order derivative
 of $F$ should have this property too. However, the $t$th order derivative
 of $F$ has a double root of $0$, contradiction.

## Grading Guidelines

(Partial)
 1. (WLOG assumed $n=k+1$ and) proved that two different divisors of $P$ share the position of a zero coefficient.
 2. Found a polynomial with only distinct real roots and has two consecutive zero coefficients.
(Almost)
 1. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

Let $P(x)$ be a polynomial of degree $n$ with real coefficients, a nonzero constant term $P(0)$, and no repeated roots. Let $k$ be a positive integer with $k<n$. Let the roots of $P(x)$ be $r_1, \dots, r_n$. The roots are distinct, and since $P(0) \ne 0$, none of them are zero. As $P(x)$ has real coefficients, its non-real roots come in conjugate pairs.

The given condition is that for any polynomial $Q(x) = a_k x^k + \dots + a_1 x + a_0$ with real coefficients that divides $P(x)$, the product of its coefficients $a_0 a_1 \dots a_k$ is zero.

First, we analyze the condition on the coefficients.
Let $Q(x)$ be a real polynomial that divides $P(x)$.
If the degree of $Q(x)$ is $m < k$, we can write $Q(x)$ as a polynomial of degree $k$ by setting the leading coefficients to zero, i.e., $a_k = a_{k-1} = \dots = a_{m+1} = 0$. In this case, $a_k=0$, and the product $a_0 a_1 \dots a_k$ is trivially zero. Thus, the condition imposes no constraint on divisors of degree less than $k$.

Now, let $Q(x) = a_k x^k + \dots + a_0$ be a divisor of $P(x)$ of degree exactly $k$.
Then $a_k \neq 0$.
The roots of $Q(x)$ are a subset of the roots of $P(x)$. Since $P(0) \neq 0$, zero is not a root of $P(x)$, and therefore not a root of $Q(x)$. This implies that $Q(0) = a_0 \neq 0$.
The condition $a_0 a_1 \dots a_k = 0$, combined with $a_0 \neq 0$ and $a_k \neq 0$, simplifies to $a_1 a_2 \dots a_{k-1} = 0$.
This means that for any real divisor of $P(x)$ of degree $k$, at least one of the coefficients of $x^1, x^2, \dots, x^{k-1}$ must be zero.

We will prove by contradiction that $P(x)$ must have a non-real root.
Assume that all roots of $P(x)$ are real. Let $R = \{r_1, \dots, r_n\}$ be the set of these roots. By our assumption and the problem statement, all $r_i$ are distinct, real, and non-zero numbers.

Let $S \subset R$ be any subset of $k$ roots. The polynomial $Q_S(x) = \prod_{s \in S} (x-s)$ is a monic polynomial of degree $k$. Since all roots in $S$ are real, $Q_S(x)$ has real coefficients and divides $P(x)$.
Let us write $Q_S(x) = x^k + c_{k-1}x^{k-1} + \dots + c_1x + c_0$. This corresponds to a divisor with coefficients $a_k=1, a_{k-1}=c_{k-1}, \dots, a_0=c_0$.
From our analysis of the condition, we must have $c_1 c_2 \dots c_{k-1} = 0$.
By Vieta's formulas, the coefficients are related to the elementary symmetric polynomials $e_j(S)$ of the roots in $S$:
$c_{k-j} = (-1)^j e_j(S)$ for $j=1, \dots, k$.
The condition $c_1 c_2 \dots c_{k-1} = 0$ implies that for some $j \in \{1, \dots, k-1\}$, we must have $c_j=0$. This is equivalent to $e_{k-j}(S)=0$. Letting $m = k-j$, we see that $m$ also ranges from $1$ to $k-1$.
So, the assumption that all roots of $P(x)$ are real leads to the following property:
(*) For any subset $S \subseteq R$ of size $k$, there exists an integer $m \in \{1, 2, \dots, k-1\}$ such that $e_m(S) = 0$.

We will now show that this property leads to a contradiction. We consider cases for $k$.

**Case 1: k=1**
The condition is that for any divisor

[Note: response truncated to first 3000 characters of 10480]
