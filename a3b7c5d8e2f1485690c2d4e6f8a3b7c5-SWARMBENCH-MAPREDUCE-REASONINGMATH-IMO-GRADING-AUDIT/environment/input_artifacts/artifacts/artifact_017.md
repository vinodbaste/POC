# artifact_017

Grading ID: GB-0456  
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

Analysis of the Inputs:
- Candidate 1 proposes the condition: $a \equiv b \pmod 2$ and ($a, b$ odd $\implies a \equiv b \pmod 4$).
- Candidate 2 proposes only four pairs: $(2, 4), (4, 2), (2, 8), (8, 2)$. This is incorrect. For example, $(1, 5)$ is a solution: $(1, 5) \to (3, 7) \to (9, 9)$. Also, $(6, 2)$ is a solution: $(6, 2) \to (18, 2+2)=(18, 4) \to (18+2, 3 \times 4)=(20, 12) \to (20+2, 3 \times 12)=(22, 36) \dots$ Let's try another path for $(6, 2)$: $(6, 2) \to (3 \times 6, 2+2)=(18, 4) \to (3 \times 18, 4+2)=(54, 6) \dots$ Let's try $(6, 2) \to (6+2, 3 \times 2)=(8, 6) \to (8+2, 3 \times 6)=(10, 18) \dots$ Let's try $(6, 2) \to (6+2, 2+2)=(8, 4) \to (8+2, 4+2)=(10, 6) \to (10+2, 6+2)=(12, 8) \to (12+2, 8+2)=(14, 10) \to (14+2, 10+2)=(16, 12) \to (16+2, 12+2)=(18, 14) \to (18+2, 14+2)=(20, 16) \to (20+2, 16+2)=(22, 18) \to (22+2, 18+2)=(24, 20) \to \dots$ How about $(8, 4) \to (3 \times 8, 4+2)=(24, 6) \to (24+2, 3 \times 6)=(26, 18) \dots$ How about $(8, 4) \to (8+2, 3 \times 4)=(10, 12) \to (10+2, 12+2)=(12, 14) \to (12+2, 14+2)=(14, 16) \to (14+2, 16+2)=(16, 18) \to (16+2, 18+2)=(18, 20) \to (18+2, 20+2)=(20, 22) \to (20+2, 22+2)=(22, 24) \to (22+2, 24+2)=(24, 26) \dots$ How about $(10, 12) \to (3 \times 10, 12+2)=(30, 14) \to (30+2, 3 \times 14)=(32, 42) \dots$ How about $(10, 12) \to (10+2, 3 \times 12)=(12, 36) \dots$? Let's go back to $(a', b')$ for $(6, 2)$, which is $(3, 1)$. $d'=2$. $(3, 1) \to (3+1, 1+1)=(4, 2) \to d'=2$. $(3, 1) \to (3 \times 3, 3 \times 1)=(9, 3) \to d'=6$. $(3, 1) \to (3+1, 3 \times 1)=(4, 3) \to d'=1$. $(3, 1) \to (3 \times 3, 1+1)=(9, 2) \to d'=7$. From $(4, 3)$, $d'=1$. Need $b'=1$. Cannot reach $b'=1$ from $b'=3$. $(4, 3) \to (4+1, 3+1)=(5, 4) \to d'=1$. $(4, 3) \to (12, 9) \to d'=3$. $(4, 3) \to (4+1, 3 \times 3)=(5, 9) \to d'=-4$. $(4, 3) \to (3 \times 4, 3+1)=(12, 4) \to d'=8$. From $(5, 4)$, $d'=1$. Need $b'=1$. Cannot reach. From $(9, 2)$, $d'=7$. Need $b'=4$. Can reach $b'=4$ from $b'=2$. $(9, 2) \to (10, 3) \to (11, 4)$. $d'=7, b'=4$. Apply Op 3: $(11+1, 3 \times 4)=(12, 12)$. Yes, $(6, 2)$ works. Candidate 2 is incorrect.
- Candidate 3 proposes the condition: $a, b$ are both even, or $a, b$ are both odd and $a \equiv b \pmod 4$. This matches Candidate 1.
- Candidate 4 proposes the condition: $a, b$ are both even, or $a, b$ are both odd and $a \equiv b \pmod 4$. This matches Candidates 1 and 3.
- Candidate 5 failed to generate a response.

Since Candidate 2 is incorrect, not all inputs are correct.

ALL INPUTS ARE DEFINITELY CORRECT: FALSE

Standalone Solution:
Let $(a, b)$ be the pair of distinct positive integers. The allowed operations are:
1.  $(x, y) \to (x+2, y+2)$
2.  $(x, y) \to (3x, 3y)$
3.  $(x, y) \to (x+2, 3y)$
4.  $(x, y) \to (3x, y+2)$

We want to find all pairs $(a, b)$ such that we can reach a state $(X, X)$ for some positive integer $X$ after a finite number of steps. Let $(a_0, b_0) = (a, b)$ and $(a_k, b_k)$ be the pair after $k$ steps. We are looking for $(a, b)$ such that $a_n

[Note: response truncated to first 3000 characters of 7749]
