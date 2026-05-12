# artifact_117

Grading ID: GB-0113  
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

Let $P$ be a convex $(18n+2)$-gon. The polygon is divided into $18n$ triangles by $18n-1$ non-intersecting diagonals.

This problem can be translated into a problem in graph theory. Let $T$ be the dual graph of the triangulation. The vertices of $T$ represent the triangles, and two vertices are connected by an edge if the corresponding triangles share a common side (which must be a diagonal). This graph $T$ is a tree with $18n$ vertices. An important property of the dual tree of a triangulated convex polygon is that its vertices have a maximum degree of 3. This is because each triangle has 3 sides, and the degree of a vertex in $T$ is the number of its sides that are diagonals shared with other triangles.

Choosing two diagonals in the triangulation corresponds to choosing two edges in the tree $T$. Removing two edges from a tree divides it into three connected components. The number of triangles in each of the three parts of the polygon is the number of vertices in each of these three components. Let the sizes of the three components be $c_1, c_2, c_3$. We have $c_1+c_2+c_3 = 18n$. We want to prove that we can choose two edges in $T$ such that $3n \le c_i \le 9n$ for $i=1,2,3$.

Our strategy is to find the two edges sequentially.

**Step 1: Finding the first edge $e_1$.**
We will show there is an edge $e_1$ that divides $T$ into two subtrees, $T_A$ and $T_B$, with sizes $k_A$ and $k_B=18n-k_A$, such that $6n \le k_A, k_B \le 12n$.

To find such an edge, root the tree $T$ at an arbitrary vertex $r$. For any vertex $v$, let $s(v)$ be the size of the subtree rooted at $v$.
Let $v$ be a vertex such that $s(v) \ge 6n$ and for all children $u$ of $v$, $s(u) < 6n$. Such a vertex must exist: the root $r$ has $s(r)=18n \ge 6n$. If this condition is not met at the root, one of its children must have a subtree of size $\ge 6n$. We can traverse down the tree from $r$ through vertices with subtree size $\ge 6n$ until we find our desired $v$.

We now show that $v$ cannot be the root $r$. If $v=r$, it has at most 3 children $u_1, u_2, u_3$ (since $\Delta(T) \le 3$). By the choice of $v=r$, we have $s(u_i) < 6n$ for each child. Then $18n = s(r) = 1 + \sum s(u_i)$. This implies $\sum s(u_i) = 18n-1$. However, as $s(u_i) \le 6n-1$, their sum is at most $3(6n-1) = 18n-3$. This is a contradiction ($18n-1 \le 18n-3$ is false). So $v$ cannot be the root.

Since $v$ is not the root, it has a parent and at most two children. Let the children be $u_1, u_2$. We have $s(v) = 1 + s(u_1) + s(u_2)$ (if there are two children). Since $s(u_i) < 6n$, we have $s(v) \le 1 + (6n-1) + (6n-1) = 12n-1$.
So, we have $6n \le s(v) \le 12n-1$. Let $e_1$ be the edge connecting $v$ to its parent. Removing $e_1$ splits the tree into the subtree at $v$ and the rest. The sizes of the two resulting components are $k=s(v)$ and $18n-k$. We have $k \in [6n, 12n-1]$, which implies $18n-k \in [18n-(12n-1), 18n-6n] = [6n+1, 12n]$.

So we have split $T$ into two trees, $T_A$ and $T_B$, with sizes $k_

[Note: response truncated to first 3000 characters of 5400]
