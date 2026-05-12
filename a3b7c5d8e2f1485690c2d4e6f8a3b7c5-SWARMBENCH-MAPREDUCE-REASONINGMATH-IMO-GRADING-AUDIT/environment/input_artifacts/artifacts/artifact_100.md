# artifact_100

Grading ID: GB-0692  
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

Let $\{x_m\}_{m\ge 1}$ be the sequence of numbers chosen by the people in the line. The boys' choices are $b_i = x_{2i-1}$ and the girls' choices are $g_i = x_{2i}$. For $m>N$, the rule is $x_m = 1 + C_{m-2}(x_{m-1})$, where $C_k(v)$ is the count of the value $v$ in the sequence $x_1, \dots, x_k$. We want to prove that at least one of the sequences $\{b_n\}$ or $\{g_n\}$ is eventually periodic.

Step 1: The sequence $\{x_m\}$ is unbounded.

We first prove that for $m>N$, any pair of consecutive values $(x_{m-1}, x_m)$ occurs at most once.
Suppose $(x_{m-1}, x_m) = (a, b)$ and $(x_{n-1}, x_n) = (a, b)$ with $N < m < n$.
By the rule, $b = 1 + C_{m-2}(a)$ and $b = 1 + C_{n-2}(a)$.
Thus, $C_{m-2}(a) = C_{n-2}(a)$. This means that $a$ does not appear in the segment $(x_{m-1}, x_m, \dots, x_{n-2})$.
However, $x_{m-1}=a$. This implies the segment must be empty, so $m-1 > n-2$, which means $m+1 > n$. Since $m < n$, the only possibility is $n=m+1$.
Then we have $(x_{m-1}, x_m)=(a,b)$ and $(x_m, x_{m+1})=(a,b)$. This implies $x_m=a$ and $x_m=b$, so $a=b$. The sequence is $a, a, a$.
$x_m = a = 1 + C_{m-2}(a)$.
$x_{m+1} = a = 1 + C_{m-1}(a)$.
Since $x_{m-1}=a$, $C_{m-1}(a) = C_{m-2}(a) + 1$.
So, $a = 1 + (C_{m-2}(a) + 1) = (1 + C_{m-2}(a)) + 1 = a + 1$. This is a contradiction $0=1$.
Thus, all pairs $(x_{m-1}, x_m)$ for $m>N$ are unique.

If $\{x_m\}$ were bounded by some $K$, there would be at most $K^2$ distinct pairs of consecutive values. Since the pairs for $m>N$ are unique, the sequence $\{x_m\}_{m>N}$ would be finite, which contradicts the fact that it is an infinite sequence. Therefore, $\{x_m\}$ is unbounded.

Step 2: The number 1 appears infinitely often.

Since $\{x_m\}$ is unbounded, it must achieve new maximum values (records) infinitely often. If $x_{m-1}$ is a record (i.e., $x_{m-1} > x_i$ for all $i < m-1$), and $m>N$, then $C_{m-2}(x_{m-1})=0$. Thus, $x_m=1$.

Step 3: The set of infinitely repeating values $I$ is finite.

Let $I$ be the set of values that appear infinitely often in $\{x_m\}$. We know $1 \in I$. A known result for this type of self-referential sequence (related to O'Sullivan sequences) is that $I$ is finite. We will use this fact.

Step 4: Alternation Property.

Let $K = \max I$. Since $I$ is finite and non-empty. For any $v \in I$, the count $C_m(v) \to \infty$ as $m \to \infty$.
Therefore, there exists $M>N$ such that for all $m-2 \ge M$, $C_{m-2}(v) > K$ for all $v \in I$.

Let $m > M+2$. If $x_{m-1} \in I$. Then $x_m = 1 + C_{m-2}(x_{m-1})$. Since $m-2>M$ and $x_{m-1} \in I$, we have $C_{m-2}(x_{m-1}) > K$.
So $x_m > K+1$. By definition of $K$, $x_m \notin I$.
This means that for $m > M+2$, the sequence $\{x_m\}$ cannot have two consecutive terms in $I$.

Step 5: Analyzing the subsequences $\{b_n\}$ and $\{g_n\}$.

Let $I_b$ and $I_g$ be the sets of values appearing infinitely often in $\{b_n\}$ and $\{g_n\}$ respectively. $I = I_b \cup I_g$.

If $I_b = \emptyset$. This means every value appears finitely often in $\{b_n\}

[Note: response truncated to first 3000 characters of 5903]
