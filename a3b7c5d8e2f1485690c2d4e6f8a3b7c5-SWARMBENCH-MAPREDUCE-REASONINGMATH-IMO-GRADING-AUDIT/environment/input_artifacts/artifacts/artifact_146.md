# artifact_146

Grading ID: GB-0895  
Problem ID: PB-Advanced-027  
Source: USAMO 2025  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Alice the architect and Bob the builder play a game. First, Alice
 chooses two points $P$ and $Q$ in the plane and a subset $S$ of
 the plane, which are announced to Bob. Next, Bob marks infinitely
 many points in the plane, designating each a city. He may not place
 two cities within distance at most one unit of each other, and no
 three cities he places may be collinear. Finally, roads are constructed
 between the cities as follows: for each pair $A,B$ of cities, they
 are connected with a road along the line segment $AB$ if and only
 if the following condition holds: For every city $C$ distinct from
 $A$ and $B$, there exists $R\in S$ such that $\triangle PQR$ is
 directly similar to either $\triangle ABC$ or $\triangle BAC$. Alice
 wins the game if

 \noindent (i) the resulting roads allow for travel between any pair
 of cities via a finite sequence of roads and

 \noindent (ii) no two roads cross.

 \noindent Otherwise, Bob wins. Determine, with proof, which player
 has a winning strategy. (Note: $\triangle UVW$ is directly similar
 to $\triangle XYZ$ if there exists a sequence of rotations, translations,
 and dilations sending $U$ to $X$, $V$ to $Y$, and $W$ to $Z$.)

## Reference Solution (for grader's calibration)

The answer is that Alice wins. Let's define a Bob-set $V$ to be
 a set of points in the plane with no three collinear and with all
 distances at least 1 . The point of the problem is to prove the following
 fact.

 Claim - Given a Bob-set $V\subseteq\mathbb{R}^{2}$, consider the
 Bob-graph with vertex set $V$ defined as follows: draw edge $ab$
 if and only if the disk with diameter $\overline{ab}$ contains no
 other points of $V$ on or inside it. Then the Bob-graph is connected
 and planar.

 Proving this claim shows that Alice wins since Alice can specify $\mathcal{S}$
 to be the set of points outside the disk of diameter $PQ$.

 We start with proving that every Bob-graph is connected. Assume for
 contradiction the graph is disconnected. Let $p$ and $q$ be two
 points in different connected components. Since $pq$ is not an edge,
 there exists a third point $r$ inside the disk with diameter $\overline{pq}$.

 Hence, $r$ is in a different connected component from at least one
 of $p$ or $q$ - let's say point $p$. Then we repeat the same argument
 on the disk with diameter $\overline{pr}$ to find a new point $s$,
 non-adjacent to either $p$ or $r$. See the figure below, where the
 X'ed out dashed edges indicate points which are not only non-adjacent
 but in different connected components.

 In this way we generate an infinite sequence of distances $\delta_{1},\delta_{2},\delta_{3},\ldots$
 among the non-edges in the picture above. By the "Pythagorean theorem"
 (or really the inequality for it), we have

 \[
 \delta_{i}^{2}\leq\delta_{i-1}^{2}-1
 \]

 and this eventually generates a contradiction for large $i$, since
 we get $0\leq\delta_{i}^{2}\leq\delta_{1}^{2}-(i-$ $1)$.

 Now we prove that every Bob-graph is planar. Assume for contradiction
 that edges $ac$ and $bd$ meet, meaning $abcd$ is a convex quadrilateral.
 WLOG assume $\angle bad\geq90^{\circ}$ (each quadrilateral has an
 angle at least $90^{\circ}$ ). Then the disk with diameter $\overline{bd}$
 contains $a$, contradiction.

## Grading Guidelines

(Partial)
 1. Argued that Alice should take $S$ to be the exterior of the circle of diameter $PQ$.
 2. Constructed $S$ as above and proved that the resulting graph is planar.
(Almost)
 1. Constructed $S$ as above and proved that the resulting graph is connected.
 2. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

Alice has a winning strategy.

Alice's strategy is to choose $P$, $Q$, and $S$ such that the resulting graph of roads, regardless of Bob's choices (subject to his constraints), is the Strict Gabriel Graph (SGG) of the cities. We will prove that the SGG is always connected and planar under the given constraints.

**1. Alice's Strategy**

Alice chooses $P=(0,0)$ and $Q=(1,0)$.
Alice chooses the subset $S$ to be the set of all points $R$ in the plane such that the angle $\angle PRQ$ is strictly acute (less than $\pi/2$).
$S = \{R \in \mathbb{R}^2 \mid \angle PRQ < \pi/2\}$.
Geometrically, $S$ is the region strictly outside the closed disk that has $PQ$ as its diameter.

**2. Analyzing the Road Construction Rule**

Bob places an infinite set of cities $C_B$, such that (B1) any two cities are at a distance $>1$, and (B2) no three cities are collinear.

A road is constructed between cities $A$ and $B$ if and only if for every other city $C \in C_B$, there exists $R \in S$ such that $\triangle PQR$ is directly similar to $\triangle ABC$ or $\triangle BAC$.

Direct similarity implies corresponding angles are equal. In both cases ($\triangle PQR \sim \triangle ABC$ or $\triangle PQR \sim \triangle BAC$), we must have $\angle PRQ = \angle ACB$.

By Alice's definition of $S$, $R \in S$ if and only if $\angle PRQ < \pi/2$.

The condition for a road $AB$ translates to: For every city $C \neq A, B$, the angle $\angle ACB$ must be strictly acute ($< \pi/2$).
(If $\angle ACB$ is acute, there exists a triangle $\triangle PQR$ similar to $\triangle ABC$ such that $\angle PRQ = \angle ACB$. Since the angle is acute, the corresponding $R$ is in $S$. Bob's constraint (B2) ensures $\triangle ABC$ is non-degenerate, so $\angle ACB > 0$).

The resulting graph $G=(C_B, E)$ is the **Strict Gabriel Graph** (SGG) of the set $C_B$.

**3. Proof of Alice's Win**

Alice wins if $G$ is (i) connected and (ii) planar (no crossing roads).

**(ii) Planarity (No crossing roads)**

We prove this by contradiction. Suppose two roads $AB$ and $CD$ cross at a point $X$.

Bob's constraint (B2) ensures no three cities are collinear. This implies that $A, B, C, D$ are distinct, and the crossing point $X$ cannot be any of the cities. The four cities $A, B, C, D$ must form a convex quadrilateral, and the crossing roads $AB$ and $CD$ are its diagonals. Let the order of vertices be $A, C, B, D$.

If $AB$ is a road, the SGG definition requires that for any other city $K$, $\angle AKB < \pi/2$.
Specifically, $\angle ACB < \pi/2$ and $\angle ADB < \pi/2$.

If $CD$ is a road, the SGG definition requires that for any other city $K$, $\angle CKD < \pi/2$.
Specifically, $\angle CAD < \pi/2$ and $\angle CBD < \pi/2$.

The internal angles of the convex quadrilateral $ACBD$ are $\angle A = \angle CAD$, $\angle C = \angle ACB$, $\angle B = \angle CBD$, and $\angle D = \angle ADB$.

If both $AB$ and $CD$ are roads, all four internal angles are strictly less than $\pi/2$. The sum of the internal angles is:
$

[Note: response truncated to first 3000 characters of 5447]
