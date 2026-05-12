# artifact_115

Grading ID: GB-0856  
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

We want to prove that the polynomial $P(x)$ must have a non-real root. We proceed by contradiction.

Suppose that all the roots of $P(x)$ are real. Let $R$ be the set of roots. We are given that $P(x)$ has degree $n$, no repeated roots, and a nonzero constant term. Thus, $R$ consists of $n$ distinct real numbers, none of which is zero.

The hypothesis states that for any polynomial $Q(x)=a_{k}x^{k}+\dots+a_{1}x+a_{0}$ with real coefficients that divides $P(x)$, the product of its coefficients $a_{0}a_{1}\dots a_{k}$ is zero.

Let $S$ be any subset of $R$ with $|S|=k$. The polynomial $Q_S(x) = \prod_{s \in S}(x-s)$ is a monic divisor of $P(x)$ of degree $k$. Since the roots are real, $Q_S(x)$ has real coefficients. Let $Q_S(x) = c_k x^k + c_{k-1}x^{k-1} + \dots + c_0$.
We have $c_k=1$. The constant term is $c_0 = (-1)^k \prod_{s \in S} s$. Since the roots are non-zero, $c_0 \neq 0$.
The hypothesis implies $c_0 c_1 \dots c_k = 0$. Since $c_0 \neq 0$ and $c_k \neq 0$, there must be some intermediate coefficient that is zero: $c_j=0$ for some $j \in \{1, \dots, k-1\}$.

The coefficients are related to the elementary symmetric polynomials (ESPs) $e_m(S)$ of the elements in $S$ by $c_{k-m} = (-1)^m e_m(S)$.
Thus, the hypothesis implies that for any $k$-subset $S \subset R$, there exists an index $m \in J=\{1, \dots, k-1\}$ such that $e_m(S)=0$.

We consider two cases based on the value of $k$.

Case 1: $k=1$.
Since $n>k=1$, $P(x)$ has at least one root $r \in R$. $r$ is real and $r \neq 0$.
The polynomial $Q(x)=x-r$ is a divisor of $P(x)$. The coefficients are $c_1=1$ and $c_0=-r$.
The hypothesis states $c_1 c_0 = 0$, so $1 \cdot (-r) = 0$, which means $r=0$. This contradicts the fact that $r \neq 0$.
Thus, for $k=1$, the assumption that all roots are real leads to a contradiction.

Case 2: $k \ge 2$.
Since $n>k$, there exists a subset $R' \subset R$ of $k+1$ distinct roots. Let $\mathcal{S}$ be the collection of all $k$-subsets of $R'$. Then $|\mathcal{S}| = \binom{k+1}{k} = k+1$.
Let $J=\{1, \dots, k-1\}$. For each $S \in \mathcal{S}$, define $J(S) = \{j \in J \mid e_j(S)=0\}$. By the hypothesis, $J(S) \neq \emptyset$.

We claim that the sets $J(S)$ for $S \in \mathcal{S}$ are pairwise disjoint.
Suppose, for contradiction, that there are two distinct subsets $S_1, S_2 \in \mathcal{S}$ such that $J(S_1) \cap J(S_2) \neq \emptyset$. Let $j \in J(S_1) \cap J(S_2)$. Then $e_j(S_1)=0$ and $e_j(S_2)=0$.

Since $S_1, S_2$ are distinct $k$-subsets of the $(k+1)$-set $R'$, their intersection $T = S_1 \cap S_2$ has size $k-1$. We can write $S_1 = T \cup \{y\}$ and $S_2 = T \cup \{z\}$, where $y, z \in R'$ and $y \neq z$.

We use the identity $e_j(A \cup \{x\}) = e_j(A) + x e_{j-1}(A)$.
$e_j(S_1) = e_j(T) + y e_{j-1}(T) = 0$.
$e_j(S_2) = e_j(T) + z e_{j-1}(T) = 0$.
Subtracting the two equations yields $(y-z)e_{j-1}(T)=0$. Since $y \neq z$, we must have $e_{j-1}(T)=0$.
Substituting this back into the first equation gives $e_j(T)=0$.

We have found a set $T \subs

[Note: response truncated to first 3000 characters of 5120]
