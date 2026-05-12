# artifact_088

Grading ID: GB-0923  
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

Here is a detailed synthetic proof.

**1. Setup and Definitions**

Let $H$ be the orthocenter of $\triangle ABC$. Let $AD$ be the altitude from $A$ to $BC$, and $CF$ be the altitude from $C$ to $AB$. $H$ is the intersection of these altitudes.
*   $AH \perp BC$.
*   $F$ is on $AB$, and $CF \perp AB$. $H$ lies on the line $CF$.
$P$ is the reflection of $H$ across the line $BC$.
Let $\Omega$ be the circumcircle of $\triangle AFP$, and let $O_\Omega$ be its center.
$X$ and $Y$ are the intersection points of $\Omega$ with the line $BC$.

We want to prove that $C$ is the midpoint of the chord $XY$.

**2. Strategy**

The segment $XY$ is a chord of the circle $\Omega$ lying on the line $BC$. A point $C$ on the chord $XY$ is the midpoint if and only if the line connecting the center $O_\Omega$ to $C$ is perpendicular to the chord. Thus, we need to prove $O_\Omega C \perp BC$.

Since $AH$ is the altitude to $BC$, we have $AH \perp BC$. Therefore, proving $C$ is the midpoint of $XY$ is equivalent to proving $O_\Omega C \parallel AH$. We will use the Midpoint Theorem to establish this parallelism.

**3. Properties of P and Introduction of Auxiliary Point K**

First, we analyze the properties of $P$, the reflection of $H$ across $BC$:
1.  Since $C$ lies on the axis of reflection $BC$, $C$ is equidistant from $H$ and $P$. Thus, $CH = CP$.
2.  Since $H$ lies on the altitude $AD$ ($AD \perp BC$), its reflection $P$ across $BC$ must also lie on the line $AD$. Thus, $A, H, P$ are collinear.

To utilize the Midpoint Theorem, we introduce an auxiliary point $K$, defined as the reflection of $H$ across the point $C$.

*   By definition, $C$ is the midpoint of $HK$, so $CH = CK$.
*   Since $H$ and $C$ both lie on the altitude line $CF$, $K$ must also lie on the line $CF$. Thus, $F, C, H, K$ are collinear.
*   Combining the equalities, we have $CH = CP = CK$.

**4. Proving AK is the Diameter of $\Omega$**

We aim to apply the Midpoint Theorem to $\triangle AHK$. We know $C$ is the midpoint of $HK$. If we can show that $O_\Omega$ (the center of $\Omega$) is the midpoint of $AK$, then $O_\Omega C \parallel AH$.

To show $O_\Omega$ is the midpoint of $AK$, we must prove that $AK$ is the diameter of $\Omega = (AFP)$. We do this by showing that $AK$ subtends right angles at $F$ and $P$.

*   **Proof that $\angle AFK = 90^\circ$:**
    $F$ is the foot of the altitude $CF$, so $CF \perp AB$. Since $K$ lies on the line $CF$, the line $KF$ is the same as $CF$. $AF$ lies on $AB$. Thus, $KF \perp AF$.
    Therefore, $\angle AFK = 90^\circ$.

*   **Proof that $\angle APK = 90^\circ$:**
    Consider $\triangle HPK$. $C$ is the midpoint of $HK$. We established that $CH = CP = CK$.
    In $\triangle HPK$, $CP$ is the median to the side $HK$. Since the median $CP$ is half the length of the side $HK$ ($CP = HK/2$), $\triangle HPK$ must be a right triangle with the right angle at $P$.
    Thus, $\angle HPK = 90^\circ$.
    Since $A, H, P$ are collinear, $\angle APK = \angle HPK = 90^\c

[Note: response truncated to first 3000 characters of 4133]
