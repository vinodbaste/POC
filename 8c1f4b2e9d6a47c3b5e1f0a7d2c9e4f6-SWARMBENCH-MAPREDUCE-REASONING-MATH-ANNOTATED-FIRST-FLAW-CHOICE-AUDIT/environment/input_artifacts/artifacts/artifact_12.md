# artifact_12

Competition: USAMO  
Problem ID: USAMO_2023_6  
Year: 2023

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \( \triangle ABC \) be a triangle with incenter \( I \) and excenters \( I_a, I_b, I_c \) opposite \( A, B, \) and \( C \), respectively. Given an arbitrary point \( D \) on the circumcircle of \( \triangle ABC \) that does not lie on any of the lines \( II_a, I_bI_c, \) or \( BC \), suppose the circumcircles of \( \triangle DII_a \) and \( \triangle DI_bI_c \) intersect at two distinct points \( D \) and \( F \). If \( E \) is the intersection of lines \( DF \) and \( BC \), prove that \( \angle BAD = \angle EAC \).

## Candidate Excerpts

### Option A

```text
1.  Since \(D\) lies on the circumcircle \((ABC)\), the usual Inscribed-Angle Lemma gives
\[
  \angle BAD
  \;=\;
  \angle BCD
  \quad\text{(directed angles in }(ABC)\text{).}
\]
Hence it suffices to show
\[
  \angle BCD \;=\;\angle EAC.
  \tag{*}
\]
```

### Option B

```text
2.  Observe now that \(F\) is the center of the unique (orientation-preserving) spiral similarity carrying the segment \(II_a\) to the segment \(I_bI_c\), because \(F\) lies on both circles \(\omega_1\) and \(\omega_2\).  But by (1–3) above the two segments \(II_a\) and \(I_bI_c\) are perpendicular.  Therefore the spiral similarity at \(F\) carries a line through \(I\) and \(I_a\) into a perpendicular line through \(I_b\) and \(I_c\), so it rotates through a right angle.  In particular
\[
  \angle IFI_a \;=\;90^\circ
  \quad\Longrightarrow\quad
  FI\;\perp\;FI_a,
  \tag{1}
\]
and likewise
\[
  \angle I_bFI_c \;=\;90^\circ
  \quad\Longrightarrow\quad
  FI_b\;\perp\;FI_c.
  \tag{2}
\]
```

### Option C

```text
Let \(D\) be an arbitrary point on the circumcircle \((ABC)\), avoiding the three “bad’’ lines \(II_a,\;I_bI_c,\;BC\).  Denote by
\[
  \omega_1=(D\,I\,I_a),\quad
  \omega_2=(D\,I_b\,I_c)
\]
the two circles through \(D\) as in the statement, and by \(F\ne D\) their second intersection.  Finally let
\[
  E \;=\; DF\;\cap\;BC.
\]
```

### Option D

```text
We must prove
\[
  \angle BAD \;=\;\angle EAC.
\]
```

## Full Candidate Proof

```text
Proof. We work throughout with directed angles modulo 180.  Label as usual by \(I\) the incenter of \(\triangle ABC\) and by \(I_a,I_b,I_c\) its \(A\)-, \(B\)-, \(C\)-excenters; thus

1.  \(A,I,I_a\) are collinear on the internal \(A\)-bisector,  
2.  \(A,I_b,I_c\) are collinear on the external \(A\)-bisector,  
3.  the internal and external bisectors at \(A\) are perpendicular, i.e.  
\[
  II_a\;\perp\;I_bI_c.
\]

Let \(D\) be an arbitrary point on the circumcircle \((ABC)\), avoiding the three “bad’’ lines \(II_a,\;I_bI_c,\;BC\).  Denote by
\[
  \omega_1=(D\,I\,I_a),\quad
  \omega_2=(D\,I_b\,I_c)
\]
the two circles through \(D\) as in the statement, and by \(F\ne D\) their second intersection.  Finally let
\[
  E \;=\; DF\;\cap\;BC.
\]

We must prove
\[
  \angle BAD \;=\;\angle EAC.
\]

1.  Since \(D\) lies on the circumcircle \((ABC)\), the usual Inscribed-Angle Lemma gives
\[
  \angle BAD
  \;=\;
  \angle BCD
  \quad\text{(directed angles in }(ABC)\text{).}
\]
Hence it suffices to show
\[
  \angle BCD \;=\;\angle EAC.
  \tag{*}
\]

2.  Observe now that \(F\) is the center of the unique (orientation-preserving) spiral similarity carrying the segment \(II_a\) to the segment \(I_bI_c\), because \(F\) lies on both circles \(\omega_1\) and \(\omega_2\).  But by (1–3) above the two segments \(II_a\) and \(I_bI_c\) are perpendicular.  Therefore the spiral similarity at \(F\) carries a line through \(I\) and \(I_a\) into a perpendicular line through \(I_b\) and \(I_c\), so it rotates through a right angle.  In particular
\[
  \angle IFI_a \;=\;90^\circ
  \quad\Longrightarrow\quad
  FI\;\perp\;FI_a,
  \tag{1}
\]
and likewise
\[
  \angle I_bFI_c \;=\;90^\circ
  \quad\Longrightarrow\quad
  FI_b\;\perp\;FI_c.
  \tag{2}
\]

3.  But \(A,I,I_a\) are collinear, so “\(FI\perp FI_a\)” in \((1)\) says exactly that
\[
  FI \;\perp\; AI.
\]
Hence the line \(DF\), which meets \(F\), is the reflection of the line \(FI\) across the perpendicular \(AI\).  Meanwhile the line \(BC\) is the reflection of the external bisector \(I_bI_c\) across the internal bisector \(AI\), again by (1–3).  In other words,
\[
  \text{reflection in }AI\;:\quad
    FI\;\longmapsto\;DF
    \quad\text{and}\quad
    I_bI_c\;\longmapsto\;BC.
\]
But a reflection in the angle-bisector is precisely the operation that carries one side of \(\angle A\) to its isogonal.  Hence we conclude that \(DF\) and \(BC\) are isogonal lines in the angle \(\angle A\).  Equivalently, if \(E=DF\cap BC\) then
\[
  \angle BAD\;=\;\angle EAC
\]
as required.

∎

Remark.  The heart of the argument is that \(F\), being the spiral‐similarity center taking the internal \(A\)-bisector \(II_a\) to the external \(A\)-bisector \(I_bI_c\), effects a \(90^\circ\) rotation (since those two bisectors are perpendicular).  Hence \(DF\) is the isogonal conjugate of the fixed line \(BC\) in \(\angle A\), which is exactly the condition \(\angle BAD=\angle EAC\).
```

## Reviewer Note

Incorrect claims and computation mistakes.
