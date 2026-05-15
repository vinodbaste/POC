You are auditing raw AI-generated proposed solutions to an olympiad-level 3D geometry problem about a tetrahedron with an inscribed sphere.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem.md`
- Provenance note for the proposed AI-generated responses: `/input_artifacts/provenance.md`
- Proposed solution files:
  - `/input_artifacts/proposed_solutions/response_A.md`
  - `/input_artifacts/proposed_solutions/response_B.md`
  - `/input_artifacts/proposed_solutions/response_C.md`
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`
  - `/input_artifacts/proposed_solutions/response_G.md`
  - `/input_artifacts/proposed_solutions/response_H.md`
  - `/input_artifacts/proposed_solutions/response_I.md`

Task:
1. Read the problem statement and all nine proposed solutions.
2. Independently determine the gold SET of statement labels (a)..(h) that are necessarily true for every tetrahedron satisfying the two hypotheses. Derive the result yourself from the problem; do not let any candidate's claimed answer influence your gold determination.
3. Determine which proposed response(s), if any, are fully correct (claimed set equals the gold set AND proof contains no defect).
4. For each proposed response A through I, audit whether its claimed set matches the gold set and, if there is any defect in its argument or answer, identify the exact set of concrete failure reasons.
5. Do not decide correctness by majority vote among the proposed responses. Independently solve the gold set first, then audit each response against that result.
6. Do not modify any files in `/input_artifacts`, `/tests`, or `/solution`.

Allowed failure reason codes:
- `rejected_perpendicularity_no_counterexample`: the response rejects statement (a) by asserting that a counterexample exists but never constructs one. The hypothesis is in fact strong enough to force (a).
- `cascaded_rejection_of_e_from_a`: having rejected (a), the response then rejects (e) on the grounds that (e) follows from (a), without checking whether (e) can be defended independently.
- `correct_gtfa_invalid_proof_chain`: the response's stated set equals the gold set, but the proof contains at least one false math claim, unconstructed step, or logical gap, so the proof is invalid even though the final answer is correct.
- `false_universal_insphere_at_face_incenter`: the response uses, as a UNIVERSAL premise, the false claim "the insphere of any tangential tetrahedron is tangent to each face at the face's incenter." This claim is false in general (it requires extra symmetry).
- `confused_centroid_and_incenter`: the response substitutes "centroid of `BCD`" for "incenter of `BCD`" at a load-bearing step, or asserts that "above the centroid" is equivalent to "above the incenter" or to "AI perpendicular to plane BCD." The two points are distinct in any non-equilateral triangle.
- `self_contradictory_centroid_above`: the response proposes a counterexample of the form "A lies directly above the centroid of BCD but is not orthogonal to plane BCD" (or any logically equivalent formulation). This is self-contradictory because "directly above" is the definition of orthogonal projection.
- `vague_word_salad_proofs`: the response defends at least two of the gold claims with vague, non-mathematical phrases (e.g. "by symmetry about A", "by the circumcircle properties dictated by the dihedral angles", "by definition of the inradius") that do not engage with hypothesis (2).
- `cot_trace_misses_distance_equivalence`: the response (typically with a visible chain-of-thought) derives the area-over-base identity `area(ABX)/BX = (1/2)*dist(A, line BX)` or `area(ABC)/BC = area(ACD)/CD = area(ABD)/DB` but explicitly fails to convert it to the equal-distance condition `dist(A, BC) = dist(A, CD) = dist(A, DB)`, ultimately rejecting (c) in spite of having just derived it.
- `repeats_false_universal_in_e`: while defending (e), the response restates or paraphrases the false universal "the insphere of any tangential tetrahedron is tangent at the face-incenter."
- `vague_almost_regular_nonconstruction`: the response dismisses one or more of the gold claims with phrases like "consider a tetrahedron that is almost regular but slightly skewed" or "it is possible to construct" without any concrete construction.
- `rejects_e_via_general_property_misapplied`: the response rejects (e) by appealing to a general property of inspheres (e.g. "the insphere touch point is not in general the incenter of the face") that is true in isolation but ignores whether the specific hypothesis (2) forces these two points to coincide here, which it does.
- `false_claim_ai_equals_inradius`: the response asserts the false equality `AI = r` (distance from vertex `A` to incenter `I` equals the inradius). Since `I` is interior to the tetrahedron and `r` is the perpendicular distance from `I` to each face, `AI > r` in general.
- `incoherent_ratio_argument_in_b`: when defending or rejecting statement (b), the response produces an incoherent ratio or proportion argument (often invoking a 1:1 ratio between `AI` and `r`, or comparing `dist(A, plane BCD)` to `r` via an unjustified ratio).
- `degenerate_counterexample_b_equals_c`: the response's "counterexample" amounts to a degenerate tetrahedron (e.g. `B = C` or collinear `B, C, D`), which does not satisfy the hypotheses.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `final_answer_correct`: `true` exactly when the response's claimed SET of necessarily-true statement labels equals the gold set (as a set; order irrelevant). Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes. Use an empty list exactly when the response's claimed set equals the gold AND the proof has no defect. If there is any defect, include every applicable concrete failure reason and no inapplicable reason.

Important scoring note:
The response audit is evaluated as an exact audit. Extra failure reasons and missing failure reasons are both wrong. Do not include a broad reason unless it is genuinely needed to explain that response's defects.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "gold_set": ["<lowercase letters a..h, alphabetical>"],
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": <true or false>,
      "failure_reasons": ["<zero or more allowed failure reason codes>"]
    }
  ]
}

In the actual output, include nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that order. Do not write anything else to that file.
