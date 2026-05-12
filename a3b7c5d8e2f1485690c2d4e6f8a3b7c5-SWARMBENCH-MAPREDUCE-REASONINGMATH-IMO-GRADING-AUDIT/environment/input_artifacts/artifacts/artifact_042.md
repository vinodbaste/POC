# artifact_042

Grading ID: GB-0540  
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

This proof relies on the use of directed angles modulo $180^\circ$, denoted by $\measuredangle(L_1, L_2)$.

The proof proceeds in four main steps: establishing the collinearity of $L, X, Y$ (via the Iran Lemma), proving that $P, I, B, C$ are concyclic, showing that $IL$ is tangent to this circle, and finally concluding that $IP \parallel XY$.

**Step 1: Collinearity of L, X, Y (The Iran Lemma)**

We are given $U$ on $AB$ and $V$ on $AC$ such that $AU=AE$ and $AV=AF$, where $E$ and $F$ are the feet of the angle bisectors from $B$ and $C$. $L$ is on $BC$ such that $IL \perp AI$.

A known result, often referred to as the Iran Lemma (IMO Shortlist 2006 G8), states that under these conditions, the points $L, U, V$ are collinear.
*(This can be proven using Menelaus' theorem on $\triangle ABC$ by calculating the ratios $\frac{AU}{UB}, \frac{CV}{VA}$ using the Angle Bisector Theorem, and $\frac{BL}{LC}$ using the Law of Sines in $\triangle IBL$ and $\triangle ICL$. The property $IL \perp AI$ is crucial for determining the ratio $\frac{BL}{LC}$.)*

By definition, $X$ lies on the line $LU$ (as the intersection of $\odot(ILC)$ and $LU$), and $Y$ lies on the line $LV$ (as the intersection of $\odot(ILB)$ and $LV$). Since $L, U, V$ are collinear, the points $L, U, V, X, Y$ all lie on the same line. Let this line be $\ell$. The line $XY$ is the line $\ell$.

**Step 2: Proving P, I, B, C are concyclic**

$P$ is the intersection of $XC$ and $YB$. We will show that $P$ lies on the circumcircle of $\triangle IBC$ by proving $\measuredangle(PC, PB) = \measuredangle(IC, IB)$.

$X$ lies on the circumcircle of $\triangle ILC$, so $I, L, C, X$ are concyclic. $X$ and $L$ lie on the line $\ell$.
$$ \measuredangle(XC, \ell) = \measuredangle(XC, XL) $$
Since $I, L, C, X$ are concyclic, the angles subtended by the chord $IL$ are equal:
$$ \measuredangle(XC, XL) = \measuredangle(IC, IL) \quad (1) $$

$Y$ lies on the circumcircle of $\triangle ILB$, so $I, L, B, Y$ are concyclic. $Y$ and $L$ lie on the line $\ell$.
$$ \measuredangle(\ell, YB) = \measuredangle(LY, YB) $$
Since $I, L, B, Y$ are concyclic, the angles subtended by the chord $IL$ are equal:
$$ \measuredangle(LY, YB) = \measuredangle(LI, IB) \quad (2) $$

Now we calculate the angle at $P$:
$$ \measuredangle(PC, PB) = \measuredangle(XC, YB) $$
We decompose this angle using the line $\ell$:
$$ \measuredangle(XC, YB) = \measuredangle(XC, \ell) + \measuredangle(\ell, YB) $$
Substituting (1) and (2):
$$ \measuredangle(PC, PB) = \measuredangle(IC, IL) + \measuredangle(LI, IB) $$
By the additive property of directed angles:
$$ \measuredangle(PC, PB) = \measuredangle(IC, IB) $$

This equality proves that the points $P, I, B, C$ are concyclic. Let $\Gamma$ be this circumcircle $\odot(PIBC)$.

**Step 3: Proving IL is tangent to the circle $\Gamma$**

$\Gamma$ is the circumcircle of $\triangle IBC$. By the Incenter-Excenter Lemma, the center $M$ of the circumcircle of $\triangle IBC$ lies on the internal angle bisector $AI$.


[Note: response truncated to first 3000 characters of 4499]
