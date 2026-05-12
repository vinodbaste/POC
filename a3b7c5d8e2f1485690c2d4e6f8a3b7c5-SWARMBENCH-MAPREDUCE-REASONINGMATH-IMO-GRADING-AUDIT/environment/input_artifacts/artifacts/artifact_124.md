# artifact_124

Grading ID: GB-0868  
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

We want to prove that $P(x)$ has a non-real root. We proceed by contradiction. Assume that all the roots of $P(x)$ are real. Let $R$ be the set of roots. The polynomial $P(x)$ has degree $n$, so $|R|=n$. We are given that $P(x)$ has no repeated roots, so the roots in $R$ are distinct. We are also given that the constant term of $P(x)$ is nonzero, which implies that $0 \notin R$.

The hypothesis states that for any polynomial $Q(x)=a_{k}x^{k}+\dots+a_{1}x+a_{0}$ that divides $P(x)$, the product $a_{0}a_{1}\dots a_{k}$ is zero.

Let's consider a divisor $Q(x)$ of degree exactly $k$. The coefficient $a_k$ is nonzero. We can assume $Q(x)$ is monic without loss of generality (by dividing by $a_k$, which does not affect the condition that the product of coefficients is zero). Let $S \subset R$ be the set of $k$ roots of $Q(x)$.
$Q(x) = \prod_{s \in S}(x-s) = x^k + a_{k-1}x^{k-1} + \dots + a_1x + a_0$.
The coefficients are related to the elementary symmetric polynomials $e_m(S)$ of the roots in $S$. $a_{k-m} = (-1)^m e_m(S)$.
$a_k=1$. The constant term is $a_0 = (-1)^k e_k(S) = (-1)^k \prod_{s \in S} s$. Since all roots are non-zero, $a_0 \neq 0$.
The hypothesis $a_0 a_1 \dots a_k = 0$ implies that at least one of the intermediate coefficients $a_1, \dots, a_{k-1}$ must be zero.
This is equivalent to the statement that for any $k$-subset $S \subset R$, there exists some $m \in \{1, \dots, k-1\}$ such that $e_m(S)=0$.

Case 1: $k=1$.
The set of intermediate indices $\{1, \dots, k-1\}$ is empty. The hypothesis states that for any divisor $Q(x)=a_1x+a_0$, $a_1a_0=0$.
Since $n>k=1$, $P(x)$ has at least one root $r \in R$. $r$ is real and $r \ne 0$.
The polynomial $Q(x)=x-r$ is a divisor of $P(x)$. Here $a_1=1$ and $a_0=-r$.
$a_1a_0 = -r \ne 0$. This contradicts the hypothesis.
Thus, for $k=1$, $P(x)$ must have a non-real root.

Case 2: $k \ge 2$.
Since $n>k$, there are at least $k+1$ distinct real non-zero roots. Let $R' \subset R$ be a subset of size $k+1$. Let $\mathcal{S}$ be the set of all $k$-subsets of $R'$. The size of $\mathcal{S}$ is $\binom{k+1}{k} = k+1$.

For each $S \in \mathcal{S}$, the hypothesis guarantees the existence of an index $m \in \{1, \dots, k-1\}$ such that $e_m(S)=0$. We define a map (coloring) $c: \mathcal{S} \to \{1, \dots, k-1\}$ by choosing such an index $c(S)=m$ for each $S$.

We will show that the map $c$ must be injective.
Suppose, for the sake of contradiction, that $c(S_1)=c(S_2)=m$ for two distinct subsets $S_1, S_2 \in \mathcal{S}$.
Since $S_1$ and $S_2$ are distinct $k$-subsets of $R'$, their intersection $K = S_1 \cap S_2$ has size $k-1$.
Let $S_1 = K \cup \{a\}$ and $S_2 = K \cup \{b\}$, where $a, b \in R'$ and $a \neq b$ (since the roots are distinct).
We use the identity $e_m(X \cup \{y\}) = e_m(X) + y e_{m-1}(X)$.
Since $e_m(S_1)=0$ and $e_m(S_2)=0$:
$e_m(K) + a e_{m-1}(K) = 0$.
$e_m(K) + b e_{m-1}(K) = 0$.
Subtracting the two equations yields $(a-b)e_{m-1}(K)=0$. Since $a \neq b$, we must have $e_{m-1}(K)=0$.
Sub

[Note: response truncated to first 3000 characters of 4597]
