# artifact_126

Grading ID: GB-0991  
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

This problem is a known result in the field of discrete fair division. The statement is true, but the proof for the general case relies on advanced mathematical techniques. We will first provide an elementary proof for the case $n=2$, and then prove the general case by relying on a known theorem concerning balanced partitions of discrete sets.

Let $C$ be the set of $m$ cupcakes. Let $P_1, \dots, P_n$ be the $n$ people. Let $S_i(G)$ denote the score person $P_i$ assigns to a subset of cupcakes $G \subseteq C$.

The hypothesis states that for each person $P_i$, there exists a partition of $C$ into $n$ consecutive groups $G_{i,1}, \dots, G_{i,n}$ such that $S_i(G_{i,j}) \ge 1$ for all $j=1, \dots, n$.

An immediate consequence of the hypothesis is that the total score of all cupcakes for any person $P_i$ is at least $n$.
$T_i = S_i(C) = S_i(\bigcup_j G_{i,j}) = \sum_{j=1}^n S_i(G_{i,j}) \ge \sum_{j=1}^n 1 = n$.

We want to prove that there exists a distribution (a partition) $A_1, \dots, A_n$ of $C$ such that $S_i(A_i) \ge 1$ for all $i$.

### Proof for the case n=2

Let $n=2$. We have two people, $P_1$ and $P_2$.

By the hypothesis for $P_1$, there is a partition of the cupcakes $C$ into two consecutive groups $G_1$ and $G_2$ such that:
$S_1(G_1) \ge 1$ and $S_1(G_2) \ge 1$.

By the hypothesis for $P_2$, $P_2$ can also partition $C$ into two consecutive groups of score at least 1. This implies that the total score for $P_2$ is $T_2 = S_2(C) \ge 1+1=2$.

We look for a distribution $(A_1, A_2)$. We consider the partition $(G_1, G_2)$ defined by $P_1$.

Possibility 1: Assign $A_1 = G_1$ to $P_1$ and $A_2 = G_2$ to $P_2$.
We know $S_1(A_1) = S_1(G_1) \ge 1$. This assignment works if $S_2(A_2) = S_2(G_2) \ge 1$.

Possibility 2: Assign $A_1 = G_2$ to $P_1$ and $A_2 = G_1$ to $P_2$.
We know $S_1(A_1) = S_1(G_2) \ge 1$. This assignment works if $S_2(A_2) = S_2(G_1) \ge 1$.

Suppose neither possibility works. This means that:
$S_2(G_2) < 1$ (from Possibility 1 failing)
$S_2(G_1) < 1$ (from Possibility 2 failing)

Adding these two inequalities, we get:
$S_2(G_1) + S_2(G_2) < 1 + 1 = 2$.

Since $G_1$ and $G_2$ form a partition of $C$, the left side is the total score for $P_2$:
$T_2 = S_2(C) = S_2(G_1) + S_2(G_2)$.
So, we have $T_2 < 2$.

However, as established earlier, the hypothesis implies $T_2 \ge 2$.
This is a contradiction. Therefore, the assumption that neither possibility works must be false. At least one of the assignments (Possibility 1 or Possibility 2) provides a valid distribution where both $P_1$ and $P_2$ receive a score of at least 1.

### Proof for the general case (n > 2)

For the general case, the proof is significantly more complex and relies on advanced results in fair division theory. We will use a theorem by Wu, Zang, and Zhao (2013).

**Theorem (WZZ Theorem, 2013):**
Let $C$ be a finite set of items, and $S_1, \dots, S_n$ be $n$ non-negative additive score functions (measures) on $C$. If the total score $S_i(C) \ge n$ for all $i=1,\d

[Note: response truncated to first 3000 characters of 4320]
