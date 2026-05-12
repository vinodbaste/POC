# artifact_003

Grading ID: GB-0312  
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

**Outcome 2: STRUCTURED PARTIAL PROGRESS & ANALYSIS**

### 1. Setup and Preliminary Analysis

Let $\omega_1 = \odot(KPQ)$ and $\omega_2 = \odot(PHM)$. $T$ is an intersection of $\omega_1$ and $\omega_2$. $P$ is always an intersection. We generally consider $T$ to be the intersection distinct from $P$.

We analyze how $P, Q, K$ vary as $X$ moves on the Euler line $OG$. $P$ lies on $AC$, $Q$ and $K$ lie on $AB$.

**Lemma 1 (Homographic Dependencies):** The mappings $P \mapsto Q$ and $P \mapsto K$ are homographies (projectivities) between the lines $AC$ and $AB$.

*Proof:*
1.  $P \mapsto Q$: As $X$ moves on the line $OG$, $P = BX \cap AC$ and $Q = CX \cap AB$. The correspondence $P \mapsto X \mapsto Q$ is a composition of perspectivities. Specifically, $P \in AC$ defines the line $BP$. $X$ is the intersection of $BP$ and $OG$. $Q$ is the intersection of $CX$ and $AB$. In projective geometry, this defines a homography between the points on $AC$ and the points on $AB$.

2.  $P \mapsto K$: $H_1$ is the projection of $P \in AC$ onto $AB$. $K$ is the reflection of $A$ about $H_1$. Using vectors originating at $A$, $\vec{H_1} = \text{proj}_{\vec{AB}}(\vec{P})$, and $\vec{K} = 2\vec{H_1}$. This relationship is linear in coordinates. If we parameterize $P$ on $AC$ and $K$ on $AB$ by their distance from $A$, say $p=AP$ and $k=AK$, then $k = 2 p \cos A$. This is a homography.

### 2. Proven Results: The Case $\angle B = 90^\circ$

**Theorem 1:** If $\angle B = 90^\circ$, $T$ is fixed at $B$.

*Proof:* If $\angle B = 90^\circ$, the orthocenter is $B$, so $H=B$. $O$ is the midpoint of $AC$. The Euler line $OG$ is the median $BO$.
Since $X \in BO$, the line $BX$ is $BO$. $P = BX \cap AC = BO \cap AC = O$. $P=O$ is fixed.
$H_1$ is the projection of $P=O$ onto $AB$. Since $O$ is the circumcenter, $H_1$ is $M_c$, the midpoint of $AB$.
$K$ is the reflection of $A$ about $H_1=M_c$. Thus $K=B$.
$\omega_2 = \odot(PHM) = \odot(OBM)$. This is a fixed circle.
$Q = CX \cap AB$ varies as $X$ moves on $BO$.
$\omega_1 = \odot(KPQ) = \odot(BOQ)$.
$T$ is an intersection of $\odot(OBM)$ and $\odot(BOQ)$. The intersections are $O$ and $B$.
Since $P=O$, if we define $T$ as the intersection distinct from $P$, then $T=B$.
As $X$ moves, $T$ remains fixed at $B$. The locus is the point circle $\{B\}$.

[Rigor Score: High]

### 3. Analysis of the General Case: The Generalized Locus Theorem

The general case relies on a powerful theorem concerning the locus of intersections of varying circles.

**Generalized Locus Theorem (C2'):** Let $F_1, F_2$ be fixed points. Let $L_P, L_Q, L_K$ be fixed lines. Let $P \in L_P$. Let $Q=\chi(P) \in L_Q$ and $K=\kappa(P) \in L_K$ be homographies of $P$. Let $T$ be the intersection distinct from $P$ of $\odot(PF_1F_2)$ and $\odot(PKQ)$. Then $T$ moves along a fixed generalized circle (a circle or a line).

We apply this theorem to our setup:
$F_1=H, F_2=M$. $L_P=AC, L_Q=AB, L_K=AB$.
By Lemma 1, $Q$ and $K$ are homographic functions of $P$.
$T$ is the int

[Note: response truncated to first 3000 characters of 5506]
