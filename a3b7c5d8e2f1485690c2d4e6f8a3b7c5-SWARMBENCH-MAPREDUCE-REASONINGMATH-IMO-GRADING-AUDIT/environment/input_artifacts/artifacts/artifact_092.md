# artifact_092

Grading ID: GB-0932  
Problem ID: PB-Advanced-028  
Source: USAMO 2025  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $H$ be the orthocenter of acute triangle $ABC$, let $F$ be
 the foot of the altitude from $C$ to $AB$, and let $P$ be the reflection
 of $H$ across $BC$. Suppose that the circumcircle of triangle $AFP$
 intersects line $BC$ at two distinct points $X$ and $Y$. Prove
 that $C$ is the midpoint of $XY$.

## Reference Solution (for grader's calibration)

Let $Q$ be the antipode of $B$ in the circumcircle of $ABC$.


 \textbf{Claim.} $AHQC$ is a parallelogram, and $APCQ$ is an isosceles
 trapezoid.



  \emph{Proof.} The claim follows from $\overline{AH}\perp\overline{BC}\perp\overline{CQ}$
 and $\overline{CF}\perp\overline{AB}\perp\overline{AQ}$.


 Let $M$ be the midpoint of $\overline{QC}$.


 \textbf{Claim.} Point $M$ is the circumcenter of $\triangle AFP$.


 \emph{Proof.} It's clear that $MA=MP$ from the isosceles trapezoid
 $APCQ$. As for $MA=MF$, let $N$ denote the midpoint of $\overline{AF}$;
 then $\overline{MN}$ is a midline of the parallelogram, so $\overline{MN}\perp\overline{AF}$.


 Since $\overline{CM}\perp\overline{BC}$ and $M$ is the center of
 $(AFP)$, it follows $CX=CY$.

## Grading Guidelines

(Partial)
  1. Constructed an external point, including the antipode of $B$ w.r.t $(ABC)$ or the antipode of $A$ w.r.t $(AFP)$, that may lead to a solution.
(Almost)
  1. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

Let $D$ be the foot of the altitude from $A$ to $BC$. Since $\triangle ABC$ is acute, the feet of the altitudes $D$ and $F$ lie on the sides $BC$ and $AB$ respectively. The orthocenter $H$ lies inside the triangle.

$H$ lies on the altitude $AD$. $P$ is the reflection of $H$ across the line $BC$. Since $AD \perp BC$, $P$ lies on the line $AD$, and $D$ is the midpoint of $HP$.
Since $H$ is inside the triangle, $A$ and $H$ are on the same side of $BC$. Thus, $P$ is on the opposite side of $BC$ from $A$. Since $A, D, P$ are collinear and $D$ is on $BC$, $D$ must lie on the segment $AP$.

Let $\Omega$ be the circumcircle of $\triangle AFP$. Let $\mathcal{P}(Z)$ denote the power of a point $Z$ with respect to $\Omega$.

We first calculate the power of point $D$. Since $A, P \in \Omega$ and $D$ is on the line $AP$,
$\mathcal{P}(D) = \overline{DA} \cdot \overline{DP}$.
Since $D$ lies between $A$ and $P$, the directed lengths have opposite signs.
$\mathcal{P}(D) = -DA \cdot DP$.
Since $D$ is the midpoint of $HP$, $DP=HD$.
$\mathcal{P}(D) = -DA \cdot HD$.

We use the property of the orthocenter that $DA \cdot HD = DB \cdot DC$. This follows from the similarity of the right triangles $\triangle ADC$ and $\triangle BDH$. Indeed, $\angle CAD = 90^\circ - \angle C$. If $BE$ is the altitude from $B$, then $\angle HBD = \angle EBC = 90^\circ - \angle C$. So $\triangle ADC \sim \triangle BDH$.
Thus, $\mathcal{P}(D) = -DB \cdot DC$.

Next, we calculate the power of point $B$. Since $A, F \in \Omega$ and $B$ is on the line $AF$,
$\mathcal{P}(B) = \overline{BF} \cdot \overline{BA}$.
Since $\triangle ABC$ is acute, $F$ lies between $A$ and $B$.
$\mathcal{P}(B) = BF \cdot BA$.

We relate this expression to the segments on $BC$. Since $\angle ADC = \angle AFC = 90^\circ$, the points $A, C, D, F$ are concyclic. The power of $B$ with respect to this circle is $BF \cdot BA$ and $BD \cdot BC$.
Thus, $BF \cdot BA = BD \cdot BC$.
Therefore, $\mathcal{P}(B) = BD \cdot BC$.

Now we consider the intersections $X$ and $Y$ of $\Omega$ with the line $BC$. We want to show that $C$ is the midpoint of $XY$.
We set up a coordinate system on the line $BC$. Let $C$ be the origin (0). Let the direction towards $B$ be positive. Let $a=BC$. The coordinate of $B$ is $a$.
Let $d=CD$. Since $\triangle ABC$ is acute, $D$ is strictly between $B$ and $C$, so $0 < d < a$. The coordinate of $D$ is $d$.
$DB = a-d$.

Let the coordinates of $X$ and $Y$ be $x$ and $y$. We want to show that $x+y=0$.

We express the powers of $D$ and $B$ using these coordinates and the geometric expressions derived earlier.

For point $D$ (coordinate $d$):
$\mathcal{P}(D) = (x-d)(y-d) = xy - d(x+y) + d^2$.
Geometrically, $\mathcal{P}(D) = -DB \cdot DC = -(a-d)d = -ad+d^2$.
Equating the two expressions:
$xy - d(x+y) + d^2 = -ad+d^2$
$xy - d(x+y) = -ad$. (1)

For point $B$ (coordinate $a$):
$\mathcal{P}(B) = (x-a)(y-a) = xy - a(x+y) + a^2$.
Geometrically, $\mathcal{P}(B) = BD \cdot BC = (a-d)a = a^2-ad$.
Equating the two

[Note: response truncated to first 3000 characters of 3701]
