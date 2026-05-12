# artifact_104

Grading ID: GB-0825  
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

Let the base be $B = 2n$. We are considering the base-$B$ representation of $n^k$. Let this representation be $(a_m a_{m-1} \dots a_1 a_0)_B$. This means that
$$n^k = \sum_{i=0}^m a_i B^i = \sum_{i=0}^m a_i (2n)^i$$
where the digits $a_i$ are integers satisfying $0 \le a_i < 2n$.

Our proof will proceed in five main steps:
1.  Determine the number of digits in the representation for large $n$.
2.  Derive a general formula for the digits $a_i$.
3.  Establish a lower bound for each digit in terms of $n$.
4.  Choose a suitable integer $N$ based on these lower bounds.
5.  Verify that this choice of $N$ satisfies the problem's conditions.

**Step 1: Number of digits**

The number of digits in the base-$2n$ representation of $n^k$ is $m+1$, where $m = \lfloor \log_{2n}(n^k) \rfloor$. Let's analyze this expression:
$$ m = \lfloor \log_{2n}(n^k) \rfloor = \left\lfloor \frac{\ln(n^k)}{\ln(2n)} \right\rfloor = \left\lfloor \frac{k \ln n}{\ln 2 + \ln n} \right\rfloor = \left\lfloor \frac{k}{1 + \frac{\ln 2}{\ln n}} \right\rfloor. $$
As $n$ becomes large, the term $\frac{\ln 2}{\ln n}$ approaches 0 from above. Thus, the expression inside the floor, $\frac{k}{1 + \frac{\ln 2}{\ln n}}$, approaches $k$ from below. For sufficiently large $n$, the number of digits will be exactly $k$. This happens when $m = k-1$.

The condition $m=k-1$ is equivalent to $k-1 \le \log_{2n}(n^k) < k$.
The right inequality, $\log_{2n}(n^k) < k$, is equivalent to $n^k < (2n)^k = 2^k n^k$, which is true for all $n \ge 1$ since $2^k > 1$.
The left inequality, $k-1 \le \log_{2n}(n^k)$, is equivalent to $(2n)^{k-1} \le n^k$. This simplifies to $2^{k-1} n^{k-1} \le n^k$. For $n>0$, we can divide by $n^{k-1}$ to get $n \ge 2^{k-1}$.

So, for any integer $n \ge 2^{k-1}$, the base-$2n$ representation of $n^k$ has exactly $k$ digits. Let these be $a_{k-1}, a_{k-2}, \dots, a_0$. The representation is given by:
$$n^k = \sum_{i=0}^{k-1} a_i (2n)^i.$$

**Step 2: Formula for the digits**

The digits $a_i$ can be calculated by the standard algorithm. Let $X_0 = n^k$. For $i \ge 0$, we define recursively:
$a_i = X_i \pmod{2n}$
$X_{i+1} = \lfloor X_i / (2n) \rfloor = (X_i - a_i)/(2n)$

From this recurrence, we can express the quotient $X_i$ directly as $X_i = \lfloor \frac{n^k}{(2n)^i} \rfloor = \lfloor \frac{n^{k-i}}{2^i} \rfloor$.
The digits are given by $a_i = X_i - 2n X_{i+1}$ for $i=0, \dots, k-2$, and $a_{k-1} = X_{k-1}$ (since $X_k = \lfloor n^0/2^k \rfloor = 0$ for $k \ge 1$).
The formula $a_i = X_i - 2n X_{i+1}$ holds for $i=k-1$ as well.
Substituting the expression for $X_i$ and $X_{i+1}$, we get:
$$a_i = \left\lfloor \frac{n^{k-i}}{2^i} \right\rfloor - 2n \left\lfloor \frac{n^{k-i-1}}{2^{i+1}} \right\rfloor.$$
To simplify this, let $x = n^{k-i-1}$ and $M = 2^{i+1}$. Let $x = qM + 

[Note: response truncated to first 3000 characters of 7345]
