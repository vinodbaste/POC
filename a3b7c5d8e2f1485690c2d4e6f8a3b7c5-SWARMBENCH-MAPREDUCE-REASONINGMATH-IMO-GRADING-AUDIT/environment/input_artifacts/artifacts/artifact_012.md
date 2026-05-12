# artifact_012

Grading ID: GB-0889  
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

Alice's strategy is to choose the points $P, Q$ and the set $S$ such that the resulting graph of roads constructed between Bob's cities is the Gabriel Graph of that set of cities. We will show that the Gabriel Graph, under the constraints imposed on Bob, is always connected and planar.

### 1. Understanding the Road Condition

Let us represent the points in the plane as complex numbers. The shape of a triangle $\triangle UVW$ can be characterized by the complex number $(W-U)/(V-U)$. $\triangle UVW$ is directly similar to $\triangle XYZ$ if and only if $(W-U)/(V-U) = (Z-X)/(Y-X)$.

Alice chooses $P$ and $Q$. Let $S$ be the subset Alice chooses. The set of allowed shapes $K$ is derived from $S$. A shape $z_R$ corresponding to $R \in S$ is $z_R = (R-P)/(Q-P)$.
Let $K_S = \{z_R \mid R \in S\}$.

A road exists between cities $A$ and $B$ if, for every other city $C$, the shape of $\triangle ABC$, $z_{ABC} = (C-A)/(B-A)$, satisfies $z_{ABC} \in K_S$ (similarity to $\triangle PQR$) or the shape of $\triangle BAC$, $z_{BAC} = (C-B)/(A-B) = 1-z_{ABC}$, satisfies $z_{BAC} \in K_S$ (similarity to $\triangle QPR$).

The set of allowed shapes for $\triangle ABC$ is $K = K_S \cup (1-K_S)$, where $1-K_S = \{1-z \mid z \in K_S\}$.

### 2. Alice's Winning Strategy: The Gabriel Graph

Alice chooses $P$ and $Q$ to be distinct points. Without loss of generality, by applying a similarity transformation (which preserves the conditions of the game), we can set $P=0$ and $Q=1$. Then $K_S = S$.

Alice chooses $S$ to be the set of complex numbers $z$ such that $|z-1/2| > 1/2$.
$S = \{z \in \mathbb{C} : |z-1/2| > 1/2\}$.

Geometrically, $S$ is the exterior of the closed disk whose diameter is the segment $PQ$ (from 0 to 1).

This set $S$ is symmetric with respect to the point $1/2$. If $z \in S$, then $|z-1/2| > 1/2$. Since $|(1-z)-1/2| = |-z+1/2| = |z-1/2|$, we have $1-z \in S$.
Therefore, $K_S = S$ and $1-K_S = S$. The set of allowed shapes is $K = S \cup (1-S) = S$.

The condition for a road between $A$ and $B$ is: for every other city $C$, $z_{ABC} \in S$.
$z_{ABC} = (C-A)/(B-A)$. The condition is $|z_{ABC}-1/2| > 1/2$.

Let's analyze this geometric condition:
$|\frac{C-A}{B-A} - \frac{1}{2}| > \frac{1}{2}$
$|\frac{2(C-A) - (B-A)}{2(B-A)}| > \frac{1}{2}$
$|\frac{2C - A - B}{2(B-A)}| > \frac{1}{2}$
$|C - \frac{A+B}{2}| > \frac{|B-A|}{2}$.

Let $M = (A+B)/2$ be the midpoint of $AB$. Let $r = |B-A|/2$ be half the length of $AB$. The condition is $|C-M| > r$.

This means that the city $C$ must lie strictly outside the open disk that has the segment $AB$ as its diameter.

The graph constructed by this rule is known as the (strict) Gabriel Graph (GG) of the set of cities.

### 3. Bob's Constraints

Bob chooses an infinite set of cities $C_B$ such that:
(i) $d(A, B) > 1$ for all $A \neq B \in C_B$.
(ii) No three cities are collinear.

Constraint (i) implies that $C_B$ is locally finite (any bounded region of the plane contains finitely many citie

[Note: response truncated to first 3000 characters of 6873]
