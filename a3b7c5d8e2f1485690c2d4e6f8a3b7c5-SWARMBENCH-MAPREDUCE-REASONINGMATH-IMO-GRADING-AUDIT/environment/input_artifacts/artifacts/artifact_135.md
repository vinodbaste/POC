# artifact_135

Grading ID: GB-0824  
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

Let $b=2n$ be the base. We want to study the digits of $n^k$ in base $b$.

Step 1: Determine the number of digits.
The number of digits in the base-$b$ representation of an integer $X$ is $\lfloor \log_b X \rfloor + 1$.
For $n^k$, the number of digits is $m+1$, where $m = \lfloor \log_{2n}(n^k) \rfloor$.
$$m = \left\lfloor k \log_{2n}(n) \right\rfloor = \left\lfloor k \frac{\ln n}{\ln(2n)} \right\rfloor = \left\lfloor k \frac{\ln n}{\ln n + \ln 2} \right\rfloor.$$
We can rewrite the fraction as $1 - \frac{\ln 2}{\ln n + \ln 2}$. So,
$$m = \left\lfloor k \left(1 - \frac{\ln 2}{\ln n + \ln 2}\right) \right\rfloor = \left\lfloor k - \frac{k \ln 2}{\ln n + \ln 2} \right\rfloor.$$
For $n > 2^{k-1}$, we have $\ln n > (k-1)\ln 2$, which implies $\ln(2n) = \ln n + \ln 2 > k \ln 2$.
Therefore, $0 < \frac{k \ln 2}{\ln(2n)} < 1$.
This gives $k-1 < k - \frac{k \ln 2}{\ln n + \ln 2} < k$.
So, $m = k-1$.
This means for any integer $n > 2^{k-1}$, the base-$2n$ representation of $n^k$ has exactly $k$ digits.
Let these digits be $a_{k-1}, a_{k-2}, \ldots, a_0$. The representation is given by:
$$n^k = \sum_{j=0}^{k-1} a_j (2n)^j, \quad \text{where } 0 \le a_j < 2n \text{ for each } j.$$

Step 2: Find a formula for the digits.
The digits $a_j$ can be found using the standard algorithm. For a number $X$, the digit $a_j$ in base $b$ is given by $a_j = \lfloor X/b^j \rfloor \pmod b$.
In our case, $X=n^k$ and $b=2n$.
$$a_j = \left\lfloor \frac{n^k}{(2n)^j} \right\rfloor \pmod{2n}.$$
This can be explicitly written as:
$$a_j = \left\lfloor \frac{n^k}{(2n)^j} \right\rfloor - 2n \left\lfloor \frac{n^k}{(2n)^{j+1}} \right\rfloor.$$
Let's simplify this expression for $a_j$:
$$a_j = \left\lfloor \frac{n^{k-j}}{2^j} \right\rfloor - 2n \left\lfloor \frac{n^{k-j-1}}{2^{j+1}} \right\rfloor.$$
Let $x = \frac{n^{k-j-1}}{2^{j+1}}$. The expression becomes $a_j = \lfloor 2n \cdot x \rfloor - 2n \lfloor x \rfloor$.
For any real number $x$, let $x = \lfloor x \rfloor + \{x\}$, where $\{x\}$ is the fractional part, $0 \le \{x\} < 1$.
$a_j = \lfloor 2n (\lfloor x \rfloor + \{x\}) \rfloor - 2n \lfloor x \rfloor = \lfloor 2n \lfloor x \rfloor + 2n \{x\} \rfloor - 2n \lfloor x \rfloor$.
Since $2n \lfloor x \rfloor$ is an integer, this simplifies to:
$a_j = 2n \lfloor x \rfloor + \lfloor 2n \{x\} \rfloor - 2n \lfloor x \rfloor = \lfloor 2n \{x\} \rfloor$.
The fractional part $\{x\}$ is given by:
$$\{x\} = \frac{n^{k-j-1}}{2^{j+1}} - \left\lfloor \frac{n^{k-j-1}}{2^{j+1}} \right\rfloor = \frac{n^{k-j-1} \pmod{2^{j+1}}}{2^{j+1}}.$$
Substituting this back into the expression for $a_j$:
$$a_j = \left\lfloor 2n \cdot \frac{n^{k-j-1} \pmod{2^{j+1}}}{2^{j+1}} \right\rfloor = \left\lfloor \frac{n \cdot (n^{k-j-1} \pmod{2^{j+1}})}{2^j} \right\rfloor.$$

Step 3: Find a lower bound for the digits.
Let $s_j = n^{k-j-1} \pmod{2^{j+1}}$. The formula for the digit is $a_j = \lfloor \frac{n s_j}{2^j} \rfloor$.
We are given that $n$ is an odd integer. Therefore, $n^p$ is odd for any integer $p \ge 0$.
For $j 

[Note: response truncated to first 3000 characters of 5449]
