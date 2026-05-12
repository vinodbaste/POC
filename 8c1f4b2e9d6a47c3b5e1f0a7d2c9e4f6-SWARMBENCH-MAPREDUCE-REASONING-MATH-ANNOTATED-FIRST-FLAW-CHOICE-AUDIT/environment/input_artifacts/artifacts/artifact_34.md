# artifact_34

Competition: USAMO  
Problem ID: USAMO_2014_3  
Year: 2014

OPC audit entry. A human annotator reviewing this incorrect olympiad proof marked the first unrecoverable flaw. Four candidate windows have been curated and randomly labeled A–D. Choose the label of the window that contains the human-marked flaw.

## Problem

In triangle \(ABC\) with semiperimeter \(s\), the incircle touches \(BC\), \(CA\), \(AB\) at \(D\), \(E\), \(F\) respectively.  Prove that \(BD = s - b\), where \(a = BC\), \(b = CA\), \(c = AB\).

## Candidate Excerpts

### Option A

```text
Let \(BD = x\).  Since tangent segments from the same external point are equal,
\(BD = BF = x\) and \(CD = CE = a - x\).  From vertex \(A\): \(AE = AF\).
We have \(AE = AC - CE = b - (a - x)\) and \(AF = AB - BF = c - x\).
```

### Option B

```text
Setting \(AE = AF\): \(b - (a - x) = c - x\).
Expanding: \(b - a + x = c - x\), so \(2x = a + c - b + 2b = a + b + c - b\).
Hence \(x = \dfrac{a + b + c}{2} - b = s - b\).  Conclusion: \(BD = s - b\).
```

### Option C

```text
Therefore \(BD = s - b\).  The same argument by symmetry gives \(CD = s - c\).
The two values are consistent since \(BD + DC = (s-b)+(s-c) = 2s - b - c = a\),
which equals \(BC\) as required.
```

### Option D

```text
Similarly, from vertex \(A\): \(AF = s - a\) and \(AE = s - a\), so the contact
points satisfy the three tangent-length relations simultaneously.  \(\square\)
```

## Full Candidate Proof

```text
Let BD = x.  Tangent lengths: BD = BF = x, CD = CE = a-x.
AE = b-(a-x), AF = c-x.  Setting equal: b-a+x = c-x → 2x = a+c-b.
Wait — the excerpt claims 2x = a+b+c-b = a+c, giving x=s, which is wrong.
The correct expansion is 2x = (c-b)+(a) = a+c-b, x = s-b.
BD = s-b, CD = s-c, BD+DC = 2s-b-c = a ✓.  □
```

## Reviewer Note

An algebra step expands the equation incorrectly, adding an extra term that changes the value of \(x\) from the correct answer.
