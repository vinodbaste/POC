# artifact_067

Grading ID: GB-0288  
Problem ID: PB-Advanced-009  
Source: Novel Problem  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $H$ be the orthocenter of an acute-angled triangle $A B C$, and let $D, E, F$ be the feet of the altitudes from vertices $A, B, C$ to the opposite sides, respectively. Let $G$ be the midpoint of $B C$. Let $I, J$ be the feet of the perpendiculars from $B, C$ to $AG$, respectively. Let $K (\neq D)$ be the second intersection of the circumcircles of triangle $D I F$ and triangle $D J E$. Let $M$ be the midpoint of segment $A H$. Let $L$ be the foot of the perpendicular from $M$ to $A G$. Let $R (\neq G)$ be the second intersection of the circumcircle of triangle $A H G$ with $B C$. Let $S$ be the intersection of line $A H$ and $E F$. Let $N$ be the foot of the perpendicular from point $D$ to $R S$. Let $O$ be the midpoint of segment $D N$. Let line $D N$ intersect the circumcircle of triangle $D K L$ again at point $P (\neq D)$. Let $Q (\neq C)$ be the second intersection of the circumcircle of triangle $O C P$ and line $B C$. Prove that $A B=A Q$. 

## Reference Solution (for grader's calibration)

 First, let $Z$ be the intersection of lines $E F$ and $B C$. From the harmonic relation $(Z D, B C)=-1$, we have $$D G \times D R=D H \times D A=D B \times D C=D Z \times D G,$$ which implies $D Z=D R$. Therefore $R S$ is the reflection of $E F$ with respect to $A H$. Now, let's invert the figure with respect to the circle centered at $D$ with radius $\sqrt{D B \times D C}$, and then reflect it across $A D$. Let the image of a point or figure $X$ after this transformation be denoted by $X^{\prime}$. It can be easily seen that $(A, H),(B, C),(Z, G),(E, F),(S, M)$ are pairs of corresponding points under this transformation. $I$ and $J$ are the intersections of $A G$ with $\odot(A D B)$ and $\odot(A D C)$ respectively, so $I^{\prime}=C H \cap \odot(D H Z)$ and $J^{\prime}=BH\cap \odot(D H Z)$. Also, $L=A G \cap \odot(D E F)$, so $L^{\prime}=\odot(D H Z) \cap E F$, which means $L'$ is the foot of the perpendicular from $H$ to $E F$. Let this point be $X$. Also, if we consider $A_{1}$, the reflection of $A$ across $G$, then $$A F \times A B=A H \times A D=2 A M \times A D=2 A L \times A G=A L \times A A_{1}$$ so $\left(B F L A_{1}\right)$ and $\left(C E L A_{1}\right)$ are sets of concyclic points. Therefore $A_{1}^{\prime}$ maps to $T \equiv \odot(C E X) \cap \odot(B F X)$. Meanwhile, since $A$ is the radical center of $\odot\left(B F L A_{1}\right), \odot\left(C E L A_{1}\right), \odot(B F E C)$, points $A, X, T$ are collinear. Furthermore, by the collinearity of $A, G, A_1$, $(H, Z, D, T)$ is a set of concyclic points.  Therefore, $$ \angle X T C=\angle A E F=\angle A H F=\angle E H X=\angle J^{\prime} H X=\angle J^{\prime} T X $$ so $J^{\prime}, T, C$ are collinear. For similar reasons, $\left(I^{\prime}, T, B\right)$ are also collinear. Therefore, by Pappus's theorem, $B F \cap C E=A, C J^{\prime} \cap B I^{\prime}=T, F J^{\prime} \cap E I^{\prime}=Y$ are collinear. At this point, $K$ is mapped to $Y$ by the transformation, so the four points $H, K, L, D$ are concyclic. $H, K, L, D, A_1, P$ all lie on this circle. Therefore, after the transformation (inversion then reflection), $A, T, Y, X, P^{\prime}$ are all collinear. Now, let $U$ be the foot of the perpendicular from $D$ to $E F$, and let $V$ be the midpoint of $D U$. Then from the harmonic cross-ratio $$X(D U, V \infty)=(A H, S D)=-1$$ it can be seen that $V, X, A$ must be collinear. Therefore, $A, T, X, Y, V, P^{\prime}$ are all collinear. Therefore $V^{\prime}$ must lie on the circle passing through $H, K, L, D, A^{\prime}, P$. Since $V$ is the reflection of $O$ about $A H$, $D, O, V^{\prime}$ is collinear and so is $D, O, P$. Therefore, $P \equiv V^{\prime}$. Thus, from $$ D B \times D C=D O \times D P=D Q \times D C $$ we have $D B=D Q$. This means $A B=A Q$.

## Grading Guidelines

(Partial)
 1. Observed $R$ and $Z$ are symmetric about $AD$, and  $(A, H),(B, C),(Z, G),(E, F),(S, M)$ have inverse relationships respect to $D$.
 2. Constructs the point $T$, or a similar point on the line $AT$.
(Almost)
 1. Observes $O, P$ are the corresponding points of inversion w.r.t. $D$ with radius $\sqrt{D B \times D C}$.

## Candidate Response (to be graded)

The goal is to prove that $A B=A Q$. Since $A D$ is the altitude to the line $B C$, this is equivalent to proving that $D$ is the midpoint of the segment $B Q$. Using directed segments along the line $B C$, we want to show $\overline{D Q} = -\overline{D B}$.

First, we observe that the configuration requires the triangle $A B C$ to be non-isosceles with $A B \neq A C$. If $A B=A C$, then $D=G$. The points $A, H, G$ are collinear, so the circumcircle of $\triangle A H G$ is undefined, and $R$ is undefined. Thus, we assume $A B \neq A C$, so $G \neq D$.

The point $Q (\neq C)$ is the second intersection of the circumcircle of $\triangle O C P$ with the line $B C$. The point $D$ lies on $B C$. The points $O$ and $P$ lie on the line $D N$ by definition ($O$ is the midpoint of $D N$, and $P$ is on the line $D N$).
The power of the point $D$ with respect to the circumcircle $(O C P)$ is:
$$ \mathcal{P}(D) = \overline{D C} \cdot \overline{D Q} = \overline{D O} \cdot \overline{D P} $$
We want to prove $\overline{D Q} = -\overline{D B}$. This is equivalent to proving:
$$ \overline{D O} \cdot \overline{D P} = -\overline{D B} \cdot \overline{D C} $$
It is a known property of the orthocenter $H$ that $\overline{D A} \cdot \overline{D H} = -\overline{D B} \cdot \overline{D C}$. Let $\rho^2 = \overline{D A} \cdot \overline{D H}$. Since the triangle is acute, $\rho^2>0$.
Since $O$ is the midpoint of $D N$, $\overline{D O} = \frac{1}{2} \overline{D N}$. The condition becomes:
$$ \frac{1}{2} \overline{D N} \cdot \overline{D P} = \rho^2 \quad \iff \quad \overline{D N} \cdot \overline{D P} = 2\rho^2 $$

To prove this relation, we utilize a coordinate system. Let $D$ be the origin $(0,0)$. Let $B C$ be the x-axis and $A D$ be the y-axis. Let $A(0, a)$ and $H(0, h)$. Then $\rho^2=ah$. Since the triangle is acute, $a>0, h>0$.
$G$ is the midpoint of $B C$. Let $G(g, 0)$. Since $A B \neq A C$, $g \neq 0$.
$M$ is the midpoint of $A H$. $M(0, m)$, where $m=(a+h)/2$.

We analyze the points $R, S, N$.
$R(\neq G)$ is the second intersection of $(A H G)$ with $B C$. The power of $D$ with respect to $(A H G)$ is $\overline{D A} \cdot \overline{D H} = \overline{D G} \cdot \overline{D R}$. So $ah = g \cdot \overline{D R}$. $R(r, 0)$ with $r=ah/g$.
$S$ is the intersection of $E F$ and $A H$. It is known that $(A, H; D, S)$ is a harmonic cross-ratio. Since $M$ is the midpoint of $A H$, by Newton's relation $MD \cdot MS = MA^2$. This leads to the coordinate of $S(0, s)$ where $s=ah/m$.

$N$ is the projection of $D(0, 0)$ onto the line $R S$. The line $R S$ connects $(r, 0)$ and $(0, s)$. Its equation is $x/r+y/s=1$, or $sx+ry=rs$.
The line $D N$ is perpendicular to $R S$, so its equation is $rx-sy=0$.
Substituting $r=ah/g$ and $s=ah/m$:
$RS$: $(ah/m)x+(ah/g)y=(ah)^2/(gm)$. $gx+my=ah$.
$DN$: $(ah/g)x-(ah/m)y=0$. $mx-gy=0$.

Now we introduce an auxiliary point $P^*$. Let $X$ be the point such that $D G X M$ is a rectangle. $X(g, m)$. Let $P^*$ be the reflection of $D$ across $X$. $P^

[Note: response truncated to first 3000 characters of 5748]
