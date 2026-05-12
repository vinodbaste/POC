# artifact_050

Grading ID: GB-0036  
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

Here is a proof that $M(f) \leq 2^{70}$, relying on known results from the theory of Boolean matrices.

1.  **Understanding the Setup**
    Let $S$ be the set of $N=120$ students. The 'love' relationships define a directed graph $G=(S, E)$.
    $F = 2^S$ is the set of all subsets of students.
    The function $f: F \rightarrow F$ is defined as $f(X) = N^+(X)$, the set of students loved by at least one student in $X$.
    $M(f)$ is the maximum length of a sequence of distinct subsets $A_1, \dots, A_t$ such that for $i<j$, $A_j = f^{k_{ij}}(A_i)$ for some $k_{ij} \geq 1$. This implies that $A_1, \dots, A_t$ form a segment of a trajectory under $f$. Thus, $M(f)$ is the maximum length of any trajectory of $f$.

2.  **f as a Linear Operator (Additive Map)**
    The function $f$ is additive (a join-homomorphism) on the Boolean lattice of subsets of $S$:
    $f(X \cup Y) = N^+(X \cup Y) = N^+(X) \cup N^+(Y) = f(X) \cup f(Y)$.

    We can represent $f$ using the adjacency matrix $M$ of the graph $G$. Let $M$ be the $N \times N$ Boolean matrix where $M_{ij}=1$ if student $i$ loves student $j$, and $0$ otherwise.
    We consider the Boolean semiring $(\{0, 1\}, \lor, \land)$, where addition is OR and multiplication is AND.
    If we represent a subset $X \subseteq S$ by its characteristic row vector $v_X \in \{0, 1\}^N$, the function $f$ corresponds to matrix multiplication:
    $v_{f(X)} = v_X M$.

3.  **Trajectories and Matrix Powers**
    The iterates of $f$ correspond to the powers of $M$:
    $v_{f^k(X)} = v_X M^k$.

    The sequence of matrix powers $M^k$ (starting from $k=0$, where $M^0=I$) in the Boolean semiring must eventually become periodic, since there are finitely many $N \times N$ Boolean matrices.
    Let $t_0$ be the transient length and $p \geq 1$ be the period, such that $M^{t_0} = M^{t_0+p}$.
    The number of distinct matrices in the sequence $\{M^k\}_{k\ge 0}$ is $T = t_0+p$.

    Consider the trajectory of a set $A_0$: $A_k = f^k(A_0)$.
    Since $M^{t_0} = M^{t_0+p}$, we have:
    $v_{A_{t_0}} = v_{A_0} M^{t_0} = v_{A_0} M^{t_0+p} = v_{A_{t_0+p}}$.
    So, $A_{t_0} = A_{t_0+p}$. The trajectory of $A_0$ also enters a cycle starting at or before $t_0$, and the length of the cycle divides $p$.
    The total number of distinct sets in the trajectory of $A_0$ is at most $t_0+p = T$.

    Therefore, $M(f) \leq T$.

4.  **Bounds on Boolean Matrix Semigroups**
    $M(f)$ is bounded by the maximum possible value of $T$ over all $N \times N$ Boolean matrices $M$. Let $L(N)$ denote this maximum.
    $M(f) \leq L(N)$.

    The value $L(N)$ has been studied in the context of semigroup theory and automata theory. It is known that $L(N)$ behaves similarly to Landau's function $g(N)$ (the maximum order of a permutation in $S_N$). The asymptotic behavior is given by:
    $L(N) \sim e^{\sqrt{N \ln N}}$.

5.  **Calculation for N=120**
    We calculate this asymptotic bound for $N=120$.
    $\ln(120) \approx 4.7875$.
    $N \ln N \approx 120 \times 4.7

[Note: response truncated to first 3000 characters of 3776]
