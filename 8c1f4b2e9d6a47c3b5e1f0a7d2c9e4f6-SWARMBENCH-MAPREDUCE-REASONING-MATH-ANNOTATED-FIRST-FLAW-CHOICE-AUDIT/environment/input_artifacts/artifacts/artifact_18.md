# artifact_18

Competition: IMOSL  
Problem ID: IMOSL_2022_24  
Year: 2022

Human annotation sourced from the Open Proof Corpus (INSAIT-Institute/OPC). The reviewer's free-form note identified a first logical error; four candidate proof windows have been curated from the incorrect attempt. Select the one window that spans the human-marked flaw.

## Problem

Let \( \triangle ABC \) and \( \triangle A'B'C' \) be two triangles having the same circumcircle \(\omega\), and the same orthocenter \(H\). Let \(\Omega\) be the circumcircle of the triangle determined by the lines \(AA', BB'\), and \(CC'\). Prove that \(H\), the center of \(\omega\), and the center of \(\Omega\) are collinear.

## Candidate Excerpts

### Option A

```text
1.  Perpendicular bisector of A A′ passes through O and H.  
Since H is the orthocenter of ΔA′B′C′, the line HA′ is perpendicular to the side B′C′.  But B′C′ is a chord of ω, so the perpendicular from the center O to the chord B′C′ is the perpendicular bisector of B′C′;  in particular it is perpendicular to B′C′ and passes through O.  Now HA′ is also perpendicular to B′C′, so HA′∥(the perpendicular bisector of B′C′).  Hence HA′ and the perpendicular bisector of B′C′ coincide.  But A lies on ω, and A′ lies on ω, so the perpendicular bisector of the chord A A′ is also perpendicular to AA′ and passes through O.  Since AA′∥HA′, that same line is the perpendicular bisector of AA′.  Thus
```

### Option B

```text
Proof.  
Let ω be the common circumcircle of ΔABC and ΔA′B′C′, and let O be its center.  Let H be their common orthocenter.  Finally, let ℓ_A=AA′, ℓ_B=BB′, ℓ_C=CC′, and write
 L=ℓ_A∩ℓ_B,\quad M=ℓ_B∩ℓ_C,\quad N=ℓ_C∩ℓ_A,
and let Ω be the circumcircle of triangle LMN, with center O′.  We must show that O,H,O′ are collinear.
```

### Option C

```text
Exactly the same argument (cycling A→B→C) shows
```

### Option D

```text
•  the perpendicular bisector of AA′ passes through O and H,
and in particular O A=O A′ and H A=H A′.
```

## Full Candidate Proof

```text
Below is a synthetic proof.  I have tried to make every step precise.  Admittedly, the key “coaxal–Miquel” step at the end is rather classical and a bit tricky in the bookkeeping of which circles meet where;  I have flagged it clearly.  If any lemma there seems unfamiliar, one can unpack it into a short angle‐chase plus power‐of‐a‐point argument.

Proof.  
Let ω be the common circumcircle of ΔABC and ΔA′B′C′, and let O be its center.  Let H be their common orthocenter.  Finally, let ℓ_A=AA′, ℓ_B=BB′, ℓ_C=CC′, and write
 L=ℓ_A∩ℓ_B,\quad M=ℓ_B∩ℓ_C,\quad N=ℓ_C∩ℓ_A,
and let Ω be the circumcircle of triangle LMN, with center O′.  We must show that O,H,O′ are collinear.

1.  Perpendicular bisector of A A′ passes through O and H.  
Since H is the orthocenter of ΔA′B′C′, the line HA′ is perpendicular to the side B′C′.  But B′C′ is a chord of ω, so the perpendicular from the center O to the chord B′C′ is the perpendicular bisector of B′C′;  in particular it is perpendicular to B′C′ and passes through O.  Now HA′ is also perpendicular to B′C′, so HA′∥(the perpendicular bisector of B′C′).  Hence HA′ and the perpendicular bisector of B′C′ coincide.  But A lies on ω, and A′ lies on ω, so the perpendicular bisector of the chord A A′ is also perpendicular to AA′ and passes through O.  Since AA′∥HA′, that same line is the perpendicular bisector of AA′.  Thus

 •  the perpendicular bisector of AA′ passes through O and H,
and in particular O A=O A′ and H A=H A′.

Exactly the same argument (cycling A→B→C) shows

 •  O B=O B′,\;H B=H B′,
 •  O C=O C′,\;H C=H C′.

2.  The three circles through H and a pair of corresponding vertices are coaxal with axis OH.  
Let Γ_A be the circle through H, B, C;  let Γ_{A′} be the circle through H, B′, C′.  Both Γ_A and Γ_{A′} pass through H, and each meets ω again in the two points B,C (resp. B′,C′).  By step 1 we saw that O and H lie on the perpendicular bisector of BB′ and of CC′;  hence

 •  O and H are equidistant from B and B′,
 •  O and H are equidistant from C and C′.

Therefore O and H have equal power to both ω and to Γ_A∪Γ_{A′}.  In particular:

 –  The radical axis of ω and of Γ_A is the line BB′;  
 –  The radical axis of ω and of Γ_{A′} is the line CC′.  

Since O and H have equal power to ω and to either of these two circles, OH is perpendicular to both BB′ and CC′.  It follows that the radical axes BB′ and CC′ of the two pairs {ω,Γ_A} and {ω,Γ_{A′}} meet on OH.  Consequently the three circles ω, Γ_A, Γ_{A′} are coaxal with common radical axis ℓ_AA′=BB′∩CC′ lying on OH.  

Likewise, if we set
 Γ_B={H, C, A}∪{H, C′, A′},  
 Γ_C={H, A, B}∪{H, A′, B′},  
then each triple {ω,Γ_B}, {ω,Γ_C} is coaxal with radical axes ℓ_B=CC′∩AA′ and ℓ_C=AA′∩BB′, and all these radical axes lie on the same line OH.  Thus in total

 The four circles ω,Γ_A,Γ_B,Γ_C are coaxal, with common radical‐axis OH.

3.  Miquel‐coaxality ⇒ O′∈OH.  
Now look at the triangle formed by the three lines ℓ_A,ℓ_B,ℓ_C.  Its vertices are L=ℓ_A∩ℓ_B, M=ℓ_B∩ℓ_C, N=ℓ_C∩ℓ_A.  By the usual Miquel‐circle argument (or “pivot theorem”), the unique circle through L,M,N is also the common circumcircle of the three triangles

 Δ(LHM),\quad Δ(MHN),\quad Δ(NHL).

But Δ(LHM) lies on the two coaxal circles Γ_A and Γ_B, Δ(MHN) lies on Γ_B and Γ_C, and Δ(NHL) lies on Γ_C and Γ_A.  Since all Γ_A,Γ_B,Γ_C were already shown to be coaxal with ω along OH, their Miquel circle Ω is likewise coaxal with them:  its center O′ must lie on the same axis.  In particular

 O′ lies on OH.

That is exactly the desired collinearity of O, H, O′.  ■

Remark.  The heart of the proof is the “coaxal‐Miquel” principle:

 If three circles Γ_1,Γ_2,Γ_3 are each coaxal with a fixed circle ω along a line ℓ,  
 and if you form the triangle of their pairwise radical‐axes,  
 then the Miquel circle of that little triangle is again coaxal with ω,Γ_1,Γ_2,Γ_3 along the same line ℓ.

Applied here with Γ_1=Γ_A, Γ_2=Γ_B, Γ_3=Γ_C and ω the common circumcircle, the radical‐axes are exactly AA′,BB′,CC′, their triangle is LMN, and its Miquel circle is Ω.  Since all four of ω,Γ_A,Γ_B,Γ_C share the same radical‐axis OH, so does Ω, forcing its center O′∈OH.
```

## Reviewer Note

Computation mistakes.
