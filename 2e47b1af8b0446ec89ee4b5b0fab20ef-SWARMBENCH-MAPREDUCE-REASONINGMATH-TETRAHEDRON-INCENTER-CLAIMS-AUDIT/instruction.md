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
2. Independently determine the gold SET of statement labels (a)..(h) that are necessarily true for every tetrahedron satisfying the two hypotheses.
3. Determine which proposed response(s), if any, are fully correct (claimed set equals the gold set AND proof contains no load-bearing defect).
4. For each proposed response A through I, audit whether its claimed set matches the gold set and identify the exact set of concrete failure reasons present in its argument, drawn from the allowed vocabulary below.
5. Do not decide correctness by majority vote among the proposed responses. Independently solve the gold set first, then audit each response against that result.

Allowed failure reason codes:
- `rejected_perpendicularity_no_counterexample`: TRIGGER — the response rejects statement (a) (`AI ⊥ plane BCD`) by asserting that a counterexample exists, but never constructs one. The hypothesis is in fact strong enough to force (a). Apply ONLY when the response explicitly rejects (a) AND writes language like "counterexample exists" / "we can have a tetrahedron where..." without producing a concrete construction.
- `cascaded_rejection_of_e_from_a`: TRIGGER — having rejected (a), the response then rejects (e) on the explicit grounds that (e) follows from (a). Apply ONLY when the rejection of (e) is justified by reference to its dependence on (a).
- `correct_gtfa_invalid_proof_chain`: TRIGGER — the response's stated final answer set equals the gold set, but at least one step of its proof contains a false math claim or a load-bearing logical gap. Apply ONLY when both conditions hold: stated set is exactly gold AND proof has a load-bearing wrong claim.
- `false_universal_insphere_at_face_incenter`: TRIGGER — the response uses, as a UNIVERSAL premise, the false claim "the insphere of any tangential tetrahedron is tangent to each face at the face's incenter." Apply ONLY when the response uses this universal claim as a premise (not when it correctly derives the touch point from the specific hypothesis here).
- `confused_centroid_and_incenter`: TRIGGER — the response substitutes the word "centroid" of `BCD` where the correct point is the "incenter" of `BCD` at a load-bearing step. Apply ONLY when "centroid" actually appears in the response at a position where "incenter" is required.
- `self_contradictory_centroid_above`: TRIGGER — the response proposes a counterexample of the form "A lies directly above the centroid of BCD but is not orthogonal" or any logically equivalent formulation. Apply ONLY when this specific self-contradictory construction appears verbatim or near-verbatim in the response.
- `false_claim_ai_equals_inradius`: TRIGGER — the response asserts the equality `AI = r` (distance from vertex `A` to incenter `I` equals the inradius). Apply ONLY when `AI = r` (or its mathematical equivalent) is asserted as a load-bearing claim.
- `vague_almost_regular_nonconstruction`: TRIGGER — the response dismisses one or more of the gold claims with phrases like "almost regular", "slightly skewed", or "it is possible to construct" without any concrete construction. Apply ONLY when this hand-wave phrase appears AND no concrete tetrahedron is exhibited.
- `cot_trace_misses_distance_equivalence`: TRIGGER — the response derives `area(ABC)/BC = area(ACD)/CD = area(ABD)/DB` (the area-over-base ratio identity) but explicitly fails to convert it to `dist(A, BC) = dist(A, CD) = dist(A, DB)`, then rejects (c). Apply ONLY when both halves are observable: the ratio is derived AND (c) is rejected.
- `rejects_e_via_misapplied_general_property`: TRIGGER — the response rejects (e) by appealing to a general property of inspheres (e.g. "the insphere touch point is not in general the incenter of the face") without checking whether the specific hypothesis (2) forces these two points to coincide here. Apply ONLY when the rejection of (e) cites a general fact about inspheres without reference to (2).

Important scoring and selection rules:
- The audit is evaluated as an EXACT set match per response. Extra failure reasons and missing failure reasons both score zero for that response.
- **Most responses have 0, 1, or 2 failure reasons.** Apply a code only when its TRIGGER condition is directly observable in the response text. Do not apply borderline or stylistic codes. Do not apply a code whose trigger phrase is only present in a different response.
- Use an empty list `[]` for failure_reasons exactly when the response's claimed set equals the gold set AND its proof has no load-bearing defect (i.e. no trigger from the vocabulary is concretely instantiated).
- `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of response_ids whose `final_answer_correct` is `true` AND whose `failure_reasons` is the empty list.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `final_answer_correct`: `true` exactly when the response's claimed SET of necessarily-true statement labels equals the gold set (as a set; order irrelevant). Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes above.

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
