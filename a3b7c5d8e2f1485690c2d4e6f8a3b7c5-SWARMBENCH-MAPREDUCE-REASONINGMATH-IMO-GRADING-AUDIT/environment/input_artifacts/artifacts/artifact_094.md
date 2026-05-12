# artifact_094

Grading ID: GB-0747  
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

**Outcome 1: COMPLETE PROOF**

We are asked to find the value of $\angle NIM + \angle B'KC'$. We will show that this sum is $180^\circ$. We will use directed angles modulo $180^\circ$, denoted by $\measuredangle(L_1, L_2)$.

**Step 1: Interpretation of $B', C'$ and Introduction of $A'$.**

Let $\omega$ be the incircle of $\triangle ABC$ with center $I$. There are two lines parallel to $AC$ and tangent to $\omega$: the side $AC$ itself, and its reflection across $I$, denoted $L_B$. $AC$ intersects $BC$ at $C$. $L_B$ intersects $BC$ at some point $B'_0$.
Similarly, the tangents parallel to $AB$ are $AB$ (intersecting $BC$ at $B$) and $L_C$ (the reflection of $AB$ across $I$, intersecting $BC$ at $C'_0$).

The problem defines $B' \neq B$ as an intersection point of such a tangent with $BC$, and $C' \neq C$ similarly. Both $C, B'_0$ satisfy $B' \neq B$, and $B, C'_0$ satisfy $C' \neq C$.

Let $N, M$ be the midpoints of $AB, AC$. Let $A'$ be the reflection of $A$ across $I$. We established in the thought process that $\angle NIM = \angle BA'C = A$.

If we choose $B'=C$ and $C'=B$, the required sum is $\angle NIM + \angle CKB$. Since $K$ is on the circumcircle of $\triangle ABC$, $\angle CKB = \angle CAB = A$. The sum is $A+A=2A$. Since the shape of $\triangle ABC$ is not fixed (only constrained by $AB<AC<BC$), $2A$ is not a constant value. As the problem asks for "the value", we must interpret $B'$ and $C'$ as $B'_0$ and $C'_0$, derived from the reflected tangents $L_B$ and $L_C$.

Let $B' = L_B \cap BC$ and $C' = L_C \cap BC$.
Since $A'$ is the reflection of $A=AB \cap AC$ across $I$, $A'$ must be the intersection of $L_C$ and $L_B$.
Thus, $A', B'$ lie on $L_B$, so $A'B' \parallel AC$.
$A', C'$ lie on $L_C$, so $A'C' \parallel AB$.

**Step 2: Relating $\angle NIM$ to $\angle BA'C$.**

$I$ is the midpoint of $AA'$. $N$ is the midpoint of $AB$, $M$ is the midpoint of $AC$.
By the Midpoint Theorem in $\triangle ABA'$, $NI \parallel A'B$.
By the Midpoint Theorem in $\triangle ACA'$, $MI \parallel A'C$.

Therefore, the directed angle between $NI$ and $MI$ equals the directed angle between $A'B$ and $A'C$:
$$ \measuredangle(NI, MI) = \measuredangle(A'B, A'C) \quad (1) $$

**Step 3: Properties of $K$ and Concyclicity.**

$K$ is the midpoint of the arc $BC$ not containing $A$ on the circumcircle $\Gamma$ of $\triangle ABC$. Thus, $AK$ is the angle bisector of $\angle A$. Since $I$ lies on $AK$, and $A'$ is the reflection of $A$ across $I$, the points $A, I, A', K$ are collinear. The line $A'K$ is the line $AK$.

We establish two key cyclic quadrilaterals. Let $L_{BC}$ denote the line $BC$.

1. **$A', K, B, B'$ are concyclic.**
Since $A, B, C, K$ are on $\Gamma$:
$$ \measuredangle(KA', KB) = \measuredangle(AK, BK) = \measuredangle(AC, BC) $$
$B'A'$ is $A'B'$. Since $A'B' \parallel AC$, and $B'B$ is $L_{BC}$:
$$ \measuredangle(B'A', B'B) = \measuredangle(A'B', BC) = \measuredangle(AC, BC) $$
Thus, $\measuredangle(KA', KB) = \measuredangle(B'A', B'B)$, so $A', 

[Note: response truncated to first 3000 characters of 4947]
