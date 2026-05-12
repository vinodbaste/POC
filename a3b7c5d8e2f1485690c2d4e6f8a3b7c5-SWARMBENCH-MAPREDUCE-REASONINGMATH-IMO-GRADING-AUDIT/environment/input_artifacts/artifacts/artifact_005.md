# artifact_005

Grading ID: GB-0613  
Problem ID: PB-Advanced-018  
Source: Novel Problem  
IMO Area: Algebra

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

For given integers $n \ge 5$ and $k \ge 1$, we color each of the $n^2$ cells of an $n \times n$ grid using one of $k$ colors. If $q$ is the largest integer which is not larger than $\frac{n^2}{k}$, then, each of the $k$ colors must be used to color exactly $q$ or $q+1$ cells. A sequence of $n$ different cells $c_1, c_2, \ldots, c_n$ in the grid is called a \textit{snake} if it satisfies the following conditions simultaneously:

 \begin{enumerate}
 \item[(a)] For each $1 \le i \le n-1$, two cells $c_i$ and $c_{i+1}$ are adjacent to their sides,
 \item[(b)] For each $1 \le i \le n-1$, cell $c_i$ and cell $c_{i+1}$ are colored with different colors.
 \end{enumerate}
 Let $a(n)$ be the minimum $k$ such that a snake exists regardless of the method of coloring. Find a constant $L$ that satisfies the following inequality and prove it:

 \[
 |La(n)- n^2 | \le n +2 \sqrt n + 3 \;.
 \]

## Reference Solution (for grader's calibration)

Let $(i, j)$ denote the cell in the $i$-th column from the left and the $j$-th row from the bottom.


 <Step 1> For any $n \geq 5$, we can color the grid with $q=3$ and $r:= n^2 - kq \leq n+\lceil 2 \sqrt{n}\rceil+2$ so that it does not satisfy the conditions. From this, we can see that $a(n) \geq \frac{n^{2}- (n+2 \sqrt{n}+3)}{3}$.


 (1) Let $m=\lceil\sqrt{n}\rceil-1$.


 (2) For the following cells, color the $2 \times 2$ square with that cell as its bottom left corner with the same color.

 \[
 \{(i, j): i, j \in \mathbb{Z}, m|i, \quad m| j, \quad 1 \leq i, j \leq n-1\}
 \]

 Color each $2 \times 2$ square with a different color. Let $A$ be the area colored in this way.


 (3) In the remaining area excluding $A$, we can color the cells so that each color is used 3 times. For any $i$ such that $m \mid i$, color the cells $(x, y)$ with $x=i$ that do not belong to $A$ with the same color as the cell above it, and color the cells $(x, y)$ with $y=i$ that do not belong to $A$ with the same color as the cell to its right. Color the remaining cells arbitrarily, but make sure that each color appears 3 or 4 times.


 (4) Since we can do this with $k=\left\lfloor\frac{n^{2}-|A|}{3}\right\rfloor, r \leq|A|+2$.


 (5) From this,
 \[
 |A|=\left\lfloor\frac{n-1}{m}\right\rfloor^{2}<\left(\frac{n-1}{\sqrt{n}-1}\right)^{2}<n+2 \sqrt{n}+1
 \]
 and $r \leq n+\lceil 2 \sqrt{n}\rceil+2$ holds.


 (6) Show that for this arrangement, there do not exist $n$ cells that satisfy the conditions. Group the cells into $m \times m$ squares starting from the bottom left of the grid. Treat any remaining cells at the top or right as if the grid were extended and group them in the same way. Each grouped section contains at most $m^{2}$ cells.


 (7) In order to start from within a grouped section and exit it, one must pass through consecutive cells of the same color due to the construction in (3) and (4). Therefore, $n \leq m^{2}$ must hold. This contradicts the definition of $m$. That is, this coloring does not satisfy the conditions.


 <Step 2> If $k \geq \frac{n^{2}}{3}$, the conditions are satisfied. Therefore, $a(n) \leq\left\lceil\frac{n^{2}}{3}\right\rceil \leq \frac{n^{2}+2}{3}$.


 (1) Consider the following graph: each cell is a vertex, and each cell is connected to the vertices of cells adjacent to it that have a different color.


 (2) Consider the $4 n-4$ cells on the border of the given $n \times n$ grid. Now, let's prove the following claim.

 Claim. For any two vertices $x, y$ belonging to the same connected component $\Phi$ on the border, if there is no vertex in $\Phi$ when moving clockwise along the border from $x$ to $y$, then the vertex one step clockwise from $x$ and the vertex one step counterclockwise from $y$ belong to the same connected component.


 (3) Let $z$ be the vertex one step clockwise from $x$ and $w$ be the vertex one step counterclockwise from $y$. Consider the boundary of the polygon formed by the cells in $\Phi$. This boundary consists of the perimeter edges of the given $n \times n$ grid or the edges shared by two adjacent cells within the $n \times n$ grid. The edge $l$ shared by $x$ and $z$ and the edge $m$ shared by $y$ and $w$ are both included in the boundary of this polygon. By the condition, on the boundary of this polygon, the line segments between $l$ and $m$ are all inside the $n \times n$ grid.


 (4) Let these line segments between $l$ and $m$ be $a_{0}, a_{1}, \cdots, a_{k}$ in order ( $a_{0}=l, a_{k}=m$ ). Each $a_{i}$ lies on the boundary between a cell belonging to $\Phi$ and a cell not belonging to $\Phi$. That is, the two cells sharing $a_{i}$ must have the same color. We will show that the cells not belonging to $\Phi$ that share $a_{i}$ all belong to the same connected component. We will use induction to show that for $i=0, \cdots, s$, the cells not belonging to $\Phi$ that share $a_{i}$ all belong to the same connected component.


 (5) Now, if $s=0$, it is trivial since there is only one cell. Therefore, using the inductive hypothesis, assume that the statement holds for $s-1$ and consider the case for $s$.


 (Case 1) If $a_{s-1}$ and $a_{s}$ lie on the same line

 This is the case where for some $2 \times 2$ square and the line connecting the midpoints of two opposite sides, one side belongs to $\Phi$ and the opposite side does not. In this case, the coloring must be symmetric with respect to this line. Therefore, the two cells not belonging to $\Phi$ must also be connected by a line segment.


 (Case 2) If $a_{s-1}$ and $a_{s}$ form a $90^{\circ}$ angle

 This means that for some $2 \times 2$ square, the two lines connecting its center to the midpoints of two consecutive sides are $a_{s-1}$ and $a_{s}$. These lines divide the $2 \times 2$ square into 1 cell and 3 cells. Place the centers of these cells on a new coordinate plane. Suppose they are divided into $(0,0)$ and $(1,0),(0,1),(1,1)$. Then $(0,0)$ and $(1,0),(0,1)$ must have the same color. Since each color is used at most 3 times, these are different from the color of $(1,1)$. Therefore, $(1,1)$ is connected to $(1,0)$ and $(0,1)$. That is, both sides of the division belong to the same connected component.


 (6) Therefore, by mathematical induction, all cells not belonging to $\Phi$ that share $a_{i}$ are in the same connected component. This means that $z$ and $w$ are in the same connected component. This completes the proof of the Claim.


 (7) Returning to the main proof, we will consider the vertices on the border. For two points $(x_1, y_1)$ and $(x_2, y_2)$, define the 'grid distance' as $|x_1 -x_2| +|y_1 - y_2|$. Let points $a$ and $b$ be the pair of points on the boarder that have the largest grid distance between them while being on the same connected component.

(8) If the grid distance between $a$ and $b$ is larger or equal to $n-1$, then the path on the connected component that connects $a$ and $b$ is a desired \textit{snake} and we are done.

(9) If the grid distance is smaller than $n-1$, then let the squares one step clockwise from $a$ and $b$ be $a_1$ and $b_1$, respectively, and the squares one step counterclockwise from $a$ and $b$ be  $a_2$ and $b_2$, respectively. Now without loss of generality, we can say the grid distance between $a_1$ and $b_2$ is smaller than $n-1$. Now think of the path along the boundary connecting $a_2$ and $b_1$, not passing $a$ and $b$. The length of this path is at least $4n-4 -(n-1)-2 = 3n-5$, so if there is a square $c$ that is in the same connected component with $a$ and $b$, the grid distance between $(a,c)$ or $(b,c)$ is larger than $n-1$, thus a contradiction to maximality. However, if there are no squares in the path from $a_2$ to $b_1$ , by Claim $a_2$ and $b_1$ must be in the same connected component, which is agian a contradiction to the maximality of $(a,b)$.

## Grading Guidelines

(Partial)
 1. Guessed $L=3$ and then explained the strategy of the proof (namely, explained how one can obtain lower and upper bound of $a(n)$ ).
 2. Partitioned the given grid into squares of size of order $\sqrt{n} \times \sqrt{n}$ or used a similar logic to determine a lower bound for $N a(n)$, but failed to meet the required lower bound as specified by the problem.
(Almost)
 1.  Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

The problem asks to find a constant $L$ such that for all integers $n \ge 5$, the inequality $|La(n)- n^2 | \le n +2 \sqrt n + 3$ holds, where $a(n)$ is the minimum $k$ such that any equitable coloring of an $n\times n$ grid with $k$ colors guarantees a snake of length $n$. Let $B(n) = n +2 \sqrt n + 3$.

We will prove that such a constant $L$ does not exist. We proceed by contradiction. Assume that such a constant $L$ exists. The inequality implies $n^2-B(n) \le La(n) \le n^2+B(n)$. Since $B(n)=O(n)$, for sufficiently large $n$, $n^2-B(n)>0$. Thus $L$ must be positive.

We will derive contradictory constraints on $L$ by constructing specific equitable colorings that do not admit a snake of length $n$, thereby establishing lower bounds on $a(n)$.

### Part 1: Derivation of the constraint $L \ge 4$

We analyze the case when $n$ is odd. Let $n=2m+1$ with $m\ge 2$ (since $n\ge 5$).

Consider the standard tiling of the $n\times n$ grid by $2\times 2$ blocks (and smaller blocks at the boundaries). Let $R_{i,j}$ be the block of cells $(x,y)$ such that $\lceil x/2 \rceil = i$ and $\lceil y/2 \rceil = j$, for $1\le i,j \le m+1$.

Let $H_T$ be the interface graph of this tiling. Two adjacent cells are connected in $H_T$ if and only if they belong to different blocks. A horizontal edge $\{(x,y), (x, y+1)\}$ is in $H_T$ iff $y$ is even. A vertical edge $\{(x,y), (x+1, y)\}$ is in $H_T$ iff $x$ is even.

**Lemma 1:** The maximum length of a simple path (snake) in $H_T$ is 4.

**Proof:** A path in $H_T$ must alternate between horizontal (H) and vertical (V) edges, otherwise two consecutive H moves, say $(x, y-1), (x,y), (x,y+1)$, would require $y-1$ and $y$ to be even, which is impossible.
Suppose there is a simple path of length 5, $c_1, \ldots, c_5$. WLOG, assume the moves are V, H, V, H. Let $c_1=(x,y)$.
Suppose the first move is V (e.g., down). $c_2=(x+1, y)$. This requires $x$ to be even.
Suppose the second move is H (e.g., right). $c_3=(x+1, y+1)$. This requires $y$ to be even.
The third move is V. Since $x+1$ is odd, the edge from $c_3$ going down is not in $H_T$. So the move must be up. $c_4=(x, y+1)$.
The fourth move is H. Since $y+1$ is odd, the edge from $c_4$ going right is not in $H_T$. So the move must be left. $c_5=(x, y)$.
Thus $c_5=c_1$, contradicting that the path is simple. Therefore, the maximum length is 4. $\blacksquare$

Now we construct an equitable coloring $C_1$. Let $K=m^2+m$.
$n^2 = (2m+1)^2 = 4m^2+4m+1 = 4K+1$.
The quotient is $q = \lfloor n^2/K \rfloor = 4$. An equitable coloring with $K$ colors must have sizes 4 or 5.

We define $C_1$ such that each color class is a union of blocks (a P-coloring).
1. The $m^2$ interior blocks $R_{i,j}$ ($1\le i,j \le m$) have size 4. Each forms a distinct color class.
2. The boundary blocks have size 2 or 1. We merge them:
For $1\le i \le m-1$, merge $R_{i, m+1}$ and $R_{m+1, i}$ (size $2+2=4$). This gives $m-1$ color classes.
3. Merge the remaining blocks $R_{m, m+1}, R_{m+1, m}, R_{m+1, m+1}$ 

[Note: response truncated to first 3000 characters of 6766]
