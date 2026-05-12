# artifact_053

Grading ID: GB-0790  
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

Let the given functional equation be
\[ (P(b-P(a))+a-P(b))(P(a+P(b-P(a)))-b)=0 \quad (*). \]
This equation holds for all rational numbers $a,b$. This implies that for any pair $(a,b)$, at least one of the two factors must be zero.

Let $S = \{P(a)+P(-a):a\in\mathbb{Q}\}$. We want to prove that $S$ is a finite set and find its maximum possible size.

Step 1: Basic properties of $P$.
First, we prove that $P(x)=0 \iff x=0$.
Suppose there exists $a_0 \in \mathbb{Q}$ with $a_0 \neq 0$ such that $P(a_0)=0$.
Substitute $a=a_0$ into the equation $(*)$:
\[ (P(b-P(a_0))+a_0-P(b))(P(a_0+P(b-P(a_0)))-b)=0. \]
Since $P(a_0)=0$, this simplifies to
\[ (P(b-0)+a_0-P(b))(P(a_0+P(b-0))-b)=0, \]
\[ (P(b)+a_0-P(b))(P(a_0+P(b))-b)=0, \]
\[ a_0(P(a_0+P(b))-b)=0. \]
Since we assumed $a_0 \neq 0$, the second factor must be zero for all $b \in \mathbb{Q}$:
\[ P(a_0+P(b))=b \quad \text{for all } b \in \mathbb{Q}. \]
This relation implies that $P$ is a bijection from $\mathbb{Q}$ to $\mathbb{Q}$.
Let's use this relation for a specific value of $b$. Let $b=a_0$:
\[ P(a_0+P(a_0)) = a_0. \]
Since $P(a_0)=0$, this becomes
\[ P(a_0+0) = a_0 \implies P(a_0)=a_0. \]
We have $P(a_0)=0$ and $P(a_0)=a_0$, which implies $a_0=0$. This contradicts our assumption that $a_0 \neq 0$.
Therefore, the only rational number $x$ for which $P(x)=0$ is $x=0$.
This implies $P(0)=0$.

Step 2: A key identity for $P$.
Set $b=0$ in the original equation $(*)$. This gives:
\[ (P(0-P(a))+a-P(0))(P(a+P(0-P(a)))-0)=0. \]
Since $P(0)=0$, the equation simplifies to:
\[ (P(-P(a))+a) \cdot P(a+P(-P(a))) = 0. \]
This must hold for all $a \in \mathbb{Q}$. So, for any given $a$, one of the two factors must be zero:
1.  $P(-P(a))+a = 0 \implies P(-P(a))=-a$.
2.  $P(a+P(-P(a))) = 0$. By Step 1, this implies $a+P(-P(a))=0$, which is also $P(-P(a))=-a$.
Thus, for all $a \in \mathbb{Q}$, we have the identity $P(-P(a))=-a$.

Step 3: Fixed points of $P$.
Let $A_P = \{x \in \mathbb{Q} \mid P(x)=x\}$ be the set of fixed points of $P$.
Let's choose $b=a+P(a)$ in the original equation $(*)$.
The first factor is:
$F_1 = P(a+P(a)-P(a)) + a - P(a+P(a)) = P(a)+a-P(a+P(a))$.
The second factor is:
$F_2 = P(a+P(a+P(a)-P(a))) - (a+P(a)) = P(a+P(a))-(a+P(a))$.
So the equation becomes:
\[ (P(a)+a-P(a+P(a))) (P(a+P(a))-(a+P(a))) = 0. \]
Let $Y = a+P(a)$ and $X=P(a+P(a))=P(Y)$. The equation is $(Y-X)(X-Y)=0$, which is $-(X-Y)^2=0$.
This implies $X-Y=0$, so $X=Y$.
Therefore, $P(a+P(a))=a+P(a)$ for all $a \in \mathbb{Q}$.
This means that for any $a \in \mathbb{Q}$, the number $a+P(a)$ is a fixed point of $P$.
So, $a+P(a) \in A_P$ for all $a \in \mathbb{Q}$.

Step 4: Properties of the set of fixed points $A_P$.
If $h \in A_P$, then $P(h)=h$. The identity from Step 2 gives $P(-P(h))=-h$, so $P(-h)=-h$. This means $-h \in A_P$.
Now we show that $A_P$ is a subgroup of $(\mathbb{Q},+)$. Let $h_1, h_2 \in A_P$.
Set $a=h_1$ in $(*)$. Since $P(h_1)=h_1$, we get:
\[ (P(b-h_1)+h_1-P(b))(P(h_1+P(b-h_1))-b)=0. \]
This holds for all $b \in \mathbb{Q

[Note: response truncated to first 3000 characters of 16914]
