# artifact_105

Grading ID: GB-0819  
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

Let $k$ and $d$ be positive integers. We want to prove that there exists a positive integer $N$ such that for every odd integer $n>N$, the digits in the base-$2n$ representation of $n^{k}$ are all greater than $d$.

Let $n$ be an odd positive integer. Let $B=2n$ be the base. We seek the representation of $n^k$ in base $B$.
We will show that $n^k$ can be written as a sum of $k$ terms in powers of $B$, $n^k = \sum_{i=0}^{k-1} a_i B^i$, where the coefficients $a_i$ are the digits. We will then find conditions on $n$ such that $0 \le a_i < B$ and $a_i > d$.

We define a sequence of remainders $r_j$ and digits $a_{k-j}$ iteratively.
Let $r_0 = 1$. For $j=1, 2, \dots, k$, we define $a_{k-j}$ and $r_j$ using the division algorithm when dividing $r_{j-1}n$ by $2^{k-j}$:
$$ r_{j-1}n = a_{k-j} 2^{k-j} + r_j, \quad \text{where } 0 \le r_j < 2^{k-j}. $$
This means $a_{k-j} = \left\lfloor \frac{r_{j-1}n}{2^{k-j}} \right\rfloor$.

First, we verify that these coefficients $a_i$ correspond to the base-$B$ representation of $n^k$. We calculate the value represented by these coefficients:
$$ \sum_{i=0}^{k-1} a_i B^i = \sum_{j=1}^k a_{k-j} B^{k-j} = \sum_{j=1}^k a_{k-j} (2n)^{k-j} = \sum_{j=1}^k a_{k-j} 2^{k-j} n^{k-j}. $$
From the definition, we have $a_{k-j} 2^{k-j} = r_{j-1}n - r_j$. Substituting this into the sum:
$$ \sum_{j=1}^k (r_{j-1}n - r_j) n^{k-j} = \sum_{j=1}^k (r_{j-1}n^{k-j+1} - r_j n^{k-j}). $$
This is a telescoping sum:
$$ (r_0 n^k - r_1 n^{k-1}) + (r_1 n^{k-1} - r_2 n^{k-2}) + \dots + (r_{k-1} n^1 - r_k n^0) = r_0 n^k - r_k. $$
We have $r_0=1$. For $j=k$, the constraint on $r_k$ is $0 \le r_k < 2^{k-k} = 2^0 = 1$. Thus, $r_k=0$.
The sum equals $n^k$. So $n^k = \sum_{i=0}^{k-1} a_i B^i$.

Next, we must verify that the coefficients $a_i$ are valid digits in base $B=2n$, i.e., $0 \le a_i < 2n$.
$a_{k-j} \ge 0$ is clear from the definition.
We check the upper bound. The constraints on the remainders are $r_j < 2^{k-j}$.
For $j=1$, $r_0=1$. $a_{k-1} = \lfloor n/2^{k-1} \rfloor$.
If $k=1$, $a_0 = n < 2n$.
If $k \ge 2$, $a_{k-1} \le n/2^{k-1} \le n/2 < 2n$.
For $j \ge 2$, we use the bound on $r_{j-1}$. $r_{j-1} < 2^{k-(j-1)} = 2^{k-j+1}$.
$$ a_{k-j} = \left\lfloor \frac{r_{j-1}n}{2^{k-j}} \right\rfloor < \frac{2^{k-j+1}n}{2^{k-j}} = 2n. $$
Thus, the coefficients $a_i$ are valid digits in base $2n$.

Now we use the assumption that $n$ is odd. We analyze the remainders $r_j$.
We claim that $r_j$ is odd for $j=0, 1, \dots, k-1$.
We prove this by induction.
Base case: $r_0=1$ is odd.
Inductive step: Assume $r_{j-1}$ is odd. We consider $r_j$ for $j \le k-1$.
We have $r_j = r_{j-1}n \pmod{2^{k-j}}$.
Since $n$ is odd and $r_{j-1}$ is odd (by hypothesis), their product $r_{j-1}n$ is odd.
Since $j \le k-1$, $k-j \ge 1$, so $2^{k-j}$ is even.
The remainder of an odd integer divided by an even integer must be odd. Thus, $r_j$ is odd.
Since $r_j$ are non-negative integers, we must have $r_j \ge 1$ for $j=0, 1, \dots, k-1$.

Now we establish a lower bound for the dig

[Note: response truncated to first 3000 characters of 5203]
