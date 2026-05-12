# artifact_120

Grading ID: GB-0006  
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

Let $S$ be the set of perfect powers, $S = \{a^b : a \ge 1, b \ge 2\}$. Let $s_1 < s_2 < \dots$ be the elements of $S$ in increasing order.
$A_n$ is the number of perfect powers less than or equal to $n$.
If $n \in [s_k, s_{k+1}-1]$, then $A_n = k$.

We want to find infinitely many $n$ such that $A_n | n+2024$.
Let $k$ be a positive integer. We look for $n$ in the interval $I_k = [s_k, s_{k+1}-1]$. For such $n$, $A_n=k$.
The condition $A_n | n+2024$ becomes $k | n+2024$, which is $n \equiv -2024 \pmod k$.

The interval $I_k$ has length $L_k = s_{k+1}-s_k$.
If $L_k \ge k$, then $I_k$ contains a complete set of residues modulo $k$. Thus, there exists $n \in I_k$ such that $n \equiv -2024 \pmod k$.

We need to show that $s_{k+1}-s_k \ge k$ for infinitely many $k$.

First, we analyze the asymptotic behavior of $A_n$. The number of perfect powers up to $n$ is dominated by the number of squares, so $A_n \sim \sqrt{n}$.
More precisely, $A_n = \sqrt{n} + O(n^{1/3})$.

Let's look at $s_k$. Since $k = A_{s_k}$, we have $k = \sqrt{s_k} + O(s_k^{1/3})$.
This implies $s_k \sim k^2$.

We can establish a bound on $s_k$.
$k = A_{s_k} \ge \lfloor \sqrt{s_k} \rfloor$. So $k \ge \sqrt{s_k}$ if $s_k$ is a square, or $k \ge \sqrt{s_k}-1$.
In any case, $s_k \le (k+1)^2$.

Also, $A_n \le \sqrt{n} + C n^{1/3} \log n$ for some constant $C$.
$k = A_{s_k} \le \sqrt{s_k} + C s_k^{1/3} \log s_k$.
Using $s_k \approx k^2$, we get $\sqrt{s_k} \ge k - O(k^{2/3} \log k)$.
$s_k \ge k^2 - O(k^{5/3} \log k)$.

Suppose for the sake of contradiction that there is $K$ such that for all $k \ge K$, $s_{k+1}-s_k < k$.
$s_{k+1}-s_k \le k-1$.
For $k>K$, we have
$s_k = s_K + \sum_{j=K}^{k-1} (s_{j+1}-s_j) \le s_K + \sum_{j=K}^{k-1} (j-1) = s_K + \frac{(k-1)k}{2} - \frac{(K-1)K}{2}$.
$s_k \le \frac{1}{2}k^2 - \frac{1}{2}k + C_K$, where $C_K$ is a constant depending on $K$.

For large $k$, $s_k \le \frac{1}{2}k^2 + O(k)$.

However, we found that $s_k = k^2 - O(k^{5/3} \log k)$.
So we must have $k^2 - O(k^{5/3} \log k) \le \frac{1}{2}k^2 + O(k)$.
$\frac{1}{2}k^2 \le O(k^{5/3} \log k)$.
Dividing by $k^{5/3}$, we get $\frac{1}{2}k^{1/3} \le O(\log k)$.
This is false for large $k$ because $k^{1/3}$ grows faster than $\log k$.

Thus, the assumption that $s_{k+1}-s_k < k$ for all $k \ge K$ is false.
Therefore, there are infinitely many $k$ such that $s_{k+1}-s_k \ge k$.

For each such $k$, the interval $I_k = [s_k, s_{k+1}-1]$ has length at least $k$, so it contains an element $n_k$ such that $n_k \equiv -2024 \pmod k$.
For this $n_k$, $A_{n_k}=k$, so $k | n_k+2024$.

Since $s_k \to \infty$ as $k \to \infty$, the values of $n_k$ are also increasing (as $n_k \ge s_k$), so we have found infinitely many distinct values of $n$ satisfying the condition.

Final Answer: The final answer is $\boxed{Infinitely many n}$
<ctrl100>
