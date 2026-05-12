# artifact_075

Grading ID: GB-0993  
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

We want to prove that it is possible to distribute the $m$ cupcakes to the $n$ people so that each person $P$ receives cupcakes of total score at least $1$ with respect to $P$.

Let $C$ be the set of $m$ cupcakes. Let $\mathcal{P}=\{P_1, \dots, P_n\}$ be the set of $n$ people. Let $S_i(A)$ denote the non-negative real score assigned by person $P_i$ to a subset of cupcakes $A \subseteq C$.

The hypothesis states that for each person $P_i$, there exists a partition of $C$ into $n$ groups of consecutive cupcakes, $\mathcal{G}_i = \{G_{i,1}, \dots, G_{i,n}\}$, such that $S_i(G_{i,j}) \ge 1$ for all $j=1, \dots, n$. The fact that the groups are consecutive around the circle ensures that they indeed form a partition (they are disjoint and their union is $C$).

We aim to find a partition of $C$ into $(A_1, \dots, A_n)$ such that $S_i(A_i) \ge 1$ for all $i$.

We will use the Aharoni-Haxell theorem on the existence of a System of Disjoint Representatives (SDR) for a collection of families of sets.

First, we define the family of satisfactory sets for each person $P_i$:
$$ \mathcal{F}_i = \{B \subseteq C : S_i(B) \ge 1\}. $$
We seek an SDR for the collection $(\mathcal{F}_1, \dots, \mathcal{F}_n)$. An SDR is a sequence of sets $(B_1, \dots, B_n)$ such that $B_i \in \mathcal{F}_i$ for all $i$, and the sets are pairwise disjoint ($B_i \cap B_j = \emptyset$ for $i \ne j$).

If we find such an SDR $(B_1, \dots, B_n)$, we can construct the desired distribution. Let $R = C \setminus \bigcup_{i=1}^n B_i$ be the set of remaining cupcakes. We define the allocation $(A_1, \dots, A_n)$ as follows:
$A_1 = B_1 \cup R$,
$A_i = B_i$ for $i=2, \dots, n$.
This forms a partition of $C$. Since the scores are non-negative, $S_i(A_i) \ge S_i(B_i)$. Since $B_i \in \mathcal{F}_i$, $S_i(B_i) \ge 1$. Thus, $S_i(A_i) \ge 1$ for all $i$.

Now we prove the existence of the SDR using the Aharoni-Haxell theorem.

**Theorem (Aharoni-Haxell, 2000).** A collection of families of sets $(\mathcal{F}_1, \dots, \mathcal{F}_n)$ has an SDR if and only if for every subset of indices $J \subseteq \{1, \dots, n\}$, the union of the corresponding families, $\mathcal{H}_J = \bigcup_{i \in J} \mathcal{F}_i$, contains a matching of size $|J|$. (A matching in $\mathcal{H}_J$ is a collection of pairwise disjoint sets belonging to $\mathcal{H}_J$).

We verify this condition. Let $J \subseteq \{1, \dots, n\}$ be an arbitrary subset of indices, and let $k = |J|$. We need to show that $\mathcal{H}_J$ contains a matching of size $k$.

If $k=0$ (i.e., $J=\emptyset$), the condition is satisfied by the empty matching.

If $k>0$, $J$ is non-empty. Choose an arbitrary index $i_0 \in J$.
By the hypothesis of the problem, for person $P_{i_0}$, there exists a partition of $C$ into $n$ consecutive groups, $\mathcal{G}_{i_0} = \{G_1, \dots, G_n\}$, such that $S_{i_0}(G_j) \ge 1$ for all $j=1, \dots, n$.

By the definition of $\mathcal{F}_{i_0}$, the condition $S_{i_0}(G_j) \ge 1$ implies that $G_j \in \mathcal{F}_{i_

[Note: response truncated to first 3000 characters of 3942]
