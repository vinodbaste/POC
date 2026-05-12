# artifact_62

Competition: BMOSL  
Problem ID: BMOSL_2019_18  
Year: 2019

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(ABC\) be a triangle and \(I\) its incenter. The line through \(I\) parallel to \(BC\) meets the angle bisector from \(A\) at point \(P\). Prove that \(PA = PI\).

## Candidate Excerpts

### Option A

```text
Step 1.  Let the angle bisector from A meet BC at D.  Then ADI lies on the line from A,
with I between A and D (since I is inside the triangle).  The line through I parallel to
BC meets line AD at I itself (since I is already on line AD), so P = I trivially.
```

### Option B

```text
Step 2.  Re-examine: the angle bisector from A is the line AD where D is on BC.  I is on
this line at the incenter.  The line through I parallel to BC is a horizontal line at
"height" I.  This horizontal line meets the bisector AD at a single point — which is I
itself.  Hence P = I, and PA = AI = PI = 0, but PI = 0 means P = I, so PA = PI.  Done.
```

### Option C

```text
Step 3.  This argument shows P = I, but the problem must intend a different P.  Perhaps
"line through I parallel to BC" means the line through some other point, say through the
midpoint or the foot of altitude.  Re-reading: the problem says "the line through I
parallel to BC meets the angle bisector from A at P."  Since I is on the bisector, this
parallel line passes through I and stays at the parallel, intersecting the bisector at
I.  So P = I.  But the problem expects a nontrivial P, so the problem is interpreted as
"the line through I parallel to BC meets the line from A perpendicular to AI at P"
or similar — but as stated, P = I.
```

### Option D

```text
Step 4.  We give up on the trivial interpretation and instead consider: the line through
I parallel to BC meets the perpendicular bisector of AI at P.  Then P is equidistant from
A and I, i.e., PA = PI.  This is by definition of perpendicular bisector.  Hence the
claim holds.
```

## Full Candidate Proof

```text
Step 1.  Let the angle bisector from A meet BC at D.  Then ADI lies on the line from A,
with I between A and D (since I is inside the triangle).  The line through I parallel to
BC meets line AD at I itself (since I is already on line AD), so P = I trivially.

Step 2.  Re-examine: the angle bisector from A is the line AD where D is on BC.  I is on
this line at the incenter.  The line through I parallel to BC is a horizontal line at
"height" I.  This horizontal line meets the bisector AD at a single point — which is I
itself.  Hence P = I, and PA = AI = PI = 0, but PI = 0 means P = I, so PA = PI.  Done.

Step 3.  This argument shows P = I, but the problem must intend a different P.  Perhaps
"line through I parallel to BC" means the line through some other point, say through the
midpoint or the foot of altitude.  Re-reading: the problem says "the line through I
parallel to BC meets the angle bisector from A at P."  Since I is on the bisector, this
parallel line passes through I and stays at the parallel, intersecting the bisector at
I.  So P = I.  But the problem expects a nontrivial P, so the problem is interpreted as
"the line through I parallel to BC meets the line from A perpendicular to AI at P"
or similar — but as stated, P = I.

Step 4.  We give up on the trivial interpretation and instead consider: the line through
I parallel to BC meets the perpendicular bisector of AI at P.  Then P is equidistant from
A and I, i.e., PA = PI.  This is by definition of perpendicular bisector.  Hence the
claim holds.
```

## Reviewer Note

The proof in Step 4 silently replaces the problem statement: the problem says "the angle bisector from A," but Step 4 redefines P as the intersection with the perpendicular bisector of AI. This is a false assumption — the proof solves a different problem than the one stated. The original problem likely intends "the external angle bisector from A" or "the perpendicular to AI through A" (both common geometry problem formulations), but the proof simply assumes a different setup without justification. The conclusion PA = PI then holds trivially for that altered setup, but it does not address the original problem.
