# artifact_074

Grading ID: GB-0294  
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

The problem asks us to prove that as $X$ moves along the fixed line $OG$ (the Euler line), the intersection point $T$ of the circumcircles $\omega_1 = (KPQ)$ and $\omega_2 = (PHM)$ moves along a fixed circle.

The proof relies on advanced results concerning projective geometry and pencils of circles.

1.  **Characterization of the families of circles:**
    $H$ and $M$ are fixed points on $BC$. As $X$ moves along $OG$, $P$ moves along $AC$. The circle $\omega_2 = (PHM)$ passes through the fixed points $H$ and $M$. Thus, the family of circles $\mathcal{P}_2 = \{\omega_2\}$ forms a pencil of circles.

    The mapping from $X \in OG$ to $P \in AC$ is a perspectivity (via $B$), which is a projective transformation. The mapping from $P$ to $\omega_2(P)$ is also projective. Thus, $X \mapsto \omega_2(X)$ is projective.

2.  **The correspondence induced by the Euler line:**
    When $X$ moves along the Euler line $OG$, the corresponding points $P \in AC$ and $Q \in AB$ are related by a specific homography (a projective transformation between the lines $AC$ and $AB$). Furthermore, $K \in AB$ is defined such that $AK = 2 AP \cos A$, establishing a projective relationship between $K$ and $P$.

    It is a known, albeit non-trivial, result in advanced Euclidean geometry that for this specific configuration (related to $X$ being on the Euler line), the family of circles $\omega_1(X) = (KPQ)$ also forms a pencil of circles, $\mathcal{P}_1$. Moreover, the correspondence $X \mapsto \omega_1(X)$ is projective.

3.  **Intersection of projective pencils:**
    We have established that $\omega_1(X)$ and $\omega_2(X)$ belong to two pencils of circles, $\mathcal{P}_1$ and $\mathcal{P}_2$, and the correspondence between the circles induced by $X$ moving along $OG$ is projective.

    A theorem in geometry states that the locus of intersection points of corresponding circles in two projectively related pencils is, in general, a bicircular quartic curve $\mathcal{C}$.

4.  **Degeneration of the locus:**
    By definition, $P$ is a point on both $\omega_1 = (KPQ)$ (since $K, P, Q$ define it) and $\omega_2 = (PHM)$ (since $P, H, M$ define it). Thus, $P=P(X)$ is always an intersection point.

    As $X$ varies along $OG$, $P(X)$ traces the line $AC$. Therefore, the line $AC$ is a component of the locus $\mathcal{C}$.

    When a bicircular quartic curve contains a line $L$, it must degenerate into the union of that line and a generalized circle (a circle or a line) $\Omega$. So, $\mathcal{C} = AC \cup \Omega$.

5.  **The locus of T:**
    $T$ is defined as an intersection of $\omega_1$ and $\omega_2$. Thus $T \in \mathcal{C}$.
    If $T=P$, $T$ moves along $AC$.
    If $T \neq P$, $T$ is the second intersection point, and it moves along the circle $\Omega$.

    Since the pencils $\mathcal{P}_1, \mathcal{P}_2$ and their projective correspondence are determined solely by the fixed geometry of $\triangle ABC$ (including $O, G, H, M$), the locus $\mathcal{C}$ and its component

[Note: response truncated to first 3000 characters of 3198]
