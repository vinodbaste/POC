# artifact_020

Grading ID: GB-0928  
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

Let $H$ be the orthocenter of the acute triangle $ABC$. Let $AD$ and $CF$ be the altitudes from $A$ to $BC$ and $C$ to $AB$, respectively. Thus, $AD \perp BC$ and $CF \perp AB$. $H$ is the intersection of $AD$ and $CF$.

$P$ is the reflection of $H$ across the line $BC$. Since $H$ lies on $AD$ and $AD \perp BC$, $P$ also lies on the line $AD$. Thus, $A, H, P$ are collinear, and $AP \perp BC$.

Let $\Omega$ be the circumcircle of $\triangle AFP$, and let $O_{\Omega}$ be its center. $\Omega$ intersects the line $BC$ at distinct points $X$ and $Y$. $XY$ is a chord of $\Omega$. To prove that $C$ is the midpoint of $XY$, it suffices to show that $O_{\Omega}C \perp BC$ (by the Chord Bisector Theorem). Since $AH \perp BC$, our goal is to prove $O_{\Omega}C \parallel AH$.

**Step 1: Construction of the auxiliary point K and key equalities.**

Let $K$ be the reflection of $H$ across the point $C$. By definition, $C$ is the midpoint of $HK$. Since $H$ and $C$ lie on the altitude line $CF$, $K$ also lies on the line $CF$.

We establish key equalities involving distances from $C$:
1. By definition of $K$, $CH = CK$.
2. $P$ is the reflection of $H$ across the line $BC$. Since $C$ lies on the line of reflection $BC$, $C$ is equidistant from $H$ and $P$. Thus, $CP = CH$.

Therefore, $CH = CP = CK$.

**Step 2: Proving that K lies on $\Omega$ and AK is a diameter.**

We will show that the quadrilateral $AFPK$ lies on $\Omega$ by demonstrating that it has right angles at $F$ and $P$, making $AK$ a diameter.

i) **Proof that $\angle AFK = 90^\circ$**:
$F$ is the foot of the altitude $CF$, so $CF \perp AB$. Since $K$ lies on the line $CF$, we have $KF \perp AB$. Thus, $\angle AFK = 90^\circ$. (Since $\triangle ABC$ is acute, $\angle A < 90^\circ$, so $A \neq F$.)

ii) **Proof that $\angle APK = 90^\circ$**:
Consider $\triangle HPK$. Since $\triangle ABC$ is acute, $H$ is strictly inside the triangle, ensuring $H, P, K$ are distinct and form a non-degenerate triangle. $C$ is the midpoint of $HK$, so $CP$ is the median to $HK$. From Step 1, $CP = CH = CK = \frac{1}{2} HK$. A triangle in which the length of a median is half the length of the side it bisects is a right triangle. Thus, $\triangle HPK$ is right-angled at $P$, so $\angle HPK = 90^\circ$.
Since $A, H, P$ are collinear (all lying on altitude $AD$), $\angle APK = \angle HPK = 90^\circ$.

Since $\angle AFK = 90^\circ$ and $\angle APK = 90^\circ$, the points $A, F, P, K$ lie on a circle with diameter $AK$. This circle passes through $A, F, P$, so it is $\Omega$.

**Step 3: Applying the Midpoint Theorem.**

Since $AK$ is the diameter of $\Omega$, the center $O_{\Omega}$ is the midpoint of $AK$.

Now consider $\triangle AHK$. Since $\triangle ABC$ is acute, $A$ does not lie on the altitude line $CF$ (which contains $H$ and $K$), so $\triangle AHK$ is non-degenerate.

In $\triangle AHK$:
1. $O_{\Omega}$ is the midpoint of $AK$.
2. $C$ is the midpoint of $HK$.

By the Midpoint Theorem

[Note: response truncated to first 3000 characters of 3589]
