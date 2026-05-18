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
5. For each response, choose ONE `primary_failure_code` from that response's `failure_reasons` set (or the literal string `"NONE"` if the set is empty). The primary code is the single most load-bearing diagnostic - the defect whose absence would most likely have produced a valid derivation.
6. For each code in the response's `failure_reasons` set, produce a short evidence quote of at least 20 characters citing or paraphrasing the response text that demonstrates that trigger. Evidence quotes are scored on presence and minimum length.
7. For each response produce a `primary_failure_code_evidence` string of at least 50 characters explaining why the chosen primary_failure_code is the most load-bearing diagnostic, citing response-specific text.
8. For each response produce an `alternative_codes_considered` list of at least two objects, each naming a code from the controlled vocabulary that is NOT the response's primary_failure_code together with a `reason_excluded` of at least 20 characters justifying why it is not the most diagnostic.
9. At the top level, build a `code_application_table` whose 12 keys are the 12 failure-reason codes from the vocabulary; each value is the alphabetically-sorted list of response_ids whose `failure_reasons` set contains that code. Codes with no matching response have an empty list. The verifier scores each key against the oracle at 70 weighted points, so accuracy on this field cascades from per-response failure_reasons accuracy.
10. At the top level, produce a `cross_response_observations` string of at least 300 characters identifying shared defect patterns across the nine responses (for example: which responses share the corner-and-subset-sum setup, which share the space-diagonal misidentification, which share fabricated-invariant derivations).

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
- The audit is evaluated on a multi-field rubric, not on a single equality check. Both extra failure-reason codes and missing failure-reason codes are wrong for the `failure_reasons` set: a response's `failure_reasons` set earns its weight only if the exact set of codes matches the oracle's set for that response.
- Most responses have 3-5 applicable codes. A few have 1.
- Apply a code only when its triggering condition is concretely instantiated in the response's text.
- Use an empty list `[]` for `failure_reasons` exactly when the response's final numeric answer equals the gold answer AND no failure-reason trigger fires.
- When `failure_reasons` is an empty list, set `primary_failure_code` to the literal string `"NONE"`.
- `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of `response_id`s whose `final_answer_correct` is `true` AND whose `failure_reasons` list is empty.

Label definitions for each released response:
- `response_id`: the response letter, exactly one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `final_answer_correct`: `true` exactly when the response's final stated numeric answer equals the gold answer. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the 12 allowed failure-reason codes above (the SET of codes whose triggers concretely fire on that response's text).
- `primary_failure_code`: a single string drawn from the response's `failure_reasons` set (the most diagnostic load-bearing defect), or the literal string `"NONE"` when `failure_reasons` is empty.
- `failure_reason_evidence`: a JSON object whose keys are exactly the codes in this response's `failure_reasons` set. Each value is a string of at least 20 characters citing or paraphrasing the response text that demonstrates that code's trigger. Generic boilerplate that does not refer to the response's actual content is insufficient.
- `primary_failure_code_evidence`: a string of at least 50 characters explaining why the chosen `primary_failure_code` is the most load-bearing diagnostic for this response, referencing response-specific text.
- `alternative_codes_considered`: a JSON array of at least 2 objects. Each object has a `code` field (a string drawn from the 12-code controlled vocabulary, or the literal string `"NONE"`, and DIFFERENT from this response's `primary_failure_code`) and a `reason_excluded` field (a string of at least 20 characters justifying why this code is not the primary diagnostic).

### Failure-code disambiguation guidance

Many candidate solutions exhibit multiple defects simultaneously. The full code vocabulary is enumerated above; the following disambiguation rules clarify boundaries between near-overlapping codes:

- `equates_max_distance_with_edge_length_directly` (a = 7) and `assumes_max_distance_equals_space_diagonal` (a = 7/√3) are mutually exclusive. A response cannot simultaneously identify the maximum distance with both the edge and the space diagonal; pick the one its load-bearing derivation actually uses.
- `claims_unique_edge_length` fires when the response's final stated conclusion asserts |S| = 1, regardless of whether the value is itself correct or wrong. It does NOT fire when the final stated value is presented as a sum over multiple candidate edge lengths.
- `treats_one_orientation_as_proof_of_uniqueness` fires when the response solves exactly one cube orientation and asserts the resulting s² as the only solution. It overlaps with but is distinct from `claims_unique_edge_length`: the former targets the geometric step (one orientation solved, asserted unique), the latter targets the final-answer wording (|S| = 1 in conclusion). This code does NOT fire when the load-bearing defect is internal contradictory equations inside one derivation chain (the response did not produce a clean single-orientation derivation), nor when the load-bearing defect is direct edge=7 identification under a face-parallel or axis-aligned setup (those framings are captured by other codes), nor when the load-bearing defect is a space-diagonal a√3=7 identification (the geometric defect is the diagonal misidentification, not the orientation), nor when the response works through multiple sign branches even if it discards one.
- `assumes_zero_distance_vertex_is_axis_corner` fires when the response fixes the zero-distance vertex at a specific cube-local corner such as (0,0,0). It does NOT fire when the response uses a symmetric signed (±, ±, ±) sign-pattern setup or a body-diagonal-aligned setup that does not pin a specific corner.
- `restricts_to_nonnegative_subset_sums` fires when the response's load-bearing search assumes all seven nonzero distances arise as non-negative subset sums of positive quantities {p, q, r}. It typically co-occurs with `assumes_zero_distance_vertex_is_axis_corner` and `omits_sign_pattern_casework`.
- `omits_sign_pattern_casework` fires when the response reaches a numeric conclusion without enumerating the sign-pattern families. It does NOT fire when the response never reaches a numeric conclusion, and it does NOT fire when the response considered the all-positive sign case at least partially (for example, derived the s² value of the all-positive case and then explicitly discarded it). When that explicit derive-then-discard pattern is present, the applicable code is `derives_correct_partial_s2_then_discards_it`, not `omits_sign_pattern_casework`.
- `accepts_internal_contradictions_in_derivation` requires BOTH (a) an explicit contradictory equation in the response text (such as "6 = 7") and (b) a final numeric answer extracted despite the contradiction. Either alone is insufficient.
- `uses_fabricated_invariant_or_invalid_derivation` fires when the response's final numeric answer rests on an invented algebraic identity (e.g., a fabricated "sum-of-squared-distances" identity) or an unsupported derivation step. The trigger requires that the load-bearing step traces back to fabrication.
- `derives_correct_partial_s2_then_discards_it` requires both (a) the value 21 (or equivalently 1² + 2² + 4²) appearing as a derived s² intermediate and (b) explicit rejection of it in favor of a different final numeric answer.
- `non_terminating_or_no_final_answer` fires when no committed final numeric answer exists at all. It is mutually incompatible with any code that requires extracting a final numeric answer; if it fires, it stands alone.
- `assumes_plane_parallel_to_cube_face` fires only when the response's primary geometric setup uses a face-parallel or axis-aligned cube with the plane at constant z. It does NOT fire when the response merely entertains and discards this hypothesis.

### Primary failure code selection guidance

The `primary_failure_code` is the single most load-bearing diagnostic among the codes in the response's `failure_reasons` set. Use the following universal selection rules; they apply uniformly to every response with no per-response naming:

- If `failure_reasons` is empty, `primary_failure_code` MUST be the literal string `"NONE"`.
- If `non_terminating_or_no_final_answer` is present, it stands alone and is the primary code.
- When the load-bearing defect is a fabricated algebraic invariant AND the response also accepts internal contradictions, prefer `uses_fabricated_invariant_or_invalid_derivation` over `accepts_internal_contradictions_in_derivation` because the fabrication is the upstream defect.
- When the response derives the correct partial s² = 21 and then explicitly discards it, prefer `derives_correct_partial_s2_then_discards_it` over `uses_fabricated_invariant_or_invalid_derivation` even if a fabricated quadratic follows the discard. The explicit discard is the more diagnostic defect.
- When the response restricts its search to non-negative subset sums of positive quantities AND also fixes the zero-distance vertex at a specific corner, prefer `restricts_to_nonnegative_subset_sums` over `assumes_zero_distance_vertex_is_axis_corner` because the subset-sum restriction is the load-bearing search restriction; the corner choice is downstream.
- When the load-bearing geometric step is identifying the maximum vertex-to-plane distance with the cube's space diagonal (a√3 = 7), prefer `assumes_max_distance_equals_space_diagonal` over `treats_one_orientation_as_proof_of_uniqueness` and over `claims_unique_edge_length`; the geometric misidentification is the upstream defect.
- When the response's primary geometric setup is face-parallel or axis-aligned with the plane at constant z, prefer `assumes_plane_parallel_to_cube_face` over `equates_max_distance_with_edge_length_directly` when both apply; the face-parallel framing is the load-bearing setup choice.
- Do NOT pick `claims_unique_edge_length` or `omits_sign_pattern_casework` as the primary code when other codes apply; these are downstream symptoms of upstream geometric or algebraic choices and are not load-bearing on their own.

### Worked scoring example

Consider a hypothetical response that places one cube vertex at the origin (0,0,0), assumes the seven nonzero distances arise as non-negative sums of three positive quantities {p, q, r}, finds the unique positive-integer solution (p, q, r) = (1, 2, 4) giving s² = 21, and concludes "the cube edge length is √21, so the answer is 21". The applicable failure-reason codes are:

- `assumes_zero_distance_vertex_is_axis_corner` because the zero-distance vertex is fixed at the cube-local origin.
- `restricts_to_nonnegative_subset_sums` because the seven distances are required to be non-negative subset sums of {p, q, r}.
- `omits_sign_pattern_casework` because the response derives a numeric conclusion without considering sign-flipped configurations.
- `treats_one_orientation_as_proof_of_uniqueness` because one geometric configuration is solved and asserted unique.
- `claims_unique_edge_length` because the final stated conclusion is a single numeric edge length.

Five codes apply; `final_answer_correct` is false because 21 ≠ gold answer. Per the selection rules, the primary_failure_code is `restricts_to_nonnegative_subset_sums` because the load-bearing search restriction outranks the downstream axis-corner choice, uniqueness wording, and orientation closure.

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

## Verifier scoring rule

The verifier scores the final JSON deterministically against the oracle. Field weights:

- `gold_final_answer` (string match): 2 points
- `gold_edge_length_squared_set` (sorted-list match): 2 points
- `acceptable_solution_ids` (set match): 2 points
- Per response (nine times):
  - `final_answer_correct` (exact bool match): 5 points
  - `failure_reasons` (exact set match against oracle, all-or-nothing): 30 points
  - `primary_failure_code` (exact string match): 25 points
  - `primary_failure_code_evidence` (presence + at least 50 characters): 8 points
  - `alternative_codes_considered` (at least 2 well-formed entries; each `code` from the controlled vocabulary or `"NONE"`, each `code` different from this response's `primary_failure_code`, each `reason_excluded` at least 20 characters): 8 points
  - `failure_reason_evidence` per code in the oracle's `failure_reasons` set (presence + at least 20 characters): 5 points per code
- `code_application_table` per key (12 keys, each value an exact sorted-list match against the oracle): 70 points per key
- `cross_response_observations` (presence + at least 300 characters): 30 points

The total possible score for this task is 1740 weighted points. The reported reward is total_earned / 1740 rounded to a float. The reducer must produce all required fields with the exact key names above; missing fields cost the weighted points for those fields. Producing complete, well-formed values for every field listed above is essential to achieve a high reward.

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
      "failure_reasons": ["<zero or more allowed failure-reason codes>"],
      "primary_failure_code": "<one of the codes in failure_reasons, or \"NONE\" if failure_reasons is empty>",
      "primary_failure_code_evidence": "<string, at least 50 characters, explaining why this primary_failure_code is the most diagnostic for this response>",
      "failure_reason_evidence": {
        "<code in failure_reasons>": "<string, at least 20 characters, citing or paraphrasing the response text justifying this code>"
      },
      "alternative_codes_considered": [
        {"code": "<one of the controlled-vocabulary codes or \"NONE\", different from this response's primary_failure_code>", "reason_excluded": "<string, at least 20 characters>"},
        {"code": "<another code>", "reason_excluded": "<string, at least 20 characters>"}
      ]
    }
  ],
  "code_application_table": {
    "claims_unique_edge_length": [<sorted list of response_ids whose failure_reasons contains this code>],
    "restricts_to_nonnegative_subset_sums": [<sorted list>],
    "assumes_max_distance_equals_space_diagonal": [<sorted list>],
    "assumes_plane_parallel_to_cube_face": [<sorted list>],
    "equates_max_distance_with_edge_length_directly": [<sorted list>],
    "uses_fabricated_invariant_or_invalid_derivation": [<sorted list>],
    "accepts_internal_contradictions_in_derivation": [<sorted list>],
    "assumes_zero_distance_vertex_is_axis_corner": [<sorted list>],
    "omits_sign_pattern_casework": [<sorted list>],
    "treats_one_orientation_as_proof_of_uniqueness": [<sorted list>],
    "derives_correct_partial_s2_then_discards_it": [<sorted list>],
    "non_terminating_or_no_final_answer": [<sorted list>]
  },
  "cross_response_observations": "<single string, at least 300 characters, identifying shared defect patterns across the nine responses>"
}

In the actual output, include nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that order. Every response_id from A through I must appear in exactly one bucket in `code_application_table` for each of its `failure_reasons` codes (so a response with five codes appears in five buckets). Codes whose triggers do not fire on any response have empty lists.
