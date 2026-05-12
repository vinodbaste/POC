# artifact_132

Grading ID: GB-0839  
Problem ID: PB-Advanced-025  
Source: USAMO 2025  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $k$ and $d$ be positive integers. Prove that there exists a
 positive integer $N$ such that for every odd integer $n>N$, the
 digits in the base-$2n$ representation of $n^{k}$ are all greater
 than $d$.

## Reference Solution (for grader's calibration)

The problem actually doesn't have much to do with digits: the idea
 is to pick any length $\ell\leq k$, and look at the rightmost $\ell$
 digits of $n^{k}$; that is, the remainder upon division by $(2n)^{\ell}$.
 We compute it exactly:

 Claim - Let $n\geq1$ be an odd integer, and $k\geq\ell\geq1$ integers.
 Then

 \[
 n^{k}\bmod(2n)^{l}=c(k,\ell)\cdot n^{l}
 \]

 for some odd integer $1\leq c(k,\ell)\leq2^{\ell}-1$.

 Proof. This follows directly by the Chinese remainder theorem, with
 $c(k,\ell)$ being the residue class of $n^{k-i}\left(\bmod2^{\ell}\right)$
 since $n$ is odd. In particular, for the $\ell$ th digit from the
 right to be greater than $d$, it would be enough that
 \[
 c(k,\ell)\cdot n^{\ell}\geq(d+1)\cdot(2n)^{\ell-1}
 \]
 But this inequality holds whenever $n\geq(d+1)\cdot2^{\ell-1}$.

 Putting this together by varying $\ell$, we find that for all odd

 \[
 n\geq(d+1)\cdot2^{k-1}
 \]

 we have that
 \begin{itemize}
 \item $n^{k}$ has $k$ digits in base- $2n$; and
 \item for each $\ell=1,\ldots,k$, the $\ell^{\text{th }}$ digit from the
 right is at least $d+1$

  so the problem is solved.

  Remark. Note it doesn't really matter that $c(k,i)$ is odd per se;
 we only need that $c(k,i)\geq1$.
 \end{itemize}

## Grading Guidelines

(Partial)
 1. Proved that $n^{k}$ has $k$ digits on base $2n$ representation for sufficiently large $n$.
 2. Expressed the $i$th digit such as $\lfloor\frac{n^{k}}{(2n)^{i}}\rfloor\pmod{2n}$.
(Almost)
 1. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

**Outcome 1: COMPLETE PROOF**

Let $k$ and $d$ be positive integers. We want to prove the existence of a positive integer $N$ such that for every odd integer $n>N$, the digits in the base-$2n$ representation of $n^{k}$ are all greater than $d$.

**1. Constructing the Base-$2n$ Representation of $n^k$**

We explicitly construct the digits $a_i$ of $n^k$ in base $2n$. We define sequences of integers $r_i$ (remainders) and $a_i$ (digits) recursively.

Let $r_k = 1$. For $i = k-1, k-2, \dots, 0$, we define $a_i$ and $r_i$ by applying the division algorithm to $r_{i+1}n$ divided by $2^i$:
$$ r_{i+1} n = a_i 2^i + r_i, \quad \text{where } 0 \le r_i < 2^i. $$
Thus, $a_i = \left\lfloor \frac{r_{i+1} n}{2^i} \right\rfloor$. Since $n>0$ and $r_i \ge 0$ (by induction starting from $r_k=1$), we have $a_i \ge 0$.

We verify that this construction yields $n^k = \sum_{i=0}^{k-1} a_i (2n)^i$.
From the definition, $a_i 2^i = r_{i+1} n - r_i$. Multiplying by $n^i$:
$$ a_i (2n)^i = a_i 2^i n^i = (r_{i+1} n - r_i) n^i = r_{i+1} n^{i+1} - r_i n^i. $$
Summing from $i=0$ to $k-1$:
$$ \sum_{i=0}^{k-1} a_i (2n)^i = \sum_{i=0}^{k-1} (r_{i+1} n^{i+1} - r_i n^i). $$
This is a telescoping sum, which evaluates to $r_k n^k - r_0 n^0$.
We have $r_k = 1$. For $i=0$, the constraint $0 \le r_0 < 2^0 = 1$ implies $r_0 = 0$.
Thus, $\sum_{i=0}^{k-1} a_i (2n)^i = n^k$.

We must verify that $a_i$ are valid digits in base $2n$, i.e., $a_i < 2n$.
For $i \in \{0, 1, \dots, k-2\}$, we have $r_{i+1} < 2^{i+1}$ by definition.
$$ a_i = \left\lfloor \frac{r_{i+1} n}{2^i} \right\rfloor < \frac{r_{i+1} n}{2^i} < \frac{2^{i+1} n}{2^i} = 2n. $$
For $i=k-1$, $r_k=1$, so $a_{k-1} = \lfloor n/2^{k-1} \rfloor$. Since $k \ge 1$, $2^{k-1} \ge 1$, so $a_{k-1} \le n < 2n$.
Thus, $a_0, a_1, \dots, a_{k-1}$ are the digits of $n^k$ in base $2n$.

**2. Analyzing Remainders when $n$ is Odd**

We now use the condition that $n$ is odd.

**Lemma:** If $n$ is odd, then $r_i$ is odd for $i=1, 2, \dots, k$.

*Proof:* We use backward induction on $i$.
Base case: $r_k = 1$, which is odd.
Inductive step: Assume $r_{i+1}$ is odd for some $i \in \{1, 2, \dots, k-1\}$.
We have $r_i = r_{i+1} n - a_i 2^i$.
Since $n$ is odd and $r_{i+1}$ is assumed odd, $r_{i+1} n$ is odd.
Since $i \ge 1$, $2^i$ is even, so $a_i 2^i$ is even.
$r_i = (\text{Odd}) - (\text{Even})$, so $r_i$ is odd.

Since $r_i$ are non-negative integers, if $r_i$ is odd, then $r_i \ge 1$.
Thus, if $n$ is odd, $r_i \ge 1$ for $i=1, 2, \dots, k$.

**3. Bounding the Digits and Determining N**

We seek a lower bound for the digits $a_i$, for $i=0, 1, \dots, k-1$.
$$ a_i = \left\lfloor \frac{r_{i+1} n}{2^i} \right\rfloor. $$
Since $i+1 \in \{1, \dots, k\}$, if $n$ is odd, we have $r_{i+1} \ge 1$.
Therefore,
$$ a_i \ge \left\lfloor \frac{1 \cdot n}{2^i} \right\rfloor = \left\lfloor \frac{n}{2^i} \right\rfloor. $$

We require $a_i > d$, or $a_i \ge d+1$. It suffices to ensure $\lfloor n/2^i \rfloor \ge d+1$ for all $i \in \{0, 1, \dots, k-1\}$.

For $i \le k-1$, we 

[Note: response truncated to first 3000 characters of 3826]
