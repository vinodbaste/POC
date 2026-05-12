# artifact_46

Competition: USAMO  
Problem ID: USAMO_2022_3  
Year: 2022

From the Open Proof Corpus benchmark set. One of the four candidate excerpts below corresponds to the first step that was marked unrecoverable by a human reviewer of this proof attempt. The excerpts appear in randomized order. Select the correct letter.

## Problem

Prove that for all real numbers \(a, b\):
\[
a^2 + b^2 \;\ge\; 2ab.
\]

## Candidate Excerpts

### Option A

```text
Write \(a^2 + b^2 - 2ab\) and aim to show it is non-negative.
```

### Option B

```text
Factor: \(a^2 - 2ab + b^2 = (a - b)^2\).
```

### Option C

```text
By the AM-GM inequality applied to \(a^2\) and \(b^2\):
\[
\frac{a^2 + b^2}{2} \;\ge\; \sqrt{a^2 \cdot b^2} = |ab| \;\ge\; ab.
\]
Hence \(a^2 + b^2 \ge 2|ab| \ge 2ab\).  This proves the inequality.
Direct factoring is therefore a redundant alternative approach.
```

### Option D

```text
In fact \((a-b)^2 \ge 0\) is the cleaner proof.  Expanding gives \(a^2-2ab+b^2 \ge 0\),
i.e.\ \(a^2+b^2 \ge 2ab\).  \(\square\)
```

## Full Candidate Proof

```text
Write a²+b²−2ab and aim to show it is non-negative.

Factor: a²−2ab+b²=(a−b)².

By the AM-GM inequality applied to a² and b²:
(a²+b²)/2 ≥ √(a²·b²)=|ab|≥ab.
Hence a²+b²≥2|ab|≥2ab.  This proves the inequality.
The factoring approach is therefore a redundant alternative.

In fact (a−b)²≥0 is the cleaner proof.  Expanding gives a²−2ab+b²≥0,
i.e., a²+b²≥2ab. □
```

## Reviewer Note

The AM-GM derivation incorrectly labels the direct factoring proof as redundant, when in fact the AM-GM route introduces the unnecessary detour through absolute values.
