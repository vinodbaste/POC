# artifact_056

Grading ID: GB-0155  
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

Let $\alpha = \angle XYZ$. We are given that $0 < \alpha < 90^\circ$ and $\alpha \ne 60^\circ$. Let $A$ be a point inside $\angle XYZ$.

We will construct the required point $D$ and angle $\theta$.

**Step 1: Construction of $D$ and $\theta$.**

Let $A_X$ be the reflection of $A$ across the line $YX$, and $A_Z$ be the reflection of $A$ across the line $YZ$.

Since $Y$ lies on both $YX$ and $YZ$, by the properties of reflection, $YA = YA_X$ and $YA = YA_Z$. Thus, $YA = YA_X = YA_Z$.

The angle $\angle A_X Y A_Z$ is formed by rotating the ray $YA$ by an angle $\angle AYX$ away from the angle $\angle XYZ$ to get $YA_X$, and by $\angle AYZ$ away from $\angle XYZ$ to get $YA_Z$.
$\angle A_X Y A_Z = \angle A_X Y X + \angle XYZ + \angle Z Y A_Z$.
Since reflection preserves angles, $\angle A_X Y X = \angle AYX$ and $\angle A_Z Y Z = \angle AYZ$.
Since $A$ is inside $\angle XYZ$, $\angle AYX + \angle AYZ = \angle XYZ = \alpha$.
Thus, $\angle A_X Y A_Z = (\angle AYX + \angle AYZ) + \alpha = \alpha + \alpha = 2\alpha$.

Let $D$ be the circumcenter of $\triangle Y A_X A_Z$. $D$ is uniquely determined by $A$ and $\angle XYZ$.

We define $\theta = 2\alpha$. Since $0 < \alpha < 90^\circ$, $0 < \theta < 180^\circ$, so $\theta \in (0, 2\pi)$.

**Step 2: Verifying the properties of $D$.**

Since $YA_X = YA_Z$, $\triangle Y A_X A_Z$ is isosceles. The circumcenter $D$ lies on the angle bisector of $\angle A_X Y A_Z$. This line $YD$ is also the angle bisector of $\angle XYZ$. Thus, $D$ lies inside $\angle XYZ$.

We must show $D \ne A$. Suppose $D=A$. Then $A$ is the circumcenter of $\triangle Y A_X A_Z$, so $AY = AA_X = AA_Z$.
$AA_X$ is twice the distance from $A$ to the line $YX$. Let $P_X$ be the projection of $A$ onto $YX$. $AA_X = 2 AP_X$.
In the right triangle $\triangle A P_X Y$, $AP_X = AY \sin(\angle AYX)$.
If $AY = AA_X$, then $AY = 2 AY \sin(\angle AYX)$. Since $A$ is inside the angle, $A \ne Y$, so $AY > 0$. We get $\sin(\angle AYX) = 1/2$. Since $\angle AYX < \alpha < 90^\circ$, $\angle AYX = 30^\circ$.
Similarly, $AY = AA_Z$ implies $\angle AYZ = 30^\circ$.
If $D=A$, then $\alpha = \angle AYX + \angle AYZ = 30^\circ + 30^\circ = 60^\circ$.
Since we are given $\alpha \ne 60^\circ$, we must have $D \ne A$.

**Step 3: Analyzing the implication.**

Let $B$ be on $\overrightarrow{YX}$ and $C$ be on $\overrightarrow{YZ}$ such that $\angle BAC = \alpha$.
We have $\angle BYC = \angle XYZ = \alpha$.
Since $A$ is inside $\angle XYZ$, $A$ and $Y$ are on the same side of the line $BC$.
The condition $\angle BAC = \angle BYC$ implies that the points $Y, A, B, C$ are concyclic. Let $\Omega$ be this circumcircle.

**Step 4: Showing $D$ is the center of $\Omega$.**

We show that $A_X$ lies on $\Omega$.
$A_X$ is the reflection of $A$ across $YX$. Since $Y$ and $B$ are on $YX$, $\triangle A_X Y B$ is the reflection of $\triangle A Y B$. Thus, $\angle Y A_X B = \angle Y A B$.

Since $Y, A, B, C$ are on $\Omega$, the angles subtended by the arc $YB$ are equal: $\angle YAB =

[Note: response truncated to first 3000 characters of 4402]
