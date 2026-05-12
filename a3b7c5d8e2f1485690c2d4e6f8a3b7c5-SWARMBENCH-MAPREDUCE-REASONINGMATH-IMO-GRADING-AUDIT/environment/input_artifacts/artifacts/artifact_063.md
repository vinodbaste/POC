# artifact_063

Grading ID: GB-0188  
Problem ID: PB-Advanced-006  
Source: Novel Problem  
IMO Area: Algebra

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Find all functions$f:\mathbb{Z}\rightarrow\mathbb{Z}$
 such that the equation
 \[
 f(x-f(xy))=f(x)f(1-y)
 \]
 holds for all $x,y\in\mathbb{Z}$.

## Reference Solution (for grader's calibration)

Let $P(x,y)$ be the assertion $f(x-f(xy))=f(x)f(1-y)$.

 If $f$ is constant, $f\equiv0$ or $f\equiv1$. From now on we will
 only consider non-constant functions.

 Claim 1 $f(f(x))=f(x)$ for all $x\in\mathbb{Z}$

 Proof. $P(0,y):f(-f(0))=f(0)f(1-y)\Longrightarrow f(0)=0$

 $P(x,0):f(x)=f(x)f(1)\Longrightarrow f(1)=1$

 $P(1,y):f(1-f(y))=f(1-y)$

 $P(1,1-y):f(1-f(1-y))=f(y)$

 $P(1,1-f(y)):f(y)=f(1-f(1-y))=f(1-f(1-f(y)))=f(f(y))\Longrightarrow f(f(x))=f(x)\forall x\in\mathbb{Z}\blacksquare$

 $\Longrightarrow P(x,1):f(x-f(x))=0$

 Now consider $f(\mathbb{Z})$.

 Case 1 $f(\mathbb{Z})\subset\{-1,0,1\}$

 Case 1.1. $f(\mathbb{Z})=\{0,1\}$

 We have $f(x)=1\textbackslash \Longrightarrow f(x-1)=0\textbackslash \Longrightarrow
 f(2-x)=1 \textbackslash \Longrightarrow f(1-x)=0$ and $f(1-x)=0
 \textbackslash \Longrightarrow f(x)=1$

 \[
 \therefore f(x)=1\Longleftrightarrow f(x-1)=0\Longleftrightarrow f(2-x)=1\Longleftrightarrow f(1-x)=0
 \]
 We can inductively prove that $f(x)=\begin{cases}
 0 & 2|x

 1 & 2\nmid x
 \end{cases}$

 Case 1.2. $f(\mathbb{Z})=\{-1,0,1\}\Longrightarrow f(-1)=-1$

 $P(1,x)$ and $P(-1,x)$ gives

 \begin{align*}
 f(x)=1 & \Longrightarrow f(1-x)=0,f(x+1)=-f(-2)

 f(x)=0 & \Longrightarrow f(1-x)=1,f(x+1)=1

 f(x)=-1 & \Longrightarrow f(1-x)=f(2),f(x+1)=0
 \end{align*}
 It's easy to see that $f(-2)=1,f(2)=-1$, and using this, we can inductively
 prove that $f(x)=\begin{cases}
 0 & 3|x

 1 & 3|x-1

 -1 & 3|x+1
 \end{cases}$

 Case 2. $f(\mathbb{Z})$ is not a subset of $\{-1,0,1\}$

 Case 2.1 $f(t)=1$ for some $2\mid t$

 \[
 P(2,\frac{t}{2}):1=f(1)=f(2)f(1-\frac{t}{2})
 \]

 Case 2.1.1 : $f(2)=1\Longrightarrow P(2,1):1=f(2)f(0)=0$. Contradiction!

 Case 2.1.2 : $f(2)=-1\Longrightarrow f(-1)=-1,f(1-\frac{t}{2})=-1$

 $P(-1,-x):f(-1-f(x))=-f(1+x)$

 $P(-1,-f(x)):f(-1-f(x))=f(-1-f(f(x)))=-f(1+f(x))\Longrightarrow f(1+x)=f(1+f(x))...(*)$

 Since $f(2)=-1$, so plugging this in $(*)$, we have

 \[
 f(2)=-1\Longrightarrow f(3)=0\Longrightarrow f(4)=1\Longrightarrow f(5)=-1\cdots
 \]
 We can prove inductively that$f(x)=\begin{cases}
 0 & 3|x

 1 & 3|x-1

 -1 & 3|x+1
 \end{cases}$ for all $x\in\mathbb{N}$.

 Plugging in $x=-1,y=-n(n\in\mathbb{N})$ gives $f(-1-n)=f(-1-f(n))=-f(1+n)$,
 so we have $f(x)=\begin{cases}
 0 & 3|x

 1 & 3|x-1

 -1 & 3|x+1
 \end{cases}$for all $x$, so contradiction since $f(\mathbb{Z})\in\{-1,0,1\}$.

 Case 2.2 $f(t)=1\Longrightarrow2\nmid t$

 Claim 2 $f(-1)=-1$ or $f(2)=0$

 Proof. Assume that $f(2)\neq0$

 We will prove that $f(t)=1\Longrightarrow f(1-t)=0$. $P(2,\frac{1-t}{2})$
 gives

 \[
 f(2)=f(2)f(\frac{t-3}{2})\Longrightarrow f(\frac{t-3}{2})=1
 \]
 We repeat this, then we get $t\equiv1(mod2^{n})$ for all $n\Longrightarrow t=1$.
 Note that

 \[
 f(-1)=c\Longrightarrow f(-1-c)=0\Longrightarrow f(c+2)=1
 \]
 Hence we conclude that $c=-1$.

 Case 2.2.1. $f(2)=0\Longrightarrow f(-1)=1$

 Define $n$ as the element of $f(\mathbb{Z})-\{-1,0,1\}$ which has
 the smallest absolute value. Then we have

 \[
 f(x-f(xy))=n\Longrightarrow\{f(x),f(1-y)\}=\{1,n\}\text{ or }\{f(x),f(1-y)\}=\{-1,-n\}...(\star)
 \]
 . Also note that $P(-n,- 1):f(-n-f(n))=0$, where $f(n)=n$ by Claim 1. Thus by $x=n,y=-2$ $(\star)\Longrightarrow f(3)=1$.
 Case 2.2.1. now becomes a repetition of Case 1.1, so contradiction!

 Case 2.2.2. $f(2)\neq0,f(-1)=-1,f(-2)=-f(2)$

 Claim 3 $f(n)=t\Longrightarrow n=t\forall t\leq1$

 Proof. We use induction on $t$. $t=1$ is already proven above. Assume
 that $t$ works.

 If $f(n)=t-1\Longrightarrow f(1+n)=f(1+f(n))=f(t)\Longrightarrow n=t-1$,
 so we're done.

 Use the same method to prove that $f(n)=n\forall n\leq1$, and $P(-1,n)(n>0)$
 gives $f(n+1)=-f(-n-1)=n+1$, so $f(n)=n$ for all $n\in\mathbb{Z}$.

## Grading Guidelines

(Partial)
 1. Proved $f(f(x))=f(x)$.
 2. Handled the case where $f\subseteq \{-1, 0, 1\}$.
 3. Handled the case where $f\not \subset \{-1, 0, 1\}$.
(Almost)
 1. Verification contains minor mistakes only.

## Candidate Response (to be graded)

We are looking for all functions $f:\mathbb{Z}\rightarrow\mathbb{Z}$ such that
 \[
 f(x-f(xy))=f(x)f(1-y) \quad (*)
 \]
 holds for all $x,y\in\mathbb{Z}$. Let $P(x,y)$ be the assertion $f(x-f(xy))=f(x)f(1-y)$.

1. Constant solutions.
If $f(x)=c$ for all $x$. Then $c = c^2$, so $c=0$ or $c=1$.
$f(x)=0$ is a solution: $0=0\cdot 0$.
$f(x)=1$ is a solution: $1=1\cdot 1$.

2. Non-constant solutions.
$P(0,y) \implies f(-f(0)) = f(0)f(1-y)$.
If $f(0)=c\neq 0$, then $f(1-y) = f(-c)/c$ is constant. Thus $f$ is constant, which we already considered.
So, for non-constant solutions, we must have $f(0)=0$.

$P(x,1) \implies f(x-f(x)) = f(x)f(0) = 0$.
Let $Z$ be the set of zeros of $f$. $Z=\{x\in\mathbb{Z} : f(x)=0\}$. We have $0\in Z$ and $x-f(x) \in Z$ for all $x$.

$P(x,0) \implies f(x-f(0)) = f(x)f(1)$, so $f(x)=f(x)f(1)$.
Since $f$ is not identically zero, there exists $x_0$ such that $f(x_0)\neq 0$. This implies $f(1)=1$.

$P(1,y) \implies f(1-f(y)) = f(1)f(1-y) = f(1-y)$.

3. Analyzing $f(2)$.
Let $f(2)=c$. Since $x-f(x)\in Z$, $2-f(2)=2-c\in Z$, so $f(2-c)=0$.

Case 3.1: $c=2$. $f(2)=2$. $0\in Z$.
We show that this implies $f(x)=x$. This is equivalent to showing $Z=\{0\}$.
Suppose $Z\neq\{0\}$. Let $k$ be the smallest positive integer in $Z$. $k>2$ since $f(1)=1, f(2)=2$.
If $k$ is even, $k=2m$ with $m>1$.
$P(2,m) \implies f(2-f(2m)) = f(2)f(1-m)$. $f(2m)=f(k)=0$.
$f(2-0) = 2f(1-m)$. $2 = 2f(1-m)$, so $f(1-m)=1$.
Then $(1-m)-f(1-m) = 1-m-1 = -m \in Z$. So $m\in Z$.
Since $m>1$, $m$ is a positive zero. But $m=k/2 < k$. This contradicts the definition of $k$.
If $k$ is odd, $k\ge 3$.
$P(1, k) \implies f(1-f(k)) = f(1-k)$. $f(1)=1$, so $f(1-k)=1$.
$P(2, (k+1)/2) \implies f(2-f(k+1)) = f(2)f(1-(k+1)/2) = 2f((1-k)/2)$.
Since $1-k\in Z$ or $1-k=0$ or $-(1-k)\in Z$ is not clear.
However, $f(1-k)=1$. So $(1-k)-1 = -k \in Z$.
Let's look at $P(1-k, y)$. $f(1-k-f((1-k)y)) = f(1-k)f(1-y) = f(1-y)$.

Let's look at $k=3$. $f(3)=0$. $f(2)=2$.
$P(2,-1) \implies f(2-f(-2)) = f(2)f(2) = 4$.
$f(1-3)=f(-2)=1$.
$f(2-1)=f(1)=1$. So $1=4$. Contradiction.
Thus, if $f(2)=2$, then $Z=\{0\}$, which means $f(x)=x$.
$f(x)=x$ is a solution: $x-xy = x(1-y)$.

Case 3.2: $c=0$. $f(2)=0$. $2\in Z$.
$P(1, 2) \implies f(1-f(2)) = f(-1)$. $f(1)=1$, so $f(-1)=1$.
$P(x, 2) \implies f(x-f(2x)) = f(x)f(-1) = f(x)$.
If $z\in Z$, $f(1-z)=1$. $f(2)=0 \implies f(-1)=1$. $f(0)=0 \implies f(1)=1$.
If $f(y)\in\{0, 1\}$ for all $y$.
$f(y)=0 \iff f(1-y)=1$. This means $y$ and $1-y$ have different values under $f$.
Since $f(0)=0$ and $f(1)=1$, this suggests $f(x)=0$ if $x$ is even and $f(x)=1$ if $x$ is odd. $f(x)=x \bmod 2$.
We verify this solution.
If $x$ is even, $f(x)=0$. LHS: $f(xy)$ is 0 since $xy$ is even. $f(x-0)=0$. RHS: $0$.
If $x$ is odd, $f(x)=1$. LHS: $f(x-f(xy))$. RHS: $f(1-y)$.
If $y$ is even, $1-y$ is odd, RHS=1. $xy$ is even, $f(xy)=0$. LHS: $f(x)=1$.
If $y$ is odd, $1-y$ is even, RHS=0. $xy$ is odd, $f(xy)=1$. LHS: $f(x-1)$. $x-1$ is even, LHS=0.
$f(x)=x \bmod 2$ is a solution.

Case 

[Note: response truncated to first 3000 characters of 3970]
