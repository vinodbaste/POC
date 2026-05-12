# artifact_079

Grading ID: GB-0987  
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

An elegant proof of this statement relies on a known result from combinatorial mathematics concerning measures on a circle. We will first state the theorem and then show how it directly applies to the problem of distributing cupcakes.

**The setup**

Let the cupcakes be $C_1, C_2, \dots, C_m$ arranged in a circle. Let the set of cupcakes be $M = \{C_1, \dots, C_m\}$. The people are $P_1, \dots, P_n$. The score of person $P_i$ for cupcake $C_j$ is $s_{ij} \ge 0$.

For each person $P_i$, we can define a measure $\mu_i$ on the set of cupcakes $M$. For any subset of cupcakes $A \subseteq M$, the measure is the sum of scores:
$$ \mu_i(A) := \sum_{C_j \in A} s_{ij} $$
The problem uses the term "groups of consecutive cupcakes", which, due to the circular arrangement, correspond to arcs.

**The given condition**

The problem states that for each person $P_i$, it is possible to partition the circle of $m$ cupcakes into $n$ arcs (groups of consecutive cupcakes) $A_{i,1}, A_{i,2}, \dots, A_{i,n}$ such that the sum of $P_i$'s scores for the cupcakes in each arc is at least 1.
In terms of our measures, this means that for each $i \in \{1, \dots, n\}$, there exists a partition of $M$ into $n$ arcs $A_{i,1}, \dots, A_{i,n}$ such that:
$$ \mu_i(A_{i,k}) \ge 1 \quad \text{for all } k \in \{1, \dots, n\} $$
A direct consequence of this condition is that the total score for each person $P_i$ is at least $n$. Let $T_i = \sum_{j=1}^m s_{ij}$ be the total score for $P_i$. Since $\{A_{i,1}, \dots, A_{i,n}\}$ is a partition of $M$, we have:
$$ T_i = \mu_i(M) = \sum_{k=1}^n \mu_i(A_{i,k}) \ge \sum_{k=1}^n 1 = n $$

**The goal**

We want to prove that it is possible to distribute the $m$ cupcakes to the $n$ people such that each person $P_i$ receives cupcakes of total score at least 1. A distribution is a partition of the set of cupcakes $M$ into $n$ disjoint subsets $X_1, X_2, \dots, X_n$, where $X_i$ is the set of cupcakes given to person $P_i$. The condition to be met is:
$$ \mu_i(X_i) \ge 1 \quad \text{for all } i \in \{1, \dots, n\} $$
Note that the sets $X_i$ are not required to be arcs.

**Applying a theorem**

The problem is a direct application of a theorem by W. Stromquist and D. R. Woodall concerning sets of measures on a circle. Although the theorem is often stated for continuous (nonatomic) measures, it holds for discrete (atomic) measures as well, which is our case. The measures $\mu_i$ are atomic, with atoms at the positions of the cupcakes.

The theorem can be stated as follows:

**Theorem (Stromquist-Woodall, 1985):** Let $\mu_1, \dots, \mu_n$ be $n$ non-negative measures on a circle $C$. Suppose that for each $i \in \{1, \dots, n\}$, there is a partition of $C$ into $n$ arcs $A_{i,1}, \dots, A_{i,n}$ such that $\mu_i(A_{i,k}) \ge 1$ for all $k \in \{1, \dots, n\}$. Then there exists a partition of $C$ into $n$ (not necessarily connected) measurable sets $X_1, \dots, X_n$ such that $\mu_i(X_i) \ge 1$ for all $i \in \{1, \dots, n\}$.

To apply this theorem

[Note: response truncated to first 3000 characters of 6501]
