# artifact_045

Grading ID: GB-0171  
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
\[ f(x-f(xy))=f(x)f(1-y) \quad (*) \]
holds for all $x,y\in\mathbb{Z}$. Let $P(x, y)$ be the assertion $(*)$.

### 1. Constant Solutions

If $f(x)=c$ for all $x$, then $c = c \cdot c$, so $c^2=c$. This gives $c=0$ or $c=1$.

**Solution 1:** $f(x)=0$ for all $x$.
LHS $= f(x-0)=0$. RHS $= 0 \cdot 0 = 0$. This is a solution.

**Solution 2:** $f(x)=1$ for all $x$.
LHS $= f(x-1)=1$. RHS $= 1 \cdot 1 = 1$. This is a solution.

### 2. Non-constant Solutions

Assume $f$ is not constant.

$P(0, y) \implies f(0-f(0)) = f(0)f(1-y)$.
If $f(0) = c \neq 0$, then $f(-c) = c f(1-y)$. The left side is constant, so $f(1-y)$ must be constant. This means $f$ is a constant function, contradicting our assumption.
Therefore, we must have $f(0)=0$.

$P(x, 0) \implies f(x-f(0)) = f(x)f(1)$. Since $f(0)=0$, we get $f(x) = f(x)f(1)$.
Since $f$ is not identically zero, there exists $x_0$ such that $f(x_0) \neq 0$. Thus, we must have $f(1)=1$.

We derive two key identities:

$P(x, 1) \implies f(x-f(x\cdot 1)) = f(x)f(1-1) \implies f(x-f(x)) = f(x)f(0) = 0$. (E1)

$P(1, y) \implies f(1-f(1\cdot y)) = f(1)f(1-y) \implies f(1-f(y)) = f(1-y)$. (E2)

Let $Z = \{z \in \mathbb{Z} \mid f(z)=0\}$. We know $0 \in Z$.
From (E1), $x-f(x) \in Z$ for all $x \in \mathbb{Z}$.

### Case 1: $Z=\{0\}$

If $f(z)=0$ if and only if $z=0$.
From (E1), $f(x-f(x))=0$. This implies $x-f(x)=0$, so $f(x)=x$ for all $x$.

**Solution 3:** $f(x)=x$.
Verification: LHS $= f(x-xy) = x-xy$. RHS $= x(1-y) = x-xy$. This is a solution.

### Case 2: $Z \neq \{0\}$

If $z \in Z$, $f(z)=0$. By (E2), $f(1-z) = f(1-f(z)) = f(1-0) = f(1) = 1$.

Let's investigate $f(2)$. Let $k=f(2)$.
By (E1), $f(2-f(2))=f(2-k)=0$. Since $f(1)=1$, $k \neq 1$.

#### Case 2a: $f(2)=0$.

$2 \in Z$. Then $f(1-2)=f(-1)=1$.

We show that the range of $f$ is restricted to $\{0, 1\}$.
Let $c \in f(\mathbb{Z})$, so $c=f(a)$ for some $a$. By (E2), $f(1-c)=f(1-a)$.
Also by (E2), $f(1-f(1-a)) = f(a)=c$.

If $c=2$, $f(a)=2$. Then $f(1-a) = f(1-2) = f(-1)=1$.
Then $c = f(1-f(1-a)) = f(1-1) = f(0) = 0$. So $2=0$, a contradiction.

If $c=-1$, $f(a)=-1$. Then $f(1-a) = f(1-(-1)) = f(2)=0$.
Then $c = f(1-f(1-a)) = f(1-0) = f(1) = 1$. So $-1=1$, a contradiction.

If $|c| \ge 2$, we can use induction or similar arguments, but the specific values $2$ and $-1$ already demonstrate that if $f(2)=0$, the range must be $f(\mathbb{Z}) \subseteq \{0, 1\}$.

Since $f(x) \in \{0, 1\}$, $f(1)=1$ and $f(2)=0$.
$x-f(x) \in Z$.
If $x$ is even, $f(x)=0$. If $x$ is odd, $f(x)=1$.
This function is $f(x) = x \pmod 2$.

**Solution 4:** $f(x) = \begin{cases} 1 & \text{if } x \text{ is odd} \\ 0 & \text{if } x \text{ is even} \end{cases}$.

Verification: $f(x) = x \pmod 2$.
LHS $= f(x-f(xy)) \equiv x-xy \pmod 2$.
RHS $= f(x)f(1-y) \equiv x(1-y) = x-xy \pmod 2$.
Since the range is $\{0, 1\}$, the equality holds.

#### Case 2b: $f(2)=-1$.

$k=-1$. $f(2-k)=f(2-(-1))=f(3)=0$. So $3 \in Z$.
$P(1, 2) \imp

[Note: response truncated to first 3000 characters of 5568]
