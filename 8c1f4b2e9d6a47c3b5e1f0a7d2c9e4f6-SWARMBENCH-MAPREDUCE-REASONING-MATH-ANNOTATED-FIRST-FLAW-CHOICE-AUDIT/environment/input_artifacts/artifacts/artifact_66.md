# artifact_66

Competition: IMOSL  
Problem ID: IMOSL_2012_6  
Year: 2012

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(ABC\) be a triangle with \(AB \ne AC\), and let the perpendicular bisector of \(BC\) meet the circumcircle at the point \(M\) on the arc \(BC\) not containing \(A\). Prove that \(M\) lies on the angle bisector of \(\angle BAC\).

## Candidate Excerpts

### Option A

```text
Step 2.  By the Inscribed Angle Theorem (the central angle is twice the inscribed angle),
angle BMC = 2 angle BAC.  Wait, the inscribed angle theorem says: the inscribed angle is
half the central angle subtended by the same arc.  Here the central angle BOC = 2 angle BAC
(if M is on the major arc).  And angle BMC = angle BAC (inscribed in the same arc BC from
the major-arc side).  But M is on the minor arc BC, so angle BMC = 180° - angle BAC by
the inscribed angle theorem for opposite arcs.
```

### Option B

```text
Step 1.  Let O be the circumcenter of triangle ABC.  By definition, M lies on the
perpendicular bisector of BC, so MB = MC.  Since M is on the circumcircle, by the
inscribed angle theorem applied to chord BC, the angles inscribing arc BC from a point
on the major arc are equal — meaning angle BMC = angle BAC.
```

### Option C

```text
Step 4.  Now to show MA bisects angle BAC.  Consider angles MAB and MAC (inscribed in
the circumcircle on chords MB and MC respectively).  By the inscribed angle theorem,
   angle MAB = angle MCB (subtending arc MB),
   angle MAC = angle MBC (subtending arc MC).
But angle MBC = angle MCB (Step 3, isosceles).  Hence angle MAB = angle MAC, so MA
bisects angle BAC.  Done.
```

### Option D

```text
Step 3.  Now since MB = MC and angle BMC is known, triangle MBC is isosceles with
MB = MC.  The base angles are equal: angle MBC = angle MCB.  And angle MBC + angle MCB
+ angle BMC = 180°, so 2 angle MBC = 180° - angle BMC.
```

## Full Candidate Proof

```text
Step 1.  Let O be the circumcenter of triangle ABC.  By definition, M lies on the
perpendicular bisector of BC, so MB = MC.  Since M is on the circumcircle, by the
inscribed angle theorem applied to chord BC, the angles inscribing arc BC from a point
on the major arc are equal — meaning angle BMC = angle BAC.

Step 2.  By the Inscribed Angle Theorem (the central angle is twice the inscribed angle),
angle BMC = 2 angle BAC.  Wait, the inscribed angle theorem says: the inscribed angle is
half the central angle subtended by the same arc.  Here the central angle BOC = 2 angle BAC
(if M is on the major arc).  And angle BMC = angle BAC (inscribed in the same arc BC from
the major-arc side).  But M is on the minor arc BC, so angle BMC = 180° - angle BAC by
the inscribed angle theorem for opposite arcs.

Step 3.  Now since MB = MC and angle BMC is known, triangle MBC is isosceles with
MB = MC.  The base angles are equal: angle MBC = angle MCB.  And angle MBC + angle MCB
+ angle BMC = 180°, so 2 angle MBC = 180° - angle BMC.

Step 4.  Now to show MA bisects angle BAC.  Consider angles MAB and MAC (inscribed in
the circumcircle on chords MB and MC respectively).  By the inscribed angle theorem,
   angle MAB = angle MCB (subtending arc MB),
   angle MAC = angle MBC (subtending arc MC).
But angle MBC = angle MCB (Step 3, isosceles).  Hence angle MAB = angle MAC, so MA
bisects angle BAC.  Done.
```

## Reviewer Note

In Step 2, the Inscribed Angle Theorem is misapplied: the proof invokes "central angle is twice the inscribed angle" but does not verify which arc M corresponds to. The theorem requires specifying whether the inscribed angle and central angle subtend the same arc or opposite arcs. The proof oscillates between "angle BMC = angle BAC" (Step 1) and "angle BMC = 2 angle BAC" then "angle BMC = 180° - angle BAC" (Step 2) without settling on a consistent statement. The key precondition — that M is on the minor arc BC — is needed before invoking the supplementary angle relation, but the proof never establishes which arc M is on rigorously (it's stated as a hypothesis but the theorem application doesn't track this).
