# artifact_122

Grading ID: GB-0523  
Problem ID: PB-Advanced-016  
Source: Novel Problem  
IMO Area: Number_Theory

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $ABC$ be a non-isosceles triangle with incenter $I$. Let line $BI$ intersect $AC$ at $E$, and line $CI$ intersect $AB$ at $F$. Two Points $U$ and $V$ are on segments $AB$ and $AC$ respectively, such that $AU = AE$ and $AV = AF$. Let the line passing through $I$ and perpendicular to $AI$ intersect line $BC$ at $L$. The circumcircle of $\triangle ILC$ intersects line $LU$ at $X$ (other than $L$), and the circumcircle of triangle $\triangle ILB$ intersects line $LV$ at $Y$ (other than $L$). Prove that if $P$ is the intersection of lines $YB$ and $XC$, then line $IP$ is parallel to line $XY$.

## Reference Solution (for grader's calibration)

By symmetry, we assume that $AC>BC$.

 <Step 1> $U, V, L$ lie on a same line

 (1) Let $B^{\prime}$ be the point on $A C$ such that $A B=A B^{\prime}$ and $C^{\prime}$ be the point on $A B$ such that $A C=A C^{\prime}$. These points lie on the circumcircle of $\triangle I B C$.

 (2) By symmetry, $\left(B^{\prime}, I, U\right)$ and $\left(C^{\prime}, I, V\right)$ are collinear.

 (3) By Pascal's theorem on $B^{\prime} C B C^{\prime} I I, U, V, L$ lie on a same line.


 <Step 2> $IPXY$ is an isosceles trapezoid

 Since $U, V, L$ are collinear,

 \[
 \angle I X Y=\angle I C B=\angle B I L=\angle B Y L=\angle P Y X
 \]

 and similarly, $\angle I Y X=\angle P X Y$, so the statement holds.


 <Step 3> Therefore, by <Step 2>, $I P$ and $X Y$ are parallel.

## Grading Guidelines

(Partial)
 1. Proved that $U, V$, and $L$ lie on a same line.
(Almost)
 1. Made a minor mistake at the proof, or made a small gap.

## Candidate Response (to be graded)

Outcome 2: STRUCTURED PARTIAL PROGRESS & ANALYSIS

### Proven Lemmas and Key Results

Let $\alpha=A/2, \beta=B/2, \gamma=C/2$. We use directed angles modulo $180^\circ$.

**Lemma 1: Setup and Reflections.**
$U$ is the reflection of $E$ across $AI$, and $V$ is the reflection of $F$ across $AI$. $IU=IE, IV=IF$. Since $E$ is on $BI$ and $F$ is on $CI$, the line $IU$ is the reflection of line $IB$ across $AI$, and $IV$ is the reflection of $IC$ across $AI$.

**Lemma 2: Properties of L.**
$L \in BC$ and $IL \perp AI$. $LI$ is tangent to the circumcircle $(BIC)$ at $I$.
This implies $(LI, IB) = (CI, CB) = -\gamma$ and $(LI, IC) = (BI, BC) = \beta$. (Assuming standard counterclockwise orientation for $\triangle ABC$).

**Lemma 3: Angles related to U and V.**
Since $IU, IV$ are reflections of $IB, IC$ across $AI$, and $LI \perp AI$, $IU$ and $IV$ are reflections of $IB$ and $IC$ across $LI$.
$(LI, IU) = -(LI, IB) = \gamma$.
$(LI, IV) = -(LI, IC) = -\beta$.

**Lemma 4: $I, X, P, Y$ are concyclic.**
$X \in (ILC) \implies (XI, XC) = (LI, LC)$.
$Y \in (ILB) \implies (YI, YB) = (LI, LB)$.
Since $L, B, C$ are collinear, $(LI, LC) = (LI, LB)$.
$P=XC \cap YB$. $(XI, XP) = (YI, YP)$. Thus $I, X, P, Y$ lie on a circle $\Gamma$.

**Lemma 5: $LI$ is tangent to $(IXU)$ and $(IYV)$. $XY \parallel UV$.**
*Proof:* $X \in (ILC)$, so $(XI, XU) = (XI, XL) = (CI, CL) = (CI, BC) = \gamma$.
From Lemma 3, $(LI, IU) = \gamma$.
Thus $(LI, IU) = (XI, XU)$, which means $LI$ is tangent to $(IXU)$ at $I$.
Similarly, $(YI, YV) = (BI, BL) = \beta$. From Lemma 3, $(LI, IV) = -\beta$.
$(IV, LI) = \beta$. So $(IV, LI) = (YI, YV)$. This also implies $LI$ is tangent to $(IYV)$ at $I$.

By power of a point $L$: $LI^2 = LX \cdot LU = LY \cdot LV$.
This implies $X, Y, U, V$ are concyclic, and $\triangle LXY \sim \triangle LVU$. Thus $XY \parallel UV$.

**Goal Reformulation:** We want to prove $IP \parallel XY$. Since $XY \parallel UV$, we need $IP \parallel UV$.

### Identification of the Crux and Conjectures

The core difficulty lies in proving a relationship between $L, U, V$ known as K2.

**Conjecture K2 (I-bisector Lemma):** $LI$ is the internal angle bisector of $\angle ULV$.
Equivalently, $d(I, LU) = d(I, LV)$, or $(LU, LI) = (LI, LV)$.

**Consequences of K2:**

**Lemma 6: If K2 holds, then $P \in (BIC)$.**
*Proof:* $P \in (BIC)$ iff $(IC, PC) = -(IB, PB)$.
$(IC, PC) = (IC, XC)$. Since $X \in (ILC)$, $(IC, XC) = (IL, XL) = (IL, LU)$.
$(IB, PB) = (IB, YB)$. Since $Y \in (ILB)$, $(IB, YB) = (IL, YL) = (IL, LV)$.
If K2 holds, $(IL, LU) = -(IL, LV)$. Thus $(IC, PC) = -(IB, PB)$, so $P \in (BIC)$.

**Lemma 7: If K2 holds, then $IP$ is the reflection of $LU$ across $LI$.**
*Proof:* If $P \in (BIC)$, since $LI$ is tangent to $(BIC)$ at $I$ (Lemma 2), we have $(LI, IP) = (CI, CP)$.
We found $(CI, CP) = (LI, LU)$.
So $(LI, IP) = (LI, LU)$. This implies $IP$ and $LU$ are the same line.

However, if $I, P, L, U$ are collinear, then $(LI, IU)=0$ or $180^\circ$, so $\gamma=0$ or $180^\circ$, which i

[Note: response truncated to first 3000 characters of 4717]
