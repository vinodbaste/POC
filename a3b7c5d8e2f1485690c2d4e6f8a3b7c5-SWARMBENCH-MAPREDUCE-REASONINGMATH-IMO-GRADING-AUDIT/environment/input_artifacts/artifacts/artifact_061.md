# artifact_061

Grading ID: GB-0725  
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

The problem asks for the value of $\angle NIM+\angle B'KC'$. Since the problem asks for a specific value, this value must be independent of the triangle $ABC$, provided it satisfies the condition $AB<AC<BC$ (i.e., $c<b<a$). We will calculate this value using a specific example: the right triangle with side lengths $c=3, b=4, a=5$. This triangle satisfies the condition $3<4<5$.

Let $A, B, C$ be the vertices of the triangle. Since $3^2+4^2=5^2$, the angle at $A$ is $90^\circ$. We set up a coordinate system with $A=(0,0)$, $B=(3,0)$, and $C=(0,4)$.

The semiperimeter is $s=(3+4+5)/2=6$. The area is $S=(1/2)(3)(4)=6$. The inradius is $r=S/s=1$.

1. Calculate the coordinates of $I, N, M$ and the angle $\angle NIM$.
The incenter $I$ is $(r,r)=(1,1)$.
$N$ is the midpoint of $AB$. $N=(3/2, 0)$.
$M$ is the midpoint of $AC$. $M=(0, 2)$.

We use vectors to calculate $\angle NIM$.
$\vec{IN} = N-I = (3/2-1, 0-1) = (1/2, -1)$.
$\vec{IM} = M-I = (0-1, 2-1) = (-1, 1)$.

$|\vec{IN}|^2 = (1/2)^2+(-1)^2 = 1/4+1 = 5/4$.
$|\vec{IM}|^2 = (-1)^2+1^2 = 2$.
$\vec{IN} \cdot \vec{IM} = (1/2)(-1) + (-1)(1) = -1/2-1 = -3/2$.

$\cos(\angle NIM) = \frac{\vec{IN} \cdot \vec{IM}}{|\vec{IN}| |\vec{IM}|} = \frac{-3/2}{\sqrt{5/4}\sqrt{2}} = \frac{-3/2}{\sqrt{10}/2} = -\frac{3}{\sqrt{10}}$.

2. Calculate the coordinates of $K, B', C'$ and the angle $\angle B'KC'$.
$K$ is the midpoint of the arc $BC$ of the circumcircle not containing $A$. $K$ lies on the angle bisector of $\angle A$. Since $A=90^\circ$ at the origin, the angle bisector is the line $y=x$.
The circumcenter of the right triangle is the midpoint of the hypotenuse $BC$. $O=(3/2, 2)$. The circumradius is $R=5/2$.
The equation of the circumcircle is $(x-3/2)^2+(y-2)^2=25/4$.
To find $K$, we substitute $y=x$:
$(x-3/2)^2+(x-2)^2=25/4$.
$x^2-3x+9/4 + x^2-4x+4 = 25/4$.
$2x^2-7x+25/4=25/4$.
$2x^2-7x=0$. $x(2x-7)=0$.
The solutions are $x=0$ (which corresponds to $A$) and $x=7/2$.
So $K=(7/2, 7/2)$.
We verify that $K$ is on the arc not containing $A$. The line $BC$ is $4x+3y-12=0$. $A(0,0)$ yields $-12$. $K(7/2, 7/2)$ yields $4(7/2)+3(7/2)-12 = 14+10.5-12=12.5$. Since the signs are opposite, $A$ and $K$ are on opposite sides of $BC$.

$B'$ is the intersection of $BC$ with the line parallel to $AC$ and tangent to the incircle, other than $AC$. $AC$ is the line $x=0$. The incircle has center $(1,1)$ and radius $1$. The parallel tangents are $x=0$ and $x=2$. The required tangent is $x=2$.
$B'$ is the intersection of $x=2$ and $4x+3y-12=0$. $4(2)+3y-12=0$, $3y=4$, $y=4/3$. $B'=(2, 4/3)$.

$C'$ is the intersection of $BC$ with the line parallel to $AB$ and tangent to the incircle, other than $AB$. $AB$ is the line $y=0$. The parallel tangent is $y=2$.
$C'$ is the intersection of $y=2$ and $4x+3y-12=0$. $4x+3(2)-12=0$, $4x=6$, $x=3/2$. $C'=(3/2, 2)$.

Now we calculate $\angle B'KC'$.
$\vec{KB'} = B'-K = (2-7/2, 4/3-7/2) = (-3/2, (8-21)/6) = (-3/2, -13/6)$.
$\vec{KC'} = C'-K = (3/2-7/2, 2-7/2) = (-4/2, -3/2) = (-2, -3/2)$.

$|\vec{KB'}

[Note: response truncated to first 3000 characters of 3793]
