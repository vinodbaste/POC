# artifact_084

Grading ID: GB-0734  
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

Part 1: Geometric interpretation and reduction of $\angle NIM$.

Let $I$ be the incenter of $\triangle ABC$. Let $r$ be the inradius.
$N$ and $M$ are the midpoints of $AB$ and $AC$ respectively.

Let's first understand the definitions of $B'$ and $C'$. There are two lines parallel to $AC$ and tangent to the incircle: $AC$ itself and its reflection across $I$, let us call it $L_b$. The distance between $AC$ and $L_b$ is $2r$.
The intersection of $AC$ with $BC$ is $C$. The intersection of $L_b$ with $BC$ is some point $P$.
The problem states that $B'$ is the intersection point of "the line parallel to $AC$ and tangent to the incircle" with $BC$, such that $B' \neq B$.
In advanced geometry problems, "the tangent parallel to a side" usually refers to the tangent other than the side itself. We adopt this standard interpretation: $B'$ is the intersection of $L_b$ and $BC$. (We verified that $B' \neq B$ since $b \neq s$).
Similarly, $C'$ is the intersection of $BC$ and $L_c$, where $L_c$ is the reflection of $AB$ across $I$.

Let $A'$ be the intersection of $L_b$ and $L_c$. Since $L_b$ and $L_c$ are reflections of $AC$ and $AB$ across $I$, their intersection $A'$ is the reflection of $A$ across $I$. Thus, $I$ is the midpoint of $AA'$.

Now we analyze $\angle NIM$.
In $\triangle ABA'$, $N$ is the midpoint of $AB$ and $I$ is the midpoint of $AA'$. By the Midline Theorem, $NI$ is parallel to $BA'$.
In $\triangle ACA'$, $M$ is the midpoint of $AC$ and $I$ is the midpoint of $AA'$. By the Midline Theorem, $MI$ is parallel to $CA'$.
Since $NI \parallel BA'$ and $MI \parallel CA'$, the angle between $NI$ and $MI$ is equal to the angle between $BA'$ and $CA'$.
Therefore, $\angle NIM = \angle BA'C$.

The problem reduces to finding the value of $\angle BA'C + \angle B'KC'$.

Part 2: Calculation using a specific triangle.

Since the problem asks for a specific value, this value must be independent of the triangle satisfying the given conditions $AB<AC<BC$. We choose the right triangle with side lengths $c=3, b=4, a=5$. This satisfies $3<4<5$.

We set up a coordinate system with $A$ at the origin, $A(0,0)$. $B(3,0)$ along the x-axis, and $C(0,4)$ along the y-axis.
The semiperimeter is $s=(3+4+5)/2=6$. The area is $S=6$. The inradius is $r=S/s=1$.
The incenter is $I(1,1)$.

1. Calculation of $\angle NIM$ (or $\angle BA'C$).
$N$ is the midpoint of $AB$, $N(3/2, 0)$. $M$ is the midpoint of $AC$, $M(0, 2)$.
$\vec{IN} = (3/2-1, 0-1) = (1/2, -1)$.
$\vec{IM} = (0-1, 2-1) = (-1, 1)$.
$\vec{IN} \cdot \vec{IM} = (1/2)(-1) + (-1)(1) = -3/2$.
$|\vec{IN}| = \sqrt{1/4+1} = \sqrt{5}/2$. $|\vec{IM}| = \sqrt{1+1} = \sqrt{2}$.
$\cos(\angle NIM) = \frac{-3/2}{(\sqrt{5}/2)\sqrt{2}} = \frac{-3}{\sqrt{10}}$.

Alternatively, $A'$ is the reflection of $A(0,0)$ across $I(1,1)$, so $A'(2,2)$.
$\vec{A'B} = (3-2, 0-2) = (1, -2)$. $\vec{A'C} = (0-2, 4-2) = (-2, 2)$.
$\vec{A'B} \cdot \vec{

[Note: response truncated to first 3000 characters of 5348]
