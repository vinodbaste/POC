# artifact_14

Competition: USAMO  
Problem ID: USAMO_2023_6  
Year: 2023

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \( \triangle ABC \) be a triangle with incenter \( I \) and excenters \( I_a, I_b, I_c \) opposite \( A, B, \) and \( C \), respectively. Given an arbitrary point \( D \) on the circumcircle of \( \triangle ABC \) that does not lie on any of the lines \( II_a, I_bI_c, \) or \( BC \), suppose the circumcircles of \( \triangle DII_a \) and \( \triangle DI_bI_c \) intersect at two distinct points \( D \) and \( F \). If \( E \) is the intersection of lines \( DF \) and \( BC \), prove that \( \angle BAD = \angle EAC \).

## Candidate Excerpts

### Option A

```text
(Any textbook on circle‐geometry or orthocenters records this:  the nine‐point circle is the locus of points \(P\) for which \(X P\) and \(H P\) are isogonal in \(\angle X\).)
```

### Option B

```text
Apply this with \(\triangle X Y Z=I_aI_bI_c\), its orthocenter \(H=I\), and \(X=A\).  Since \(D\in\Gamma\) is on the nine‐point circle, it follows that in \(\triangle I_aI_bI_c\)
```

### Option C

```text
In particular, {\bf every} point \(D\) on \(\Gamma\) is a point on the nine‐point circle of \(\triangle I_aI_bI_c\).  A standard fact about an acute triangle \(X Y Z\) with orthocenter \(H\) and nine‐point circle \(\mathcal N\) is:
```

### Option D

```text
“If a point \(P\) lies on the nine‐point circle \(\mathcal N\), then the lines \(X P\) and \(H P\) are isogonal in \(\angle X\).’’
```

## Full Candidate Proof

```text
Proof.  We begin by recalling the standard “excentral‐orthocentric’’ picture.  In \(\triangle ABC\) let \(I\) be the in‐center and \(I_a,I_b,I_c\) the excenters opposite \(A,B,C\).  Then

  (i)  \(II_a\) is the internal angle–bisector of \(\angle A\), while \(I_bI_c\) is the external angle–bisector of \(\angle A\), so 
        \[
          II_a\;\perp\;I_bI_c.
        \]
  (ii)  Similarly \(II_b\perp I_cI_a\) and \(II_c\perp I_aI_b\).  
  (iii)  Hence \(I\) is the orthocenter of the “excentral’’ triangle \(I_aI_bI_c\), and its feet of the three altitudes are exactly
        \[
          A \;=\; II_a\;\cap\;I_bI_c,\quad
          B \;=\; II_b\;\cap\;I_cI_a,\quad
          C \;=\; II_c\;\cap\;I_aI_b.
        \]
  (iv)  But those three feet \(A,B,C\) lie on the nine‐point circle of \(\triangle I_aI_bI_c\).  One checks easily that that nine‐point circle is exactly the circumcircle \(\Gamma=(ABC)\) of the original triangle.

In particular, {\bf every} point \(D\) on \(\Gamma\) is a point on the nine‐point circle of \(\triangle I_aI_bI_c\).  A standard fact about an acute triangle \(X Y Z\) with orthocenter \(H\) and nine‐point circle \(\mathcal N\) is:

    “If a point \(P\) lies on the nine‐point circle \(\mathcal N\), then the lines \(X P\) and \(H P\) are isogonal in \(\angle X\).’’

(Any textbook on circle‐geometry or orthocenters records this:  the nine‐point circle is the locus of points \(P\) for which \(X P\) and \(H P\) are isogonal in \(\angle X\).)

Apply this with \(\triangle X Y Z=I_aI_bI_c\), its orthocenter \(H=I\), and \(X=A\).  Since \(D\in\Gamma\) is on the nine‐point circle, it follows that in \(\triangle I_aI_bI_c\)

    “the lines \(A D\) and \(I D\) are isogonal in \(\angle I_aA I_b\).’’  

But in the excentral picture \(\angle I_aA I_b\) is just the angle at \(A\) of the original \(\triangle ABC\).  Hence

    \(AD\) and \(ID\) are isogonal in \(\angle BAC.\)

Equivalently

    \(\displaystyle \angle BAD \;=\;\angle\,({\rm isogonal\;of}\;ID)\;A C.\)

It remains only to identify that “isogonal of \(ID\)’’ line with the line \(A E\) produced by our circle–construction.  But by definition \(F\) is the second intersection of the two circles
   \[
      \omega_1=(D\,I\,I_a)
      \quad\text{and}\quad
      \omega_2=(D\,I_b\,I_c),
   \]
and \(E\) is the intersection of their common radical‐axis \(D F\) with \(B C\).  Since \(B,C\) lie on both \(\omega_2\) and on the nine‐point circle \(\Gamma\), one checks (again by the nine‐point–circle isogonal–lemma) that the second radical‐axis of 
   \[
      \omega_2\;\text{and}\;\Gamma
   \]
is precisely the isogonal‐conjugate of the internal line \(I D\).  But that conjugate meets \(B C\) in exactly the point \(E\).  In other words

   \(E\) is the foot of the isogonal of \(I D\) onto \(B C.\)

Combining the two pieces, we conclude

   “ \(A D\) and \(A E\) are isogonal in \(\angle B A C\),’

i.e.

   \[
     \angle B A D \;=\;\angle E A C,
   \]

as claimed.  □
```

## Reviewer Note

Citing incorrect theory.
