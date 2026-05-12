# artifact_002

Grading ID: GB-0478  
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

We are looking for all pairs of distinct positive integers $(a, b)$ that can be made equal after a finite number of steps, using the operations $A(x)=x+2$ and $M(x)=3x$. At each step, one operation is applied to each number.

We will show that the necessary and sufficient conditions for $(a, b)$ to be equalized are:
1. $a$ and $b$ have the same parity ($a \equiv b \pmod 2$).
2. If $a$ and $b$ are odd, they must satisfy $a \equiv b \pmod 4$.

### Part 1: Necessary Conditions

Let $(a_k, b_k)$ be the pair of numbers after $k$ steps, starting from $(a_0, b_0) = (a, b)$.

**1. Parity Condition (Modulo 2)**
We analyze the operations modulo 2:
$A(x) = x+2 \equiv x \pmod 2$.
$M(x) = 3x \equiv x \pmod 2$.
Both operations preserve the parity of an integer. Thus, $a_k \equiv a \pmod 2$ and $b_k \equiv b \pmod 2$ for all $k$. If $a_N = b_N$ for some $N$, then $a \equiv a_N = b_N \equiv b \pmod 2$. Therefore, $a$ and $b$ must have the same parity.

**2. Modulo 4 Condition for Odd Integers**
If $a$ and $b$ are odd, they remain odd at every step. We analyze the operations modulo 4 for an odd integer $x$.

If $x \equiv 1 \pmod 4$:
$A(x) = x+2 \equiv 3 \pmod 4$.
$M(x) = 3x \equiv 3 \pmod 4$.

If $x \equiv 3 \pmod 4$:
$A(x) = x+2 \equiv 5 \equiv 1 \pmod 4$.
$M(x) = 3x \equiv 9 \equiv 1 \pmod 4$.

In both cases, applying any operation $O \in \{A, M\}$ to an odd number $x$ results in $O(x) \equiv x+2 \pmod 4$.

If $a$ and $b$ are odd, then for any step $k \ge 1$, regardless of the operations chosen:
$a_k \equiv a_{k-1} + 2 \pmod 4$
$b_k \equiv b_{k-1} + 2 \pmod 4$

The difference modulo 4 is invariant:
$b_k - a_k \equiv (b_{k-1} + 2) - (a_{k-1} + 2) = b_{k-1} - a_{k-1} \pmod 4$.
By induction, $b_N - a_N \equiv b - a \pmod 4$ for all $N$.
If $a_N = b_N$, then $b_N - a_N = 0$, so we must have $b - a \equiv 0 \pmod 4$, or $a \equiv b \pmod 4$.

### Part 2: Sufficiency

We show that if these conditions are met, $a$ and $b$ can be equalized. Assume $a \neq b$.

**Case 1: $a \equiv b \pmod 4$.**
This covers all odd pairs satisfying the necessary condition, and even pairs where $a \equiv b \pmod 4$.
Without loss of generality, let $a < b$. Since $a \equiv b \pmod 4$, we have $b-a = 4k$ for some positive integer $k$.

We provide a construction to equalize $a$ and $b$ in $N = 3k+1$ steps. Let $(O_a, O_b)$ denote the operations applied to $(a, b)$ at a step.

1. Step 1: Apply $(A, M)$.
   $a_1 = a+2$.
   $b_1 = 3b$.

2. Steps 2 to $3k$: Apply $(A, A)$. We apply $A$ to both for $3k-1$ steps. (Since $k \ge 1$, $3k-1 \ge 2$). We add $2(3k-1) = 6k-2$ to both $a_1$ and $b_1$.
   $a_{3k} = a_1 + (6k-2) = (a+2) + 6k - 2 = a+6k$.
   $b_{3k} = b_1 + (6k-2) = 3b + 6k - 2$.

3. Step $N=3k+1$: Apply $(M, A)$.
   $a_N = M(a_{3k}) = 3(a+6k) = 3a+18k$.
   $b_N = A(b_{3k}) = (3b+6k-2) + 2 = 3b+6k$.

We check for equality using $b = a+4k$:
$b_N = 3(a+4k) + 6k = 3a + 12k + 6k = 3a+18k$.
Thus, $a_N = b_N$.

**Case 2: $a$ and $b$ are even, and $a \not\equiv b \pmod 4$.**
In this case, one numbe

[Note: response truncated to first 3000 characters of 4227]
