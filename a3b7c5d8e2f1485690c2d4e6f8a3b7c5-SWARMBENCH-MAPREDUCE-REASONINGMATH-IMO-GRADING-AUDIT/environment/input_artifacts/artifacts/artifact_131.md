# artifact_131

Grading ID: GB-0998  
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

This problem is a known result in the field of fair division, proven by Noga Alon in 1997 (Theorem 2.1 in "Partitioning a cake"). The proof is non-trivial, relying on combinatorial arguments derived from topological methods. We will first establish the case for $n=2$ and then outline the proof strategy for the general case using induction, following Alon's approach.

Let $C$ be the set of $m$ cupcakes, and $\mathcal{P} = \{P_1, \dots, P_n\}$ be the set of $n$ people. Let $V_i(A)$ denote the score person $P_i$ assigns to a subset of cupcakes $A \subseteq C$.

The hypothesis states that for each person $P_i$, there exists a partition of $C$ into $n$ consecutive groups $G_{i,1}, \dots, G_{i,n}$ such that $V_i(G_{i,j}) \ge 1$ for all $j$.

An immediate consequence of the hypothesis is that the total score of all cupcakes for any person $P_i$ is $V_i(C) = \sum_{j=1}^n V_i(G_{i,j}) \ge n$.

We want to prove that there exists a distribution (a partition) $A_1, \dots, A_n$ of $C$ such that $V_i(A_i) \ge 1$ for all $i$.

### Proof for the case n=2

Let $n=2$. We have two people $P_1$ and $P_2$.
By the hypothesis, $P_1$ has a partition of the cupcakes into two consecutive groups, $A$ and $B$, such that $V_1(A) \ge 1$ and $V_1(B) \ge 1$.
Also, the hypothesis for $P_2$ implies that $V_2(C) \ge 2$.

We attempt to distribute $A$ and $B$ between $P_1$ and $P_2$. There are two possible assignments where $P_1$ receives a satisfactory share:

1. Assignment 1: $P_1$ receives $A$, $P_2$ receives $B$. ($V_1(A) \ge 1$).
2. Assignment 2: $P_1$ receives $B$, $P_2$ receives $A$. ($V_1(B) \ge 1$).

If Assignment 1 works, we must have $V_2(B) \ge 1$.
If Assignment 2 works, we must have $V_2(A) \ge 1$.

Suppose neither assignment is satisfactory for $P_2$. This means:
$V_2(B) < 1$ (from failure of Assignment 1)
$V_2(A) < 1$ (from failure of Assignment 2)

Since $(A, B)$ is a partition of $C$, the total score for $P_2$ is $V_2(C) = V_2(A) + V_2(B)$.
If both assignments fail, $V_2(C) < 1 + 1 = 2$.
This contradicts the fact that $V_2(C) \ge 2$.
Therefore, at least one of the assignments is satisfactory for both people.

### Proof Outline for the General Case (Induction)

We proceed by induction on $n$. The base case $n=1$ is trivial, and $n=2$ is proven above.
Assume the statement holds for $n-1$ people. We prove it for $n$ people.

The strategy is to find a "detachable pair" $(P_i, A)$, defined as follows:
1. $A$ is a consecutive block of cupcakes.
2. $V_i(A) \ge 1$.
3. For every other person $P_j$ ($j\ne i$), the remaining segment of cupcakes $C' = C \setminus A$ satisfies the hypothesis of the theorem for $n-1$ groups. That is, $P_j$ can partition $C'$ into $n-1$ consecutive groups, each of score at least 1 for $P_j$.

If we find such a detachable pair $(P_i, A)$, we assign $A$ to $P_i$. The remaining cupcakes $C'$ form a consecutive segment (since $C$ is a circle and $A$ is consecutive). The condition (3) ensures that the induction hypothesis applies to the $n-1$ remaining

[Note: response truncated to first 3000 characters of 5237]
