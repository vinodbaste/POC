I'll work through this systematically, using the given conditions to analyze each statement.

## Setting up the problem

Let me denote:
- $V = \text{vol}(ABCD)$ (volume of the tetrahedron)
- $S_1, S_2, S_3, S_4$ = areas of faces $BCD, ABC, ACD, ADB$ respectively
- $h_A$ = distance from $A$ to plane $BCD$

Since $I$ is the incenter with inradius $r$:
$$V = \frac{1}{3}r(S_1 + S_2 + S_3 + S_4)$$

Also, if we decompose the tetrahedron from $I$:
$$\text{vol}(IABC) = \frac{1}{3}r \cdot S_2, \quad \text{vol}(IACD) = \frac{1}{3}r \cdot S_3, \quad \text{vol}(IADB) = \frac{1}{3}r \cdot S_4$$

## Analyzing Condition (2)

The condition $\frac{\text{vol}(IABC)}{BC} = \frac{\text{vol}(IACD)}{CD} = \frac{\text{vol}(IADB)}{DB}$ becomes:

$$\frac{S_2}{BC} = \frac{S_3}{CD} = \frac{S_4}{DB}$$

Let this common ratio be $k$. Then $S_2 = k \cdot BC$, $S_3 = k \cdot CD$, $S_4 = k \cdot DB$.

For any triangle with area $S$ and one side of length $\ell$, we have $S = \frac{1}{2}\ell h_\ell$ where $h_\ell$ is the altitude to that side.

Thus:
- In $\triangle ABC$: $S_2 = \frac{1}{2} BC \cdot h_{BC}^{ABC}$, so $h_{BC}^{ABC} = 2k$
- In $\triangle ACD$: $S_3 = \frac{1}{2} CD \cdot h_{CD}^{ACD}$, so $h_{CD}^{ACD} = 2k$
- In $\triangle ADB$: $S_4 = \frac{1}{2} DB \cdot h_{DB}^{ADB}$, so $h_{DB}^{ADB} = 2k$

**All three altitudes from $A$ (to sides $BC$, $CD$, $DB$ respectively) equal $2k$.**

## Analyzing Statement (c)

**Statement (c): The distances from $A$ to each of the three lines $BC$, $CD$, and $DB$ are equal.**

The distances from $A$ to the three lines are precisely the altitudes we just calculated. Since all equal $2k$, statement **(c) is TRUE**.

## Analyzing Statement (d)

**Statement (d): The areas of triangles $ABC, ACD, ADB$ are in the ratio $BC : CD : DB$.**

We have $S_2 : S_3 : S_4 = k \cdot BC : k \cdot CD : k \cdot DB = BC : CD : DB$.

Statement **(d) is TRUE**.

## Analyzing Statement (f)

**Statement (f): $AB = AC = AD$.**

The condition that distances from $A$ to lines $BC$, $CD$, $DB$ are equal is necessary but not sufficient for $AB = AC = AD$.

**Counterexample for (f)**: Consider a tetrahedron where $A$ is positioned such that its distances to the three edges $BC$, $CD$, $DB$ are equal, but $AB \neq AC$. We can construct this: place $B, C, D$ in a plane, and let $A$ be at a point equidistant from the three lines. This is possible without $AB = AC = AD$ (the distances to edges differ from distances to vertices).

Statement **(f) is FALSE**.

## Analyzing Statement (g)

**Statement (g): Triangle $ABC$ is isosceles with $AB = AC$.**

This doesn't follow from having equal altitudes in $\triangle ABC, ACD, ADB$ to their respective bases. A triangle can have an altitude of a given length without being isosceles.

Statement **(g) is FALSE**.

## Analyzing Statement (h)

**Statement (h): Triangle $BCD$ is equilateral.**

There's no reason the base triangle $BCD$ must be equilateral. Condition (2) constrains the areas relative to edge lengths, but not the triangle itself.

Statement **(h) is FALSE**.

## Analyzing Statement (a)

**Statement (a): $AI$ is perpendicular to plane $BCD$.**

For this to be true, we'd need $A$ to lie on the line through $I$ perpendicular to plane $BCD$. This follows only if the projection of $A$ onto $BCD$ is directly below/above $I$.

This is **not necessarily true** from our conditions. Counterexample: we can have a tetrahedron satisfying (2) where $AI$ is not perpendicular to $BCD$.

Statement **(a) is FALSE**.

## Analyzing Statement (b)

**Statement (b): The orthogonal projection of $A$ onto plane $BCD$ coincides with the incenter of triangle $BCD$.**

This is a strong claim. Let $H$ be the projection of $A$ onto plane $BCD$. Then $H$ is the point in plane $BCD$ equidistant from the three lines $BC$, $CD$, $DB$ (since distances from $A$ to these lines all equal $2k$).

If $H$ lies on all three altitudes of sides $BC, CD, DB$ at equal perpendicular distance, then $H$ is the incenter of $\triangle BCD$.

Actually, the locus of points equidistant from three lines in a plane (when the lines form a triangle) is indeed the incenter.

Statement **(b) is TRUE**.

## Analyzing Statement (e)

**Statement (e): The point at which the inscribed sphere touches face $BCD$ is the incenter of triangle $BCD$.**

The incenter of a tetrahedron is equidistant from all four faces. The point where the sphere touches face $BCD$ is the foot of the perpendicular from $I$ to plane $BCD$.

From statement (b), we know the projection of $A$ onto plane $BCD$ is the incenter of $\triangle BCD$. For the sphere's tangency point to be the incenter of $\triangle BCD$, we need $I$ to project onto the incenter of $\triangle BCD$.

This is **not necessarily true** unless $I$ projects to the incenter. The tangency point is determined by the perpendicular from $I$, not by $A$.

Statement **(e) is FALSE**.

After careful reconsideration of the geometric constraints and condition (2), the statements that are **necessarily true** are:

$$\boxed{\{c, d, b\}}$$
