# artifact_026

Grading ID: GB-0438  
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

The inequality we want to prove is
\[
 \frac{1}{b_{1}}+\frac{1}{b_{2}}+\cdots+\frac{1}{b_{n}} \geq \frac{1}{2}-\frac{1}{2^{n+1}}
\]
where $b_{k}=2^{k}\left(1+a_{k}^{2^{k}}\right)$.
The right hand side is the value of the left hand side when $a_k=1$ for all $k$.
Let $S$ be the left hand side. The inequality is equivalent to
\[
 S - \sum_{k=1}^n \frac{1}{2^{k+1}} \geq 0
\]
\[
 \sum_{k=1}^n \left( \frac{1}{2^k(1+a_k^{2^k})} - \frac{1}{2^{k+1}} \right) = \sum_{k=1}^n \frac{1}{2^{k+1}} \frac{1-a_k^{2^k}}{1+a_k^{2^k}} \geq 0
\]
Let $x_k = a_k^{2^k}$. The condition $\prod a_k = 1$ becomes $\prod x_k^{1/2^k} = 1$.
Let $y_k = \ln x_k = 2^k \ln a_k$. The condition becomes $\sum_{k=1}^n y_k/2^k = 0$.
The inequality becomes
\[
 \sum_{k=1}^n \frac{1}{2^{k+1}} \frac{1-e^{y_k}}{1+e^{y_k}} \geq 0
\]
Let $g(y) = \frac{1-e^y}{1+e^y} = -\tanh(y/2)$. We want to prove $\sum_{k=1}^n \frac{g(y_k)}{2^{k+1}} \geq 0$.
Let $h(y) = g(y) + y/2$. The sum is
\[
 \sum_{k=1}^n \frac{h(y_k)-y_k/2}{2^{k+1}} = \sum_{k=1}^n \frac{h(y_k)}{2^{k+1}} - \frac{1}{4} \sum_{k=1}^n \frac{y_k}{2^k} = \sum_{k=1}^n \frac{h(y_k)}{2^{k+1}}
\]
since $\sum y_k/2^k = 0$. We want to prove $S(y) = \sum_{k=1}^n \frac{h(y_k)}{2^{k+1}} \geq 0$.

The function $h(y) = y/2 - \tanh(y/2)$ is an odd function.
Its derivative is $h'(y) = 1/2 - 1/2 \text{sech}^2(y/2) = 1/2 \tanh^2(y/2) \geq 0$.
So $h(y)$ is increasing. $h(y)>0$ for $y>0$ and $h(y)<0$ for $y<0$.
The constraints on $a_k$ are $a_1 \leq \dots \leq a_n$. This translates to $y_k/2^k \leq y_{k+1}/2^{k+1}$.
Let $u_k = y_k/2^k$. We have $u_1 \leq \dots \leq u_n$ and $\sum u_k = 0$.
The expression becomes
\[
 S(u) = \sum_{k=1}^n \frac{h(2^k u_k)}{2^{k+1}} = \frac{1}{2} \sum_{k=1}^n G_k(u_k)
\]
where $G_k(x) = h(2^k x)/2^k$.

Let's analyze the convexity of $h(y)$. $h''(y) = 1/4 \text{sech}^2(y/2) \tanh(y/2)$.
$h''(y)>0$ for $y>0$ and $h''(y)<0$ for $y<0$.
So $h(y)$ is convex for $y>0$ and concave for $y<0$.
Since $G_k(x)$ is a scaled version of $h(x)$, it has the same convexity/concavity properties.

Let $m$ be the index such that $u_m \leq 0$ and $u_{m+1} \geq 0$.
Let $N=\{1, \dots, m\}$ and $P=\{m+1, \dots, n\}$.
$S(u) = \frac{1}{2} \left( \sum_{k \in P} G_k(u_k) + \sum_{k \in N} G_k(u_k) \right)$.

For $k \in P$, $u_k \geq 0$, so $G_k(u_k)$ are convex.
For $k \in N$, $u_k \leq 0$, so $G_k(u_k)$ are concave.

Let's consider $n=2$. $u_1 \leq u_2$ and $u_1+u_2=0$. So $u_1 \leq 0$ and $u_2 \geq 0$. $u_2=-u_1$.
$2S = G_1(u_1) + G_2(u_2) = G_1(-u_2) + G_2(u_2)$.
$G_1(-x) = h(2(-x))/2 = -h(2x)/2$. $G_2(x) = h(4x)/4$.
$2S = h(4x)/4 - h(2x)/2$. We want this to be $\geq 0$ for $x \geq 0$.
$h(4x) \geq 2h(2x)$.
Let $H(x) = h(x)$ for $x \geq 0$. $H(x)$ is convex and $H(0)=0$, so $H(x)/x$ is increasing.
$H(4x)/(4x) \geq H(2x)/(2x)$, so $H(4x) \geq 2H(2x)$.

Let's generalize this. We use the superadditivity property $H(x+y) \geq H(x)+H(y)$ which is true for convex functions with $H(0)=0$.

Let's try to prove that the minimum is attained when $u_k=0$ for all $k$.
Since 

[Note: response truncated to first 3000 characters of 7632]
