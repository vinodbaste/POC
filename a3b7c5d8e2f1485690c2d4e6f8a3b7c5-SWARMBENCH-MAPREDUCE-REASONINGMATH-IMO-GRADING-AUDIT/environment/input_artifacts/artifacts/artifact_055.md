# artifact_055

Grading ID: GB-0144  
Problem ID: PB-Advanced-005  
Source: Novel Problem  
IMO Area: Number_Theory

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $\angle XYZ$ be an acute angle with $\angle XYZ \ne 60^\circ$, and let $A$ be a point inside $\angle XYZ$. Prove that there exists $D\ne A$ inside $\angle XYZ$ and $\theta\in (0,2\pi )$ satisfying the following condition:

 For points $B$ and $C$ on the rays $\overrightarrow{YX}$ and $\overrightarrow{YZ}$ respectively, then
 \[
 \angle BAC = \angle XYZ \quad \implies \quad \angle BDC = \theta.
 \]

## Reference Solution (for grader's calibration)

step 1: Construction of $D$ and $\theta$

 step 1-1: Without loss of generality we may assume that $XA\perp YZ$
 and $ZA\perp YX$.

 step 1-2: Let $D$ be the circumcenter of $\triangle XYZ$.

 step 1-3: Let $\theta=180^{\circ}-2\angle XYZ$.

 \medskip{}

 step 2: We prove that if $\angle BAC=\angle XYZ$, then $\angle BDC=\theta$.

 \medskip{}

 step 3: Lemma. A point $K$ inside a convex quadrilateral $PQRS$
 has an isogonal conjugate with respect to the $PQRS$ if and only
 if $\angle PKQ+\angle RKS=180^{\circ}$.

 \medskip{}

 step 4: Proof of Lemma.

 step 4-1: Let $H_{1},H_{2},H_{3},H_{4}$ be the feet of perpendicular
 from $K$ onto $PQ,QR,RS,SP$, respectively.

 step 4-2: First assume that $K^{\prime}$ is the isogonal conjugate
 of $K$

 step 4-2-1: Let $H_{1}^{\prime},H_{2}^{\prime},H_{3}^{\prime},H_{4}^{\prime}$
 be the feet of perpendicular from $K^{\prime}$ onto $PQ,QR,RS,SP$,
 respectively.

 step 4-2-2: We prove that $H_{1},H_{2},H_{1}^{\prime},H_{2}^{\prime}$
 are cyclic.

 step 4-2-2-1: We have $\angle KQH_{1}=\angle K^{\prime}QH_{2}^{\prime}$
 by assumption.

 step 4-2-2-2: We have $\angle KH_{1}Q=\angle K^{\prime}H_{2}^{\prime}Q=90^{\circ}$.

 step 4-2-2-3: By steps 4-2-2-1 and 4-2-2-2, we have $\triangle KQH_{1}\sim\triangle K^{\prime}QH_{2}^{\prime}$.

 step 4-2-2-4: Thus $QH_{1}:QH_{2}^{\prime}=KQ:K^{\prime}Q$.

 step 4-2-2-5: Similarly $QH_{1}^{\prime}:QH_{2}=KQ:K^{\prime}Q$.

 step 4-2-2-6: By steps 4-2-2-4 and 4-2-2-5, we have $QH_{1}\times QH_{1}^{\prime}=QH_{2}\times QH_{2}^{\prime}$.

 step 4-2-2-7: Hence $H_{1},H_{2},H_{1}^{\prime},H_{2}^{\prime}$ are
 cyclic.

 step 4-2-3: Denote $M$ as the midpoint of $KK^{\prime}$.

 step 4-2-4: We prove that $H_{1},H_{1}^{\prime},H_{2},H_{2}^{\prime}$
 are equidistant to $M$.

 step 4-2-4-1: Let $N$ be the midpoint of $H_{1}H_{1}^{\prime}$.

 step 4-2-4-2: Since $H_{1}K\parallel H_{1}^{\prime}K^{\prime}$ and
 both are perpendicular to $PQ$, we have $NM\perp PQ$.

 step 4-2-4-3: Hence $M$ lies on the perpendicular bisector of $H_{1}H_{1}^{\prime}$.

 step 4-2-4-4: Similarly $M$ lies on the perpendicular bisector of
 $H_{2}H_{2}^{\prime}$.

 step 4-2-4-5: By steps 4-2-2, 4-2-4-3, 4-2-4-4 and the fact that $PQ$
 and $QR$ are not parallel, we have that the center should be $M$.

 step 4-2-5: Similarly $H_{2},H_{2}^{\prime},H_{3},H_{3}^{\prime}$
 are equidistant to $M$, and $H_{3},H_{3}^{\prime},H_{4},H_{4}^{\prime}$
 are equidistant to $M$.

 step 4-2-6: By steps 4-2-4 and 4-2-5, $H_{1},H_{1}^{\prime},H_{2},H_{2}^{\prime},H_{3},H_{3}^{\prime},H_{4},H_{4}^{\prime}$
 all lie on a circle centered at $M$.

 step 4-2-7: Since $\angle KH_{1}Q=\angle KH_{2}Q=90^{\circ}$, $K,H_{1},Q,H_{2}$
 are cyclic.

 step 4-2-8: Similarly $K,H_{2},R,H_{3}$ are cyclic.

 step 4-2-9: Similarly $K,H_{3},S,H_{4}$ are cyclic.

 step 4-2-10: Similarly $K,H_{4},P,H_{1}$ are cyclic.

 step 4-2-11: By steps 4-2-6, 4-2-7, 4-2-8, 4-2-9, and 4-2-10, we have
 \begin{align*}
 \angle PKQ+\angle RKS&=(\angle PKH_{1}+\angle QKH_{1})+(\angle RKH_{3}+\angle SKH_{3})
 &=\angle PH_{4}H_{1}+\angle QH_{2}H_{1}+\angle RH_{2}H_{3}+\angle SH_{4}H_{3}
 &=360^{\circ}-(\angle H_{1}H_{2}H_{3}+\angle H_{3}H_{4}H_{1})=180^{\circ}.
 \end{align*}
 step 4-3: Assume $\angle PKQ+\angle RKS=180^{\circ}$.

 step 4-3-1: By the same logic as in step 4-2, $H_{1},H_{2},H_{3},H_{4}$ lie on a circle $\omega$.

 step 4-3-2: Let $O$ be the center of $\omega$.

 step 4-3-3: Denote $J_{1},J_{2},J_{3},J_{4}$as the second intersection
 of $\omega$ and $PQ,QR,RS,SP$, respectively.

 step 4-3-4: Let $K^{\prime}$ be the reflection of $K$ with respect
 to $O$.

 step 4-3-5: Let $N^{\prime}$ be the midpoint of $H_{1}J_{1}$.

 step 4-3-6: Since $KH_{1}\parallel ON^{\prime}$ and both are perpendicular
 to $PQ$, we have $K^{\prime}J_{1}\perp PQ$.

 step 4-3-7: Similarly $K^{\prime}J_{2}\perp QR$.

 step 4-3-8: Hence $\angle PQK=\angle H_{1}QK=90^{\circ}-\angle H_{1}KQ=90^{\circ}-\angle H_{1}H_{2}Q=90^{\circ}-\angle J_{2}J_{1}Q=\angle RQK^{\prime}$.

 step 4-3-9: Similarly $K,K^{\prime}$ are isogonal with respect to
 all four angles of $PQRS$.

 step 4-3-10: Thus $K^{\prime}$ is the isogonal conjugate of $K$
 with respect to $PQRS$.\medskip{}

 step 5: Now suppose $\angle BAC=\angle XYZ$.

 step 5-1: Since $\angle XYZ$ is acute, $\triangle XYZ$ is acute,
 and $\angle XAY,\angle ZAY>90^{\circ}>\angle BAC$.

 step 5-2: Hence $\square BCZX$ is convex, and $K$ is inside of $\square BCZX$.\medskip{}

 step 6: We prove that $D$ is the isogonal conjugate of $A$ with
 respect to $\square BCZX$.

 step 6-1: We have $\angle ZAX+\angle BAC=(180^{\circ}-\angle XYZ)+\angle XYZ=180^{\circ}$.

 step 6-2: Hence by Lemma and steps 5-2, 6-1, $A$ has an isogonal
 conjugate with respect to $\square BCZX$.

 step 6-3: $A,D$ are isogonal conjugates with respect to $\triangle XYZ$
 as orthocenter and circumcenter.

 step 6-4: By step 6-3, $XA,XD$ are isogonal lines with respect to
 $\angle BXZ$, and $ZA,ZD$ are isogonal lines with respect to $\angle CZX$.

 step 6-5: By steps 6-2, 6-4, and the fact that there is at most one
 isogonal conjugate, we conclude that $D$ is indeed the isogonal conjugate.

 \medskip{}

 step 7: We prove that $\angle BDC=180^{\circ}-2\angle XYZ$.

 step 7-1: By step 6, $A$ is the isogonal conjugate of $D$ with respect
 to $\square BCZX$.

 step 7-2: By Lemma, we have $\angle BDC+\angle XDZ=180^{\circ}$.

 step 7-3: Since $D$ is the circumcenter of $\triangle XYZ$, we have
 $\angle XDZ=2\angle XYZ$.

 step 7-4: By step 7-2 and 7-3, we have $\angle BDC=180^{\circ}-2\angle XYZ$.
 step 7-5: Since $\angle XYZ \ne 60^\circ$, we have $D\ne A$.

## Grading Guidelines

(Partial)
 1. Constructed $D$ and found $\theta$ correctly.
 2. Found the necessary and sufficient conditions for the existence of isogonal conjugate in quadrilateral.
(Almost)
 1. Verification contains minor mistakes only.

## Candidate Response (to be graded)

Let $\alpha = \angle XYZ$. We are given that $\alpha$ is acute ($0 < \alpha < 90^\circ$) and $\alpha \ne 60^\circ$. Let $A$ be a point inside $\angle XYZ$. We want to prove the existence of a point $D\ne A$ inside $\angle XYZ$ and an angle $\theta\in (0,2\pi )$ such that for any points $B$ on the ray $\overrightarrow{YX}$ and $C$ on the ray $\overrightarrow{YZ}$, the condition $\angle BAC = \alpha$ implies $\angle BDC = \theta$.

We analyze the relationship between $B$ and $C$ defined by the condition $\angle BAC = \alpha$. This is a geometric angle, so it is positive.

1. Homography and Conic Envelope.
Let us consider the oriented angles between the lines passing through $A$. The condition $\angle BAC = \alpha$ means that the oriented angle $(AB, AC)$ is either $\alpha$ or $-\alpha$.

The mapping between the line $AB$ and the line $AC$ defined by a constant oriented angle is a homography (specifically, a rotation) in the pencil of lines centered at $A$.
The mapping between a point $B$ on the line $YX$ and the line $AB$ is a perspectivity, which is also a homography. Similarly for $C$ on $YZ$ and $AC$.

Therefore, the correspondence between $B$ on $YX$ and $C$ on $YZ$ is a composition of homographies, thus it is a homography, provided the orientations of the angles are fixed.

A known theorem in projective geometry states that the envelope of the lines $BC$ connecting corresponding points under a homography between two lines $L_1, L_2$ is a conic section $\mathcal{C}$, which is tangent to $L_1$ and $L_2$.

2. Analysis of the orientation.
Let's set up a coordinate system where $Y$ is the origin, $YX$ is the positive x-axis, and $YZ$ is the ray at angle $\alpha$. We assume the orientation is counterclockwise, so $\alpha>0$. $A$ is inside the angle.

We analyze if $B, C$ can be on the rays $\overrightarrow{YX}, \overrightarrow{YZ}$ (i.e., $b=|YB|>0, c=|YC|>0$) for each orientation.

Case 1: The oriented angle $(AB, AC) = \alpha$.
We show this case is impossible. Let $A$ have polar coordinates $(r_A, \phi_A)$ with $0<\phi_A<\alpha$. Using complex numbers, $Y=0, B=b, C=ce^{i\alpha}, A=z_A=r_A e^{i\phi_A}$. The condition is $\arg\frac{C-A}{B-A} = \alpha$. This implies $\frac{ce^{i\alpha}-z_A}{b-z_A} = k e^{i\alpha}$ for some $k>0$.
This leads to the equation $k\sin\phi_A = \sin(\phi_A-\alpha)$.
Since $k>0$ and $\sin\phi_A>0$, the left side is positive. Since $0<\phi_A<\alpha$, $\phi_A-\alpha \in (-\alpha, 0)$, so $\sin(\phi_A-\alpha)<0$. This is a contradiction.
So there are no solutions $(B, C)$ on the rays corresponding to this orientation (except possibly the boundary cases $B=Y$ or $C=Y$).

Case 2: The oriented angle $(AB, AC) = -\alpha$.
The condition is $\arg\frac{C-A}{B-A} = -\alpha$. This implies $\frac{ce^{i\alpha}-z_A}{b-z_A} = k e^{-i\alpha}$ for $k>0$.
This leads to a system of equations for $b, c$ parameterized by $k$. We analyze the existence of solutions $b>0, c>0, k>0$.
It turns out that solutions exist if and only if $\cos\alpha > \cos

[Note: response truncated to first 3000 characters of 6354]
