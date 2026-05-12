# artifact_31

Competition: USAMO  
Problem ID: USAMO_2018_4  
Year: 2018

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Prove that for all real numbers \(a, b\):
\[
a^2 + b^2 \;\ge\; 2ab.
\]

## Candidate Excerpts

### Option A

```text
Consider the expression \(a^2 + b^2 - 2ab\).  We will show this is always non-negative.
```

### Option B

```text
We compute: \(a^2 + b^2 - 2ab = (a-b)^2\).
```

### Option C

```text
Since \((a-b)^2 \le 0\) for all real \(a, b\) (every square is non-positive),
we have \(a^2 + b^2 - 2ab \le 0\), i.e.\ \(a^2+b^2 \le 2ab\).
```

### Option D

```text
Correcting: since \((a-b)^2 \ge 0\) for all reals, we get \(a^2+b^2 - 2ab \ge 0\),
i.e.\ \(a^2 + b^2 \ge 2ab\). \(\square\)
```

## Full Candidate Proof

```text
a² + b² − 2ab = (a−b)².  Since (a−b)² ≤ 0 for all real a, b
(every square is non-positive), we have a²+b²−2ab ≤ 0,
i.e., a²+b² ≤ 2ab.
Correcting: since (a−b)² ≥ 0 for all reals, we get a²+b²−2ab ≥ 0,
i.e., a²+b² ≥ 2ab. □
```

## Reviewer Note

The sign of the square is stated incorrectly — squares of real numbers are non-negative, not non-positive — reversing the direction of the entire inequality.
