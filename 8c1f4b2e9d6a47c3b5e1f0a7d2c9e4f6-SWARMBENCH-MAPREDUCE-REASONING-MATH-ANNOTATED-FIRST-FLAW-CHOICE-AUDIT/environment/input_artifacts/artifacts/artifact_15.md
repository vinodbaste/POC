# artifact_15

Competition: USAMO  
Problem ID: USAMO_2023_6  
Year: 2023

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \( \triangle ABC \) be a triangle with incenter \( I \) and excenters \( I_a, I_b, I_c \) opposite \( A, B, \) and \( C \), respectively. Given an arbitrary point \( D \) on the circumcircle of \( \triangle ABC \) that does not lie on any of the lines \( II_a, I_bI_c, \) or \( BC \), suppose the circumcircles of \( \triangle DII_a \) and \( \triangle DI_bI_c \) intersect at two distinct points \( D \) and \( F \). If \( E \) is the intersection of lines \( DF \) and \( BC \), prove that \( \angle BAD = \angle EAC \).

## Candidate Excerpts

### Option A

```text
and let F ≠ D be their second intersection.  Finally let E = DF ∩ BC.  We must prove
```

### Option B

```text
Our key claim is that in the orthocentric triangle I_aI_bI_c the point F is exactly the “Miquel–Simson” foot of D which forces DF to be isogonal to DI_a in the angle at A.  Equivalently, one shows that DF is the reflection of the line AD across the internal bisector AI of ∠A, whence its intersection with BC (namely E) is the isogonal‐conjugate of D on BC.  We give the angle‐chase below.
```

### Option C

```text
∠BAD = ∠EAC.
```

### Option D

```text
1.  Since I is the orthocenter of I_aI_bI_c, we have  
 I_bI_c ⟂ IA,  
so ∠(I_bI_c, IA) = 90°.
```

## Full Candidate Proof

```text
Proof.  We begin by recalling two classical facts about the excentral triangle  

Lemma 1 (Orthocentricity of the Excentral Triangle).  In any triangle ABC let I be its incenter and let I_a,I_b,I_c be its excenters opposite A,B,C.  Then in the triangle I_aI_bI_c the point I is the orthocenter, and the feet of the altitudes from I onto the sides I_bI_c, I_cI_a, I_aI_b are precisely A,B,C respectively.  

Proof of Lemma 1.  For example, I_b and I_c both lie on the external bisector of ∠A, whereas I lies on the internal bisector of ∠A, and internal and external bisectors are perpendicular.  Hence I_bI_c ⟂ IA, so A is the foot of the perpendicular from I to I_bI_c.  Two analogous arguments show that B and C are the other two feet.  ∎  

Corollary 2.  The nine‐point circle of triangle I_aI_bI_c is exactly the circumcircle of triangle ABC.  

Proof.  In any triangle the nine‐point circle is the circumcircle of the orthic triangle (the triangle formed by the feet of the altitudes).  In I_aI_bI_c the feet are A,B,C, so the nine‐point circle is (ABC).  ∎  

Now let D be an arbitrary point on the circumcircle (ABC), and (by Corollary 2) on the nine‐point circle of I_aI_bI_c.  Denote by  

 Γ₁ = the circumcircle of triangle D I I_a,  
 Γ₂ = the circumcircle of triangle D I_b I_c,  

and let F ≠ D be their second intersection.  Finally let E = DF ∩ BC.  We must prove  

  ∠BAD = ∠EAC.  

Our key claim is that in the orthocentric triangle I_aI_bI_c the point F is exactly the “Miquel–Simson” foot of D which forces DF to be isogonal to DI_a in the angle at A.  Equivalently, one shows that DF is the reflection of the line AD across the internal bisector AI of ∠A, whence its intersection with BC (namely E) is the isogonal‐conjugate of D on BC.  We give the angle‐chase below.  

1.  Since I is the orthocenter of I_aI_bI_c, we have  
 I_bI_c ⟂ IA,  
so ∠(I_bI_c, IA) = 90°.  

2.  Because F lies on Γ₂ = (D I_b I_c), points D,I_b,I_c,F are concyclic.  Therefore  
 ∠DFI_b = ∠DC I_b  
  (in the circle through D,I_b,I_c)  
but C lies on I_aI_b ⟂ I_cI_a, so in fact  
 ∠DC I_b = 90° – ∠ACI_b = 90° – ∠ACI,  
and one checks by excenter‐incenter angle‐formulas that ∠ACI = A/2.  Hence  
 ∠DFI_b = 90° – (A/2).  

3.  Similarly, F lies on Γ₁ = (D I I_a), so D,I,I_a,F are concyclic, and  
 ∠DFI = ∠DI_a I  
  (in that circle).  
But I lies on the internal bisector at A, and I_a on the external bisector, so II_a ⟂ AI.  Hence  
 ∠DI_a I = 90° – ∠(AI, ID) = 90° – ∠AID.  
Meanwhile ∠AID = 90° + (A/2) (the well‐known incenter angle), so  
 ∠DI_a I = 90° – (90° + A/2) = –(A/2).  
Thus  
 ∠DFI = –(A/2).  

4.  Now compare the two facts:  
 (I) ∠DFI_b = 90° – A/2,  
 (II)  ∠DFI   = –A/2.  
But I_b lies on BC, so line I_bC is just BC, and IA is perpendicular to BC by step 1.  Altogether these give  
 ∠(DF, IA) = ∠DFI_b – ∠IA I_b  
  = (90° – A/2) – 90°  
  = –(A/2)  
  = ∠DFI.  
On the other hand, from (II) we have exactly  
 ∠(IA, AD) = ∠DFI.  
Hence  
 ∠(DF, IA) = ∠(IA, AD).  

But equality of these two (undirected) angles means that the line DF is the reflection of the line AD across the angle‐bisector AI.  Therefore DF is the A‐isogonal of AD, and so its intersection E with BC satisfies  
 ∠BAD = ∠EAC  
(as required).  

∎
```

## Reviewer Note

Incorrect claims, computation mistakes.
