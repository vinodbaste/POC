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

### Failure-code disambiguation guidance

Many candidate solutions exhibit multiple defects simultaneously. The full code vocabulary is enumerated above; the following disambiguation rules clarify boundaries between near-overlapping codes:

- `equates_max_distance_with_edge_length_directly` (a = 7) and `assumes_max_distance_equals_space_diagonal` (a = 7/√3) are mutually exclusive. A response cannot simultaneously identify the maximum distance with both the edge and the space diagonal; pick the one its load-bearing derivation actually uses.
- `claims_unique_edge_length` fires when the response's final stated conclusion asserts |S| = 1, regardless of whether the value is itself correct or wrong. It does NOT fire when the final stated value is presented as a sum over multiple candidate edge lengths.
- `treats_one_orientation_as_proof_of_uniqueness` fires when the response solves exactly one cube orientation and asserts the resulting s² as the only solution. It overlaps with but is distinct from `claims_unique_edge_length`: the former targets the geometric step (one orientation solved, asserted unique), the latter targets the final-answer wording (|S| = 1 in conclusion).
- `assumes_zero_distance_vertex_is_axis_corner` fires when the response fixes the zero-distance vertex at a specific cube-local corner such as (0,0,0). It does NOT fire when the response uses a symmetric signed (±, ±, ±) sign-pattern setup or a body-diagonal-aligned setup that does not pin a specific corner.
- `restricts_to_nonnegative_subset_sums` fires when the response's load-bearing search assumes all seven nonzero distances arise as non-negative subset sums of positive quantities {p, q, r}. It typically co-occurs with `assumes_zero_distance_vertex_is_axis_corner` and `omits_sign_pattern_casework`.
- `omits_sign_pattern_casework` fires when the response reaches a numeric conclusion without enumerating the sign-pattern families. It does NOT fire when the response never reaches a numeric conclusion.
- `accepts_internal_contradictions_in_derivation` requires BOTH (a) an explicit contradictory equation in the response text (such as "6 = 7") and (b) a final numeric answer extracted despite the contradiction. Either alone is insufficient.
- `uses_fabricated_invariant_or_invalid_derivation` fires when the response's final numeric answer rests on an invented algebraic identity (e.g., a fabricated "sum-of-squared-distances" identity) or an unsupported derivation step. The trigger requires that the load-bearing step traces back to fabrication.
- `derives_correct_partial_s2_then_discards_it` requires both (a) the value 21 (or equivalently 1² + 2² + 4²) appearing as a derived s² intermediate and (b) explicit rejection of it in favor of a different final numeric answer.
- `non_terminating_or_no_final_answer` fires when no committed final numeric answer exists at all. It is mutually incompatible with any code that requires extracting a final numeric answer; if it fires, it stands alone.
- `assumes_plane_parallel_to_cube_face` fires only when the response's primary geometric setup uses a face-parallel or axis-aligned cube with the plane at constant z. It does NOT fire when the response merely entertains and discards this hypothesis.

### Worked scoring example

Consider a hypothetical response that places one cube vertex at the origin (0,0,0), assumes the seven nonzero distances arise as non-negative sums of three positive quantities {p, q, r}, finds the unique positive-integer solution (p, q, r) = (1, 2, 4) giving s² = 21, and concludes "the cube edge length is √21, so the answer is 21". The applicable failure-reason codes are:

- `assumes_zero_distance_vertex_is_axis_corner` because the zero-distance vertex is fixed at the cube-local origin.
- `restricts_to_nonnegative_subset_sums` because the seven distances are required to be non-negative subset sums of {p, q, r}.
- `omits_sign_pattern_casework` because the response derives a numeric conclusion without considering sign-flipped configurations.
- `treats_one_orientation_as_proof_of_uniqueness` because one geometric configuration is solved and asserted unique.
- `claims_unique_edge_length` because the final stated conclusion is a single numeric edge length.

Five codes apply; `final_answer_correct` is false because 21 ≠ gold answer.

### Common audit anti-patterns

The following patterns recur across candidate responses and require careful classification:

- Asserting that the cube must be axis-aligned with one vertex at the origin and then computing the seven non-zero distances as subset sums of three positive integers. This triggers both `assumes_zero_distance_vertex_is_axis_corner` and `restricts_to_nonnegative_subset_sums`; typically also triggers `omits_sign_pattern_casework`.
- Identifying the maximum vertex-to-plane distance with the cube edge length (a = 7) directly, without projecting the cube edge through the plane normal. Triggers `equates_max_distance_with_edge_length_directly`.
- Identifying the maximum vertex-to-plane distance with the space diagonal (a√3 = 7). Triggers `assumes_max_distance_equals_space_diagonal` and is mutually exclusive with the previous code.
- Reaching a single numeric answer from one cube orientation and asserting it as unique without ruling out other orientations. Triggers `treats_one_orientation_as_proof_of_uniqueness`.
- Inventing an algebraic identity such as "sum of squared distances = 3a²(1 + T²)" and using it as the load-bearing derivation. Triggers `uses_fabricated_invariant_or_invalid_derivation`.
- Looping on a phrase or truncating mid-sentence without reaching a final numeric answer. Triggers `non_terminating_or_no_final_answer` alone; do NOT add other codes.
- Deriving s² = 21 as a partial result, then rejecting it in favor of a fabricated final value. Triggers `derives_correct_partial_s2_then_discards_it` and typically also `uses_fabricated_invariant_or_invalid_derivation`.

### Resolution rules for borderline cases

When multiple codes plausibly apply, use the following resolution rules:

- A response that gives the correct final answer but with internal logical gaps still requires its applicable failure codes; correctness of the numeric answer is independent of trigger detection.
- A response that gives the wrong final answer with a sound partial argument should receive only the codes whose triggers concretely fire in its text; do not add codes that describe defects absent from the response.
- When a response produces a final numeric value via a clearly fabricated derivation step, prefer `uses_fabricated_invariant_or_invalid_derivation` even if other codes (e.g., `omits_sign_pattern_casework`) also apply.
- When a response halts mid-derivation without a final numeric value, `non_terminating_or_no_final_answer` is the only applicable code; no other code fires in the absence of a final answer.

### Glossary

- s²: the squared cube edge length (the square of any allowed edge length).
- S: the set of distinct edge-length values consistent with the seven non-zero vertex-to-plane distances 1, 2, 3, 4, 5, 6, 7.
- gold final answer: the sum of squares of all elements of S, i.e., the sum of all distinct s² values.
- Sign-pattern family: a choice of signs (±, ±, ±) applied to the three "axis projection" magnitudes (u, v, w) of the cube relative to the plane. The all-same-sign family gives one s² value; one-axis-flipped families give additional s² values when feasible.
- Axis-aligned cube: a cube with edges parallel to the coordinate axes, typically with one vertex at the origin and the opposite vertex at (a, a, a).
- Body-diagonal-aligned cube: a cube oriented so that one of its body diagonals lies along a chosen direction (often the normal to the cutting plane).
- Subset sum of {p, q, r}: any sum of zero or more of p, q, r, used to model vertex-to-plane distances when projections are assumed non-negative.

Note that the workflow steps in the Task section above are intended as guidance for the auditor's reasoning process; the verifier scores only the final JSON output and its labels, not the auditor's working procedure.

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
