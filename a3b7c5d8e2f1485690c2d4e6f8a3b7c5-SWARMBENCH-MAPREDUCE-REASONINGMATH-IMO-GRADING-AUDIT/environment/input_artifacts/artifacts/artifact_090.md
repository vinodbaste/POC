# artifact_090

Grading ID: GB-0424  
Problem ID: PB-Advanced-013  
Source: Novel Problem  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

For an integer $n \geq 2$, let $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$ be positive real numbers satisfying $a_{1} a_{2} \cdots a_{n}=1$. For each $k=1,2, \cdots, n$, define $b_{k}=2^{k}\left(1+a_{k}^{2^{k}}\right)$. Prove that the following inequality holds:

 \[
 \frac{1}{2}-\frac{1}{2^{n+1}} \leq \frac{1}{b_{1}}+\frac{1}{b_{2}}+\cdots+\frac{1}{b_{n}}
 \]

## Reference Solution (for grader's calibration)

The following Lemma is often used in problems involving multiple variables or sequences.

 <Lemma> For positive real numbers $x, y$ satisfying $xy \geq 1$, the following inequality holds:

 \[
 \frac{1}{1+x}+\frac{1}{1+y} \geq \frac{2}{1+\sqrt{x y}}
 \]

 <Proof of Lemma> The proof is a simple calculation. Multiplying both sides by $(1+\sqrt{x y})(1+x)(1+y)$, the given inequality simplifies to $(\sqrt{x y}-1)(\sqrt{x}-\sqrt{y})^{2} \geq 0$, which holds trivially under the condition $x y \geq 1$. Therefore, the inequality is proven.\qed

 Now, let's prove the main problem. We will prove by induction that the following inequality holds for each $k=n, n-1, \cdots, 1$:

 \begin{equation*}
 \frac{1}{2^{n+1}}+\frac{1}{b_{n}}+\frac{1}{b_{n-1}}+\cdots+\frac{1}{b_{k}} \geq \frac{1}{2^{k-1}} \frac{1}{1+\left(a_{n} a_{n-1} \cdots a_{k}\right)^{2^{k-1}}} \tag{1.1}
 \end{equation*}

 In particular, if this inequality holds for $k=1$, then the inequality in the problem is proven due to the condition $a_{1} a_{2} \cdots a_{n}=1$.
 <Step 1> First, for $k=n$, since $a_{n} \geq 1$, we obtain the following by <Lemma>:

 \[
 \frac{1}{2^{n+1}}+\frac{1}{b_{n}}=\frac{1}{2^{n}}\left(\frac{1}{1+1}+\frac{1}{1+a_{n}^{2^{n}}}\right) \geq \frac{1}{2^{n-1}} \frac{1}{1+a_{n}^{2^{n-1}}}
 \]

 Therefore, (1.1) holds.

 <Step 2> Next, let's prove that if (1.1) holds for $k=m$, then it also holds for $k=m-1$ (where $2 \leq m \leq n$).

 <Step 2.1> First, by the induction hypothesis, we obtain the following inequality:

 \[
 \frac{1}{2^{n+1}}+\frac{1}{b_{n}}+\frac{1}{b_{n-1}}+\cdots+\frac{1}{b_{m}}+\frac{1}{b_{m-1}} \geq \frac{1}{2^{m-1}}\left[\frac{1}{1+\left(a_{n} a_{n-1} \cdots a_{m}\right)^{2^{m-1}}}+\frac{1}{1+a_{m-1}^{2_{m-1}^{m}}}\right]
 \]

 <Step 2.2> By the condition of the problem,

 \[
 \left(a_{n} a_{n-1} \cdots a_{m}\right)^{2^{m-1}} \cdot a_{m-1}^{2^{m-1}} \geq 1
 \]

 Therefore, by <Lemma>,

 \[
 \frac{1}{2^{m-1}}\left[\frac{1}{1+\left(a_{n} a_{n-1} \cdots a_{m}\right)^{2^{m-1}}}+\frac{1}{1+a_{m-1}^{2^{m-1}}}\right] \geq \frac{1}{2^{m-2}} \frac{1}{1+\left(a_{n} a_{n-1} \cdots a_{m} a_{m-1}\right)^{2^{m-2}}}
 \]

 This confirms that inequality (1.1) also holds for $k=m-1$.

 In conclusion, by mathematical induction, (1.1) holds for $k=1$, completing the proof.

## Grading Guidelines

(Partial)
 1. Tried to apply induction in an appropriate direction.
 2. Found any localization inequality, e.g., the one equivalent to the Lemma of solution.
 (Almost)
 1. Verification contains minor mistakes only.

## Candidate Response (to be graded)

We are asked to prove the inequality
\[
 \frac{1}{2}-\frac{1}{2^{n+1}} \leq \frac{1}{b_{1}}+\frac{1}{b_{2}}+\cdots+\frac{1}{b_{n}}
\]
where $b_{k}=2^{k}\left(1+a_{k}^{2^{k}}\right)$, given that $0 < a_{1} \leq a_{2} \leq \cdots \leq a_{n}$ are positive real numbers satisfying $a_{1} a_{2} \cdots a_{n}=1$.

First, we recognize the left-hand side (LHS) as the sum of a geometric progression:
\[
\text{LHS} = \frac{1}{2}\left(1-\frac{1}{2^n}\right) = \sum_{k=1}^{n} \frac{1}{2^{k+1}}.
\]

We introduce a change of variables by letting $a_k = e^{z_k}$ for $k=1, \dots, n$. The conditions on $a_k$ translate to conditions on $z_k$:
1. $a_1 \leq a_2 \leq \cdots \leq a_n \implies z_1 \leq z_2 \leq \cdots \leq z_n$.
2. $\prod_{k=1}^n a_k = 1 \implies \sum_{k=1}^n z_k = 0$.

Now we analyze the terms $1/b_k$.
\[
\frac{1}{b_k} = \frac{1}{2^k(1+a_k^{2^k})} = \frac{1}{2^k(1+e^{2^k z_k})}.
\]
We use the identity $\frac{1}{1+e^X} = \frac{1}{2}(1-\tanh(X/2))$. Let $X=2^k z_k$. Then $X/2 = 2^{k-1} z_k$.
\[
\frac{1}{b_k} = \frac{1}{2^k} \cdot \frac{1}{2} \left(1-\tanh(2^{k-1}z_k)\right) = \frac{1}{2^{k+1}} \left(1-\tanh(2^{k-1}z_k)\right).
\]
The sum on the right-hand side (RHS) of the inequality is:
\[
\sum_{k=1}^n \frac{1}{b_k} = \sum_{k=1}^n \frac{1}{2^{k+1}} - \sum_{k=1}^n \frac{1}{2^{k+1}} \tanh(2^{k-1}z_k).
\]
The desired inequality is equivalent to:
\[
\sum_{k=1}^n \frac{1}{2^{k+1}} \leq \sum_{k=1}^n \frac{1}{2^{k+1}} - \sum_{k=1}^n \frac{1}{2^{k+1}} \tanh(2^{k-1}z_k).
\]
This simplifies to proving that
\[
T_n = \sum_{k=1}^n \frac{1}{2^{k+1}} \tanh(2^{k-1}z_k) \leq 0.
\]

Let $w_k = \frac{1}{2^{k+1}}$ and $u_k = 2^{k-1}z_k$. We want to prove $T_n = \sum_{k=1}^n w_k \tanh(u_k) \leq 0$.

If all $a_k=1$, then all $z_k=0$, so $u_k=0$. $T_n=0$, and the inequality holds with equality.

Suppose not all $a_k$ are 1. Since $z_1 \leq \cdots \leq z_n$ and $\sum z_k = 0$, we must have $z_1 < 0$ and $z_n > 0$. There exists an index $m \in \{1, 2, \dots, n-1\}$ such that $z_k \leq 0$ for $k=1, \dots, m$ and $z_k > 0$ for $k=m+1, \dots, n$.
Consequently, $u_k \leq 0$ for $k=1, \dots, m$ and $u_k > 0$ for $k=m+1, \dots, n$.

Let $N=\{1, \dots, m\}$ and $P=\{m+1, \dots, n\}$. We split the sum $T_n$ into two parts:
\[
S_- = \sum_{k \in N} w_k \tanh(u_k), \quad S_+ = \sum_{k \in P} w_k \tanh(u_k).
\]
We analyze the function $\phi(x)=\tanh(x)$. Its second derivative is $\phi''(x) = -2\text{sech}^2(x)\tanh(x)$.
For $x>0$, $\phi''(x)<0$, so $\phi(x)$ is strictly concave on $[0, \infty)$.
For $x<0$, $\phi''(x)>0$, so $\phi(x)$ is strictly convex on $(-\infty, 0]$.

We apply Jensen's inequality. Let $W_- = \sum_{k \in N} w_k$ and $W_+ = \sum_{k \in P} w_k$.

For $S_+$, since $u_k > 0$ for $k \in P$, we use the concavity of $\tanh(x)$:
\[
S_+ = W_+ \sum_{k \in P} \frac{w_k}{W_+} \tanh(u_k) \leq W_+ \tanh\left(\frac{1}{W_+} \sum_{k \in P} w_k u_k\right).
\]
For $S_-$, since $u_k \leq 0$ for $k \in N$, we use the convexity of $\tanh(x)$:
\[
S_- = W_- \sum_{k \in N} \frac{w_k}{W_-} \tanh(u_

[Note: response truncated to first 3000 characters of 5245]
