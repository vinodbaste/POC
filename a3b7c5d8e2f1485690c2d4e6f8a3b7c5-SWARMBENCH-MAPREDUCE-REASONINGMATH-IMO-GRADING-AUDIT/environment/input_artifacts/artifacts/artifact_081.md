# artifact_081

Grading ID: GB-0731  
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

Let the angles of $\triangle ABC$ be $A, B, C$ at the respective vertices. Let $a, b, c$ be the lengths of sides $BC, CA, AB$. We are given $c<b<a$. Let $s = (a+b+c)/2$ be the semi-perimeter, $\Delta$ the area, and $r$ the inradius of $\triangle ABC$.

The problem asks for the value of $\angle NIM + \angle B'KC'$. The formulation of the problem suggests that this sum is a constant value for any triangle satisfying the given conditions. We can verify this by calculating the sum for a specific, non-degenerate scalene triangle. A right-angled triangle is a good choice for simplifying calculations.

Let's consider a right-angled triangle with $\angle A = 90^\circ$ and side lengths $c=3, b=4, a=5$. This satisfies the condition $c<b<a$.
For this triangle:
-   Semi-perimeter: $s = (3+4+5)/2 = 6$.
-   Area: $\Delta = (1/2) \cdot 3 \cdot 4 = 6$.
-   Inradius: $r = \Delta/s = 6/6 = 1$.

**1. Calculation of $\angle NIM$**

$N$ and $M$ are the midpoints of $AB$ and $AC$, respectively. So $AN = c/2 = 3/2$ and $AM = b/2 = 4/2 = 2$.
Let the incircle be tangent to sides $AB$ and $AC$ at points $F$ and $E$, respectively.
The distances from vertex $A$ to the tangency points are $AF = AE = s-a = 6-5=1$.
The incenter $I$ is located at a distance $r=1$ from the sides $AB$ and $AC$. In a right-angled triangle at $A$, $AEIF$ is a square with side length $r=1$.
We have two right-angled triangles, $\triangle IFN$ and $\triangle IEM$, with right angles at $F$ and $E$.
The lengths of the legs are:
-   $IF = IE = r = 1$.
-   $FN = |AN - AF| = |3/2 - 1| = 1/2$.
-   $EM = |AM - AE| = |2 - 1| = 1$.

We can find the lengths of the sides of $\triangle NIM$:
-   $IN^2 = IF^2 + FN^2 = 1^2 + (1/2)^2 = 1 + 1/4 = 5/4$.
-   $IM^2 = IE^2 + EM^2 = 1^2 + 1^2 = 2$.
-   $NM$ is the midline of $\triangle ABC$ connecting the midpoints of $AB$ and $AC$. So, $NM = a/2 = 5/2$, which gives $NM^2 = 25/4$.

Now, we use the Law of Cosines in $\triangle NIM$ to find $\cos(\angle NIM)$:
$$ \cos(\angle NIM) = \frac{IN^2 + IM^2 - NM^2}{2 \cdot IN \cdot IM} = \frac{5/4 + 2 - 25/4}{2 \cdot \sqrt{5/4} \cdot \sqrt{2}} = \frac{13/4 - 25/4}{2 \cdot (\sqrt{5}/2) \cdot \sqrt{2}} = \frac{-12/4}{\sqrt{10}} = \frac{-3}{\sqrt{10}} $$

**2. Calculation of $\angle B'KC'$**

First, let's determine the positions of $B'$ and $C'$ on the side $BC$.
The line tangent to the incircle parallel to $AC$ cuts off a small triangle from corner $B$ that is similar to $\triangle ABC$. The ratio of similarity is $k_B = 1-2r/h_b = 1-b/s$. The length of the segment $BB'$ is $a \cdot k_B = a(1-b/s) = a(s-b)/s$.
$BB' = 5 \cdot (6-4)/6 = 5 \cdot 2/6 = 5/3$.

Similarly, for $C'$, the line is parallel to $AB$. The ratio of similarity is $k_C = 1-c/s$. The length of the segment $CC'$ is $a \cdot k_C = a(s-c)/s$.
$CC' = 5 \cdot (6-3)/6 = 5 \cdot 3/6 = 5/2$.

Let's place the triangle in a coordinate system. Let $C=(0,0)$ and $B=(5,0)$. The side $BC$ lies on the x-axis.
-   $C'$ is at a distance $CC' = 5/2$ from $C$. So $C'=(5/2, 0)$.
-   $B'

[Note: response truncated to first 3000 characters of 5544]
