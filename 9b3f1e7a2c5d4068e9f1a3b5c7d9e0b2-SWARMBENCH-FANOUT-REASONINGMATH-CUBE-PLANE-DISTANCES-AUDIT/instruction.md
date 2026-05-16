You are conducting an olympiad-level 3D geometry audit. Nine real, unedited model responses from the public `RUC-AIBOX/OlymMATH-eval` benchmark each attempt the same cube-and-plane problem. Your work is primarily mathematical reasoning: you must independently solve the problem from first principles, then mathematically dissect each response's argument and identify where its mathematical reasoning fails.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem.md`
- Provenance note for the released model responses: `/input_artifacts/provenance.md`
- Released model response files (real outputs from the public benchmark):
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
1. Solve the geometry problem yourself from first principles. Produce the gold final numeric answer (the sum of squares of all possible cube edge lengths consistent with the eight given vertex-to-plane distances) and the underlying set of distinct values of s² (the squared edge lengths). Do not rely on any of the released responses for this step.
2. Verify your derivation. The final numeric answer must follow rigorously from the geometric configuration and the constraint that the eight vertex-to-plane distances are 0, 1, 2, 3, 4, 5, 6, 7. Identify every distinct (non-degenerate) cube orientation that satisfies the constraint, and report each s² value once.
3. Read all nine released responses. For each one, extract its claimed final numeric answer and compare it against your gold answer.
4. For each released response A through I, audit its mathematical reasoning chain. Identify the load-bearing algebraic identities, the geometric setup assumptions, and the logical steps that determine the response's final answer. Then identify the exact set of failure-reason codes whose trigger phrase is concretely instantiated in that single response's text.
5. Do not decide correctness by majority vote among the released responses. Independently solve the problem first, then audit each response against your own derivation.

Allowed failure-reason codes (phrase-triggered; each code applies ONLY when its trigger phrase or its near-verbatim paraphrase is present in that single response's text):

- `claims_unique_edge_length`
  - TRIGGER: the response's final stated conclusion asserts that there is exactly one possible cube edge length (i.e., the set S has exactly one element), regardless of what value the unique edge length is claimed to be. Look for phrases such as "only possible edge length", "the only solution", "uniquely determined", "the cube edge length is", or a final boxed answer that equals (one numeric edge-length value)² rather than a sum of squares over multiple values. This code does NOT fire if the response explicitly lists multiple distinct edge lengths in its final conclusion (even if those values are themselves wrong), or if the response never reaches a final numeric conclusion.

- `restricts_to_nonnegative_subset_sums`
  - TRIGGER: the response's load-bearing argument assumes that the seven non-zero vertex-to-plane distances must all arise as non-negative sums of three "axis projections" or "subset sums" of three positive quantities {p, q, r}, i.e., it implicitly or explicitly requires all eight cube vertices to lie on the same side of the plane (or on the plane). Look for phrases like "projections must be non-negative", "subset sums of {p, q, r}", "non-empty subset sums", "signed projections have the same sign", "all distances on the same side", or a search restricted to positive-integer triples whose subset sums equal {1,2,...,7}. This code applies even when the response correctly derives one value of s² (e.g., s²=21) from the all-positive case before declaring that value unique.

- `assumes_max_distance_equals_space_diagonal`
  - TRIGGER: the response equates the maximum vertex-to-plane distance (7) with the cube's space diagonal a√3, deriving a = 7/√3 and s² = 49/3 (or equivalent) as the cube edge length. Look for the literal phrases "space diagonal = 7", "a√3 = 7", "a = 7/√3", "the space diagonal must equal 7", or "maximum distance is the space diagonal" used as a load-bearing identification rather than as a discarded hypothesis.

- `assumes_plane_parallel_to_cube_face`
  - TRIGGER: the response's primary geometric setup assumes the cutting plane is parallel to one face of the cube (or equivalently, an axis-aligned cube cut by a plane of the form z = k), so that the eight vertex distances take at most two distinct values. Look for the literal phrases "distances would be the z-coordinates", "plane parallel to a face", "plane z = k" with an axis-aligned cube, or a conclusion that the edge length equals the maximum distance directly (e.g., "the edge length is 7"). This trigger does NOT fire if the response merely entertains and discards a face-parallel orientation as a special case.

- `uses_fabricated_invariant_or_invalid_derivation`
  - TRIGGER: the response's final numeric answer rests on an invented algebraic identity that does not follow from the problem (for example, asserting that the sum of squared distances equals `3a²(1 + T²)` with `T = n·(a,a,a)`, or deriving the answer as the sum of roots of a quadratic whose coefficients come from a fabricated invariant), OR the response openly accepts mutually contradictory equations such as "6 = 7" / "3 = 4" inside its derivation and then selects a numeric answer that is not justified by the surviving algebra. Look for an explicit fabricated equation, a Vieta-sum step over an unjustified quadratic, or accepted self-contradictions paired with a final boxed value that has no valid algebraic chain.

- `non_terminating_or_no_final_answer`
  - TRIGGER: the response does not produce an identifiable final numeric answer. This includes: no boxed answer and no equivalent "final answer is N" sentence; a generation that loops on a phrase tens or hundreds of times until truncation; a mid-sentence cut-off before any conclusion. The trigger fires regardless of whether the early portion of the response is mathematically reasonable.

Important scoring and selection rules:
- The audit is evaluated as an EXACT set match per response. Extra failure reasons and missing failure reasons both score zero for that response.
- Most responses have 1 or 2 failure reasons. Apply a code only when its trigger phrase is directly observable in the response text.
- Use an empty list `[]` for `failure_reasons` exactly when the response's final numeric answer equals the gold answer AND no failure-reason trigger phrase appears in that response.
- `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of response_ids whose `final_answer_correct` is `true` AND whose `failure_reasons` list is empty.
- `claims_unique_edge_length` and `restricts_to_nonnegative_subset_sums` are distinct codes. `restricts_to_nonnegative_subset_sums` describes the REASONING step (forcing all 7 non-zero distances to be sums of positive projections); `claims_unique_edge_length` describes the FINAL stated conclusion (|S|=1). Both can apply to the same response when both triggers are present.
- `assumes_plane_parallel_to_cube_face` is distinct from `assumes_max_distance_equals_space_diagonal`. The face-parallel trigger is geometric ("plane parallel to a face", "z = k"). The space-diagonal trigger is algebraic ("a√3 = 7"). A response that uses only one of these triggers gets only that one code; do not apply both unless both triggers are concretely present.

Label definitions for each released response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `final_answer_correct`: `true` exactly when the response's final stated numeric answer equals your independently derived gold answer. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure-reason codes above.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "gold_final_answer": "<your independently derived numeric answer as a string>",
  "gold_edge_length_squared_set": [<sorted list of all distinct s² values>],
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": <true or false>,
      "failure_reasons": ["<zero or more allowed failure-reason codes>"]
    }
  ]
}

In the actual output, include nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that order. Do not write anything else to that file.
