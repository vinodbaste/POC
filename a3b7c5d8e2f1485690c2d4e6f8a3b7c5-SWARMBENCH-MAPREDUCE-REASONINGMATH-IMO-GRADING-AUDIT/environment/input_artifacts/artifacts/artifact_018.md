# artifact_018

Grading ID: GB-0724  
Problem ID: PB-Advanced-022  
Source: (Modified) IMO 2024 P4  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Given a triangle $ABC$ with $AB<AC<BC$, let $I$ be the incenter
 of triangle $ABC$, and let $M$ and $N$ be the midpoints of sides
 $CA$ and $AB$, respectively. Let $K$ be the midpoint of the arc
 $BC$ of the circumcircle of triangle $ABC$ which does not contain
 $A$. Let $B'\neq B$ be the point where the line parallel to $AC$
 and tangent to the incircle of triangle $ABC$ intersects side $BC$,
 and similarly, let $C'\neq C$ be the point where the line parallel
 to $AB$ and tangent to the incircle of triangle $ABC$ intersects
 side $BC$. Find the value of $\angle NIM+\angle B'KC'$ in terms
 of degree.

## Reference Solution (for grader's calibration)

Let $IB'$ intersect $CK$ at $Q$.


 \textbf{Claim. }Triangle $CB'Q$ is similar to $\triangle AIB$ (and
 $Q$ lies on circle $BIC$).


 \emph{Proof.} Since the tangent at $B'$ to the incircle, distinct
 from $BC$, is parallel to $AC$, and $B'I$ bisects the two tangents
 from $B'$,
 \[
 \angle CB'I=\frac{1}{2}\left(180^{\circ}-\angle ACB\right)=90^{\circ}-\frac{1}{2}\angle ACB.
 \]
 Using this, we get
 \[
 \angle CQB'=\angle CB'I-\angle BCK=90^{\circ}-\frac{1}{2}\angle ACB-\angle BAK=90^{\circ}-\frac{1}{2}(\angle ACB+\angle BAC)=\frac{1}{2}\angle CBA
 \]
 Which is enough to show $Q$ lies on circle $BIC$. Combining this
 with $\angle B'CQ=\angle BCK=$ $\angle BAI$ gives the similarity.

 Note that $K$ is the centre of circle $BIC$ so $K$ is the midpoint
 of $CQ$. Since $N$ is the midpoint of $AB$, $K$ and $N$ are similar
 points in the two triangles in the Claim so
 \[
 \angle KB'C'=\angle KB'C=\angle AIN.
 \]

 Similarly $\angle B'C'K=\angle MIA$ so
 \[
 \angle MIN+\angle C'KB'=\angle MIA+\angle AIN+\angle C'KB'=\angle B'C'K+\angle KB'C'+\angle C'KB'=180^{\circ}.
 \]

## Grading Guidelines

(Partial)
 1. Constructed the reflection of $A$ over $I$, or any auxiliary point that helps angle computation regarding the midpoints.
(Almost)
 1. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

The problem asks for the value of $\angle NIM+\angle B'KC'$. We will show that this value is $180^\circ$.

Let $I$ be the incenter of $\triangle ABC$. Let $N$ be the midpoint of $AB$ and $M$ be the midpoint of $AC$.

Step 1: Analyze $\angle NIM$.
Let $A'$ be the reflection of $A$ with respect to $I$. So $I$ is the midpoint of $AA'$.
Consider $\triangle ABA'$. $N$ is the midpoint of $AB$ and $I$ is the midpoint of $AA'$. By the Midsegment Theorem, $NI$ is parallel to $BA'$.
Consider $\triangle ACA'$. $M$ is the midpoint of $AC$ and $I$ is the midpoint of $AA'$. By the Midsegment Theorem, $MI$ is parallel to $CA'$.
Therefore, the angle between $NI$ and $MI$ is equal to the angle between $BA'$ and $CA'$.
$\angle NIM = \angle BA'C$.

Step 2: Analyze the points $B'$ and $C'$.
Let $\omega$ be the incircle of $\triangle ABC$, centered at $I$ with radius $r$.
$B'$ is the intersection of $BC$ and the line $L_b$, which is parallel to $AC$ and tangent to $\omega$, distinct from $AC$.
$C'$ is the intersection of $BC$ and the line $L_c$, which is parallel to $AB$ and tangent to $\omega$, distinct from $AB$.

Since $L_b$ is parallel to $AC$ and both are tangent to the incircle centered at $I$, $L_b$ must be the reflection of $AC$ across $I$. Similarly, $L_c$ is the reflection of $AB$ across $I$.
Let $A^*$ be the intersection of $L_b$ and $L_c$. Since reflection is an isometry, $A^*$ must be the reflection of the intersection of $AC$ and $AB$ (which is $A$) across $I$.
Thus, $A^*=A'$. So $A'$ lies on both $L_b$ and $L_c$.
$B'$ is the intersection of $L_b$ and $BC$. $C'$ is the intersection of $L_c$ and $BC$.
The points $A', B', C'$ form a triangle where the side $A'B'$ lies on $L_b$ (parallel to $AC$) and $A'C'$ lies on $L_c$ (parallel to $AB$).

Step 3: The relationship between the angles.
We want to find $\angle NIM + \angle B'KC' = \angle BA'C + \angle B'KC'$.
$K$ is the midpoint of the arc $BC$ not containing $A$. It is known that $K$ lies on the angle bisector of $\angle A$. So $A, I, K$ are collinear. Since $A'$ is the reflection of $A$ across $I$, $A, I, A', K$ are collinear.

It is a known theorem in Euclidean geometry (sometimes attributed to L. Emelyanov) that in this configuration, $\angle BA'C + \angle B'KC' = 180^\circ$.

Since the problem asks for a specific value, this value must be independent of the triangle (provided it satisfies the given conditions). We can verify this result using a specific example.

Step 4: Verification using a specific triangle.
Let us consider the right triangle $ABC$ with $A=90^\circ$, $AB=3$, and $AC=4$. Then $BC=5$. The condition $AB<AC<BC$ ($3<4<5$) is satisfied.
We set up coordinates with $A(0,0)$, $B(3,0)$, and $C(0,4)$.
The semiperimeter is $s=(3+4+5)/2=6$. The inradius is $r=Area/s = 6/6 = 1$.
The incenter is $I(1,1)$.

Calculate $\angle NIM$.
$N$ is the midpoint of $AB$, $N=(3/2, 0)$. $M$ is the midpoint of $AC$, $M=(0, 2)$.
$\vec{IN} = (3/2-1, 0-1) = (1/2, -1)$.
$\vec{IM} = (0-1, 2-1) = (-1, 1)$.
$\vec{IN} \cd

[Note: response truncated to first 3000 characters of 4954]
