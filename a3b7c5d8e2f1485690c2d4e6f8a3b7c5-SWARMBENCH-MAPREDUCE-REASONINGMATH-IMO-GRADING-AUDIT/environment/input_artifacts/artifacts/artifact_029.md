# artifact_029

Grading ID: GB-0051  
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

Let $S$ be the set of 120 students, and $F = \mathcal{P}(S)$ be the power set of $S$.
The function $f: F \rightarrow F$ is defined by $f(X) = \bigcup_{s \in X} L(s)$, where $L(s) \subseteq S$ is the set of students loved by student $s$.

A key property of $f$ is that it distributes over the union of sets. For any $X, Y \subseteq S$:
$$f(X \cup Y) = \bigcup_{s \in X \cup Y} L(s) = \left(\bigcup_{s \in X} L(s)\right) \cup \left(\bigcup_{s \in Y} L(s)\right) = f(X) \cup f(Y)$$
This also means $f$ is monotone: if $A \subseteq B$, then $f(A) \subseteq f(B)$. Also, note that $f(\emptyset) = \emptyset$.

The condition that distinct elements $A_1, \ldots, A_t$ from $F$ have a 'lovely relationship' for any pair means that for any $i \neq j$, either $A_j = f^k(A_i)$ or $A_i = f^k(A_j)$ for some natural number $k \ge 1$. This implies that the set $\{A_1, \ldots, A_t\}$ is totally ordered by the reachability relation of $f$. We can relabel these sets to form a chain $X_1, X_2, \ldots, X_t$ such that for any $1 \le i < j \le t$, $X_j = f^{k_{ij}}(X_i)$ for some $k_{ij} \ge 1$.

This chain of distinct sets must be part of a sequence of iterates of an initial set. Let $X_0$ be such that $X_1 = f^{k_0}(X_0)$ for some $k_0 \ge 0$. To maximize $t$, we can assume the sets are consecutive iterates, $X_k = f^k(X_0)$ for $k=0, \ldots, t-1$. Then $M(f)$ is the maximum possible number of distinct sets in such a sequence, maximized over all choices of $X_0 \in F$ and all possible functions $f$.

Let $Y_0 = f(S) = \bigcup_{s \in S} L(s)$. This is the set of all students who are loved by at least one student.
For any set $X \subseteq S$, its image $f(X) = \bigcup_{s \in X} L(s) \subseteq \bigcup_{s \in S} L(s) = Y_0$.
This means that for any sequence of iterates $X_0, X_1=f(X_0), X_2=f(X_1), \ldots$, all sets $X_k$ for $k \ge 1$ are subsets of $Y_0$.

We will prove the main result by considering two cases based on the size of $Y_0$.

**Case 1: $|Y_0| \le 70$.**
Let $\{A_1, \ldots, A_t\}$ be a set satisfying the problem's conditions. As argued, we can order it into a chain $X_1, \ldots, X_t$ where $X_{j} = f^{k_j}(X_i)$ for $i < j$.
For any $j \in \{2, \ldots, t\}$, we have $X_j = f^{k_{j-1}}(X_{j-1})$. Since $k_{j-1} \ge 1$, $X_j$ is in the image of $f$, which means $X_j \subseteq Y_0$.
So, the sets $X_2, X_3, \ldots, X_t$ are $t-1$ distinct subsets of $Y_0$.
The total number of subsets of $Y_0$ is $2^{|Y_0|}$. This gives a first bound $t-1 \le 2^{|Y_0|}$, so $t \le 2^{|Y_0|}+1$.

We can strengthen this bound. Suppose $\emptyset$ is one of these sets, say $X_j = \emptyset$ for some $j \in \{2, \ldots, t\}$.
If $j < t$, then the chain continues to $X_{j+1} = f^k(X_j)$ for some $k \ge 1$.
This gives $X_{j+1} = f^k(\emptyset) = \emptyset = X_j$. But the sets $X_1, \ldots, X_t$ must be distinct, which is a contradiction.
Therefore, if $\emptyset$ is part of the chain $\{X_2, \ldots, X_t\}$, it must be the last element, $X_t$.

So, the sets $X_2, \ldots, X_{t-1}$ are all non-em

[Note: response truncated to first 3000 characters of 9491]
