# artifact_06

Competition: BMOSL  
Problem ID: BMOSL_2019_9  
Year: 2019

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Given an acute triangle \(ABC\), let \(M\) be the midpoint of \(BC\) and \(H\) the orthocenter. Let \(\Gamma\) be the circle with diameter \(HM\), and let \(X, Y\) be distinct points on \(\Gamma\) such that \(AX, AY\) are tangent to \(\Gamma\). Prove that \(BXYC\) is cyclic.

## Candidate Excerpts

### Option A

```text
2.  The tangent–chord angles at \(X\) and at \(Y\).  
Since \(AX\) is tangent to \(\Gamma\) at \(X\), the “tangent–chord” theorem (or “alternate‐segment” theorem) gives
\[
\angle DXA \;=\;\angle DHX
\]
where the right‐hand angle is measured along the circle \(\Gamma\).  Likewise
\[
\angle DYA \;=\;\angle DHY.
\]
We will use these to relate angles at \(X,Y\) back to triangle \(ABC\).
```

### Option B

```text
1.  Construction of the foot \(D\).  
Let \(D\) be the foot of the altitude from \(A\) onto \(BC\).  Then by definition \(AD\perp BC\).  But \(H\) is the orthocenter, so \(AH\perp BC\) as well; hence \(HD\perp BC\).  Since \(M\) lies on \(BC\), we conclude
\[
\angle HDM \;=\; 90^\circ.
\]
On the other hand, \(\Gamma\) has diameter \(HM\), so for any point \(P\in\Gamma\),
\[
\angle HPM \;=\;90^\circ.
\]
In particular
\[
\angle HXM=90^\circ,
\]
so both \(D\) and \(X\) lie on the same circle with diameter \(HM\).  Thus
\[
H,\;D,\;M,\;X\qquad\text{(and similarly }H,D,M,Y)\text{)}
\]
all lie on \(\Gamma\).
```

### Option C

```text
(a)  First, in \(\triangle ADX\),
\[
\angle ADX = 90^\circ
\]
because \(AD\perp BC\) and \(D\in BC\).  In the cyclic quadrilateral \(H,D,M,X\) we saw above, also
\[
\angle HDM=90^\circ.
\]
Hence
\[
\angle ADX = \angle HDM =90^\circ.
\]
```

### Option D

```text
3.  Similarity of \(\triangle ADX\) and \(\triangle DMH\).
```

## Full Candidate Proof

```text
Proof.  Let \(ABC\) be an acute triangle, \(H\) its orthocenter, \(M\) the midpoint of \(BC\), and \(\Gamma\) the circle with diameter \(HM\).  Let \(X,Y\) be the two (distinct) points on \(\Gamma\) so that \(AX\) and \(AY\) are both tangent to \(\Gamma\).  We must show that \(B,X,Y,C\) are concyclic.

1.  Construction of the foot \(D\).  
Let \(D\) be the foot of the altitude from \(A\) onto \(BC\).  Then by definition \(AD\perp BC\).  But \(H\) is the orthocenter, so \(AH\perp BC\) as well; hence \(HD\perp BC\).  Since \(M\) lies on \(BC\), we conclude
\[
\angle HDM \;=\; 90^\circ.
\]
On the other hand, \(\Gamma\) has diameter \(HM\), so for any point \(P\in\Gamma\),
\[
\angle HPM \;=\;90^\circ.
\]
In particular
\[
\angle HXM=90^\circ,
\]
so both \(D\) and \(X\) lie on the same circle with diameter \(HM\).  Thus
\[
H,\;D,\;M,\;X\qquad\text{(and similarly }H,D,M,Y)\text{)}
\]
all lie on \(\Gamma\).

2.  The tangent–chord angles at \(X\) and at \(Y\).  
Since \(AX\) is tangent to \(\Gamma\) at \(X\), the “tangent–chord” theorem (or “alternate‐segment” theorem) gives
\[
\angle DXA \;=\;\angle DHX
\]
where the right‐hand angle is measured along the circle \(\Gamma\).  Likewise
\[
\angle DYA \;=\;\angle DHY.
\]
We will use these to relate angles at \(X,Y\) back to triangle \(ABC\).

3.  Similarity of \(\triangle ADX\) and \(\triangle DMH\).  

(a)  First, in \(\triangle ADX\),
\[
\angle ADX = 90^\circ
\]
because \(AD\perp BC\) and \(D\in BC\).  In the cyclic quadrilateral \(H,D,M,X\) we saw above, also
\[
\angle HDM=90^\circ.
\]
Hence
\[
\angle ADX = \angle HDM =90^\circ.
\]

(b)  Next,
\[
\angle AXD = \angle DMH
\]
because in the same cyclic quadrilateral \(H,D,M,X\),
\[
\angle DMH
\]
is the inscribed angle subtending arc \(DX\), and by the tangent‐chord theorem
\(\angle AXD=\angle DHX\) also subtends that same arc.

Together, (a) and (b) give two equal angles between \(\triangle ADX\) and \(\triangle HDM\), so
\[
\triangle ADX\;\sim\;\triangle HDM.
\]
An exactly analogous argument shows
\[
\triangle ADY\;\sim\;\triangle HDM.
\]

4.  The key spiral‐similarity at \(D\).  
From the similarity \(\triangle ADX\sim\triangle HDM\) at vertex \(D\) we get that the rays
\[
D X\;\longleftrightarrow\;D M
\quad\text{and}\quad
D A\;\longleftrightarrow\;D H
\]
are paired by a spiral similarity centered at \(D\).  In particular the same spiral similarity that carries segment \(HM\) to segment \(AX\) also carries segment \(HB\) to segment \(B X\).  But in triangle \(BHC\) (where \(H\) is the orthocenter of \(ABC\)) it is well‐known that
\[
\angle BHC \;=\;180^\circ-\angle A.
\]
Since a spiral similarity preserves angles, it follows that
\[
\angle BXC \;=\;\angle BHC\;=\;180^\circ-\angle A.
\]
By exactly the same reasoning with \(Y\) in place of \(X\), one also obtains
\[
\angle BYC \;=\;180^\circ-\angle A.
\]
Hence
\[
\angle BXC=\angle BYC,
\]
and that equality of opposite angles shows that \(B,X,Y,C\) are concyclic, as desired.  ∎
```

## Reviewer Note

False claims and computation mistakes.
