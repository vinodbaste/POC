# artifact_060

Grading ID: GB-0336  
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

Outcome 2: STRUCTURED PARTIAL PROGRESS & ANALYSIS

We are looking for functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ satisfying:
$$yf(yf(x)+1) = f\left(\frac{1}{x} + f(y)\right) \quad (*)$$
Let $P(x, y)$ denote the assertion $(*)$. Let $R_f$ be the range of $f$.

We verified that $f(x) = 1/x$ is a solution.

### Proven Lemmas and Key Results

**Lemma 1: If $f$ is injective, then $f(x) = 1/x$.**

*Proof:* Let $c = f(1)$. $P(x, 1) \implies f(f(x)+1) = f(1/x + c)$. If $f$ is injective, $f(x)+1 = 1/x+c$. Thus $f(x) = 1/x + A$, where $A=c-1$. Since $f(x)>0$ for all $x>0$, we must have $A \ge 0$.
Substituting $f(x)=1/x+A$ into $(*)$:
LHS $= y f(y(1/x+A)+1) = y (\frac{1}{y/x+Ay+1} + A) = \frac{xy}{x+y+Axy} + Ay$.
RHS $= f(1/x + 1/y+A) = \frac{1}{1/x+1/y+A} + A = \frac{xy}{x+y+Axy} + A$.
Equating LHS and RHS gives $Ay = A$ for all $y \in \mathbb{R}^+$. Thus $A=0$, and $f(x)=1/x$.

**Lemma 2: The range of $f$ satisfies $\inf R_f = 0$ and $\sup R_f = \infty$.**

*Proof:* Let $m = \inf R_f$. Suppose $m>0$. Then $f(t) \ge m$ for all $t$.
Fix $x$ and let $z=f(x)$. $P(x, y) \implies y f(yz+1) = f(1/x+f(y)) \in R_f$.
$y f(yz+1) \ge y m$. As $y\to\infty$, $y m \to \infty$. Thus $\sup R_f = \infty$.

Let $A \in R_f$. $P(x_A, y)$ where $f(x_A)=A$. $y f(Ay+1) \ge m$. $f(Ay+1) \ge m/y$.
Let $t=Ay+1$. $y=(t-1)/A$. $f(t) \ge \frac{mA}{t-1}$ for all $t>1$.
For $t=2$, $f(2) \ge mA$. Since $\sup R_f = \infty$, we can choose $A \in R_f$ arbitrarily large. This implies $f(2)$ is arbitrarily large, a contradiction. Thus $m=0$. $\inf R_f = 0$.

Since $\inf R_f = 0$, there exists $x_n$ such that $A_n = f(x_n) \to 0$. Let $y_n = 1/A_n \to \infty$.
$P(x_n, y_n) \implies y_n f(y_n f(x_n)+1) = y_n f(1+1) = y_n f(2)$.
Since $f(2)>0$, $LHS \to \infty$. The LHS equals $f(1/x_n + f(y_n)) \in R_f$. Thus $\sup R_f = \infty$.

**Lemma 3: If $L^+ = \limsup_{t\to 1^+} f(t)$ is finite, then $f$ is injective.**

*Proof:* Suppose $f(y_1) = f(y_2)$. Comparing $P(x, y_1)$ and $P(x, y_2)$ yields:
$y_1 f(y_1 f(x)+1) = y_2 f(y_2 f(x)+1)$.
Let $z=f(x) \in R_f$. $y_1 f(y_1 z+1) = y_2 f(y_2 z+1)$ for all $z \in R_f$.
Assume $y_1 \ne y_2$. WLOG, let $k = y_2/y_1 > 1$.
$f(y_1 z+1) = k f(y_2 z+1)$ for $z \in R_f$.

By Lemma 2, $\inf R_f = 0$. We can choose sequences $z_n \in R_f$ such that $z_n \to 0$.
Let $t_n(z) = y_1 z+1$ and $s_n(z) = y_2 z+1$. Both tend to $1^+$ as $z\to 0$.

Assume $L^+ < \infty$. Since $f(1)>0$, $L^+>0$.
We can choose a sequence $z_n \to 0$ in $R_f$ such that $f(t_n(z_n)) \to L^+$.
Then $f(s_n(z_n)) = f(t_n(z_n))/k \to L^+/k$.
We can also choose a sequence $z'_n \to 0$ in $R_f$ such that $f(s_n(z'_n)) \to L^+$.
Then $f(t_n(z'_n)) = k f(s_n(z'_n)) \to k L^+$.
$k L^+$ is a limit point of $f(t)$ as $t\to 1^+$.
Since $k>1$ and $L^+>0$, $k L^+ > L^+$. This contradicts $L^+ = \limsup_{t\to 1^+} f(t)$.
Therefore, we must have $k=1$, so $y_1=y_2$. $f$ is injective.

### Identification of the Crux

The key to solving the problem is proving injectivity. We have rigorously shown that if $\li

[Note: response truncated to first 3000 characters of 3922]
