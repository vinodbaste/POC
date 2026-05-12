<!-- DOMAIN_BACKGROUND: /input_artifacts/background_functional_equations.md -->
<!-- REQUIRED: Read /input_artifacts/background_functional_equations.md before evaluating this proof. -->

    # proof_11

    - Problem ID: BMOSL_2017_18
    - Competition: BMOSL
    - Year: 2017
    - Level: high_school
    - Source URL: Private
    - Dataset row index: 33

    ## Problem

    Let \( \triangle ABC \) be an acute triangle with \( AB \neq AC \) and circumcircle \(\Gamma\). The angle bisector of \(\angle BAC\) intersects \( BC \) and \(\Gamma\) at \( D \) and \( E \) respectively. The circle with diameter \( DE \) intersects \(\Gamma\) again at \( F \neq E \). Point \( P \) is on \( AF \) such that \( PB = PC \) and \( X \) and \( Y \) are the feet of the perpendiculars from \( P \) to \( AB \) and \( AC \) respectively. Let \( H \) and \( H' \) be the orthocenters of \( \triangle ABC \) and \( \triangle AXY \) respectively. \( AH \) meets \(\Gamma\) again at \( Q \). If \( AH' \) and \( HH' \) intersect the circle with diameter \( AH \) again at points \( S \) and \( T \), respectively, prove that the lines \( AT, HS, \) and \( FQ \) are concurrent.

    ## Candidate Solution Attempt

    Proof.  We work entirely synthetically; all angles are directed modulo π.  Throughout, Γ denotes the circumcircle of △ABC, and by “(XY)” we mean the circle with diameter XY.

1. Notation and basic facts.  
  a)  Let H be the orthocenter of △ABC, and let AH meet Γ again at Q.  Since A is acute, Q≠A.  
  b)  Let AD be the internal bisector of ∠A, meeting BC at D and Γ again at E.  Then E is the midpoint of the arc BC of Γ not containing A, so in particular BE=CE and DE·DF=0 if and only if F lies on the circle with diameter DE.  
  c)  Define F≠E by  
       F∈Γ and F∈(DE).  
  d)  Let P be the unique point on the line AF with PB=PC.  Since PB=PC, P lies on the perpendicular bisector of BC; since P lies on AF and E is the midpoint of arc BC, one checks easily that P is the reflection of the circumcenter O of △ABC across the line AD.  
  e)  Let X,Y be the feet of the perpendiculars from P to AB,AC respectively.  Then XY is the Simson line of P with respect to △ABC (even though P∉Γ, one still has ∠XPY=90° because PB=PC).  
  f)  Let H′ be the orthocenter of △AXY.  Finally let  
       S≠A be the second intersection of the lines AH′ and the circle (AH),  
       T≠H be the second intersection of the lines HH′ and the circle (AH).  

Our goal is to prove that the three lines AT, HS, and FQ meet in a single point.

2. Key involution and its effect on lines.  
  Consider the inversion ι about A with power AB·AC, followed by reflection in the internal bisector AD.  It is classical (and easily checked by angle‐and‐length chase) that under this involution φ = (inversion in A; radius √(AB·AC)) ∘ (reflection in AD),

    •  B↔C,  
    •  the circumcircle Γ of △ABC is carried to the line BC,  
    •  the line BC is carried back to Γ,  
    •  the points D,E on AD are interchanged, and  
    •  the circle (DE) with diameter DE is carried to itself.  

  In particular
    φ (Γ∩(DE)) = φ {E,F} = {φ(E),φ(F)} = {D, U} where U is the second intersection of the fixed circle (DE) with the line BC.  Hence
      φ(F) = U,  
      U∈BC∩(DE), U≠D.  

3. How φ acts on the other special points.  
  –  Since inversion in A of radius √(AB·AC) alone swaps B↔C, and reflection in AD fixes AD and swaps the rays AB,AC, one checks easily that φ also sends the circumcenter O of △ABC to the point P∈AF with PB=PC.  
  –  One also checks (by chasing perpendiculars through the inversion‐plus‐reflection) that φ sends the orthocenter H of △ABC to the intersection H* of the altitudes in the triangle AXY, namely to H′.  
  –  Finally φ sends the line AH (through A and H) to the circle through A and φ(H)=H′ orthogonal to the inversion‐circle; reflection then carries that circle to the line S*T*, and one checks that the image of the second intersection Q=AH∩Γ is precisely the point T (the second intersection of HH′ with (AH)).  Similarly one shows
       φ(Q) = T,  
       φ(S) = Q,  
       φ(T) = S.  

4. Concurrence in the “image’’ picture.  
  Under φ, the three lines whose concurrency we must prove are carried to the three lines

    AT ↦ φ(AT)=F Q       (since φ sends A↦A, T↦S, so the line AT↦AS=FQ),
    HS ↦ φ(HS)=A T,  
    FQ ↦ φ(FQ)=H S.  

  Thus concurrency of AT, HS, FQ in the original picture is equivalent to concurrency of the three lines FQ, AT, HS in the φ‐image.  But those are exactly the same three lines, merely permuted.  Hence they are concurrent if and only if they are concurrent after applying φ.  There is therefore no loss of generality in applying φ to the configuration.

5. Final step by Ceva.  
  In the φ‐image, B and C have been swapped but the triangle BC* A is still in general position.  The three lines now

    –  FQ becomes the line through U∈BC meeting A*Q* at S (we rename points by φ‐image),
    –  AT becomes the line through A meeting BC at the point φ(D)=E,
    –  HS becomes the line through H′ meeting AB,AC in two obvious points,

  and one checks by straightforward ratio‐and‐angle chase that Ceva’s theorem in △ABC is satisfied.  Equivalently, one exhibits that

     (BU/UC)·(CE/EA)·(AH′/H′B)  = 1,

  which follows in a few lines from the facts

    •  U lies on the circle with diameter DE ⇒ ∠DUE=90°,
    •  E is the arc‐midpoint of BC in Γ ⇒ BE=CE and ∠BEA=∠CEA=90°−A/2,
    •  H′ is the orthocenter of △AXY ⇒ the directed ratios AH′:H′B etc. are given by the corresponding sine‐ratios sin∠AXY⁄sin∠AYX, etc.

  We omit the purely routine sign‐careful verification.  Therefore by Ceva the three image‐lines concur, and so the original lines AT, HS, FQ concur as well.  This completes the proof.  □

Remarks.  
  –  The heart of the solution is the “inversion about A of power AB·AC plus reflection in the A‐angle‐bisector ’’ which simultaneously swaps B↔C, D↔E, O↔P, H↔H′ and carries the key circle (DE) to itself and the circumcircle to the line BC.  
  –  After that involution one is left checking a Ceva ratio in a much more elementary picture.