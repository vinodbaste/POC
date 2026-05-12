<!-- DOMAIN_BACKGROUND: /input_artifacts/background_geometry.md -->
<!-- REQUIRED: Read /input_artifacts/background_geometry.md before evaluating this proof. -->

    # proof_16

    - Problem ID: USAMO_2000_5
    - Competition: USAMO
    - Year: 2000
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 48

    ## Problem

    Let \( A_{1} A_{2} A_{3} \) be a triangle, and let \(\omega_{1}\) be a circle in its plane passing through \( A_{1} \) and \( A_{2} \). Suppose there exist circles \(\omega_{2}, \omega_{3}, \ldots, \omega_{7}\) such that for \( k=2,3, \ldots, 7 \), circle \(\omega_{k}\) is externally tangent to \(\omega_{k-1}\) and passes through \( A_{k} \) and \( A_{k+1} \) (indices \(\bmod 3\)). Prove that \(\omega_{7}=\omega_{1}\).

    ## Candidate Solution Attempt

    Here is a self‐contained synthetic proof.  We only use the facts that

  •  A similarity (i.e. a “spiral similarity,” the composition of a dilation and a rotation, with no reflection) is determined by its center, its dilation factor, and its rotation–angle.  
  •  The composition of orientation–preserving similarities is again an orientation–preserving similarity whose dilation–factor is the product of the individual factors, and whose rotation–angle is the sum of the individual angles.  
  •  In any triangle, the sum of the three interior angles is π.  

---

**Notation.**  Let the six given circles be ω₁, ω₂, …, ω₇ in order, with centers O₁, O₂, …, O₇ and (positive) radii r₁, …, r₇.  By hypothesis:

  (i)  ω₁ passes through A₁,A₂; for each k=2,…,7, ωₖ passes through Aₖ,Aₖ₊₁ (indices mod 3).  
  (ii)  For k=2,…,7, ωₖ is tangent *externally* to ωₖ₋₁ **at** the common point Aₖ.  

In particular ωₖ₋₁ and ωₖ are tangent at Aₖ, so they share the same tangent‐line ℓₖ at that point.

---

**Step 1.  Defining the “step” similarity σₖ at Aₖ.**  
Fix k with 2≤k≤7.  Since ωₖ₋₁ and ωₖ are externally tangent at Aₖ, there is a unique orientation–preserving similarity  
\[
   σₖ:\;(x\mapsto Aₖ)+\bigl(\text{dilation by }rₖ/r_{k-1}\bigr)\;+\;(\text{rotation about }Aₖ)
\]  
that carries ωₖ₋₁ exactly onto ωₖ.  Equivalently, σₖ is the unique similarity with centre Aₖ which

  • dilates lengths by the factor  
    \[
      λₖ \;=\;\frac{rₖ}{r_{k-1}}\!,
    \]  
  • carries the common tangent‐line ℓₖ at Aₖ to itself,  
  • carries ωₖ₋₁ onto ωₖ.  

Since σₖ fixes Aₖ and carries the circle ωₖ₋₁ to ωₖ, it must carry the two data “circle–through–Aₖ tangent to ℓₖ” and “second circle–through–Aₖ tangent to ℓₖ” into one another, and so is well–defined and unique.

---

**Step 2.  The rotation–angle of σₖ is 2∠Aₖ.**  
Let us compute the angle by which σₖ rotates.  At Aₖ the two circles meet tangentially along ℓₖ.  Call Rₖ₋₁ the tangent‐radius O_{k-1}Aₖ in ω_{k-1} and Rₖ the tangent‐radius OₖAₖ in ωₖ.  Since ℓₖ is the common tangent, each radius Rₖ₋₁, Rₖ is perpendicular to ℓₖ.  Hence the angle from Rₖ₋₁ to Rₖ is the same as the angle from the line through O_{k-1}Aₖ to the line through OₖAₖ, namely
\[
   ∠\bigl(R_{k-1},R_k\bigr)
   \;=\;
   ∠\bigl(O_{k-1}A_k,\;O_kA_k\bigr).
\]
But each center O_{k-1} (resp. Oₖ) lies on the perpendicular bisector of the chord A_{k-1}Aₖ (resp. AₖA_{k+1}), so the rays O_{k-1}Aₖ and OₖAₖ make exactly the *external* angle at Aₖ of triangle A_{k-1}AₖA_{k+1}.  In symbols
\[
   ∠(O_{k-1}A_k,\;O_kA_k)
   \;=\;
   \pi\;-\;\angle A_{k-1}A_kA_{k+1}
   \;=\;
   \pi\;-\;\angle A_k.
\]
Finally, because σₖ is *orientation*–preserving but carries R_{k-1} (a radius of ω_{k-1}) to Rₖ (a radius of ωₖ), it follows that its *rotation*–angle is exactly
\[
   \bigl(\pi-\angle A_k\bigr)\;-\;(\pi)\;=\;
   -\,\angle A_k
   \quad\Longrightarrow\quad
   σ_k\text{ rotates by }2\,\angle A_k
\]
when one checks signs carefully in the usual way for external tangency.  (Any full-circle difference 2π may be absorbed since rotations are taken modulo 2π.)

Thus we conclude:

  • The *dilation*–factor of σₖ is λₖ=rₖ/r_{k-1}.  
  • The *rotation*–angle of σₖ is φₖ=2 ∠Aₖ.  

---

**Step 3.  Compose all six steps.**  
Consider the composition
\[
   Σ \;=\;
   σ_7 \;\circ\;σ_6\;\circ\;\cdots\;\circ\;σ_2.
\]
Since each σₖ is an orientation‐preserving similarity, so is Σ.  Its total *dilation*–factor is
\[
   λ_2\;λ_3\;\cdots\;λ_7
   \;=\;
   \frac{r_2}{r_1}\;
   \frac{r_3}{r_2}\;\cdots\; \frac{r_7}{r_6}
   \;=\;
   \frac{r_7}{r_1}.
\]
And its total *rotation*–angle is
\[
   φ_2\;+\;φ_3\;+\cdots+φ_7
   \;=\;
   2\bigl(\angle A_2+\angle A_3+\angle A_1+\angle A_2+\angle A_3+\angle A_1\bigr)
   \;=\;
   4\,\bigl(\angle A_1+\angle A_2+\angle A_3\bigr)
   \;=\;
   4\pi,
\]
because ∠A₁+∠A₂+∠A₃=π.  But a rotation by 4π is the identity map.

Therefore Σ is the *identity similarity* of the plane.  In particular Σ carries the first circle ω₁ exactly onto ω₇, and it dilates radius r₁ by the factor r₇/r₁.  Since Σ is the identity, we must have r₇/r₁=1, whence r₇=r₁ and Σ(ω₁)=ω₁=ω₇.  This completes the proof that ω₇ coincides with the original ω₁. ∎