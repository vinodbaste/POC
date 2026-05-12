<!-- DOMAIN_BACKGROUND: /input_artifacts/background_geometry.md -->
<!-- REQUIRED: Read /input_artifacts/background_geometry.md before evaluating this proof. -->

    # proof_09

    - Problem ID: BMOSL_2017_23
    - Competition: BMOSL
    - Year: 2017
    - Level: high_school
    - Source URL: Private
    - Dataset row index: 25

    ## Problem

    For any set of points \(A_{1}, A_{2}, \ldots, A_{n}\) on the plane, one defines \(r\left(A_{1}, A_{2}, \ldots, A_{n}\right)\) as the radius of the smallest circle that contains all of these points. Prove that if \(n \geq 3\), there are indices \(i, j, k\) such that

\[
r\left(A_{1}, A_{2}, \ldots, A_{n}\right)=r\left(A_{i}, A_{j}, A_{k}\right)
\]

    ## Candidate Solution Attempt

    Here is a self‐contained elementary proof.  All of the ingredients below are standard facts from planar Euclidean geometry (Thales’ theorem, basic convex‐combination arguments, and the fact that three non‐collinear points have a unique circumcircle).

Proof.  Let 
\[
r_0 \;=\; r(A_1,A_2,\dots,A_n)
\]
be the minimal radius of a circle containing all of the points, and let \(C\) be such a circle of radius \(r_0\), with center \(O\).  Call a point \(A_i\) a “support point’’ if \(\lvert OA_i\rvert = r_0\), i.e.\ if \(A_i\) lies on the boundary circle of \(C\).  We will show that

(a) there are either exactly two support points or at least three of them, and  

(b) in either case one can pick three indices \(i,j,k\) among the support points so that \(r(A_i,A_j,A_k)=r_0\).  

---

Step 1.  There are at least two support points.  

Suppose, to the contrary, that exactly one of the \(A_i\) lies on the boundary of \(C\); relabel so that \(\lvert OA_1\rvert=r_0\) and \(\lvert OA_i\rvert<r_0\) for \(i\ge2\).  Then set
\[
\delta \;=\;\min_{2\le i\le n}\bigl(r_0-\lvert OA_i\rvert\bigr)\;>\;0,
\]
and move the center \(O\) a tiny amount \(t\) (with \(0<t<\delta\)) in the direction of \(A_1\).  Concretely, let
\[
O'=O + t\,\frac{A_1-O}{\lvert A_1-O\rvert}.
\]
Then
\[
\lvert O'A_1\rvert \;=\;\lvert OA_1\rvert - t \;=\; r_0 - t
\;<\;r_0,
\]
while for every \(i\ge2\),
\[
\lvert O'A_i\rvert
\;\le\;\lvert OA_i\rvert + t
\;<\;r_0-\delta + t
\;\le\;r_0.
\]
Hence the circle of radius \(r_0-t\) about \(O'\) still contains all the points, contradicting the minimality of \(r_0\).  Thus there must be at least two support points.

---

Step 2.  If there are exactly two support points, say \(A_i,A_j\), then they are diametrically opposite on \(C\).  

Indeed, since \(\lvert OA_i\rvert=\lvert OA_j\rvert=r_0\), the line \(m\) joining \(A_i\) to \(A_j\) has perpendicular bisector passing through \(O\).  If \(\lvert A_iA_j\rvert<2r_0\), then \(O\) is not the midpoint of \(A_iA_j\), so one can move \(O\) a little bit along that perpendicular bisector toward the line \(A_iA_j\).  As in Step 1, this strictly decreases the common distance to \(A_i,A_j\) and, by continuity, does not raise any other distance above \(r_0\).  That again contradicts minimality.  Hence \(\lvert A_iA_j\rvert=2r_0\), i.e.\ \(A_iA_j\) is a diameter of \(C\).  

Now pick any third point \(A_k\).  By Thales’ theorem, the angle \(A_iA_kA_j\) is a right angle, so the circle with diameter \(A_iA_j\) (which is exactly \(C\)) is the minimal circle containing \(\{A_i,A_j,A_k\}\).  Therefore
\[
r(A_i,A_j,A_k)\;=\;r_0.
\]

---

Step 3.  If there are at least three support points, we produce three whose circumcircle is already \(C\), and which form an acute‐ or right‐angled triangle so that that circumcircle is their minimal enclosing circle.  

Let \(B\) be the set of all support points.  First we show \(O\) lies in the convex hull of \(B\).  If not, then there is a line \(L\) strictly separating \(O\) from \(\mathrm{Conv}(B)\).  Moving \(O\) a little towards \(\mathrm{Conv}(B)\) across \(L\) will strictly decrease the distance from \(O\) to every point of \(B\) (all at distance \(r_0\)) while, by continuity, keeping every other \(\lvert OA_i\rvert\le r_0\).  This again contradicts minimality of \(r_0\).  Hence
\[
O\;\in\;\mathrm{Conv}(B).
\]

By Carathéodory’s theorem in the plane, any point in the convex hull of a set lies in the convex hull of three of its points.  Thus there exist three support points \(A_i,A_j,A_k\in B\) such that
\[
O\;\in\;\mathrm{Conv}\,\{A_i,A_j,A_k\},
\]
i.e.\ \(O\) lies inside or on the boundary of the triangle \(\triangle A_iA_jA_k\).  But for any triangle in the plane one knows:

– Its circumcenter lies inside the triangle if and only if the triangle is acute.  
– Its circumcenter lies on a side if and only if the triangle is right.  
– Its circumcenter lies outside if and only if it is obtuse.

Since \(O\) is the circumcenter of \(\triangle A_iA_jA_k\) (all three lie on the circle \(C\) of radius \(r_0\)) and \(O\) lies in \(\triangle A_iA_jA_k\), that triangle is either acute or right.  In either case its minimal enclosing circle is its own circumcircle.  Hence the circle \(C\) of radius \(r_0\) is already the minimal disk containing \(\{A_i,A_j,A_k\}\), i.e.
\[
r(A_i,A_j,A_k)\;=\;r_0.
\]

---

Conclusion.  In all cases (exactly two support points or at least three) we have produced indices \(i,j,k\) for which
\[
r\bigl(A_i,A_j,A_k\bigr)\;=\;r\bigl(A_1,\dots,A_n\bigr),
\]
as required.  ∎