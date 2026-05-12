# artifact_39

Competition: IMOSL  
Problem ID: IMOSL_2018_8  
Year: 2018

OPC audit entry. A human annotator reviewing this incorrect olympiad proof marked the first unrecoverable flaw. Four candidate windows have been curated and randomly labeled A–D. Choose the label of the window that contains the human-marked flaw.

## Problem

In triangle \(ABC\) with semiperimeter \(s\), the incircle touches \(BC\), \(CA\), \(AB\) at \(D\), \(E\), \(F\) respectively.  Prove that \(BD = s - b\), where \(a = BC\), \(b = CA\), \(c = AB\).

## Candidate Excerpts

### Option A

```text
Let \(BD = x\).  Tangent lengths from the same external point are equal:
\(BD = BF = x\) and \(CD = CE = a - x\).
From \(A\): \(AE = AC - CE = b-(a-x)\) and \(AF = AB - BF = c - x\).
```

### Option B

```text
Setting \(AE = AF\): \(b - a + x = c - x\), giving \(2x = a + c - b\),
hence \(x = \dfrac{a + c - b}{2} = s - b\).
```

### Option C

```text
Therefore \(BD = s - b\).  By the same reasoning, \(CD = s - a\).
We verify: \(BD + DC = (s-b) + (s-a) = 2s - a - b = c = AB\).
But \(BD + DC\) should equal \(BC = a\), not \(AB = c\).
```

### Option D

```text
Correcting: \(CD = s - c\), not \(s - a\).  Then \(BD + DC = (s-b)+(s-c) = 2s-b-c = a = BC\). \checkmark
Similarly \(AE = AF = s-a\).  \(\square\)
```

## Full Candidate Proof

```text
BD=BF=x, CD=CE=a−x.  AE=b−(a−x), AF=c−x.
2x=a+c−b → x=s−b ✓.
Therefore BD=s−b.  By the same reasoning, CD=s−a.

We verify: BD+DC=(s−b)+(s−a)=2s−a−b=c=AB.
But BD+DC should equal BC=a, not AB=c.

Correcting: CD=s−c (not s−a).  Then BD+DC=(s−b)+(s−c)=2s−b−c=a=BC. ✓
Similarly AE=AF=s−a. □
```

## Reviewer Note

After correctly computing \(BD\), the derivation of the companion tangent length \(CD\) inverts the roles of the sides, giving a self-contradicting consistency check.
