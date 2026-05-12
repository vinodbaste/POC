# artifact_70

Competition: USAMO  
Problem ID: USAMO_2011_3  
Year: 2011

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

In hexagon \(ABCDEF\), inscribed in a circle, sides \(AB, CD\) and \(EF\) are all equal to the circumradius. Prove that the midpoints of the other three sides \(BC, DE\) and \(FA\) form an equilateral triangle.

## Candidate Excerpts

### Option A

```text
Step 4.  Midpoint M_1 of BC: at angle (60° + 60° + α)/2 = 60° + α/2.  Similarly M_2 at
60° + α + 60° + β/2 + ... computation gets complex, but by direct angle-counting:
   M_1 is at angle 60° + α/2,
   M_2 is at angle 60° + 60° + α + β/2,
   M_3 is at angle 60° + 60° + 60° + α + β + γ/2.
The pairwise differences: M_2 - M_1 = 60° + α/2 + β/2, M_3 - M_2 = 60° + β/2 + γ/2.
For M_1 M_2 M_3 to be equilateral inscribed on the circle (of midpoints), we need
these arc-differences to be equal: 60° + α/2 + β/2 = 60° + β/2 + γ/2, giving α = γ.
Similarly β = α (from another pair).  So α = β = γ = 60° (using α + β + γ = 180°).
Hence the hexagon has all six sides equal, contradicting the freedom we wanted.
```

### Option B

```text
Step 2.  Let M_1, M_2, M_3 be the midpoints of sides BC, DE, FA.  Since arcs AB, CD, EF
each cover 60° of the circle, the remaining arcs BC, DE, FA cover (360° - 3·60°)/3 = 60°
each, on average — but they need not all be equal.
```

### Option C

```text
Step 1.  Let O be the center of the circumscribed circle.  Since AB = CD = EF = R
(the circumradius), each of the triangles OAB, OCD, OEF is equilateral (two sides equal
to R and the third equal to R).  Hence each of arcs AB, CD, EF subtends a 60° central
angle.
```

### Option D

```text
Step 3.  Place coordinates: let the circle have center O = (0, 0) and radius R = 1.
Place A at angle 0, B at angle 60° (since arc AB is 60°).  The remaining vertices C, D,
E, F are at angles 60° + α, 60° + α + 60°, 60° + α + 60° + β, 60° + α + 60° + β + 60°,
where α and β are the arcs BC and DE respectively.  Constraint: total angle is 360°, so
3 · 60° + α + β + γ = 360°, with γ = arc FA.  Hence α + β + γ = 180°.
```

## Full Candidate Proof

```text
Step 1.  Let O be the center of the circumscribed circle.  Since AB = CD = EF = R
(the circumradius), each of the triangles OAB, OCD, OEF is equilateral (two sides equal
to R and the third equal to R).  Hence each of arcs AB, CD, EF subtends a 60° central
angle.

Step 2.  Let M_1, M_2, M_3 be the midpoints of sides BC, DE, FA.  Since arcs AB, CD, EF
each cover 60° of the circle, the remaining arcs BC, DE, FA cover (360° - 3·60°)/3 = 60°
each, on average — but they need not all be equal.

Step 3.  Place coordinates: let the circle have center O = (0, 0) and radius R = 1.
Place A at angle 0, B at angle 60° (since arc AB is 60°).  The remaining vertices C, D,
E, F are at angles 60° + α, 60° + α + 60°, 60° + α + 60° + β, 60° + α + 60° + β + 60°,
where α and β are the arcs BC and DE respectively.  Constraint: total angle is 360°, so
3 · 60° + α + β + γ = 360°, with γ = arc FA.  Hence α + β + γ = 180°.

Step 4.  Midpoint M_1 of BC: at angle (60° + 60° + α)/2 = 60° + α/2.  Similarly M_2 at
60° + α + 60° + β/2 + ... computation gets complex, but by direct angle-counting:
   M_1 is at angle 60° + α/2,
   M_2 is at angle 60° + 60° + α + β/2,
   M_3 is at angle 60° + 60° + 60° + α + β + γ/2.
The pairwise differences: M_2 - M_1 = 60° + α/2 + β/2, M_3 - M_2 = 60° + β/2 + γ/2.
For M_1 M_2 M_3 to be equilateral inscribed on the circle (of midpoints), we need
these arc-differences to be equal: 60° + α/2 + β/2 = 60° + β/2 + γ/2, giving α = γ.
Similarly β = α (from another pair).  So α = β = γ = 60° (using α + β + γ = 180°).
Hence the hexagon has all six sides equal, contradicting the freedom we wanted.

Step 5.  Therefore the only way M_1 M_2 M_3 can be equilateral is for the hexagon to be
regular, but the problem assumes a general inscribed hexagon — contradiction.  So the
statement is false in general.  But the problem claims it's true.  Resolution: the
midpoints are NOT necessarily on the same circle, so the "inscribed equilateral" condition
doesn't directly translate to equal arc-differences.
```

## Reviewer Note

In Step 4, the proof applies a criterion that holds for triangles inscribed in a circle (equal arc-differences ⇒ equilateral) to the midpoints M_1, M_2, M_3, which are NOT on the original circumcircle. The midpoints of chords of a circle lie on a smaller circle (specifically a circle of half the chord's apothem distance from center), but they are not on the circumcircle. The proof's application of the "equal arcs imply equilateral inscribed triangle" criterion to M_1, M_2, M_3 is a scope violation: the criterion is valid for points on the same circle, not for midpoints of chords. The correct approach is to compute the Cartesian coordinates of M_1, M_2, M_3 (each lies inside the circle, not on it) and check the distances |M_1 M_2|, |M_2 M_3|, |M_3 M_1| directly.
