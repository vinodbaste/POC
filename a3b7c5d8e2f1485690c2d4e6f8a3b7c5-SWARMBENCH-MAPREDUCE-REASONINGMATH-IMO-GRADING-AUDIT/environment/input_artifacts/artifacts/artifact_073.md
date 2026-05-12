# artifact_073

Grading ID: GB-0979  
Problem ID: PB-Advanced-030  
Source: USAMO 2025  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $m$ and $n$ be positive integers with $m\ge n$. There are
 $m$ cupcakes of different flavors arranged around a circle and $n$
 people who like cupcakes. Each person assigns a non-negative real
 number score to each cupcake, depending on how much they like the
 cupcake. Suppose that for each person $P$, it is possible to partition
 the circle of $m$ cupcakes into $n$ groups of consecutive cupcakes
 so that the sum of $P$'s scores of the cupcakes in each group is
 at least $1$. Prove that it is possible to distribute the $m$ cupcakes
 to the $n$ people so that each person $P$ receives cupcakes of total
 score at least $1$ with respect to $P$.

## Reference Solution (for grader's calibration)

Arbitrarily pick any one person - call her Pip - and her $n$ arcs.
 The initial idea is to try to apply Hall's marriage lemma to match
 the $n$ people with Pip's arcs (such that each such person is happy
 with their matched arc). To that end, construct the obvious bipartite
 graph $\mathfrak{G}$ between the people and the arcs for Pip.

 We now consider the following algorithm, which takes several steps.
 \begin{itemize}
 \item If a perfect matching of $\mathfrak{G}$ exists, we're done!
 \item We're probably not that lucky. Per Hall's condition, this means there
 is a bad set $\mathcal{B}_{1}$ of people, who are compatible with
 fewer than $\left|\mathcal{B}_{1}\right|$ of the arcs. Then delete
 $\mathcal{B}_{1}$ and the neighbors of $\mathcal{B}_{1}$, then try
 to find a matching on the remaining graph.
 \item If a matching exists now, terminate the algorithm. Otherwise, that
 means there's another bad set $\mathcal{B}_{2}$ for the remaining
 graph. We again delete $\mathcal{B}_{2}$ and the fewer than $\mathcal{B}_{2}$
 neighbors.
 \item Repeat until some perfect matching $\mathcal{M}$ is possible in the
 remaining graph, i.e. there are no more bad sets (and then terminate
 once that occurs).
 \end{itemize}
 Since Pip is a universal vertex, it's impossible to delete Pip, so
 the algorithm does indeed terminate with nonempty $\mathcal{M}$.

 We commit to assigning each of person in $\mathcal{M}$ their matched
 arc (in particular if there are no bad sets at all, the problem is
 already solved). Now we finish the problem by induction on $n$ (for
 the remaining people) by simply deleting the arcs used up by $\mathcal{M}$.

 To see why this deletion-induction works, consider any particular
 person Quinn not in $\mathcal{M}$. By definition, Quinn is not happy
 with any of the $\operatorname{arcs}$ in $\mathcal{M}$. So when
 an $\operatorname{arc}\mathcal{A}$ of $\mathcal{M}$ is deleted,
 it had value less than 1 for Quinn so in particular it couldn't contain
 entirely any of Quinn's arcs. Hence at most one endpoint among Quinn's
 arcs was in the deleted $\operatorname{arc}\mathcal{A}$. When this
 happens, this causes two arcs of Quinn to merge, and the merged value
 is

 \[
 (\geq1)+(\geq1)-(\leq1)\quad\geq1
 \]

 meaning the induction is OK.

## Grading Guidelines

(Partial)
 1. Observed that when an arc with scores smaller than $1$ to some person $X$ is deleted, the problem condition still holds for $X$.
 2. Applied Hall's theorem to the arcs of a fixed person and the $n$ people.
(Almost)
 1. Found a perfect matching and uses induction, but didn't explain why the induction works.
 2. Full proof, but didn't mention that there exists a nonempty set that satisfies Hall's condition.

## Candidate Response (to be graded)

This problem can be solved by reformulating it in terms of graph theory, specifically concerning rainbow independent sets in circular arc graphs.

Let $C$ be the set of $m$ cupcakes arranged in a circle, and let $P_1, \dots, P_n$ be the $n$ people. Let $S_i(A)$ denote the score person $P_i$ assigns to a subset of cupcakes $A \subseteq C$.

The goal is to find a partition of $C$ into $A_1, \dots, A_n$ such that $S_i(A_i) \ge 1$ for all $i$.

**1. Reduction to Finding Disjoint Consecutive Blocks**

We will prove a stronger statement: it is possible to find $n$ pairwise disjoint sets of consecutive cupcakes (arcs) $B_1, \dots, B_n$ such that $S_i(B_i) \ge 1$ for all $i$.

If we find such blocks $B_1, \dots, B_n$, we can construct the desired distribution. Let $R = C \setminus \bigcup_{i=1}^n B_i$ be the set of remaining cupcakes. We define the distribution $A_1, \dots, A_n$ as follows:
$A_1 = B_1 \cup R$, and $A_i = B_i$ for $i=2, \dots, n$.
This is a partition of $C$. Since the scores are non-negative, $S_i(A_i) \ge S_i(B_i) \ge 1$ for all $i$.

**2. Formulation as a Graph Problem**

Let $\mathcal{F}$ be the family of all possible groups of consecutive cupcakes (arcs).
For each person $P_i$, we define the family of sufficient blocks $\mathcal{F}_i \subseteq \mathcal{F}$:
$$ \mathcal{F}_i = \{B \in \mathcal{F} \mid S_i(B) \ge 1\} $$
We are looking for a selection of blocks $B_1, \dots, B_n$ such that $B_i \in \mathcal{F}_i$ for all $i$, and the blocks are pairwise disjoint. This is known as a System of Disjoint Representatives (SDR) for the families $(\mathcal{F}_1, \dots, \mathcal{F}_n)$.

We construct the intersection graph $G$ of the family $\mathcal{F}$. The vertices of $G$ are the blocks in $\mathcal{F}$. Two vertices are connected by an edge if the corresponding blocks intersect (share at least one cupcake). Since $\mathcal{F}$ consists of arcs on a circle, $G$ is a circular arc graph.

A set of pairwise disjoint blocks corresponds to an independent set in $G$ (a set of vertices where no two are connected by an edge). The SDR we are looking for corresponds to an independent set $\{B_1, \dots, B_n\}$ such that $B_i \in \mathcal{F}_i$. This is called a rainbow independent set with respect to the families $\mathcal{F}_1, \dots, \mathcal{F}_n$.

**3. Analyzing the Hypothesis**

The hypothesis states that for each person $P_i$, it is possible to partition the circle of cupcakes into $n$ consecutive groups $\{G_{i,1}, \dots, G_{i,n}\}$ such that $S_i(G_{i,j}) \ge 1$ for all $j$.

This means that $G_{i,j} \in \mathcal{F}_i$ for all $j$. Since these groups form a partition, they are pairwise disjoint.
In the graph $G$, the set $\{G_{i,1}, \dots, G_{i,n}\}$ forms an independent set of size $n$. Furthermore, all these vertices belong to the subset $\mathcal{F}_i$.

Let $G[\mathcal{F}_i]$ be the subgraph of $G$ induced by the vertices $\mathcal{F}_i$. The independence number $\alpha(H)$ of a graph $H$ is the size of the largest independent set in $H$. Th

[Note: response truncated to first 3000 characters of 4486]
