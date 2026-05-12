# artifact_038

Grading ID: GB-0506  
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

The proof relies on several known theorems in advanced Euclidean geometry. We will break down the proof into steps, analyzing the condition and the points involved.

Let $\Gamma$ be the circumcircle of $\triangle ABC$, $O$ its center and $R$ its radius. Let $I$ be the incenter and $r$ the inradius. Let $r_A$ be the $A$-exradius. Let $D_a$ be the point where the $A$-excircle touches $BC$. Let $M_A$ be the midpoint of the arc $BC$ of $\Gamma$ not containing $A$.

Step 1: Analyze the condition that $EF$ is tangent to the incircle.
$E$ and $F$ are the feet of the altitudes from $B$ and $C$. Since $\triangle ABC$ is acute, $E$ is on $AC$ and $F$ is on $AB$. The incircle $(I)$ is tangent to $AB$ and $AC$. If it is also tangent to $EF$, it must be the $A$-excircle of $\triangle AEF$ (as shown in the thought process, it cannot be the incircle).
$\triangle AEF \sim \triangle ABC$ with ratio $\cos A$. The $A$-exradius of $\triangle AEF$ is $r_A \cos A$.
The condition is $r = r_A \cos A$. This condition is known to be equivalent to $r_A = 2R$ and $r = 2R \cos A$. It is also equivalent to $1+\cos A = \cos B + \cos C$. Acute non-isosceles triangles satisfying this condition exist.

Step 2: Identify the point $K$.
$K$ is the intersection of $IO$ and $BC$. Let $M$ be the midpoint of $BC$. $I$ projects to $D$ on $BC$, and $O$ projects to $M$. The distance $ID=r$ and $OM=R\cos A$.
Since $r=2R\cos A$, we have $ID=2OM$. By similar triangles (considering the heights of $I$ and $O$ above $BC$), $K$ is the intersection point such that $M$ is the midpoint of $DK$.
Since $M$ is also the midpoint of $DD_a$, $K$ must coincide with $D_a$.
So, $K=D_a$.

Step 3: Identify the point $Y$.
$Y$ is the point of tangency of the $A$-mixtilinear excircle (externally tangent to $\Gamma$) with $\Gamma$. Let $Y=Y_{ex}$.

Step 4: Utilize the property of $Y_{ex}$.
A known theorem by K.Y. Lee states that $Y_{ex}, D_a, M_A$ are collinear.

Step 5: Analyze the required collinearity.
We want to prove that $X, Y, K$ are collinear. This is equivalent to $X, Y_{ex}, D_a$ being collinear.
Since $X$ is on $\Gamma$, $X$ must be the second point of intersection of the line $Y_{ex}D_a$ with $\Gamma$.
By Step 4, the line $Y_{ex}D_a$ is the line $Y_{ex}D_a M_A$. The intersections with $\Gamma$ are $Y_{ex}$ and $M_A$.
Since $AB \ne AC$, $Y_{ex} \ne M_A$. Thus, we must prove that $X=M_A$.

Step 6: Identify $X$ and $Q$.
$Q$ is the intersection of the ray $IH_0$ with $\Gamma$. $X$ is the second intersection of the line $QD$ with $\Gamma$.
To have $X=M_A$, the line $QD$ must pass through $M_A$. So we need to prove that $Q, D, M_A$ are collinear.

Step 7: The crucial claim.
We rely on the following claim, which is a known property related to the condition $r_A=2R$.
Claim: If $r_A=2R$, then $Q, D, M_A$ are collinear, where $Q$ is the intersection of the ray $IH_0$ with $\Gamma$.

(Note: This claim seems to contradict a theorem by Emelyanov if $Q$ in Emelyanov's theorem is interpreted differently, but geometri

[Note: response truncated to first 3000 characters of 3587]
