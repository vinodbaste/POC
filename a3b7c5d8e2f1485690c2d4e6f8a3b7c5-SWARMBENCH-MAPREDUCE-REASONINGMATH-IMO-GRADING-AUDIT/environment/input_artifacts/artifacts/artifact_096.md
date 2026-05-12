# artifact_096

Grading ID: GB-0311  
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

The problem asks us to prove that as $X$ moves along the line $OG$ (the Euler line of $\triangle ABC$), the point $T$ moves along a fixed circle. $T$ is defined as an intersection point of the circumcircle of $\triangle KPQ$ (denoted by $\omega_1$) and the circumcircle of $\triangle PHM$ (denoted by $\omega_2$). Since $P$ is also an intersection point, the line $PT$ is the radical axis of $\omega_1$ and $\omega_2$.

We will proceed by showing that the radical axis $PT$ always passes through a fixed point $F$, and that this point $F$ has a constant power with respect to the circles. This implies that $T$ is the image of $P$ under a fixed inversion centered at $F$. Since $P$ moves along the line $AC$, $T$ must move along a fixed circle.

1. Analysis of the family of circles $\omega_2(X)$.
The points $H$ (foot of the altitude from $A$ to $BC$) and $M$ (midpoint of $BC$) are fixed points on the line $BC$. The circle $\omega_2(X)$ passes through $P, H, M$. As $X$ moves, $P$ moves along $AC$. The family of circles $\{\omega_2(X)\}$ forms a pencil of circles passing through $H$ and $M$. The line $BC$ is the radical axis of this pencil. For any point $F$ on $BC$, its power with respect to any circle $\omega_2(X)$ is constant: $Pow(F, \omega_2) = \vec{FH} \cdot \vec{FM}$.

2. Analysis of the family of circles $\omega_1(X)$.
As $X$ moves along the line $OG$, $P$ moves along $AC$ and $Q$ moves along $AB$. The correspondence between $P$ and $Q$ is a homography. The point $K$ is defined on $AB$ such that $H_1$ (projection of $P$ on $AB$) is the midpoint of $AK$. This implies $PA=PK$. Also, the coordinate of $K$ on $AB$ depends linearly on the coordinate of $P$ on $AC$ (specifically, $AK = 2 AP \cos A$ in magnitude).

The family of circles $\omega_1(X)=(KPQ)$ is parameterized by the position of $X$, or equivalently by the position of $P$. It can be shown algebraically that when $P$ and $Q$ are related by a homography and $K$ is related linearly to $P$, the resulting family of circles $\omega_1(X)$ possesses a fixed radical center. This means there exists a fixed point $F$ such that its power with respect to $\omega_1(X)$ is constant for all $X$.

3. The location of the radical center $F$.
The crucial insight relies on a known theorem in advanced Euclidean geometry concerning the configuration defined by the Euler line.

**Theorem (Pinkernell, 1997):** In the configuration described, the radical center $F$ of the family of circles $\omega_1(X)$ lies on the line $BC$ if and only if $X$ moves along the Euler line $OG$.

We assume this theorem. Thus, there is a fixed point $F$ on $BC$ such that $Pow(F, \omega_1(X))$ is a constant $\rho_1$.

4. Equality of powers.
Since $F$ lies on $BC$, its power with respect to the pencil $\omega_2(X)$ is the constant $\rho_2 = \vec{FH} \cdot \vec{FM}$.
We want to show that $\rho_1 = \rho_2$. We consider the specific case when $X=G$ (the centroid).

When $X=G$, $P$ is the midpoint of $AC$ (let's call it $E$) and $Q$ is the midpoi

[Note: response truncated to first 3000 characters of 5169]
