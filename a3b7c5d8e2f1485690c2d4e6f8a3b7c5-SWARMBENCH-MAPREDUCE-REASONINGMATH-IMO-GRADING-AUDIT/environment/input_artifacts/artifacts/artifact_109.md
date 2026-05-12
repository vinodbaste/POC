# artifact_109

Grading ID: GB-0324  
Problem ID: PB-Advanced-010  
Source: Novel Problem  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $O$ and $G$ be the circumcenter and centroid of a non-isosceles triangle $ABC$, respectively. Let $H$ be the foot of the perpendicular from $A$ to $BC$, and let $M$ be the midpoint of $BC$. For a point $X$ on the line $OG$, let the line $BX$ intersect $AC$ at $P$, and let the line $CX$ intersect $AB$ at $Q$. Let $H_1$ be the foot of the perpendicular from $P$ to the line $AB$, and let $K$ be the reflection of $A$ about $H_1$. Let $T$ be the intersection of the circumcircle of triangle $KPQ$ and the circumcircle of triangle $PHM$. Prove that as $X$ moves along the line $OG$, $T$ moves along a fixed circle.

## Reference Solution (for grader's calibration)

The most difficult part of this problem is to observe that $(B, T, P, C)$ are concyclic. If this holds, let $Y$ be the intersection of $TP$ and $BC$. Then $YH \cdot YM = YT \cdot YP = YB \cdot YC$,
 which means that $Y$ is the point such that $(B, H, C, Y)$ is a harmonic division. This is a fixed point. Thus, $T$ lies on the inversion of $AC$ with respect to the circle centered at $Y$ with radius $\sqrt{YB \cdot YC}$. This is a fixed circle.

 \textbf{Claim:} $(B, T, P, C)$ are concyclic. This means that the circumcircles of $\triangle BPC$, $\triangle PHM$, and $\triangle KPQ$ are coaxial. We will use the following well-known Lemma: For two circles, the locus of points where the ratio of the powers with respect to the two circles is constant is a circle coaxial with the two circles.
 Now, using the Lemma, we see that it suffices to show that: The ratio of the powers of $B$ and $C$ with respect to the circumcircles of $\triangle PHM$ and $\triangle KPQ$ are the same.

 1) The ratio of powers of $B$ and $C$ with respect to the circumcircle of $\triangle PHM$ is $\frac{BH \cdot BM}{CH \cdot CM} = \frac{BH}{CH}$.

 2) Let's compute the ratio of powers of $B$ and $C$ with respect to the circumcircle of $\triangle KPQ$. Let $H_2$ be the foot of the perpendicular from $Q$ to $AC$, and let $L$ be the reflection of $A$ across $H_2$. Since $\angle QKP = \angle QLP = 180^\circ - \angle A$, $(K, L, P, Q)$ are concyclic. The power of $B$ is $BK \cdot BQ$, and the power of $C$ is $CL \cdot CP$. We want to show that $\frac{CL \cdot CP}{BK \cdot BQ} = \frac{CH}{BH}$.

 Let $D, E$ be the intersection of the Euler line of $\triangle ABC$ with $AB, AC$ respectively. Let $R$ be the intersection of $AX$ and $BC$.
 By Ceva's theorem, $\frac{CP}{BQ} = \frac{AP}{AQ} \times \frac{CR}{BR}$. $BK = BA - KA = BA - 2AP \cos A$, $CL = CA - LA = CA - 2AQ \cos A$.
 Thus $\frac{CL \cdot CP}{BK \cdot BQ} = \frac{CA - 2AQ \cos A}{BA - 2AP \cos A} \times \frac{AP}{AQ} \times \frac{CR}{BR} = \frac{\frac{CA}{AQ} - 2 \cos A}{\frac{BA}{AP} - 2 \cos A} \times \frac{CR}{BR}$.

 Let $\frac{XE}{DX} = \lambda$.
 $\frac{CR}{BR} = \frac{AC \sin \angle CAR}{AB \sin \angle BAR} = \frac{AC}{AB} \cdot \frac{AD}{AE} \cdot \frac{XE}{DX} = \frac{AC \cdot AD}{AB \cdot AE} \lambda$.
 By Menelaus' theorem on $\triangle ADE$ and line $CXQ$,
 $\frac{AQ}{QD} \cdot \frac{CE}{AC} \cdot \frac{DX}{EX} = 1$. Thus, $\frac{AQ}{QD} = \frac{AC}{CE} \lambda$, so $AQ = \frac{1}{1 + \frac{AC}{CE} \lambda} AD = \frac{AD}{1+\lambda \frac{AC}{CE}}.$
 Similarly, $AP = \frac{1}{1 + \frac{1}{\lambda} \frac{AB}{BD}} AE$.
 Thus $\frac{CL \cdot CP}{BK \cdot BQ} = \frac{\frac{CA}{AQ} - 2 \cos A}{\frac{BA}{AP} - 2 \cos A} \times \frac{CR}{BR}$ has the form $\frac{(\text{linear in } \lambda)}{(\text{linear in } \lambda)}$. That is, if it is $\frac{CH}{BH}$ for two values of $\lambda$, then it is $\frac{CH}{BH}$ for all $\lambda$.

 Case 1) $X = H$.
 In this case, $P, Q$ are the feet of the altitudes from $B, C$ respectively. Thus $KL \parallel BC$. Thus $\frac{CL \cdot CP}{BK \cdot BQ} = \frac{CH \cdot CB}{BH \cdot BC} = \frac{CH}{BH}$.

 Case 2) $X = G$.
 In this case, $P, Q$ are the midpoints of $AC, AB$, and $K, L$ are the feet of altitudes from $C, B$ respectively. Thus $\frac{CL \cdot CP}{BK \cdot BQ} = \frac{CH \cdot \frac{CB}{2}}{BH \cdot \frac{BC}{2}} = \frac{CH}{BH}$.
 Since $H \neq G$ due to scalene condition, we have two different values of $\lambda$, completing the proof.

## Grading Guidelines

(Partial)
 1. Proved that $B, T, P, C$ lie on a circle.
 2. Observed that it suffices to show that the ratio of powers of $B$ and $C$ respect to the circumcircles of $\triangle PHM$ and $\triangle KPQ$ are the same.
(Almost)
 1. In addition to items 1 and 2 of (Partial), observed that it is enough to prove $2$ of (Partial) only for two different $X$.
 2. Verification contains minor mistakes only.

## Candidate Response (to be graded)

**Outcome 1: COMPLETE PROOF**

We want to prove that $T$ moves along a fixed circle as $X$ moves along the line $OG$. We will show that there exists a fixed point $F$ on the line $BC$ such that $T$ is the image of $P$ under a fixed inversion centered at $F$.

**Step 1: Setup and Powers of B and C**

Let $A$ be the origin. We use signed distances along the lines $AB$ and $AC$. Let $c=AB$ and $b=AC$. Let $p=AP$ and $q=AQ$. Let $\gamma = \cos A$.

$H_1$ is the projection of $P$ onto $AB$. $AH_1 = p\gamma$. $K$ is the reflection of $A$ about $H_1$. $K$ is on $AB$ and $AK = 2p\gamma$.

Let $\omega_1(X) = \odot(KPQ)$. We calculate the power of $B$ and $C$ with respect to $\omega_1(X)$.

$P_B(X) = \vec{BK} \cdot \vec{BQ} = (AK-AB)(AQ-AB) = (2p\gamma - c)(q-c)$.
$P_B(p, q) = 2\gamma pq - 2c\gamma p - cq + c^2$.

To find $P_C(X)$, we first find the power of $A$. $P_A(X) = \vec{AK} \cdot \vec{AQ} = 2p\gamma q$.
Let $P'$ be the second intersection of $AC$ with $\omega_1(X)$. $P_A(X) = \vec{AP} \cdot \vec{AP'} = p \cdot AP'$. Assuming $P\neq A$, $AP' = 2q\gamma$.
$P_C(X) = \vec{CP} \cdot \vec{CP'} = (p-b)(2q\gamma-b)$.
$P_C(p, q) = 2\gamma pq - bp - 2b\gamma q + b^2$.

$P_B$ and $P_C$ are bilinear functions of $p$ and $q$.

**Step 2: Homography and Linear Dependence**

$X$ is the intersection of $BP$ and $CQ$. As $X$ moves along the fixed line $OG$, the correspondence between $P$ on $AC$ and $Q$ on $AB$ is a projective transformation (a homography). This means $p$ and $q$ satisfy a fixed bilinear relation $H(p, q) = 0$.

The space $V$ of bilinear functions $f(p,q) = C_1 pq + C_2 p + C_3 q + C_4$ has dimension 4. The functions $H(p, q)$, $P_B(p, q)$, $P_C(p, q)$, and $1$ are in $V$. Thus, there is a non-trivial linear dependence:
$\lambda H(p, q) + \alpha P_B(p, q) + \beta P_C(p, q) + \delta = 0$, holding identically for all $p, q$.

We must show $\lambda \neq 0$. If $\lambda=0$, then $\alpha P_B + \beta P_C + \delta = 0$ identically. Comparing the coefficients of $pq$: $2\gamma(\alpha+\beta)=0$.

Case 1: $\gamma = \cos A \neq 0$ ($A \neq 90^\circ$). Then $\alpha+\beta=0$. Let $\beta=1, \alpha=-1$.
$P_C - P_B + \delta = 0$.
$P_C - P_B = p(2c\gamma-b) + q(c-2b\gamma) + (b^2-c^2)$.
For this to be constant $(-\delta)$ for all $p, q$, the coefficients of $p$ and $q$ must be zero.
$b=2c\gamma$ and $c=2b\gamma$. Substituting $\gamma=c/(2b)$ into the first equation gives $b=2c(c/(2b))$, so $b^2=c^2$. Since lengths are positive, $b=c$. This contradicts that $\triangle ABC$ is non-isosceles.

Case 2: $\gamma = 0$ ($A=90^\circ$). $P_B = -cq+c^2, P_C = -bp+b^2$.
$\alpha(-cq+c^2) + \beta(-bp+b^2) + \delta = 0$ for all $p, q$.
This requires the coefficients of $p$ and $q$ to be zero: $\beta b=0$ and $\alpha c=0$. Since $b, c \neq 0$, $\alpha=\beta=0$. Then $\delta=0$. This contradicts the non-triviality of the dependence.

Thus, $\lambda \neq 0$. We can normalize so $\lambda=1$.

**Step 3: Existence of a Fixed Center F**

When $X \in OG$, $H(p(X), q(X))=0$. The identity b

[Note: response truncated to first 3000 characters of 5729]
