# artifact_086

Grading ID: GB-0742  
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

**Complete Proof**

Let $I$ be the incenter of $\triangle ABC$, and let $\omega$ be its incircle. Let $M$ and $N$ be the midpoints of $CA$ and $AB$, respectively. Let $K$ be the midpoint of the arc $BC$ of the circumcircle of $\triangle ABC$ not containing $A$.

1. **Definition of $A', B', C'$ and the angle $\angle NIM$.**

Let $L_b$ be the line parallel to $AC$, tangent to $\omega$, and distinct from $AC$. Let $L_c$ be the line parallel to $AB$, tangent to $\omega$, and distinct from $AB$. By definition, $B'$ is the intersection of $L_b$ and $BC$, and $C'$ is the intersection of $L_c$ and $BC$. (This interpretation is standard and necessary for the result to be a constant value).

Since $I$ is the center of the incircle, $L_b$ is the reflection of $AC$ across $I$, and $L_c$ is the reflection of $AB$ across $I$. Let $A'$ be the intersection of $L_b$ and $L_c$. Then $A'$ is the reflection of $A$ across $I$. Thus, $I$ is the midpoint of $AA'$.

In $\triangle ABA'$, $N$ is the midpoint of $AB$ and $I$ is the midpoint of $AA'$. By the Midpoint Theorem, $NI \parallel BA'$.
In $\triangle ACA'$, $M$ is the midpoint of $AC$ and $I$ is the midpoint of $AA'$. By the Midpoint Theorem, $MI \parallel CA'$.

Therefore, the angle $\angle NIM$ is equal to the angle $\angle BA'C$. Using directed angles modulo $180^\circ$, denoted by $\measuredangle(L_1, L_2)$:
$$ \measuredangle(NI, MI) = \measuredangle(A'B, A'C) $$

2. **The Homothety.**

The triangle $\triangle A'B'C'$ is formed by the lines $L_b, L_c, BC$. We have $A'B' \subset L_b \parallel AC$ and $A'C' \subset L_c \parallel AB$. $B'C' \subset BC$.
The corresponding angles are $\angle A' = \angle A$, $\angle B' = \angle C$, and $\angle C' = \angle B$ (in magnitude). Thus, there is a homothety $H$ that maps $\triangle ABC$ to $\triangle A'C'B'$. The correspondence of vertices is $H(A)=A', H(B)=C', H(C)=B'$.

The center of the homothety $D$ is the intersection of $AA'$ and $BC$. Since $A, I, A'$ are collinear, the line $AA'$ is the internal angle bisector of $\angle A$. Thus $D$ is the foot of the $A$-angle bisector on $BC$.

Let $k$ be the ratio of the homothety $H$. Using directed segments along the lines passing through $D$:
$\overline{DA'} = k\overline{DA}$, $\overline{DC'} = k\overline{DB}$, $\overline{DB'} = k\overline{DC}$.

3. **Concyclicity via Power of a Point.**

Let $\Gamma$ be the circumcircle of $\triangle ABC$. $K$ is the midpoint of the arc $BC$ not containing $A$, so $K$ lies on $\Gamma$ and on the line $AD$. The points $A, D, K$ are collinear, and $B, D, C$ are collinear.
By the Power of a Point theorem applied to $D$ with respect to $\Gamma$:
$$ P = \overline{DA} \cdot \overline{DK} = \overline{DB} \cdot \overline{DC} $$

We use the converse of the Power of a Point theorem to establish concyclicity.
Consider the points $A', K$ on the line $AD$ and $B, B'$ on the line $BC$.
$$ \overline{DA'} \cdot \overline{DK} = (k\overline{DA}) \cdot \overline{DK} = k(\overline{DA} \cdot \overline{DK}) = kP 

[Note: response truncated to first 3000 characters of 5428]
