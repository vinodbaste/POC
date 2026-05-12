# artifact_150

Grading ID: GB-0172  
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

We are looking for all functions $f:\mathbb{Z}\rightarrow\mathbb{Z}$ such that for all $x,y\in\mathbb{Z}$,
\[f(x-f(xy))=f(x)f(1-y) \quad (*).\]
Let $P(x,y)$ be the assertion $f(x-f(xy))=f(x)f(1-y)$.

First, we test for constant solutions. Let $f(x) = c$ for some constant $c \in \mathbb{Z}$.
Substituting into the equation $(*)$, we get $c = c \cdot c$, which implies $c^2-c=0$. The integer solutions are $c=0$ and $c=1$.
1.  If $f(x)=0$ for all $x$, LHS is $f(x-f(xy)) = f(x-0) = 0$. RHS is $f(x)f(1-y) = 0 \cdot 0 = 0$. So $f(x)=0$ is a solution.
2.  If $f(x)=1$ for all $x$, LHS is $f(x-f(xy)) = f(x-1) = 1$. RHS is $f(x)f(1-y) = 1 \cdot 1 = 1$. So $f(x)=1$ is a solution.

Now, assume $f$ is not a constant function.
$P(0,y) \implies f(0-f(0)) = f(0)f(1-y)$.
Let $k=f(0)$. This gives $f(-k) = k f(1-y)$ for all $y \in \mathbb{Z}$.
The LHS, $f(-k)$, is a constant. So the RHS, $k f(1-y)$, must also be constant.
If $k \neq 0$, then $f(1-y)$ must be constant. As $y$ ranges over $\mathbb{Z}$, $1-y$ also ranges over all of $\mathbb{Z}$. This means $f(z)$ is a constant function for all $z \in \mathbb{Z}$.
We have already found the constant solutions. If $f(x)=c$, then $f(0)=c=k$.
If $c=1$, $k=1 \neq 0$. We've confirmed $f(x)=1$ is a solution.
If $c=0$, $k=0$, which contradicts $k \neq 0$.
So, any solution that is not $f(x)=1$ must have $f(0)=0$.

Let's assume $f(0)=0$.
$P(x,0) \implies f(x-f(0)) = f(x)f(1-0)$, which simplifies to $f(x) = f(x)f(1)$.
This can be written as $f(x)(1-f(1))=0$.
Since we are looking for non-constant solutions, $f$ is not the zero function. Thus, there exists $x_0 \in \mathbb{Z}$ such that $f(x_0) \neq 0$.
For this $x_0$, we must have $1-f(1)=0$, which implies $f(1)=1$.

So, any solution other than the constant functions must satisfy $f(0)=0$ and $f(1)=1$.
Let's derive some key properties for such functions.
$P(x,1) \implies f(x-f(x)) = f(x)f(1-1) = f(x)f(0) = 0$.
(1) $f(x-f(x)) = 0$ for all $x \in \mathbb{Z}$.

$P(1,y) \implies f(1-f(y)) = f(1)f(1-y) = f(1-y)$.
(2) $f(1-f(y)) = f(1-y)$ for all $y \in \mathbb{Z}$.

Let $Z = \{x \in \mathbb{Z} \mid f(x)=0\}$ be the set of roots of $f$. From $f(0)=0$, we know $0 \in Z$.
From (1), we have $x-f(x) \in Z$ for all $x \in \mathbb{Z}$.

**Case 1: The set of roots is $Z=\{0\}$.**
From (1), $x-f(x)=0$ for all $x \in \mathbb{Z}$. This implies $f(x)=x$ for all $x \in \mathbb{Z}$.
Let's verify this solution:
LHS: $f(x-f(xy)) = f(x-xy) = x-xy = x(1-y)$.
RHS: $f(x)f(1-y) = x(1-y)$.
LHS = RHS, so $f(x)=x$ is a solution.

**Case 2: The set of roots $Z$ contains non-zero elements.**
Let $a = f(-1)$ and $k=f(2)$.
From (1), applied to $x=-1$ and $x=2$:
$f(-1-f(-1))=0 \implies f(-1-a)=0$. So $-1-a \in Z$.
$f(2-f(2))=0 \implies f(2-k)=0$. So $2-k \in Z$.

From (2), applied to $y=-1$ and $y=2$:
$f(1-f(-1))=f(1-(-1)) \implies f(1-a)=f(2)=k$.
$f(1-f(2))=f(1-2) \implies f(1-k)=f(-1)=a$.

We analyze the values of $a$ and $k$.
$P(2,-1) \implies f(2-f(-2)) = f(2)f(1-(-1)) = f(2)f(2) = k^2$.

If $a=0$, $f(-1)=0$. T

[Note: response truncated to first 3000 characters of 9119]
