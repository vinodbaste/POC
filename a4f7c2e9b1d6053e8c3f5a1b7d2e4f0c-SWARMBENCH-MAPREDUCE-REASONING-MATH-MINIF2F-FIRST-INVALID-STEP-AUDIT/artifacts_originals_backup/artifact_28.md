# artifact_28

Competition: MATH
Problem ID: mathd_numbertheory_495
Year: 2020

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

How many two-digit positive integers have digits that sum to $10$?

## Candidate Excerpts

### Option A

```text
A two-digit number has the form 10a+b where a ∈ {1,...,9} and b ∈ {0,...,9}.
We need a+b = 10. Since b = 10-a and b ≤ 9, we need 10-a ≤ 9, i.e., a ≥ 1.
Also b ≥ 0 means a ≤ 10, but a ≤ 9. So a ∈ {1,...,9} and b = 10-a ∈ {1,...,9}.
```

### Option B

```text
For each valid a ∈ {1,...,9}, b = 10-a is uniquely determined and lies in {1,...,9}.
So there are exactly 9 ordered pairs: (1,9),(2,8),(3,7),(4,6),(5,5),(6,4),(7,3),(8,2),(9,1).
```

### Option C

```text
The 9 two-digit numbers are: 19, 28, 37, 46, 55, 64, 73, 82, 91.
Each has digit sum 10. ✓
```

### Option D

```text
Since the digit-sum condition a+b=10 is symmetric (swapping a and b gives the same
sum), each unordered pair {a,b} with a≠b contributes two distinct numbers. The
8 pairs with a≠b give 8×2=16 numbers, and the pair {5,5} gives 1, for a total of 17.
But we also exclude numbers whose tens digit is 0, removing any with a=0 (none
here since b=10-0=10 is not a single digit). So the final count is 17.
```

## Full Candidate Proof

```text
Step 1. Two-digit form: a ∈ {1,...,9}, b ∈ {0,...,9}, a+b=10. Since b=10-a and
b ≤ 9 requires a ≥ 1, and b ≥ 0 requires a ≤ 10 (but a ≤ 9 anyway). All 9 values
of a ∈ {1,...,9} work with b=10-a ∈ {1,...,9}.

Step 2. There are exactly 9 ordered pairs (a,b) with a ∈ {1,...,9} and b=10-a.

Step 3. The 9 numbers: 19,28,37,46,55,64,73,82,91. All correct.

Step 4. Since the condition a+b=10 is symmetric, unordered pairs with a≠b each
give two numbers, and the pair (5,5) gives one. 8 pairs × 2 + 1 = 17 total.
```

## Reviewer Note

Option D (Step 4) is the first invalid step. The proof in Steps 1–3 correctly enumerates **ordered** pairs (tens digit $a$, units digit $b$) — these are distinct two-digit numbers. For example, $(1,9)\to 19$ and $(9,1)\to 91$ are both already counted among the 9 ordered pairs. Step 4 incorrectly re-treats them as **unordered** pairs and tries to "double-count" each asymmetric pair, producing a spurious count of 17. The 9 ordered pairs already capture every distinct two-digit number with digit sum 10; no doubling is needed.
