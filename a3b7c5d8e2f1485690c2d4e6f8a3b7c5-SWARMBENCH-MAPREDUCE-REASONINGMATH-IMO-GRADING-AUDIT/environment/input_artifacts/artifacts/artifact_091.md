# artifact_091

Grading ID: GB-0543  
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

We will use standard notation for $\triangle ABC$, with side lengths $a, b, c$, semiperimeter $s$, and angles $A, B, C$. Let $I$ be the incenter. We denote directed angles modulo $180^\circ$ by $\measuredangle(l_1, l_2)$.

The proof is divided into three main steps.

**Step 1: Proving that L, U, V are collinear.**

We first analyze the points $U$ and $V$. $E$ is on $AC$ such that $BE$ bisects $\angle B$. By the Angle Bisector Theorem, $AE = bc/(a+c)$. $U$ is on $AB$ such that $AU=AE$.
$UB = c - AU = c - \frac{bc}{a+c} = \frac{c(a+c-b)}{a+c} = \frac{2c(s-b)}{a+c}$.
Thus, $\frac{AU}{UB} = \frac{bc/(a+c)}{2c(s-b)/(a+c)} = \frac{b}{2(s-b)}$.

Similarly, $F$ is on $AB$ such that $CF$ bisects $\angle C$. $AF = bc/(a+b)$. $V$ is on $AC$ such that $AV=AF$.
$CV = b - AV = b - \frac{bc}{a+b} = \frac{b(a+b-c)}{a+b} = \frac{2b(s-c)}{a+b}$.
Thus, $\frac{CV}{VA} = \frac{2b(s-c)/(a+b)}{bc/(a+b)} = \frac{2(s-c)}{c}$.

Next, we analyze the point $L$. $L$ is on $BC$ such that $IL \perp AI$.
Let $M$ be the intersection of the angle bisector $AI$ and the circumcircle of $\triangle ABC$. It is known that $M$ is the circumcenter of $\triangle BIC$ (since $\angle MBI = \angle MBC + \angle CBI = \angle MAC + B/2 = A/2 + B/2$, and $\angle MIB = \angle IAB + \angle IBA = A/2 + B/2$, so $MI=MB$, and $MB=MC$ as $M$ bisects arc $BC$).
Since $M$ is the circumcenter of $\triangle BIC$ and lies on $AI$, $MI$ is a radius of the circumcircle $(BIC)$. As $LI \perp AI$, $LI$ is perpendicular to the radius $MI$ at $I$. Therefore, $LI$ is tangent to the circumcircle $(BIC)$ at $I$.

By the Alternate Segment Theorem, $|\angle LIB| = |\angle ICB| = C/2$ and $|\angle LIC| = |\angle IBC| = B/2$.
We calculate the ratio $BL/LC$ using areas:
$$ \frac{BL}{LC} = \frac{\text{Area}(LBI)}{\text{Area}(LCI)} = \frac{\frac{1}{2} LI \cdot IB \sin(\angle LIB)}{\frac{1}{2} LI \cdot IC \sin(\angle LIC)} = \frac{IB \sin(C/2)}{IC \sin(B/2)} $$
In $\triangle IBC$, by the Law of Sines, $IB/\sin(C/2) = IC/\sin(B/2)$. Thus $IB/IC = \sin(C/2)/\sin(B/2)$.
$$ \frac{BL}{LC} = \frac{\sin^2(C/2)}{\sin^2(B/2)} $$
Using the half-angle formulas $\sin^2(B/2) = \frac{(s-a)(s-c)}{ac}$ and $\sin^2(C/2) = \frac{(s-a)(s-b)}{ab}$, we get:
$$ \frac{BL}{LC} = \frac{c(s-b)}{b(s-c)} $$

Now we apply Menelaus' Theorem to $\triangle ABC$ and points $L, U, V$:
$$ \frac{AU}{UB} \cdot \frac{BL}{LC} \cdot \frac{CV}{VA} = \left(\frac{b}{2(s-b)}\right) \cdot \left(\frac{c(s-b)}{b(s-c)}\right) \cdot \left(\frac{2(s-c)}{c}\right) = 1 $$
Thus, $L, U, V$ are collinear. Since $X$ is on $LU$ and $Y$ is on $LV$, $L, X, Y, U, V$ are collinear. The line $XY$ is the line $LUV$.

**Step 2: Proving that I, X, P, Y are concyclic.**

$X$ is on the circumcircle of $\triangle ILC$, so $I, L, C, X$ are concyclic.
$$ \measuredangle(IX, IL) = \measuredangle(CX, CL) $$
$P$ is on line $XC$, and $L$ is on line $BC$ (which is $CL$). Thus,
$$ \measuredangle(IX, IL) = \measuredangle(PX, BC) \quad (1) $$

$Y$ is on the circumcircle of $\tria

[Note: response truncated to first 3000 characters of 4952]
