# artifact_016

Grading ID: GB-0872  
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

**Complete Proof**

We are given a polynomial $P(x)$ of degree $n$ with real coefficients, distinct roots, and a nonzero constant term ($P(0) \neq 0$). We are given integers $1 \le k < n$. The hypothesis (H) is that for any divisor $Q(x) = a_k x^k + \dots + a_0$ of $P(x)$, the product $a_0 a_1 \dots a_k$ is zero. We want to prove that $P(x)$ has a non-real root.

We proceed by contradiction. Assume all roots of $P(x)$ are real. Let $R$ be the set of these $n$ roots. Since $P(x)$ has distinct roots and $P(0) \neq 0$, $R$ consists of $n$ distinct non-zero real numbers.

**Analysis of the Hypothesis (H)**

Consider any subset $S \subset R$ of size $k$. The monic polynomial $Q_S(x) = \prod_{s \in S}(x-s)$ divides $P(x)$. Let $Q_S(x) = x^k + c_{k-1}x^{k-1} + \dots + c_0$.
Here $c_k=1$. Since $0 \notin R$, $c_0 = Q_S(0) \neq 0$.
Hypothesis (H) implies $c_0 c_1 \dots c_k = 0$. Since $c_0 \neq 0$ and $c_k \neq 0$, there must be some $j \in \{1, \dots, k-1\}$ such that $c_j=0$.

The coefficients are related to the elementary symmetric polynomials $e_m(S)$ by $c_j = (-1)^{k-j} e_{k-j}(S)$. Thus, $c_j=0$ implies $e_{k-j}(S)=0$.
The assumption that all roots are real implies that for every $k$-subset $S \subset R$, there is some $m \in \{1, \dots, k-1\}$ such that $e_m(S)=0$.

**Case k=1**

If $k=1$, then $n>1$. Since $P(x)$ has at least one root $r \in R$, $Q(x) = x-r$ is a divisor of degree 1. The coefficients are $a_1=1$ and $a_0=-r$. Hypothesis (H) requires $a_1 a_0 = -r = 0$, so $r=0$. This contradicts $P(0) \neq 0$. Thus, for $k=1$, $P(x)$ must have a non-real root.

**Case k ≥ 2**

We first prove a necessary lemma.

**Lemma:** Let $Q(x) = \sum_{i=0}^d c_i x^i$ be a polynomial of degree $d \ge 2$ with $d$ distinct non-zero real roots. Then $Q(x)$ cannot have two consecutive zero coefficients $c_i = c_{i+1} = 0$ for any $i \in \{1, \dots, d-2\}$.

*Proof of Lemma:* Suppose $c_i = c_{i+1} = 0$ for some $i \ge 1$. Consider $R(x) = Q^{(i-1)}(x)$. Since $Q(x)$ has distinct real roots, by Rolle's theorem, $R(x)$ also has distinct real roots.
Let $R(x) = b_0 + b_1 x + b_2 x^2 + \dots$. We have $b_1 \propto c_i = 0$ and $b_2 \propto c_{i+1} = 0$.
If $b_0 = 0$, then $R(0)=0$ and $R'(0)=b_1=0$. This means $x=0$ is a multiple root of $R(x)$, contradicting that $R(x)$ has distinct roots. Thus, $b_0 \neq 0$.
Since $b_0 \neq 0$, the roots of $R(x)$ are non-zero. Let $Y$ be the set of reciprocals of the roots of $R(x)$. $Y$ consists of distinct non-zero real numbers.
The elementary symmetric sums of $Y$ satisfy $e_1(Y) = -b_1/b_0 = 0$ and $e_2(Y) = b_2/b_0 = 0$.
The sum of squares of elements in $Y$ is $P_2(Y) = e_1(Y)^2 - 2e_2(Y) = 0$. Since the elements of $Y$ are real, this implies all elements are 0, a contradiction. Thus, the Lemma holds. $\square$

**Main Argument for k ≥ 2**

Since $n>k$, we choose a subset $R' \subset R$ of $k+1$ distinct non-zero real roots, $R' = \{r_1, \dots, r_{k+1}\}$.
For $i=1, \dots, k+1$, let $S_i = R' \setminus \{r_i\}$. $|S_i|=k$.
B

[Note: response truncated to first 3000 characters of 5238]
