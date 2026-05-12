# artifact_041

Grading ID: GB-0532  
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

This is a known difficult problem (IMO Shortlist 2017 G8). The proof relies on several non-trivial observations and lemmas. We will use directed angles modulo $\pi$, denoted by $(L_1, L_2)$.

Step 1: Prove that $I, X, P, Y$ are concyclic.
$X$ lies on the circumcircle of $\triangle ILC$. Thus, $(XI, XC) = (LI, LC)$.
$Y$ lies on the circumcircle of $\triangle ILB$. Thus, $(YI, YB) = (LI, LB)$.
Since $L, B, C$ are collinear, the lines $LB$ and $LC$ coincide (the line $BC$). Thus, $(LI, LC) = (LI, LB)$.
$P$ is the intersection of $XC$ and $YB$. So $XC$ is $XP$ and $YB$ is $YP$.
$(XI, XP) = (LI, BC)$ and $(YI, YP) = (LI, BC)$.
Therefore, $(XI, XP) = (YI, YP)$, which proves that the points $I, X, P, Y$ lie on a common circle.

Step 2: Properties related to U, V, and L.
$U$ and $V$ are defined such that $AU=AE$ and $AV=AF$. Since $AI$ is the angle bisector of $\angle A$, $U$ is the reflection of $E$ across $AI$, and $V$ is the reflection of $F$ across $AI$.
$L$ is on $BC$ such that $IL \perp AI$.

The key property of this configuration is the following non-trivial lemma.
Lemma 1: The lines $LU$ and $LV$ are symmetric with respect to the line $BC$.
In directed angles, $(BC, LU) = -(BC, LV)$.

Step 3: Angle relations derived from Lemma 1.
$X$ is on $(ILC)$ and $LU$. $(IC, IX) = (LC, LX) = (BC, LU)$.
$Y$ is on $(ILB)$ and $LV$. $(IB, IY) = (LB, LY) = (BC, LV)$.
By Lemma 1, we have $(IC, IX) = -(IB, IY) = (IY, IB)$.

Step 4: Concyclicity of I, B, C, P.
This step is often derived from Lemma 1 and related properties, sometimes involving another difficult result that $B, C, X, Y$ are concyclic (Claim A), or arguments involving similarities. A known path (although verification using directed angles is subtle and led to contradictions in the scratchpad) argues that the configuration implies an inverse similarity $\triangle IYB \sim_{inv} \triangle IXC$. This inverse similarity implies $(BI, BY) = -(CI, CX)$.
Since $P$ lies on $BY$ and $CX$, $(BI, BP) = -(CI, CP)$.
We can show this implies $I, B, C, P$ are concyclic.
$(PB, PC) = (PB, IB) + (IB, IC) + (IC, PC)$
$= -(BI, BP) + (IB, IC) - (CI, CP)$
$= -(CI, CP) + (IB, IC) - (CI, CP) = (IB, IC) - 2(CI, CP)$.
This derivation seems incorrect based on the scratchpad analysis.

Let's use the argument presented in some solutions which rely on the established concyclicity of $I, B, C, P$.
Assuming $I, B, C, P$ are concyclic.

Step 5: Proving $IP \parallel XY$.
We have established (A) $I, X, P, Y$ are concyclic, and we assume (C) $I, B, C, P$ are concyclic.

We want to prove $IP \parallel XY$. Since $IXPY$ is cyclic, this is equivalent to $IPXY$ being an isosceles trapezoid. This is equivalent to the condition $(IP, IY) = (XP, XY)$.

It can be shown that given (A) and (C), $IP \parallel XY$ is equivalent to the condition $(IB, IC) = (YB, IY)$.

Let's verify this condition.
Let $A/2=\alpha, B/2=\beta, C/2=\gamma$. $\alpha+\beta+\gamma=\pi/2$.
$(IB, IC) = \beta+\gamma$ (assuming standard orientation).

$(YB, IY) = -(IY, YB)$.

[Note: response truncated to first 3000 characters of 4535]
