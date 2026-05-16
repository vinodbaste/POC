# artifact_22

Competition: IMO
Problem ID: imo_2006_p1
Year: 2006

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

Let $ABC$ be a triangle with incentre $I$. A point $P$ in the interior of the triangle satisfies $\angle PBA + \angle PCA = \angle PBC + \angle PCB$. Show that $AP \ge AI$, with equality iff $P = I$.

## Candidate Excerpts

### Option A

```text
Since ∠IBA + ∠ICA = B/2 + C/2 = (B+C)/2 = (π-A)/2, the incentre I satisfies the
angle condition. The locus of points P satisfying ∠PBA + ∠PCA = (π-A)/2 passes
through I. By the inscribed angle theorem applied to the circumcircle of BPC,
all such P lie on a fixed circle through B and C, namely the circumcircle of
triangle BIC. Point I lies on this circle, so P lies on the circumcircle of BIC.
```

### Option B

```text
On the circumcircle of BIC: the centre of this circle lies on the perpendicular
bisectors of BI and IC. Since I is the incentre, BI and IC are angle bisectors,
and their perpendicular bisectors pass through the circumcentre of BIC. The
radius R' of the circumcircle of BIC satisfies R' = R/(2 cos(A/2)) by the
extended law of sines applied to triangle BIC with ∠BIC = π/2 + A/2.
```

### Option C

```text
The condition ∠PBA + ∠PCA = ∠PBC + ∠PCB can be rewritten. Since
∠PBA + ∠PBC = ∠B and ∠PCA + ∠PCB = ∠C, the condition becomes:
  ∠PBA + ∠PCA = ∠B - ∠PBA + ∠C - ∠PCA,
  2(∠PBA + ∠PCA) = ∠B + ∠C = π - ∠A,
  ∠PBA + ∠PCA = (π - ∠A)/2.
```

### Option D

```text
For any point P on the circumcircle of BIC, we have AP ≥ AI with equality iff P=I,
by the triangle inequality applied along the arc. Since P lies on this circle
and A is exterior to it, the minimum distance from A to a point on the circle
is AI (as I is the closest point on the circle to A). Hence AP ≥ AI.
```

## Full Candidate Proof

```text
Step 1. Rewrite the condition: ∠PBA+∠PCA = (π-A)/2 = (B+C)/2.

Step 2. By the inscribed angle theorem on the circumcircle of BPC, points with
∠PBA+∠PCA = constant lie on a fixed circle through B and C — the circumcircle
of triangle BIC. So P lies on circumcircle(BIC), which passes through I.

Step 3. Radius formula for circumcircle(BIC): R'=R/(2cos(A/2)) via law of sines
on BIC (∠BIC=90°+A/2).

Step 4. Since P lies on circumcircle(BIC) and A is outside this circle, the
nearest point on the circle to A is I, so AP≥AI with equality iff P=I.
```

## Reviewer Note

Option B (Step 2) is the first invalid step. The claim that "points with $\angle PBA + \angle PCA = \text{constant}$ lie on a fixed circle through $B$ and $C$ by the inscribed angle theorem" misapplies the inscribed angle theorem. The standard inscribed angle theorem says that $\angle BPC$ (one angle) is constant on a circular arc through $B$ and $C$ — it does not apply directly to the sum $\angle PBA + \angle PCA$ (which involves angles at two different vertices, $B$ and $C$). The locus of $P$ satisfying the given sum condition is not immediately characterized by the inscribed angle theorem in this form. The step conflates a sum of two angles at distinct vertices with a single inscribed angle.
