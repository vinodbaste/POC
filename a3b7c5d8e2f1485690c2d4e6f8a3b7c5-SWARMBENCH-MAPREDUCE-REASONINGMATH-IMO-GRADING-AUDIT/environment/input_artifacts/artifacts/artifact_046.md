# artifact_046

Grading ID: GB-0308  
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

This solution relies on properties of power of a point, radical axes, and inversion. We will state and prove the necessary standard theorems.

### Part 1: Preliminary Theorems

**Theorem 1: Power of a Point (PoP)**
*Statement:* For a point $B$ and a circle $\omega$, if a line through $B$ intersects $\omega$ at $Y_1$ and $Y_2$, the product of the directed segment lengths $\vec{BY_1} \cdot \vec{BY_2}$ is constant, independent of the line. This constant is the power of $B$ with respect to $\omega$, $\mathcal{P}(B, \omega)$.

*Proof:* Let $L_1$ intersect $\omega$ at $Y_1, Y_2$ and $L_2$ intersect $\omega$ at $Z_1, Z_2$. By comparing angles in $\triangle BY_1Z_1$ and $\triangle BZ_2Y_2$, we find they are similar because $\angle Y_1BZ_1 = \angle Z_2BY_2$ and $\angle BY_1Z_1 = \angle BZ_2Y_2$ (angles subtended by the same arc $Z_1Y_2$ in $\omega$, or appropriate supplementary angles). Thus, $BY_1/BZ_2 = BZ_1/BY_2$, leading to $BY_1 \cdot BY_2 = BZ_1 \cdot BZ_2$.

**Theorem 2: Radical Center Theorem**
*Statement:* The three radical axes of three circles $\omega_1, \omega_2, \omega_3$, taken pairwise, are concurrent at the radical center. The radical axis of two intersecting circles is their common chord line.

*Proof:* Let $L_{ij}$ be the radical axis of $\omega_i$ and $\omega_j$. Let $R$ be the intersection of $L_{12}$ and $L_{23}$. Since $R \in L_{12}$, $\mathcal{P}(R, \omega_1) = \mathcal{P}(R, \omega_2)$. Since $R \in L_{23}$, $\mathcal{P}(R, \omega_2) = \mathcal{P}(R, \omega_3)$. Therefore, $\mathcal{P}(R, \omega_1) = \mathcal{P}(R, \omega_3)$, so $R \in L_{13}$.

**Theorem 3: Inversion of a Line**
*Statement:* An inversion $\mathcal{I}$ centered at $B$ maps $P$ to $T$ such that $\vec{BP} \cdot \vec{BT} = k$ (constant). The image of a line $L$ not passing through $B$ is a fixed circle passing through $B$.

*Proof:* Let $F$ be the foot of the perpendicular from $B$ to $L$. Let $F' = \mathcal{I}(F)$. $F'$ is fixed. Let $P \in L$ and $T = \mathcal{I}(P)$. We have $\vec{BP} \cdot \vec{BT} = \vec{BF} \cdot \vec{BF'} = k$. This implies $\triangle BFP \sim \triangle BTF'$. Thus, $\angle BTF' = \angle BFP = 90^\circ$. Since $B$ and $F'$ are fixed, $T$ lies on the fixed circle with diameter $BF'$.

### Part 2: The Key Property and Radical Center

We rely on the following geometric property related to the Euler line $OG$:

**Key Property:** If $X$ lies on the line $OG$, then the points $K, Q, H, M$ are concyclic.

Let $\Gamma$ be the circle passing through $K, Q, H, M$.
Let $\omega_1 = \odot(KPQ)$ and $\omega_2 = \odot(PHM)$. $T$ and $P$ are their intersections.

We identify the radical axes of these three circles:

1.  **Radical axis of $\omega_1$ and $\Gamma$:** Both circles contain $K$ and $Q$. By construction, $Q$ is on $AB$. $H_1$ is the projection of $P$ onto $AB$, and $K$ is the reflection of $A$ about $H_1$, so $K$ is also on $AB$. The radical axis is the line $KQ$, which is $AB$.
2.  **Radical axis of $\omega_2$ and $\Gamma$:** Both circles contain $

[Note: response truncated to first 3000 characters of 4550]
