# artifact_007

Grading ID: GB-0855  
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

We are asked to prove that $P(x)$ must have a non-real root, given the conditions on $P(x)$ and its divisors. We proceed by contradiction.

**1. Setup and Assumptions**

Assume, for the sake of contradiction, that all roots of $P(x)$ are real. Let $R$ be the set of roots.
We are given that $P(x)$ has degree $n$, real coefficients, no repeated roots, and a nonzero constant term ($P(0) \neq 0$).
Therefore, $R$ consists of $n$ distinct real numbers, none of which is zero.

**2. Interpreting the Hypothesis (H)**

The hypothesis (H) states that if $Q(x) = a_{k}x^{k}+\dots+a_{1}x+a_{0}$ divides $P(x)$, then $a_{0}a_{1}\dots a_{k}=0$.

Consider a divisor $Q(x)$ of $P(x)$ of degree exactly $k$. (Since $k<n$ and $P(x)$ has $n$ distinct roots, such divisors exist.)
1. Since $\deg(Q)=k$, the leading coefficient $a_k \neq 0$.
2. Since $Q(x)$ divides $P(x)$ and $P(0) \neq 0$, $Q(0) \neq 0$. Thus, the constant term $a_0 \neq 0$.

The hypothesis (H), $a_{0}a_{1}\dots a_{k} = 0$, combined with $a_0 \neq 0$ and $a_k \neq 0$, implies that at least one intermediate coefficient must be zero:
$a_j = 0$ for some $j \in \{1, 2, \dots, k-1\}$.

**3. Case k=1**

If $k=1$, the set of intermediate indices $\{1, \dots, k-1\}$ is empty. Let's examine the hypothesis (H) directly.
Since $n>k=1$, $P(x)$ has at least one root $r \in R$. We know $r \neq 0$.
The polynomial $Q(x) = x-r$ is a divisor of $P(x)$ of degree $k=1$.
$Q(x) = a_1 x + a_0$, with $a_1=1$ and $a_0=-r$.
The hypothesis (H) requires $a_1 a_0 = 0$. But $a_1 a_0 = 1 \cdot (-r) = -r$.
Since $r \neq 0$, $a_1 a_0 \neq 0$. This contradicts (H).
Thus, for $k=1$, the assumption that all roots are real leads to a contradiction.

**4. Case k ≥ 2**

We translate the hypothesis into a condition on the roots. A divisor of degree $k$ corresponds to a subset of $k$ roots $S \subset R$. Let $Q_S(x) = \prod_{s \in S}(x-s)$ be the corresponding monic divisor. The coefficients $a_j$ of $Q_S(x)$ are related to the elementary symmetric polynomials (ESPs) $e_m(S)$ by $a_{k-m} = (-1)^m e_m(S)$.

The interpretation of (H) from Step 2 (that some $a_j=0$ for $j \in \{1, \dots, k-1\}$) means:
(H'): For any $S \subset R$ with $|S|=k$, there exists $m \in \{1, \dots, k-1\}$ such that $e_m(S)=0$.

We first establish a necessary lemma regarding ESPs of real roots.

**Lemma (Impossibility of Consecutive Vanishing ESPs):** Let $T$ be a finite set of distinct non-zero real numbers. It is impossible for $e_{j-1}(T)=0$ and $e_j(T)=0$ simultaneously for any $j \ge 1$.

*Proof of Lemma:*
If $j=1$, $e_{j-1}(T) = e_0(T) = 1 \neq 0$.
If $j \ge 2$. Let $Q_T(x) = \prod_{t \in T}(x-t)$. $Q_T(x)$ has only distinct non-zero real roots. If $e_{j-1}(T)=0$ and $e_j(T)=0$, then $Q_T(x)$ has two consecutive zero coefficients (the coefficients of $x^{d-j+1}$ and $x^{d-j}$, where $d=|T|$).
Let $m = d-j$. The coefficients $c_m$ and $c_{m+1}$ are zero.
If $m=0$, $c_0=0$, implying $0$ is a root, which contradicts $T$ having non-zero roots.
If $m \ge 1$. Since $Q_T(x)$

[Note: response truncated to first 3000 characters of 5146]
