# artifact_093

Grading ID: GB-0801  
Problem ID: PB-Advanced-024  
Source: (Modified) IMO 2024 P6  
IMO Area: Algebra

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $P$ be a function from the set $\mathbb{Q}$ of rational numbers
 to itself, and suppose that $P$ satisfies
 \[
 (P(b-P(a))+a-P(b))(P(a+P(b-P(a)))-b)=0
 \]
 for all rational numbers $a,b$. Prove that the set $\{P(a)+P(-a):a\in\mathbb{Q}\}$
 is a finite set, and find the maximum possible number of elements
 in this set.

## Reference Solution (for grader's calibration)

Let the given condition be
 \[
 (P(b-P(a))+a-P(b))(P(a+P(b-P(a)))-b)=0\quad(*)
 \]
 for all $a,b\in\mathbb{Q}$. Let $y=b-P(a)$. Then $b=y+P(a)$. Substituting
 this into $(*)$, we get
 \[
 (P(y)+a-P(y+P(a)))(P(a+P(y))-(y+P(a)))=0.
 \]
 This must hold for all $a\in\mathbb{Q}$ and all $y$ in the image
 of $b\mapsto b-P(a)$. Since $b$ can be any rational number, $y$
 can be any rational number (assuming $P(a)\in\mathbb{Q}$). Thus,
 for all $a,y\in\mathbb{Q}$, we have
 \[
 P(y+P(a))=P(y)+a\quad\text{or}\quad P(a+P(y))=y+P(a).
 \]
 Let's rewrite this by swapping variable names $a\to y$ and $y\to x$:
 For all $x,y\in\mathbb{Q}$,
 \[
 P(x+P(y))=P(x)+y\quad\text{or}\quad P(P(x)+y)=x+P(y).\quad(**)
 \]
 We want to find the maximum possible number of elements in the set
 $S=\{P(a)+P(-a):a\in\mathbb{Q}\}$. Let $g(a)=P(a)+P(-a)$. We want
 to find the maximum possible size of the image of $g$.


 We begin by providing an example of a function $P$ for which there
 are two values of $g(a)$. We take the function $P(x)=2\lfloor x\rfloor-x=\lfloor x\rfloor-\{x\}$.
 First, we show that $P$ satisfies $(**)$. Given $x,y\in\mathbb{Q}$,
 writing $f$ instead of $P$: If $\{x\}<\{y\}$, then $f(f(x)+y)=x+f(y)$.
 This is the second case of $(**)$. If $\{x\}>\{y\}$, then $f(x+f(y))=f(x)+y$.
 This is the first case of $(**)$. If $\{x\}=\{y\}$, then $f(x)+y=x+f(y)=N$
 (an integer). $f(N)=N$. So $f(x+f(y))=f(N)=N=f(x)+y$ and $f(f(x)+y)=f(N)=N=x+f(y)$.
 Both cases of $(**)$ hold. In all cases, the relation $(**)$ is
 satisfied, which is equivalent to the original condition $(*)$.


 Finally, we compute $g(a)=P(a)+P(-a)$ for this function. $g(a)=(2\lfloor a\rfloor-a)+(2\lfloor-a\rfloor-(-a))=2(\lfloor a\rfloor+\lfloor-a\rfloor)$.
 If $a$ is an integer, $\lfloor a\rfloor=a$ and $\lfloor-a\rfloor=-a$,
 so $g(a)=2(a-a)=0$. If $a$ is not an integer, $\lfloor-a\rfloor=-\lfloor a\rfloor-1$,
 so $g(a)=2(\lfloor a\rfloor-\lfloor a\rfloor-1)=-2$. The set of values
 for $g(a)$ is $\{0,-2\}$. There are two values for $g(a)$.

 Now, we prove that there cannot be more than two values of $g(a).$
 Applying $(**)$ with $y=x$ tells us that $P(x+P(x))=P(x)+x$ or
 $P(P(x)+x)=x+P(x)$. In either case, if we let $z=x+P(x)$, then $P(z)=z$.
 So
 \[
 P(x+P(x))=x+P(x)\qquad\tag{(1)}
 \]
 for all $x\in\mathbb{Q}$.


 We begin with the following lemma.


 \textbf{Lemma 1.} $P$ is a bijection, and satisfies
 \[
 P(-P(-x))=x\qquad\tag{(2)}
 \]

 \emph{Proof.} We first prove that $P$ is injective. Suppose that
 $P(x_{1})=P(x_{2})=Y$. The condition $(**)$ applied to $(x_{1},x_{2})$
 gives $P(x_{1}+P(x_{2}))=P(x_{1})+x_{2}$ or $P(P(x_{1})+x_{2})=x_{1}+P(x_{2})$.
 Substituting $P(x_{1})=P(x_{2})=Y$, this becomes $P(x_{1}+Y)=Y+x_{2}$
 or $P(Y+x_{2})=x_{1}+Y$.

 From (1), we know $P(x_{1}+P(x_{1}))=x_{1}+P(x_{1})$, i.e., $P(x_{1}+Y)=x_{1}+Y$.
 Also from (1), $P(x_{2}+P(x_{2}))=x_{2}+P(x_{2})$, i.e., $P(x_{2}+Y)=x_{2}+Y$.

 Case A: $P(x_{1}+Y)=Y+x_{2}$ holds. Using $P(x_{1}+Y)=x_{1}+Y$,
 we get $x_{1}+Y=Y+x_{2}$, which implies $x_{1}=x_{2}$.

 Case B: $P(Y+x_{2})=x_{1}+Y$ holds. Using $P(x_{2}+Y)=x_{2}+Y$,
 we get $x_{2}+Y=x_{1}+Y$, which implies $x_{1}=x_{2}$.

 In both cases, $x_{1}=x_{2}$. So $P$ is injective.


 Now, (1) with $x=0$ tells us that $P(0+P(0))=0+P(0)$, so $P(P(0))=P(0)$.
 By injectivity, $P(0)=0$.

 Let $C(x,y)$: $P(x+P(y))=P(x)+y$ or $P(P(x)+y)=x+P(y)$.

 $C(x,-P(x))$: $P(x+P(-P(x)))=P(x)-P(x)=0$ or $P(P(x)-P(x))=x+P(-P(x))$.

 Case 1: $P(x+P(-P(x)))=0$. Since $P(0)=0$ and $P$ is injective,
 $x+P(-P(x))=0$, so $P(-P(x))=-x$.

 Case 2: $P(0)=x+P(-P(x))$. Since $P(0)=0$, this gives $0=x+P(-P(x))$,
 so $P(-P(x))=-x$.

 Both options yield $P(-P(x))=-x$. Replace $x$ with $-x$: $P(-P(-x))=-(-x)=x$.
 This proves (2).


 Finally, bijectivity follows immediately from (2). $P$ is injective.
 For any $y\in\mathbb{Q}$, let $x=-P(-y)$. Then $P(x)=P(-P(-y))=y$.
 So $P$ is surjective.


 Since $P$ is bijective, it has an inverse, which we denote $P^{-1}$.
 From (2), $P(-P(-x))=x$. Let $z=-P(-x)$. Then $P(z)=x$, so $z=P^{-1}(x)$.
 Thus, $P^{-1}(x)=-P(-x)$. Rearranging gives $P(-x)=-P^{-1}(x)$.
 We have $g(x)=P(x)+P(-x)=P(x)-P^{-1}(x)$.

 Suppose $g(x)=u$ and $g(y)=v$, where $u\neq v$ are both nonzero.
 Define $x^{\prime}=P^{-1}(x)$ and $y^{\prime}=P^{-1}(y)$. By definition,
 $P(x')=x$ and $P(y')=y$. We have $g(x)=P(x)-P^{-1}(x)=P(x)-x'=u$,
 so $P(x)=x'+u$. Similarly,
 \[
 g(y)=P(y)-P^{-1}(y)=P(y)-y'=v,
 \]
 so $P(y)=y'+v$.


 Apply $(**)$ to $(x',y)$:

 \[
 P(x'+P(y))=P(x')+y\text{ or }P(P(x')+y)=x'+P(y).
 \]
 $P(x'+y'+v)=x+y$ or $P(x+y)=x'+y'+v$. (Let $A=x+y,B=x'+y'+v$. $P(B)=A$
 or $P(A)=B$.)



  Apply $(**)$ to $(x,y')$:
 \[
 P(x+P(y'))=P(x)+y'\text{ or }P(P(x)+y')=x+P(y').
 \]
 $P(x+y)=P(x)+y'=(x'+u)+y'$ or $P(x'+u+y')=x+y$. (Let $C=x'+y'+u$.
 $P(A)=C$ or $P(C)=A$.)


 We have the possibilities:

 (1a) $P(B)=A$ and (2a) $P(A)=C$.

 (1a) $P(B)=A$ and (2b) $P(C)=A$. Since $P$ is injective, $B=C$,
 so $x'+y'+v=x'+y'+u$, which implies $u=v$. Contradiction.

 (1b) $P(A)=B$ and (2a) $P(A)=C$. Since $P(A)$ must be unique, $B=C$,
 which implies $u=v$. Contradiction.

 (1b) $P(A)=B$ and (2b) $P(C)=A$.

 So we must have either ($P(B)=A$ and $P(A)=C$) or ($P(A)=B$ and
 $P(C)=A$).


 Case 1: $P(x'+y'+v)=x+y$ and $P(x+y)=x'+y'+u$.

 Case 2: $P(x+y)=x'+y'+v$ and $P(x'+y'+u)=x+y$.


 Swapping $(x,u)$ with $(y,v)$ transforms Case 1 into Case 2 structure
 and vice versa. So, without loss of generality, assume Case 2 holds:
 $P(x+y)=x'+y'+v$ and $P(x'+y'+u)=x+y$.


 Now consider $(**)$ applied to $(x+y,-x'-u)$. Let $A=x+y$ and $Z=-x'-u$.
 Using $P(-z)=-P^{-1}(z)$, we have $P(-x'-u)=-P^{-1}(x'+u)$. From
 $P(x)=x'+u$ we have $x=P^{-1}(x'+u)$. Therefore, $P(Z)=P(-x'-u)=-x$.

 Now $C(A,Z)$ gives: $P(A+P(Z))=P(A)+Z$ or $P(P(A)+Z)=A+P(Z)$. Substitute
 $A=x+y$, $Z=-x'-u$, $P(Z)=-x$. And $P(A)=P(x+y)=x'+y'+v$ (using
 Case 2).


 Option 1: $P((x+y)+(-x))=P(x+y)+(-x'-u)$. $P(y)=(x'+y'+v)-x'-u=y'+v-u$.

 Option 2: $P(P(x+y)+Z)=A+P(Z)$. $P((x'+y'+v)+(-x'-u))=(x+y)+(-x)$.
 $P(y'+v-u)=y$.


 So we have $P(y)=y'+v-u$ or $P(y'+v-u)=y$. This means $y'+v-u$
 must be either $P(y)$ or $P^{-1}(y)$. We know $P(y)=y'+v$ and $P^{-1}(y)=y'$.
 If $y'+v-u=P(y)=y'+v$, then $v-u=v$, which means $u=0$. This contradicts
 our assumption $u\neq0$. If $y'+v-u=P^{-1}(y)=y'$, then $v-u=0$,
 which means $u=v$. This contradicts our assumption $u\neq v$.


 Both possibilities lead to a contradiction. Therefore, the initial
 assumption that there exist distinct non-zero values $u,v$ for $g(x)$
 must be false. The set $S=\{g(a):a\in\mathbb{Q}\}$ can contain $g(0)=P(0)+P(0)=0$.
 It can contain at most one non-zero value $u$. Thus, the set $S$
 must be a subset of $\{0,u\}$ for some $u\in\mathbb{Q}$. The maximum
 possible number of elements in $S$ is $2$.


 Since we found an example where the set of values is $\{0,-2\}$,
 which has 2 elements, the maximum possible number of elements is exactly
 2.

## Grading Guidelines

(Partial)
 1. Correctly guessed all the possible $P$.
 2. Proved that $P$ is bijective.
 3. Proved that $P(-P(x))=-x$.
(Almost)
 1. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

We are given a function $P: \mathbb{Q} \to \mathbb{Q}$ satisfying the equation:
\[ (P(b-P(a))+a-P(b))(P(a+P(b-P(a)))-b)=0 \quad (*) \]
for all $a,b \in \mathbb{Q}$. We want to prove that the set $S = \{P(a)+P(-a): a \in \mathbb{Q}\}$ is finite and find the maximum possible number of elements in $S$.

**Step 1: Prove that $P(x)=0$ if and only if $x=0$.**

Suppose $P(k)=0$ for some $k \in \mathbb{Q}$. We substitute $a=k$ into $(*)$.

The first factor becomes:
$P(b-P(k))+k-P(b) = P(b-0)+k-P(b) = P(b)+k-P(b) = k$.

The second factor becomes:
$P(k+P(b-P(k)))-b = P(k+P(b-0))-b = P(k+P(b))-b$.

The equation $(*)$ simplifies to:
\[ k (P(k+P(b))-b) = 0 \quad \text{for all } b \in \mathbb{Q}. \]

If we assume $k \neq 0$, then we must have $P(k+P(b))=b$ for all $b \in \mathbb{Q}$.
Setting $b=k$ in this equation, we get $P(k+P(k))=k$.
Since we assumed $P(k)=0$, this simplifies to $P(k+0)=k$, so $P(k)=k$.
But $P(k)=0$, so $k=0$. This contradicts the assumption $k \neq 0$.

Therefore, we must have $k=0$. This proves that $P(x)=0 \implies x=0$.
Consequently, $P(0)=0$. Thus, $P(x)=0 \iff x=0$.

**Step 2: Prove that $P(-P(a))=-a$ and $P$ is a bijection.**

Set $b=0$ in $(*)$. Since $P(0)=0$:
$(P(0-P(a))+a-P(0))(P(a+P(0-P(a)))-0)=0$.
\[ (P(-P(a))+a) P(a+P(-P(a))) = 0. \]

Let $K_a = P(-P(a))+a$. The equation is $K_a P(K_a) = 0$.
For any $a \in \mathbb{Q}$, either $K_a=0$ or $P(K_a)=0$.
By Step 1, if $P(K_a)=0$, then $K_a=0$.
In both cases, $K_a=0$.
\[ P(-P(a)) = -a \quad \text{for all } a \in \mathbb{Q}. \]

This identity implies that $P$ is a bijection:
*   Injectivity: If $P(a_1)=P(a_2)$, then $P(-P(a_1))=P(-P(a_2))$, so $-a_1=-a_2$, which means $a_1=a_2$.
*   Surjectivity: For any $y \in \mathbb{Q}$, let $x = -P(-y)$. Then $P(x) = P(-P(-y)) = -(-y) = y$.

**Step 3: Analyze the set $S = \{P(a)+P(-a): a \in \mathbb{Q}\}$.**

We use the identity $P(-P(x))=-x$.
Apply this for $x=a$: $P(-P(a))=-a$.
Apply this for $x=-a$: $P(-P(-a))=-(-a)=a$.

Adding these two equations gives:
\[ P(-P(a)) + P(-P(-a)) = 0 \quad (**) \]

Let $s$ be an arbitrary element of $S$. Then $s = P(a)+P(-a)$ for some $a \in \mathbb{Q}$.
Let $u=P(a)$. Then $P(-a)=s-u$.

Substituting these into the identity $(**)$:
$P(-u) + P(-(s-u)) = 0$.
$P(-u) + P(u-s) = 0$.
\[ P(u-s) = -P(-u). \]

Since $P$ is surjective (Step 2), $u=P(a)$ spans all of $\mathbb{Q}$ as $a$ spans $\mathbb{Q}$.
Therefore, if $s \in S$, the function $P$ must satisfy the identity:
\[ P(x-s) = -P(-x) \quad \text{for all } x \in \mathbb{Q}. \]

**Step 4: Prove that $S$ is a finite set with exactly one element.**

Let $s_1$ and $s_2$ be any two elements in $S$. (We know $S$ is non-empty, as $P(0)+P(0)=0 \in S$).
From Step 3, the following identities must hold for all $x \in \mathbb{Q}$:
$P(x-s_1) = -P(-x)$.
$P(x-s_2) = -P(-x)$.

Therefore, $P(x-s_1) = P(x-s_2)$ for all $x \in \mathbb{Q}$.
Since $P$ is injective (Step 2), we must have $x-s_1 = x-s_2$ for all $x$.
This implies $s_1=s_2$.

This proves that the set $S$ contains exactly on

[Note: response truncated to first 3000 characters of 4026]
