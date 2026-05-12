# artifact_078

Grading ID: GB-0829  
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

Let $k$ and $d$ be positive integers. We want to prove that there exists a positive integer $N$ such that for every odd integer $n>N$, the digits in the base-$2n$ representation of $n^k$ are all greater than $d$.

Let $n$ be an odd positive integer, and let the base be $b=2n$.

**1. Base-$b$ Representation of $n^k$**

First, we observe the magnitude of $n^k$ in base $b$.
$$n^k < (2n)^k = b^k.$$
Thus, $n^k$ has at most $k$ digits in base $b$. We write the representation as:
$$n^k = \sum_{i=0}^{k-1} a_i b^i = a_{k-1}b^{k-1} + \dots + a_1 b + a_0,$$
where $a_i$ are the digits, satisfying $0 \le a_i < b$.

**2. Analyzing the Digits $a_i$**

We seek a lower bound for the digits $a_i$. The $i$-th digit $a_i$ (for $i \in \{0, 1, \dots, k-1\}$) can be expressed using the remainder of $n^k$ when divided by $b^{i+1}$. Let $R_i = n^k \pmod{b^{i+1}}$. Then $R_i = a_i b^i + a_{i-1}b^{i-1} + \dots + a_0$.
The digit $a_i$ is given by:
$$a_i = \left\lfloor \frac{R_i}{b^i} \right\rfloor.$$

We need to analyze the remainder $R_i = n^k \pmod{b^{i+1}}$.
We substitute $b=2n$:
$$b^{i+1} = (2n)^{i+1} = 2^{i+1} n^{i+1}.$$

We write $n^k$ as:
$$n^k = n^{i+1} \cdot n^{k-i-1}.$$
(Since $i \le k-1$, the exponent $k-i-1 \ge 0$.)

We perform the division of $n^{k-i-1}$ by $2^{i+1}$:
$$n^{k-i-1} = q_i \cdot 2^{i+1} + r_{i+1},$$
where $q_i$ is the quotient and $r_{i+1}$ is the remainder, satisfying $0 \le r_{i+1} < 2^{i+1}$.

Now we substitute this back into the expression for $n^k$:
$$n^k = n^{i+1} (q_i \cdot 2^{i+1} + r_{i+1}) = q_i (n^{i+1} 2^{i+1}) + r_{i+1} n^{i+1} = q_i b^{i+1} + r_{i+1} n^{i+1}.$$

We must verify that $r_{i+1} n^{i+1}$ is indeed the remainder $R_i$. We check if it is less than the modulus $b^{i+1}$.
Since $r_{i+1} < 2^{i+1}$, we have $r_{i+1} n^{i+1} < 2^{i+1} n^{i+1} = (2n)^{i+1} = b^{i+1}$.
So, $R_i = r_{i+1} n^{i+1}$.

**3. Using the Oddness of $n$**

The crucial step is utilizing the fact that $n$ is odd.
Since $n$ is odd, $n^{k-i-1}$ is also odd (as the exponent is non-negative).
The remainder $r_{i+1}$ is defined by $r_{i+1} = n^{k-i-1} \pmod{2^{i+1}}$.

Since $i \ge 0$, $i+1 \ge 1$, so the modulus $2^{i+1}$ is an even integer.
When an odd integer ($n^{k-i-1}$) is divided by an even integer ($2^{i+1}$), the remainder ($r_{i+1}$) must be odd.
Since $r_{i+1}$ is a non-negative integer, we must have $r_{i+1} \ge 1$.

**4. Lower Bound for the Digits $a_i$**

Now we can find a lower bound for the digit $a_i$:
$$a_i = \left\lfloor \frac{R_i}{b^i} \right\rfloor = \left\lfloor \frac{r_{i+1} n^{i+1}}{b^i} \right\rfloor.$$
Substituting $b^i = (2n)^i = 2^i n^i$:
$$a_i = \left\lfloor \frac{r_{i+1} n^{i+1}}{2^i n^i} \right\rfloor = \left\lfloor \frac{r_{i+1} n}{2^i} \right\rfloor.$$

Using the fact that $r_{i+1} \ge 1$ (from Step 3):
$$a_i \ge \left\lfloor \frac{1 \cdot n}{2^i} \right\rfloor = \left\lfloor \frac{n}{2^i} \right\rfloor.$$

**5. Determining N**

We want to find $N$ such that for every odd integer $n>N$, $a_i > d$ (i.e., $a_i \ge d+1$) for all $i \

[Note: response truncated to first 3000 characters of 4189]
