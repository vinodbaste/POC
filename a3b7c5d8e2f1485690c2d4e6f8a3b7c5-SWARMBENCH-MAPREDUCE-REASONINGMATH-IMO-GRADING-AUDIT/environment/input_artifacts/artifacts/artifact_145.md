# artifact_145

Grading ID: GB-0764  
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

Here is a structured analysis of the problem.

**Analysis of the Problem**

Let $R=3002$ (rows), $C=3001$ (columns), and $K=3000$ (traps). The intermediate rows are $R_{mid} = \{2, \ldots, K+1\}$. James starts at $(1, 1)$ and wants to reach row $R=K+2$. We assume moves are to orthogonally adjacent cells.

Let $N_{max}$ be the maximum number of penalties James might incur using an optimal strategy. We seek $n = N_{max} + 1$.

After $k$ penalties, James knows $k$ traps $H_k$. Let $C_k$ and $R_k$ be their columns and rows. The set of potentially unsafe cells is $U_k = R'_k \times C'_k$, where $R'_k = R_{mid} \setminus R_k$ and $C'_k = C \setminus C_k$.
$G_k$ is the graph of guaranteed safe cells (avoiding $H_k \cup U_k$). James can guarantee success on attempt $k+1$ if and only if $G_k$ is connected from row 1 to row $R$.

**Lower Bound Analysis ($N_{max} \ge K$)**

We show that Peter has a strategy to force $K=3000$ penalties against a specific strategy by James, and analyze why James cannot avoid scenarios where safe paths are blocked.

Consider James's strategy $J_C$: Probe columns sequentially $V_1, V_2, V_3, \ldots$.

Peter adopts a strategy $P_{diag}$ where he places traps at $P = \{(i+1, i) \mid i=1, \ldots, K\}$.

1.  James tries $V_1$. Hits $T_1=(2, 1)$.
2.  James tries $V_2$. Hits $T_2=(3, 2)$.
...
k. James tries $V_k$. Hits $T_k=(k+1, k)$.

After $k$ penalties, $H_k = \{(i+1, i) \mid i=1\ldots k\}$.
$C_k = \{1, \ldots, k\}$. $R_k = \{2, \ldots, k+1\}$.

We analyze the connectivity of $G_k$, provided $k < K$ (so $R'_k$ is non-empty).

Let $A_r$ be the set of safe cells in row $r$ reachable from Row 1 within $G_k$.

**Lemma:** For $H_k$ defined above, $A_r = \{(r, c) \mid c \ge r\}$ for $r \in R_k = \{2, \ldots, k+1\}$.

*Proof by induction:* $A_2 = \{(2, c) \mid c \ge 2\}$. Assuming $A_r = \{(r, c) \mid c \ge r\}$. Row $r+1$ has a trap at $(r+1, r)$. Safe columns $S_k(r+1) = C \setminus \{r\}$. Reachable columns from $A_r$ are $\{c \ge r\} \cap (C \setminus \{r\}) = \{c \ge r+1\}$. Since $S_k(r+1)$ is disconnected at column $r$, $A_{r+1} = \{(r+1, c) \mid c \ge r+1\}$.

Now consider connectivity to row $k+2$. We need $k+2 \le K+1$, so $k \le K-1$.
Row $k+2 \in R'_k$. Safe columns $S_k(k+2) = C_k = \{1, \ldots, k\}$.
We need a vertical connection from $A_{k+1}$ to $V_{k+2}^{safe}$.
$C(A_{k+1}) = \{k+1, \ldots, C\}$.
$C(A_{k+1}) \cap S_k(k+2) = \{k+1, \ldots, C\} \cap \{1, \ldots, k\} = \emptyset$.

Thus, $A_{k+2} = \emptyset$. $G_k$ is disconnected for $k=1, \ldots, K-1$.

If James uses strategy $J_C$, Peter forces $K-1$ penalties resulting in $H_{K-1}$. $G_{K-1}$ is disconnected. James cannot guarantee success on attempt $K$.

James must choose $P_K$. $P_K$ must enter $U_{K-1}$. Peter can force a $K$-th penalty $T_K$.

This shows that for strategy $J_C$, $N(J_C, P_{diag}) = K$.

We suspect $N_{max}=K=3000$.

**Upper Bound Analysis ($N_{max} \le K$)**

James can adopt the strategy $J_C$: Probe $V_1, V_2, \ldots, V_K$.
If attempt $V_i$ fails

[Note: response truncated to first 3000 characters of 11754]
