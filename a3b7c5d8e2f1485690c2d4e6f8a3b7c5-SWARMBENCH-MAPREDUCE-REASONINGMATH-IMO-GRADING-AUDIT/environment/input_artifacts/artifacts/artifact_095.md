# artifact_095

Grading ID: GB-0547  
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

We provide a proof using standard geometry theorems, including Menelaus' theorem and angle chasing with directed angles.

Let $a, b, c$ be the lengths of sides $BC, CA, AB$ respectively.

**Part 1: Proving L, U, V are collinear.**

$E$ is on $AC$ such that $BE$ is the angle bisector of $\angle B$. $F$ is on $AB$ such that $CF$ is the angle bisector of $\angle C$. By the Angle Bisector Theorem:
$AE = bc/(a+c)$ and $AF = bc/(a+b)$.

$U$ is on $AB$ with $AU=AE$, and $V$ is on $AC$ with $AV=AF$.
We calculate the ratios $AU/UB$ and $CV/VA$.
$UB = c - AU = c - \frac{bc}{a+c} = \frac{c(a+c-b)}{a+c}$.
$\frac{AU}{UB} = \frac{b}{a+c-b}$.
$VC = b - AV = b - \frac{bc}{a+b} = \frac{b(a+b-c)}{a+b}$.
$\frac{CV}{VA} = \frac{a+b-c}{c}$.

$L$ is on $BC$ such that $IL \perp AI$.

**Lemma 1:** Let $M$ be the midpoint of the arc $BC$ of the circumcircle of $\triangle ABC$ not containing $A$. Then $M$ lies on $AI$, and $M$ is the circumcenter of $\triangle IBC$.
*Proof:* Since $M$ bisects arc $BC$, $AM$ bisects $\angle A$, so $M$ lies on $AI$. We have $MB=MC$. Let $\alpha=A/2, \beta=B/2$.
$\angle MBI = \angle MBC + \angle CBI$. Since $M, A, B, C$ are concyclic, $\angle MBC = \angle MAC = \alpha$. So $\angle MBI = \alpha+\beta$.
In $\triangle ABI$, $\angle BIA = 180^\circ - (\alpha+\beta)$. Since $M, I, A$ are collinear, $\angle MIB = 180^\circ - \angle BIA = \alpha+\beta$.
Thus, $\triangle MIB$ is isosceles with $MI=MB$. So $MI=MB=MC$, and $M$ is the circumcenter of $\triangle IBC$.

Since $M$ is the circumcenter of $\triangle IBC$ and lies on $AI$, $MI$ is a radius along $AI$. Given $IL \perp AI$, $IL$ is tangent to the circumcircle of $\triangle IBC$ at $I$.

By the Tangent-Chord Theorem, $\angle LIB = \angle ICB = C/2 = \gamma$, and $\angle LIC = \angle IBC = B/2 = \beta$.

We calculate the ratio $BL/LC$ using the Law of Sines in $\triangle IBL$ and $\triangle ICL$:
$BL = IL \sin\gamma/\sin\beta$ and $LC = IL \sin\beta/\sin\gamma$.
$\frac{BL}{LC} = \frac{\sin^2\gamma}{\sin^2\beta}$.

Using standard identities relating half-angles to side lengths, $\frac{\sin^2\gamma}{\sin^2\beta} = \frac{c(s-b)}{b(s-c)} = \frac{c(a+c-b)}{b(a+b-c)}$.

We apply Menelaus' Theorem to $\triangle ABC$ and points $U, V, L$:
$$ \frac{AU}{UB} \cdot \frac{BL}{LC} \cdot \frac{CV}{VA} = \left(\frac{b}{a+c-b}\right) \cdot \left(\frac{c(a+c-b)}{b(a+b-c)}\right) \cdot \left(\frac{a+b-c}{c}\right) = 1. $$
Thus, $L, U, V$ are collinear. Since $X$ is on $LU$ and $Y$ is on $LV$, $L, X, Y$ are collinear. Let $k$ be the line $XY$.

**Part 2: Proving $IP \parallel XY$ using directed angles.**

We use directed angles modulo $180^\circ$, denoted by $\measuredangle(l_1, l_2)$.

**Step 2.1: Prove $I, X, P, Y$ are concyclic.**

$X$ is on the circumcircle $(ILC)$, so $I, L, C, X$ are concyclic.
$\measuredangle(IX, IL) = \measuredangle(CX, CL)$.
$Y$ is on the circumcircle $(ILB)$, so $I, L, B, Y$ are concyclic.
$\measuredangle(IL, IY) = \measuredangle(BL, BY)$.

$L, B, C$ are on $BC$, so $CL=BL=BC$. $P = XC \c

[Note: response truncated to first 3000 characters of 4384]
