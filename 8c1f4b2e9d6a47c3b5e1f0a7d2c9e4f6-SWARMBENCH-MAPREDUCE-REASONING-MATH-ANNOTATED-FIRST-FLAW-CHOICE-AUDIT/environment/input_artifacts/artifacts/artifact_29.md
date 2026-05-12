# artifact_29

Competition: BMOSL  
Problem ID: BMOSL_2021_3  
Year: 2021

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

In triangle \(ABC\) with semiperimeter \(s\), the incircle touches \(BC\), \(CA\), \(AB\) at \(D\), \(E\), \(F\) respectively.  Prove that \(BD = s - b\), where \(a = BC\), \(b = CA\), \(c = AB\).

## Candidate Excerpts

### Option A

```text
Let \(BD = x\).  Since tangent segments from the same external point to a circle are equal,
\(BD = BF = x\) and \(CD = CE = a - x\).  From vertex \(A\): the tangent lengths satisfy
\(AE = AF\).  We compute \(AE = AC - CE = b - (a - x) = b - a + x\) and
\(AF = AB - BF = c + x\).
```

### Option B

```text
Setting \(AE = AF\): \(b - a + x = c + x\), which simplifies to \(b - a = c\), i.e.\ \(b = a + c\).
This would mean \(b \ge a + c\), violating the triangle inequality (since in any triangle
each side is strictly less than the sum of the other two).
```

### Option C

```text
Since the equation \(b - a + x = c + x\) gives \(b - a = c\) with no solution for \(x\),
the tangent-length argument must be applied differently: we should use
\(AE = b - (a - x)\) and \(AF = c - x\) and set them equal to find \(x\).
```

### Option D

```text
From \(b - a + x = c - x\) (corrected), we get \(2x = a + c - b\), so
\(x = \dfrac{a + c - b}{2} = s - b\).  Hence \(BD = s - b\).  \(\square\)
```

## Full Candidate Proof

```text
Let BD = x.  Tangent lengths: BD = BF = x, CD = CE = a - x.
From A: AE = b - (a-x) = b - a + x.  But AF = c + x (claimed).
Setting AE = AF: b - a + x = c + x → b - a = c → triangle inequality violated.
Since this fails, use AF = c - x instead.
Then b - a + x = c - x → 2x = a + c - b → x = s - b.
Hence BD = s - b. □
```

## Reviewer Note

An arithmetic error in one of the tangent-length computations corrupts the key equation from the very first step.
