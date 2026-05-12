# artifact_015

Grading ID: GB-0454  
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

Let the two distinct positive integers be $a$ and $b$. Let the operations be $O_1(x) = x+2$ and $O_2(x) = x \times 3$. At each step, we apply one operation to $a$ and one to $b$. Let the pairs be $(a_0, b_0) = (a, b)$, $(a_1, b_1)$, ..., $(a_n, b_n)$. We want to find all pairs $(a, b)$ such that $a_n = b_n$ for some $n$.

Let's look at the parity of the numbers.
$O_1(x) = x+2$. If $x$ is even, $x+2$ is even. If $x$ is odd, $x+2$ is odd. $O_1$ preserves parity.
$O_2(x) = 3x$. If $x$ is even, $3x$ is even. If $x$ is odd, $3x$ is odd. $O_2$ also preserves parity.
Since both operations preserve parity, the parity of $a$ will be the same as $a_n$, and the parity of $b$ will be the same as $b_n$.
If we reach a state $a_n = b_n = X$, then $a_n$ and $b_n$ must have the same parity. This means that $a$ and $b$ must have the same parity.
So, a necessary condition is $a \equiv b \pmod 2$.
Is this condition sufficient?

Let's see how we can reach equality. Suppose we reach equality for the first time at step $n$. So $a_n = b_n = X$, and $a_{n-1} \neq b_{n-1}$.
The four possibilities for the $n$-th step are:
1.  $a_n = a_{n-1}+2$ and $b_n = b_{n-1}+2$. This implies $a_{n-1} = b_{n-1}$, which contradicts our assumption.
2.  $a_n = 3a_{n-1}$ and $b_n = 3b_{n-1}$. This implies $a_{n-1} = b_{n-1}$, also a contradiction.
3.  $a_n = 3a_{n-1}$ and $b_n = b_{n-1}+2$. Here $X = 3a_{n-1} = b_{n-1}+2$. So we must have reached the state $(a_{n-1}, b_{n-1}) = (k, 3k-2)$ for some integer $k$.
4.  $a_n = a_{n-1}+2$ and $b_n = 3b_{n-1}$. Here $X = a_{n-1}+2 = 3b_{n-1}$. So we must have reached the state $(a_{n-1}, b_{n-1}) = (3k-2, k)$ for some integer $k$.

So, to reach equality, we must be able to reach a state of the form $(k, 3k-2)$ or $(3k-2, k)$ for some positive integer $k$. If we reach $(k, 3k-2)$, we apply $(O_2, O_1)$ to get $(3k, 3k-2+2) = (3k, 3k)$. If we reach $(3k-2, k)$, we apply $(O_1, O_2)$ to get $(3k-2+2, 3k) = (3k, 3k)$.
Note that $k$ and $3k-2$ have the same parity: $3k-2-k = 2k-2$, which is even. If a pair $(a, b)$ can reach $(k, 3k-2)$, it must have $a \equiv k \pmod 2$ and $b \equiv 3k-2 \pmod 2$. Since $k \equiv 3k-2$, this means $a \equiv b \pmod 2$. This is consistent with our necessary condition.

Let's try to show that $a \equiv b \pmod 2$ is sufficient. Assume $a < b$. Our goal is to reach a state $(k, 3k-2)$ or $(3k-2, k)$. Maybe we can try to reach $b = 3a-2$. The difference $3a-b = 2$. Or $a = 3b-2$. $a-3b = -2$, or $3b-a = 2$. We want to reach a state where $|3a-b|$ or $|3b-a|$ is 2.

Let's define a "goal strategy". Assume $a < b$. We want $b = 3a-2$. This is $3a-b=2$. We look at $3a-b$.
Case 1: $3a-b = 2$. We win. Just apply $(O_2, O_1)$. $(3a, b+2) = (3a, 3a)$.
Case 2: $3a-b < 2$. This means $b > 3a-2$. We want to increase $3a-b$. Let's try the operation $(O_2, O_1)$, i.e., $(3a, b+2)$. The new value is $3(3a) - (b+2) = 9a-b-2$. $9a-b-2 - (3a-b) = 6a-2$. Since $a \ge 1$, $6a-2 \ge 4$. The value increases. If we keep applying this operation

[Note: response truncated to first 3000 characters of 10880]
