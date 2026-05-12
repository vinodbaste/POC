# artifact_047

Grading ID: GB-0439  
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

Here is a detailed proof of the inequality.

We are given $n \geq 2$, and positive real numbers $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$ such that $\prod_{k=1}^{n} a_{k}=1$.
We define $b_{k}=2^{k}\left(1+a_{k}^{2^{k}}\right)$. We want to prove:
\[ \sum_{k=1}^{n} \frac{1}{b_{k}} \geq \frac{1}{2}-\frac{1}{2^{n+1}} \]

**Step 1: Transform the inequality**

The right-hand side (RHS) is a geometric series sum:
\[ \frac{1}{2}-\frac{1}{2^{n+1}} = \frac{1}{2}\left(1-\frac{1}{2^n}\right) = \sum_{k=1}^{n} \frac{1}{2^{k+1}} \]
Let $x_k = a_k^{2^k}$. Then $b_k = 2^k(1+x_k)$. The inequality becomes:
\[ \sum_{k=1}^{n} \frac{1}{2^k(1+x_k)} \geq \sum_{k=1}^{n} \frac{1}{2^{k+1}} \]
We can rewrite the terms in the sum using the identity $\frac{1}{1+x} = \frac{1}{2} - \frac{x-1}{2(x+1)}$.
\[ \frac{1}{2^k(1+x_k)} = \frac{1}{2^k} \left( \frac{1}{2} - \frac{x_k-1}{2(x_k+1)} \right) = \frac{1}{2^{k+1}} - \frac{1}{2^{k+1}} \frac{x_k-1}{x_k+1} \]
Summing over $k=1$ to $n$:
\[ \sum_{k=1}^{n} \frac{1}{b_k} = \sum_{k=1}^{n} \frac{1}{2^{k+1}} - \sum_{k=1}^{n} \frac{1}{2^{k+1}} \frac{x_k-1}{x_k+1} \]
The inequality holds if and only if the second sum (let's call it $T_n$) is less than or equal to 0:
\[ T_n = \sum_{k=1}^{n} \frac{1}{2^{k+1}} \frac{x_k-1}{x_k+1} \leq 0 \]

**Step 2: Logarithmic transformation and constraints**

Let $c_k = \ln a_k$. The constraints on $a_k$ translate to:
1. $c_1 \leq c_2 \leq \cdots \leq c_n$.
2. $\sum_{k=1}^n c_k = 0$.

From these constraints, it follows that $c_1 \leq 0$ (since if all $c_k>0$, the sum would be positive) and $c_n \geq 0$.

Now we express $x_k$ in terms of $c_k$: $x_k = a_k^{2^k} = e^{2^k c_k}$.
The term $\frac{x_k-1}{x_k+1}$ can be written using the hyperbolic tangent function:
\[ \frac{x_k-1}{x_k+1} = \frac{e^{2^k c_k}-1}{e^{2^k c_k}+1} = \tanh\left(\frac{2^k c_k}{2}\right) = \tanh(2^{k-1} c_k) \]

Let $d_k = 2^{k-1} c_k$. The inequality $T_n \leq 0$ becomes:
\[ T_n = \sum_{k=1}^{n} \frac{1}{2^{k+1}} \tanh(d_k) = \frac{1}{4} \sum_{k=1}^{n} \frac{1}{2^{k-1}} \tanh(d_k) \leq 0 \]
It is sufficient to prove $S_n = \sum_{k=1}^{n} \frac{1}{2^{k-1}} \tanh(d_k) \leq 0$. (Note: The definition of $S_n$ here differs slightly from the thought block for convenience).

The constraints on $d_k$ are:
1. $c_k = d_k/2^{k-1}$. The ordering $c_k \leq c_{k+1}$ means $\frac{d_k}{2^{k-1}} \leq \frac{d_{k+1}}{2^k}$, or $2d_k \leq d_{k+1}$.
2. The sum constraint: $A_n = \sum_{k=1}^n c_k = \sum_{k=1}^n \frac{d_k}{2^{k-1}} = 0$.
3. $d_1 = c_1 \leq 0$.

**Step 3: Auxiliary Lemma**

We will use an auxiliary lemma related to weighted Jensen's inequality for the $\tanh$ function.

**Lemma:** Let $w_1, \dots, w_m$ be positive weights. Let $d'_1, \dots, d'_m$ be real numbers. Define $A = \sum_{k=1}^m w_k d'_k$ and $W = \sum_{k=1}^m w_k$. If $A \geq 0$, then
\[ \sum_{k=1}^m w_k \tanh(d'_k) \leq W \tanh(A/W) \]
This lemma holds because $\tanh(x)$ is concave for $x \geq 0$. If all $d'_k \geq 0$, it is Jensen's inequality. If some $d'_k < 0$, the inequality stil

[Note: response truncated to first 3000 characters of 6958]
