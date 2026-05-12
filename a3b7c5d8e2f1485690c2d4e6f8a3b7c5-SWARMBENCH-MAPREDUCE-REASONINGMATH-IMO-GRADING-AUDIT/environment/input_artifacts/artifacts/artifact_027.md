# artifact_027

Grading ID: GB-0920  
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

**Outcome 1: COMPLETE PROOF**

Let $D$ be the foot of the altitude from $A$ to $BC$. Since $H$ is the orthocenter of $\triangle ABC$, $H$ lies on $AD$. $F$ is the foot of the altitude from $C$ to $AB$.

$P$ is the reflection of $H$ across $BC$. Since $AD \perp BC$ at $D$, $D$ lies on $BC$, and $D$ is the midpoint of $HP$. Furthermore, $A, H, D, P$ are collinear.

Let $\Omega$ be the circumcircle of $\triangle AFP$. $X$ and $Y$ are the intersection points of $\Omega$ with the line $BC$. We aim to prove that $C$ is the midpoint of $XY$. We will use directed lengths along lines, denoted by $\overline{UV}$, and the power of a point with respect to $\Omega$, denoted by $\mathcal{P}_\Omega(K)$.

**Step 1: Calculate the power of point B with respect to $\Omega$.**

Since $A$ and $F$ are on $\Omega$, and $B, F, A$ are collinear on line $AB$,
$$ \mathcal{P}_\Omega(B) = \overline{BF} \cdot \overline{BA}. $$

Since $AD$ and $CF$ are altitudes, $\angle ADC = 90^\circ$ and $\angle AFC = 90^\circ$. Therefore, the points $A, F, D, C$ lie on a circle (the circle with diameter $AC$).
The power of point $B$ with respect to the circle $(AFDC)$ is $\overline{BD} \cdot \overline{BC} = \overline{BF} \cdot \overline{BA}$.

Thus,
$$ \mathcal{P}_\Omega(B) = \overline{BD} \cdot \overline{BC}. \quad (1) $$

**Step 2: Calculate the power of point D with respect to $\Omega$.**

Since $A$ and $P$ are on $\Omega$, and $D$ lies on the line $AP$,
$$ \mathcal{P}_\Omega(D) = \overline{DA} \cdot \overline{DP}. $$
Since $D$ is the midpoint of $HP$, $\overline{DP} = -\overline{DH}$.
$$ \mathcal{P}_\Omega(D) = -\overline{DA} \cdot \overline{DH}. $$

We now relate $\overline{DA} \cdot \overline{DH}$ to segments on $BC$. Let $E$ be the foot of the altitude from $B$ to $AC$.
We have $\angle DAC = 90^\circ - \angle C$ (in right triangle $\triangle ADC$) and $\angle DBH = \angle EBC = 90^\circ - \angle C$ (in right triangle $\triangle BEC$).
Thus, $\angle DAC = \angle DBH$. Since $\angle ADC = \angle BDH = 90^\circ$, we have $\triangle ADC \sim \triangle BDH$.
This implies $AD \cdot DH = BD \cdot DC$.

Since $\triangle ABC$ is acute, the orthocenter $H$ lies inside the triangle. Thus, $H$ is between $A$ and $D$, so $\overline{DA}$ and $\overline{DH}$ have the same direction, meaning $\overline{DA} \cdot \overline{DH} = AD \cdot DH > 0$. Also, $D$ lies between $B$ and $C$, so $\overline{DB}$ and $\overline{DC}$ have opposite directions, meaning $\overline{DB} \cdot \overline{DC} = -BD \cdot DC < 0$.
Therefore, $\overline{DA} \cdot \overline{DH} = -\overline{DB} \cdot \overline{DC}$.

Substituting this into the power equation for $D$:
$$ \mathcal{P}_\Omega(D) = -(-\overline{DB} \cdot \overline{DC}) = \overline{DB} \cdot \overline{DC}. \quad (2) $$

**Step 3: Prove C is the midpoint of XY.**

We establish a coordinate system on the line $BC$. Let $C$ be the origin ($c=0$). Let $b, d, x, y$ be the coordinates of $B, D, X, Y$, respectively. $C$ is the midpoint of $XY$ if and only if $x+y=0$.

T

[Note: response truncated to first 3000 characters of 4117]
