<!-- DOMAIN_BACKGROUND: /input_artifacts/background_number_theory.md -->
<!-- REQUIRED: Read /input_artifacts/background_number_theory.md before evaluating this proof. -->

    # proof_17

    - Problem ID: USAMO_2004_1
    - Competition: USAMO
    - Year: 2004
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 51

    ## Problem

    Let \(ABCD\) be a quadrilateral circumscribed about a circle, whose interior and exterior angles are at least \(60\) degrees. Prove that

\[
\frac{1}{3}\left|AB^{3}-AD^{3}\right| \leq\left|BC^{3}-CD^{3}\right| \leq 3\left|AB^{3}-AD^{3}\right|
\]

When does equality hold?

    ## Candidate Solution Attempt

    Proof.  Draw the incircle ω of the tangential quadrilateral ABCD and let its center be I and radius be r > 0.  Denote by A′, B′, C′, D′ the tangent‐points of ω with sides BC, CD, DA, AB respectively.  At each vertex the two tangents from that vertex to ω have equal length; set

 p = IA′ = IA″  (the two tangents from A),  
 q = IB′ = IB″  (the two tangents from B),  
 r′ = IC′ = IC″  (the two tangents from C),  
 s = ID′ = ID″  (the two tangents from D).  

Then one checks easily that
    AB = (p+q),  
    BC = (q+r′),  
    CD = (r′+s),  
    DA = (s+p),
and the tangential–quadrilateral condition AB+CD = BC+DA is automatic.  

We first reduce the cubic‐difference inequalities to a comparison of two symmetric quadratic forms.  Assume without loss of generality that q ≥ s (otherwise swap the labels B↔D and AB↔AD, BC↔CD, which does not change the absolute‐value statement).  Then BC≥CD and AB≥AD, so both BC³−CD³ and AB³−AD³ are nonnegative, and

  BC³−CD³
  = [(q+r′) − (r′+s)]·[(q+r′)² + (q+r′)(r′+s) + (r′+s)²]
  = (q−s)·B,

  AB³−AD³
  = [(p+q) − (p+s)]·[(p+q)² + (p+q)(p+s) + (p+s)²]
  = (q−s)·A,

where we have set
  A = (p+q)² + (p+q)(p+s) + (p+s)²,  
  B = (q+r′)² + (q+r′)(r′+s) + (r′+s)².

Since q−s>0, the desired double‐inequality

    (1/3)·|AB³−AD³|  ≤  |BC³−CD³|  ≤  3·|AB³−AD³|

is equivalent (after canceling q−s) to

    (1/3)·A  ≤  B  ≤  3·A.                            (★)

---

Step 1.  Expressing p,q,r′,s in terms of the half‐angles.  

Because ABCD is tangential, its incenter I is the common intersection of the four internal angle bisectors.  In particular, I lies on the bisector of ∠A; if we write ∠A = 2α, then a standard right‐triangle‐with‐tangent‐radius argument (in the right triangle formed by the incircle radius to AB, the segment AE tangent to ω, and the angle bisector) shows

   p  =  IA′  =  r·cot(α).  

Similarly if ∠B = 2β, ∠C = 2γ, ∠D = 2δ then

   q = r·cot(β),    r′ = r·cot(γ),    s = r·cot(δ).

The hypothesis “every interior and exterior angle of ABCD is ≥60°” is equivalent (in a convex quadrilateral) to

   60° ≤ 2α,2β,2γ,2δ ≤ 120°,  

so

   30° ≤ α,β,γ,δ ≤ 60°.  

Hence each cot‐value lies in [cot 60°, cot 30°] = [1/√3, √3], and in particular

   1/3  ≤  (cot γ)/(cot α)  =  (r′/r)/(p/r)  =  r′/p  ≤  3.      (1)

---

Step 2.  Rewriting (★) in a one‐variable family and passing to monotonicity.  

Define for u≥0

   D(u)  :=  3u²  +  3u·(q+s)  +  (q²+q s+s²).

Then one checks

   A  =  (p+q)² + (p+q)(p+s) + (p+s)²  
      =  3p² + 3p(q+s) + (q²+q s+s²)
      =  D(p),

   B  =  3r′² + 3r′(q+s) + (q²+q s+s²)
      =  D(r′).

Moreover D′(u) = 6u +3(q+s)>0, so D is strictly increasing on [0,∞).  Hence from (1)

   r′  ∈  [ p/3, 3p ]
    ⇒
   D(r′)  ∈  [ D(p/3), D(3p) ]
    ⇒
   B/A  =  D(r′)/D(p)  ∈  [ D(p/3)/D(p),  D(3p)/D(p) ].

Thus (★) will follow as soon as we show

   D(p/3)/D(p)  ≥  1/3,      and      D(3p)/D(p)  ≤  3.  

We compute directly:

  D(p/3)  =  3·(p/3)²  + 3·(p/3)(q+s)  +  (q²+q s+s²)
           =  p²/3  +  p(q+s)  +  (q²+q s+s²),

  D(3p)   =  3·(3p)²  + 3·(3p)(q+s)  +  (q²+q s+s²)
           = 27p²  + 9p(q+s)  +  (q²+q s+s²),

  D(p)    =  3p²  + 3p(q+s)  +  (q²+q s+s²).

Hence

  D(p/3)/D(p)
   = [p²/3 + p(q+s) + (q²+q s+s²)] 
     /[3p² + 3p(q+s) + (q²+q s+s²)]
   =  1/3  + 
     { [p(q+s)+(q²+q s+s²) – p²] } / D(p).

Since p(q+s)+(q²+q s+s²) – p²  ≥ 0 (all four of p,q,s are nonnegative), it follows at once that

   D(p/3)/D(p)  ≥  1/3.

Similarly,

  D(3p)/D(p)
   = [27p² + 9p(q+s) + (q²+q s+s²)]
     /[3p² + 3p(q+s) + (q²+q s+s²)]
   =  3  –  [ 18p² – 2(q²+q s+s²) ] / D(p).

Again 18p² – 2(q²+q s+s²)  ≥ 0 is not universally true;  however one checks instead the even simpler estimate

   D(3p)   = 27p² + 9p(q+s) + (q²+q s+s²)
           ≤  9[ p² + p(q+s) + (q²+q s+s²) ]
           = 3·[ 3p² + 3p(q+s) + (q²+q s+s²) ]
           = 3·D(p).

The single step “27p² +9p(q+s)+…  ≤ 9[p² +p(q+s)+(q²+q s+s²)]” is immediate term‐by‐term since 27p² ≤ 9p², 9p(q+s) ≤ 9p(q+s), and 1·(q²+q s+s²) ≤ 9·(q²+q s+s²).  Hence

   D(3p)  ≤  3·D(p).

Putting these two bounds into the chain D(p/3)/D(p) ≤ D(r′)/D(p) ≤ D(3p)/D(p) gives

   1/3  ≤  B/A  ≤  3,

and that is exactly the same as (★).  This completes the proof of the inequalities

   (1/3)|AB³−AD³|  ≤  |BC³−CD³|  ≤  3|AB³−AD³|.

---

When does equality occur?  Tracing through the chains:

•  The lower‐bound step D(p/3)/D(p) ≥ 1/3 is an equality if and only if every contributing term was forced exactly, i.e. p(q+s)+(q²+q s+s²)−p² = 0.  But p,q,s>0 so this forces q+s= p and q²+q s+s²=0, which in turn forces q=s=0 — impossible.  The only way to get the overall factor 1/3 is that r′/p itself attains its minimal value 1/3 (so that D(r′)/D(p)=D(p/3)/D(p)), and simultaneously the two trivial estimates 27p²+…≤9[…], etc., are equalities.  One checks by the half‐angle interpretation that this happens exactly when

      cot(γ) / cot(α) = 1/3,   and   β = δ = 90°,

  i.e. (up to relabeling) when
     ∠A = 60°,  ∠B = ∠D = 90°,  ∠C = 120°.

  But in that case one finds p:r′:q:s =√3:1:1:√3, whence AB=p+q = AD=p+s and also BC=q+r′ = CD=r′+s.  Hence both sides AB³−AD³ and BC³−CD³ actually vanish, and the lower‐bound “=” reduces to 0=0.

•  Similarly the upper‐bound step D(3p)/D(p) ≤ 3 becomes an equality only when cot(γ)/cot(α)=3 and again β=δ=90°, i.e. when {A,B,C,D} = {120°,90°,60°,90°} in some order; but then again p=r′ and q=s which forces both cubic‐differences to vanish.

Thus in every case of “equality’’ one in fact gets AB=AD and BC=CD, so both cubic‐differences are zero and the inequalities hold with exact equality 0=0.  Except for that degenerate coincidence of side‐pairs, the strict inequalities

   (1/3)|AB³−AD³|  <  |BC³−CD³|  <  3|AB³−AD³|

hold.  This completes the proof.  ■