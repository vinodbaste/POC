# artifact_139

Grading ID: GB-0770  
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

Let $R=3002$ be the number of rows and $C=3001$ be the number of columns. Let $K=3000$. Peter places $K$ stones in the middle rows $R_{mid}=\{2, \dots, R-1\}$, one per row, and at most one per column. Since $C=K+1$, there is exactly one column $c^*$ with no stones, called the free column.

James starts at $(1,1)$ and wants to reach row $R$. Moves are to adjacent cells (4-connectivity). If James hits a stone, he gets a penalty and restarts at $(1,1)$. We want to find the smallest $n$ such that James has a strategy to guarantee reaching the goal with at most $n-1$ penalties. Let $P_{max}$ be the maximum number of penalties James might receive under his optimal strategy in the worst case (Peter playing optimally). Then $n = P_{max} + 1$.

We will show that $P_{max} = K = 3000$.

Part 1: Upper bound on $P_{max}$ (James's strategy).
James can adopt the Strategy of Sequential Column Testing (SCT). He tries the columns one by one. To test column $c$, he moves from $(1,1)$ to $(1,c)$ (safe, as row 1 has no stones) and then moves straight down to $(R,c)$.
If column $c$ is the free column $c^*$, James succeeds.
If column $c$ has a stone, James hits it, receives a penalty, and learns that $c \neq c^*$.

In the worst case, the free column is the last one tested. If James tests columns $1, 2, \dots, K$, and they all have stones, he receives $K$ penalties. He then knows that $c^*=K+1=C$. He succeeds on the next attempt.
Thus, James has a strategy that guarantees success with at most $K$ penalties. $P_{max} \le K$.

Part 2: Lower bound on $P_{max}$ (Peter's strategy).
We need to show that for any strategy James chooses, Peter can choose a configuration $P$ such that James receives at least $K$ penalties.

Let $J$ be James's strategy. Peter knows $J$ and chooses $P$ to maximize the penalties.

Let's consider the specific strategy J=SCT for James (testing columns $1, 2, \dots, K$).
Peter can choose the "diagonal" configuration $P_{diag} = \{(i+1, i) \mid i=1, \dots, K\}$.
The rows used are $\{2, \dots, K+1\}$. The columns used are $\{1, \dots, K\}$. The free column is $c^*=K+1=C$.

James tries C1. He hits the stone at $(2,1)$. Penalty 1.
James tries C2. He hits the stone at $(3,2)$. Penalty 2.
...
James tries CK. He hits the stone at $(K+1, K)$. Penalty $K$.

James succeeds after $K$ penalties.

However, we must consider if James can win earlier without identifying $c^*$.
Let $S$ be the set of known stones. Let $X(S)$ be the set of all cells that might contain a stone (the union of all possible configurations consistent with $S$). If there is a path from R1 to RR avoiding $X(S)$, James can take this path and win guaranteed. James only needs to take risks if $X(S)$ is a cut (blocks all paths).

Let's verify that for J=SCT and $P=P_{diag}$, $X(S)$ remains a cut until $K$ penalties are received.
After $M$ penalties ($M<K$), James knows $S_M = \{(i+1, i) \mid i=1..M\}$.
$R_{used}=\{2..M+1\}$. $C_{used}=\{1..M\}$.
$R_{rem}=\{M+2..K+1\}$. $C_{rem}=\{M+1..K+1\}$.
$X(S_M

[Note: response truncated to first 3000 characters of 4816]
