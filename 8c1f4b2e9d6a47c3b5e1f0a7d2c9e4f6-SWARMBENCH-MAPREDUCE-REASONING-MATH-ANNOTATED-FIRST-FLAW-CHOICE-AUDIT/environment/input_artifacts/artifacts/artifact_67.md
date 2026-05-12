# artifact_67

Competition: USAMO  
Problem ID: USAMO_2012_5  
Year: 2012

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(P\) be a point in the plane of triangle \(ABC\), and let \(\gamma\) be a line passing through \(P\). Let \(A', B', C'\) be the points where the reflections of lines \(PA, PB, PC\) with respect to \(\gamma\) intersect lines \(BC, CA, AB\), respectively. Prove that \(A', B', C'\) are collinear.

## Candidate Excerpts

### Option A

```text
Step 3.  Consider the cross-ratio (BC; A A') on line BC.  By the projective properties
of reflection through P, the cross-ratio is preserved up to the involution induced by γ.
Hence A' lies on a specific projective line through B and C, determined by the involution.
```

### Option B

```text
Step 4.  By Desargues' theorem applied to triangles ABC and A'B'C': these two triangles
are in perspective from the point P (each pair of corresponding vertices lies on a line
through P).  Hence the corresponding sides intersect collinearly — but the corresponding
sides are BC, CA, AB themselves (the lines containing the original triangle), so the
intersections are A', B', C'.  Hence A', B', C' are collinear, as required.
```

### Option C

```text
Step 1.  Assume γ passes through P, with arbitrary direction.  Reflect lines PA, PB, PC
in γ to get lines PA*, PB*, PC*, where A*, B*, C* are the reflected images of A, B, C in
γ.  Then PA* = line(P, A*), etc.  Since γ passes through P, P is fixed by the reflection.
```

### Option D

```text
Step 2.  A' is the intersection of PA* with BC.  By the definition of reflection,
A' is constructed by:  draw line PA from P, reflect across γ to get line PA*, then
intersect PA* with BC.  This is a projective construction in the plane.
```

## Full Candidate Proof

```text
Step 1.  Assume γ passes through P, with arbitrary direction.  Reflect lines PA, PB, PC
in γ to get lines PA*, PB*, PC*, where A*, B*, C* are the reflected images of A, B, C in
γ.  Then PA* = line(P, A*), etc.  Since γ passes through P, P is fixed by the reflection.

Step 2.  A' is the intersection of PA* with BC.  By the definition of reflection,
A' is constructed by:  draw line PA from P, reflect across γ to get line PA*, then
intersect PA* with BC.  This is a projective construction in the plane.

Step 3.  Consider the cross-ratio (BC; A A') on line BC.  By the projective properties
of reflection through P, the cross-ratio is preserved up to the involution induced by γ.
Hence A' lies on a specific projective line through B and C, determined by the involution.

Step 4.  By Desargues' theorem applied to triangles ABC and A'B'C': these two triangles
are in perspective from the point P (each pair of corresponding vertices lies on a line
through P).  Hence the corresponding sides intersect collinearly — but the corresponding
sides are BC, CA, AB themselves (the lines containing the original triangle), so the
intersections are A', B', C'.  Hence A', B', C' are collinear, as required.
```

## Reviewer Note

In Step 4, the proof assumes A, A', and P are collinear (that is, A' lies on line PA), which would make ABC and A'B'C' in perspective from P. But A' is defined as the intersection of PA* (the reflected line) with BC, not as the intersection of PA with BC. Hence in general A' is NOT on line PA — it's on line PA*, the reflection of PA across γ. The triangles ABC and A'B'C' are not in perspective from P unless PA* = PA, which holds only when PA is parallel to γ or PA is symmetric to itself across γ. The application of Desargues' theorem rests on this false assumption about perspectivity.
