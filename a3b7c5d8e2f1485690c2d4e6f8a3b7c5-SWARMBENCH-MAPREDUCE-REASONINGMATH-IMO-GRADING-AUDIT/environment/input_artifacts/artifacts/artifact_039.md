# artifact_039

Grading ID: GB-0032  
Problem ID: PB-Advanced-002  
Source: Novel Problem  
IMO Area: Geometry

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

There are 120 students in DeepMind highschool, and each student `loves' some of the students. Here `love' is not always a mutual relationship; a student A may love B while B may not love A, and it is also possible that a student loves oneself. For the set $F$ of all $2^{120}$ subsets of the students, define the function $f: F \rightarrow F$ as the function that maps each $X \in F$ to the set of students loved by one or more students in $X$. For $A, B \in F$, $A$ and $B$ are said to have a 'lovely relationship' iff there exists a natural number $k$ such that $f^{k}(A)=B$. Now we want to select distinct elements $A_{1}, A_{2}, \cdots A_{t}$ from $F$ such that for any $1 \leq i<j \leq t$, $A_{i}$ and $A_{j}$ have a lovely relationship. Let $M(f)$ be the maximum possible value of $t$.  Show that $M(f) \leq 2^{70}$. 

## Reference Solution (for grader's calibration)

To being with, we prove there must be some $A \in F$ such that $\left\{A_{1}, \cdots A_{t}\right\} \subset \cup_{i=0}^{\infty}\left\{f^{i}(A)\right\}$. Why is this? Consider a graph $H$ with $A_{1}, A_{2}, \cdots A_{t}$ as its vertices. If $f^{k}\left(A_{i}\right)=A_{j}$ for some $k$, draw a directed edge $A_{i} \rightarrow A_{j}$ to create a directed graph. This graph is a tournament. Now, if there is a vertex $A$ such that $d^{-}(A)=0$, then it holds directly. If not, then in this graph, the in-degree of any vertex is at least 1. This means the graph contains a cycle. Having a cycle means that for each element $A$ in the cycle, there is some $T$ such that $f^{T}(A)=A$. Therefore, for two vertices $A, B$ in the cycle, if $f^{i}(A)=B$, then $f^{T-i}(B)=A$. This means any two vertices in the cycle can reach each other via applications of $f$. Now, if we remove all but one vertex from the cycle and then use induction on the number of vertices, we can immediately find that there is a vertex $A$ such that $d^{+}(A)=t-1$. Thus, we can obtain our desired conclusion.

Now, considering a directed graph $G$ whose vertices are the students and where an edge $i \rightarrow j$ is drawn if student $i$ loves student $j$, we need to find $\max_{A_0 \in F} \left| \{f^i(A_0) \mid i \in \mathbb{Z}_{\ge 0} \} \right|$. Now, in $G$, let's perform the following procedure: \begin{itemize} \item Pick any cycle in $G$ and call it $C_{1}$. \item Pick any cycle in $G-C_{1}$ (the graph after removing all vertices of $C_1$) and call it $C_{2}$. \item Repeat this procedure until no more cycles can be found. \end{itemize} As a result of this procedure, we will have disjoint cycles $C_{1}, C_{2}, \cdots, C_{m}$, and a graph $H$ (which is $G - \bigcup C_i$) that has no cycles. Let $a_i$ be the number of vertices in $C_i$, and let $|V(H)|=x$. Then $a_{1}+a_{2}+\cdots+a_{m}=n-x \leq n$ (where $n=120$). Let $L =c\operatorname{lcm}\left[a_{1}, a_{2}, \cdots, a_{m}\right]$, where $c$ is the smallest positive integer such that $L\ge n$.
\\Consider some nonempty $A \subset V(G)$. Now, if we define $T(k) = \bigcup_{j=1}^{m} (f^{k}(A) \cap C_{j})$, then since each $|f^{k}(A) \cap C_{j}|$ is non-decreasing, $|T(k)|$ is a non-decreasing function. Now let's look at $|T(L)|, \cdots, |T((2n+1)L)|$. Since $|T(k)| \leq |V(G)|=n$ and $|T(k)|$ is non-decreasing, there exists some $i$ such that $|T(iL)|=|T((i+1)L)|=|T((i+2)L)|$. At this point, by the definition of $L$, it must be that $T(iL) \subset T((i+1)L) \subset T((i+2)L)$, and therefore $T(iL)=T((i+1)L)=T((i+2)L)$. Therefore, for each $1 \leq r < L$, $T(iL+r)=T((i+1)L+r)$ also holds.
\\Now, if $f^{(i+2)L}(A) \neq f^{(i+1)L}(A)$, then there must be a $v_{0} \in f^{(i+2)L}(A) \triangle f^{(i+1)L}(A)$ (symmetric difference; $A \triangle B=(A-B) \cup (B-A)$), and in this case, $v_{0} \in H$ must hold. Therefore, there also exists $v_1 \in f^{(i+2)L-1}(A) \triangle f^{(i+1)L-1}(A)$ (from which $v_0$ is reached), and $v_2 \in \dots$, so we can keep finding $v_j$ such that there is a path $v_k \rightarrow \dots \rightarrow v_1 \rightarrow v_0$. If $v_1 , v_2, \cdots, v_{|V(H)|+1}$ are all in $H$, then some point should appear at least twice, which is a contradiction to the fact that $H$ has no cycles. Therefore, there exists some $k \le n$ such that $v_k \not \in H$, or equivalently  $v_k \in \bigcup C_j$. However, since $v_k \in f^{(i+2)L -k} (A) \triangle f^{(i+1)L -k} (A)$ where $k \le n \le L$, this is a contradiction to the observation above that $T(iL+r)=T((i+1)L+r)$ for each $1\le r \le L$.

Thus, $f^{(i+2)L}(A)=f^{(i+1)L}(A)$ and thus it follows that $\left\{f^{j}(A) \mid j \in \mathbb{Z}_{\ge 0}\right\}=\left\{f^{j}(A) \mid j \leq (i+1)L \right\}$. Since $i <2n$, we can conclude that $M(f) \leq 2nL$.
\\Now, $\operatorname{lcm}[a_1, a_2, \cdots, a_m] \leq 120 \cdot 60 \cdot 40 \cdot 30 \cdot 24 \cdot 20 \cdot 17 \cdot 15 \cdot 13 \cdot \operatorname{lcm}[1,2,3, \cdots, 12]<2^{60}$ so $L \le \max\{2^{60}, 2n\} = 2^{60}$ Since $2n=240<2^8$, $2nL < 2^8 \cdot 2^{60} = 2^{68}$.

## Grading Guidelines

(Partial)
 1. Proved there must be some $A \in F$ such that $\left\{A_{1}, \cdots A_{t}\right\} \subset \cup_{i=0}^{\infty}\left\{f^{i}(A)\right\}$.
 2. Considered the non-intersecting cycles
(Almost)
 1.  Introduced a quantity like $\lcm[a_1, a_2, \cdots, a_n]$, but failed to find the desired numerical bound.
 2.  Verification contains minor mistakes only.

## Candidate Response (to be graded)

Let $S$ be the set of 120 students, so $N=120$. Let $F=2^S$ be the set of all subsets of students. The 'love' relationship defines a directed graph $G=(S, E)$. The function $f: F \rightarrow F$ is defined such that for $X \subseteq S$, $f(X)$ is the set of students loved by at least one student in $X$. That is, $f(X) = \{y \in S \mid \exists x \in X, (x, y) \in E\}$.

Two distinct subsets $A, B \in F$ have a 'lovely relationship' if $f^k(A)=B$ for some natural number $k \geq 1$. We are looking for the maximum size $t$ of a sequence of distinct elements $A_1, \dots, A_t \in F$ such that for $1 \leq i < j \leq t$, $A_i$ and $A_j$ have a lovely relationship. This means the sequence $A_1, \dots, A_t$ is strictly ordered along a trajectory of $f$. $M(f)$ is the maximum possible value of $t$, which corresponds to the maximum length of an orbit (trajectory) of distinct sets generated by $f$.

The function $f$ is additive, meaning $f(X \cup Y) = f(X) \cup f(Y)$. We can represent this dynamic system using Boolean matrices. Let $M$ be the $N \times N$ adjacency matrix of the graph $G$. If we represent a subset $X$ by its characteristic row vector $v_X \in \{0, 1\}^N$, then $f(X)$ corresponds to the Boolean matrix-vector product $v_X M$. The trajectory starting at $A_1=X$ is given by $f^k(X)$, which corresponds to $v_X M^k$ (where $M^0=I$).

The length of the trajectory starting at $X$ is the number of distinct vectors in the sequence $(v_X M^k)_{k \geq 0}$. This length is bounded by the number of distinct matrices in the sequence of powers of $M$, $(M^k)_{k \geq 0}$.

The sequence of powers of a Boolean matrix eventually becomes periodic. Let $k(M)$ be the index (the smallest $k \geq 1$ such that $M^k$ belongs to the cycle) and $d(M)$ be the period (the length of the cycle). The number of distinct matrices in $\{M^k\}_{k \geq 1}$ is $O(M) = k(M)+d(M)-1$. The total number of distinct matrices including $M^0=I$ is at most $1+O(M) = k(M)+d(M)$.
Thus, $M(f) \leq k(M)+d(M)$.

We want to find an upper bound for $M(f)$ over all possible graphs, which means bounding the maximum possible value of $k(M)+d(M)$ for an $N \times N$ Boolean matrix.

We use established bounds from the theory of Boolean matrices.
1. The period $d(M)$ is bounded by Landau's function $g(N)$, which is the maximum least common multiple (LCM) of partitions of $N$. $d(M) \leq g(N)$.
2. The index $k(M)$ is bounded in terms of the period $d(M)$. A result by J. L. Nicolas (1985, Théorème 1) states that:
$$k(M) \leq N + \frac{N(N-1)}{2} d(M).$$

Combining these bounds, we get:
$$M(f) \leq k(M)+d(M) \leq N + d(M) \left(1 + \frac{N(N-1)}{2}\right).$$
$$M(f) \leq N + g(N) \left(1 + \frac{N(N-1)}{2}\right).$$

Now we calculate this bound for $N=120$.
First, we calculate the polynomial factor:
$P(N) = 1 + \frac{N(N-1)}{2} = 1 + \frac{120 \times 119}{2} = 1 + 60 \times 119 = 1 + 7140 = 7141$.

Next, we need to bound $g(120)$. We can use a rigorous upper bound for Landau's function established by J. P. Ma

[Note: response truncated to first 3000 characters of 4121]
