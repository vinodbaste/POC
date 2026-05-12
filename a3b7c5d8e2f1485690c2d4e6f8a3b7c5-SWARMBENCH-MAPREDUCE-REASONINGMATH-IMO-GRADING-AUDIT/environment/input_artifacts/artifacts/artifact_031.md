# artifact_031

Grading ID: GB-0457  
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

We are looking for all pairs of distinct positive integers $(a, b)$ such that we can make them equal after a finite number of steps, where each step involves applying an operation from $\{+2, \times 3\}$ to both numbers simultaneously.

We claim that the necessary and sufficient conditions for $(a, b)$ to be equalizable are:
1. $a$ and $b$ have the same parity ($a \equiv b \pmod 2$).
2. If $a$ and $b$ are odd, then $a \equiv b \pmod 4$.

### Part 1: Necessary Conditions

**1. Necessity of $a \equiv b \pmod 2$.**

We examine the operations modulo 2. For any integer $x$:
$x+2 \equiv x \pmod 2$.
$3x \equiv x \pmod 2$.
Both operations preserve the parity of a number. If we start with $(a, b)$ and reach a state $(a_k, b_k)$ after $k$ steps, we must have $a_k \equiv a \pmod 2$ and $b_k \equiv b \pmod 2$. If the numbers become equal, say $a_N = b_N = X$, then $a \equiv X \equiv b \pmod 2$. Thus, $a$ and $b$ must have the same parity.

**2. Necessity of $a \equiv b \pmod 4$ when $a, b$ are odd.**

If $a$ and $b$ are odd, all subsequent numbers generated remain odd. We examine the operations modulo 4 for an odd integer $x$.

If $x \equiv 1 \pmod 4$:
$x+2 \equiv 1+2 = 3 \pmod 4$.
$3x \equiv 3(1) = 3 \pmod 4$.

If $x \equiv 3 \pmod 4$:
$x+2 \equiv 3+2 = 5 \equiv 1 \pmod 4$.
$3x \equiv 3(3) = 9 \equiv 1 \pmod 4$.

In both cases, applying either operation to an odd number $x$ results in a number $x'$ such that $x' \equiv x+2 \equiv -x \pmod 4$. The residue modulo 4 flips (from 1 to 3, or 3 to 1) in every step.

Let $(a_k, b_k)$ be the numbers after $k$ steps. If $a$ and $b$ are odd, $a_k \equiv (-1)^k a \pmod 4$ and $b_k \equiv (-1)^k b \pmod 4$.
If $a_N = b_N$ for some $N$, then $a_N \equiv b_N \pmod 4$.
$(-1)^N a \equiv (-1)^N b \pmod 4$. Multiplying by $(-1)^N$, we get $a \equiv b \pmod 4$.

### Part 2: Sufficient Conditions

We show that if $a$ and $b$ satisfy the conditions, they can be equalized. Since $a \neq b$, assume without loss of generality $a < b$. Let $D = b-a$. Since $a \equiv b \pmod 2$, $D$ is a positive even integer.

**Target Configuration:** If we reach a pair $(A, B)$ such that $B = 3A-2$, we can equalize them in one step by applying $(\times 3, +2)$:
$(A, 3A-2) \to (3A, (3A-2)+2) = (3A, 3A)$.

We consider two cases based on $D \pmod 4$.

**Case 1: $D \equiv 0 \pmod 4$.**

This case covers both $a, b$ odd (where $a \equiv b \pmod 4$ is required) and $a, b$ even with $D \equiv 0 \pmod 4$.
Since $D>0$, let $D = 4m$ for some integer $m \ge 1$.

We employ the following strategy (Strategy C):
1. Apply $(+2, \times 3)$ to $(a, b)$. We get $(a_1, b_1) = (a+2, 3b)$.
2. Apply $(+2, +2)$ repeatedly $k$ times to $(a_1, b_1)$. We get $(A, B) = (a_1+2k, b_1+2k)$.
3. Apply $(\times 3, +2)$ to $(A, B)$.

We need to find a non-negative integer $k$ such that $B = 3A-2$.
$b_1+2k = 3(a_1+2k)-2$
$3b+2k = 3(a+2)+6k-2$
$3b+2k = 3a+6+6k-2$
$3(b-a) - 4 = 4k$
$3D - 4 = 4k$.

Substituting $D=4m$:
$4k = 3(4m) - 4 = 12m - 4$.
$k = 3m-1$.
Since $m \ge 1$, $k \ge 3(1

[Note: response truncated to first 3000 characters of 4385]
