# artifact_072

Grading ID: GB-0460  
Problem ID: PB-Advanced-014  
Source: Novel Problem  
IMO Area: Combinatorics

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Two distinct positive integers \( a \) and \( b \) are written on a blackboard. At each step, you must choose one of the two operations — either adding 2 or multiplying by 3 — for each number separately, and apply the chosen operation to both numbers (possibly using different operations). You must apply an operation to both numbers every step. Find all pairs $(a, b)$ such that we can make the two numbers on the blackboard equal after a finite number of steps.

## Reference Solution (for grader's calibration)

The answer is that $a$ and $b$ are both even, or $a$ and $b$ are both odd and have the same remainder when divided by 4.
 <Step 1> Finding an invariant

 Let's observe how the remainder when divided by 4 changes under the operations. First, for odd numbers, both operations change the remainder as follows:

 $1 \rightarrow 3,3 \rightarrow 1$

 For even numbers, adding 2 changes the remainder as follows:

 \[
 0 \rightarrow 2,2 \rightarrow 0
 \]

 and multiplying by 3 changes the remainder as follows:
 \[
 0 \rightarrow 0,2 \rightarrow 2
 \]


 <Step 2> Finding impossible cases

 <Step 2.1> From the observation in <Step 1>, we can find conditions on $a$ and $b$ for which the conclusion of the problem does not hold. Let's consider the following two cases:

 <Step 2.2> (Case 1) $a$ and $b$ have different parity.

 Since the parity of the two numbers does not change under the operations, the two numbers cannot become equal. Therefore, the answer is impossible in this case.

 <Step 2.3> (Case 2) $a$ and $b$ are both odd and have different remainders when divided by 4.

 Since odd numbers change their remainders when divided by 4 under each operation, the remainders of the two numbers when divided by 4 will always be different, regardless of the operations. Therefore, the answer is impossible in this case.

 Now, let's prove that the answer is possible for $a$ and $b$ that do not satisfy (Case 1) and (Case 2).

 <Step 3> Showing that the operations exist for the remaining cases.

 <Step 3.1> The remaining cases are as follows:

 (Case 3) $a, b$ are both odd and have the same remainder when divided by 4.

 (Case 4) $a, b$ are both even.

 <Step 3.2> First, let's show that we can make $a \equiv b(\bmod 4)$ for both cases by applying operations to $a$ and $b$. In (Case 3), $a \equiv b(\bmod 4)$ is already satisfied.

 In (Case 4), if $a \neq b(\bmod 4)$, then by applying the operation of changing $a$ to $3a$ and $b$ to $b+2$, we can see that $3a \equiv b+2(\bmod 4)$. Therefore, we can make the two numbers congruent modulo 4.

 <Step 3.3> Now, let's write the two numbers with the same remainder when divided by 4 as $x$ and $x+4n$. Let's add 2 to $x$ for $k$ times and then multiply it by 3. On the other hand, let's multiply $x+4n$ by 3 and then add 2 to it for $k$ times. As a result of the operations, $x$ becomes $3(x+2k)$ and $x+4n$ becomes $3x+12n+2k$.

 Therefore, if we set $k=3n$, then the two numbers become equal.

 [Short answer] $a$ and $b$ are both even, or $a$ and $b$ are both odd and have the same remainder when divided by 4.

## Grading Guidelines

(Partial)
 1. Found a correct invariant $\pmod 4$.
(Almost)
 1. Verification contains minor mistakes only.

## Candidate Response (to be graded)

**Outcome 1: COMPLETE PROOF**

We are looking for all pairs of distinct positive integers $(a, b)$ such that they can be made equal by simultaneously applying operations $S(x)=x+2$ or $M(x)=3x$ to both numbers at each step.

We prove that the necessary and sufficient conditions are that $a$ and $b$ have the same parity, and if they are odd, they are congruent modulo 4.

### Part 1: Necessary Conditions

Let $(a_k, b_k)$ denote the pair of numbers after $k$ steps, starting with $(a_0, b_0) = (a, b)$.

**1. Parity Condition (Modulo 2):**
Both operations preserve parity:
$x+2 \equiv x \pmod 2$.
$3x \equiv x \pmod 2$.
Thus, $a_k \equiv a \pmod 2$ and $b_k \equiv b \pmod 2$ for all $k$. If $a_N = b_N$ for some $N$, then $a \equiv a_N = b_N \equiv b \pmod 2$.
*Condition 1: $a$ and $b$ must have the same parity.*

**2. Modulo 4 Condition (Odd Case):**
If $a$ and $b$ are odd, all subsequent numbers $a_k, b_k$ remain odd.
If $x$ is odd, $x \equiv \pm 1 \pmod 4$. Both operations flip the residue modulo 4:
$x+2 \equiv -x \pmod 4$.
$3x \equiv -x \pmod 4$.

If $a_k$ is odd, $a_{k+1} \equiv -a_k \pmod 4$, regardless of the operation chosen for $a_k$.
By induction, if $a, b$ are odd, $a_N \equiv (-1)^N a \pmod 4$ and $b_N \equiv (-1)^N b \pmod 4$.
If $a_N = b_N$, then $(-1)^N a \equiv (-1)^N b \pmod 4$, which implies $a \equiv b \pmod 4$.
*Condition 2: If $a$ and $b$ are odd, we must have $a \equiv b \pmod 4$.*

### Part 2: Sufficiency of Conditions (Constructive Proof)

We show that if $(a, b)$ satisfies the necessary conditions, we can equalize them.

**The Strategy:** We aim for a penultimate state $(A, B)$ such that $A = 3B-2$. From this state, applying $(+2)$ to $A$ and $(\times 3)$ to $B$ yields $(A+2, 3B) = (3B, 3B)$.

Define the characteristic function $C(X, Y) = X - 3Y + 2$. We aim for $C(A, B) = 0$.

Consider the operation $P_{SS} = (+2, +2)$. It transforms $(X, Y)$ to $(X+2, Y+2)$.
$C(X+2, Y+2) = (X+2) - 3(Y+2) + 2 = C(X, Y) - 4$.

If we can reach a state $(A, B)$ such that $C(A, B) = 4m$ for some integer $m \ge 0$, we can apply $P_{SS}$ exactly $m$ times to reach $(A', B')$ where $C(A', B') = 0$.

**The Overtake Strategy:**
We apply $N$ steps of the operation $P_{MS} = (\times 3, +2)$ to $(a, b)$.
The resulting pair is $(A_N, B_N) = (3^N a, b+2N)$.
Let $C_N = C(A_N, B_N) = 3^N a - 3(b+2N) + 2 = 3^N a - 3b - 6N + 2$.

**Step 1: Ensuring $C_N \ge 0$.**
Since $a \ge 1$, $3^N a$ grows exponentially while $6N$ grows linearly. Thus, $C_N \to \infty$ as $N \to \infty$.
Furthermore, $C_{N+1} - C_N = 2 \cdot 3^N a - 6$. For $N \ge 1$ and $a \ge 1$, $C_{N+1} \ge C_N$.
There exists $N_0 \ge 1$ such that $C_N \ge 0$ for all $N \ge N_0$.

**Step 2: Ensuring $C_N \equiv 0 \pmod 4$.**
We analyze $C_N \pmod 4$. Since $3 \equiv -1 \pmod 4$:
$C_N \equiv (-1)^N a - 3b - 6N + 2 \equiv (-1)^N a + b + 2N + 2 \pmod 4$.

We analyze the cases satisfying the necessary conditions:

**Case 1: $a \equiv b \pmod 4$.** (This covers all valid odd pairs, and even pairs congruent mo

[Note: response truncated to first 3000 characters of 4070]
