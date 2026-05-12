# artifact_059

Grading ID: GB-0522  
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

Let the angles of $\triangle ABC$ at vertices $A, B, C$ be denoted by $\alpha, \beta, \gamma$ respectively. Let $I$ be the incenter. The lines $BI$ and $CI$ are the internal angle bisectors of $\angle B$ and $\angle C$.

**Step 1: Symmetry with respect to AI**

Let $s_{AI}$ be the reflection across the line $AI$. Since $AI$ is the angle bisector of $\angle A$, $s_{AI}$ maps the line $AB$ to $AC$ and vice-versa.
The point $E$ lies on $AC$. Its reflection $s_{AI}(E)$ is a point on $AB$. By the property of reflections, the distance from $A$ is preserved, so $A(s_{AI}(E)) = AE$. We are given that $U$ is on segment $AB$ such that $AU=AE$. Thus, $U=s_{AI}(E)$.
Similarly, $F$ is on $AB$. Its reflection $s_{AI}(F)$ is a point on $AC$ with $A(s_{AI}(F)) = AF$. We are given a point $V$ on segment $AC$ such that $AV=AF$. Thus, $V=s_{AI}(F)$.
Since $I$ lies on the axis of reflection $AI$, we have $s_{AI}(I)=I$. The reflection property implies that $\triangle AIE \cong \triangle AIU$ and $\triangle AIF \cong \triangle AIV$. From these congruences, we get $IE=IU$ and $IF=IV$.

**Step 2: Proving $I, X, P, Y$ are concyclic**

Let $\angle(l_1, l_2)$ denote the directed angle between lines $l_1$ and $l_2$ modulo $180^\circ$.
Let $\omega_C$ be the circumcircle of $\triangle ILC$ and $\omega_B$ be the circumcircle of $\triangle ILB$.
Since $L,I,C,X$ are concyclic on $\omega_C$, we have $\angle(XC,XI) = \angle(LC,LI)$.
Since $L,I,B,Y$ are concyclic on $\omega_B$, we have $\angle(YB,YI) = \angle(LB,LI)$.
The point $L$ lies on the line $BC$. Thus, the lines $LB$ and $LC$ are the same line $BC$.
Therefore, $\angle(LC,LI) = \angle(LB,LI)$.
This implies $\angle(XC,XI) = \angle(YB,YI)$.
The point $P$ is the intersection of $XC$ and $YB$. So we can write this equality as $\angle(PX,XI) = \angle(PY,YI)$.
This condition implies that the four points $P, I, X, Y$ are concyclic.

**Step 3: Condition for $IP \parallel XY$**

For a cyclic quadrilateral $IXPY$, the condition $IP \parallel XY$ is equivalent to it being an isosceles trapezoid with parallel sides $IP$ and $XY$. This means the other two sides must be equal in length, i.e., $IX=PY$ and $IY=PX$.
By the symmetry of the problem statement with respect to swapping the roles of $B$ and $C$ (which swaps $E \leftrightarrow F$, $U \leftrightarrow V$, $\omega_B \leftrightarrow \omega_C$, $X \leftrightarrow Y$), the condition $IY=PX$ implies $IX=PY$.
Thus, to prove $IP \parallel XY$, it suffices to prove either $IY=PX$ or the equivalent ratio condition $PX/PY = IY/IX$.

**Step 4: Calculation of the ratio $IY/IX$**

From $\triangle AIU \cong \triangle AIE$, we have $IU=IE$ and $\angle AUI = \angle AEI$. In $\triangle ABE$, $\angle AEB = 180^\circ - \alpha - \beta/2 = \gamma + \beta/2$. So $\angle AUI = \gamma+\beta/2$.
$X$ lies on the line $LU$, so $\angle IUX = 180^\circ - \angle AUI = 180^\circ - (\gamma+\beta/2) = \alpha+\beta/2$.
In $\triangle IUX$, by the Law of Sines, $\frac{IX}{\sin\angle IUX} = \frac{IU}{\sin\angle IXU}$.
$

[Note: response truncated to first 3000 characters of 8806]
