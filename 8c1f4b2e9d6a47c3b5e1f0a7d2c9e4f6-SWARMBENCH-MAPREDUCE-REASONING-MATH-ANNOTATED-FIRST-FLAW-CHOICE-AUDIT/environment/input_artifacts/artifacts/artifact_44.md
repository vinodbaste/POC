# artifact_44

Competition: BMOSL  
Problem ID: BMOSL_2023_7  
Year: 2023

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

In triangle \(ABC\) with semiperimeter \(s\), the incircle touches \(BC\), \(CA\), \(AB\) at \(D\), \(E\), \(F\) respectively.  Prove that \(BD = s - b\), where \(a = BC\), \(b = CA\), \(c = AB\).

## Candidate Excerpts

### Option A

```text
Let \(BD = x\).  Tangent segments from an external point to a circle are equal:
\(BD = BF = x\) and \(CD = CE = a - x\).
```

### Option B

```text
From vertex \(A\): \(AE = AC - CE = b - (a - x) = b - a + x\)
and \(AF = AB - BF = c - x\).  Setting \(AE = AF\):
\(b - a + x = c - x\), so \(2x = a + c - b\), giving \(x = \dfrac{a+c-b}{2} = s - b\).
```

### Option C

```text
Consistency check: \(BD + DC = x + (a - x) = a = BC\).  \checkmark
Also, \(AE + EC = (s-b) + (s-c)\).  But \(AE + EC\) should equal \(AC = b\).
And indeed \((s-b)+(s-c) = 2s - b - c = a + b + c - b - c = a = BC\), not \(b\).
```

### Option D

```text
Correcting: \(AE = s - a\) (tangent from \(A\)), and \(CE = s - c\).
Then \(AE + EC = (s-a)+(s-c) = 2s - a - c = b = CA\).  \checkmark
Hence \(BD = s-b\) and all tangent lengths are confirmed.  \(\square\)
```

## Full Candidate Proof

```text
BD=BF=x, CD=CE=a−x.  AE=b−a+x, AF=c−x.
2x=a+c−b → x=s−b ✓.

Consistency check: BD+DC=x+(a−x)=a=BC. ✓
Also, AE+EC=(s−b)+(s−c).  But AE+EC should equal AC=b.
And indeed (s−b)+(s−c)=2s−b−c=a+b+c−b−c=a=BC, not b.

Correcting: AE=s−a (tangent from A), and CE=s−c.
Then AE+EC=(s−a)+(s−c)=2s−a−c=b=CA. ✓
Hence BD=s−b and all tangent lengths are confirmed. □
```

## Reviewer Note

The consistency verification conflates two different tangent lengths — it assigns \(s-b\) to the wrong vertex's tangent segment when checking that \(AE + EC = b\).
