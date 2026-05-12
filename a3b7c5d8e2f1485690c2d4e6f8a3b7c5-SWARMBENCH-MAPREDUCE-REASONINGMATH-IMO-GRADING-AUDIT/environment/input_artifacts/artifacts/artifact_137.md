# artifact_137

Grading ID: GB-0769  
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

Outcome 2: STRUCTURED PARTIAL PROGRESS & ANALYSIS

Let $R=3002$ be the number of rows and $C=3001$ be the number of columns. Let $K=3000$ be the number of stones. The intermediate rows are $R_I=\{2, \dots, K+1\}$. Peter selects a configuration $S$, which is a matching between $R_I$ and $K$ columns of $C$. James aims to find a 4-connected path from $(1, 1)$ to Row $R$, avoiding $S$. Let $W(K)$ be the minimax number of penalties James receives. We seek $n=W(K)+1$.

Let $H=1500$, so $K=2H$ and $C=2H+1$. We conjecture that $W(2H)=H+1$, which implies $n=1502$.

### Proven Lemmas and Key Results

We rigorously prove the upper bound $W(2H) \le H+1$.

**Preliminaries: Grid Connectivity Principle (GCP)**
James can find a safe path (Top-Bottom 4-connected) if and only if the potential barrier (the set of cells that might contain a stone) does not contain a Left-Right (L-R) 8-connected path.

**Theorem 1 (Upper Bound):** $W(2H) \le H+1$.

**Proof:** We present a strategy for James, the Odd Column Strategy ($J_{Odd}$). Let $C_{Odd}=\{1, 3, \dots, 2H+1\}$ be the $H+1$ odd columns, and $C_{Even}=\{2, 4, \dots, 2H\}$ be the $H$ even columns. James sequentially probes the columns in $C_{Odd}$. A probe of column $c$ is the path that goes from $(1, 1)$ to $(1, c)$ and then straight down to $(R, c)$.

If any of these $H+1$ probes succeed, James wins with at most $H$ penalties.

Suppose all $H+1$ probes fail. James incurs $H+1$ penalties. Let $H^*$ be the set of discovered stones. $H^* = \{h_i=(r_i, 2i-1) \mid i=1, \dots, H+1\}$. Since $H^*$ is part of a matching $S$, the rows $r_i \in R_I$ must be distinct.

Let $R_K = \{r_i\}$ be the rows of the hits ($|R_K|=H+1$). Let $R_U = R_I \setminus R_K$ be the remaining rows ($|R_U|=2H-(H+1)=H-1$).

The remaining stones $S \setminus H^*$ must form a matching $M$ between $R_U$ and the remaining columns, which are $C_{Even}$ (since all odd columns are occupied by $H^*$).

We analyze the potential barrier $B(H^*)$. We must consider the information gained from the safe prefixes $K^*$. Since the probes are vertical paths in $C_{Odd}$, the safe prefixes $K^*$ are also contained in $C_{Odd}$. The matching $M$ must be contained in $R_U \times C_{Even}$. Since $C_{Odd} \cap C_{Even} = \emptyset$, $M \cap K^* = \emptyset$. Thus, any matching between $R_U$ and $C_{Even}$ is consistent with the observations.

Since $|R_U|=H-1$ and $|C_{Even}|=H$, any cell in $R_U \times C_{Even}$ can be part of such a matching. The potential barrier is $B(H^*) = H^* \cup (R_U \times C_{Even})$.

We claim that $B(H^*)$ is L-R 8-disconnected. Suppose, for contradiction, there is an L-R 8-connected path $P$ in $B(H^*)$.
Since $H^*$ is in $C_{Odd}$ and $R_U \times C_{Even}$ is in $C_{Even}$, the path $P$ must alternate between odd and even columns. To go from C1 to C(2H+1), $P$ must visit the hits in order:
$P: h_1 \to P_1 \to h_2 \to \dots \to P_H \to h_{H+1}$, where $P_i$ is a path segment in $R_U \times \{2i\}$.

The segment $P_i$ connects $h_i$ and $h

[Note: response truncated to first 3000 characters of 7797]
