# artifact_110

Grading ID: GB-0512  
Problem ID: PB-Advanced-015  
Source: Novel Problem  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Consider an acute triangle $ABC$ that is not isosceles. Let $H_0$, $E$, and $F$ be the feet of the perpendiculars dropped from vertices $A$, $B$, and $C$ to their opposite sides, respectively. Let $D$ be the point where the incircle of $\triangle ABC$ is tangent to side $ BC $. Denote the incenter and circumcenter of $\triangle ABC$ as $I$ and $O$, respectively. Let $K$ be the intersection of line $IO$ and line $BC$. Let $Q$ be the point where the ray $IH_0$ intersects the circumcircle of $\triangle ABC$ again. Let $X$ be the point where the line $ QD $ intersects the circumcircle of $\triangle ABC$ at a point other than $Q$.
 Let $Y$ be the point where the circle that touches rays $AB$, $AC$, and is also externally tangent to the circumcircle of $\triangle ABC$, touches the circumcircle of $ \triangle ABC$. Prove that if segment $EF$ is tangent to the incircle of $ \triangle ABC$, then $X$, $Y$, and $K$ are collinear.

## Reference Solution (for grader's calibration)

Let $W, V$ be the points where the incircle of $\triangle ABC$ tangent to $AB,AC$, respectively.

 <Step 1> The circumcircle of $\triangle A B C$, the circumcircle of $\triangle A V W$, and the circumcircle of $\triangle A E F$ meet at a point $P$ other than $A$.

 (1) Let $P(\neq A)$ be the intersection of the circumcircle of $\triangle A B C$ and the circumcircle of $\triangle A E F$. Then, $\triangle P E C \sim \triangle P F B(A A)$.

 (2) From the perspective of $\triangle A E F$, the incircle is the excircle, and since $\triangle A B C \sim \triangle A E F$, we have $\frac{F W}{E V}=\frac{B W}{C V}$.

 (3) Therefore, $\frac{B W}{F W}=\frac{C V}{E V}$, so $\triangle P E V \sim \triangle P F W(S A S)$, and by the inscribed angle theorem, we know that $A, V, W, P$ must lie on a circle.


 <Step 2> Using radical axis

 (1) By considering the radical axis of the circumcircle of $\triangle A B C$, the circumcircle of $\triangle A E F$, and $(E, F, B, C)$, we see that $E F, A P, B C$ must be concurrent. Let this point be $R$.

 (2) By considering the radical axis of the circumcircle of $\triangle A B C$, the circumcircle of $\triangle I B C$, and the circumcircle of $\triangle A V W$, we see that $I R$ must be tangent to the circumcircle of $\triangle I B C$.


 <Step 3> $Q$ is the point of tangency between the $A$-inmixtilinear circle of $\triangle A B C$ and the circumcircle.

 (1) $B, H_{0}, C, R$ are harmonic conjugates, so for the midpoint $M$ of $B C, R M \times R H_{0}=R B \times R C$. This is equal to $R I^{2}$ since $R I$ is tangent to the circumcircle of $\triangle I B C$.

 (2) Therefore, $I H_{0}$ is the symmedian of $\triangle I B C$.

 (3) Therefore, $Q$ must be the point of tangency between the $A$-inmixtilinear circle of $\triangle A B C$ and the circumcircle.


 <Step 4> $V, H, W$ are collinear and $H V$ bisects $\angle E H C$.

 Since $\frac{H E}{H C}=\frac{E F}{B C}=\frac{E V}{C V}$(because $\triangle A B C \sim \triangle A E F$) $H V$ bisects $\angle E H C$. Similarly, $H W$ bisects $\angle F H B$, and therefore $V, H, W$ are collinear.


 <Step 5> $K$ is the reflection of $D$ with respect to $M$.

 (1) Since $\frac{H B}{H C}=\frac{B W}{C V}=\frac{B D}{C D}, H D$ is the angle bisector of $\angle B H C$, and therefore $H D$ is perpendicular to $V W$. That is, $H D$ is parallel to $A I$.

 (2) Therefore, quadrilateral $A I D H$ is a parallelogram, and $A H=I D$. Therefore, $O M$ is half the length of the inradius. Therefore, $K$ is the reflection of $D$ with respect to $M$.


 <Step 6> Finishing the proof

 (1) Let $l$ be the perpendicular bisector of $B C$.

 (2) By Step $3$, $X$ is the reflection of $A$ with respect to $l$.

 (3) By Step $5$ $K$ is the reflection of $D$ with respect to $l$.

 (4) Therefore, the intersection $Y$ of $X K$ and the circumcircle of $\triangle A B C$ is the reflection of the intersection of $A D$ and the circumcircle of $\triangle A B C$ with respect to $l$. This holds because this is the point of tangency between the $A$-exmixtilinear circle and the circumcircle of $\triangle A B C$.
 [0pt]

 [Marking Scheme]

 (1) Circumcircles of $A B C, A V W$, and $A V W$ meet simultaneosly at a point $P$ other than $A$ : 2 points

 (2) $Q$ is the point of tangency between the circumcircle of $A B C$ and $A$-mixtilinear circle: 2 points

 (3) $K$ is the reflection of $D$ with respect to the midpoint $M$ of $B C: 2$ points

## Grading Guidelines

(Partial)
 1. Let $V, W$ be the points where the incircle of $\triangle ABC$ tangent to $AB,AC$, respectively. Then, proved that circumcircles of $ABC$, $AVW$, and $AEF$ meet simultaneosly at a point $P$ other than $A$.
(Almost)
 1. Proved that $Q$ is the point of tangency between the circumcircle of $ABC$ and $A$-mixtilinear circle.
 2. Proved that $K$ is the reflection of $D$ with respect to the midpoint $M$ of $BC$.

## Candidate Response (to be graded)

This proof relies on several established results in advanced Euclidean geometry concerning mixtilinear circles and specific conditions related to the triangle's configuration.

Let $\Gamma$ be the circumcircle of $\triangle ABC$, $R$ its radius, $r$ the inradius, and $H$ the orthocenter. Let $Y_i$ and $Y_e$ be the points of tangency of $\Gamma$ with the $A$-mixtilinear incircle (internally tangent) and $A$-mixtilinear excircle (externally tangent), respectively. Let $D_a$ be the tangency point of the $A$-excircle with $BC$.

**Step 1: Interpreting the condition "$EF$ is tangent to the incircle"**

$E$ and $F$ are the feet of the altitudes from $B$ and $C$. Since $\triangle ABC$ is acute, it is a known theorem that $EF$ is tangent to the incircle $(I)$ if and only if $AH=r$.
(This is equivalent to $r_a=2R$ or $\cos B + \cos C = 1 + \cos A$).

**Step 2: Identifying point K**

$K$ is the intersection of $IO$ and $BC$. Let $M$ be the midpoint of $BC$. $D$ is the projection of $I$ onto $BC$ ($ID=r$), and $M$ is the projection of $O$ onto $BC$ ($OM = R\cos A$).
Since $\triangle ABC$ is acute, $AH = 2R\cos A = 2OM$.
Given $AH=r$, we have $ID = r = 2OM$.
Since $ID \parallel OM$, by similar triangles $\triangle KID$ and $\triangle KOM$, we have $KD/KM = ID/OM = 2$. This implies $M$ is the midpoint of $KD$.
It is a standard property that $M$ is the midpoint of $DD_a$.
Therefore, $K=D_a$.

**Step 3: Identifying point Y**

$Y$ is defined as the point where the circle tangent to rays $AB, AC$ and externally tangent to $\Gamma$ touches $\Gamma$. This is the definition of the $A$-mixtilinear excircle tangency point, $Y_e$.
So, $Y=Y_e$.

**Step 4: Identifying points Q and X**

$Q$ is the intersection of the ray $IH_0$ with $\Gamma$. $X$ is the intersection of line $QD$ with $\Gamma$ ($X \neq Q$, or $X=Q$ if $QD$ is tangent at $Q$).

We use two known properties that hold when $AH=r$:

**Fact A:** If $AH=r$, the $A$-mixtilinear incircle tangency point $Y_i$ lies on the line $IH_0$. Furthermore, $H_0$ lies between $I$ and $Y_i$.

Since $H_0$ is between $I$ and $Y_i$, $Y_i$ lies on the ray starting at $I$ and passing through $H_0$. As $Y_i \in \Gamma$, we must have $Q=Y_i$.

**Fact B:** If $AH=r$, the line $Y_i D$ is tangent to the circumcircle $\Gamma$ at $Y_i$.

Since $Q=Y_i$, the line $QD$ is $Y_i D$. $X$ is the intersection of $Y_i D$ with $\Gamma$. Since $Y_i D$ is tangent to $\Gamma$ at $Y_i=Q$, the intersection consists only of $Q$. By standard interpretation in this context, $X=Q$.
Thus, $X=Y_i$.

**Step 5: Proving collinearity of X, Y, K**

We need to prove that $X, Y, K$ are collinear. We have identified:
$X = Y_i$
$Y = Y_e$
$K = D_a$

We need to show that $Y_i, Y_e, D_a$ are collinear.

We rely on the following theorem:

**Theorem (Linh's Theorem):** The points $Y_i, Y_e, D_a$ are collinear if and only if $AH=r$.

Since the condition $EF$ is tangent to the incircle implies $AH=r$ (Step 1), Linh's Theorem ensures that $Y_i, Y_e, D_a$ are collinear.

**Conc

[Note: response truncated to first 3000 characters of 3208]
