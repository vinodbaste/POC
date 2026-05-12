# artifact_052

Grading ID: GB-0468  
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

The problem asks for all pairs of distinct positive integers $(a, b)$ such that the two numbers can be made equal after a finite number of steps, where at each step we apply either the operation $A(x)=x+2$ or $M(x)=3x$ to both numbers simultaneously, possibly choosing different operations for each number.

We claim that the necessary and sufficient conditions for $(a, b)$ to be equalized are:
(C1) $a$ and $b$ have the same parity ($a \equiv b \pmod 2$).
(C2) If $a$ and $b$ are odd, then $a \equiv b \pmod 4$.

**Part 1: Necessity of the Conditions**

Let $(a_k, b_k)$ be the sequence of pairs on the blackboard, starting with $(a_0, b_0)=(a, b)$. Suppose $a_N=b_N$ for some finite $N$.

1. **Necessity of (C1) (Parity).**
We examine the operations modulo 2.
$A(x) = x+2 \equiv x \pmod 2$.
$M(x) = 3x \equiv x \pmod 2$.
Both operations preserve the parity of the number. Thus, for all $k \ge 0$, $a_k \equiv a \pmod 2$ and $b_k \equiv b \pmod 2$. If $a_N=b_N$, then $a \equiv a_N = b_N \equiv b \pmod 2$. Therefore, $a$ and $b$ must have the same parity.

2. **Necessity of (C2) (Modulo 4 for Odd Numbers).**
Suppose $a$ and $b$ are odd. Since parity is preserved, $a_k$ and $b_k$ remain odd for all $k$.
Let $x$ be an odd integer. We examine the operations modulo 4.
$A(x) = x+2$. $M(x) = 3x$.
The difference between the outcomes is $M(x)-A(x) = 3x-(x+2) = 2x-2 = 2(x-1)$.
Since $x$ is odd, $x-1$ is even, so $x-1=2j$ for some integer $j$. Then $2(x-1)=4j$.
Thus, $M(x) \equiv A(x) \pmod 4$.
This implies that for any odd number $x$, regardless of the operation $O \in \{A, M\}$ chosen, the result satisfies $O(x) \equiv A(x) = x+2 \pmod 4$.

At every step $k$, since $a_k$ and $b_k$ are odd:
$a_{k+1} \equiv a_k+2 \pmod 4$
$b_{k+1} \equiv b_k+2 \pmod 4$
The difference modulo 4 is invariant:
$b_{k+1}-a_{k+1} \equiv (b_k+2)-(a_k+2) = b_k-a_k \pmod 4$.
By induction, $b_N-a_N \equiv b-a \pmod 4$. If $a_N=b_N$, then $b_N-a_N=0$, so $b-a \equiv 0 \pmod 4$. Thus, if $a$ and $b$ are odd, $a \equiv b \pmod 4$.

**Part 2: Sufficiency of the Conditions**

Assume the conditions (C1) and (C2) hold for the distinct positive integers $(a, b)$. Without loss of generality, assume $a < b$. Let $D=b-a$. Since $a, b$ are distinct, $D>0$. By (C1), $D$ is a positive even integer.

We first prove a key lemma based on the non-commutativity of the operations $A$ and $M$. Let $A^k(x)$ denote applying $A$ successively $k$ times, so $A^k(x)=x+2k$.

**Equalization Lemma.** If $x$ and $y$ are positive integers such that $x<y$ and $y-x=4m$ for some positive integer $m$, then the pair $(x, y)$ can be equalized in a finite number of steps.

*Proof of the Lemma.*
We compare the results of applying $k$ additions followed by one multiplication ($M \circ A^k$) and applying one multiplication followed by $k$ additions ($A^k \circ M$).
$M(A^k(z)) = 3(z+2k) = 3z+6k$.
$A^k(M(z)) = 3z+2k$.

We aim to apply the faster growing composition $M \circ A^k$ to the smaller number $x$, and the slower composition $A^k \c

[Note: response truncated to first 3000 characters of 5839]
