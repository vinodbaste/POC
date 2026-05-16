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
2. Independently determine the gold final numeric answer (the sum of squares of all elements of S, where S is the set of possible cube edge lengths) and the underlying set of distinct values of s² (the squared edge lengths). Do not modify any files under `/input_artifacts`, `/tests`, or `/solution`.
3. Determine which response(s), if any, are fully correct (final numeric answer equals the gold answer).
4. For each response A through I, audit it using the labels defined below.
5. Do not decide correctness by majority vote among the responses. Solve the problem independently first, then audit each response against your derivation.

## Per-response label definitions

For each response A through I, you must produce the following fields. Most are booleans; a few are strings or categorical enums with controlled values.

- `response_id`: the response letter, exactly one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.

- `extracted_final_answer`: a string giving the response's claimed final numeric answer for the sum of squares of edge lengths, normalized as the response wrote it (for example `"21"`, `"49"`, `"49/3"`, `"140/3"`, `"6"`). Use `null` if the response gives no identifiable final numeric answer (a repetition loop, no boxed answer, or mid-sentence cut-off). This is a faithful extraction of the response's own claim, not a correction.

- `final_answer_correct`: `true` exactly when the response's `extracted_final_answer` equals the gold final answer; otherwise `false`. A `null` extracted answer is never correct.

- `final_answer_category`: exactly one of the following controlled categories.
  - `CORRECT` — extracted answer equals the gold answer.
  - `S2_EQUALS_21_SINGLE_ORIENTATION` — extracted answer equals `21` (s² from the all-positive case, mistaking S for a single-element set).
  - `SPACE_DIAGONAL_FALLACY` — extracted answer equals `49/3` (the response set 7 = a√3 and reported s² = 49/3).
  - `FACE_PARALLEL_FALLACY` — extracted answer equals `49` (the response set a = 7 directly with a face-parallel cutting plane).
  - `FABRICATED_INVARIANT_SUM` — extracted answer comes from summing roots of a fabricated quadratic (e.g., `140/3`).
  - `NUMERIC_WITHOUT_DERIVATION` — extracted answer is a numeric value that the response asserts without a valid algebraic chain (typical of internally-contradictory derivations).
  - `NO_FINAL_ANSWER` — response produced no identifiable final numeric answer.

- `claims_unique_edge_length`: `true` exactly when the response's final stated conclusion asserts that there is exactly one possible cube edge length (|S| = 1), regardless of what value the unique edge length is claimed to be. `false` when the response either does not reach a final conclusion or explicitly treats the final answer as a sum over multiple distinct edge-length values.

- `derives_s2_equals_21_for_some_orientation`: `true` exactly when the response, at any point in its reasoning, correctly derives s² = 21 (equivalently, the all-positive case `(p, q, r) = (1, 2, 4)` with `p² + q² + r² = 21`) for at least one cube orientation, even if the response then declares that value unique or rejects it. `false` if the response never produces s² = 21 as an intermediate or final value.

- `uses_axis_aligned_cube_at_origin_with_zero_vertex_at_corner`: `true` exactly when the response's primary geometric setup places the cube with edges along the coordinate axes and fixes the vertex at distance 0 to be the cube-local corner `(0, 0, 0)` (or an equivalent named corner of an axis-aligned `{0, a}³` cube), then treats the other seven vertices as non-negative coordinate combinations of edges from that corner. `false` if the response uses a different geometric setup (for example, a body-diagonal aligned cube, or a symbolic `(±, ±, ±)` sign-pattern setup that does not fix a specific corner).

- `equates_max_distance_with_space_diagonal`: `true` exactly when the response uses the load-bearing identification 7 = a√3 (the cube's space diagonal equals the maximum vertex-to-plane distance) to derive a = 7/√3. `false` otherwise.

- `assumes_plane_parallel_to_cube_face`: `true` exactly when the response's primary geometric setup assumes the cutting plane is parallel to one face of the cube (or equivalently, an axis-aligned cube cut by a plane of the form z = k), so the eight vertex distances take at most two distinct values. `false` if the response merely entertains and discards this hypothesis.

- `equates_max_distance_with_edge_length_directly`: `true` exactly when the response directly identifies the maximum vertex-to-plane distance (7) with the cube's edge length a (so a = 7 and s² = 49), without projecting through a plane normal. Mutually exclusive with `equates_max_distance_with_space_diagonal`.

- `uses_fabricated_invariant_or_invalid_derivation`: `true` exactly when the response's final numeric answer rests on (a) an invented algebraic identity that does not follow from the problem (e.g., an asserted "sum of squared distances = 3a²(1 + T²)" identity, or a Vieta-sum over a fabricated quadratic), or (b) the response openly accepts mutually contradictory equations ("6 = 7", "3 = 4") inside its derivation and selects a numeric answer not justified by the surviving algebra. `false` otherwise.

- `restricts_to_nonnegative_subset_sums`: `true` exactly when the response's load-bearing argument requires all seven non-zero vertex-to-plane distances to arise as non-negative sums of three positive "axis projections" or "subset sums" of a positive triple {p, q, r}. Trigger phrases include "projections must be non-negative", "subset sums of {p, q, r}", "non-empty subset sums", "signed projections have the same sign", or a search restricted to positive-integer triples whose subset sums equal {1, 2, …, 7}. `false` otherwise.

- `reasoning_coherence_level`: exactly one of three values describing the overall coherence of the response's reasoning chain.
  - `coherent` — the response argues in a linear, internally-consistent fashion, even if it reaches a wrong conclusion.
  - `rambling` — the response cycles through hypotheses, contradicts itself, or hand-waves between approaches, but eventually produces a final answer.
  - `incoherent` — the response is dominated by repetition, self-loops, or other non-progressing text and never produces a final answer.

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format. Top-level keys must be exactly `gold_final_answer`, `gold_edge_length_squared_set`, `acceptable_solution_ids`, and `per_response_assessment`. Include no other top-level keys.

```
{
  "gold_final_answer": "<gold numeric answer as a string>",
  "gold_edge_length_squared_set": [<sorted list of all distinct s² values>],
  "acceptable_solution_ids": ["<uppercase letters of responses with final_answer_correct=true>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "extracted_final_answer": "<response's claimed answer as a string, or null>",
      "final_answer_correct": <true or false>,
      "final_answer_category": "<one controlled category>",
      "claims_unique_edge_length": <true or false>,
      "derives_s2_equals_21_for_some_orientation": <true or false>,
      "uses_axis_aligned_cube_at_origin_with_zero_vertex_at_corner": <true or false>,
      "equates_max_distance_with_space_diagonal": <true or false>,
      "assumes_plane_parallel_to_cube_face": <true or false>,
      "equates_max_distance_with_edge_length_directly": <true or false>,
      "uses_fabricated_invariant_or_invalid_derivation": <true or false>,
      "restricts_to_nonnegative_subset_sums": <true or false>,
      "reasoning_coherence_level": "<coherent | rambling | incoherent>"
    }
  ]
}
```

In the actual output, include exactly nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that order. `acceptable_solution_ids` is the alphabetically-sorted uppercase list of `response_id`s whose `final_answer_correct` is `true`. Do not write anything else to that file.
