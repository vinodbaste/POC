# artifact_106

Grading ID: GB-0138  
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

This problem asks for the existence of a point $D$ inside a given acute angle $\angle XYZ=\alpha$ (with $\alpha \ne 60^\circ$), different from a given interior point $A$, such that the angle $\angle BDC$ is constant whenever $B$ is on $YX$ and $C$ is on $YZ$ satisfying $\angle BAC = \alpha$.

The proof relies on the construction of a specific point $D$, often referred to as the Stammler point or Collings point in this context, and a known theorem about its properties regarding the angle $\angle BDC$.

**1. Construction of D**

Let $\alpha = \angle XYZ$. We set up a coordinate system using complex numbers, with the vertex $Y$ at the origin (0) and the ray $YX$ along the positive real axis. The ray $YZ$ is along the angle $\alpha$.
Let $A$ be represented by the complex number $a$. Since $A$ is inside the angle, $a = r e^{i\phi}$ with $r>0$ and $0 < \phi < \alpha$.

1. Let $A_X$ be the reflection of $A$ across $YX$. $A_X$ corresponds to $\bar{a} = r e^{-i\phi}$.
2. Let $A_Z$ be the reflection of $A$ across $YZ$. $A_Z$ corresponds to $e^{i2\alpha}\bar{a} = r e^{i(2\alpha-\phi)}$.
3. Let $D$ be the reflection of $Y$ (the origin) across the line $A_X A_Z$.

Since $YA_X = | \bar{a} | = r$ and $YA_Z = |e^{i2\alpha}\bar{a}| = r$, the triangle $\triangle Y A_X A_Z$ is isosceles. The reflection $D$ of $Y$ across $A_X A_Z$ forms a rhombus $Y A_X D A_Z$.
In complex numbers, $D$ is given by $d = a_X + a_Z$.
$d = \bar{a} + e^{i2\alpha}\bar{a} = \bar{a}(1+e^{i2\alpha})$.
$d = \bar{a} e^{i\alpha}(e^{-i\alpha}+e^{i\alpha}) = \bar{a} e^{i\alpha} (2\cos\alpha)$.

**2. Verification that D is inside $\angle XYZ$**

Substituting $a = r e^{i\phi}$:
$d = (r e^{-i\phi}) e^{i\alpha} (2\cos\alpha) = (2r\cos\alpha) e^{i(\alpha-\phi)}$.

Since $\alpha$ is acute ($0 < \alpha < \pi/2$), $\cos\alpha > 0$. Since $r>0$, $|d| = 2r\cos\alpha > 0$.
The argument of $D$ is $\arg(d) = \alpha-\phi$.
Since $A$ is inside the angle, $0 < \phi < \alpha$. This implies $0 < \alpha-\phi < \alpha$.
Thus, $D$ is strictly inside (in the interior of) $\angle XYZ$.

**3. Verification that $D \ne A$**

We check when $D=A$.
$d=a \iff (2r\cos\alpha) e^{i(\alpha-\phi)} = r e^{i\phi}$.
Since $r>0$, we must have equality of magnitudes and arguments.
Magnitudes: $2\cos\alpha = 1$, so $\cos\alpha = 1/2$. Since $\alpha$ is acute, $\alpha = 60^\circ$.
Arguments: $\alpha-\phi = \phi$, so $2\phi = \alpha$. $A$ must be on the angle bisector.

$D=A$ if and only if $\alpha=60^\circ$ and $A$ is on the angle bisector.
The problem states that $\angle XYZ \ne 60^\circ$. Therefore, $D \ne A$.

**4. Constancy of $\angle BDC$ (The Collings-Stammler Theorem)**

We now rely on a known theorem in geometry concerning the point $D$ constructed above.

*Theorem:* Let $D$ be the Stammler point constructed from $A$. If $B$ is on $YX$ and $C$ is on $YZ$ such that $\angle BAC = \alpha$, then $\angle BDC = 2\alpha$ (or $2\pi-2\alpha$).

*Detailed explanation based on orientations:*
The condition $\angle BAC = \alpha$ (undirected an

[Note: response truncated to first 3000 characters of 4430]
