# artifact_103

Grading ID: GB-0092  
Problem ID: PB-Advanced-003  
Source: Novel Problem  
IMO Area: Number_Theory

Benchmark item from IMO-GradingBench (Google DeepMind, 2025). Read the problem, the reference solution, the grading guidelines, and the candidate student response. Predict the four-class grade the response would receive from a human IMO grader.

## Problem

Let $ ABC $ be an acute triangle which is not an isosceles.Let $ I $ be the incenter and let $ \omega $ be the circumcircle of $ABC$. Let the intersections of lines $ AI $, $ BI $, and $ CI $ with $ BC $, $ CA $, and $ AB $ be $ D $, $ E $, and $ F $ respectively. Also, let $ \omega_A $ be the circle that lies inside $\angle BAC$, tangent to lines $ AB $ and $ AC $, and internally tangent to the circumcircle $ \omega $ at $ T_A $. Similarly, define $ T_B $ and $ T_C $ for points $ B $ and $ C $ respectively. Prove that there exist two points $ X $ and $ Y $ such that the circumcircles of triangles $ ADT_A $, $ BET_B $, and $ CFT_C $ all pass through $ X $ and $ Y $.

## Reference Solution (for grader's calibration)

Let's define some points as follows:
 \begin{enumerate}
  \item Let $A_1$, $B_1$, and $C_1$ be the points of tangency of the incircle with sides $BC$, $CA$, and $AB$, respectively.
  \item Let $N$ be the midpoint of arc $BC$.
  \item Let $S_A$ be the intersection of line $NT_A$ and side $BC$ (if they are parallel, consider $S_A$ as the point at infinity).
  \item Let $\Gamma_A$, $\Gamma_B$, and $\Gamma_C$ be the circumcircles of triangles $ADT$, $BET$, and $CFT$, respectively.
 \end{enumerate}

 <Step 1> Finding a point on the radical axis of circles $\Gamma_A$, $\Gamma_B$, and $\Gamma_C$

 By the well-known property of Mixtilinear circles, $AT_A$ is isogonal to the line joining the point of tangency of the excircle opposite to vertex $A$ and vertex $A$.
 Similarly, consider the lines joining the points of tangency of the excircles opposite to vertices $B$ and $C$ with their respective vertices. It is well-known that these three lines intersect at a single point, the Nagel point.
 Therefore, lines $AT_A$, $BT_B$, and $CT_C$ also intersect at a single point, which is the isogonal conjugate of the Nagel point. Let this point be $T$.
 Clearly, $T$ lies on segments $AT_A$, $BT_B$, and $CT_C$, and is inside circles $\Gamma_A$, $\Gamma_B$, and $\Gamma_C$.

 Furthermore, by the power of a point theorem with respect to the circumcircle of triangle $ABC$, we have
 \[AT \cdot TT_A = BT \cdot TT_B = CT \cdot TT_C.\]
 Therefore, point $T$ has the same power with respect to circles $\Gamma_A$, $\Gamma_B$, and $\Gamma_C.$

 Hence, to prove the statement, it is sufficient to find another point that has the same power with respect to circles $\Gamma_A$, $\Gamma_B$, and $\Gamma_C$.

 <Step 2> $(A, D, T_A, S_A)$ is cyclic

 $\angle ADS_A = \frac{\angle A}{2} + \angle C = \angle ACN = \angle A T_A SA$, so $(A, D, T_A, S_A)$ is cyclic.

 <Step 3> $\angle AIS_A = 90^\circ$

 This is also a well-known property of Mixtilinear circles. By angle chasing, we can show that the circumcircles of triangles $BIC$ and $NIT_A$ are tangent to each other at point $I$.
 Let's consider the radical axes of these three circles:
 \begin{itemize}
  \item The radical axis of the circumcircles of triangles $BIC$ and $NITA$ is the line passing through $I$ and perpendicular to $AI$.
  \item The radical axis of the circumcircles of triangles $BIC$ and $ABC$ is $BC$.
  \item The radical axis of the circumcircles of triangles $ABC$ and $NITA$ is $NT_A$.
 \end{itemize}
 Therefore, the intersection point $S_A$ of $BC$ and $NT_A$ satisfies $\angle AIS_A = 90^\circ$.

 <Step 4> Inversion with respect to the incircle of triangle $ABC$

 Now, let's invert the figure with respect to the incircle $I$. In particular, let's pay attention to which circle $I$ maps to under this inversion.
 Let $A'$, $B'$, and $C'$ be the images of points $A$, $B$, and $C$ under the inversion. Also, let $D'$ and $S_A'$ be the images of points $D$ and $S_A$ under the inversion.

 Let's investigate the properties of the inverted points.
 Since $DA_1$ is tangent to the circle, $D'$ is the foot of the perpendicular from $A_1$ to $ID$. $A'$ is the midpoint of $B_1C_1$. Finally, since $SA_1$ is tangent to the circle, $S_A'$ is the foot of the perpendicular from $A_1$ to $IS_A$.
 By the conclusion of Step 3, $A_1S_A'$ is parallel to $AI$.
 By the observation from step 2, the inversion of the circumcircle of $ADT_A$ is the circumcircle of triangle $A'S_A'D'$. Similarly, the circumcircles of $B'S_B'E'$ and $C'S_C'F'$ are our desired circles. Let's prove that the three circumcircles pass through two common points.

 <Step 5> The circumcircles of triangles $A'S_A'D', B'S_B'E'$, and $C'S_C'F'$ pass through two common points

 Now, let's consider the figure with respect to triangle $A_1B_1C_1$.

 In triangle $A_1B_1C_1$, point $I$ is the circumcenter. Let $H_1$ be the foot of the perpendicular from $A_1$ to $B_1C_1$.
 Then, points $A'$, $S_A'$, and $D'$ are constructed as follows:
 \begin{itemize}
  \item Point $A'$ is the midpoint of $B_1C_1$.
  \item Point $D'$ is the intersection of the line parallel to $B_1C_1$ passing through $A_1$ and the perpendicular bisector of $B_1C_1$.
  \item Point $S_A'$ is the foot of the perpendicular from $I$ to $AH_1$.
 \end{itemize}
 Through this construction, we can find that the circumcenter $O_A$ of triangle $A'S_A'D'$ lies on the perpendicular bisector of $A'D'$, which is the line $B'C'$.
 Now, let's consider the point $O_A'$ which is the reflection of $O_A$ with respect to the midpoint of $B'C'$.

 <Step 6> $O_A'$ is the circumcenter of triangle $A_1IH_1$

 Since $A'$, $B'$, $C'$, and $H_1$ lie on the nine-point circle of triangle $ABC$, these four points are concyclic. Therefore, quadrilateral $A'H_1 B'C'$ is an isosceles trapezoid, and points $A'$ and $H_1$ are symmetric with respect to the perpendicular bisector of line $B_1 C_1$.
 Furthermore, $A_1$ and $D'$ are symmetric with respect to the perpendicular bisector of line $B'C'$.
 Therefore, triangle $AIH_1$ is the reflection of triangle $A'S_A'D'$ across the perpendicular bisector of line $B'C'$, and the circumcenters $O_A$ and $O_A'$ are also symmetric with respect to each other.

 <Step 7> $O_A, O_B$, and $O_C$ are collinear

 Now, let's define $O_B, O_C, O_B'$, and $O_C'$ similarly, and show that $O_A, O_B$, and $O_C$ are collinear.
 First, let's show that $O_A'$, $O_B'$, and $O_C'$ are collinear. It is sufficient to prove that the circumcircles of triangles $AIH_1$, $BIH_B$, and $C_1IH_C$ have a common radical axis.
 On the other hand, the circumcenter $I$ of $ABC$ and the orthocenter $A_1H_A \cap B_1H_B \cap C_1H_C$ have the same power with respect to these three circumcircles. Therefore, these three circles have a common radical axis. Hence, the centers of these three circles, $O_A'$, $O_B'$, and $O_C'$, are collinear.
 Now, by Menelaus' theorem, we have
 \[\frac{C'O_A' \cdot B'O_C' \cdot A'O_B'}{O_A'B' \cdot O_C'A' \cdot O_B'C'} = 1\]
 \[\frac{C'O_A \cdot B'O_C \cdot A'O_B}{O_AB' \cdot O_CA' \cdot O_BC'} = 1\]
 Therefore, $O_A, O_B$, and $O_C$ are also collinear.

 <Step 8> Circles $\Gamma_A, \Gamma_B$, and $\Gamma_C$ have two common points

 Now, the circles $\Gamma_A, \Gamma_B$, and $\Gamma_C$ are inverted into circles. The centers of these three circles are collinear, as proven earlier. Therefore, these three circles either have a common radical axis or their radical axes are parallel. This property remains true before the inversion.
 However, in Step 1, we found point $T$ that has the same power with respect to these three circles. Therefore, circles $\Gamma_A, \Gamma_B$, and $\Gamma_C$ have a common radical axis.
 Furthermore, since point $T$ lies inside all three circles, this common radical axis intersects each circle at two distinct points. Therefore, the three circles have two common points.

## Grading Guidelines

(Partial)
 1. Showed that $AT_a$, $BT_b, CT_c$ are concurrent (there are many possible solutions).
(Almost)
 1. Verification contains minor mistakes only.

## Candidate Response (to be graded)

Let $\omega$ be the circumcircle of $\triangle ABC$, with center $O$ and radius $R$. Let $\Omega_A, \Omega_B, \Omega_C$ be the circumcircles of triangles $ADT_A, BET_B, CFT_C$ respectively. We want to prove that these three circles share two common points. This is equivalent to proving that the three circles belong to a coaxial pencil of the intersecting type.

A set of circles is coaxial if they share a common radical axis. Our proof will be structured as follows:
1.  We will prove that the circles $\Omega_A, \Omega_B, \Omega_C$ are coaxial.
2.  We will then prove that their common radical axis intersects the circles, which implies they share two distinct real points.

**Part 1: Proving Coaxality**

The coaxality of the three circles is a direct consequence of a theorem by Dao Thanh Oai. We will first state the theorem and then apply it to our problem.

**Dao's Theorem on Coaxial Circles:** Let $P$ be a point in the plane of $\triangle ABC$, and let $DEF$ be its cevian triangle. Let $A', B', C'$ be three points on the circumcircle $\omega$ of $\triangle ABC$. The circumcircles of triangles $ADA'$, $BEB'$, and $CFC'$ are coaxial if and only if the lines $AA'$, $BB'$, and $CC'$ are concurrent.

Let's apply this theorem to our problem configuration:
-   The point $P$ in the theorem corresponds to the incenter $I$ of $\triangle ABC$.
-   The cevian triangle $DEF$ of $I$ is formed by the feet of the angle bisectors on the sides $BC, CA, AB$, which matches the definition in the problem.
-   The points $A', B', C'$ on the circumcircle $\omega$ correspond to the points $T_A, T_B, T_C$.
-   The three circles in the theorem are therefore the circumcircles of $ADT_A, BET_B, CFT_C$, which are exactly the circles $\Omega_A, \Omega_B, \Omega_C$.

Dao's theorem states that these circles are coaxial if and only if the lines $AT_A, BT_B, CT_C$ are concurrent. The concurrency of these three lines is a well-known property of the mixtilinear incircles.

**Theorem on Mixtilinear Incircleges:** The lines connecting the vertices $A, B, C$ to the points of tangency $T_A, T_B, T_C$ of their respective mixtilinear incircles with the circumcircle are concurrent. The point of concurrency is the isogonal conjugate of the Gergonne point, which is also the external center of similitude between the incircle and the circumcircle.

Let's denote this point of concurrency by $S$. Since the lines $AT_A, BT_B, CT_C$ are concurrent at $S$, the condition of Dao's theorem is satisfied. Therefore, the circles $\Omega_A, \Omega_B, \Omega_C$ are coaxial.

Let $\mathcal{L}$ be their common radical axis.

**Part 2: Proving the circles intersect at two distinct points**

Now that we have established that the three circles are coaxial, we need to determine the type of the pencil. A coaxial pencil can be intersecting, tangent, or non-intersecting. The circles intersect at two distinct real points $X$ and $Y$ if and only if the pencil is of the intersecting type. This occurs when their common r

[Note: response truncated to first 3000 characters of 8059]
