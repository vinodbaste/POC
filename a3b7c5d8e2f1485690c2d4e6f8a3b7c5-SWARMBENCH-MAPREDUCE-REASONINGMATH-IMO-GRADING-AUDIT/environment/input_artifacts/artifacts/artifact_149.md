# artifact_149

Grading ID: GB-0475  
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

**Complete Proof**

We are given two distinct positive integers $a$ and $b$. At each step, we apply an operation $O(x) \in \{A(x)=x+2, M(x)=3x\}$ to both numbers simultaneously. We seek all pairs $(a, b)$ that can be made equal after a finite number of steps.

We claim that the necessary and sufficient condition is:
**(C): $a$ and $b$ have the same parity ($a \equiv b \pmod 2$), and if $a$ and $b$ are odd, then $a \equiv b \pmod 4$.**

### Part 1: Necessity of Condition (C)

Let $(a_k, b_k)$ be the sequence of pairs, starting with $(a_0, b_0) = (a, b)$. Suppose $a_N = b_N$ for some finite $N \ge 1$.

**1. Necessity of $a \equiv b \pmod 2$ (Same Parity)**

We examine the operations modulo 2:
$A(x) = x+2 \equiv x \pmod 2$.
$M(x) = 3x \equiv x \pmod 2$.

Both operations preserve the parity of an integer. Thus, for all $k$, $a_k \equiv a \pmod 2$ and $b_k \equiv b \pmod 2$. If $a_N = b_N$, then $a_N \equiv b_N \pmod 2$, which implies $a \equiv b \pmod 2$.

**2. Necessity of $a \equiv b \pmod 4$ if $a, b$ are odd**

If $a$ and $b$ are odd, they remain odd throughout the process since parity is preserved. We analyze the operations modulo 4 for an odd integer $x$.

If $x \equiv 1 \pmod 4$:
$A(x) = x+2 \equiv 1+2 = 3 \equiv -1 \equiv -x \pmod 4$.
$M(x) = 3x \equiv 3(1) = 3 \equiv -1 \equiv -x \pmod 4$.

If $x \equiv 3 \pmod 4$:
$A(x) = x+2 \equiv 3+2 = 5 \equiv 1 \equiv -3 \equiv -x \pmod 4$.
$M(x) = 3x \equiv 3(3) = 9 \equiv 1 \equiv -3 \equiv -x \pmod 4$.

In all cases, if $x$ is odd, applying any operation $O \in \{A, M\}$ results in $O(x) \equiv -x \pmod 4$.

If $a$ and $b$ are odd, then for any step $k \ge 1$, regardless of the specific operations chosen:
$a_k \equiv -a_{k-1} \pmod 4$ and $b_k \equiv -b_{k-1} \pmod 4$.

By induction, after $N$ steps:
$a_N \equiv (-1)^N a \pmod 4$ and $b_N \equiv (-1)^N b \pmod 4$.

If $a_N = b_N$, then $a_N \equiv b_N \pmod 4$, so $(-1)^N a \equiv (-1)^N b \pmod 4$. Multiplying by $(-1)^N$ yields $a \equiv b \pmod 4$.

Thus, Condition (C) is necessary.

### Part 2: Sufficiency of Condition (C)

We show that if a pair of distinct positive integers $(a, b)$ satisfies Condition (C), they can be equalized. Without loss of generality, assume $a < b$.

**Case 1: $a \equiv b \pmod 4$.**

This case covers all allowed odd pairs, and even pairs where $b-a$ is a multiple of 4. Since $a < b$ and $a \equiv b \pmod 4$, we have $b-a = 4k$ for some positive integer $k \ge 1$.

We provide a construction using $N = 3k+1$ steps. We aim to apply the multiplication $M$ exactly once to $a$ and exactly once to $b$, and the addition $A$ otherwise.

Consider $N$ steps. Let $i_a$ be the step where $M$ is applied to $a$, and $i_b$ be the step where $M$ is applied to $b$. We require $1 \le i_a, i_b \le N$.

If an integer $x$ undergoes $M$ at step $i$ and $A$ at all other $N-1$ steps, the final value $x_N$ is:
$x_N = 3(x + 2(i-1)) + 2(N-i) = 3x + 6i - 6 + 2N - 2i = 3x + 4i + 2N - 6$.

We want $a_N = b_N$:
$3a + 4i_a + 2N - 6 = 3b + 4i_b + 2N - 

[Note: response truncated to first 3000 characters of 5189]
