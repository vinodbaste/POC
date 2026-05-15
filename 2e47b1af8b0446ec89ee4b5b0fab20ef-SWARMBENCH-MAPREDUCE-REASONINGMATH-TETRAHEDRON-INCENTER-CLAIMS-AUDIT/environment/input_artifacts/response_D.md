### Notation used

* (r) – in-radius of the insphere.
* (H) – orthogonal projection of (A) on the plane (BCD).
* (T) – point where the insphere is tangent to (BCD).
* (h=!AH).
* For any two vectors (u,v),  ([u,v]) denotes the magnitude of their cross-product.

---

## Step-0 What the given ratio really says

Because (I) is the centre of the insphere, its distance to every face equals (r).
Hence

[
\mathrm{vol}(IABC)=\frac13,(\text{area }ABC),r ,\qquad
\mathrm{vol}(IACD)=\frac13,(\text{area }ACD),r ,\quad\text{etc.}
]

The hypothesis

[
\frac{\mathrm{vol}(IABC)}{BC}= \frac{\mathrm{vol}(IACD)}{CD}= \frac{\mathrm{vol}(IADB)}{DB}
]

therefore becomes

[
\frac{\text{area }ABC}{BC}= \frac{\text{area }ACD}{CD}= \frac{\text{area }ADB}{DB}. \tag{1}
]

But (\text{area }ABC=\tfrac12,BC\cdot AH), and similarly for the other two
triangles that contain (A).
Cancelling the factor (\tfrac12) we obtain

[
AH_{BC}=AH_{CD}=AH_{DB},(=:h), \tag{2}
]

i.e. **the distances from (A) to the three edges (BC,CD,DB) are equal**.

---

## Consequences of (2)

### (c) Equal distances from (A) to the three lines

(2) is exactly statement (c).
**(c) is necessarily true.**

### The projection (H) is the in-centre of (\triangle BCD)

Let (d_{BC}) be the (planar) distance from (H) to (BC).
In the right-angled triangle with altitude (AH=h) one has

[
\text{dist}(A,BC)^2 = h^{2}+d_{BC}^{2},
]

and analogous formulas for the other two edges.
Because the left–hand sides are equal by (2), the three (d)’s are equal;
hence **(H) is equidistant from the sides of (\triangle BCD)** –
so (H) is its in-centre.
This settles statement (b):

### (b) (H) coincides with the in-centre of (BCD)

**(b) is necessarily true.**

---

### (d) Ratio of the areas of the three (A)-faces

From (1) we have

[
\text{area }ABC :\text{area }ACD :\text{area }ADB
= BC:CD:DB .
]

So **(d) is necessarily true.**

---

## Where is the insphere tangent to (BCD)?

Because (I) is equidistant from the two planes (ABC) and (ABD),
it lies on the internal bisector of the dihedral angle along the edge (AB).
Analogous statements hold for edges (AC) and (AD).
The three bisector planes meet in the line (AI);
each of them also contains the corresponding interior
bisector of the angle of (\triangle BCD) at (B,C,D) respectively,
and these three angle–bisectors meet at the in-centre (H).
Consequently **(I,H,A) are collinear**.
But (IH!\perp!BCD) (since (IH) is the radius to the tangent point),
so the whole line (AI) is perpendicular to (BCD).

### (a) (AI\perp BCD)

**(a) is necessarily true.**

Because (IH=r), (H) is exactly the point of tangency of the insphere with the
face (BCD):

### (e) Tangency point is the triangle in-centre

**(e) is necessarily true.**

---

## The remaining three statements are **not** forced

Take any **acute** triangle (BCD) that is *not* isosceles
(e.g. the one with vertices (B(0,0,0),;C(2,0,0),;D(0.5,1,0))).
Let (H) be its in-centre and put (A) a small height (h>0)
directly above (H) (for instance (h=0.1)).
Conditions (1)–(2) and the acuteness of every dihedral angle
are fulfilled (for sufficiently small (h)), yet:

* (AB\ne AC\ne AD) ⇒ **(f) is false**;
* (\triangle ABC) is not isosceles ⇒ **(g) is false**;
* (\triangle BCD) was chosen non-equilateral ⇒ **(h) is false**.

Thus the last three claims are **not** necessary.

---

## Summary

The set of statements that hold for **every** tetrahedron satisfying the two hypotheses is

[
\boxed{{a,,b,,c,,d,,e}}.
]

---

*Proofs for (a)–(e) and the explicit counter-example for (f)–(h) complete the solution.*
