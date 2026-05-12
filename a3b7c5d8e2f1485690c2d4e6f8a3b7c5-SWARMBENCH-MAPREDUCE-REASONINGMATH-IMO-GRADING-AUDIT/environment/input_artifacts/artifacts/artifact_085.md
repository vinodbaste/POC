# artifact_085

Grading ID: GB-0102  
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

The triangulation of the polygon $P$ defines a dual graph $G$ which is a tree with $18n$ vertices (representing the triangles) and $18n-1$ edges (representing the diagonals). The maximum degree of $G$ is 3, as each triangle has at most 3 sides. We are looking for two edges in $G$ such that their removal divides $G$ into three components, each having a size (number of vertices) between $3n$ and $9n$.

Let's use the concept of a centroid of a tree. A centroid of a tree $T$ is a vertex $C$ such that any component of $T-C$ has size at most $|T|/2$.

Let $G$ be the dual tree with $|G|=18n$. Let $C$ be a centroid of $G$. The components of $G-C$, denoted by $K_1, \dots, K_k$, have sizes $S_i = |K_i| \le 9n$. Since the maximum degree of $G$ is 3, we have $k \le 3$. The total number of vertices is $\sum S_i + 1 = 18n$.

We analyze the possible values of $k$.
If $k=1$, $S_1 = 18n-1$. But $S_1 \le 9n$, so $18n-1 \le 9n$, which means $9n \le 1$. This is impossible since $n$ is a positive integer.
If $k=2$, $S_1+S_2 = 18n-1$. Assume $S_1 \ge S_2$. Then $S_1 \ge (18n-1)/2 = 9n-1/2$. Since $S_i$ are integers, $S_1 \ge 9n$. Since $S_1 \le 9n$, we must have $S_1=9n$. Then $S_2=9n-1$.
If we choose the two edges incident to $C$, the three parts have sizes $S_1=9n$, $S_2=9n-1$, and the vertex $C$ itself, which has size 1. We require all parts to be at least $3n$. So $1 \ge 3n$, which implies $n \le 1/3$. This is impossible for a positive integer $n$.

Thus, we must have $k=3$. Let $S_1 \ge S_2 \ge S_3$. We have $S_1+S_2+S_3 = 18n-1$.
$S_1 \ge (18n-1)/3 = 6n-1/3$, so $S_1 \ge 6n$. Also $S_1 \le 9n$.
$S_3 \le (18n-1)/3$, so $S_3 \le 6n-1$.

We consider two cases based on the size of $S_3$.

Case 1: $S_3 \ge 3n$.
Since $S_1 \ge S_2 \ge S_3$, we have $S_1, S_2, S_3 \ge 3n$.
We choose the two diagonals corresponding to the edges connecting $C$ to $K_1$ and $C$ to $K_2$.
The three resulting parts are $K_1$, $K_2$, and $K_3 \cup \{C\}$.
Their sizes are $S_1, S_2, S_3+1$.
We check the constraints. $S_1, S_2 \ge 3n$. $S_3+1 \ge 3n+1 > 3n$.
$S_1, S_2 \le 9n$. $S_3+1 \le 6n-1+1 = 6n \le 9n$ (since $n \ge 0$).
So in this case, we found the required two diagonals.

Case 2: $S_3 < 3n$.
We have $S_1+S_2 = 18n-1-S_3 > 18n-1-3n = 15n-1$.
Since $S_1, S_2 \le 9n$, we have $S_1+S_2 \le 18n$.
Also, $S_2 = 18n-1-S_1-S_3$. Since $S_1 \le 9n$ and $S_3 \ge 1$ (as $k=3$), $S_2 \ge 18n-1-9n-S_3 = 9n-1-S_3$.
Since $S_3 \le 3n-1$, $S_2 \ge 9n-1-(3n-1) = 6n$.
So $S_1, S_2 \in [6n, 9n]$.

Let $e_1$ be the edge connecting $C$ to $K_1$. We choose $e_1$ as the first diagonal.
Removing $e_1$ splits $G$ into two components: $C_1=K_1$ and $C_2=G-K_1$.
$|C_1| = S_1 \in [6n, 9n]$. This part satisfies the condition.
$|C_2| = 18n-S_1$. Since $6n \le S_1 \le 9n$, we have $9n \le |C_2| \le 12n$.

Now we need to find a second diagonal $e_2$ within $C_2$ that splits $C_2$ into two parts $C_{21}$ and $C_{22}$ such that $3n \le |C_{2i}| \le 9n$.
$C_2$ is a connected subgraph of $G$, so it is a tree and its maxim

[Note: response truncated to first 3000 characters of 4412]
