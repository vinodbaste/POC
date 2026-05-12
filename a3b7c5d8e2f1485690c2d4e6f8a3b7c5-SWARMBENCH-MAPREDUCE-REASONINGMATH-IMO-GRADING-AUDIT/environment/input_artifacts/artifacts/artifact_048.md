# artifact_048

Grading ID: GB-0854  
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

Outcome 1: COMPLETE PROOF

We are given a polynomial $P(x)$ of degree $n$ with real coefficients, a nonzero constant term ($P(0) \neq 0$), and no repeated roots. We are given integers $1 \le k < n$. The hypothesis (H) is: if a polynomial $A(x) = a_k x^k + \dots + a_0$ divides $P(x)$, then $a_0 a_1 \dots a_k = 0$. We must prove that $P(x)$ has a non-real root.

We proceed by contradiction. Assume all $n$ roots of $P(x)$ are real. Let $R$ be the set of roots. By the given conditions, $R$ consists of $n$ distinct, non-zero real numbers.

**Case 1: $k=1$.**
Since $n > k=1$, $P(x)$ has at least one root $r \in R$. Since $P(0) \neq 0$, $r \neq 0$.
Consider the polynomial $A(x) = x-r$. $A(x)$ divides $P(x)$ and has degree $k=1$. The coefficients are $a_1=1$ and $a_0=-r$.
Hypothesis (H) requires $a_1 a_0 = 0$. However, $a_1 a_0 = 1 \cdot (-r) = -r$. Since $r \neq 0$, $a_1 a_0 \neq 0$. This contradicts (H).

**Case 2: $k \ge 2$.**

**Step 1: Interpreting the Hypothesis.**
Let $S \subset R$ be any subset of $k$ distinct roots. The polynomial $Q_S(x) = \prod_{s \in S} (x-s)$ is a monic divisor of $P(x)$ of degree $k$. Let $Q_S(x) = c_k x^k + \dots + c_1 x + c_0$.
We have $c_k=1$. Since $0 \notin R$, $c_0 = Q_S(0) \neq 0$.
By (H), $c_0 c_1 \dots c_k = 0$. Since $c_0 \neq 0$ and $c_k \neq 0$, there must exist $j \in \{1, \dots, k-1\}$ such that $c_j = 0$.

By Vieta's formulas, $c_j = (-1)^{k-j} e_{k-j}(S)$, where $e_m(S)$ denotes the $m$-th elementary symmetric polynomial of $S$. Let $m=k-j$. Since $j \in \{1, \dots, k-1\}$, $m \in M = \{1, \dots, k-1\}$.

The assumption that all roots are real implies the following property:
(H'): For any $k$-subset $S \subset R$, there exists $m \in M$ such that $e_m(S)=0$.

**Step 2: A Key Lemma.**

**Lemma:** Let $T$ be a set of $d \ge 1$ distinct real numbers. It is impossible to have $e_{m-1}(T)=0$ and $e_m(T)=0$ simultaneously for any $m \in \{1, \dots, d\}$.

*Proof of Lemma:*
If $m=1$, $e_{m-1}(T) = e_0(T) = 1 \neq 0$.

If $m \ge 2$ (requiring $d \ge 2$). Let $Q_T(x) = \prod_{t \in T}(x-t) = \sum_{i=0}^d q_i x^i$. $Q_T(x)$ has $d$ distinct real roots.
Let $j=d-m$. Since $2 \le m \le d$, $0 \le j \le d-2$.
$e_m(T)=0$ implies $q_j=0$, and $e_{m-1}(T)=0$ implies $q_{j+1}=0$.

Let $H(x) = Q_T^{(j)}(x)$, the $j$-th derivative of $Q_T(x)$. Since $Q_T(x)$ has $d$ distinct real roots, by repeated application of Rolle's Theorem, $H(x)$ has $d-j=m$ distinct real roots.
We have $H(0) = j! q_j$ and $H'(0) = (j+1)! q_{j+1}$.
If $q_j=0$ and $q_{j+1}=0$, then $H(0)=0$ and $H'(0)=0$. This means $x=0$ is a root of $H(x)$ with multiplicity at least 2. This contradicts the fact that $H(x)$ has distinct roots.

**Step 3: Analyzing $k+1$ roots.**
Since $n>k$, we choose a subset $R' \subset R$ of $k+1$ distinct roots, $R' = \{r_1, \dots, r_{k+1}\}$.
Let $S_i = R' \setminus \{r_i\}$ for $i=1, \dots, k+1$. These are $k+1$ subsets of size $k$.

We claim that for a fixed $m \in M=\{1, \dots, k-1\}$, $e_m(S_i)=0$ holds for at most one index $i

[Note: response truncated to first 3000 characters of 4608]
