# artifact_09

Competition: IMOSL  
Problem ID: IMOSL_2018_G2  
Year: 2018

Benchmark item — published olympiad solution under peer-review audit. Verify each numbered key claim against the solution text, identify the central technique, and assign a rigor score per the audit rubric.

## Problem

Let \(ABC\) be a triangle with incircle \(\omega\) touching \(BC\) at \(D\). The line through \(D\) parallel to \(AB\) meets the line \(AC\) at \(E\). Prove that \(BE\) bisects \(\angle ABD\).

## Full Published Solution

```text
Step 1.  Set up coordinates: let the incircle ω have center I and radius r.  D is the tangency
point on BC.  By the standard tangent-length formula, BD = s - b, where s = (a + b + c)/2 is
the semiperimeter and b = CA.

Step 2.  Since DE is parallel to AB, triangles BDE and BAB' are similar where B' is the point
on AC at the foot of the parallel.  Hmm, this similarity is awkwardly stated; instead, use
the parallel line directly:  DE || AB implies angle BDE = angle ABD (alternate angles).

Step 3.  By the power of a point, the line through D parallel to AB meets line AC at E with
the relation BD · DE = DA · DE' for some E' — but this doesn't lead anywhere obvious.

Step 4.  By Menelaus's theorem applied to triangle ABC with transversal DE (extended), we get
(BE / EA) · (something) = 1.  After working out the proportions: BE / EA = (BD / DC) · (CA / AB) = ...

Step 5.  Using BD = s - b, DC = s - c, AB = c, AC = b:
BE / EA = ((s - b) / (s - c)) · (b / c).

Step 6.  By the angle bisector theorem, BE bisects angle ABD iff AE / EC = AB / BD.  Plugging
in: AE / EC = c / (s - b), and our derived BE / EA inverted gives EA / BE = (s - c) c / ((s - b) b).
These are not obviously equal.

Step 7.  After algebraic verification: ((s - b) · b) / ((s - c) · c) does equal c / (s - b) when
s, b, c satisfy a specific identity related to the triangle's incircle.  Hence BE bisects
angle ABD.
```

## Key Claims

[C1] In Step 1, the tangent-length formula BD = s - b is a standard incircle property.

[C2] In Step 2, the parallel-line property DE || AB gives angle BDE = angle ABD by alternate angles.

[C3] In Step 4, Menelaus's theorem with appropriate transversal yields BE / EA = (BD / DC) · (CA / AB).

[C4] In Step 5, substituting BD = s - b, DC = s - c gives BE / EA = ((s - b)/(s - c)) · (b/c).

[C5] In Step 6, the angle bisector theorem condition for BE bisecting angle ABD is AE / EC = AB / BD.

[C6] In Step 7, the equality ((s - b) · b) / ((s - c) · c) = c / (s - b) follows from a triangle-specific identity related to the incircle.

[C7] The proof's conclusion that BE bisects angle ABD is established by Step 7's algebraic verification.

## Editor's Note

This solution applies several classical theorems (tangent-length, parallel-line angle, Menelaus, angle-bisector) but the Step 7 closing step claims the algebraic identity "follows from a triangle-specific identity" without actually deriving it — a gap.
