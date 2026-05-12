# artifact_108

Grading ID: GB-0062  
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

Let $S$ be the set of 120 students, so $|S|=120$. Let $F = \mathcal{P}(S)$ be the power set of $S$.
The 'love' relationship can be represented by a directed graph $G=(S, E)$, where an edge $(u,v) \in E$ means student $u$ loves student $v$. For each student $u \in S$, let $N(u) = \{v \in S \mid (u,v) \in E\}$ be the set of students loved by $u$.

The function $f: F \rightarrow F$ is defined for any $X \in F$ as
$$f(X) = \bigcup_{u \in X} N(u).$$
This definition implies that $f$ is a join-homomorphism on the lattice $(\mathcal{P}(S), \subseteq, \cup)$, because for any $X, Y \in F$:
$$f(X \cup Y) = \bigcup_{u \in X \cup Y} N(u) = \left(\bigcup_{u \in X} N(u)\right) \cup \left(\bigcup_{u \in Y} N(u)\right) = f(X) \cup f(Y).$$

Two sets $A, B \in F$ have a 'lovely relationship' if there exists a natural number $k$ such that $f^k(A) = B$ or $f^k(B) = A$. We assume natural numbers mean positive integers, so $k \ge 1$. The relationship is symmetric by definition.

We are given distinct elements $A_1, A_2, \dots, A_t \in F$ such that for any $1 \le i < j \le t$, $A_i$ and $A_j$ have a lovely relationship. Let $\mathcal{A}=\{A_1, \dots, A_t\}$.
Let's define a relation $\prec$ on $\mathcal{A}$ such that $A_i \prec A_j$ if there exists $k \ge 1$ with $f^k(A_i)=A_j$. The condition on $\mathcal{A}$ means that for any two distinct $A_i, A_j \in \mathcal{A}$, either $A_i \prec A_j$ or $A_j \prec A_i$. This turns $(\mathcal{A}, \prec)$ into a tournament.

Any tournament has a Hamiltonian path. This means we can reorder the elements of $\mathcal{A}$ to form a sequence, let's call it $B_1, B_2, \dots, B_t$, such that $B_1 \prec B_2 \prec \dots \prec B_t$.
This means that for each $i \in \{1, \dots, t-1\}$, there exists an integer $k_i \ge 1$ such that $B_{i+1} = f^{k_i}(B_i)$.
This implies that every $B_j$ for $j>1$ is an iterate of $B_1$:
$B_2 = f^{k_1}(B_1)$
$B_3 = f^{k_2}(B_2) = f^{k_2}(f^{k_1}(B_1)) = f^{k_1+k_2}(B_1)$
...
$B_j = f^{k_1+k_2+\dots+k_{j-1}}(B_1)$.
Since the sets $A_1, \dots, A_t$ are distinct, so are $B_1, \dots, B_t$. This implies that they are all distinct members of the trajectory of $f$ starting from $B_1$.
The trajectory of $f$ starting from a set $A$ is the sequence $A, f(A), f^2(A), \dots$.
The number of sets $t$ is therefore bounded by the maximum possible length of such a trajectory without repetition.
The problem asks for $M(f)$, the maximum possible value of $t$ for a given $f$. This is the length of the longest trajectory of $f$. We want to show that $M(f) \le 2^{70}$ for any function $f$ defined by a love graph. The maximum possible value of $M(f)$ over all possible love graphs must be bounded.

To analyze the trajectory of $f$, we can model the function $f$ using Boolean matrix multiplication. Let the students be indexed from 1 to $n=120$. A subset $X \subseteq S$ can be represented by a binary row vector $x \in \{0,1\}^n$, where $x_i=1$ if student $i$ is in $X$, and $x_i=0$ otherwise.
Let $M$ be the $n \times n$ adjacency matrix of

[Note: response truncated to first 3000 characters of 10055]
