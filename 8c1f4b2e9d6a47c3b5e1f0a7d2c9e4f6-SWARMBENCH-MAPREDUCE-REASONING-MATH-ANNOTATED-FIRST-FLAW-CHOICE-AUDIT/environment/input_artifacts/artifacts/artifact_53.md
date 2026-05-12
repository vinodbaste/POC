# artifact_53

Competition: BMOSL  
Problem ID: BMOSL_2020_11  
Year: 2020

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(ABC\) be an acute triangle with circumcircle \(\Omega\). Let \(D, E, F\) be the feet of the altitudes from \(A, B, C\), respectively. Prove that the circumcircle of triangle \(DEF\) (the nine-point circle) has radius half that of \(\Omega\).

## Candidate Excerpts

### Option A

```text
Let N be the midpoint of OH.  We claim N is the center of the circle through D, E, F.
To see this, observe that the homothety h centered at H with ratio 1/2 maps each H_X
(reflection of H over the opposite side) to the foot of the corresponding altitude.
For instance, h(H_A) is the midpoint of HH_A, which equals D since H_A is the reflection
of H over BC.
```

### Option B

```text
Since h(Ω) is a circle centered at h(O) with radius (1/2) · R = R/2, where R is the
circumradius, and h(Ω) passes through h(H_A) = D, h(H_B) = E, h(H_C) = F, we conclude
that D, E, F lie on a circle of radius R/2 centered at h(O).  Furthermore, h(O) is the
midpoint of segment HO, which is exactly the nine-point center N.
```

### Option C

```text
Therefore the circumradius of DEF is R/2 = (1/2) · (circumradius of ABC), as required.
```

### Option D

```text
Let O be the circumcenter and H the orthocenter of triangle ABC.  By a standard result,
the reflection of H over any side of the triangle lies on the circumcircle Ω.
In particular, the reflection H_A of H over line BC lies on Ω.
```

## Full Candidate Proof

```text
Step 1.  Let O be the circumcenter and H the orthocenter of triangle ABC.  By a standard
result, the reflection of H over any side of the triangle lies on the circumcircle Ω.
In particular, the reflection H_A of H over line BC lies on Ω.

Step 2.  Let N be the midpoint of OH.  We claim N is the center of the circle through
D, E, F.  To see this, observe that the homothety h centered at H with ratio 1/2 maps each
H_X (reflection of H over the opposite side) to the foot of the corresponding altitude.
For instance, h(H_A) is the midpoint of HH_A, which equals D since H_A is the reflection
of H over BC.

Step 3.  Since h(Ω) is a circle centered at h(O) with radius (1/2) · R = R/2, where R is
the circumradius, and h(Ω) passes through h(H_A) = D, h(H_B) = E, h(H_C) = F, we conclude
that D, E, F lie on a circle of radius R/2 centered at h(O).  Furthermore, h(O) is the
midpoint of segment HO, which is exactly the nine-point center N.

Step 4.  Therefore the circumradius of DEF is R/2 = (1/2) · (circumradius of ABC),
as required.
```

## Reviewer Note

The step claiming "h(O) is the midpoint of segment HO" is asserted without explanation. While the conclusion happens to be true, the proof does not derive it from the definition of h (homothety at H with ratio 1/2 applied to O gives the midpoint of HO). The intermediate identification h(H_A) = D also conflates the homothety image with the foot of the altitude D — D is the midpoint of segment HH_A, but the homothety at H with ratio 1/2 maps H_A to the midpoint of HH_A only if H is the center of the homothety and we are halving the segment HH_A. This identification step needs justification and the cited "standard result" about the homothety mapping reflections to feet is asserted as obvious when it is not.
