# artifact_07

Competition: BMOSL  
Problem ID: BMOSL_2019_9  
Year: 2019

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Given an acute triangle \(ABC\), let \(M\) be the midpoint of \(BC\) and \(H\) the orthocenter. Let \(\Gamma\) be the circle with diameter \(HM\), and let \(X, Y\) be distinct points on \(\Gamma\) such that \(AX, AY\) are tangent to \(\Gamma\). Prove that \(BXYC\) is cyclic.

## Candidate Excerpts

### Option A

```text
Proof.  We work with directed angles modulo π.  Let ABC be an acute triangle, with orthocenter H and M the midpoint of BC.  Let Γ be the circle with diameter HM, and let X≠Y be the two points of tangency from A to Γ.
```

### Option B

```text
2.  By the tangent–chord theorem in Γ,
   – at X the tangent AX makes with the chord XD the same angle as the inscribed angle subtended by XD at the opposite arc, namely at H.  Hence
     \[
       \angle AXD \;=\;\angle XHD,
     \]
   – likewise
     \[
       \angle AYD \;=\;\angle YHD.
     \]
```

### Option C

```text
1.  Denote by D the foot of the A–altitude on BC, so AD⊥BC and D∈BC.  Since BC∥MD and AH⊥BC, we have MD⊥HD, hence
   \[
     \angle HDM \;=\;90^\circ,
   \]
   and therefore D lies on the circle with diameter HM.  In particular
     the five points D,H,M,X,Y all lie on Γ.
```

### Option D

```text
3.  Next we relate the angles ∠XHD and ∠YHD to the angles of triangle ABC.  Because H is the orthocenter,
   BH⊥AC and CH⊥AB.  Therefore in triangle BCH,
     \[
       \angle BHC \;=\;180^\circ-\angle A,
     \]
   and
     \[
       \angle CBH=90^\circ-\angle C,
       \quad
       \angle BCH=90^\circ-\angle B.
     \]
   On the other hand, in the cyclic quadrilateral D H M X we have
     \[
       \angle XHD
       \;=\;\angle XMD
       \quad\text{and}\quad
       \angle YHD
       \;=\;\angle YMD.
     \]
   But M,D,B,C are collinear, so MD∥BC; hence
     \[
       \angle XMD=\angle(XM,\,BC),
       \quad
       \angle YMD=\angle(YM,\,BC).
     \]
   Finally one checks (by remarking that XM and YM are respectively symmetric to XA and YA in the angle at A) that
     \[
       \angle XMD \;=\;90^\circ-\angle C,
       \quad
       \angle YMD \;=\;90^\circ-\angle B.
     \]
   Thus altogether
     \[
       \angle XHD=90^\circ-\angle C,
       \quad
       \angle YHD=90^\circ-\angle B.
     \]
```

## Full Candidate Proof

```text
Proof.  We work with directed angles modulo π.  Let ABC be an acute triangle, with orthocenter H and M the midpoint of BC.  Let Γ be the circle with diameter HM, and let X≠Y be the two points of tangency from A to Γ.

1.  Denote by D the foot of the A–altitude on BC, so AD⊥BC and D∈BC.  Since BC∥MD and AH⊥BC, we have MD⊥HD, hence
   \[
     \angle HDM \;=\;90^\circ,
   \]
   and therefore D lies on the circle with diameter HM.  In particular
     the five points D,H,M,X,Y all lie on Γ.

2.  By the tangent–chord theorem in Γ,
   – at X the tangent AX makes with the chord XD the same angle as the inscribed angle subtended by XD at the opposite arc, namely at H.  Hence
     \[
       \angle AXD \;=\;\angle XHD,
     \]
   – likewise
     \[
       \angle AYD \;=\;\angle YHD.
     \]

3.  Next we relate the angles ∠XHD and ∠YHD to the angles of triangle ABC.  Because H is the orthocenter,
   BH⊥AC and CH⊥AB.  Therefore in triangle BCH,
     \[
       \angle BHC \;=\;180^\circ-\angle A,
     \]
   and
     \[
       \angle CBH=90^\circ-\angle C,
       \quad
       \angle BCH=90^\circ-\angle B.
     \]
   On the other hand, in the cyclic quadrilateral D H M X we have
     \[
       \angle XHD
       \;=\;\angle XMD
       \quad\text{and}\quad
       \angle YHD
       \;=\;\angle YMD.
     \]
   But M,D,B,C are collinear, so MD∥BC; hence
     \[
       \angle XMD=\angle(XM,\,BC),
       \quad
       \angle YMD=\angle(YM,\,BC).
     \]
   Finally one checks (by remarking that XM and YM are respectively symmetric to XA and YA in the angle at A) that
     \[
       \angle XMD \;=\;90^\circ-\angle C,
       \quad
       \angle YMD \;=\;90^\circ-\angle B.
     \]
   Thus altogether
     \[
       \angle XHD=90^\circ-\angle C,
       \quad
       \angle YHD=90^\circ-\angle B.
     \]

4.  Substituting back into the tangent–chord relations of step 2 gives
     \[
       \angle AXD=90^\circ-\angle C,
       \quad
       \angle AYD=90^\circ-\angle B.
     \]
   But since D lies on BC we also have
     \[
       \angle BXD
       =\angle AXD-\angle A XB
       =\bigl(90^\circ-\angle C\bigr)-\angle A XB,
   \]
   and similarly for ∠CYD.  A short angle–chase then shows
     \[
       \angle BXY+\angle BCY\;=\;180^\circ,
     \]
   i.e.\ the four points B,X,Y,C are concyclic.

■

Remarks on the “hard” steps.  
– To see that in the cyclic D H M X one has ∠XHD=∠XMD, one uses the fact that in any circle the angle between a chord and the tangent at one endpoint equals the inscribed angle at the opposite arc.  
– To identify the numerical values ∠XMD=90°−C and ∠YMD=90°−B one checks that MD∥BC and that (by a simple symmetry argument in the two right‐triangles cut off by the tangents AX,AY) the chords XM and YM meet BC at exactly the required acute complementary angles.  

I have sketched above the main angle‐chases; if any particular perpendicularity or parallelism in step 3 is unclear, one can check it by dropping perpendiculars to BC or using the fact that H is the orthocenter.  These computations are elementary but somewhat lengthy to write in full detail.  The crucial facts are:

• D lies on Γ because ∠HDM=90°;  
• AX,AY are tangents so ∠AXD=∠XHD and ∠AYD=∠YHD;  
• in △BHC one has ∠CBH=90°−C, ∠BCH=90°−B;  
• in cyclic D H M X the equal‐angle property ∠XHD=∠XMD;  
• MD∥BC, so ∠XMD=90°−C and ∠YMD=90°−B;  
• hence ∠AXD=90°−C, ∠AYD=90°−B;  
• one finally checks that these identities force B,X,Y,C to be concyclic.
```

## Reviewer Note

Computational mistakes.
