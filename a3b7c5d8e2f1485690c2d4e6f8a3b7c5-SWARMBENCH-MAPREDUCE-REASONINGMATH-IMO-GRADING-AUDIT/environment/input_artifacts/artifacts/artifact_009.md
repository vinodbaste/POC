# artifact_009

Grading ID: GB-0143  
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

Let $\alpha = \angle XYZ$. We are given that $\alpha$ is an acute angle, so $\alpha \in (0, \pi/2)$, and $\alpha \ne 60^\circ$. Let $Y$ be the origin of the complex plane. Let the ray $\overrightarrow{YX}$ be the positive real axis, and the ray $\overrightarrow{YZ}$ be given by complex numbers $z$ such that $\arg(z) = \alpha$.

A point $A$ inside $\angle XYZ$ is represented by a complex number $a = |a|e^{i\phi}$ with $|a|>0$ and $0 < \phi < \alpha$.
A point $B$ on the ray $\overrightarrow{YX}$ is represented by a positive real number $b$.
A point $C$ on the ray $\overrightarrow{YZ}$ is represented by a complex number $c = |c|e^{i\alpha}$ with $|c|>0$.

The condition $\angle BAC = \alpha$ is an equality of unoriented angles. In terms of complex numbers, this means that the argument of the ratio of vectors $\vec{AC}$ to $\vec{AB}$ is either $\alpha$ or $-\alpha$.
So, we must have $\arg\left(\frac{c-a}{b-a}\right) = \pm\alpha \pmod{2\pi}$.

Let's analyze these two cases:

Case 1: $\arg\left(\frac{c-a}{b-a}\right) = \alpha$.
This implies $\frac{c-a}{b-a} = k e^{i\alpha}$ for some real number $k>0$.
Rearranging, we get $c-a = k(b-a)e^{i\alpha}$.
Since $c = |c|e^{i\alpha}$, we can divide by $e^{i\alpha}$:
$|c| - a e^{-i\alpha} = k(b-a)$.
The imaginary part of the right side is $\text{Im}(k(b-a)) = -k\text{Im}(a) = -k|a|\sin\phi$.
The imaginary part of the left side is $\text{Im}(|c| - a e^{-i\alpha}) = -\text{Im}(|a|e^{i(\phi-\alpha)}) = -|a|\sin(\phi-\alpha) = |a|\sin(\alpha-\phi)$.
Equating the imaginary parts: $|a|\sin(\alpha-\phi) = -k|a|\sin\phi$.
Since $A$ is inside the angle, $|a|>0$, $0 < \phi < \alpha$. This implies $\sin\phi > 0$ and $\sin(\alpha-\phi) > 0$.
The left side of the equation is positive. The right side is negative since $k>0$.
This is a contradiction. So, this case is impossible for points $B,C$ on the given rays.

Case 2: $\arg\left(\frac{c-a}{b-a}\right) = -\alpha$.
This is equivalent to $\arg\left(\frac{b-a}{c-a}\right) = \alpha$.
This implies $\frac{b-a}{c-a} = k e^{i\alpha}$ for some real $k>0$.
$b-a = k(c-a)e^{i\alpha}$. Since $b$ is real, its imaginary part is 0.
$\text{Im}(a + k(c-a)e^{i\alpha}) = 0$.
$\text{Im}(a + k|c|e^{i2\alpha} - kae^{i\alpha}) = 0$.
Let $a = a_x+ia_y$.
$a_y + k|c|\sin(2\alpha) - k\text{Im}(ae^{i\alpha}) = 0$.
$a_y + k|c|\sin(2\alpha) - k(a_x\sin\alpha + a_y\cos\alpha) = 0$.
We can solve for $k$ in terms of $|c|$:
$k = \frac{-a_y}{|c|\sin(2\alpha) - (a_x\sin\alpha+a_y\cos\alpha)}$.
Since we need $k>0$, and $a_y>0$, the denominator must be negative. This is true for $|c|$ small enough.
The real part of the equation for $b$ is:
$b = a_x + k\text{Re}((c-a)e^{i\alpha}) = a_x + k(|c|\cos(2\alpha) - (a_x\cos\alpha - a_y\sin\alpha))$.
Substituting $k$, we get a relation between $b$ and $|c|$:
$b-a_x = \frac{-a_y(|c|\cos(2\alpha) - a_x\cos\alpha + a_y\sin\alpha)}{|c|\sin(2\alpha) - a_x\sin\alpha - a_y\cos\alpha}$.
This can be rearranged into the form $|c| = \frac{pb+q}{rb+s}$ for constants $p,q,r,s$ that dep

[Note: response truncated to first 3000 characters of 12060]
