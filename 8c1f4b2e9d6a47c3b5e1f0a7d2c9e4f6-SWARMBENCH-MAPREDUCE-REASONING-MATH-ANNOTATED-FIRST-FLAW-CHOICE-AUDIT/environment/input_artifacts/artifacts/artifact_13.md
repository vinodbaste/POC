# artifact_13

Competition: USAMO  
Problem ID: USAMO_2023_6  
Year: 2023

This item is drawn from the INSAIT Open Proof Corpus. A human reviewer identified the first unrecoverable flaw in the proof below; a curator extracted four candidate excerpts from the proof text. Select the letter of the excerpt that contains the annotated flaw. Excerpts are ordered randomly, not by proof position.

## Problem

Let \( \triangle ABC \) be a triangle with incenter \( I \) and excenters \( I_a, I_b, I_c \) opposite \( A, B, \) and \( C \), respectively. Given an arbitrary point \( D \) on the circumcircle of \( \triangle ABC \) that does not lie on any of the lines \( II_a, I_bI_c, \) or \( BC \), suppose the circumcircles of \( \triangle DII_a \) and \( \triangle DI_bI_c \) intersect at two distinct points \( D \) and \( F \). If \( E \) is the intersection of lines \( DF \) and \( BC \), prove that \( \angle BAD = \angle EAC \).

## Candidate Excerpts

### Option A

```text
•  Likewise the circle \(\omega_2=\bigl(DI_bI_c\bigr)\) meets \(I_bI_c\) in those two excenters and also meets \(D\).  But \(I_bI_c\perp II_a\), so again a 180° rotation about the same line \(II_a\) swaps \(I_b\) with \(I_c\) and carries the circle \(\omega_2\) to itself—hence carries \(D\) to the *same* point \(F\).
```

### Option B

```text
\[
\{D,F\}\;\subset\;\omega_1,\quad
\{D,F\}\;\subset\;\omega_2,
\]
and the half‐turn about \(II_a\) swaps \(D\) and \(F\).
```

### Option C

```text
•  The circle \(\omega_1=\bigl(DII_a\bigr)\) carries the diameter \(II_a\) (because \(II_a\perp BC\) and \(A\) lies on \(BC\), making \(A\) the right‐angle foot for the excentral orthic configuration).  Hence \(\omega_1\) is *symmetric* under 180° about the line \(II_a\).  In particular that half‐turn swaps its two intersection points \(D\) and \(F\).
```

### Option D

```text
Thus the unique half‐turn about the altitude line \(II_a\) takes \(D\) to \(F\) and preserves *both* \(\omega_1\) and \(\omega_2\).  Equivalently,
```

## Full Candidate Proof

```text
**Proof.**

We begin by recalling a key “excentral‐orthic’’ picture.  Let \(I_aI_bI_c\) be the **excentral** triangle of \(\triangle ABC\), so that
\[
I = I_aI_bI_c\text{\quad is the orthocenter,}
\]
and the feet of the altitudes from \(I\) onto the sides \(I_bI_c,\;I_cI_a,\;I_aI_b\) are exactly
\[
A,\;B,\;C
\]
respectively.  In particular
\[
ABC
\]
is the **orthic** triangle of \(I_aI_bI_c\).  It is well‐known (or else a routine angle–chase) that the **nine‐point circle** of \(I_aI_bI_c\) is precisely the **circumcircle** of \(ABC\).  Hence the hypothesis that
\[
D\in (ABC)
\]
is equivalently
\[
D\in\text{nine‐point circle of }I_aI_bI_c.
\]

---

**Step 1.**  Let \(\ell\) denote the altitude from \(I\) in \(\triangle I_aI_bI_c\) dropping to \(I_bI_c\).  By the orthic‐triangle description, that foot of altitude is \(A\), and
\[
\ell = II_a
\]
is **perpendicular** to \(I_bI_c\).  In the “orthic” picture the other two altitudes meet \(I_cI_a\) at \(B\) and \(I_aI_b\) at \(C\), so indeed
\[
A,\;B,\;C
\]
are the feet of the three altitudes, and the nine‐point circle of \(I_aI_bI_c\) goes through \(A,B,C\) (hence through \(A,B,C\) it is exactly \((ABC)\)).

---

**Step 2.**  Because \(D\) lies on that nine‐point circle, there is a well‐known *180° rotation* (a “half‐turn”) about the **altitude line** \(\ell=II_a\) which carries
\[
D\;\longmapsto\;F
\]
where \(F\) is the *second* intersection of the two circles \(\bigl(DII_a\bigr)\) and \(\bigl(DI_bI_c\bigr)\).  We now explain why.

  •  The circle \(\omega_1=\bigl(DII_a\bigr)\) carries the diameter \(II_a\) (because \(II_a\perp BC\) and \(A\) lies on \(BC\), making \(A\) the right‐angle foot for the excentral orthic configuration).  Hence \(\omega_1\) is *symmetric* under 180° about the line \(II_a\).  In particular that half‐turn swaps its two intersection points \(D\) and \(F\).

  •  Likewise the circle \(\omega_2=\bigl(DI_bI_c\bigr)\) meets \(I_bI_c\) in those two excenters and also meets \(D\).  But \(I_bI_c\perp II_a\), so again a 180° rotation about the same line \(II_a\) swaps \(I_b\) with \(I_c\) and carries the circle \(\omega_2\) to itself—hence carries \(D\) to the *same* point \(F\).

Thus the unique half‐turn about the altitude line \(II_a\) takes \(D\) to \(F\) and preserves *both* \(\omega_1\) and \(\omega_2\).  Equivalently,

\[
\{D,F\}\;\subset\;\omega_1,\quad
\{D,F\}\;\subset\;\omega_2,
\]
and the half‐turn about \(II_a\) swaps \(D\) and \(F\).

---

**Step 3.**  But in the **original** triangle \(ABC\), the line \(II_a\) is exactly the **internal** bisector of \(\angle A\).  (Indeed \(I\) is the incenter and \(I_a\) the \(A\)-excenter, so \(II_a\) is the common bisector of the two equal tangents from \(A\) to the incircle and \(A\)-excircle.)

Since a 180° rotation about the angle-bisector \(AI\) sends the ray \(AD\) to the ray \(AF\), it follows that
\[
AF
\]
is the reflection of
\[
AD
\]
across the bisector of \(\angle A\).  In particular **lines** \(AD\) and \(AF\) are *isogonal* in \(\angle A\).

---

**Step 4.**  Finally, by definition \(E\) is the intersection
\[
E = DF\;\cap\;BC.
\]
But if \(DF\) is the *reflection* of \(AD\) across the bisector of \(\angle A\), then the point \(E\) on \(BC\) is exactly the **isogonal conjugate** of \(D\) with respect to \(\angle A\).  Hence the standard criterion for isogonal lines gives

\[
\angle BAD \;=\;\angle EAC
\]

as required.  \(\boxed{}\)

---

**Remark.**  The heart of the argument is the “excentral → orthic” picture:

• The **excentral** triangle \(I_aI_bI_c\) has orthocenter \(I\).  
• Its **orthic** triangle is \(ABC\).  
• Its nine‐point circle is \((ABC)\).  
• Rotating \(180°\) about the \(A\)-altitude \(II_a\) swaps any two points on the nine‐point circle, and likewise swaps the two intersection points of any circle through \(I\) and \(I_a\).  
• Hence the second intersections of the two circles \((DII_a)\) and \((DI_bI_c)\) are carried into one another, forcing the isogonal property that yields \(\angle BAD=\angle EAC\).
```

## Reviewer Note

Incorrect claims and implications.
