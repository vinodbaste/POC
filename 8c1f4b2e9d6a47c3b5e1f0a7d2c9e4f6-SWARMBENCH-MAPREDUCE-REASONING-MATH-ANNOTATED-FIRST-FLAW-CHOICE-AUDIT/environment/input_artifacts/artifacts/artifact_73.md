# artifact_73

Competition: USAMO  
Problem ID: USAMO_2014_5  
Year: 2014

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(ABC\) be a triangle with orthocenter \(H\) and let \(P\) be the second intersection of the circumcircle of triangle \(AHC\) with the internal bisector of \(\angle BAC\). Let \(X\) be the circumcenter of triangle \(APB\) and \(Y\) the orthocenter of triangle \(APC\). Prove that the length of segment \(XY\) is equal to the circumradius of triangle \(ABC\).

## Candidate Excerpts

### Option A

```text
Step 2.  Therefore the circumcircle of AHC has the same radius R as the circumcircle of
ABC.  P, being the second intersection with the angle bisector from A, lies on this
reflected circle and is determined by the angular relationship at A.
```

### Option B

```text
Step 3.  Now consider the circumcenter X of triangle APB.  Since X is equidistant from
A, P, and B, it lies on the perpendicular bisectors of AP, PB, and AB.  In particular,
X lies on the perpendicular bisector of AB.
```

### Option C

```text
Step 4.  By a lengthy angle-chasing argument (omitted for brevity), one establishes that
the segment XY has the same length as the circumradius R of triangle ABC.  This completes
the proof.
```

### Option D

```text
Step 1.  We begin by noting that since H is the orthocenter of ABC, the circumcircle of
AHC has center diametrically opposite to A with respect to the angle bisector reflection.
This is a classical configuration: the circumcircle of triangle AHC is the reflection of
the circumcircle of ABC across the line BC.
```

## Full Candidate Proof

```text
Step 1.  We begin by noting that since H is the orthocenter of ABC, the circumcircle of
AHC has center diametrically opposite to A with respect to the angle bisector reflection.
This is a classical configuration: the circumcircle of triangle AHC is the reflection of
the circumcircle of ABC across the line BC.

Step 2.  Therefore the circumcircle of AHC has the same radius R as the circumcircle of
ABC.  P, being the second intersection with the angle bisector from A, lies on this
reflected circle and is determined by the angular relationship at A.

Step 3.  Now consider the circumcenter X of triangle APB.  Since X is equidistant from
A, P, and B, it lies on the perpendicular bisectors of AP, PB, and AB.  In particular,
X lies on the perpendicular bisector of AB.

Step 4.  By a lengthy angle-chasing argument (omitted for brevity), one establishes that
the segment XY has the same length as the circumradius R of triangle ABC.  This completes
the proof.
```

## Reviewer Note

Step 4 simply asserts the result "by a lengthy angle-chasing argument (omitted for brevity)" without providing any of the actual angle-chasing. The conclusion XY = R is the whole content of the problem — saying "omitted for brevity" leaves the entire proof to the reader. This is the canonical case of an unjustified claim: the key step is replaced with an unsupported assertion.
