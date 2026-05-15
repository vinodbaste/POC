I need to carefully analyze each statement given the two hypotheses about tetrahedron ABCD.

## Setting Up the Framework

**Understanding Hypothesis 2:** The inscribed sphere touches face BCD at a point, and the tetrahedra IABC, IACD, IADB share vertex I with the three faces containing A.

The volume of IXYZ where XYZ is a face equals (1/3)·Area(XYZ)·r, since I is at distance r from each face.

So:
- vol(IABC) = (1/3)·[ABC]·r
- vol(IACD) = (1/3)·[ACD]·r  
- vol(IADB) = (1/3)·[ADB]·r

**Hypothesis 2 becomes:**
$$\frac{[ABC]}{BC} = \frac{[ACD]}{CD} = \frac{[ADB]}{DB}$$

Since [ABC] = (1/2)·BC·h_A(BC) where h_A(BC) is the distance from A to line BC, we get:
$$\frac{(1/2)·BC·d(A,BC)}{BC} = \frac{(1/2)·CD·d(A,CD)}{CD} = \frac{(1/2)·DB·d(A,DB)}{DB}$$

**This simplifies to:** $d(A, BC) = d(A, CD) = d(A, DB)$

So hypothesis 2 is equivalent to: **A is equidistant from lines BC, CD, DB.**

This means **(c) is necessarily true** — immediately, by the above.

## Analyzing What "Equidistant from BC, CD, DB" Means

The locus of points equidistant from lines BC and CD lies on planes bisecting the dihedral-like angles. The point equidistant from all three sides BC, CD, DB of triangle BCD (measuring distance to the lines, not just within the plane) lies on a line through the incenter of BCD perpendicular to plane BCD — **but only if** the projection onto plane BCD is the incenter of BCD.

Let me be precise. Let P be the projection of A onto plane BCD. The distance from A to line BC equals $\sqrt{d(P,BC)^2 + h^2}$... wait, no. The distance from a point A to a line BC is the minimum distance. If we write A = P + h·**n** where P is in plane BCD and **n** is the unit normal, then:

$$d(A, BC)^2 = d(P, BC)^2 + h^2 \cdot \sin^2\theta$$

where θ is the angle between **n** and line BC... Actually, $d(A,\ell)^2 = d(P,\ell)^2 + h^2\sin^2\angle(\mathbf{n}, \ell) $... 

More carefully: $d(A,BC)^2 = |AP'|^2$ where P' is foot on BC. We have $d(A,BC)^2 = d(P,BC)^2 + h^2$ only if **n** ⊥ BC. In general, for line BC with direction **u**: $d(A,BC)^2 = d(P,BC)^2 + h^2(1 - (\mathbf{n}\cdot\mathbf{u})^2)$. Since **n** ⊥ plane BCD and BC lies in plane BCD, **n**·**u** = 0, so indeed:

$$d(A, BC)^2 = d(P, BC)^2 + h^2$$

where h = height of A above BCD. Similarly for CD and DB. Since h is the same for all three lines:

$$d(A,BC) = d(A,CD) = d(A,DB) \iff d(P,BC) = d(P,CD) = d(P,DB)$$

**Therefore P is the incenter of triangle BCD** (using the acute dihedral angle condition to ensure it's interior).

This proves **(b) is necessarily true**.

## Now Checking Each Statement

**(a) AI perpendicular to BCD?**

AI is perpendicular to BCD iff I lies on the vertical line through P (the incenter of BCD). The incenter I lies on this vertical line iff... The incenter is located at distances from all four faces equal to r. Let me check if I must lie above the incenter of BCD.

The incenter I satisfies: distance from I to plane BCD = r, and distance from I to planes ABC, ACD, ADB = r. The foot of the perpendicular from I to BCD is the point of tangency of the insphere with BCD, which is the incenter of BCD **only for isosceles tetrahedra** in general. 

The touch point of the insphere on face BCD: The insphere center I is at height r above BCD, and the touch point is the foot of perpendicular from I to BCD. For this to be the incenter of BCD, we need I to lie directly above the incenter of BCD.

We know A lies above the incenter of BCD (from (b)). But I is the incenter of the whole tetrahedron, not necessarily on line from A to incenter of BCD.

**Counterexample for (a):** Consider a tetrahedron where A is above the incenter of BCD but where the geometry is skewed so I is not on line AP. Actually, let me think about whether (b) forces (a)...

In fact, let's think about when the insphere center lies above the incenter of BCD. The insphere center I has equal distance r to all four faces. Its foot on face BCD is the tangency point, which generally is NOT the incenter of BCD unless special conditions hold.

Consider a concrete example: Let BCD be a non-equilateral triangle (say a 3-4-5 right triangle scaled), place A directly above the incenter of BCD at the right height to satisfy all conditions. Then hypothesis 2 is satisfied. But AI need not be perpendicular to BCD since I is the incenter of the tetrahedron, determined by all four faces.

Let me try to construct this explicitly. Place BCD with incenter at origin in the xy-plane. Let B, C, D be arranged so incenter is at origin. Put A = (0, 0, H) directly above. Now I must be equidistant from all faces.

The face BCD has equation z = 0, so d(I, BCD) = z_I = r.

The other faces: since A = (0,0,H) and BCD has incenter at origin, the three faces ABC, ACD, ADB are symmetric in the sense that A is above the incenter... but BCD need not be equilateral.

For a non-equilateral BCD, the incenter is at a specific interior point. With A directly above the incenter, the three faces ABC, ACD, ADB have a certain symmetry. The insphere center I = (x_I, y_I, r) must be equidistant from all four faces.

By symmetry of the configuration (A above incenter of BCD), is I necessarily at (0, 0, r)? Not obviously — the three lateral faces have different shapes.

Let me use coordinates. Let BCD be the triangle with B = (3,0,0), C = (-1,2,0), D = (-1,-2,0) (isoceles but not equilateral). Incenter of BCD: sides are BC = √(16+4) = √20, CD = 4, DB = √20. Incenter = (aB·B + aCD·C... wait, incenter = (a·B + b·C + c·D)/(a+b+c) where a = |CD|, b = |DB|, c = |BC|.

|CD| = 4, |DB| = √20, |BC| = √20. Incenter = (4·(3,0) + √20·(-1,2) + √20·(-1,-2))/(4+2√20) = (12 - 2√20, 0)/(4+2√20).

Hmm, let me use a simpler example. Let BCD be isoceles with B=(2,0,0), C=(-2,0,0), D=(0,3,0). 

|BC|=4, |CD|=√(4+9)=√13, |BD|=√(4+9)=√13.

Incenter = (|CD|·B + |BD|·C + |BC|·D)/(|BC|+|CD|+|BD|) = (√13·(2,0)+√13·(-2,0)+4·(0,3))/(4+2√13) = (0, 12)/(4+2√13) = (0, 6/(2+√13)).

Place A = (0, 6/(2+√13), H) above incenter. By the isoceles symmetry of BCD (symmetric about the y-axis) and A on the y-axis (above incenter), the configuration has a reflection symmetry (x → -x), so I must also lie on the y-axis: I = (0, y_I, r).

Now d(I, plane ABC): A=(0,y_0,H), B=(2,0,0), C=(-2,0,0) where y_0=6/(2+√13).

By the x→-x symmetry, d(I,ABC)=d(I,ACD) automatically, so we just need d(I,ABC)=d(I,BCD)=r and d(I,ABD)=r.

This is getting complicated. The key question for (a) is: does I lie directly above the incenter of BCD?

The tangency point of the insphere on BCD is the foot of perpendicular from I to BCD, which is (x_I, y_I, 0). For (a): AI ⊥ BCD iff I = (x_A, y_A, r) where A = (x_A, y_A, H). 

For (e): tangency point on BCD = (x_I, y_I, 0) = incenter of BCD = (x_A, y_A, 0) [since A is above incenter of BCD]. So (e) ⟺ (a) in this coordinate framing.

So (a) and (e) are equivalent: both say I is directly above the incenter of BCD.

Now is this necessarily true? We've established A is above the incenter Q of BCD. Is I necessarily above Q?

**Key insight:** The incenter of the tetrahedron is at position:

$$I = \frac{[BCD]\cdot A + [ACD]\cdot B + [ABD]\cdot C + [ABC]\cdot D}{[BCD]+[ACD]+[ABD]+[ABC]}$$

Wait, that's not right. The incenter is the weighted average by face areas? Actually yes — the insphere center is:

$$I = \frac{S_{BCD}\cdot A + S_{ACD}\cdot B + S_{ABD}\cdot C + S_{ABC}\cdot D}{S_{BCD}+S_{ACD}+S_{ABD}+S_{ABC}}$$

where $S_{XYZ}$ denotes area of face XYZ. This is because the incenter is at equal distance r from all faces, and can be expressed as the weighted combination.

Hmm, actually I need to verify this formula. The incenter of a tetrahedron is indeed $I = \frac{\sum S_i \mathbf{v}_i}{\sum S_i}$ where the sum is over faces and $\mathbf{v}_i$ is the vertex opposite face $i$... actually that's not standard. Let me reconsider.

The incenter satisfies: it's equidistant from all four faces. It can be written as a convex combination. The correct formula is:

$$I = \frac{S_A \cdot A + S_B \cdot B + S_C \cdot C + S_D \cdot D}{S_A + S_B + S_C + S_D}$$

where $S_A = [BCD]$ (area of face opposite A), etc. This is analogous to the 2D incenter formula.

Using this:
$$I = \frac{[BCD]\cdot A + [ACD]\cdot B + [ABD]\cdot C + [ABC]\cdot D}{[BCD]+[ACD]+[ABD]+[ABC]}$$

The projection of I onto plane BCD (z=0) is:

$$\pi(I) = \frac{[BCD]\cdot \pi(A) + ([ACD]+[ABD]+[ABC])\cdot\text{(weighted combo of B,C,D)}}{[BCD]+[ACD]+[ABD]+[ABC]}$$

where $\pi(A)$ is the projection of A onto BCD, and B,C,D are already in plane BCD.

For $\pi(I)$ to equal the incenter of BCD (which equals $\pi(A)$), we need... this to work out to $\pi(A)$.

The incenter of triangle BCD is $\frac{|CD|\cdot B + |BD|\cdot C + |BC|\cdot D}{|BC|+|CD|+|BD|}$.

We need $\pi(I) = \pi(A)$, i.e., the projection is the incenter Q of BCD.

$$\pi(I) = \frac{[BCD]\cdot Q + [ACD]\cdot B + [ABD]\cdot C + [ABC]\cdot D}{[BCD]+[ACD]+[ABD]+[ABC]}$$

For this to equal Q:
$$[BCD]\cdot Q + [ACD]\cdot B + [ABD]\cdot C + [ABC]\cdot D = Q\cdot([BCD]+[ACD]+[ABD]+[ABC])$$
$$[ACD]\cdot B + [ABD]\cdot C + [ABC]\cdot D = ([ACD]+[ABD]+[ABC])\cdot Q$$
$$Q = \frac{[ACD]\cdot B + [ABD]\cdot C + [ABC]\cdot D}{[ACD]+[ABD]+[ABC]}$$

But the incenter of BCD is $Q = \frac{|CD|\cdot B + |BD|\cdot C + |BC|\cdot D}{|BC|+|CD|+|BD|}$.

So we need: $\frac{[ACD]}{|CD|} = \frac{[ABD]}{|BD|} = \frac{[ABC]}{|BC|}$.

But $[ACD] = \frac{1}{2}|CD|\cdot d(A, CD)$ and similarly, so $\frac{[ACD]}{|CD|} = \frac{1}{2}d(A,CD)$.

The condition becomes: $d(A,CD) = d(A,BD) = d(A,BC)$, which is exactly **hypothesis 2**!

Therefore, **given hypothesis 2, we have $\pi(I) = Q$ = incenter of BCD**.

This means:
- **(b) is true** ✓ (already shown)
- **(e) is true** ✓ (tangency point on BCD = foot of ⊥ from I to BCD = π(I) = Q = incenter of BCD)
- **(a) is true** ✓ (A is directly above Q = π(I), and I is also directly above Q, so AI is vertical = perpendicular to BCD)

Wait, let me re-examine (a). We have A above Q (from hypothesis 2 + (b)), and I above Q (just proved). So A, I, Q are collinear with AQ ⊥ BCD, confirming AI ⊥ BCD. **(a) is true.**

## Checking (d)

Statement (d): Areas of ABC, ACD, ADB are in ratio BC : CD : DB.

$\frac{[ABC]}{BC} = \frac{[ACD]}{CD} = \frac{[ADB]}{DB}$

This is exactly hypothesis 2 restated! (After multiplying out from the volume ratio condition). **Yes, (d) is necessarily true.**

Wait, let me re-derive. From hypothesis 2: $\frac{\text{vol}(IABC)}{BC} = \frac{\text{vol}(IACD)}{CD} = \frac{\text{vol}(IADB)}{DB}$.

vol(IABC) = (1/3)·[ABC]·r (since I is at distance r from face ABC). So hypothesis 2 gives:

$\frac{[ABC]}{BC} = \frac{[ACD]}{CD} = \frac{[ADB]}{DB}$

which says $[ABC] : [ACD] : [ADB] = BC : CD : DB$. 

**Yes, (d) is necessarily true.** ✓

## Summary So Far
- (a) ✓, (b) ✓, (c) ✓, (d) ✓, (e) ✓

## Checking (f): AB = AC = AD

This is a much stronger statement. Let's see if it's forced.

We know A is directly above the incenter Q of BCD. Does this force AB = AC = AD? Only if B, C, D are equidistant from Q, i.e., if Q is the circumcenter of BCD. The incenter equals circumcenter only for equilateral triangles. So for a non-equilateral BCD with A above its incenter, AB ≠ AC ≠ AD in general.

But wait — we also need to check that dihedral angles are acute. Let me construct a counterexample.

Let BCD be an isoceles (non-equilateral) triangle. Let B = (2,0,0), C = (-2,0,0), D = (0,d,0) for some d ≠ 2√3 (so not equilateral).

|BC| = 4, |CD| = √(4+d²), |BD| = √(4+d²). Incenter: since |CD| = |BD|, by symmetry Q lies on the y-axis. Q = (|CD|·B + |BD|·C + |BC|·D)/(|BC|+|CD|+|BD|)... 

Hmm wait, incenter formula: Q = (a·A + b·B + c·C)/(a+b+c) for triangle with side lengths a=|BC|, b=|CA|, c=|AB| opposite to A, B, C. For triangle BCD with vertices B, C, D: let's use a = |CD|, b = |BD|, c = |BC| as weights:

Q = (a·B + b·C + c·D)/(a+b+c) where a=|CD|, b=|BD|, c=|BC|.

With |CD|=|BD|=s=√(4+d²) and |BC|=4:
Q = (s·B + s·C + 4·D)/(2s+4) = (s(2,0)+s(-2,0)+4(0,d))/(2s+4) = (0, 4d/(2s+4)) = (0, 2d/(s+2)).

Place A at (0, 2d/(s+2), H) for some H > 0. Then A is above Q. Hypothesis 2 is satisfied (by our derivation). 

Now AB = √(4 + (2d/(s+2))² + H²), AC = same (by symmetry), AD = √((d - 2d/(s+2))² + H²) = √((d·s/(s+2))² + H²).

AB = AC but AB ≠ AD unless 4 + (2d/(s+2))² = (d·s/(s+2))², i.e., unless d²s²/(s+2)² - 4d²/(s+2)² = 4, i.e., d²(s²-4)/(s+2)² = 4. Since s²=4+d², s²-4=d², so d⁴/(s+2)² = 4, i.e., d² = 2(s+2) = 2(√(4+d²)+2). This gives a specific relationship, not generally true.

So for generic d (like d=3): s=√(4+9)=√13, Q=(0, 6/(√13+2), H). AB=AC≠AD.

We need to check the acute dihedral angle condition. For small H or large H, we can adjust. For reasonable d and H, dihedral angles can be made acute.

**Therefore (f) is NOT necessarily true.** ✗

## Checking (g): Triangle ABC isosceles with AB = AC

From the example above with isoceles BCD (|BD|=|CD|) and A above incenter on the symmetry axis, we get AB = AC. But is this always true?

What if BCD is scalene? Can we still have hypothesis 2 satisfied with A above the incenter of a scalene triangle?

Yes! Take any scalene triangle BCD with incenter Q, place A above Q. Then hypothesis 2 is satisfied (as we've shown: d(A, BC) = d(A, CD) = d(A, BD) since A is above the incenter, and incenter equidistant from all three lines). But then generally AB ≠ AC ≠ AD.

For example, take an equilateral-ish but slightly scalene BCD. Then AB ≠ AC, so (g) fails.

**Therefore (g) is NOT necessarily true.** ✗

## Checking (h): Triangle BCD is equilateral

From the isoceles example above (B=(2,0,0), C=(-2,0,0), D=(0,3,0) which is not equilateral), hypothesis 2 is satisfied with A above incenter. So BCD need not be equilateral.

**Therefore (h) is NOT necessarily true.** ✗

## Wait — Re-examine acute dihedral angle condition

The problem states dihedral angles are acute. Let me verify this doesn't force additional constraints.

The acute dihedral angle condition ensures:
1. The insphere touches each face in the interior (not a degenerate case)
2. The incenter is in the interior

For our counterexamples to (f), (g), (h), we placed A above the incenter of BCD. We need to verify dihedral angles remain acute.

For the example B=(2,0,0), C=(-2,0,0), D=(0,3,0), A=(0, y_Q, H):

The dihedral angles depend on the specific geometry. By choosing H appropriately (not too small, not too large), we can likely ensure all dihedral angles are acute. The condition that dihedral angles are acute is an open condition, so if satisfied for some H, it's satisfied for nearby H. 

A regular tetrahedron has all dihedral angles equal to arccos(1/3) ≈ 70.5°, which is acute. By perturbing from a regular tetrahedron slightly (making BCD slightly non-equilateral but keeping A above the incenter of BCD), we maintain acute dihedral angles and violate (f), (g), (h).

## Final Verification of (a), (b), (c), (d), (e)

Let me double-check the proof of (a).

We showed:
1. From hyp 2: $d(A, BC) = d(A, CD) = d(A, DB)$ (equivalent form of hyp 2)
2. This means the projection P of A onto plane BCD satisfies $d(P, BC) = d(P, CD) = d(P, DB)$
3. So P = incenter Q of BCD → **(b) true**
4. Using the incenter formula for I, and the condition $\frac{[ACD]}{CD} = \frac{[ABD]}{BD} = \frac{[ABC]}{BC}$, we showed π(I) = Q
5. Since A is directly above Q and I is directly above Q, AI ⊥ plane BCD → **(a) true**
6. The tangency point of insphere on BCD = π(I) = Q = incenter of BCD → **(e) true**
7. (c) is the equivalent restatement of hyp 2 → **(c) true**
8. (d) is the direct restatement of hyp 2 in terms of areas → **(d) true**

## Answer

The necessarily true statements are **(a), (b), (c), (d), (e)**.

$$\boxed{\{a, b, c, d, e\}}$$
