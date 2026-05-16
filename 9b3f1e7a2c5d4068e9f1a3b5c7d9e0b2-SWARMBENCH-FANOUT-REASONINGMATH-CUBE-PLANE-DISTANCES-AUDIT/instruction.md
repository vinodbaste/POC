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

This task has three independent deliverable groups, and all three must be correct in your final JSON output:

(1) **Gold geometric derivation** — multiple independent values from solving the problem yourself:
   - the gold final numeric answer (sum of squares of all elements of S);
   - the full set of distinct s² (squared edge length) values consistent with the eight given vertex-to-plane distances;
   - the s² value obtained from the "all-positive" cube orientation (where no vertex sits on the opposite side of the plane from the rest);
   - the sorted list of s² values obtained from the "sign-flipped" cube orientations (where the plane passes through the cube's interior);
   - the four sorted "axis-length triples" (p, q, r) underlying the four valid s² values;
   - the total number of distinct cube orientations consistent with the constraint.

(2) **Per-response audit** — for each of the nine released responses A through I, extract its claimed final numeric answer and identify the EXACT SET of failure-reason codes (from the 12-code controlled vocabulary defined below) whose triggering condition is concretely present in that single response.

(3) **Cross-response synthesis** — aggregate, across all nine responses, how many responses each failure-reason code applies to. This must equal the count obtained by tallying your nine per-response failure-reasons sets.

Do not decide correctness by majority vote among the responses. Solve the problem independently first, then audit each response against your derivation.

## Allowed failure-reason codes

Each code applies ONLY when its triggering condition is concretely instantiated in that single response's text.

- `claims_unique_edge_length` — TRIGGER: the response's final stated conclusion asserts that there is exactly one possible cube edge length (|S| = 1), regardless of the value claimed. Trigger phrases: "only possible edge length", "the only solution", "uniquely determined", "the cube edge length is", or a final boxed answer equal to (one numeric edge-length value)² rather than a sum of squares over multiple values. Does NOT fire if the response presents its final answer as a sum over multiple candidate edge lengths, or if the response never reaches a final numeric conclusion.

- `restricts_to_nonnegative_subset_sums` — TRIGGER: the response's load-bearing argument requires all seven non-zero vertex-to-plane distances to arise as non-negative sums of three "axis projections" or "subset sums" of three positive quantities {p, q, r}. Trigger phrases: "projections must be non-negative", "subset sums of {p, q, r}", "non-empty subset sums", "signed projections have the same sign", or a search restricted to positive-integer triples whose subset sums equal {1, …, 7}.

- `assumes_max_distance_equals_space_diagonal` — TRIGGER: the response equates the maximum vertex-to-plane distance (7) with the cube's space diagonal a√3, deriving a = 7/√3 and s² = 49/3 (or equivalent) as a load-bearing step.

- `assumes_plane_parallel_to_cube_face` — TRIGGER: the response's primary geometric setup assumes the cutting plane is parallel to one face of the cube (or an axis-aligned cube cut by z = k), so the eight vertex distances take at most two distinct values.

- `equates_max_distance_with_edge_length_directly` — TRIGGER: the response directly identifies the maximum vertex-to-plane distance (7) with the cube's edge length a (so a = 7 and s² = 49). Mutually exclusive with `assumes_max_distance_equals_space_diagonal`.

- `uses_fabricated_invariant_or_invalid_derivation` — TRIGGER: the response's final numeric answer rests on an invented algebraic identity that does not follow from the problem (e.g., asserting a "sum of squared distances = 3a²(1 + T²)" identity, or summing roots of a quadratic whose coefficients come from a fabricated invariant), OR the response invents a derivation step lacking algebraic backing such that the final boxed value is the output of a fabricated algebraic chain.

- `accepts_internal_contradictions_in_derivation` — TRIGGER: the response openly accepts mutually contradictory equations such as "6 = 7" or "3 = 4" inside its derivation and then proceeds to select a numeric answer that the surviving algebra does not justify. Requires both (a) an explicit contradiction in the text and (b) a final numeric answer extracted despite it.

- `assumes_zero_distance_vertex_is_axis_corner` — TRIGGER: the response fixes the vertex at distance 0 to be a specific cube-local corner (typically (0,0,0) of an axis-aligned cube) and treats every other vertex's signed distance as a non-negative coordinate combination of three outgoing edge directions from that corner, without justifying why the zero-vertex must be that specific corner. Trigger phrases: "place the cube with one vertex at the origin", "vertex (0,0,0) lies on the plane", "the cube has vertices at {0, a}³". Does NOT fire if the response uses a symbolic (±, ±, ±) sign-pattern setup or a body-diagonal aligned setup that does not fix a specific corner.

- `omits_sign_pattern_casework` — TRIGGER: the response reaches a numeric conclusion (correct or wrong) without enumerating the sign-pattern families of the cube's vertex configurations relative to the plane (i.e., it does not branch on whether the plane intersects the cube's interior). Does NOT fire if the response never reaches a numeric conclusion.

- `treats_one_orientation_as_proof_of_uniqueness` — TRIGGER: the response solves a single cube orientation (axis-aligned, body-diagonal-aligned, face-parallel, or any other single geometric configuration), derives some s² value from that one orientation, and then asserts (explicitly or implicitly) that this s² value is the only solution without ruling out other orientations.

- `derives_correct_partial_s2_then_discards_it` — TRIGGER: the response correctly derives s² = 21 (the all-positive case value) at some point in its reasoning chain and then explicitly rejects or discards that value, choosing a different final numeric answer.

- `non_terminating_or_no_final_answer` — TRIGGER: the response does not produce an identifiable final numeric answer. Includes: no boxed answer and no equivalent "final answer is N" sentence; a generation that loops on a phrase tens or hundreds of times until truncation; a mid-sentence cut-off before any conclusion. Mutually incompatible with any code that requires extracting a final numeric answer.

## Scoring rules

- The per-response audit is evaluated as EXACT SET MATCH on `failure_reasons`. Both extra and missing codes are wrong: the audit for a given response receives credit only if `response_id`, `extracted_final_answer`, `final_answer_correct`, and the exact `failure_reasons` set all match. Most responses have 3–5 applicable codes; one has 1.
- Top-level gold fields and cross-response synthesis are scored independently.
- `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of `response_id`s whose `final_answer_correct` is `true` AND whose `failure_reasons` list is empty.

## Per-response field definitions

- `response_id` — the response letter, exactly one of `"A"` … `"I"`.
- `extracted_final_answer` — a string giving the response's claimed final numeric answer, normalized as the response wrote it (for example `"21"`, `"49"`, `"49/3"`, `"140/3"`, `"6"`). Use `null` if the response gives no identifiable final numeric answer.
- `final_answer_correct` — `true` exactly when `extracted_final_answer` equals the gold final answer; otherwise `false`. A `null` extracted answer is never correct.
- `failure_reasons` — a JSON list of strings chosen only from the 12 allowed failure-reason codes above.

## Cross-response synthesis field

- `failure_reason_frequency` — a JSON object whose keys are the 12 allowed failure-reason codes and whose values are the integer counts of how many of the nine per-response `failure_reasons` lists contain that code. Include every code (use `0` for codes that do not fire on any response).

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "gold_final_answer": "<gold numeric answer as a string>",
  "gold_edge_length_squared_set": [<sorted list of all distinct s² values>],
  "gold_case_a_s_squared": <integer s² for the all-positive orientation>,
  "gold_case_b_s_squared_values": [<sorted list of s² values from sign-flipped orientations>],
  "gold_axis_lengths_triples": [<list of sorted [p,q,r] triples, one per valid orientation, in the same order as combining case A and case B>],
  "total_distinct_orientations": <integer count of distinct cube orientations consistent with the constraint>,
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "extracted_final_answer": "<response's claimed answer as a string, or null>",
      "final_answer_correct": <true or false>,
      "failure_reasons": ["<zero or more allowed failure-reason codes>"]
    }
  ],
  "failure_reason_frequency": {
    "<each of the 12 codes>": <integer count>
  }
}

In the actual output, include nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that order. `gold_axis_lengths_triples` must list the triples sorted overall (each inner triple sorted ascending; outer list sorted by lex order). `failure_reason_frequency` must include all 12 codes as keys. Do not write anything else to that file.
