# artifact_142

Grading ID: GB-0717  
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

**Complete Proof**

Let $\{x_m\}_{m\ge 1}$ be the sequence of chosen numbers. For $m>N$, $x_m = C_{m-1}(x_{m-1})$, where $C_k(v)$ is the count of $v$ in $x_1, \dots, x_k$. We have $b_n = x_{2n-1}$ and $g_n = x_{2n}$.

**Part A: At Least One Sequence is Bounded**

1. **Unboundedness:** The sequence $\{x_m\}$ is unbounded. If it were bounded, some value $v$ appears infinitely often at indices $m_i$. Then $x_{m_i+1} = C_{m_i}(v) = i$ (for large $i$), which is unbounded, a contradiction.

2. **Finiteness of Infinite Values ($V_\infty$):** Let $V_\infty$ be the set of values appearing infinitely often in $\{x_m\}$. If $V_\infty$ were infinite, then every integer $k \ge 1$ would appear infinitely often, so $V_\infty = \mathbb{Z}^+$.
If $V_\infty = \mathbb{Z}^+$, fix $K \ge 1$. Since $C_m(v) \to \infty$ for $v \in \{1, \dots, K\}$, there exists $M_K$ such that for $m > M_K$, $C_{m-1}(v) > K$ for all $v \in \{1, \dots, K\}$.
For $m > M_K$:
If $x_{m-1} \le K$, then $x_m = C_{m-1}(x_{m-1}) > K$.
If $x_m \le K$, then $C_{m-1}(x_{m-1}) \le K$, so $x_{m-1} > K$.
Thus, $\{x_m\}_{m>M_K}$ alternates between being $\le K$ and $> K$. One of $\{b_n\}$ or $\{g_n\}$ is eventually bounded by $K$.
If $\{b_n\}$ is bounded, let $v$ be a value appearing infinitely often in $\{g_n\}$ at indices $n_i$. Then $b_{n_i+1} = C_{2n_i}(v) \ge i$, so $\{b_n\}$ is unbounded, a contradiction. Thus, $\{g_n\}$ has no infinitely recurring values. $V_\infty$ is contained in the bounded set of values of $\{b_n\}$, so $V_\infty$ is finite. This contradicts $V_\infty = \mathbb{Z}^+$.
Therefore, $V_\infty$ is finite.

3. **Boundedness of Transient Counts:** Let $K = \max V_\infty$. Let $V_f = \mathbb{Z}^+ \setminus V_\infty$. For $v \in V_f$, let $R(v)$ be its total count. If $\sup_{v \in V_f} R(v)$ were infinite, there would be infinitely many $v \in V_f$ such that $R(v) > K+1$. Each such $v$ generates an occurrence of $K+1$. Thus $K+1$ appears infinitely often, $K+1 \in V_\infty$, contradicting $K = \max V_\infty$.
Thus $T_{max} = \sup_{v \in V_f} R(v)$ is finite.

4. **Establishing Boundedness:** Let $B^* = \max(K, 1+T_{max})$.
If $x_m > B^*$ (for $m>N$), then $x_m \in V_f$. $x_{m+1} = C_m(x_m) \le R(x_m) \le T_{max} < B^*$. No two consecutive terms exceed $B^*$.

Let $I_0 = \{n : b_n \le B^* \text{ and } g_n \le B^*\}$.
Choose $M_1$ large enough such that for $m \ge M_1$, if $x_{m-1} \in V_\infty$, then $x_m = C_{m-1}(x_{m-1}) > B^*$.
If $n \in I_0$ is large ($2n-2 \ge M_1$), then $b_n \le B^*$ implies $g_{n-1} \notin V_\infty$, and $g_n \le B^*$ implies $b_n \notin V_\infty$.
So, for large $n \in I_0$, $b_n$ and $g_n$ belong to $V_f^{\le B^*} = \{v \in V_f : v \le B^*\}$. Since $V_f^{\le B^*}$ is finite and its elements appear finitely often, $I_0$ must be finite.

Let $M$ be such that $n \ge M \implies n \notin I_0$. For $n \ge M$, $b_n > B^*$ or $g_n > B^*$. Since they cannot both be $> B^*$, exactly one is $> B^*$.

If $g_{M} > B^*$, then $b_{M+1} \le B^*$. Since $M+1 \notin I_0$, $g

[Note: response truncated to first 3000 characters of 5721]
