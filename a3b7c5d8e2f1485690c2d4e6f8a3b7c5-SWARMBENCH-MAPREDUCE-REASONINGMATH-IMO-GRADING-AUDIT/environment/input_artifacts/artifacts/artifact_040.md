# artifact_040

Grading ID: GB-0178  
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
\[ f(x-f(xy))=f(x)f(1-y) \quad (E) \]
holds for all $x,y\in\mathbb{Z}$. Let $P(x, y)$ be this assertion.

**Step 1: Constant solutions and $f(0)=0$.**

If $f(x)=c$, then $c=c^2$, so $c=0$ or $c=1$.
Solution 1: $f(x)=0$.
Solution 2: $f(x)=1$.

$P(0, y) \implies f(-f(0)) = f(0)f(1-y)$. If $f(0) \neq 0$, $f(1-y)$ is constant, implying $f$ is constant. Thus, for non-constant solutions, we must have $f(0)=0$.

**Step 2: Properties of non-constant solutions.**

Assume $f$ is non-constant. $f(0)=0$.
$P(x, 0) \implies f(x-f(0)) = f(x)f(1)$, so $f(x)=f(x)f(1)$. Since $f$ is not identically zero, $f(1)=1$.

$P(x, 1) \implies f(x-f(x)) = f(x)f(0) = 0$.

Let $Z = \{z \in \mathbb{Z} \mid f(z)=0\}$. We have $0 \in Z$, and $x-f(x) \in Z$ for all $x$.

$P(1, z)$ for $z \in Z \implies f(1-f(z)) = f(1)f(1-z)$. $f(1-0) = f(1-z)$.
So $f(1-z)=1$ for all $z \in Z$.

If $z \in Z$, then $1-z$ maps to 1. $(1-z)-f(1-z) = (1-z)-1 = -z \in Z$. So $Z$ is symmetric.

**Step 3: Case $Z=\{0\}$.**

If $Z=\{0\}$, then $x-f(x)=0$, so $f(x)=x$.
Solution 3: $f(x)=x$.

**Step 4: Case $Z \neq \{0\}$. Determining $k_0$.**

Let $k_0 = \min(Z \cap \mathbb{Z}^+)$. Since $f(1)=1$, $k_0 \ge 2$.
$f(x) \equiv x \pmod{k_0}$.

Suppose $k_0 \ge 4$.

If $k_0=2m$ (even, $m \ge 2$). $f(2m)=0$. $f(m) \neq 0$.
$P(m, 2) \implies f(m-f(2m)) = f(m)f(-1)$. $f(m) = f(m)f(-1)$.
Since $f(m) \neq 0$, $f(-1)=1$.
Then $-1-f(-1) = -1-1 = -2 \in Z$. So $2 \in Z$. $k_0 \le 2$. Contradiction to $k_0 \ge 4$.

If $k_0=2m+1$ (odd, $k_0 \ge 5$, $m \ge 2$). $f(k_0)=0$. $f(1-k_0)=f(-2m)=1$.
$P(2, -m) \implies f(2-f(-2m)) = f(2)f(1+m)$.
$f(2-1) = f(1) = 1 = f(2)f(m+1)$.
So $f(2) \in \{1, -1\}$.
If $f(2)=1$, $2-f(2)=1 \in Z$. $k_0=1$. Contradiction.
If $f(2)=-1$, $2-f(2)=3 \in Z$. $k_0 \le 3$. Contradiction to $k_0 \ge 5$.

Thus, $k_0=2$ or $k_0=3$.

**Step 5: Case $k_0=2$.**

$f(2)=0$. $f(x) \equiv x \pmod 2$. $f(-1)=1$.

We show $f(x) \ge 0$.
If $f(a)=-1$. $a$ is odd. $f(1-f(a)) = f(2)=0$.
$P(1, a) \implies f(1-f(a)) = f(1-a)$. So $f(1-a)=0$. $1-a \in Z$.
By $f(1-z)=1$ for $z \in Z$, $f(1-(1-a)) = f(a)=1$. Contradiction $1=-1$.

If $f(a)=-2$. $a$ is even.
$P(2, a/2) \implies f(2-f(a)) = f(2)f(1-a/2) = 0$.
$f(2-(-2)) = f(4) = 0$.
$P(a, 2) \implies f(a-f(2a)) = f(a)f(-1) = -2 \cdot 1 = -2$.

If $a=4$, $f(4)=0$. $f(4-f(8)) = -2$.
$f(8)$ is even. $f(8) \ge 0$ or $f(8) \le -2$.
If $f(8)=0$, $f(4)=-2$. $0=-2$. Contradiction.

Thus, $f(x) \ge 0$ for all $x$.

Now we show $f(x)=1$ for odd $x$.
Let $a$ be odd. $f(a)=O \ge 1$. If $O \ge 3$.
$P(1, a) \implies f(1-O) = f(1-a)$.
$f(1-a)=E \ge 0$ (even).
If $E=0$, $f(1-a)=0$. $1-a \in Z$. $f(a)=f(1-(1-a))=1$. Contradiction $O=1$.
So $f(x)=1$ for all odd $x$.

If $E$ is even, $1-E$ is odd, $f(1-E)=1$.
$P(1, 1-E) \implies f(1-f(1-E)) = f(E)$.
$f(1-1) = f(0) = 0 = f(E)$.
So $f(x)=0$ for even $x$.
Solution 4: $f(x) = x \pmod 2$.

**Step 6: Case $k_0=3$.**

$f(3)=0$. $f(x) \equiv x \pmod 3$. $f(1)=1$.
As shown 

[Note: response truncated to first 3000 characters of 3706]
