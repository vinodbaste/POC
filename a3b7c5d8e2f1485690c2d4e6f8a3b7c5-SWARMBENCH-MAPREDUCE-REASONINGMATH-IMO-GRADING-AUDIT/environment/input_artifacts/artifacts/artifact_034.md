# artifact_034

Grading ID: GB-0517  
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

Let $\omega_B$ be the circumcircle of $\triangle ILB$ and $\omega_C$ be the circumcircle of $\triangle ILC$.
$L$ is on $BC$ such that $IL \perp AI$.
$U \in AB, V \in AC$ such that $AU=AE, AV=AF$.
$X = LU \cap \omega_C, X \neq L$.
$Y = LV \cap \omega_B, Y \neq L$.
$P = YB \cap XC$.
We want to prove $IP \parallel XY$.

Let $s_{AI}$ denote the reflection across the line $AI$. Since $AI$ is the angle bisector of $\angle A$, $s_{AI}(AB)=AC$ and $s_{AI}(AC)=AB$.
$E=BI \cap AC$, $F=CI \cap AB$.
$s_{AI}(E)$ is a point $U'$ on $AB$ such that $AU'=AE$. By definition, $U'=U$. So $U=s_{AI}(E)$.
$s_{AI}(F)$ is a point $V'$ on $AC$ such that $AV'=AF$. By definition, $V'=V$. So $V=s_{AI}(F)$.
Let $L'=s_{AI}(L)$. Since $IL \perp AI$, $s_{AI}(IL)$ is the line through $s_{AI}(I)=I$ perpendicular to $s_{AI}(AI)=AI$. Thus $s_{AI}(IL)=IL$. Since $L$ is not on $AI$ (because $\triangle ABC$ is non-isosceles), $L' \neq L$. $L'$ must be on the line $IL$.
Let $X'=s_{AI}(X), Y'=s_{AI}(Y)$.
$X \in LU \implies X' \in s_{AI}(LU)=s_{AI}(L)s_{AI}(U)=L'E$.
$X \in \omega_C=\odot(ILC) \implies X' \in s_{AI}(\omega_C)=\odot(s_{AI}(I)s_{AI}(L)s_{AI}(C))=\odot(IL'C')$.
So $X'=L'E \cap \odot(IL'C')$.
$Y \in LV \implies Y' \in s_{AI}(LV)=L'F$.
$Y \in \omega_B=\odot(ILB) \implies Y' \in s_{AI}(\omega_B)=\odot(IL'B')$.
So $Y'=L'F \cap \odot(IL'B')$.
$P=YB \cap XC \implies P'=s_{AI}(P)=s_{AI}(YB) \cap s_{AI}(XC)=Y'B' \cap X'C'$.
$IP \parallel XY \iff s_{AI}(IP) \parallel s_{AI}(XY) \iff IP' \parallel X'Y'$.

Let's consider the special case where $X'=E, Y'=F$. This would happen if $E \in \odot(IL'C')$ and $F \in \odot(IL'B')$.
If $X'=E, Y'=F$, then $X=s_{AI}(E)=U, Y=s_{AI}(F)=V$.
$X=U \implies U \in \omega_C \implies I, L, C, U$ concyclic.
$Y=V \implies V \in \omega_B \implies I, L, B, V$ concyclic.
If $X=U, Y=V$, then $P=VB \cap UC$. We need to prove $IP \parallel UV$.
Since $U=s_{AI}(E), V=s_{AI}(F)$, $UV \perp AI$.
$IP \parallel UV \implies IP \perp AI$. This means $P$ must lie on the line $IL$.
So, if $X=U, Y=V$, the claim is equivalent to $P=VB \cap UC$ lying on $IL$.
It turns out that $X=U, Y=V$ holds. Let's prove $I, L, C, U$ concyclic.
$\angle LIU = \angle LIA - \angle UIA = 90^\circ - \angle EIA$.
$\angle LCU = \angle LCB + \angle BCU = \angle LCB + \angle(BC, CU)$.
This path seems complicated. Let's try another way.

Maybe $Y=s_{AI}(X)$?
$Y=s_{AI}(X) \implies Y \in s_{AI}(LU)=L'E$. $Y$ is on $LV$. $Y=LV \cap L'E$?
$Y=s_{AI}(X) \implies Y \in s_{AI}(\omega_C)=\odot(IL'C')$. $Y$ is on $\omega_B=\odot(ILB)$. $Y \in \odot(ILB) \cap \odot(IL'C')$?
Let $Y^*=\odot(ILB) \cap \odot(IL'C')$. $I$ is one intersection. Let $Y^*$ be the other.
Let $X^*=\odot(ILC) \cap \odot(IL'B')$. $I$ is one intersection. Let $X^*$ be the other.
$s_{AI}(Y^*)=X^*, s_{AI}(X^*)=Y^*$.
$Y=s_{AI}(X) \iff Y=Y^*, X=X^*$ and $Y^* \in LV, X^* \in LU$?
Maybe $Y=Y^*, X=X^*$ holds.
If $Y=s_{AI}(X)$, then $XY \perp AI$. $IP \parallel XY \implies IP \perp AI \implies P \in IL$.
If $P \in IL$, then $IP \perp AI$. $IP \paral

[Note: response truncated to first 3000 characters of 17619]
