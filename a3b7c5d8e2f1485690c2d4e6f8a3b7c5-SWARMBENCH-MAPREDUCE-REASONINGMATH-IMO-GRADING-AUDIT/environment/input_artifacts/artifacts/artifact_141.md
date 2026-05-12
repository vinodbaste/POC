# artifact_141

Grading ID: GB-0348  
Problem ID: PB-Advanced-011  
Source: Novel Problem  
IMO Area: Number_Theory

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Find all functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ such that $$yf(yf(x)+1) = f(\frac{1}{x} + f(y))$$ for all $x, y \in \mathbb{R}^+$

## Reference Solution (for grader's calibration)


Let $P(x,y)$ be the given assertion.
$$P(c+1, \frac{c}{f(c+1)}): \quad c= \frac{c}{f(c+1)} f(\frac{c}{f(c+1)} \times f(c+1)+1)= f(\frac{1}{c+1} + f(\frac{c}{f(c+1)}))$$, hence $f$ is surjective. \\ Now assume that $f(x) = f(b)$ for some $a>b>0$. Since $f$ is surjective, there exists some $t\in \mathbb{R}^+$ such that $f(t)=1$. comparing $P(a,t)$ and $f(b,t)$ gives $f(1+\frac{1}{a}) = f(1+\frac{1}{b})$. Again since $f$ is surjective, there exists some $t\in \mathbb{R}^+$ such that $f(t)=\frac{1}{ab}$. Comparing $P(s,a)$ and $P(s,b)$ gives $af(\frac{1}{b} +1) = b f(\frac{1}{a}+1)$, which is a contradiction. Therefore $f$ is injective. \\
Now $P(x,1)$ implies $f(x) = \frac{1}{x}+c$, and by surjectivity, $c=0$, thus $f(x) = \frac{1}{x}$, which is indeed a solution.


## Grading Guidelines

(Partial)
 1. Considered $(x,y) = (c+1, \frac{c}{f(c+1)})$.
 2. Proved that $f$ is subjective.
(Almost)
 1. Proved that $f$ is injective.

## Candidate Response (to be graded)

We are looking for all functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ such that for all $x, y \in \mathbb{R}^+$,
$$yf(yf(x)+1) = f(\frac{1}{x} + f(y)) \quad (*)$$
Let $P(x, y)$ be the assertion $yf(yf(x)+1) = f(\frac{1}{x} + f(y))$.

First, we test the function $f(x) = 1/x$.
LHS = $y f(y(1/x)+1) = y f(y/x+1) = y \frac{1}{y/x+1} = y \frac{x}{y+x} = \frac{xy}{x+y}$.
RHS = $f(\frac{1}{x} + f(y)) = f(\frac{1}{x} + \frac{1}{y}) = f(\frac{x+y}{xy}) = \frac{xy}{x+y}$.
LHS = RHS, so $f(x)=1/x$ is a solution.

We now prove it's the only solution.
Step 1: Prove that $f$ is injective.
Suppose for the sake of contradiction that $f$ is not injective. Then there exist $x_1, x_2 \in \mathbb{R}^+$ with $x_1 \neq x_2$ such that $f(x_1) = f(x_2)$.
Let $c = f(x_1) = f(x_2)$.
$P(x_1, y) \implies yf(yc+1) = f(\frac{1}{x_1} + f(y))$.
$P(x_2, y) \implies yf(yc+1) = f(\frac{1}{x_2} + f(y))$.
Therefore, $f(\frac{1}{x_1} + f(y)) = f(\frac{1}{x_2} + f(y))$ for all $y \in \mathbb{R}^+$.
Let $S = \mathrm{Im}(f)$ be the range of $f$. For any $z \in S$, there exists $y \in \mathbb{R}^+$ such that $f(y)=z$.
Let $u_1 = 1/x_1$ and $u_2 = 1/x_2$. Since $x_1 \neq x_2$, $u_1 \neq u_2$. Let's assume $u_1 > u_2$ without loss of generality. Let $T = u_1 - u_2 > 0$.
Then, for any $z \in S$, we have $f(u_1+z) = f(u_2+z)$, which can be written as $f(u_2+T+z) = f(u_2+z)$.

Let's see what happens in the original equation. Let $a, b \in \mathbb{R}^+$ with $a \neq b$ such that $f(a) = f(b)$.
$P(a, y) \implies yf(yf(a)+1) = f(1/a+f(y))$.
$P(b, y) \implies yf(yf(b)+1) = f(1/b+f(y))$.
Since $f(a)=f(b)$, the left hand sides are equal. Thus, for any $y \in \mathbb{R}^+$,
$f(1/a+f(y)) = f(1/b+f(y))$.
This must hold for any sequence of values $f(y_n)$. Let's choose $y_n$ such that $y_n \to \infty$.
Let's consider the RHS of the original equation. $f(1/x+f(y))$.
Let $x=a$ and $x=b$ and take an arbitrary $y_n \to \infty$.
$f(1/a + f(y_n)) = f(1/b + f(y_n))$.
The LHS of $(*)$ for $y=y_n$ is $y_n f(y_n f(x)+1)$. Let's use this.
$P(x, y_n) \implies y_n f(y_n f(x)+1) = f(1/x+f(y_n))$.
Let's choose $x=a$ and $x=b$.
$y_n f(y_n f(a)+1) = f(1/a+f(y_n))$.
$y_n f(y_n f(b)+1) = f(1/b+f(y_n))$.
The RHS are equal for any $y_n$, as we know. So LHS are equal.
$y_n f(y_n f(a)+1) = y_n f(y_n f(b)+1)$. Since $y_n>0$, $f(y_n f(a)+1) = f(y_n f(b)+1)$.
But we assumed $f(a)=f(b)$, so this is a tautology. This does not lead to a contradiction.

Let's use $f(1/a+z)=f(1/b+z)$ for all $z \in S$.
Let $x$ be any value. Let $y_n \to \infty$.
$P(x, y_n) \implies y_n f(y_n f(x)+1) = f(1/x + f(y_n))$.
Let $f(x)=c$. Then $y_n f(y_n c+1) = f(1/x+f(y_n))$.
Now let's use the non-injectivity property. For $f(a)=f(b)$ where $a \ne b$:
$f(1/a+z)=f(1/b+z)$ for all $z \in S$.
$P(a, y_n) \implies y_n f(y_n f(a)+1) = f(1/a+f(y_n))$.
$P(b, y_n) \implies y_n f(y_n f(b)+1) = f(1/b+f(y_n))$.
As $f(a)=f(b)$, we get $f(1/a+f(y_n))=f(1/b+f(y_n))$ for any $y_n$.
Let $z_n = f(y_n)$. The set of values $\{z_n\}$ is a subset of $S$. This is just a restateme

[Note: response truncated to first 3000 characters of 13280]
