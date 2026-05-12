# artifact_098

Grading ID: GB-0903  
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

Alice has a winning strategy. We provide the strategy and prove that it guarantees Alice wins regardless of Bob's choices, provided Bob follows his constraints.

We identify the plane with the set of complex numbers $\mathbb{C}$.

### 1. Mathematical Formulation

The shape of an ordered triangle $\triangle UVW$ is $Z(U, V, W) = \frac{W-U}{V-U}$.
Alice chooses $P, Q$ and $S$. Let $K = \{ Z(P, Q, R) : R \in S \}$.
Bob chooses a set of cities $\mathcal{C}$ such that (B1) $|A-B| > 1$ for distinct $A, B \in \mathcal{C}$, and (B2) no three cities are collinear.

A road connects $A$ and $B$ if for every $C \in \mathcal{C} \setminus \{A, B\}$, $z_C = Z(A, B, C)$ satisfies $z_C \in K$ or $Z(B, A, C) = 1-z_C \in K$. The set of allowed shapes is $T = K \cup (1-K)$.

### 2. Alice's Strategy: The Strict Gabriel Graph (SGG)

Alice aims to force the road network $G$ to be the Strict Gabriel Graph $SGG(\mathcal{C})$.

$A, B \in \mathcal{C}$ are connected in $SGG(\mathcal{C})$ if and only if $\angle ACB < \pi/2$ (strictly acute) for all $C \in \mathcal{C} \setminus \{A, B\}$.

In terms of shapes $z = Z(A, B, C)$, the condition $\angle ACB < \pi/2$ is equivalent to $|z - 1/2| > 1/2$. Let $T_{SGG} = \{ z \in \mathbb{C} : |z - 1/2| > 1/2 \}$.

**Alice's Strategy:**
1. Alice chooses $P=0$ and $Q=1$. Then $Z(P, Q, R) = R$, so $K=S$.
2. Alice chooses $S = T_{SGG}$.

We verify the set of allowed shapes $T$. Since $|z - 1/2| = |(1-z) - 1/2|$, if $z \in T_{SGG}$, then $1-z \in T_{SGG}$. Thus $1-S = S$, and $T = S \cup (1-S) = T_{SGG}$.

Alice's strategy ensures that a road $AB$ is constructed if and only if $\angle ACB < \pi/2$ for all $C \neq A, B$. The resulting graph $G$ is exactly $SGG(\mathcal{C})$.

We now prove that $G=SGG(\mathcal{C})$ satisfies Alice's winning conditions (i) connectivity and (ii) planarity, under Bob's constraints.

### 3. Proof of Planarity (Condition ii)

Suppose, for contradiction, that two roads $AB$ and $CD$ cross. By (B2), $A, B, C, D$ are distinct and form a convex quadrilateral, say $ACBD$.

If $AB$ is a road, then $\angle ACB < \pi/2$ and $\angle ADB < \pi/2$.
If $CD$ is a road, then $\angle CAD < \pi/2$ and $\angle CBD < \pi/2$.

The sum of the interior angles of the convex quadrilateral $ACBD$ is $2\pi$:
$2\pi = \angle ACB + \angle ADB + \angle CAD + \angle CBD$.

If both $AB$ and $CD$ are roads, summing the strict inequalities yields:
$2\pi < \frac{\pi}{2} + \frac{\pi}{2} + \frac{\pi}{2} + \frac{\pi}{2} = 2\pi$.
This contradiction ($2\pi < 2\pi$) proves that $G$ has no crossing roads and is planar.

### 4. Proof of Connectivity (Condition i)

We use Bob's constraint (B1): $d(X, Y) > 1$ for distinct cities $X, Y$.

Suppose, for contradiction, that $G$ is disconnected. Partition $\mathcal{C}$ into non-empty sets $V_1$ and $V_2$ with no roads between them.

Let $L = \inf \{ d(A, B) : A \in V_1, B \in V_2 \}$. By (B1), $L \ge 1$.

There exists a sequence of pairs $(A_n, B_n) \in V_1 \times V_2$ such that $L_n = d(A_n, B_n) \to L$ as $n \t

[Note: response truncated to first 3000 characters of 4010]
