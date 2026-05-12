# artifact_019

Grading ID: GB-0333  
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

We are looking for all functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ such that
$$yf(yf(x)+1) = f\left(\frac{1}{x} + f(y)\right) \quad (*)$$
for all $x, y \in \mathbb{R}^+$. Let $P(x, y)$ be the assertion $(*)$.

Step 1: Verification of the candidate solution $f(x)=1/x$.
LHS: $y f(y(1/x)+1) = y f(y/x+1) = y \frac{1}{y/x+1} = y \frac{x}{y+x} = \frac{xy}{x+y}$.
RHS: $f(1/x+1/y) = \frac{1}{1/x+1/y} = \frac{xy}{x+y}$.
Since LHS=RHS, $f(x)=1/x$ is a solution.

Step 2: Proving that if $f$ is injective, then $f(x)=1/x$.
$P(x, 1) \implies 1 \cdot f(1 \cdot f(x)+1) = f(1/x+f(1))$.
Let $c=f(1)$. $c>0$.
$f(f(x)+1) = f(1/x+c)$.
If $f$ is injective, then $f(x)+1 = 1/x+c$.
$f(x) = 1/x + k$, where $k=c-1$.
Since $f(x)>0$ for all $x>0$. As $x\to\infty$, $1/x\to 0$, so we must have $k \ge 0$.

Substitute this form into $(*)$:
LHS: $y f(y(1/x+k)+1) = y f(y/x+ky+1) = y \left(\frac{1}{y/x+ky+1} + k\right)$.
LHS $= y \left(\frac{x}{y+kxy+x} + k\right) = \frac{xy}{x+y+kxy} + ky$.
RHS: $f(1/x+1/y+k) = \frac{1}{1/x+1/y+k} + k = \frac{xy}{x+y+kxy} + k$.
Equating LHS and RHS gives $ky=k$ for all $y \in \mathbb{R}^+$.
This implies $k(y-1)=0$ for all $y$. Thus $k=0$.
So, if $f$ is injective, then $f(x)=1/x$.

Step 3: Proving that if $f$ is surjective, then $f$ is injective.
Assume $f$ is surjective. The range of $f$ is $R_f=(0, \infty)$.
Suppose $f(x_1)=f(x_2)$ for some $x_1, x_2 \in \mathbb{R}^+$.
$P(x_1, y) \implies yf(yf(x_1)+1) = f(1/x_1+f(y))$.
$P(x_2, y) \implies yf(yf(x_2)+1) = f(1/x_2+f(y))$.
The LHS are equal, so $f(1/x_1+f(y)) = f(1/x_2+f(y))$.
Let $A=1/x_1$ and $B=1/x_2$. Since $f$ is surjective, $z=f(y)$ spans $(0, \infty)$.
$f(A+z)=f(B+z)$ for all $z>0$.
If $x_1 \ne x_2$, then $A \ne B$. Let $T=|A-B|>0$.
Let $B_0 = \min(A, B)$. Then $f(w+T)=f(w)$ for all $w>B_0$.
The function $f$ is eventually periodic with period $T$.

Let $c=f(1)$. $P(1, y) \implies yf(cy+1) = f(1+f(y))$.
Since $f$ is eventually periodic, there exists $Y$ such that for all $y>Y$, $f(y+T)=f(y)$. We can also ensure $cy+1>B_0$.
Consider $P(1, y+T)$ for $y>Y$.
$(y+T)f(c(y+T)+1) = f(1+f(y+T))$.
Since $f(y+T)=f(y)$, the RHS are equal for $P(1, y)$ and $P(1, y+T)$.
$yf(cy+1) = (y+T)f(cy+cT+1)$.
Let $x=cy+1$. For sufficiently large $x$ (since $y>Y$). $y=(x-1)/c$.
$\frac{x-1}{c} f(x) = \left(\frac{x-1}{c}+T\right) f(x+cT) = \frac{x-1+cT}{c} f(x+cT)$.
$(x-1)f(x) = (x-1+cT)f(x+cT)$. (R)

We use the periodicity $f(x+T)=f(x)$ for large $x$. We evaluate $f(x+cT+T)$ in two ways for sufficiently large $x$.
1) $f(x+cT+T) = f((x+cT)+T)$. Since $x+cT$ is large, by periodicity this is $f(x+cT)$.
Using (R), $f(x+cT) = \frac{x-1}{x-1+cT} f(x)$.
2) $f(x+cT+T) = f((x+T)+cT)$. Let $x'=x+T$. Using (R) at $x'$ (which is large):
$f(x'+cT) = \frac{x'-1}{x'-1+cT} f(x')$.
Since $x$ is large, $f(x')=f(x+T)=f(x)$.
So $f((x+T)+cT) = \frac{x+T-1}{x+T-1+cT} f(x)$.

Equating the two expressions, and since $f(x)>0$:
$\frac{x-1}{x-1+cT} = \frac{x+T-1}{x+T-1+cT}$.
Let $u=x-1$. $\frac{u}{u+cT} = \frac{u+T}{u+T+cT}$.
$u(u+T+cT) = (u+T)

[Note: response truncated to first 3000 characters of 4507]
