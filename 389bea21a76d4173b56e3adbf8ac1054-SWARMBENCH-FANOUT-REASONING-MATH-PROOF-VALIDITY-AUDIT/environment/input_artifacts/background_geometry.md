# Domain Background: Geometry Proof Evaluation

This reference covers the mathematical theory, common proof techniques, and evaluation criteria relevant to olympiad geometry problems. Sub-agents auditing **proof_02**, **proof_04**, **proof_09**, and **proof_16** should read this document before evaluating their assigned proof.

---

## Part I: Euclidean Geometry Fundamentals

### 1.1 Angles and Circles

**Inscribed angle theorem:** An angle inscribed in a circle is half the central angle that subtends the same arc. If A, B, C lie on a circle with center O and arc BC (not containing A), then ∠BAC = (1/2)·∠BOC.

**Consequence:** Angles inscribed in the same arc are equal. If A, A' both lie on the same arc BC (i.e., same side), then ∠BAC = ∠BA'C.

**Tangent-chord angle:** The angle between a tangent to a circle at point P and a chord PQ equals the inscribed angle in the alternate segment.

**Power of a point:** For a point P and circle ω, the power of P is |PO|² - r² (where O is center, r is radius). If a line through P meets ω at X and Y, then PX · PY = power of P (with sign conventions for interior/exterior). For two chords through P intersecting circle: PA · PB = PC · PD.

### 1.2 Cyclic Quadrilaterals

Four points A, B, C, D are concyclic if and only if ∠ABC + ∠ADC = 180° (opposite angles of cyclic quadrilateral are supplementary). Equivalently, ∠ABD = ∠ACD (angles subtending the same arc AD from the same side).

**Ptolemy's theorem:** For cyclic quadrilateral ABCD: AC · BD = AB · CD + AD · BC.

### 1.3 Directed Angles Modulo 180°

In olympiad geometry, **directed angles** (angles mod 180°) are often more convenient than signed angles because they avoid case distinctions based on the configuration.

**Definition:** ∠(ℓ, m) denotes the angle from line ℓ to line m, measured mod 180°. Equivalently, for points A, B, C: ∠ABC denotes the directed angle from ray BA to ray BC, mod 180°.

**Key property:** A, B, C, D are concyclic if and only if ∠ACB = ∠ADB (directed angles mod 180°). This eliminates the need to specify which arc or which side.

**Angle chasing rules:**
- ∠(AB, CD) = -∠(CD, AB)
- ∠(AB, CD) + ∠(CD, EF) = ∠(AB, EF)
- If O is the center: ∠AOB = 2∠ACB (directed angles, where C is on the major arc)

**Common error in directed angle proofs:** Failing to consistently use directed angles — mixing signed and unsigned angles within the same argument. If a step uses ∠ACB = 90° and another uses ∠ACB = -90° without acknowledging they represent the same directed angle, the proof is internally inconsistent.

**Evaluation criterion:** In an angle-chase proof, every angle equality claimed between inscribed angles must follow from concyclicity of four points. If the claim "∠PAQ = ∠PBQ" is made, verify that P, A, B, Q are concyclic (or that PQ is a diameter and angles are right angles, etc.). An unjustified angle equality is a first material issue.

### 1.4 Radical Axis and Coaxial Circles

The **radical axis** of two circles ω₁ and ω₂ is the locus of points with equal power with respect to both circles. It is always a line perpendicular to the line through the centers.

**Radical center:** For three circles with pairwise non-parallel radical axes, the three radical axes meet at a single point, the radical center.

**Coaxial circles:** A family of circles sharing a common radical axis. Any two circles in the family have the same radical axis.

### 1.5 Inversion

**Inversion with center O and radius r:** Maps each point P ≠ O to P' on ray OP with OP · OP' = r².

Key properties:
- Circles through O ↔ Lines not through O
- Circles not through O ↔ Circles not through O
- Lines through O ↔ Lines through O
- Angles are preserved (inversion is conformal)
- If P, Q, R, S are concyclic and O is not on their circle, their images P', Q', R', S' are also concyclic (or collinear if O is on the circle)

---

## Part II: Coordinate Geometry and Analytic Methods

### 2.1 Setting Up Coordinates

**Choice of coordinates:** For an isosceles triangle with AB = AC and ∠A = α, convenient choices include:
- A at origin, axis of symmetry along y-axis: A=(0,0), B=(-b, 0), C=(b,0) with apex at (0,h)
- A at origin with one leg along x-axis: A=(0,0), B=(1,0), C=(cos α, sin α)

The second choice places angle A at the origin explicitly and is often more natural.

**Circumcenter computation:** The circumcenter O of triangle ABC is equidistant from A, B, C. For A=(0,0), B=(1,0), C=(cos θ, sin θ) with angle θ = 45°:
- Perpendicular bisector of AB: x = 1/2
- Perpendicular bisector of AC: midpoint of AC is (cos θ/2, sin θ/2), slope of AC is sin θ/cos θ = tan θ, so perpendicular bisector has slope -cot θ and passes through (cos θ/2, sin θ/2)

For θ = 45°: C = (√2/2, √2/2), midpoint = (√2/4, √2/4), perpendicular bisector has slope -1 and equation y - √2/4 = -(x - √2/4), i.e., y = -x + √2/2. Intersecting with x = 1/2: y = √2/2 - 1/2 = (√2-1)/2.

Hence O = (1/2, (√2-1)/2). Verify: |OA|² = 1/4 + (√2-1)²/4 = (1 + 3-2√2)/4 = (4-2√2)/4 = (2-√2)/2. And |OC|² = (√2/2 - 1/2)² + (√2/2 - (√2-1)/2)² = ((√2-1)/2)² + (1/2)² = (3-2√2+1)/4 = (4-2√2)/4. ✓

### 2.2 Finding Circle Intersections

To find where two circles intersect: subtract one equation from the other to get a linear equation (the radical axis), then substitute back.

**Example:** Circle 1: (x-h₁)²+(y-k₁)²=r₁² and Circle 2: (x-h₂)²+(y-k₂)²=r₂². Subtracting: 2(h₂-h₁)x + 2(k₂-k₁)y = r₁²-r₂²+h₂²-h₁²+k₂²-k₁². This is the radical axis — a line.

**Checking collinearity:** Three points P₁, P₂, P₃ are collinear if and only if the vectors P₁P₂ and P₁P₃ are parallel, i.e., the determinant |x₁-x₃, y₁-y₃; x₂-x₃, y₂-y₃| = 0. Equivalently, slopes of P₁P₂ and P₁P₃ are equal.

**Checking concurrence:** Three lines L₁, L₂, L₃ are concurrent if and only if any two of the three pairwise intersection points coincide. In coordinate proofs, one typically finds the intersection P = L₁∩L₂ and then verifies P ∈ L₃.

### 2.3 Line Slope Computations

For points P = (x₁, y₁) and Q = (x₂, y₂) with x₁ ≠ x₂:
slope(PQ) = (y₂-y₁)/(x₂-x₁)

**Rationalization:** When slopes involve √2, rationalize: 1/(√2-1) = (√2+1)/((√2-1)(√2+1)) = (√2+1)/(2-1) = √2+1.

**Perpendicularity:** Lines with slopes m and m' are perpendicular iff mm' = -1. Lines with the same slope are parallel.

**Evaluation criterion for coordinate proofs:** Every arithmetic step (especially with surds like √2) must be correct. A computation error in the coordinates of O, F, E, Z, or P invalidates all subsequent claims that depend on those coordinates. Verify key steps: circumradius formula, circle-intersection radical axis formula, substitution into line equation.

### 2.4 The Circle-Chord Characterization

For a circle ω with center C and radius r, and a line ℓ, the chord of intersection can be found by:
1. Computing the distance from C to ℓ
2. Using the Pythagorean theorem to find half the chord length

For ℓ: ax+by=c, the distance from (h,k) to ℓ is |ah+bk-c|/√(a²+b²).

---

## Part III: Transformational Geometry

### 3.1 Rotations

A rotation by angle θ about center O transforms point P to point P' where:
- |OP'| = |OP|
- ∠POP' = θ (with appropriate orientation convention)

In Cartesian coordinates with center O = (a,b):
x' - a = (x-a)cos θ - (y-b)sin θ
y' - b = (x-a)sin θ + (y-b)cos θ

**Special cases:**
- θ = π (rotation by 180°): P' = 2O - P (point reflection through O)
- θ = π/2: x'-a = -(y-b), y'-b = x-a (90° counterclockwise)
- θ = -π/2: x'-a = y-b, y'-b = -(x-a) (90° clockwise)

**Key property:** Rotation preserves distances and angles. If P maps to P' and Q maps to Q', then |P'Q'| = |PQ| and ∠P'O Q' = ∠POQ.

### 3.2 Common Error: Wrong Rotation Angle

In olympiad problems involving rotations, the rotation angle must be derived from the geometric constraints, not assumed. Common sources of the rotation angle:
- ∠BOC = 2∠BAC for inscribed angles (central angle = twice inscribed angle)
- The angle between two chords meeting at a point
- The supplement of an angle in a polygon

**Evaluation criterion:** If a proof sets up a rotation with angle θ, verify that θ is correctly computed from the given data. An error in θ will cause all subsequent rotation-image relations to be wrong, even if the rotation technique is otherwise correctly applied.

### 3.3 Reflections and Symmetry

A reflection over line ℓ maps each point P to P' such that ℓ is the perpendicular bisector of PP'.

For ℓ: y = mx + b:
If m = 0 (horizontal): P' = (x, 2b-y)
If ℓ is the x-axis: P' = (x, -y)
If ℓ is the y-axis: P' = (-x, y)
General formula: if ℓ is y = mx and we reflect P = (p,q), then P' has coordinates determined by the projection formula.

### 3.4 Homothety (Dilation)

A homothety with center O and ratio k maps P to P' on ray OP with OP' = k·OP. For k < 0, P' is on the opposite ray.

**Property:** Homothety maps circles to circles (same or opposite orientation depending on sign of k). The ratio of radii equals |k|.

---

## Part IV: Concurrence and Collinearity Theorems

### 4.1 Ceva's Theorem

In triangle ABC, let D, E, F be points on sides BC, CA, AB respectively (or their extensions). The lines AD, BE, CF are concurrent (or all parallel) if and only if:

(BD/DC) · (CE/EA) · (AF/FB) = 1

(with signed ratios if points are on extensions).

**Trigonometric form:** AD, BE, CF concur iff (sin∠BAD/sin∠DAC) · (sin∠CBE/sin∠EBA) · (sin∠ACF/sin∠FCB) = 1.

### 4.2 Menelaus's Theorem

Points D on BC, E on CA, F on AB (or extensions) are collinear iff:
(BD/DC) · (CE/EA) · (AF/FB) = -1

(with signed ratios).

### 4.3 Pascal's Theorem

If six points A, B, C, D, E, F lie on a conic (circle, ellipse, parabola, hyperbola), then the three intersection points of opposite sides of hexagon ABCDEF are collinear.

**For circles:** This is a powerful tool for concurrence and collinearity in problems involving multiple points on a circle.

### 4.4 Radical Axis Method for Concurrence

Three circles are coaxial (share a common radical axis) if and only if their three pairwise radical axes are the same line. Three circles with different centers have a unique radical center.

This is sometimes used to prove that three lines (which happen to be radical axes of three circles) are concurrent.

---

## Part V: Geometry of Specific Configurations

### 5.1 Isosceles Triangle with ∠A = 45°

For isosceles triangle ABC with AB = AC = 1 and ∠A = 45°:
- ∠B = ∠C = (180°-45°)/2 = 67.5°
- BC = 2sin(22.5°) ≈ 2 · 0.3827 ≈ 0.765 (using the law of sines or half-angle formula)

In coordinates (A at origin, B=(1,0), C=(cos45°, sin45°) = (√2/2, √2/2)):
- Circumradius R = BC/(2sin∠A) = BC/(2sin45°) = BC/√2
- Alternatively: R = |OA| = √{1/4 + (√2-1)²/4} = √{(2-√2)/2}

### 5.2 Construction with Two Circles: Finding Intersections

When two circles overlap, their intersection is characterized by the radical axis (linear equation). The actual intersection points satisfy both:
1. The linear equation (from subtracting the two circle equations)
2. Either circle's equation (substituting the linear relation back)

This always gives a quadratic with (generically) two solutions. To identify which intersection is which (e.g., "Z on arc BC" vs "E on arc AC"), substitute the candidate points into inequalities that characterize the arcs.

### 5.3 The Foot of the Perpendicular

The foot D of the perpendicular from point C = (cx, cy) to line AB:
- If AB is the x-axis: D = (cx, 0)
- If AB has equation ax+by+c=0: D = C - ((a·cx+b·cy+c)/(a²+b²))·(a,b)

The distance CD = |a·cx+b·cy+c|/√(a²+b²).

### 5.4 Line FM and Point P in Concurrence Proofs

For concurrence of three lines L₁, L₂, L₃:
**Standard approach in coordinates:** Find P = L₁∩L₂ by solving the system of two linear equations. Verify P ∈ L₃ by substituting P's coordinates into L₃'s equation.

**Slope method for collinearity:** For collinearity of points F, M, P, compute slope(FP) and slope(FM) separately (or FM and MP). They must be equal.

---

## Part VI: Combinatorial Geometry

### 6.1 Configurations with Points on Circles

When points are defined on circles (e.g., A_k defined as the k-th point in some sequence), claims that a third point lies on a specific circle must be justified by one of:
- The circle's defining equation being satisfied
- The inscribed angle theorem (finding equal inscribed angles subtending the same arc)
- The power of the point condition being met
- An explicit construction that places the point on the circle

**Support point arguments:** In circle packing and convex hull problems, a "support point" is a point on the boundary of the convex hull. If a construction says "A_k lies on circle ω," the justification must be either geometric (from angle conditions) or algebraic (coordinates satisfy the circle equation), not just asserted.

**Evaluation criterion:** If a proof claims "A_k lies on circle ω" without justification — neither a geometric argument (angle equality, power of point) nor an algebraic check — this is a material gap. The entire subsequent argument that uses A_k ∈ ω fails if this claim is unverified.

### 6.2 Convex Hulls and Support Lines

A convex polygon's boundary consists of support lines: each edge ℓ of the polygon has all polygon vertices on one side (or on ℓ). A point Q is a vertex of the convex hull if and only if no line through Q has all other points strictly on one side.

**In circle arguments:** If a circle ω is internally tangent to a circle Ω, and A_k is defined as the tangent point or a point on ω, saying A_k ∈ Ω requires showing A_k simultaneously lies on ω (by construction) and on Ω (by a separate argument). These are two distinct conditions.

### 6.3 Intersection and Overlap of Circles

Two distinct circles intersect in 0, 1, or 2 points depending on the relationship between the distance d between centers and the radii r₁, r₂:
- d > r₁+r₂: external, 0 intersections
- d = r₁+r₂: externally tangent, 1 intersection
- |r₁-r₂| < d < r₁+r₂: overlapping, 2 intersections
- d = |r₁-r₂|: internally tangent, 1 intersection
- d < |r₁-r₂|: one inside the other, 0 intersections

---

## Part VII: Standard Proof Evaluation Criteria for Geometry

### 7.1 Angle-Chase Proofs

An angle-chase proof establishes a chain of angle equalities, each justified by one of:
- Inscribed angle theorem (angles subtending same arc are equal)
- Tangent-chord angle theorem
- Vertical angles, supplementary angles, etc.
- Parallel line angle relationships (alternate interior, corresponding, co-interior)

**Evaluation criterion:** For EACH angle equality claimed, identify which theorem or rule justifies it. If a claim "∠XYZ = ∠XWZ" is made without specifying that X,Y,Z,W are concyclic (or another justification), it is unjustified. The first unjustified angle equality is the first material issue.

**Directed angle advantage:** Using directed angles mod 180° eliminates the need to distinguish cases (which arc, which side). But it requires every angle equality to be valid as a directed angle equality. If a proof mixes directed and undirected angles, errors can arise.

### 7.2 Coordinate Geometry Proofs

A coordinate proof is valid if and only if:
1. The coordinate setup correctly represents the given geometric configuration
2. Every arithmetic computation is correct
3. The final claim (concurrence, collinearity, etc.) is verified by the stated equalities/checks

**Verification steps:**
- Circumcenter: check it is equidistant from all three vertices
- Intersection points: check they lie on both curves
- Concurrence: check the intersection of two lines lies on the third
- Collinearity: check equal slopes or zero determinant

**Common arithmetic errors with √2:**
- (√2-1)/2: correct, approximately 0.207
- (√2+1)/2: correct, approximately 1.207
- 1/(√2-1) = √2+1 after rationalization
- (√2-1)² = 2-2√2+1 = 3-2√2
- (√2/2)² = 1/2, not 2

### 7.3 Rotation Proofs

**Evaluation criterion:** A rotation proof must:
1. Specify the center, angle, and orientation of the rotation
2. Correctly compute the angle from the given data
3. Correctly identify the image of each relevant point
4. Verify that the image satisfies the claimed property

The rotation angle is typically derived from the angles of the figure. An error in computing the rotation angle (e.g., π instead of the correct angle) will cause the images to be incorrectly identified, invalidating all subsequent claims.

**Warning:** A rotation by angle π is point reflection. This is only valid if the geometric configuration indeed has a 180° rotational symmetry, which must be established from the hypotheses, not assumed.

---

## Part VIII: Extended Examples for Geometry Proof Evaluation

### Example 1: Valid angle-chase

**Claim:** Let ABCD be a cyclic quadrilateral. Then ∠BAC = ∠BDC (since both are inscribed in circle and subtend arc BC from the same side).

**Analysis:** This is CORRECT. Both A and D lie on the same arc (opposite arc BC), so the inscribed angles subtending BC from that arc are equal. ✓

### Example 2: Invalid angle-chase — wrong concyclicity

**Claim:** Let P, Q, R, S be four points with ∠PQR = ∠PSR = 50°. Then P, Q, R, S are concyclic.

**Analysis:** This is BACKWARD. The converse is true: if P,Q,R,S are concyclic, then ∠PQR = ∠PSR. But the claim uses equal angles to conclude concyclicity — this IS valid by the converse of the inscribed angle theorem. So this claim is CORRECT. (Note: The converse holds as long as Q and S are on the same side of PR.)

### Example 3: Unjustified claim in coordinate proof

**Claim:** By direct computation, the circumcircle has equation (x-1/2)²+(y-k)²=R² for appropriate k.

**Missing step:** The value of k must be computed, not just asserted to be "appropriate." Without the explicit formula for k (derived from equating distances to the three vertices), the claim is unsupported.

### Example 4: Slope computation with surds

**Verify:** slope(CO) where C = (√2/2, √2/2) and O = (1/2, (√2-1)/2).

slope = [(√2-1)/2 - √2/2] / [1/2 - √2/2]
     = [(√2-1-√2)/2] / [(1-√2)/2]
     = [-1/2] / [(1-√2)/2]
     = -1/(1-√2)
     = 1/(√2-1)
     = (√2+1)/((√2-1)(√2+1))
     = (√2+1)/(2-1)
     = √2+1 ✓

This is a correct computation. The step 1/(√2-1) = √2+1 requires the rationalization step.

### Example 5: Checking concurrence in coordinate proof

**Method:** Lines L₁: y = (√2+1)x - 1 and L₂: y = 1/2-(√2-1)x.

Intersection: (√2+1)x-1 = 1/2-(√2-1)x
(√2+1+√2-1)x = 3/2
2√2·x = 3/2
x = 3/(4√2) = 3√2/8

y = (√2+1)·3√2/8 - 1 = (3·2+3√2)/8 - 1 = (6+3√2-8)/8 = (3√2-2)/8

Point P = (3√2/8, (3√2-2)/8).

**Checking P on line FM:** F = ((√2-1)/2, (√2-1)/2) and M = ((2+√2)/4, √2/4).

slope(FM) = [√2/4 - (√2-1)/2] / [(2+√2)/4 - (√2-1)/2]
          = [(√2 - 2(√2-1))/4] / [(2+√2 - 2(√2-1))/4]
          = (√2 - 2√2 + 2) / (2+√2-2√2+2)
          = (2-√2) / (4-√2) ✓

slope(FP) = [(3√2-2)/8 - (√2-1)/2] / [3√2/8 - (√2-1)/2]
          = [(3√2-2 - 4(√2-1))/8] / [(3√2 - 4(√2-1))/8]
          = (3√2-2-4√2+4) / (3√2-4√2+4)
          = (2-√2) / (4-√2) ✓

So slope(FP) = slope(FM). F, M, P are collinear. ✓

### Example 6: Missing justification for point on circle

**Claim:** "Since A_k is constructed as the intersection of the supporting line at A_{k-1} with circle ω_k, it lies on circle ω_k."

**Analysis:** By construction, A_k = supporting line ∩ ω_k, so A_k ∈ ω_k. But does A_k ∈ Ω (the larger circle)? That is a SEPARATE claim requiring separate justification. If the proof asserts A_k ∈ Ω without showing either the coordinates of A_k satisfy Ω's equation or an angle/power argument shows A_k ∈ Ω, this is a gap. ✓ Correctly evaluating this requires checking whether the proof provides such a justification.

---

## Part IX: Specific Problem Type Guidance

### 9.1 Concurrence of Three Lines (e.g., ZE, CO, FM)

For a proof that three lines are concurrent, the minimum valid structure is:
1. Find the intersection P of two of the lines
2. Show P lies on the third line

In a coordinate proof, this means:
- Solve the system for two lines to get explicit (x,y) coordinates of P
- Substitute into the equation of the third line and verify the equation holds
- OR: show that the slope from P to one point on the third line equals the slope of the third line

**Evaluation criterion:** If a coordinate proof finds P and claims P lies on line FM "by similar computation," the reader must be able to fill in this computation. If the computation is absent but the conclusion is stated, this is an incomplete but potentially valid proof (minor omission, routine verification). If the computation would actually FAIL (i.e., slope(FP) ≠ slope(FM) due to an arithmetic error earlier), then the entire proof is invalid.

### 9.2 Arcs and Sub-Arc Identification

When problem states "Z lies on arc BC" and "E lies on arc AC," these constraints determine which of the two intersection points of the small circle with the circumcircle is Z and which is E. A proof that just computes the two intersection points without verifying which is on which arc is incomplete.

**Evaluation criterion:** Verify that the proof either:
- Shows explicit coordinates for E and Z and checks which arc each lies on
- Provides a geometric argument (e.g., Z is closer to B than to A, hence on arc BC)
- Notes that the specific identification doesn't affect the concurrence conclusion

### 9.3 Rotation Angle Determination

In a rotation proof for a geometry problem:
1. Identify the center of rotation (often a specific vertex or special point)
2. The angle of rotation comes from the geometry: for example, if two segments subtend equal angles at a common point, the rotation maps one to the other
3. The direction (clockwise/counterclockwise) must be consistent with the configuration

**Checking angle = π (180°):** A rotation by π about a center O maps P to 2O-P (the point symmetric to P through O). This is valid only if the problem's geometric structure has a 180° symmetry. The angle π is correct if:
- The center is the midpoint of some key segment
- Two triangles are identified as centrally symmetric
- Some other explicit π-rotation symmetry is established

If instead the correct angle should be, e.g., π/2, and the proof uses π, then images of all points under the rotation are wrong.

---

## Part X: Evaluation Rubric Summary for Geometry Proofs

1. **Angle equalities:** Every claimed angle equality must cite a theorem (inscribed angle, tangent-chord, parallel lines, vertical angles, or supplementary angles). An unjustified equality is a material issue.

2. **Concyclicity:** Claims that four points are concyclic must be established (angle sum = 180°, equal inscribed angles, power of point = 0, all equidistant from a center).

3. **Arithmetic correctness (for coordinate proofs):** Every calculation with specific coordinates must be verified. An arithmetic error that produces a wrong coordinate invalidates all subsequent claims using that coordinate.

4. **Rotation angle:** In rotation arguments, the angle must be explicitly derived from the given data and correctly computed.

5. **Third point on circle:** A claim that a specific point lies on a circle must be justified either algebraically (satisfies the circle's equation) or geometrically (angle condition, power condition, etc.).

6. **Concurrence conclusion:** The proof must actually establish concurrence, not just set up a rotation/inversion and stop before the final conclusion.

**First material issue identification:** The first place in the proof where one of the above criteria fails — an unjustified claim, a wrong calculation, or a missing verification — is the first material issue to report.


---

## Appendix A: Extended Worked Examples — Geometry Proof Evaluation

### A.1 Angle-Chase Evaluation — 25 Scenarios

**Scenario 1 (Correct).** "Let ABCD be a cyclic quadrilateral. Then ∠DAB + ∠BCD = 180°."
Proof: ∠DAB and ∠BCD are opposite angles of the cyclic quadrilateral. They subtend arcs BCD and DAB respectively (the full circle minus each arc). Since arc(BCD) + arc(DAB) = 360°, and inscribed angles are half their arcs: ∠DAB + ∠BCD = (arc BCD + arc DAB)/2 = 360°/2 = 180°. CORRECT. ✓

**Scenario 2 (Incorrect — invalid concyclicity claim).** "Points P,Q,R,S lie on a circle since ∠PQR = 60° and ∠PSR = 60°."
Assessment: For four points to be concyclic with ∠PQR = ∠PSR, Q and S must be on the SAME SIDE of PR. The claim doesn't specify the configuration. Moreover, just knowing both angles are 60° doesn't by itself prove concyclicity without verifying they subtend the same arc. But actually: by the converse of the inscribed angle theorem, if ∠PQR = ∠PSR and Q,S lie on the same side of PR, then P,Q,R,S are concyclic. Without the same-side condition, this could fail (e.g., Q and S on opposite sides gives ∠PQR + ∠PSR = 180°, so PQRS is cyclic but Q and S are on opposite arcs). So the claim needs the same-side condition explicitly stated.

**Scenario 3 (Correct).** "By the inscribed angle theorem, ∠ACB = ∠ADB since both are inscribed in circle ω and subtend arc AB not containing C and D, where C and D are on the same arc."
CORRECT, assuming the same-arc condition is verified.

**Scenario 4 (Incorrect — direction of implication).** "∠ACB = 90° implies A, C, B lie on a circle with AB as diameter."
Assessment: This is CORRECT — the converse of Thales' theorem. If ∠ACB = 90°, then C lies on the circle with AB as diameter.

**Scenario 5 (Incorrect — wrong tangent-chord formula).** "The angle between tangent t at P and chord PQ equals ∠PRQ where R is any point on the arc PQ not containing the tangent point."
Assessment: The tangent-chord angle equals the inscribed angle in the ALTERNATE segment. So the angle between t and PQ at P equals the inscribed angle in the arc on the OTHER SIDE of PQ from the tangent direction. CORRECT as stated if "alternate segment" is understood.

**Scenario 6 (Correct — directed angle computation).** "∠(AB, CD) = ∠(AB, EF) + ∠(EF, CD) by linearity of directed angles."
CORRECT. Directed angles mod 180° satisfy: ∠(AB,CD) = ∠(AB,EF)+∠(EF,CD) for any line EF. This is just the additive property of angles.

**Scenario 7 (Incorrect — mixing directed and undirected).** "∠BAC = 30° and ∠BDC = 150°, so A,B,C,D are NOT concyclic."
Assessment: Using directed angles mod 180°: ∠BAC and ∠BDC as directed angles: 30° and 150° are NOT congruent mod 180° (since 150° = 180°-30° and directed angle differences are taken mod 180°, 30° ≠ 150° mod 180°... wait: 150° mod 180° = 150°, and 30° mod 180° = 30°. These differ, so in directed angle sense, A,B,C,D are not concyclic. But in undirected sense: ∠BAC + ∠BDC = 30°+150° = 180°, so opposite angles of quadrilateral ABCD sum to 180°, meaning ABCD IS cyclic. The issue: are A and D on the same side of BC? If ∠BAC = 30° and ∠BDC = 30° they're on the same side (concyclic). If ∠BAC = 30° and ∠BDC = 150° = 180°-30°, they're on opposite sides of BC, and the QUADRILATERAL ABCD is cyclic (opposite angles sum to 180°). CORRECT — A,B,C,D ARE concyclic.

**Scenario 8 (Incorrect — wrong power of point formula).** "For point P outside circle with tangent PA and secant PBC: PA² = PB · PC."
CORRECT (power of a point for external point). PA² = PB·PC. ✓

**Scenario 9 (Incorrect — wrong power formula for internal point).** "For point P inside circle with chords AB and CD through P: PA·PB = PC·PD."
CORRECT. For intersecting chords, PA·PB = PC·PD (both equal the power of P). ✓

**Scenario 10 (Incorrect — sign error in radical axis).** "The radical axis of two circles is where they have equal power, so the equation of the radical axis is obtained by adding the circle equations."
FIRST MATERIAL ISSUE: The radical axis is obtained by SUBTRACTING the circle equations (not adding). Subtracting: (x-h₁)²+(y-k₁)²-r₁² = (x-h₂)²+(y-k₂)²-r₂² gives a linear equation. Adding gives a quadratic (the "coaxial" circle through their intersection points). ✓ Subtraction gives the radical axis.

### A.2 Coordinate Geometry Verification — 20 Scenarios

**Scenario C1 (Correct).** "For A=(0,0), B=(1,0), C=(√2/2, √2/2) with ∠A=45°: |AB|=1, |AC|=√(1/2+1/2)=1. Triangle is isosceles with AB=AC=1."
Check: |AC| = √((√2/2)²+(√2/2)²) = √(1/2+1/2) = √1 = 1. ✓ AB=AC=1. ✓

**Scenario C2 (Correct).** "Circumcenter O of A=(0,0), B=(1,0), C=(√2/2,√2/2): O lies on x=1/2 (perpendicular bisector of AB)."
Check: Midpoint of AB is (1/2,0). AB is horizontal, so perpendicular bisector is vertical: x=1/2. ✓

**Scenario C3 (Correct).** "Perpendicular bisector of AC (from A=(0,0) to C=(√2/2,√2/2)): midpoint is (√2/4, √2/4), slope of AC is 1, so perp bisector has slope -1 and equation y-√2/4 = -(x-√2/4), i.e., y = -x+√2/2."
Check: slope of AC = (√2/2-0)/(√2/2-0) = 1. ✓ Perp slope = -1. ✓ Through (√2/4,√2/4): y-√2/4 = -(x-√2/4) → y = -x+√2/4+√2/4 = -x+√2/2. ✓

**Scenario C4 (Correct).** "Intersection of x=1/2 and y=-x+√2/2: y = -1/2+√2/2 = (√2-1)/2. So O=(1/2,(√2-1)/2)."
Check: substitute x=1/2: y = -1/2+√2/2 = (√2-1)/2. ✓

**Scenario C5 (Correct).** "Verification |OA|²=|OB|²=|OC|²: |OA|²=(1/2)²+((√2-1)/2)²=(1+(√2-1)²)/4=(1+3-2√2)/4=(4-2√2)/4=(2-√2)/2. ✓"
Detailed check: (√2-1)² = 2-2√2+1 = 3-2√2. (1+(3-2√2))/4 = (4-2√2)/4 = (2-√2)/2. ✓
|OB|²=(1/2-1)²+((√2-1)/2)²=1/4+(3-2√2)/4=(4-2√2)/4=(2-√2)/2. ✓
|OC|²=(1/2-√2/2)²+((√2-1)/2-√2/2)²=((1-√2)/2)²+((√2-1-√2)/2)²=((1-√2)²+1)/4=(3-2√2+1)/4=(4-2√2)/4. ✓

**Scenario C6 (Incorrect — arithmetic error).** "D = foot of perpendicular from C=(√2/2,√2/2) to AB (x-axis): D = (√2/2, 0). CD = distance from C to x-axis = √2/2. Circle with center C, radius CD: (x-√2/2)²+(y-√2/2)² = 2." 
INCORRECT: CD = √2/2 so r = √2/2, r² = 1/2. The circle equation should be (x-√2/2)²+(y-√2/2)² = 1/2, NOT 2.

**Scenario C7 (Correct).** "F = intersection of y=x with (x-√2/2)²+(y-√2/2)²=1/2: substitute y=x to get 2(x-√2/2)²=1/2, (x-√2/2)²=1/4, x=√2/2±1/2. The internal point on segment AC is x=(√2-1)/2 (since (√2+1)/2 > √2/2 = |C|, would be outside AC)."
Check: √2/2 ≈ 0.707. (√2+1)/2 ≈ 1.207 > 0.707, outside [0,√2/2]. (√2-1)/2 ≈ 0.207 ∈ [0,√2/2]. ✓ So F = ((√2-1)/2, (√2-1)/2). ✓

**Scenario C8 (Correct).** "Subtracting circumcircle equation from small circle equation gives radical axis: 2(√2/2-1/2)x+2(√2/2-(√2-1)/2)y = constant."
More explicitly: circumcircle: (x-1/2)²+(y-(√2-1)/2)² = (2-√2)/2. Small circle: (x-√2/2)²+(y-√2/2)² = 1/2.
Expand both, subtract:
Circumcircle: x²-x+1/4+y²-(√2-1)y+(√2-1)²/4 = (2-√2)/2.
Small circle: x²-√2x+1/2+y²-√2y+1/2 = 1/2.
Subtract: (-1+√2)x+(-(√2-1)+√2)y+(1/4+(3-2√2)/4-1/2-1/2) = (2-√2)/2-1/2.
= (√2-1)x+(1)y+... let me redo this carefully.

Expanding circumcircle: x²-x+1/4+y²-(√2-1)y+(3-2√2)/4=(2-√2)/2.
Expanding small circle: x²-√2x+1/2+y²-√2y+1/2=1/2.

Subtract (small - circ):
(-√2+1)x+(-√2+√2-1)y+(1/2+1/2-1/4-(3-2√2)/4)=(1/2-(2-√2)/2).

(-√2+1)x+(-1)y+(1-1/4-(3-2√2)/4)=(1/2-1+√2/2).

(1-√2)x-y+(4/4-1/4-(3-2√2)/4)=(√2/2-1/2).

(1-√2)x-y+((4-1-3+2√2)/4)=(√2-1)/2.

(1-√2)x-y+(2√2/4)=(√2-1)/2.

(1-√2)x-y+(√2/2)=(√2-1)/2.

(1-√2)x-y=((√2-1)/2-√2/2)=(-1/2).

(1-√2)x-y=-1/2.

Or: (√2-1)x+y=1/2. ✓ Matches the line y=1/2-(√2-1)x. ✓

**Scenario C9 (Correct).** "Intersection of y=(√2+1)x-1 and y=1/2-(√2-1)x:"
(√2+1)x-1=1/2-(√2-1)x
(√2+1+√2-1)x=3/2
2√2x=3/2, x=3/(4√2)=3√2/8.
y=(√2+1)·3√2/8-1=(3·2+3√2)/8-1=(6+3√2-8)/8=(3√2-2)/8.
P=(3√2/8,(3√2-2)/8). ✓

**Scenario C10 (Correct).** "Slope of FM: F=((√2-1)/2,(√2-1)/2), M=((2+√2)/4,√2/4)."
Δx=(2+√2)/4-(√2-1)/2=(2+√2-2√2+2)/4=(4-√2)/4.
Δy=√2/4-(√2-1)/2=(√2-2√2+2)/4=(2-√2)/4.
slope=(2-√2)/(4-√2). ✓

**Scenario C11 (Correct).** "Slope of FP: F=((√2-1)/2,(√2-1)/2), P=(3√2/8,(3√2-2)/8)."
Δx=3√2/8-(√2-1)/2=3√2/8-(4√2-4)/8=(3√2-4√2+4)/8=(4-√2)/8.
Δy=(3√2-2)/8-(√2-1)/2=(3√2-2-4√2+4)/8=(2-√2)/8.
slope=(2-√2)/(4-√2). ✓ Same as slope FM, confirming collinearity. ✓

### A.3 Rotation and Transformation — 15 Scenarios

**Scenario R1 (Incorrect — wrong rotation angle).** "Rotate triangle ABC by π about midpoint M of BC. This maps B↦C and C↦B, and A↦A'."
Check: Rotation by π about M: M is midpoint of BC, so B↦C and C↦B ✓. A maps to the point A' with M=(A+A')/2, so A'=2M-A. If M is NOT the midpoint of AA', then A'≠A.

**Scenario R2 (Correct).** "If rotating by angle θ about center O maps X to X' and Y to Y', then ∠XOY = ∠X'OY' = θ and |OX|=|OX'|, |OY|=|OY'|, |XY|=|X'Y'|."
CORRECT. Rotations preserve distances and angles between any two points. ✓

**Scenario R3 (Incorrect — wrong rotation angle in geometry proof).** "In triangle ABC with ∠A=45°, rotate by angle π about the circumcenter O."
Assessment: Rotation by π about O maps each point P to 2O-P (point symmetry). This maps A to the antipode A* of A on the circumcircle. The angle ∠A=45° does NOT imply a π-rotation is the right transformation. The rotation angle should be ∠BOC = 2∠BAC = 90° (central angle theorem), NOT π=180°.

**Scenario R4 (Correct).** "The rotation by ∠BOC = 2∠BAC about O maps arc BC to arc BC."
Central angle ∠BOC = 2·∠BAC (inscribed angle theorem). Rotation by ∠BOC about O: this is the rotation that "moves along the circle" by the arc BC. Points ON the circle would be mapped to other points on the circle. This is correct for the standard rotation in circle geometry.

**Scenario R5 (Incorrect — incorrect images).** "Rotation by π/2 about origin maps (a,b) to (-b,a)." 
Check: Rotation by π/2 counterclockwise: x'=x·cos(π/2)-y·sin(π/2)=-y, y'=x·sin(π/2)+y·cos(π/2)=x. So (a,b)↦(-b,a). ✓ CORRECT.

**Scenario R6 (Correct).** "Rotation by π about O=(h,k) maps P=(x,y) to P'=(2h-x, 2k-y)."
x' = (x-h)cos(π)-(y-k)sin(π)+h = -(x-h)+h = 2h-x. ✓
y' = (x-h)sin(π)+(y-k)cos(π)+k = -(y-k)+k = 2k-y. ✓

**Scenario R7 (Incorrect — missing case in rotation).** "There are two possible rotation angles: θ and -θ. The proof only checks θ."
If the problem has a reflection symmetry (equilateral triangle, etc.), both θ and -θ (clockwise and counterclockwise) might be relevant. A proof that only checks one rotation may miss solutions or draw wrong conclusions.

### A.4 Circle Geometry Patterns — 15 Scenarios

**Scenario Ci1 (Correct — Ptolemy application).** "For cyclic quadrilateral ABCD: AC·BD = AB·CD + AD·BC."
PTOLEMY'S THEOREM. ✓

**Scenario Ci2 (Correct — inversion application).** "Inversion with center P and radius r maps circle Γ not through P to another circle Γ' (not through P). The image of lines through P are lines through P."
CORRECT. Inversion swaps circles not through P with circles not through P, and swaps circles through P with lines not through P. ✓

**Scenario Ci3 (Incorrect — wrong inversion formula).** "Inversion with center O and radius r maps P=(a,b) to P'=(a/r², b/r²)."
INCORRECT. Inversion maps P to P' on ray OP with OP·OP'=r². If P=(a,b), then |OP|=√(a²+b²) and the image P'= (r²/(a²+b²))·(a,b). So P'=(r²a/(a²+b²), r²b/(a²+b²)). The formula (a/r², b/r²) is wrong.

**Scenario Ci4 (Correct).** "For a circle ω with center O and radius R, and a chord PQ, the perpendicular from O bisects PQ."
CORRECT. The perpendicular from the center to a chord always bisects the chord (by symmetry). ✓

**Scenario Ci5 (Correct).** "Two circles are internally tangent at T if and only if their centers O₁,O₂ and T are collinear (T between O₁ and O₂ for external tangency, T on the extension for internal tangency)."
CORRECT for tangency. For internal tangency (one circle inside the other): |O₁O₂| = |r₁-r₂| and the tangent point T lies on segment O₁O₂ (extended if needed). ✓

### A.5 Collinearity and Concurrence Patterns

**Pattern Col1 (Correct).** "Three points A=(x₁,y₁), B=(x₂,y₂), C=(x₃,y₃) are collinear iff the matrix [[x₁,y₁,1],[x₂,y₂,1],[x₃,y₃,1]] has determinant 0."
CORRECT. The determinant condition: x₁(y₂-y₃)+x₂(y₃-y₁)+x₃(y₁-y₂)=0. ✓

**Pattern Con1 (Correct).** "Lines L₁: a₁x+b₁y=c₁, L₂: a₂x+b₂y=c₂, L₃: a₃x+b₃y=c₃ are concurrent iff their system has a solution, i.e., det([[a₁,b₁,c₁],[a₂,b₂,c₂],[a₃,b₃,c₃]])=0."
CORRECT. The three lines meet at a single point iff the 3×3 determinant with the line equation coefficients vanishes. ✓

**Pattern Con2 (Ceva's theorem check).** For triangle ABC with D on BC, E on CA, F on AB: AD, BE, CF concurrent iff (BD/DC)·(CE/EA)·(AF/FB)=1 (Ceva's theorem with signed ratios).

**Pattern Col2 (Slope method).** Points P,Q,R collinear iff slope(PQ)=slope(QR). Requires Q≠P and Q≠R and Q not at infinity.

---

## Appendix B: Competition-Specific Geometry Notes

### B.1 BMOSL Geometry Problems

BMOSL (British Mathematical Olympiad Shortlist) geometry problems typically involve:
- Cyclic quadrilaterals and concyclic points
- Angle chasing with directed angles
- Coordinate geometry for construction verification
- The olympiad standard: all steps must be justified, but "standard facts" (inscribed angle theorem, power of a point) can be cited without re-proof

### B.2 USAMO Geometry Problems

USAMO geometry problems are generally harder and may require:
- Projective geometry (cross-ratio, harmonic ranges)
- Advanced circle theorems (Miquel's theorem, radical axes)
- Sophisticated inversion arguments
- Rigorous handling of degenerate cases

### B.3 Evaluation Standard for Competition Geometry

At competition level, the following are considered "standard" and do NOT need proof:
- Inscribed angle theorem
- Power of a point
- Ceva's theorem and Menelaus's theorem
- Basic trigonometric identities (law of sines, law of cosines)
- Ptolemy's theorem

The following DO need justification even if "standard":
- That specific points are concyclic (must establish which condition holds)
- That a point lies on a specific circle (must verify one of the conditions)
- That a rotation maps one specific point to another (must verify distance and angle)

---

## Appendix C: Extended Reference — Angles in Complex Numbers

For geometry in the complex plane, a point P corresponds to complex number z_P. Key facts:

**Rotation:** Rotation by angle θ about origin multiplies by e^{iθ}.

**Reflection:** Reflection over real axis: z ↦ z̄. Reflection over line through origin at angle α: z ↦ e^{2iα}z̄.

**Collinearity:** A, B, C collinear iff (C-A)/(B-A) is real.

**Concyclicity:** A, B, C, D concyclic (or collinear) iff (A-C)(B-D)/((A-D)(B-C)) is real (cross-ratio is real).

**Angle:** Directed angle ∠(AB,AC) = arg((C-A)/(B-A)) mod π.

These formulas provide an algebraic framework for verifying geometric claims. When a coordinate proof is too computational, complex number methods can simplify.

---

*End of Geometry Background Reference*


---

## Appendix D: Extended Geometry Problem Patterns

### D.1 Angle-Chase Reference — Additional Patterns

**AC1 (Directed angle formula).** For points A,B,C,D with ABCD concyclic: angle(AC,BC) = angle(AD,BD) as directed angles mod 180 degrees. This is the key rule for angle chasing.

**AC2 (Central angle rule).** Central angle = 2 * inscribed angle subtending same arc. angle(AOB) = 2 * angle(ACB) where O is center and C is on the circle.

**AC3 (Tangent-chord angle).** Angle between tangent at P and chord PQ equals angle subtended by arc PQ in the alternate segment.

**AC4 (Alternate segment theorem).** If T is on circle omega and l is tangent to omega at T, and AB is a chord, then angle(l, AT) = angle(ABT) where the angle is in the alternate segment.

**AC5 (Cyclic polygon).** In a cyclic polygon with n sides, the sum of alternating exterior angles = 180 degrees. For cyclic quadrilateral: opposite angles sum to 180 degrees.

### D.2 Coordinate Computation Reference — Standard Formulas

**Distance formula:** |PQ|^2 = (x_Q - x_P)^2 + (y_Q - y_P)^2.

**Midpoint formula:** M = ((x_P+x_Q)/2, (y_P+y_Q)/2).

**Line through P=(x_1,y_1) and Q=(x_2,y_2):** (y-y_1)/(x-x_1) = (y_2-y_1)/(x_2-x_1) if x_1 != x_2. Or: (x_2-x_1)(y-y_1) = (y_2-y_1)(x-x_1).

**Circumcenter:** For triangle with vertices A,B,C, the circumcenter O satisfies |OA|=|OB|=|OC|. Found by intersecting perpendicular bisectors of any two sides.

**Circumradius formula:** R = |AB|/(2*sin(angle(ACB))) by law of sines.

**Standard surds:**
- sqrt(2) ≈ 1.41421
- sqrt(2)/2 ≈ 0.70711
- sqrt(2)-1 ≈ 0.41421
- sqrt(2)+1 ≈ 2.41421
- (sqrt(2)-1)/2 ≈ 0.20711
- (sqrt(2)+1)/2 ≈ 1.20711
- (3*sqrt(2)-2)/8 ≈ 0.28033
- 3*sqrt(2)/8 ≈ 0.53033

These approximate values help verify that computed points are in expected relative positions.

### D.3 Rotation Proof Methodology

**Step-by-step rotation proof structure:**

1. **Identify rotation center:** Usually a vertex, circumcenter, or special point.
2. **Determine rotation angle:** From the geometric data (e.g., central angle, polygon angle).
3. **Compute images:** Use rotation formula or geometric argument.
4. **Establish claimed equalities:** Show the image of a specific segment/angle equals another.
5. **Conclude the geometric claim:** (concurrence, collinearity, etc.) from the rotation.

**Rotation angle errors are common.** The angle is typically:
- pi/n for regular n-gon
- 2*angle_A for central angle at vertex A
- Angle of some inscribed figure

If the proof states angle = pi without deriving this from the problem, check whether the configuration really has 180-degree rotational symmetry.

### D.4 Circle Tangency and Intersection Patterns

**Internal tangency:** Two circles internally tangent at T: centers O1, O2 with |O1O2| = |r1-r2|. The tangent at T is the common internal tangent.

**External tangency:** |O1O2| = r1+r2. Tangent point T lies on segment O1O2.

**Radical axis of two intersecting circles:** If they intersect at P and Q, the radical axis is line PQ.

**Finding angle subtended by chord at center:** If chord has length c in circle of radius r: angle = 2*arcsin(c/(2r)).

### D.5 Trigonometric Identities in Geometry

**Law of sines:** a/sin(A) = b/sin(B) = c/sin(C) = 2R.

**Law of cosines:** c^2 = a^2+b^2-2ab*cos(C).

**Extended law of sines:** a = 2R*sin(A) where R is circumradius.

**Area formula:** [ABC] = (1/2)ab*sin(C) = (abc)/(4R).

**Stewart's theorem:** For cevian d from A to side BC at point D with BD=m, DC=n: b^2*m+c^2*n = a(d^2+mn).

**Ptolemy (generalized):** For cyclic ABCD: AC*BD = AB*CD + AD*BC.

### D.6 Combinatorial Geometry Patterns

**Support line:** A line l is a support line of convex set K at point p in K if l contains p and K lies entirely in one closed half-plane bounded by l.

**Support point:** A point p on the boundary of convex K is a support point if there exists a support line at p.

**Evaluation criterion for support point arguments:** A claim that "point A_k is a support point" must be substantiated. Options:
- Show A_k is on the boundary of the convex hull
- Show there exists a support line at A_k
- Use the definition directly (A_k is on a tangent line with all other points on one side)

If a proof claims A_k lies on a specific circle because "it would be a support point otherwise," this reasoning is BACKWARDS unless the support property has been established first.

**Inscribed polygon in circle:** A polygon inscribed in circle omega has all vertices on omega. A point P lies on omega iff |P - O| = r (where O is center, r is radius).

**Point on circle verification methods:**
1. Show |P-O|^2 = r^2 (coordinate check)
2. Show ∠PAQ = ∠POQ/2 for some chord AQ (inscribed angle)
3. Show the power of P with respect to omega equals 0

### D.7 Proof of Concurrence — Methods

**Ceva's theorem:** In triangle ABC with cevians AD, BE, CF (D on BC, E on CA, F on AB): concurrent iff (BD/DC)*(CE/EA)*(AF/FB) = 1.

**Radical axis:** Three radical axes of three circles are concurrent at the radical center.

**Perspective triangles:** Triangles ABC and A'B'C' are perspective from a point iff AA', BB', CC' are concurrent (lines through corresponding vertices meet at one point).

**Coordinate method:** Find intersection of two lines; verify on third.

**Vector method:** Express each line as P = A + t*(B-A) and solve for t. Three lines concurrent iff the system is consistent.

### D.8 Special Lines and Points

**Euler line:** In any non-equilateral triangle, the circumcenter O, centroid G, and orthocenter H are collinear. OG:GH = 1:2.

**Nine-point circle:** The midpoints of sides, feet of altitudes, and midpoints of segments from vertices to orthocenter all lie on one circle (nine-point circle) of radius R/2.

**Simson line:** For a point P on the circumcircle of triangle ABC, the projections of P onto the sides of ABC are collinear (Simson line).

**Polar-pole:** For a circle omega with center O and radius r, the polar of point P (with respect to omega) is the line perpendicular to OP at the inverse point of P.

*End of Geometry Extended Appendix*
