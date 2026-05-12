# artifact_076

Grading ID: GB-0529  
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

**Complete Proof**

We use directed angles modulo $180^\circ$, denoted by $(L_1, L_2)$.

**Part 1: Setup and Key Angles**

Let $I$ be the incenter of the non-isosceles triangle $ABC$. Let $L$ be the point on $BC$ such that $IL \perp AI$. Since $AI$ is the internal angle bisector of $\angle A$, $IL$ is parallel to the external angle bisector of $\angle A$.

Let $\Theta = (LI, BC)$. Since $\triangle ABC$ is non-isosceles, the line $AI$ is not perpendicular to $BC$. Thus $IL$ is not parallel to $BC$, so $L$ is well-defined and $\Theta \neq 0$.

Since $L$ lies on the line $BC$, we have $LB = LC = BC$. Thus,
$$(LI, LB) = (LI, LC) = \Theta.$$

**Part 2: Proving Concyclicity of I, X, P, Y**

$X$ lies on the circumcircle of $\triangle ILC$. Thus $I, L, C, X$ are concyclic. By the property of cyclic quadrilaterals:
$$(XI, XC) = (LI, LC) = \Theta.$$

$Y$ lies on the circumcircle of $\triangle ILB$. Thus $I, L, B, Y$ are concyclic.
$$(YI, YB) = (LI, LB) = \Theta.$$

$P$ is defined as the intersection of lines $XC$ and $YB$. Thus, $XC$ is the line $XP$, and $YB$ is the line $YP$.
$$(XI, XP) = \Theta \quad \text{and} \quad (YI, YP) = \Theta.$$

Since $(XI, XP) = (YI, YP)$, the points $I, X, P, Y$ are concyclic.

Furthermore, since $\Theta \neq 0$, $I, X, P$ are not collinear, and $I, Y, P$ are not collinear. This ensures the quadrilateral $IXPY$ is non-degenerate. (The specific definitions of $U$ and $V$ ensure $X$ and $Y$ are well-defined points distinct from $L$, as stated in the problem.)

**Part 3: Proving $IP \parallel XY$**

We utilize the property that a cyclic quadrilateral is an isosceles trapezoid if and only if the angles formed by a side and the diagonals meeting at that side are equal.

**Lemma (Isosceles Trapezoid Condition):** Let $I, X, P, Y$ be concyclic points. $IP \parallel XY$ if and only if $IXPY$ is an isosceles trapezoid with bases $IP$ and $XY$. This holds if and only if $(IX, PX) = (IY, PY)$.

*Proof of Lemma:* $IP \parallel XY$ if and only if there is an axis of symmetry $m$ such that reflection $s_m$ swaps $I \leftrightarrow P$ and $X \leftrightarrow Y$. This implies $s_m(IX)=PY$ and $s_m(PX)=IY$. Since reflection reverses directed angles:
$(IX, PX) = -(s_m(IX), s_m(PX)) = -(PY, IY) = (IY, PY)$.

We now apply this lemma to our configuration. From Part 2, we have $(XI, XP) = \Theta$ and $(YI, YP) = \Theta$.

We calculate the required angles for the lemma:
$$(IX, PX) = -(XI, XP) = -\Theta.$$
$$(IY, PY) = -(YI, YP) = -\Theta.$$

Since $(IX, PX) = (IY, PY)$, and $I, X, P, Y$ are concyclic, $IXPY$ is an isosceles trapezoid with parallel bases $IP$ and $XY$.

Therefore, $IP \parallel XY$.
