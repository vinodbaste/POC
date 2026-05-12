# artifact_144

Grading ID: GB-0130  
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

Let $\alpha = \angle XYZ$. We are given that $\alpha$ is an acute angle with $\alpha \ne 60^\circ$, and $A$ is a point inside this angle. We wish to prove the existence of a point $D \ne A$ inside the angle and an angle $\theta \in (0, 2\pi)$ such that for any points $B$ on the ray $\overrightarrow{YX}$ and $C$ on the ray $\overrightarrow{YZ}$, the following implication holds:
\[ \angle BAC = \alpha \quad \implies \quad \angle BDC = \theta. \]

### Step 1: Geometric Interpretation of the Condition

Let $B$ be a point on the ray $\overrightarrow{YX}$ and $C$ be a point on the ray $\overrightarrow{YZ}$, both distinct from the vertex $Y$. A triangle $\triangle YBC$ is formed, and we have $\angle BYC = \alpha$. The premise of the implication is that for such a pair of points $(B, C)$, we have $\angle BAC = \alpha$.

So, the condition is $\angle BAC = \angle BYC$. The point $A$ is specified to be inside the angle $\angle XYZ$. For any non-degenerate choice of $B$ and $C$, the point $A$ lies on the same side of the line $BC$ as the vertex $Y$. The locus of points $P$ on one side of a line segment $BC$ for which the angle $\angle BPC$ is constant is a circular arc passing through $B$ and $C$. Since both $A$ and $Y$ satisfy this condition for the same angle and lie on the same side of $BC$, the four points $Y, B, A, C$ must be concyclic.

Conversely, if the points $Y, B, A, C$ are concyclic, then since $A$ and $Y$ are on the same side of the line $BC$, they must subtend the same angle at the chord $BC$. Thus, $\angle BAC = \angle BYC = \alpha$.

The problem can therefore be reformulated as follows:
*Prove that there exists a point $D \ne A$ inside $\angle XYZ$ and an angle $\theta$ such that for any circle $\omega$ passing through the two fixed points $Y$ and $A$, if this circle intersects the rays $\overrightarrow{YX}$ and $\overrightarrow{YZ}$ at points $B$ and $C$ (distinct from $Y$), then the angle $\angle BDC$ is equal to the constant angle $\theta$.*

### Step 2: Simplification using Geometric Inversion

The problem involves a family of circles all passing through a common point $Y$. This structure is particularly well-suited for the geometric transformation of inversion. Let us perform an inversion, which we denote by $\mathcal{I}$, with respect to a circle centered at $Y$ with an arbitrary radius. For any point $P \ne Y$, its image under this inversion is denoted by $P' = \mathcal{I}(P)$.

We will use the following fundamental properties of inversion, which are standard results in high school geometry:
1.  A line passing through the center of inversion $Y$ is mapped to itself. Thus, the rays $\overrightarrow{YX}$ and $\overrightarrow{YZ}$ are invariant as sets of points.
2.  A circle passing through the center of inversion $Y$ is mapped to a line that does not pass through $Y$. The converse is also true: the inverse image of a line not passing through $Y$ is a circle passing through $Y$.
3.  A fixed point not at the center of inversion is mapped 

[Note: response truncated to first 3000 characters of 10887]
