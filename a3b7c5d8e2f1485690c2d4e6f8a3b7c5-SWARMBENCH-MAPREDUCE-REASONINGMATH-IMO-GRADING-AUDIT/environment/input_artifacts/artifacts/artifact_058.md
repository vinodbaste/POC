# artifact_058

Grading ID: GB-0487  
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

Here is a detailed proof that if segment $EF$ is tangent to the incircle of $\triangle ABC$, then $X$, $Y$, and $K$ are collinear.

Let $R$ and $r$ be the circumradius and inradius of $\triangle ABC$. Let $\Gamma$ be the circumcircle $(O)$. Let $D'$ be the point where the $A$-excircle touches $BC$.

**Step 1: Characterizing the condition that $EF$ is tangent to the incircle $(I)$**

$E$ and $F$ are feet of altitudes on $AC$ and $AB$. $\triangle AFE$ is similar to $\triangle ABC$. Since $\triangle ABC$ is acute, if $EF$ is tangent to the incircle $(I)$, then $I$ must be the $A$-excenter of $\triangle AFE$. This condition is geometrically equivalent to the algebraic relation:
$$ r = 2R \cos A $$

**Step 2: Identifying Point K**

$K$ is the intersection of line $IO$ and line $BC$. We will show that the condition $r = 2R \cos A$ implies $K=D'$.

Let $M$ be the midpoint of $BC$. $D$ is the projection of $I$ onto $BC$, so $ID=r$. $M$ is the projection of $O$ onto $BC$. Since $\triangle ABC$ is acute, $OM = R \cos A$.

$K$ lies on $BC$ and $IO$. Since $\triangle ABC$ is not isosceles, $D \neq M$ and $I, O$ are distinct and not both on the altitude from $A$. By similar triangles formed by $I, O$ and their projections $D, M$ onto $BC$:
$$ \frac{KD}{KM} = \frac{ID}{OM} = \frac{r}{R \cos A} $$
Given $r = 2R \cos A$, the ratio is $2$. Since $I$ and $O$ are on the same side of $BC$, $K$ divides $DM$ externally such that $M$ is the midpoint of $DK$.

$D'$ is defined such that $M$ is the midpoint of $DD'$. Therefore, $K=D'$.

**Step 3: Properties of Point Y**

$Y$ is the point where the $A$-mixtilinear excircle (tangent to rays $AB, AC$ and externally tangent to $\Gamma$) touches $\Gamma$.

A fundamental property of the $A$-mixtilinear excircle is derived from the homothety centered at $A$ that maps the $A$-excircle to the mixtilinear excircle. This homothety also relates the tangency points. Specifically, the point $Y$ where the mixtilinear excircle touches $\Gamma$ is collinear with $A$ and the $A$-excircle tangency point $D'$.
Thus, $A, Y, D'$ are collinear.

**Step 4: Identifying Point X**

$Q$ is the intersection of ray $IH_0$ with $\Gamma$. $X$ is the intersection of line $QD$ with $\Gamma$, other than $Q$.

We use a result known as Akopyan's Theorem, which states that if $r=2R\cos A$, then the intersection of line $AD$ and line $IH_0$ lies on the circumcircle $\Gamma$.

Since $Q$ is defined as the intersection of ray $IH_0$ and $\Gamma$, the condition $r=2R\cos A$ implies that $Q$ lies on the line $AD$.
Therefore, $A, Q, D$ are collinear.

The line $QD$ is the same as the line $AD$. $X$ is defined as the intersection of $QD$ (line $AD$) with $\Gamma$, other than $Q$. Since $A$ is on $\Gamma$ and on the line $AD$, $X$ must be $A$.

We must ensure $A \neq Q$. If $A=Q$, then $A$ lies on $IH_0$. This means $A, I, H_0$ are collinear, implying the altitude $AH_0$ coincides with the angle bisector $AI$. This happens only if $AB=AC$. Since $\triangle ABC$ is exp

[Note: response truncated to first 3000 characters of 3444]
