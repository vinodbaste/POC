# artifact_112

Grading ID: GB-0771  
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

Outcome 1: COMPLETE PROOF

Let $R=3002$ be the number of rows and $C=3001$ be the number of columns. The intermediate rows are $R_{int} = \{2, 3, \dots, R-1\}$. Peter places traps (stones) such that there is exactly one trap in each row $r \in R_{int}$ (Rule 1), and at most one trap in each column (Rule 2). James starts at $(1, 1)$ and aims to reach Row $R$. Rows 1 and $R$ are safe. If James hits a trap, he receives a penalty, learns the trap's location, and restarts at $(1, 1)$. We seek the smallest $n$ such that James guarantees reaching the goal before receiving $n$ penalties (i.e., with at most $n-1$ penalties).

We will prove that $n=3$.

### Part 1: Lower Bound ($n \ge 3$)

We show that Peter can force James to receive at least 2 penalties. This requires $R \ge 4$ (so there are at least 2 intermediate rows), which holds since $R=3002$.

**Attempt 1:** James chooses a path $P_1$. Since $R>2$, $P_1$ must enter $R_{int}$. Let $T_1=(r_1, c_1)$ be the first cell of $P_1$ in $R_{int}$. An adversarial Peter can choose a configuration where $T_1$ is a trap. In the worst case, James hits $T_1$, receives 1 penalty, and learns the location of $T_1$.

**Attempt 2:** To guarantee success on this attempt, James must follow a path $P_2$ consisting only of Guaranteed Safe Cells (GSCs). A cell is a GSC if it cannot be a trap in any valid configuration consistent with the known trap $T_1$.

We analyze the GSCs in $R_{int}$:
1.  **Row $r_1$:** By Rule 1 (exactly one trap per row), the trap in row $r_1$ is at $T_1=(r_1, c_1)$. Thus, all other cells $(r_1, c)$ where $c \neq c_1$ are GSCs.
2.  **Rows $r \in R_{int}, r \neq r_1$:** By Rule 2 (at most one trap per column), since column $c_1$ has a trap at $r_1$, there can be no other traps in column $c_1$. Thus, $(r, c_1)$ is a GSC.

A cell $(r, c)$ is risky (not a GSC) if $r \neq r_1$ and $c \neq c_1$, because a valid configuration could place the trap of row $r$ at column $c$.

We now show that the graph of GSCs is disconnected. Let $r_2 \in R_{int}$ be a row adjacent to $r_1$ (e.g., $r_2 = r_1+1$. This exists since $R\ge 4$).

For a path of GSCs to move vertically from row $r_1$ to row $r_2$, there must be a column $c$ such that both $(r_1, c)$ and $(r_2, c)$ are GSCs.
- $(r_1, c)$ is a GSC implies $c \neq c_1$.
- $(r_2, c)$ is a GSC (since $r_2 \neq r_1$) implies $c = c_1$.

These conditions are contradictory. There is no connection between the GSCs in row $r_1$ and the adjacent row $r_2$. Therefore, there is no guaranteed safe path from Row 1 to Row $R$.

Any path $P_2$ James chooses must contain at least one risky cell $T_2=(r_2, c_2)$ (where $r_2 \neq r_1, c_2 \neq c_1$). Peter can choose a configuration containing traps at both $T_1$ and $T_2$ (this is valid since they are in different rows and columns, and $K=3000 \ge 2$). Against this configuration, James fails Attempt 1 at $T_1$ and Attempt 2 at $T_2$, receiving 2 penalties.

Thus, $n-1 \ge 2$, so $n \ge 3$.

### Part 2: Upper Bound ($n \le 3$)

We prov

[Note: response truncated to first 3000 characters of 4863]
