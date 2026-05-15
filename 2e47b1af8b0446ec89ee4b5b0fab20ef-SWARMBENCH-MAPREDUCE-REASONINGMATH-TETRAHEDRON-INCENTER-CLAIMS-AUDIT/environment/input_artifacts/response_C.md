Let the insphere of tetrahedron (ABCD) have center (I) and inradius (r).
Since the sphere is inscribed, the distance from (I) to each face equals (r).

For any face (XYZ),
[
\operatorname{vol}(IXYZ)
= \frac13 [XYZ]\cdot r,
]
because the height from (I) to plane (XYZ) equals (r).

---

## Step 1. Rewriting the given condition

The hypothesis
[
\frac{\operatorname{vol}(IABC)}{BC}
===================================

# \frac{\operatorname{vol}(IACD)}{CD}

\frac{\operatorname{vol}(IADB)}{DB}
]
becomes, using (\operatorname{vol}(IXYZ)=\frac13 r[XYZ]),

[
\frac{[ABC]}{BC}
================

# \frac{[ACD]}{CD}

\frac{[ADB]}{DB}.
]

Now,
[
[ABC]=\tfrac12 BC\cdot h_A^{BC},
]
where (h_A^{BC}) is the distance from (A) to line (BC).

Thus
[
\frac{[ABC]}{BC}
=\frac12 h_A^{BC}.
]

Hence the condition becomes

[
h_A^{BC}
========

# h_A^{CD}

h_A^{DB}.
]

So:

> **The distances from (A) to the three lines (BC,CD,DB) are equal.**

This proves:

### (c) is necessarily true.

---

## Step 2. Geometric meaning

If a point in space has equal distances to the three sides of a triangle (BCD), then its orthogonal projection onto plane (BCD) has equal distances to those three sides in that plane.

But in a triangle, the unique point equidistant from all three sides is the **incenter**.

Hence the projection of (A) onto plane (BCD) is the incenter of triangle (BCD).

So:

### (b) is necessarily true.

---

## Step 3. Orthogonality of (AI)

The incenter of triangle (BCD) is exactly the tangency point of the insphere with face (BCD) (since the insphere is tangent to each face at its face-incenter).

Let (T) be the tangency point on face (BCD).

From (b), the projection of (A) onto plane (BCD) equals the incenter, which is (T).

Since (IT\perp BCD) (radius to tangency point is perpendicular to the face) and (AT\perp BCD) (projection property),

points (A,I,T) are collinear.

Hence (AI\perp BCD).

So:

### (a) is necessarily true.

---

## Step 4. Statement (e)

The insphere always touches a face at the incenter of that face, independently of any extra hypothesis.

Hence:

### (e) is necessarily true.

---

## Step 5. Statements that are **not** forced

The condition constrains only the position of (A) relative to triangle (BCD).
It imposes **no symmetry conditions** on edge lengths.

We can choose an arbitrary acute triangle (BCD), then place (A) along the line perpendicular to the plane through the incenter. This preserves all hypotheses but does not force any side equalities.

Therefore:

### (f) (AB=AC=AD) — not necessary.

### (g) (AB=AC) — not necessary.

### (h) (BCD) equilateral — not necessary.

---

## Step 6. Statement (d)

Since
[
[ABC]=\tfrac12 BC\cdot h,
\quad
[ACD]=\tfrac12 CD\cdot h,
\quad
[ADB]=\tfrac12 DB\cdot h,
]
with common height (h),

[
[ABC]:[ACD]:[ADB]
=================

BC:CD:DB.
]

So:

### (d) is necessarily true.

---

# Final Answer

The statements that are necessarily true are

[
\boxed{{a,b,c,d,e}}.
]
