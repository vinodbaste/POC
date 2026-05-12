# artifact_147

Grading ID: GB-0641  
Problem ID: PB-Advanced-019  
Source: (Modified) IMO 2024 P1  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

For a real number $r$, let $A(r)$ denote the fractional part of $2r$ in its decimal representation. For a real number $r$ and a positive integer $n$, define $B(n,r)$ as
 $$
 B(n,r)=\sum_{k=1}^n A(kr).
 $$
 Find all positive real numbers $r$ such that $n(n+1)r - B(n,r)$ is a multiple of $n$ for all positive integers $n$.

## Reference Solution (for grader's calibration)

Let $r$ be a positive real number. Let $A(r)$ denote the fractional part of $2r$, so $A(r) = 2r - \lfloor 2r \rfloor$. We are given that $B(n,r) = \sum_{k=1}^n A(kr)$. We want to find all positive real numbers $r$ such that $n(n+1)r - B(n,r)$ is a multiple of $n$ for all positive integers $n$.

 We can rewrite the condition as
 $$
 n(n+1)r - \sum_{k=1}^n (2kr - \lfloor 2kr \rfloor) = \sum_{k=1}^n \lfloor 2kr \rfloor \quad \text{is a multiple of } n.
 $$
 Let $\alpha = 2r$. Then the condition becomes: $\sum_{k=1}^n \lfloor k\alpha \rfloor$ is a multiple of $n$ for all positive integers $n$.

 We prove that all even integers $\alpha$ satisfy the condition, and no other real number $\alpha$ does so. First we will show that
 even integers satisfy the condition. If $\alpha=2m$ where $m$ is
 an integer then

 \[
 \lfloor\alpha\rfloor+\lfloor2\alpha\rfloor+\cdots+\lfloor n\alpha\rfloor=2m+4m+\cdots+2mn=mn(n+1)
 \]

 which is a multiple of $n$. Since $r > 0$, we must have $\alpha = 2r > 0$. So $\alpha$ must be a positive even integer. If $\alpha = 2m$ for some positive integer $m$, then $r = m$, which is a positive integer.

 Now we will show that they are the only real numbers satisfying the
 conditions of the problem. Let $\alpha=k+\epsilon$ where $k$ is
 an integer and $0\leqslant\epsilon<1$. Then the number
 \[
 \begin{aligned}\lfloor\alpha\rfloor+\lfloor2\alpha\rfloor+\cdots+\lfloor n\alpha\rfloor & = \lfloor k+\epsilon \rfloor+\lfloor2(k+\epsilon)\rfloor+\cdots+\lfloor n(k+\epsilon)\rfloor

 & = k+\lfloor\epsilon\rfloor+2k+\lfloor2\epsilon\rfloor+\cdots+nk+\lfloor n\epsilon\rfloor

 & =\frac{kn(n+1)}{2}+\lfloor\epsilon\rfloor+\lfloor2\epsilon\rfloor+\cdots+\lfloor n\epsilon\rfloor
 \end{aligned}
 \]
 has to be a multiple of $n$. We consider two cases based on the parity
 of $k$.


 \begin{itemize}
 \item Case 1: \textbf{$k$ is even.} Then $\frac{kn(n+1)}{2}$ is always
 a multiple of $n$. Thus
 \[
 \lfloor\epsilon\rfloor+\lfloor2\epsilon\rfloor+\cdots+\lfloor n\epsilon\rfloor
 \]
 also has to be a multiple of $n$. We will prove that $\lfloor n\epsilon\rfloor=0$
 for every positive integer $n$ by strong induction. The base case
 $n=1$ follows from the fact that $0\leqslant\epsilon<1$. Let us
 suppose that $\lfloor m\epsilon\rfloor=0$ for every $1\leqslant m<n$.
 Then the number
 \[
 \lfloor\epsilon\rfloor+\lfloor2\epsilon\rfloor+\cdots+\lfloor n\epsilon\rfloor=\lfloor n\epsilon\rfloor
 \]
 has to be a multiple of $n$. As $0\leqslant\epsilon<1$ then $0\leqslant n\epsilon<n$,
 which means that the number $\lfloor n\epsilon\rfloor$ has to be
 equal to 0. The equality $\lfloor n\epsilon\rfloor=0$ implies $0\leqslant\epsilon<1/n$.
 Since this has to happen for all $n$, we conclude that $\epsilon=0$.
 Thus $\alpha$ is an even integer. Since $r > 0$, $\alpha = 2r > 0$. So $\alpha$ must be a positive even integer. This means $2r = 2m$ for some positive integer $m$. Therefore, $r=m$ must be a positive integer.
 \item Case 2: \textbf{$k$ is odd.} We will prove that $\lfloor n\epsilon\rfloor=n-1$
 for every natural number $n$ by strong induction. The base case $n=1$
 again follows from the fact that $0\leqslant\epsilon<1$. Let us suppose
 that $\lfloor m\epsilon\rfloor=m-1$ for every $1\leqslant m<n$.
 We need the number
 \[
 \begin{aligned}\frac{kn(n+1)}{2}+\lfloor\epsilon\rfloor+\lfloor2\epsilon\rfloor+\cdots+\lfloor n\epsilon\rfloor & =\frac{kn(n+1)}{2}+0+1+\cdots+(n-2)+\lfloor n\epsilon\rfloor

 & =\frac{kn(n+1)}{2}+\frac{(n-2)(n-1)}{2}+\lfloor n\epsilon\rfloor

 & =\frac{k+1}{2}n^{2}+\frac{k-3}{2}n+1+\lfloor n\epsilon\rfloor
 \end{aligned}
 \]
 to be a multiple of $n$. As $k$ is odd, we need $1+\lfloor n\epsilon\rfloor$
 to be a multiple of $n$. Again, as $0\leqslant\epsilon<1$ then $0\leqslant n\epsilon<n$,
 so $\lfloor n\epsilon\rfloor=n-1$ as we wanted. This implies that
 $1-\frac{1}{n}\leqslant\epsilon<1$ for all $n$. Taking the limit as $n \to \infty$, we get $\epsilon=1$, which contradicts $0 \le \epsilon < 1$.
 So there are no other solutions in this case.

 \end{itemize}
 Therefore, $\alpha = 2r$ must be a positive even integer. This implies $r$ must be a positive integer.

## Grading Guidelines

(Partial)
 1. Verified that integer $r$ works.
 2. Proved that $r$ should be integer if $r$ is a rational number.
(Almost)
 1. Proved that $r$ should be an integer, but did not verified that integers indeed work.
 2. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

We are asked to find all positive real numbers $r$ such that $n(n+1)r - B(n,r)$ is a multiple of $n$ for all positive integers $n$, where $A(r) = \{2r\}$ and $B(n,r) = \sum_{k=1}^n A(kr) = \sum_{k=1}^n \{2kr\}$.

**Step 1: Simplify the expression $n(n+1)r - B(n,r)$.**

We use the definition of the fractional part, $\{x\} = x - \lfloor x \rfloor$.
$$
B(n,r) = \sum_{k=1}^n \{2kr\} = \sum_{k=1}^n (2kr - \lfloor 2kr \rfloor) = \left(\sum_{k=1}^n 2kr\right) - \sum_{k=1}^n \lfloor 2kr \rfloor.
$$
The first summation is:
$$
\sum_{k=1}^n 2kr = 2r \sum_{k=1}^n k = 2r \frac{n(n+1)}{2} = n(n+1)r.
$$
Let $S(n,r) = \sum_{k=1}^n \lfloor 2kr \rfloor$. $S(n,r)$ is an integer.
Then $B(n,r) = n(n+1)r - S(n,r)$.

Let $C(n,r) = n(n+1)r - B(n,r)$. Substituting $B(n,r)$:
$$
C(n,r) = n(n+1)r - (n(n+1)r - S(n,r)) = S(n,r).
$$
The condition requires $C(n,r)$ to be a multiple of $n$ for all $n \ge 1$. Therefore, $S(n,r) = \sum_{k=1}^n \lfloor 2kr \rfloor$ must be a multiple of $n$ for all $n \ge 1$.

**Step 2: Analyze the average value.**

Let $K_n = \frac{S(n,r)}{n}$. The condition requires $K_n$ to be an integer for all $n \ge 1$.

We can also express $K_n$ as:
$$
K_n = \frac{C(n,r)}{n} = \frac{n(n+1)r - B(n,r)}{n} = (n+1)r - F_n,
$$
where $F_n = \frac{B(n,r)}{n} = \frac{1}{n} \sum_{k=1}^n \{2kr\}$ is the average of the fractional parts.
Since $0 \le \{x\} < 1$, we have $0 \le B(n,r) < n$, and thus $0 \le F_n < 1$.

**Step 3: Analyze differences of consecutive terms.**

Since $K_n$ is an integer for all $n \ge 1$, the difference $D_n = K_{n+1} - K_n$ must also be an integer for all $n \ge 1$.
$$
D_n = K_{n+1} - K_n = \left((n+2)r - F_{n+1}\right) - \left((n+1)r - F_n\right) = r - (F_{n+1} - F_n).
$$
Let $\Delta_n = F_{n+1} - F_n$. Then $D_n = r - \Delta_n$.

**Step 4: Bound the difference $\Delta_n$.**

We relate $F_{n+1}$ and $F_n$. Note that $B(n+1,r) = B(n,r) + \{2(n+1)r\}$.
Using $B(n,r) = nF_n$:
$$
(n+1)F_{n+1} = nF_n + \{2(n+1)r\}.
$$
We calculate $\Delta_n = F_{n+1} - F_n$:
$$
\begin{aligned}
(n+1)\Delta_n &= (n+1)F_{n+1} - (n+1)F_n \\
&= (nF_n + \{2(n+1)r\}) - (n+1)F_n \\
&= \{2(n+1)r\} - F_n.
\end{aligned}
$$
So, $\Delta_n = \frac{\{2(n+1)r\} - F_n}{n+1}$.

Since $0 \le \{2(n+1)r\} < 1$ and $0 \le F_n < 1$, the numerator is strictly bounded:
$$
-1 < \{2(n+1)r\} - F_n < 1.
$$
Therefore, the magnitude of $\Delta_n$ is bounded by:
$$
|\Delta_n| = \frac{|\{2(n+1)r\} - F_n|}{n+1} < \frac{1}{n+1}.
$$

**Step 5: Prove that $r$ must be an integer.**

We established that $D_n = r - \Delta_n$ is an integer for all $n \ge 1$. This implies:
$$
|r - D_n| = |\Delta_n| < \frac{1}{n+1}.
$$
This inequality means that for any positive integer $n$, there exists an integer $D_n$ whose distance from $r$ is less than $1/(n+1)$.

Assume, for the sake of contradiction, that $r$ is not an integer. Let $d$ be the distance from $r$ to the nearest integer. Since $r$ is not an integer, $d > 0$. By definition, for any integer $J$, $|r - J| \ge d$.

We can choose a positive integer $N$ large

[Note: response truncated to first 3000 characters of 4044]
