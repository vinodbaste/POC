# artifact_008

Grading ID: GB-0026  
Problem ID: PB-Advanced-001  
Source: Novel Problem  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

For a positive integer $n$, let $A_{n}$ be the number of perfect powers less than or equal to $n$. Here, a perfect power is a number that can be expressed in the form $a^{b}$, where $a$ is a positive integer and $b$ is an integer greater than or equal to 2. Prove that there are infinitely many $n$ such that $A_{n}$ divides $n+2024$.

## Reference Solution (for grader's calibration)

Let's look at the following lemma using the intermediate value property.

 <Lemma 1> If a sequence of non-negative integers $\left(x_{n}\right)_{n=1}^{\infty}$ satisfies $x_{n+1}-x_{n} \in\{0,1\}$ and for any $M>0$, there exists a positive integer $n$ such that $\frac{n}{x_{n}}>M$, then there are infinitely many $n$ such that $\frac{n}{x_{n}}$ is a positive integer.

 <Proof of Lemma 1> First, let $k_{0}$ be the smallest $k$ such that $x_{k} \geq 1$. Now, we will prove that for any integer $m \geq k_{0}$, there exists an $n$ such that $\frac{n}{x_{n}}=m$.

 (1) There exists a positive integer $n$ such that $\frac{n}{x_{n}}>m$, and let $n_{0}$ be the smallest such $n$. Since $\frac{k_{0}}{x_{k_{0}}} \leq k_{0}$, we have $n_{0} \geq k_{0}+1$.

 (2) By the minimality of $n_{0}$ and $n_{0} \geq k_{0}+1$, we have $\frac{n_{0}-1}{x_{n_{0}-1}} \leq m$. If $\frac{n_{0}-1}{x_{n_{0}-1}}<m$, then

 \[
 n_{0}<m x_{n_{0}-1}+1 \quad \Rightarrow \quad n_{0} \leq m x_{n_{0}-1}.
 \]

 However, from $\frac{n_{0}}{x_{n_{0}}}>m$, we have $m x_{n_{0}}<n_{0}$, so combining the two results gives

 \[
 m x_{n_{0}-1} \geq n_{0}>m x_{n_{0}},
 \]

 which leads to $x_{n_{0}-1}>x_{n_{0}}$. This contradicts the condition of the problem that $x_{n+1}-x_{n} \in\{0,1\}$. Therefore, we must have $\frac{n_{0}-1}{x_{n_{0}-1}}=m$, and the proof is complete.

 Therefore, for any integer $m \geq k_{0}$, there exists an $n$ such that $\frac{n}{x_{n}}=m$, and it is obvious that these values of $n$ are different for different $m$, so the proof is complete. \qed

 The following lemma is a Bernoulli-type inequality.

 <Lemma 2> For any integer $k \geq 2$, we have $2^{k} \geq \frac{k^{2}}{2}$.

 <Proof of Lemma 2> Since $k \geq 2$, by the binomial theorem, we have

 \[
 2^{k} \geq 1+k+\binom{k}{2}=1+\frac{k}{2}+\frac{k^{2}}{2}>\frac{k^{2}-k}{2},
 \]

 so the proof is complete. $\qed$

 Now, let's prove the main problem.

 <Step 1> Finding an upper bound for $A_{n}$

 <Step 1.1> For a positive integer $a$ and $k \geq 2$, let a number of the form $a^{k}$ be called a $k$-th power. Then, for any $k$-th power $a^{k}$ to be less than or equal to $n$, we must have

 \[
 a^{k} \leq n \quad \Rightarrow \quad a \leq n^{\frac{1}{k}},
 \]

 so the number of $k$-th powers less than or equal to $n$ is less than or equal to $n^{\frac{1}{k}}$.

 <Step 1.2> If any $k$-th power other than 1 is less than or equal to $n$, then we must have $2^{k} \leq n$, so $k \leq \log _{2} n$.

 <Step 1.3> By (1) and (2) above, $A_{n}$ satisfies the following:

 \[
 A_{n} \leq \sum_{k=2}^{\left[\log _{2} n\right]} n^{\frac{1}{k}} \leq\left(\left[\log _{2} n\right]-1\right) n^{\frac{1}{2}}<\log _{2} n \cdot n^{\frac{1}{2}}.
 \]

 <Step 2> Solving the problem using the lemma

 Now, let the sequence $\left(x_{n}\right)_{n=1}^{\infty}$ be defined as $x_{n}=0$ if $n \leq 2024$ and $x_{n}=A_{n-2024}$ for $n \geq 2025$.

 <Step 2.1> Since $A_{1}=1$ and $A_{n+1}-A_{n}$ is 1 if $n+1$ is a perfect power and 0 otherwise, $x_{n}$ satisfies $x_{n+1}-x_{n} \in\{0,1\}$ for any $n \geq 1$.

 <Step 2.2> By <Step 1>, we have $A_{2^{2 k}} \leq 2 k \cdot 2^{k}$, so by <Lemma 2>, we have

 \[
 \frac{2^{2 k}}{A_{2^{2 k}}} \geq \frac{2^{k}}{2 k} \geq \frac{k}{4}.
 \]

 Since $A_{n}$ is an increasing sequence, we have $A_{n} \geq x_{n}$, so $\frac{n}{x_{n}} \geq \frac{n}{A_{n}}$. Combining these results gives

 \[
 \frac{2^{2 k}}{x_{2^{2 k}}} \geq \frac{2^{2 k}}{A_{2^{2 k}}} \geq \frac{k}{4},
 \]

 so for any $M>0$, there exists an $n$ such that $\frac{n}{x_{n}}>M$.

 <Step 2.3> By (1), (2), and <Lemma 1> above, there are infinitely many $n$ such that $x_{n} \mid n$. Therefore, there are also infinitely many $n$ such that

 \[
 \frac{n+2024}{A_{n}}=\frac{n+2024}{x_{n+2024}}
 \]

 is a positive integer.

## Grading Guidelines

(Partial)
 1. Observed that $A_n$ is a slowly increasing sequence, and from there guessed that the sequence satisfied some property such as Lemma 1 of the given solution.
(Almost)
 1. Applied intermediate value property to get useful information, but couldn't complete the proof.

## Candidate Response (to be graded)

Let $A_n$ be the number of perfect powers less than or equal to $n$. A perfect power is an integer of the form $a^b$ where $a\ge 1$ and $b\ge 2$. We want to prove that there are infinitely many positive integers $n$ such that $A_n$ divides $n+2024$.

Let $S$ be the set of perfect powers. Let $s_1 < s_2 < s_3 < \dots$ be the elements of $S$ in increasing order (so $s_1=1, s_2=4, s_3=8, \dots$).
The function $A_n$ is a step function that increases by 1 at each perfect power. For any integer $k \ge 1$, $A_n=k$ if and only if $n$ belongs to the interval $I_k = [s_k, s_{k+1}-1]$.

We are looking for integers $n$ such that $A_n \mid n+2024$. If we fix $A_n=k$, we are looking for $n \in I_k$ such that $k \mid n+2024$, which is equivalent to $n \equiv -2024 \pmod k$.

The interval $I_k$ consists of $L_k = s_{k+1}-s_k$ consecutive integers. If $L_k \ge k$, then $I_k$ contains a complete set of residues modulo $k$. Therefore, there must exist an $n \in I_k$ such that $n \equiv -2024 \pmod k$.

To prove the statement, it is sufficient to show that $s_{k+1}-s_k \ge k$ for infinitely many values of $k$. We will prove this using the asymptotic density of perfect powers.

First, we estimate the growth of $A_n$. The perfect powers are the union of squares, cubes, fifth powers, and so on. The dominant term is the number of squares.
$A_n = |S \cap [1, n]|$. Let $Q$ be the set of perfect squares. $|Q \cap [1, n]| = \lfloor \sqrt{n} \rfloor$.
$A_n = \lfloor \sqrt{n} \rfloor + B_n$, where $B_n$ is the number of non-square perfect powers up to $n$.
A non-square perfect power must be of the form $a^b$ where $b\ge 3$. (In fact, it must have a prime exponent $p\ge 3$ in its canonical representation as $y^g$).
$B_n \le \sum_{b=3}^{\lfloor \log_2 n \rfloor} \lfloor n^{1/b} \rfloor$.
$B_n \le n^{1/3} + n^{1/4} + \dots + n^{1/\lfloor \log_2 n \rfloor}$.
$B_n \le n^{1/3} + (\log_2 n) n^{1/4}$.
So $B_n = O(n^{1/3})$.
Thus, $A_n = \sqrt{n} + O(n^{1/3})$.

This implies that $A_n \sim \sqrt{n}$ as $n\to\infty$. That is, $\lim_{n\to\infty} \frac{A_n}{\sqrt{n}} = 1$.

Now consider the $k$-th perfect power $s_k$. We have $A_{s_k}=k$. Since $s_k \to \infty$ as $k\to\infty$, we have:
$k \sim \sqrt{s_k}$.
This implies $s_k \sim k^2$. That is, $\lim_{k\to\infty} \frac{s_k}{k^2} = 1$.

Now we prove that $s_{k+1}-s_k \ge k$ for infinitely many $k$ by contradiction.
Suppose that there are only finitely many such $k$. Then there exists an integer $K$ such that for all $k \ge K$, we have $s_{k+1}-s_k < k$.

Let $m$ be an integer such that $m > K$. We sum the gaps from $K$ to $m-1$:
$s_m - s_K = \sum_{k=K}^{m-1} (s_{k+1}-s_k) < \sum_{k=K}^{m-1} k$.
The sum on the right is the sum of an arithmetic progression:
$\sum_{k=K}^{m-1} k = \sum_{k=1}^{m-1} k - \sum_{k=1}^{K-1} k = \frac{(m-1)m}{2} - \frac{(K-1)K}{2} = \frac{m^2-m}{2} - C_K'$, where $C_K'$ is a constant depending on $K$.

So, $s_m < \frac{1}{2}m^2 - \frac{1}{2}m + C_K$, where $C_K = s_K - C_K'$ is a constant.

Now we examine the ratio 

[Note: response truncated to first 3000 characters of 4330]
