# artifact_025

Grading ID: GB-0098  
Problem ID: PB-Advanced-004  
Source: Novel Problem  
IMO Area: Number_Theory

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

For a positive integer $n$, a convex $18n+2$-gon $P$ is divided into $18n$ triangles by drawing $18n-1$ diagonals. Prove that we can choose two of these diagonals such that the three parts of $P$ divided by these two diagonals each contain at least $3n$ and at most $9n$ triangles.

## Reference Solution (for grader's calibration)

First, let's look at the following well-known theorem.

 <Lemma>
 For a graph $G$ with $n$ vertices, the following four statements are equivalent. Therefore, if one of them holds, $G$ is a tree.

 (A) $G$ is connected and has no cycles.

 (B) $G$ is connected and has $n-1$ edges.

 (C) $G$ has $n-1$ edges and no cycles.

 (D) There is exactly one path between any two vertices in $G$.

 The following lemma is a general fact about the division of trees.

 For a positive integer $k \geq 2$, if the degree of each vertex in a tree is at most $k$, then we can remove an edge from the tree so that both resulting connected components have size at least $\frac{n-1}{k}$.

 <Proof of Lemma>

 (1) Let $H_{e}, K_{e}$ be the two connected components obtained by removing an edge $e$ from the tree, and let $h_{e}, k_{e}$ be the number of vertices in the two components. (Of course, $h_{e}+k_{e}=n$.) Let $l=\{x, y\}$ be the edge for which $\min \left(h_{e}, k_{e}\right)$ is maximized. (If there are multiple such edges, choose one arbitrarily)

 (2) Assume for contradiction that the smaller component obtained by removing $l$ has size less than $\frac{n-1}{k}$. Without loss of generality, let this be the component containing $x$. Let this component be $A$.

 (3) Now, for any edge $e$ other than $l$ connected to vertex $y$, if we remove that edge instead of $l$, let $H_{e}$ be the component containing $l$ and $K_{e}$ be the other component. Then $H_{e}$ contains $A$, so it is larger than $A$. If the number of vertices in $H_{e}$ is less than or equal to the number of vertices in $K_{e}$, then it contradicts the maximality of $A$. Therefore, the number of vertices in $K_{e}$ must be less than the number of vertices in $H_{e}$. Therefore, by the maximality of $A$, the number of vertices in $K_{e}$ is less than or equal to the number of vertices in $A$, and therefore less than $\frac{n-1}{k}$.

 (4) Therefore, when we remove each edge adjacent to vertex $y$, each resulting connected component has less than $\frac{n-1}{k}$ vertices. Since the degree of vertex $y$ is at most $k$, there are at most $k$ such components, and therefore the number of vertices excluding $y$ is less than $\frac{n-1}{k} \times k=n-1$, which is a contradiction.

 Therefore, the proof is complete. \qed

 Now, let's prove the problem. First, let's look at the general properties of triangulation of a convex $n$-gon before looking at the convex $18n+2$-gon.

 <Step 1> Basic properties of triangulation of a convex polygon

 <Step 1.1> The sum of the interior angles of a convex $n$-gon is $(n-2) \pi$. Therefore, in order for triangles with an interior angle sum of $\pi$ to divide this sum, we need a total of $n-2$ triangles. Since each time we draw a diagonal, the division of the convex $n$-gon increases by one, we know that if we have divided a convex $n$-gon into $n-2$ triangles, we have drawn a total of $n-3$ diagonals. In summary, to triangulate a convex $n$-gon, we need to draw $n-3$ diagonals to divide it into $n-2$ triangles.

 <Step 1.2> If $n \geq 4$, then there are $n-2$ triangles, and each triangle cannot have all 3 sides as sides of the convex $n$-gon. Therefore, there must be at least 2 triangles that share 2 sides with the convex $n$-gon.

 <Step 2> Mapping triangulation of a convex polygon to a tree

 The problem of dividing a convex $n$-gon $P$ into triangles is directly related to trees. For convenience, assume $n \geq 4$. Let's consider the triangles as vertices and connect two vertices if the corresponding triangles share a side to draw a graph $G$.

 <Step 2.1> By <Step 1>, this graph has $n-2$ vertices and $n-3$ edges. (This is because each diagonal drawn during the division corresponds to one edge in $G$.)

 <Step 2.2> We can confirm that this graph $G$ is connected by mathematical induction. The case $n=4$ is trivial. Now, assume that $G$ is connected for triangulations of convex $n-1$-gons for $n \geq 5$, and consider a triangulation $T$ of a convex $n$-gon $P$. By (2) of <Step 1>, this triangulation includes a triangle $X$ that has two consecutive sides of $P$.

 <Step 2.3> The vertex corresponding to this triangle $X$ has degree 1 in graph $G$. Let $Y$ be the vertex connected to $X$. Now, the remaining part of the $n$-gon $P$ excluding triangle $X$ is an $n-1$-gon $P^{\prime}$, and if we remove triangle $X$ from triangulation $T$, the remaining part is $T^{\prime}$, which is a triangulation of $P^{\prime}$. Let $G^{\prime}$ be the graph for this triangulation. Clearly, $G^{\prime}$ is the graph obtained by removing vertex $X$ and edge $XY$ from $G$. By the inductive hypothesis, $G^{\prime}$ is connected, so the graph $G$ obtained by adding edge $XY$ to it is also connected.

 In conclusion, graph $G$ is a connected graph with $n-2$ vertices and $n-3$ edges. Therefore, by -(B), $G$ is a tree.

 <Step 3> Analysis of the problem situation

 <Step 3.1> According to the above analysis, we can see that the triangulation given in the problem corresponds to a tree $T$ with $18n$ vertices. It is very important that the degree of each vertex in this tree is at most 3.

 <Step 3.2> Choosing two diagonals to divide the convex $18n+2$-gon can be thought of as removing two edges from this tree to divide it into three connected components. The question is whether we can do this so that the size of each connected component is at least $3n-1$ and at most $8n+1$.

 <Step 4> Solving the problem

 <Step 4.1> First, the tree $T$ corresponding to the triangulation has $18n$ vertices, and the degree of each vertex is at most 3. Therefore, by Lemma, we can remove one edge to make the sizes of the two resulting components at least $6n-1$.

 <Step 4.2> Let $A$ be the component with fewer vertices and $B$ be the component with more vertices (if the sizes are the same, assign $A$ and $B$ arbitrarily). The number of vertices in $A$ is at least $6n-1$ and at most $9n$, and the number of vertices in $B$ is at least $9n$ and at most $12n+1$.

 <Step 4.3> Since $B$ is also a tree with degree at most 3, we can apply again to $B$. By removing one edge from $B$, we can divide it into $B_{1}, B_{2}$ so that the size of each component is at least $\frac{9n-1}{3}$ and at most $\frac{2(12 n+1)+1}{3}=8 n+1$. Therefore, the sizes of $B_{1}, B_{2}$ are at least $3n$ and at most $8n+1$.

 <Step 4.4> Therefore, we can divide it into $A, B_{1}, B_{2}$.

## Grading Guidelines

(Partial)
 1. Found a first diagonal that cuts the polygon into at least $3n$ triangles, or attempted an argument where an unbalanced cut can be modified to create a more balanced cut.
 2. Successfully connected the triangulation with a tree.
(Almost)
 1. Established first cut diagonal as and in the solution attempts to successively apply the argument again on one of the sides, but with errors (e.g. not fulfilling the same hypotheses as the original cut).

## Candidate Response (to be graded)

Let $V$ be the number of vertices of the polygon $P$. We are given $V = 18n+2$.
The polygon $P$ is divided into $T$ triangles by $D$ diagonals.
The number of triangles is $T = V-2 = (18n+2) - 2 = 18n$.
The number of diagonals is $D = V-3 = (18n+2) - 3 = 18n-1$. This matches the problem statement.

We need to choose two diagonals, say $d_1$ and $d_2$. These two diagonals divide $P$ into three parts.
Let $P$ be the set of vertices $\{v_0, v_1, \dots, v_{18n+1}\}$. The edges of $P$ are $(v_i, v_{i+1})$ (indices mod $18n+2$).
The polygon is triangulated. Let $\mathcal{T}$ be the set of triangles, $|\mathcal{T}| = 18n$.
Let $\mathcal{D}$ be the set of $18n-1$ diagonals used in the triangulation.

We need to choose $d_1, d_2 \in \mathcal{D}$.
These two diagonals divide $P$ into three parts. Let's analyze how this happens.

If $d_1$ and $d_2$ intersect in the interior of $P$, then they divide $P$ into four parts.
However, the diagonals belong to a triangulation. In a triangulation, diagonals cannot cross each other.
So $d_1$ and $d_2$ do not intersect in the interior of $P$.
They could share a vertex. Or they are disjoint.

Let's consider what happens when we remove a diagonal $d$ from the triangulation.
Let $\mathcal{T}$ be the set of triangles. The sides of these triangles are either edges of $P$ or diagonals in $\mathcal{D}$.
Each diagonal in $\mathcal{D}$ is a side of exactly two triangles in $\mathcal{T}$.
If we remove $d$, these two triangles merge into a quadrilateral.

If we want to divide $P$ into parts, we are talking about subpolygons of $P$.
When we choose a diagonal $d \in \mathcal{D}$, it cuts $P$ into two smaller polygons, say $P_1$ and $P_2$.
Since we have a fixed triangulation, $P_1$ and $P_2$ are also triangulated by a subset of $\mathcal{D}$.
Let $T(Q)$ denote the number of triangles in a polygon $Q$ (in this triangulation).
$T(P) = 18n$.
If $d$ divides $P$ into $P_1$ and $P_2$, then $T(P_1) + T(P_2) = T(P) = 18n$.

Now we choose two diagonals $d_1$ and $d_2$.
Since they don't cross, they divide $P$ into three parts.
Let's visualize this.
Imagine the polygon $P$.
$d_1$ connects two vertices $u_1, v_1$ of $P$. $d_2$ connects $u_2, v_2$.
Since they don't cross, the vertices must appear in a specific order around the boundary of $P$.
Let's say we list the vertices in counterclockwise order.

If $d_1$ and $d_2$ share a vertex, say $v_1 = u_2$. Then $d_1 = (u_1, v_1)$ and $d_2 = (v_1, v_2)$.
The polygon $P$ is divided into three parts by $d_1$ and $d_2$.
One part is the triangle formed by $u_1, v_1, v_2$ if $(u_1, v_2)$ is also a diagonal or an edge of $P$.
But we are given a triangulation.

Let's consider the dual graph of the triangulation.
The dual graph $G$ has vertices corresponding to triangles in $\mathcal{T}$. Two vertices in $G$ are connected if the corresponding triangles share a side (which must be a diagonal in $\mathcal{D}$).
Since $P$ is a polygon, the dual graph is a tree.
There are $T=18n$ nodes in $G$.
Diagonals in $\mathc

[Note: response truncated to first 3000 characters of 46669]
