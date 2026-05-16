# artifact_05

Competition: AIME
Problem ID: aime_1987_p8
Year: 1987

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

What is the remainder when $2^{1987}$ is divided by $15$?

## Candidate Excerpts

### Option A

```text
Using the Chinese Remainder Theorem, compute 2^{1987} mod 3 and mod 5 separately.
  mod 3: ord_3(2) = 2, since 2^2 = 4 ≡ 1 (mod 3). 1987 = 2·993+1, so 2^{1987} ≡ 2 (mod 3).
  mod 5: ord_5(2) = 4, since 2^4 = 16 ≡ 1 (mod 5). 1987 = 4·496+3, so 2^{1987} ≡ 2^3 = 8 ≡ 3 (mod 5).
```

### Option B

```text
By CRT, we need x ≡ 2 (mod 3) and x ≡ 3 (mod 5) with 0 ≤ x < 15.
Testing: x = 8: 8 mod 3 = 2 ✓, 8 mod 5 = 3 ✓. So 2^{1987} ≡ 8 (mod 15).
```

### Option C

```text
Therefore the remainder when 2^{1987} is divided by 15 is 8.
```

### Option D

```text
By Fermat's Little Theorem, for any prime p and integer a with gcd(a,p)=1,
we have a^{p-1} ≡ 1 (mod p). Taking p = 15, this gives 2^{14} ≡ 1 (mod 15),
so 2^{1987} = 2^{14·141+13} = (2^{14})^{141} · 2^{13} ≡ 1^{141} · 2^{13} = 8192
≡ 8192 - 546·15 = 8192 - 8190 = 2 (mod 15).
```

## Full Candidate Proof

```text
Step 1. By Fermat's Little Theorem with p = 15, we get 2^{14} ≡ 1 (mod 15).
Then 1987 = 14·141+13, so 2^{1987} ≡ 2^{13} = 8192 ≡ 2 (mod 15).

Step 2. [Correct approach using CRT.] Compute mod 3: ord_3(2)=2, 1987≡1 (mod 2),
so 2^{1987}≡2 (mod 3). Compute mod 5: ord_5(2)=4, 1987≡3 (mod 4), so
2^{1987}≡2^3=8≡3 (mod 5).

Step 3. By CRT: x≡2 (mod 3) and x≡3 (mod 5). Testing x=8: 8≡2 (mod 3) ✓ and
8≡3 (mod 5) ✓. So 2^{1987}≡8 (mod 15).

Step 4. The remainder is 8.
```

## Reviewer Note

Option A (Step 1) is the first invalid step. Fermat's Little Theorem requires the modulus to be **prime**. The number 15 = 3×5 is composite, so FLT does not apply to it directly. The claim that 2^{14} ≡ 1 (mod 15) is incidentally false (2^4 = 16 ≡ 1 (mod 15) is the actual order). The legitimate proof uses CRT to reduce to the prime moduli 3 and 5, which the later steps do correctly.
