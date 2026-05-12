# artifact_133

Grading ID: GB-0482  
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

Let the two distinct positive integers be \(a\) and \(b\). The allowed operations are adding 2 (denoted by $A$) and multiplying by 3 (denoted by $M$). At each step, we choose an operation for each number and apply it. Let the numbers at step $k$ be $(a_k, b_k)$, with $(a_0, b_0) = (a, b)$. We want to find all pairs $(a, b)$ for which $a_n = b_n$ for some finite number of steps $n$.

### 1. Parity Analysis

First, let's analyze how the operations affect the parity of a number.
- The operation $A(x) = x+2$ preserves parity: if $x$ is even, $x+2$ is even; if $x$ is odd, $x+2$ is odd.
- The operation $M(x) = 3x$ also preserves parity: if $x$ is even, $3x$ is even; if $x$ is odd, $3x$ is odd.

Since both operations preserve the parity of a number, the parity of $a_k$ will be the same as the parity of $a$ for all $k$, and the parity of $b_k$ will be the same as the parity of $b$ for all $k$.
If we can make the numbers equal, say $a_n = b_n = X$, then they must have the same parity as $X$. This implies that the initial numbers, $a$ and $b$, must have the same parity.
Therefore, a necessary condition is $a \equiv b \pmod 2$.

We now consider the two cases: both numbers are even, and both numbers are odd.

### 2. Both numbers are even

Let $a$ and $b$ be two distinct even positive integers. We will show that they can always be made equal. Let's assume $a < b$ without loss of generality. The difference $b-a$ is a positive even integer.

**Case 2.1: The difference $b-a$ is a multiple of 4.**
Let $b-a = 4k$ for some positive integer $k$. We can construct a sequence of $n = 3k+1$ operations to make the numbers equal.
The sequence of operation pairs is as follows:
- Step 1: Apply $(A, M)$ to $(a,b)$.
- Steps 2 to $3k$: Apply $(A, A)$.
- Step $3k+1$: Apply $(M, A)$.

Let's trace the values:
$(a_0, b_0) = (a, b)$.
Step 1: $(a_1, b_1) = (a+2, 3b)$.
Step 2: $(a_2, b_2) = (a_1+2, b_1+2) = (a+4, 3b+2)$.
...
After $3k$ steps, we have applied $A$ to $a$ $3k$ times in total so far, and applied $M$ to $b$ once, followed by $3k-1$ applications of $A$.
$a_{3k} = a + 2(3k) = a+6k$.
$b_{3k} = 3b + 2(3k-1) = 3b+6k-2$.
Step $3k+1$: We apply $M$ to $a_{3k}$ and $A$ to $b_{3k}$.
$a_{3k+1} = 3a_{3k} = 3(a+6k) = 3a+18k$.
$b_{3k+1} = b_{3k}+2 = (3b+6k-2)+2 = 3b+6k$.

To make the numbers equal, we require $a_{3k+1} = b_{3k+1}$:
$3a+18k = 3b+6k$
$12k = 3(b-a)$
$4k = b-a$.
This matches our initial assumption. Thus, if $a$ and $b$ are even and their difference is a multiple of 4, they can be made equal.

**Case 2.2: The difference $b-a$ is not a multiple of 4.**
Since $a$ and $b$ are even, $b-a$ is an even integer. If it's not a multiple of 4, it must be of the form $4k+2$ for some non-negative integer $k$. Since $a \neq b$, $k \ge 0$.
Let's apply one step of operations: multiply $a$ by 3 and add 2 to $b$.
The new pair is $(a_1, b_1) = (3a, b+2)$. Both $a_1$ and $b_1$ are even.
Let's compute the new difference. We consider two possibilities for the ordering of $a_1, b_1$.
The differen

[Note: response truncated to first 3000 characters of 7042]
