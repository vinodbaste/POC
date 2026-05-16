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
3. Determine which proposed response(s), if any, are fully correct (claimed set equals the gold set AND no failure reason fires on their proof).
4. For each proposed response A through I, audit whether its claimed set matches the gold set and identify the exact set of failure reasons whose phrase trigger is concretely instantiated in that response.
5. Do not decide correctness by majority vote among the proposed responses. Independently solve the gold set first, then audit each response against that result.

Allowed failure reason codes (phrase-triggered; each code applies ONLY when its trigger phrase or its near-verbatim paraphrase is present in that single response's text):

- `asserts_AI_equals_r`
  - TRIGGER: the response asserts the equality "AI = r" (the distance from vertex A to the incenter I equals the inradius r) as a load-bearing claim. Look for the literal phrase "AI = r" or any direct paraphrase asserting equality of AI to the inradius. This claim is mathematically false in general because I is strictly interior to the tetrahedron.

- `rejects_a_with_we_can_have_assertion`
  - TRIGGER: the response REJECTS statement (a) — that is, the response's FINAL claimed set of necessarily-true statements does NOT contain "a" — AND the rejection is justified by a sentence of the form "we can have a tetrahedron satisfying (2) where AI is not perpendicular to BCD" or its near-verbatim paraphrase, without producing a concrete construction. If the response includes (a) in its final claimed set, this trigger does NOT fire, even if a "we can have / counterexample" sentence appears earlier in the response's reasoning.

- `asserts_universal_face_incenter_tangency`
  - TRIGGER: the response asserts, as a UNIVERSAL premise about any tangential tetrahedron, that the inscribed sphere is tangent to each face at the face's incenter. Look for phrases like "insphere is tangent to each face at its face-incenter", "tangent to each face at the incenter of that face", or "point of tangency on each face is the incenter of that face" used as a general fact rather than as a conclusion derived from hypothesis (2).

- `counterexample_places_a_above_centroid`
  - TRIGGER: the response's counterexample paragraph for statement (a) contains the literal word "centroid" (not "incenter", not "in-centre", not a named symbol). The phrase must occur inside an explicit counterexample to (a) and place vertex A "directly above the centroid" of triangle BCD. If the response writes "directly above the in-centre" / "directly above H" / "directly above the incenter", the trigger does NOT fire.

- `appeals_to_almost_regular_or_slightly_skewed`
  - TRIGGER: the response dismisses one or more of the gold claims with an appeal to a tetrahedron that is "almost regular" or "slightly skewed" or any near-verbatim paraphrase, without producing a concrete construction. Look for the literal phrase "almost regular" or "slightly skewed".

Important scoring and selection rules:
- The audit is evaluated as an EXACT set match per response. Extra failure reasons and missing failure reasons both score zero for that response.
- Most responses have 0 or 1 failure reasons. Apply a code only when its trigger phrase is directly observable in the response text.
- Use an empty list `[]` for failure_reasons exactly when the response's claimed set equals the gold set AND no failure-reason trigger phrase appears in that response.
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
