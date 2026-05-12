# artifact_118

Grading ID: GB-0539  
Problem ID: PB-Advanced-016  
Source: Novel Problem  
IMO Area: Number_Theory

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $ABC$ be a non-isosceles triangle with incenter $I$. Let line $BI$ intersect $AC$ at $E$, and line $CI$ intersect $AB$ at $F$. Two Points $U$ and $V$ are on segments $AB$ and $AC$ respectively, such that $AU = AE$ and $AV = AF$. Let the line passing through $I$ and perpendicular to $AI$ intersect line $BC$ at $L$. The circumcircle of $\triangle ILC$ intersects line $LU$ at $X$ (other than $L$), and the circumcircle of triangle $\triangle ILB$ intersects line $LV$ at $Y$ (other than $L$). Prove that if $P$ is the intersection of lines $YB$ and $XC$, then line $IP$ is parallel to line $XY$.

## Reference Solution (for grader's calibration)

By symmetry, we assume that $AC>BC$.

 <Step 1> $U, V, L$ lie on a same line

 (1) Let $B^{\prime}$ be the point on $A C$ such that $A B=A B^{\prime}$ and $C^{\prime}$ be the point on $A B$ such that $A C=A C^{\prime}$. These points lie on the circumcircle of $\triangle I B C$.

 (2) By symmetry, $\left(B^{\prime}, I, U\right)$ and $\left(C^{\prime}, I, V\right)$ are collinear.

 (3) By Pascal's theorem on $B^{\prime} C B C^{\prime} I I, U, V, L$ lie on a same line.


 <Step 2> $IPXY$ is an isosceles trapezoid

 Since $U, V, L$ are collinear,

 \[
 \angle I X Y=\angle I C B=\angle B I L=\angle B Y L=\angle P Y X
 \]

 and similarly, $\angle I Y X=\angle P X Y$, so the statement holds.


 <Step 3> Therefore, by <Step 2>, $I P$ and $X Y$ are parallel.

## Grading Guidelines

(Partial)
 1. Proved that $U, V$, and $L$ lie on a same line.
(Almost)
 1. Made a minor mistake at the proof, or made a small gap.

## Candidate Response (to be graded)

This is a structured partial progress report and analysis. A seemingly complete proof is presented (Derivation B), relying on standard techniques of directed angles modulo $\pi$. However, an alternative analysis using the same techniques (Derivation A) leads to a contradiction for any non-degenerate triangle. As the requirement for rigor is paramount, and this contradiction cannot be resolved, a complete proof cannot be provided.

We use the notation $(L_1, L_2)$ for the directed angle modulo $\pi$ between the lines $L_1$ and $L_2$. We rely on the standard theorems: Inscribed Angle Theorem (IAT) and Directed Alternate Segment Theorem (DAST).

**1. Proven Lemmas and Key Results**

Let $I$ be the incenter of the non-isosceles triangle $ABC$. Let $a, b, c$ be the side lengths.

**Lemma 1: Properties of L and Tangency of IL.**
$L$ is on $BC$ such that $IL \perp AI$. The center of the circumcircle of $\triangle BIC$, denoted by $\Omega$, lies on $AI$ (by the Incenter-Excenter Lemma). Thus $IL$ is perpendicular to the radius at $I$, meaning $IL$ is tangent to $\Omega=(BIC)$ at $I$.

**Lemma 2: Collinearity of L, U, V.**
$E, F$ are the feet of the angle bisectors from $B, C$. $U$ on $AB, V$ on $AC$ with $AU=AE, AV=AF$.
By the Angle Bisector Theorem, $AE=bc/(a+c), AF=bc/(a+b)$.
The ratios for Menelaus theorem are calculated as:
$\frac{AU}{UB} = \frac{AE}{c-AE} = \frac{b}{a+c-b}$.
$\frac{CV}{VA} = \frac{b-AF}{AF} = \frac{a+b-c}{c}$.
Since $IL$ is tangent to $(BIC)$, by AST (magnitudes), $\angle LIB=C/2, \angle LIC=B/2$. By the Law of Sines in $\triangle IBL$ and $\triangle ICL$, $\frac{BL}{CL} = \frac{\sin^2(C/2)}{\sin^2(B/2)}$.
In terms of side lengths, $\frac{BL}{CL} = \frac{c(a+c-b)}{b(a+b-c)}$.
The product of the magnitudes is 1. Since $L$ lies outside the segment $BC$ (as $LI^2>0$ is the power of $L$), and $U, V$ are on the segments $AB, AC$. By Menelaus' theorem, $L, U, V$ are collinear. Let this line be $\ell$. Since $X$ is on $LU$ and $Y$ is on $LV$, the line $XY$ is $\ell$.

**Lemma 3: $I \notin \ell$.**
If $I \in \ell$, then $\ell=IL$. Since $AI \perp IL$, $AI \perp UV$. As $AI$ is the angle bisector of $\angle UAV$, $\triangle AUV$ is isosceles. $AU=AV \implies AE=AF \implies b=c$. This contradicts the assumption that $\triangle ABC$ is non-isosceles.

**Lemma 4: $I, P, B, C$ are concyclic.**
$X \in (ILC)$, so by IAT (chord $IX$): $(CI, CX) = (LI, LX)$. Since $P$ is on $XC$ and $X$ is on $\ell$, $(CI, CP) = (LI, \ell)$. (1)
$Y \in (ILB)$, so by IAT (chord $IY$): $(BI, BY) = (LI, LY)$. $(BI, BP) = (LI, \ell)$. (2)
From (1) and (2), $(CI, CP) = (BI, BP)$. Thus $I, P, B, C$ are concyclic. $P \in \Omega$.
(We verified that $X \neq L$ and $Y \neq L$ for non-degenerate triangles, so IAT applies).

**Lemma 5: $I, P, X, Y$ are concyclic.**
This follows from Miquel's Theorem applied to the complete quadrilateral formed by lines $BC, \ell, XC, YB$. The circumcircles are $(LXC)=(ILC)$ and $(LYB)=(ILB)$, which intersect at $I$ (and $L$). Thus $I$ is the Mi

[Note: response truncated to first 3000 characters of 7272]
