# artifact_119

Grading ID: GB-0707  
Problem ID: PB-Advanced-021  
Source: (Modified) IMO 2024 P3  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Infinitely many boys and girls stand in a line alternatingly. For
 a given positive integer $N$, they choose positive integers according
 to the following rules:

 (1) The first $N$ people in the line choose any positive integers
 they want.

 (2) For each $m>N$, the $m$-th person chooses the number that is
 one more than the number of appearances of the number chosen by the
 $(m-1)$-th person appears among the numbers chosen by the first $m-2$
 people.

 Let $b_{i}$ be the number chosen by the $i$-th boy, and $g_{i}$
 be the number chosen by the $i$-th girl. Prove that at least one
 of the following holds:

 (i) There exists a sufficiently large integer $M$ such that $\{b_{n}\}_{n\ge M}$
 is a periodic sequence.

 (ii) There exists a sufficiently large integer $M$ such that $\{g_{n}\}_{n\ge M}$
 is a periodic sequence.

## Reference Solution (for grader's calibration)

Let $N$ be the given positive integer. Let $s_{m}$ be the number
 chosen by the $m$-th person in the line. For $m\ge N+1$, $s_{m}$
 is one more than the number of appearances of $s_{m-1}$ in the sequence
 $s_{1},s_{2},\dots,s_{m-2}$. Let $b_{i}=s_{2i-1}$ be the number
 chosen by the $i$-th boy, and $g_{i}=s_{2i}$ be the number chosen
 by the $i$-th girl. We want to show that at least one of the sequences
 $\{b_{n}\}_{n\ge M}$ or $\{g_{n}\}_{n\ge M}$ is periodic for some
 sufficiently large integer $M$.


 Let $M>\max\left(s_{1},\ldots,s_{2N}\right)$. We first prove that
 some integer appears infinitely many times. If not, then the sequence
 contains arbitrarily large integers. The first time each integer larger
 than $M$ appears, it is followed by a 1 . So 1 appears infinitely
 many times, which is a contradiction.


 Now we prove that every integer $x\geq M$ appears at most $M-1$
 times. If not, consider the first time that any $x\geq M$ appears
 for the $M^{\text{th }}$ time. Up to this point, each appearance
 of $x$ is preceded by an integer which has appeared $x\geq M$ times.
 So there must have been at least $M$ numbers that have already appeared
 at least $M$ times before $x$ does, which is a contradiction.


 Thus there are only finitely many numbers that appear infinitely many
 times. Let the largest of these be $k$. Since $k$ appears infinitely
 many times there must be infinitely many integers greater than $M$
 which appear at least $k$ times in the sequence, so each integer
 $1,2,\ldots,k-1$ also appears infinitely many times. Since $k+1$
 doesn't appear infinitely often there must only be finitely many numbers
 which appear more than $k$ times. Let the largest such number be
 $l\geq k$. From here on we call an integer $x$ big if $x>l$, medium
 if $l\geq x>k$ and small if $x\leq k$. To summarise, each small
 number appears infinitely many times in the sequence, while each big
 number appears at most $k$ times in the sequence.


 Choose a large enough $N^{\prime}>2N$ such that $s_{N^{\prime}}$
 is small, and in $s_{1},\ldots,s_{N^{\prime}}$ :
 \begin{enumerate}
 \item every medium number has already made all of its appearances;
 \item every small number has made more than $\max(k,N)$ appearances.
 \end{enumerate}
 Since every small number has appeared more than $k$ times, past this
 point each small number must be followed by a big number. Also, by
 definition each big number appears at most $k$ times, so it must
 be followed by a small number. Hence the sequence alternates between
 big and small numbers after $s_{N^{\prime}}$.


 \textbf{Lemma 1. }Let $g$ be a big number that appears after $s_{N^{\prime}}$.
 If $g$ is followed by the small number $h$, then $h$ equals the
 amount of small numbers which have appeared at least $g$ times before
 that point.


 \emph{Proof. }By the definition of $N^{\prime}$, the small number
 immediately preceding $g$ has appeared more than $\max(k,2N)$ times,
 so $g>\max(k,2N)$. And since $g>2N$, the $g^{\text{th }}$ appearance
 of every small number must occur after $s_{2N}$ and hence is followed
 by $g$. Since there are $k$ small numbers and $g$ appears at most
 $k$ times, $g$ must appear exactly $k$ times, always following
 a small number after $s_{2N}$. Hence on the $h^{\text{th }}$ appearance
 of $g$, exactly $h$ small numbers have appeared at least $g$ times
 before that point.


 Denote by $s_{[i,j]}$ the subsequence $s_{i},s_{i+1},\ldots,s_{j}$.


 \textbf{Lemma 2. }Suppose that $i$ and $j$ satisfy the following
 conditions:

 (a) $j>i>N^{\prime}+2$,

 (b) $s_{i}$ is small and $s_{i}=s_{j}$,

 (c) no small value appears more than once in $s_{[i,j-1]}$.

 Then $s_{i-2}$ is equal to some small number in $s_{[i,j-1]}$.


 \emph{Proof. }Let $\mathcal{I}$ be the set of small numbers that
 appear at least $s_{i-1}$ times in $s_{[1,i-1]}$. By Lemma 1, $s_{i}=|\mathcal{I}|$.
 Similarly, let $\mathcal{J}$ be the set of small numbers that appear
 at least $s_{j-1}$ times in $s_{[1,j-1]}$. Then by Lemma $1,s_{j}=|\mathcal{J}|$
 and hence by (b), $|\mathcal{I}|=|\mathcal{J}|$. Also by definition,
 $s_{i-2}\in\mathcal{I}$ and $s_{j-2}\in\mathcal{J}$.


 Suppose the small number $s_{j-2}$ is not in $\mathcal{I}$. This
 means $s_{j-2}$ has appeared less than $s_{i-1}$ times in $s_{[1,i-1]}$.
 By (c), $s_{j-2}$ has appeared at most $s_{i-1}$ times in $s_{[1,j-1]}$,
 hence $s_{j-1}\leq s_{i-1}$. Combining with $s_{[1,i-1]}\subset s_{[1,j-1]}$,
 this implies $\mathcal{I}\subseteq\mathcal{J}$. But since $s_{j-2}\in\mathcal{J}\backslash\mathcal{I}$,
 this contradicts $|\mathcal{I}|=|\mathcal{J}|$. So $s_{j-2}\in\mathcal{I}$,
 which means it has appeared at least $s_{i-1}$ times in $s_{[1,i-1]}$
 and one more time in $s_{[i,j-1]}$. Therefore $s_{j-1}>s_{i-1}$.


 By (c), any small number appearing at least $s_{j-1}$ times in $s_{[1,j-1]}$
 has also appeared $s_{j-1}-1\geq$ $s_{i-1}$ times in $s_{[1,i-1]}$.
 So $\mathcal{J}\subseteq\mathcal{I}$ and hence $\mathcal{I}=\mathcal{J}$.
 Therefore, $s_{i-2}\in\mathcal{J}$, so it must appear at least $s_{j-1}-s_{i-1}=1$
 more time in $s_{[i,j-1]}$.


 For each small number $s_{n}$ with $n>N^{\prime}+2$, let $p_{n}$
 be the smallest number such that $s_{n+p_{n}}=s_{i}$ is also small
 for some $i$ with $n\leq i<n+p_{n}$. In other words, $s_{n+p_{n}}=s_{i}$
 is the first small number to occur twice after $s_{n-1}$. If $i>n$,
 Lemma 2 (with $j=n+p_{n}$ ) implies that $s_{i-2}$ appears again
 before $s_{n+p_{n}}$, contradicting the minimality of $p_{n}$. So
 $i=n$. Lemma 2 also implies that $p_{n}\geq p_{n-2}$. So $p_{n},p_{n+2},p_{n+4},\ldots$
 is a nondecreasing sequence bounded above by $2k$ (as there are only
 $k$ small numbers). Therefore, $p_{n},p_{n+2},p_{n+4},\ldots$ is
 eventually constant and the subsequence of small numbers is eventually
 periodic with period at most $k$.

## Grading Guidelines

(Partial)
 1. Proved that there are only finitely many integers that appear infinitely many times in $\{b_{n}\}\cup\{g_{n}\}$.
 2. Came up with multiple observations that may lead to the proof, but failed to rigorously combine them.
(Almost)
 1. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

This problem is a known result related to sequences defined by frequency counting with a delay (specifically, IMO Shortlist 2009 C6). The proof relies on analyzing the occurrences of the number 1 and utilizing a key property about the finiteness of other generated values.

Let $\{x_m\}_{m\ge 1}$ be the sequence of numbers chosen by the people. The boys' choices are $b_n = x_{2n-1}$ and the girls' choices are $g_n = x_{2n}$.
Let $C_k(v)$ denote the count of the value $v$ in the sequence $x_1, \dots, x_k$.
The rule for $m>N$ is $x_m = 1 + C_{m-2}(x_{m-1})$.

**Step 1: The sequence $\{x_m\}$ is unbounded.**

Suppose, for contradiction, that $\{x_m\}$ is bounded. Since $x_m$ are positive integers, some value $v$ must appear infinitely often. Let $m_k$ be an infinite sequence of indices (with $m_k>N$) such that $x_{m_k-1}=v$.
Then $x_{m_k} = 1 + C_{m_k-2}(v)$.
As $k\to\infty$, $m_k\to\infty$. Since $v$ appears infinitely often, $C_{m_k-2}(v) \to \infty$.
Thus, $x_{m_k} \to \infty$. This contradicts the assumption that $\{x_m\}$ is bounded.

**Step 2: The value 1 appears infinitely often.**

Since $\{x_m\}$ is unbounded, there are infinitely many "record" values (a value strictly larger than all preceding values). Let $x_{m-1}$ be a record value, with $m>N$.
Then $x_{m-1}$ does not appear in $x_1, \dots, x_{m-2}$, so $C_{m-2}(x_{m-1})=0$.
By the rule, $x_m = 1 + C_{m-2}(x_{m-1}) = 1 + 0 = 1$.
Since there are infinitely many records, the value 1 appears infinitely often.

**Step 3: The Key Lemma (Finiteness of $V_{>1}$).**

Let $V_{>1}$ be the set of values generated when the previous term is greater than 1:
$V_{>1} = \{ x_m \mid m>N \text{ and } x_{m-1}>1 \}$.

**Lemma:** The set $V_{>1}$ is finite.

This is a known, non-trivial property of sequences generated by the rule $x_m = 1 + C_{m-2}(x_{m-1})$. It implies that large numbers in the sequence must be generated following an occurrence of 1.

Let $K_0$ be a constant defined as the maximum of the initial values and the values in $V_{>1}$:
$K_0 = \max(\{x_1, \dots, x_N\} \cup V_{>1} \cup \{1\})$.
By the Lemma, $K_0$ is finite.

**Step 4: Analyzing the occurrences of 1.**

Let $\{i_k\}_{k\ge 1}$ be the increasing sequence of indices where $x_{i_k}=1$. We know this sequence is infinite (Step 2).

Choose $J$ large enough such that $J > K_0$ and $i_J > N$.
For $k \ge J$, the rules apply to $x_{i_k+1}$ and $x_{i_k+2}$.

Consider $x_{i_k+1}$:
$x_{i_k+1} = 1 + C_{i_k-1}(x_{i_k}) = 1 + C_{i_k-1}(1)$.
$C_{i_k-1}(1)$ is the count of 1s before the $k$-th occurrence, which is exactly $k-1$.
So, $H_k = x_{i_k+1} = 1 + (k-1) = k$.

Consider $x_{i_k+2}$:
$x_{i_k+2} = 1 + C_{i_k}(x_{i_k+1}) = 1 + C_{i_k}(k)$.

**Step 5: Proving $k$ is a new value.**

We show that for $k \ge J$, the value $k$ has not appeared up to index $i_k$, i.e., $C_{i_k}(k)=0$.
Since $k \ge J > K_0$, we have $k>K_0$.

Suppose $C_{i_k}(k) > 0$. This means $x_j = k$ for some $j \le i_k$.

Case 1: $j \le N$.
$k = x_j \in \{x_1, \dots, x_N\}$. So $k \

[Note: response truncated to first 3000 characters of 4909]
