# artifact_05

Competition: BMOSL  
Problem ID: BMOSL_2019_9  
Year: 2019

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Given an acute triangle \(ABC\), let \(M\) be the midpoint of \(BC\) and \(H\) the orthocenter. Let \(\Gamma\) be the circle with diameter \(HM\), and let \(X, Y\) be distinct points on \(\Gamma\) such that \(AX, AY\) are tangent to \(\Gamma\). Prove that \(BXYC\) is cyclic.

## Candidate Excerpts

### Option A

```text
•  Power‐of‐a‐Point.  For any point U and any circle ω, if through U we draw a tangent of length t and a secant meeting ω in U,V (with U nearer) and W, then  
   (T2)   t²  =  (UV)·(UW).
```

### Option B

```text
We split the proof into three lemmas.
```

### Option C

```text
•  Tangent–Chord Theorem.  If L is a tangent to a circle at P and Q is any other point on the circle, then  
   (T1)   ∠ ( L, PQ )  =  ∠ ( QP, PR ),  
where R is the third point of the circle with P and Q (i.e. the angle “in the opposite arc”).
```

### Option D

```text
Lemma 1.  AX² = AM·AH.  In particular, AX = AY.
```

## Full Candidate Proof

```text
Proof.  We work in the usual Euclidean plane and denote by “∠(ℓ,m)” the (undirected) angle between lines ℓ and m, taken in [0°,180°).  All angles are mod 180°.  

Let ABC be an acute triangle with orthocenter H and let M be the midpoint of BC.  Let Γ be the circle with diameter HM.  From A draw the two tangents to Γ, meeting Γ again at X and at Y (so that AX and AY are tangent to Γ).  We must show that B,X,Y,C lie on one circle.  

Throughout we will use freely:

•  Tangent–Chord Theorem.  If L is a tangent to a circle at P and Q is any other point on the circle, then  
   (T1)   ∠ ( L, PQ )  =  ∠ ( QP, PR ),  
where R is the third point of the circle with P and Q (i.e. the angle “in the opposite arc”).  

•  Power‐of‐a‐Point.  For any point U and any circle ω, if through U we draw a tangent of length t and a secant meeting ω in U,V (with U nearer) and W, then  
   (T2)   t²  =  (UV)·(UW).  

We split the proof into three lemmas.

Lemma 1.  AX² = AM·AH.  In particular, AX = AY.  

Proof.  By (T2), applied to U=A, ω=Γ, the tangent AX (of length AX) and the secant through A meeting Γ again in M and H,  
    AX²  =  (AM)·(AH).  
This immediately gives AX² = AM·AH = AY², so AX=AY.  ■

Lemma 2.  The four points B,C,H,M are not concyclic, and in fact ∠ (HM,BC)=∠A.  

Proof.  Since H is the orthocenter, AH⊥BC.  But M∈BC, so AH⊥BM.  On the other hand, HM is the diameter‐line of Γ, and A lies off Γ, so AH is not parallel to HM; in particular H,M,B,C are not concyclic.  Moreover at M,  
   ∠ (HM,BC)  =  ∠ (HM,MB)  
               =  90°  (because AH⊥BC and AH meets HM at H)  
               =  ∠A,  
since in triangle ABC the altitude from A makes a right angle with BC.  ■

Lemma 3.  ∠BXY = ∠BCY.  Hence B,X,Y,C are concyclic.  

Proof.  We will show that X and Y see BC under the same angle.  Since BC∥MB,  
   ∠BXY  =  ∠(BX,XY)  
          =  ∠( BX, AY )     (because AY is the same line as XY at Y)  
          =  ∠(AY, BX).  

But at X we may apply the Tangent–Chord Theorem (T1) to the tangent AX and the chord XH on Γ.  It says  
   ∠(AX,XH)  =  ∠HMX.  
Hence  
   ∠(AY,BX)  =  ∠(AX,BX)               (since AX=AY as lines through A)  
              =  ∠(AX,XH)  +  ∠(XH,BX)  
              =  ∠HMX    +  ∠(XH,HB)    (because H,B,X are collinear in that order)  
              =  ∠HMX    +  ∠(HM, MB)  (since HX⊥MX on Γ implies XH⊥MX, so XH∥HM)  
              =  ∠HMX  +  ∠A             (by Lemma 2).  

On the other hand, at Y the same argument (interchanging X↔Y) shows  
   ∠BCY  =  ∠(BC,CY)  
          =  ∠(MB, CY)  
          =  ∠(AX,CY)  
          =  ∠(AX,YH)  +  ∠(YH,CY)  
          =  ∠HMY    +  ∠(MH, HC)  
          =  ∠HMY    +  ∠(HM, MB)  
          =  ∠HMY  +  ∠A.  

But Γ is a circle with diameter HM, so M,X,Y,H all lie on it, which gives  
   ∠HMX  =  ∠HMY    (angles in the same segment).  

It follows that  
   ∠BXY  =  ∠HMX  +  ∠A  
          =  ∠HMY  +  ∠A  
          =  ∠BCY.  

Hence X and Y subtend the same angle at BC, so B,X,Y,C are concyclic.  ■

Putting Lemmas 1–3 together completes the proof: the two tangents from A to the circle on diameter HM meet that circle at X,Y, and one checks by tangent–chord arguments plus the orthocenter condition that ∠BXY=∠BCY, so BXYC is cyclic.  ■
```

## Reviewer Note

A lot of computation mistakes.
