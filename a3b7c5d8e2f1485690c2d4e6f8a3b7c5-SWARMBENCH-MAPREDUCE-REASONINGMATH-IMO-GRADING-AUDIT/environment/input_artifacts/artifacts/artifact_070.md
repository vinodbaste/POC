# artifact_070

Grading ID: GB-0758  
Problem ID: PB-Advanced-023  
Source: (Modified) IMO 2024 P5  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

On a table of size $3002\times3001$, a stone is placed on the leftmost cell of the first row. James and Peter play a game on this table. Peter selects $3000$ cells, under the rule that he must choose one from each row except the first and last rows (i.e., the $1$st and $3002$th row), and there must be at most one selected cell in each column. James knows this rule too, but he doesn't know which cells Peter selected. The goal of James is to move the stone to the last row, avoiding the cells selected by Peter. The stone can only move to adjacent cells on the table. If the stone enters a cell selected by Peter, James receives a penalty of 1 point, and the stone returns to its initial position (i.e., the leftmost cell). Find the smallest positive integer $n$ such that there exists a method for James to achieve his goal before receiving a penalty of $n$ points.

## Reference Solution (for grader's calibration)

First we demonstrate that there is no winning strategy if James has
 2 attempts.


 Suppose that $(2,i)$ is the first cell in the second row that James
 reaches on his first attempt. Peter could have selected this cell,
 in which case James receives a penalty and returns to the initial
 position, and he cannot have reached any other cells past the first
 row.


 Next, suppose that $(3,j)$ is the first cell in the third row that
 James reaches on his second attempt. James must have moved to this
 cell from $(2,j)$, so we know $j\neq i$. So it is possible that
 Peter selected the cell $(3,j)$, in which case James also receives
 a penalty and returns to the initial position on his second attempt.
 Therefore James cannot guarantee to reach the last row in 2 attempts.


 Next, we exhibit a strategy for $n=3$. On the first attempt, James
 travels along the path

 \[
 (1,1)\rightarrow(2,1)\rightarrow(2,2)\rightarrow\cdots\rightarrow(2,3001).
 \]

 This path meets every cell in the second row, so James will find the
 selected cell in row 2, receive a penalty, and return to the initial
 position.


 If the selected cell in the second row is not on the edge of the board
 (that is, it is in cell $(2,i)$ with $2\leq i\leq3000$ ), then James
 takes the following two paths in his second and third attempts:

 \[
 \begin{aligned} & (1,1)\rightarrow\dots\rightarrow(1,i-1)\rightarrow(2,i-1)\rightarrow(3,i-1)\rightarrow(3,i)\rightarrow(4,i)\rightarrow\cdots\rightarrow(3002,i).

  & (1,1)\rightarrow\dots\rightarrow(1,i+1)\rightarrow(2,i+1)\rightarrow(3,i+1)\rightarrow(3,i)\rightarrow(4,i)\rightarrow\cdots\rightarrow(3002,i).
 \end{aligned}
 \]

 The only cells that Peter might have selected in either of these paths
 are $(3,i-1)$ and $(3,i+1)$. At most one of these can have been
 selected by Peter, so at least one of the two paths will be successful.
 James starts each path from the initial position $(1,1)$, but he
 knows where the selected cell in row 2 is, so he can navigate to $(1,i-1)$
 or $(1,i+1)$ directly.


 If the selected cell in the second row is on the edge of the board,
 without loss of generality we may assume it is in $(2,1)$. Then,
 on the second attempt, James takes the following path:

 \[
 (1,1)\rightarrow(1,2)\rightarrow(2,2)\rightarrow(2,3)\rightarrow(3,3)\rightarrow\cdots\rightarrow(3000,3001)\rightarrow(3001,3001)\rightarrow(3002,3001).
 \]

 If none of the cells on this path were selected by Peter, then James
 wins. Otherwise, let $(i,j)$ be the first cell on which James encounters
 a selected cell. We have that $j=i$ or $j=i+1$. Then, on the third
 attempt, James takes the following path:

 \[
 \begin{aligned}(1,1)\rightarrow\dots\rightarrow(1,2) & \rightarrow(2,2)\rightarrow(2,3)\rightarrow(3,3)\rightarrow\cdots\rightarrow(i-2,i-1)\rightarrow(i-1,i-1)

  & \rightarrow(i,i-1)\rightarrow(i,i-2)\rightarrow\cdots\rightarrow(i,2)\rightarrow(i,1)

  & \rightarrow(i+1,1)\rightarrow\cdots\rightarrow(3001,1)\rightarrow(3002,1).
 \end{aligned}
 \]

 Now note that:
 \begin{itemize}
 \item The cells from $(1,2)$ to $(i-1,i-1)$ were not selected because
 they were reached earlier than $(i,j)$ on the previous attempt.
 \item The cells $(i,k)$ for $1\leq k\leq i-1$ were not selected because
 there is only one selected cell in row $i$, and it lies in $(i,i)$
 or $(i,i+1)$.
 \item The cells $(k,1)$ for $i\leq k\leq3002$ were not selected because
 Peter selected at most one cell in column 1 (since there is one selected
 cell per row from 2 to 3001), and it lies in $(2,1)$.
 \end{itemize}
 Therefore James will win on the third attempt. Therefore, the smallest
 positive integer $n$ is $3$.

## Grading Guidelines

(Partial)
 1. Proved that the answer is at least $3$.
 2. Solved the case where the stone in the second row is not on the edge.
(Almost)
 1. Solved the case where the stone in the second row is on the edge.
 2. Solution is almost complete, but made minor mistakes which are not negligible.

## Candidate Response (to be graded)

The problem asks for the smallest integer $n$ such that James can guarantee reaching the last row before receiving $n$ penalties. This is equivalent to finding the maximum number of penalties James might receive in the worst case, assuming he plays optimally, let this be $H$. Then $n=H+1$.

The table has $R=3002$ rows and $C=3001$ columns. Let $N=3000$. There are $N$ intermediate rows $R_I=\{2, \dots, N+1\}$. Peter places $N$ stones, one in each row of $R_I$, and in distinct columns. This means there is exactly one free column $c^*$.

We want to find the minimax value $H = \min_S \max_P H(S, P)$, where $S$ is James' strategy and $P$ is Peter's configuration of stones.

1. Upper bound on $H$.
James can adopt the sequential probing strategy $S_{seq}$. He tries the columns one by one.
$S_{seq}$: For $c=1$ to $N+1$: Try the path $Path(c)$ (from $(1,1)$ to $(1,c)$, then straight down to $(R,c)$). If a penalty is received, proceed to the next column.

If James receives a penalty when probing column $c$, he learns that $c$ is blocked, so $c^* \ne c$.
In the worst case, the first $N$ columns he tries (say $C_1, \dots, C_N$) are blocked. This results in $N$ penalties. At this point, James knows that the only remaining column, $C_{N+1}$, must be the free column $c^*$. He can then take $Path(N+1)$ and win.
Thus, $H \le N$. $H \le 3000$.

2. Lower bound on $H$.
We want to show that $H \ge N$. This means for any strategy $S$ James employs, Peter has a choice of configuration $P$ that forces at least $N$ penalties.

Let's analyze the knowledge James has. Let $K$ be the set of known stones (revealed by penalties). Let $k=|K|$. James can guarantee a win in the next step if there is a path from R1 to RR that is guaranteed to be safe regardless of the placement of the remaining $N-k$ stones. This safe region is denoted by $G_S(K)$. If $G_S(K)$ connects R1 and RR, James wins.

If $G_S(K)$ is disconnected, James must take a risk by entering the danger zone $D(K)$ (cells where the remaining stones might be). If he enters $D(K)$, Peter might have placed a stone there.

We show that there exists a configuration of $k$ stones $K_k$ such that $G_S(K_k)$ is disconnected, for any $k < N$.

Consider the diagonal configuration $K^*_k = \{(i+1, i) \mid i=1, \dots, k\}$.
The rows involved are $R_K=\{2, \dots, k+1\}$. The columns involved are $C_K=\{1, \dots, k\}$.
The remaining rows are $R_U=\{k+2, \dots, N+1\}$. The remaining columns are $C_U=\{k+1, \dots, N+1\}$.
The danger zone is $D_k = R_U \times C_U$.

We analyze the connectivity of $G_S(K^*_k)$. Let $C_1$ be the component connected to R1.
We claim that for any cell $(r, c) \in C_1$ with $r \in R_K$, we must have $c \ge r$.
We prove this by induction on the row index $r$.
Base case: $r=2$. The stone is at $(2, 1)$. R1 connects to R2 at safe cells. So $c \ge 2$.
Inductive step: Assume it holds up to $r-1$. Let $C_1(r-1)$ be the reachable cells in row $r-1$. By hypothesis, if $r-1 \in R_K$, $C_1(r-1) \subseteq \{r-1, \dots

[Note: response truncated to first 3000 characters of 6022]
