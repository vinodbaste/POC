# artifact_082

Grading ID: GB-0765  
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

Let $R=3002$ be the number of rows and $C=3001$ be the number of columns. Let $K=3000$. Peter places $K$ stones in the intermediate rows $R'=\{2, \dots, K+1\}$, one per row and at most one per column. This implies exactly one column is free of stones, the safe column $c^*$. James starts at $(1,1)$ and wants to reach the last row $R$. He receives a penalty and restarts if he hits a stone. We want to find the smallest $n$ such that James can guarantee achieving his goal with at most $n-1$ penalties. This is a minimax problem. Let $M$ be the minimum worst-case number of penalties. We want to find $n=M+1$.

Let $H$ be the set of stones James has discovered. A cell is "safe" if James knows it does not contain a stone based on $H$ and the rules. Let $G_{safe}(H)$ be the graph of safe cells. James can guarantee a win if $G_{safe}(H)$ connects the first row (R1) to the last row (RR).

1. Upper bound on $M$.
James can adopt the strategy $S_{col}$ of testing columns sequentially: $C_1, C_2, \dots, C_K$.
In attempt $i$, James tries to follow column $C_i$. He moves from $(1,1)$ to $(1,i)$ (which is safe) and then moves straight down.
If $C_i$ is the safe column $c^*$, he wins.
If $C_i$ is not safe, it contains exactly one stone. James will eventually hit this stone, unless he deviates from the column.

Let's define the strategy $S_{col}$ more precisely. In attempt $i$, James follows the path along $C_i$. If a cell $(r,i)$ is known to be safe, he proceeds. If it is risky, he proceeds as well. If he hits a stone, the attempt ends with a penalty.

Consider the worst-case scenario for $S_{col}$. Peter chooses a configuration $P$ that maximizes the penalties. Peter can choose the safe column to be $C_{K+1}$. The columns $C_1, \dots, C_K$ are blocked. For instance, Peter can choose the diagonal configuration $P_{diag} = \{(i+1, i) : i=1, \dots, K\}$.

Attempt 1 (C1). James moves to (2,1). It is risky. He hits the stone. Penalty 1. $H_1=\{(2,1)\}$.
Attempt 2 (C2). James moves to (1,2). Then (2,2). This is safe because the stone in R2 is at (2,1). Then (3,2). This is risky. He hits the stone (3,2). Penalty 2. $H_2=\{(2,1), (3,2)\}$.
...
Attempt $K$ (CK). James moves along CK. Cells $(r, K)$ for $r=2, \dots, K$ are safe because the stones in these rows are already located in $C_1, \dots, C_{K-1}$. Cell $(K+1, K)$ is risky. He hits the stone $(K+1, K)$. Penalty $K$. $H_K=P_{diag}$.

After $K$ penalties, James has located all $K$ stones. He knows the safe column is $C_{K+1}$. He wins in the next attempt.
The maximum number of penalties is $K=3000$. So $M \le 3000$. $n \le 3001$.

2. Lower bound on $M$.
We want to show that for any strategy James uses, Peter can force at least $K$ penalties.
We use an adversarial strategy for Peter. Peter does not choose $P$ in advance but adaptively based on James's moves.

Let $H_k$ be the set of $k$ stones discovered after $k$ penalties.
James chooses a path $Q_{k+1}$. If $G_{safe}(H_k)$ is connected, James can choose a safe path and

[Note: response truncated to first 3000 characters of 5072]
