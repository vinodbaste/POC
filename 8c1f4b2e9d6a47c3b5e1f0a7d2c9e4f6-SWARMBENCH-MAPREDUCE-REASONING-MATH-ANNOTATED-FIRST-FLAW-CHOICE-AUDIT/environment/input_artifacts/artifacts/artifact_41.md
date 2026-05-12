# artifact_41

Competition: BMOSL  
Problem ID: BMOSL_2022_4  
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
We may assume without loss of generality that \(a \ge b \ge 0\), since the inequality
is symmetric in \(a, b\) and replacing both \(a, b\) by \(|a|, |b|\) does not change
\(a^2 + b^2\) while it can only decrease \(2ab\) (if one of \(a, b\) is negative).
Hence it suffices to prove the inequality for non-negative reals.
```

### Option B

```text
For \(a \ge b \ge 0\): \(a^2 + b^2 - 2ab = (a-b)^2 \ge 0\).
```

### Option C

```text
Therefore \(a^2 + b^2 \ge 2ab\), with equality iff \(a = b\).  \(\square\)
```

### Option D

```text
The full inequality (without the WLOG assumption) follows by
noting that \((a-b)^2 \ge 0\) holds for all reals, not just non-negative ones.
```

## Full Candidate Proof

```text
We may assume without loss of generality that a≥b≥0, since the inequality
is symmetric in a,b and replacing both a,b by |a|,|b| does not change
a²+b² while it can only decrease 2ab (if one of a,b is negative).
Hence it suffices to prove the inequality for non-negative reals.

For a≥b≥0: a²+b²−2ab=(a−b)²≥0.

Therefore a²+b²≥2ab, with equality iff a=b.

The full inequality (without the WLOG assumption) follows from noting that
(a−b)²≥0 holds for all reals, not just non-negative ones.
```

## Reviewer Note

The WLOG reduction to non-negative reals is invalid: taking absolute values can increase \(2ab\) (when the signs of \(a\) and \(b\) differ), so the reduction does not make the inequality easier to prove.
