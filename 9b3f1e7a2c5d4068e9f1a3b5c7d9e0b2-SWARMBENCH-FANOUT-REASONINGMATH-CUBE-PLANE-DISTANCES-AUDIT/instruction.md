You are auditing nine real, unedited model responses (from the public `RUC-AIBOX/OlymMATH-eval` benchmark) to an olympiad-level 3D geometry problem about a cube and a plane.

Working directory: `/workspace`.

Input artifacts:
- Problem statement: `/input_artifacts/problem.md`
- Provenance note for the released model responses: `/input_artifacts/provenance.md`
- Released model response files:
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
1. Read the problem statement and all nine released responses.
2. Independently determine the gold final numeric answer (the sum of squares of all elements of S, where S is the set of possible cube edge lengths) and the underlying set of distinct values of s².
3. Determine which response(s), if any, give the correct final numeric answer.
4. For each response A through I, identify the EXACT SET of failure-reason codes from the controlled vocabulary below whose triggering condition is concretely present in that single response's text. Each response typically has 1-5 applicable codes.

Allowed failure-reason codes (each code applies ONLY when its triggering condition is concretely instantiated in that single response's text):

- `claims_unique_edge_length`
  - TRIGGER: the response's final stated conclusion asserts that there is exactly one possible cube edge length (|S| = 1), regardless of the value claimed. Trigger phrases include "only possible edge length", "the only solution", "uniquely determined", "the cube edge length is", or a final boxed answer that equals (one numeric edge-length value)² rather than a sum of squares over multiple values. Does NOT fire if the response presents its final answer as a sum over multiple candidate edge lengths, or if the response never reaches a final numeric conclusion.

- `restricts_to_nonnegative_subset_sums`
  - TRIGGER: the response's load-bearing argument requires all seven non-zero vertex-to-plane distances to arise as non-negative sums of three "axis projections" or "subset sums" of three positive quantities {p, q, r}. Trigger phrases: "projections must be non-negative", "subset sums of {p, q, r}", "non-empty subset sums", "signed projections have the same sign", or a search restricted to positive-integer triples whose subset sums equal {1, …, 7}.

- `assumes_max_distance_equals_space_diagonal`
  - TRIGGER: the response equates the maximum vertex-to-plane distance (7) with the cube's space diagonal a√3, deriving a = 7/√3 and s² = 49/3 (or equivalent) as a load-bearing step. Trigger phrases: "space diagonal = 7", "a√3 = 7", "a = 7/√3", "the space diagonal must equal 7", "maximum distance is the space diagonal".

- `assumes_plane_parallel_to_cube_face`
  - TRIGGER: the response's primary geometric setup assumes the cutting plane is parallel to one face of the cube (or an axis-aligned cube cut by z = k), so the eight vertex distances take at most two distinct values. Trigger phrases: "distances would be the z-coordinates", "plane parallel to a face", "plane z = k" with an axis-aligned cube. Does NOT fire if the response merely entertains and discards this hypothesis.

- `equates_max_distance_with_edge_length_directly`
  - TRIGGER: the response directly identifies the maximum vertex-to-plane distance (7) with the cube's edge length a (so a = 7 and s² = 49), without projecting through any plane normal. Mutually exclusive with `assumes_max_distance_equals_space_diagonal` (the first sets a = 7, the second sets a = 7/√3).

- `uses_fabricated_invariant_or_invalid_derivation`
  - TRIGGER: the response's final numeric answer rests on an invented algebraic identity that does not follow from the problem (e.g., asserting a "sum of squared distances = 3a²(1 + T²)" identity, or summing roots of a quadratic whose coefficients come from a fabricated invariant), OR the response openly invents a derivation step without algebraic backing. The trigger is met whenever the response's final boxed value is the output of a fabricated algebraic chain.

- `accepts_internal_contradictions_in_derivation`
  - TRIGGER: the response openly accepts mutually contradictory equations such as "6 = 7" or "3 = 4" inside its derivation and then proceeds to select a numeric answer that the surviving algebra does not justify. The trigger requires both (a) an explicit contradiction in the response text and (b) a final numeric answer extracted despite the contradiction.

- `assumes_zero_distance_vertex_is_axis_corner`
  - TRIGGER: the response fixes the vertex at distance 0 to be a specific cube-local corner (typically (0,0,0) of an axis-aligned cube) and treats every other vertex's signed distance to the plane as a non-negative coordinate combination of three outgoing edge directions from that corner, without justifying why the zero-vertex must be that specific corner. Trigger phrases: "place the cube with one vertex at the origin", "vertex (0,0,0) lies on the plane", "the cube has vertices at {0, a}³". Does NOT fire if the response uses a symbolic (±, ±, ±) sign-pattern setup or a body-diagonal aligned setup that does not fix a specific corner.

- `omits_sign_pattern_casework`
  - TRIGGER: the response reaches a numeric conclusion (correct or wrong) without enumerating the sign-pattern families of the cube's vertex configurations relative to the plane (i.e., it does not consider configurations in which some vertices have negative signed distance to the plane and others positive). The trigger fires when the response does not branch on whether the plane intersects the cube's interior. Does NOT fire if the response never reaches a numeric conclusion.

- `treats_one_orientation_as_proof_of_uniqueness`
  - TRIGGER: the response solves a single cube orientation (axis-aligned, body-diagonal-aligned, face-parallel, or any other single geometric configuration), derives some s² value from that one orientation, and then asserts (explicitly or implicitly) that this s² value is the only solution without ruling out other orientations. Trigger pattern: ONE derivation chain producing ONE numeric value that the response then names as the unique answer. Does NOT fire if the response considers multiple orientations or treats its final answer as a sum over multiple candidates.

- `derives_correct_partial_s2_then_discards_it`
  - TRIGGER: the response correctly derives s² = 21 (the all-positive case value) at some point in its reasoning chain and then explicitly rejects or discards that value, choosing a different final numeric answer. The trigger requires both (a) the value 21 (or equivalently 1² + 2² + 4²) appearing as a derived s² intermediate and (b) explicit rejection of it.

- `non_terminating_or_no_final_answer`
  - TRIGGER: the response does not produce an identifiable final numeric answer. Includes: no boxed answer and no "final answer is N" sentence; a generation that loops on a phrase tens or hundreds of times until truncation; a mid-sentence cut-off before any conclusion. Fires regardless of whether the early portion of the response is mathematically reasonable. Mutually incompatible with any other code that requires extracting a final numeric answer.

Important scoring and selection rules:
- The audit is evaluated as an EXACT SET MATCH per response. Both extra failure-reason codes and missing failure-reason codes are wrong: a response audit receives credit only if the exact set of codes matches the oracle's set for that response.
- Most responses have 3-5 applicable codes. A few have 1.
- Apply a code only when its triggering condition is concretely instantiated in the response's text.
- Use an empty list `[]` for `failure_reasons` exactly when the response's final numeric answer equals the gold answer AND no failure-reason trigger fires.
- `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of `response_id`s whose `final_answer_correct` is `true` AND whose `failure_reasons` list is empty.

Label definitions for each released response:
- `response_id`: the response letter, exactly one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `final_answer_correct`: `true` exactly when the response's final stated numeric answer equals the gold answer. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the 12 allowed failure-reason codes above.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "gold_final_answer": "<gold numeric answer as a string>",
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
