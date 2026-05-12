<!-- DOMAIN_BACKGROUND: /input_artifacts/background_geometry.md -->
<!-- REQUIRED: Read /input_artifacts/background_geometry.md before evaluating this proof. -->

    # proof_04

    - Problem ID: BMOSL_2020_13
    - Competition: BMOSL
    - Year: 2020
    - Level: high_school
    - Source URL: https://www.imo-official.org/
    - Dataset row index: 8

    ## Problem

    Let \( \triangle ABC \) be an isosceles triangle with \( AB = AC \) and \( \angle A = 45^\circ \). Its circumcircle \((c)\) has center \( O \). \( M \) is the midpoint of \( BC \) and \( D \) is the foot of the perpendicular from \( C \) to \( AB \). With center \( C \) and radius \( CD \), we draw a circle which internally intersects \( AC \) at the point \( F \) and the circle \((c)\) at the points \( Z \) and \( E \), such that \( Z \) lies on the small arc \(\overparen{BC}\) and \( E \) on the small arc \(\overparen{AC}\). Prove that the lines \( ZE, CO, FM \) are concurrent.

    ## Candidate Solution Attempt

    Proof.  We give a completely elementary proof by placing the figure in the plane with coordinates and then checking by direct computation that the three lines meet at one point.

1.  Coordinates for A, B, C.  Since \(AB=AC\) and \(\angle A=45^\circ\), we may take
\[
A=(0,0),\quad B=(1,0),\quad C=\Bigl(\cos45^\circ,\;\sin45^\circ\Bigr)
     =\Bigl(\tfrac{\sqrt2}2,\;\tfrac{\sqrt2}2\Bigr).
\]

2.  The circumcenter \(O\).  The perpendicular bisector of \(AB\) is the vertical line \(x=\tfrac12\).  The segment \(AC\) has midpoint
\[
\Bigl(\tfrac{\sqrt2}{4},\,\tfrac{\sqrt2}{4}\Bigr)
\]
and slope \(1\), so its perpendicular bisector has slope \(-1\) and passes through \(\bigl(\tfrac{\sqrt2}{4},\tfrac{\sqrt2}{4}\bigr)\).  Hence its equation is
\[
y-\tfrac{\sqrt2}{4}\;=\;-1\Bigl(x-\tfrac{\sqrt2}{4}\Bigr).
\]
Intersecting with \(x=\tfrac12\) gives
\[
y-\tfrac{\sqrt2}{4}
\;=\;-1\Bigl(\tfrac12-\tfrac{\sqrt2}{4}\Bigr)
\;=\;\tfrac{\sqrt2}{4}-\tfrac12,
\]
so
\[
y=\tfrac{\sqrt2}{2}-\tfrac12=\frac{\sqrt2-1}2.
\]
Thus
\[
O=\Bigl(\tfrac12,\;\tfrac{\sqrt2-1}2\Bigr).
\]
The circumradius is
\[
R=OA
=\sqrt{\Bigl(\tfrac12\Bigr)^2+\Bigl(\tfrac{\sqrt2-1}2\Bigr)^2}
=\sqrt{\tfrac14+\tfrac{(\sqrt2-1)^2}{4}}
=\sqrt{\tfrac{4-2\sqrt2}{4}}
=\sqrt{\frac{2-\sqrt2}2}.
\]
Hence the circumcircle \((c)\) has equation
\[
(x-\tfrac12)^2+(y-\tfrac{\sqrt2-1}2)^2=\frac{2-\sqrt2}2.
\]

3.  The points \(M,D\).  The midpoint of \(BC\) is
\[
M=\Bigl(\tfrac{1+\frac{\sqrt2}2}2,\;\tfrac{0+\frac{\sqrt2}2}2\Bigr)
  =\Bigl(\tfrac{2+\sqrt2}4,\;\tfrac{\sqrt2}4\Bigr).
\]
The foot \(D\) of the perpendicular from \(C\) to \(AB\) (the \(x\)–axis) is
\[
D=\bigl(\tfrac{\sqrt2}2,\,0\bigr).
\]
Hence
\[
CD=\frac{\sqrt2}2,
\]
and the “small” circle with center \(C\) and radius \(CD\) has equation
\[
(x-\tfrac{\sqrt2}2)^2+(y-\tfrac{\sqrt2}2)^2=\frac12.
\]

4.  The point \(F\).  The line \(AC\) has equation \(y=x\).  Intersecting it with 
\[
(x-\tfrac{\sqrt2}2)^2+(y-\tfrac{\sqrt2}2)^2=\tfrac12
\]
we substitute \(y=x\) and get
\[
2\bigl(x-\tfrac{\sqrt2}2\bigr)^2=\tfrac12
\quad\Longrightarrow\quad
\bigl(x-\tfrac{\sqrt2}2\bigr)^2=\tfrac14
\quad\Longrightarrow\quad
x-\tfrac{\sqrt2}2=\pm\tfrac12.
\]
Hence the two intersection points are
\[
x=\frac{\sqrt2}2\pm\frac12,
\quad y=x.
\]
The “internal” one on the segment \(AC\) is
\[
F=\Bigl(\tfrac{\sqrt2-1}2,\;\tfrac{\sqrt2-1}2\Bigr).
\]

5.  The points \(E\) and \(Z\).  These are the two intersection points of the circle
\[
(x-\tfrac12)^2+(y-\tfrac{\sqrt2-1}2)^2=\frac{2-\sqrt2}2
\qquad\text{and}\qquad
(x-\tfrac{\sqrt2}2)^2+(y-\tfrac{\sqrt2}2)^2=\frac12.
\]
Subtract the first equation from the second.  A straightforward expansion yields the linear relation
\[
(\sqrt2-1)\,x\;+\;y\;=\;\tfrac12.
\]
Hence \(E\) and \(Z\) lie on the line
\[
L:\;y=\frac12-(\sqrt2-1)\,x.
\]
We do not need their explicit coordinates, only that \(\overline{EZ}\subset L\).

6.  The line \(CO\).  From
\[
C=\Bigl(\tfrac{\sqrt2}2,\tfrac{\sqrt2}2\Bigr),
\quad
O=\Bigl(\tfrac12,\;\tfrac{\sqrt2-1}2\Bigr)
\]
one computes the slope
\[
m_{CO}
=\frac{\frac{\sqrt2-1}2-\frac{\sqrt2}2}{\tfrac12-\tfrac{\sqrt2}2}
=\frac{-\tfrac12}{-\tfrac{\,\sqrt2-1}2}
=\frac12\;\Big/\;\frac{\sqrt2-1}2
=\frac1{\sqrt2-1}
=\sqrt2+1.
\]
Hence the equation of the line \(CO\) is
\[
y-\frac{\sqrt2}2=(\sqrt2+1)\!\Bigl(x-\frac{\sqrt2}2\Bigr)
\quad\Longleftrightarrow\quad
y=(\sqrt2+1)x-1.
\]

7.  Intersection \(P\) of \(L\) and \(CO\).  We solve
\[
\begin{cases}
y=(\sqrt2+1)x-1,\\
y=\tfrac12-(\sqrt2-1)x.
\end{cases}
\]
Equating the two right–hand sides,
\[
(\sqrt2+1)x-1
\;=\;\tfrac12-(\sqrt2-1)x
\;\Longrightarrow\;
(\sqrt2+1+\,\sqrt2-1)\,x=\tfrac32
\;\Longrightarrow\;
2\sqrt2\;x=\tfrac32
\;\Longrightarrow\;
x=\frac{3}{4\sqrt2}=\frac{3\sqrt2}{8}.
\]
Then
\[
y=(\sqrt2+1)\,\frac{3\sqrt2}{8}-1
=\frac{3(2+\sqrt2)}8-1
=\frac{6+3\sqrt2-8}8
=\frac{3\sqrt2-2}8.
\]
Thus the two lines \(L\) (hence \(EZ\)) and \(CO\) meet at
\[
P=\Bigl(\tfrac{3\sqrt2}{8},\;\tfrac{3\sqrt2-2}{8}\Bigr).
\]

8.  Collinearity of \(F,M,P\).  Finally we check that \(F\), \(M\), and \(P\) lie on one line.  Compute the “rise over run” from \(F\) to \(P\):
\[
F=\Bigl(\tfrac{\sqrt2-1}2,\;\tfrac{\sqrt2-1}2\Bigr),
\quad
P=\Bigl(\tfrac{3\sqrt2}{8},\;\tfrac{3\sqrt2-2}{8}\Bigr).
\]
Then
\[
x_P-x_F
=\frac{3\sqrt2}{8}-\frac{\sqrt2-1}2
=\frac{3\sqrt2-(4\sqrt2-4)}8
=\frac{4-\,\sqrt2}8,
\quad
y_P-y_F
=\frac{3\sqrt2-2}8-\frac{\sqrt2-1}2
=\frac{2-\,\sqrt2}8.
\]
Hence the slope \(PF\) is
\[
\frac{y_P-y_F}{x_P-x_F}
=\frac{\,2-\sqrt2\,}{\,4-\sqrt2\,}.
\]
On the other hand
\[
M=\Bigl(\tfrac{2+\sqrt2}4,\;\tfrac{\sqrt2}4\Bigr)
\]
and a similar computation shows
\[
x_M-x_F=\frac{4-\sqrt2}4,
\quad
y_M-y_F=\frac{2-\sqrt2}4,
\]
so the slope \(FM\) is again
\[
\frac{\,2-\sqrt2\,}{\,4-\sqrt2\,}.
\]
Therefore
\[
\text{slope}(PF)=\text{slope}(FM),
\]
so \(P\) lies on the line \(FM\).

9.  Conclusion.  We have shown
\[
P=EZ\cap CO
\quad\text{and}\quad
P\in FM.
\]
Hence the three lines \(EZ,\,CO,\,FM\) concur at the single point \(P\), as required.  ∎