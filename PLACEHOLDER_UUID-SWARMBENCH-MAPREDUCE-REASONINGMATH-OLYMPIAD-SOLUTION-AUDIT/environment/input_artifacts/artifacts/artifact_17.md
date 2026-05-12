# artifact_17

Competition: IMO  
Problem ID: IMO_2007_2  
Year: 2007

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Consider five points \(A, B, C, D, E\) such that \(ABCD\) is a parallelogram and \(BCED\) is a cyclic quadrilateral. Let \(\ell\) be a line passing through \(A\), and suppose that \(\ell\) intersects the interior of the segment \(DC\) at \(F\) and intersects line \(BC\) at \(G\). Suppose that \(EF = EG = EC\). Prove that \(\ell\) is the bisector of angle \(\angle DAB\).

## Full Published Solution

```text
Step 1.  Since BCED is cyclic, the points B, C, E, D lie on a common circle, call it ω.

Step 2.  Construct the auxiliary line through E parallel to BC, and let it meet AD extended at
point P.  Since BCED is cyclic and DE = ... wait, this construction doesn't directly help.

Step 3.  Instead, use the condition EF = EG = EC.  Triangle EFG has EC as a side as well, and
since EF = EG = EC, the points F, G, C are all equidistant from E.  Hence F, G, C lie on a
circle centered at E.

Step 4.  Therefore E is the circumcenter of triangle FGC.  The line through E perpendicular to
FG passes through the midpoint of FG (by perpendicular bisector property).

Step 5.  Now consider angles.  Since BCED is cyclic, angle DBE = angle DCE (inscribed in same
arc).  Since ABCD is a parallelogram, AB || DC, so angle BAD = angle BCD (by parallelogram
property).

Step 6.  Combining angle relations: the perpendicular from E to FG and the diagonals of the
parallelogram give us the angle bisector condition.  Specifically, the line ℓ through A
intersects DC at F and BC at G with EF = EG; by symmetry of the circumcircle of FGC at E,
the angles that ℓ makes with AB and AD must be equal.

Step 7.  Hence ℓ bisects angle DAB, as required.
```

## Key Claims

[C1] In Step 1, the cyclic quadrilateral BCED has all four points on a common circle ω.

[C2] In Step 3, the equality EF = EG = EC means F, G, C lie on a circle centered at E.

[C3] In Step 4, E is the circumcenter of triangle FGC, and the perpendicular from E to FG bisects FG.

[C4] In Step 5, the inscribed angle theorem applied to BCED gives angle DBE = angle DCE.

[C5] In Step 5, the parallelogram property gives angle BAD = angle BCD.

[C6] In Step 6, the symmetry of the circumcircle of FGC at E forces the angles that ℓ makes with AB and AD to be equal.

[C7] In Step 7, the conclusion that ℓ bisects angle DAB follows from the symmetric angle condition.

## Editor's Note

This is a notoriously difficult IMO problem. The solution outlines a path via auxiliary construction and angle-chasing, but Step 6's "by symmetry of the circumcircle of FGC at E, the angles ℓ makes with AB and AD must be equal" hides several non-trivial geometric arguments behind one sentence. A reader cannot reconstruct the full argument without independent insight.
