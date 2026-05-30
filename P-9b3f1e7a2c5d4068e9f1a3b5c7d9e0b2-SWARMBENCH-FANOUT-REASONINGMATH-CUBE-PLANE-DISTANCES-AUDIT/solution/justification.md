# Oracle Justification

## Gold final answer

The gold sum of squares of all elements of S (the set of possible cube edge lengths) is **210**:

```
S² = {21, 54, 66, 69}
21 + 54 + 66 + 69 = 210
```

## Gold derivation

Place the cube with one vertex on the plane. The eight vertices have signed distances of the form

    d(α, β, γ) = (1 + α) u + (1 + β) v + (1 + γ) w,    α, β, γ ∈ {−1, +1},

with 4(u² + v² + w²) = s². The (−, −, −) vertex sits at distance 0; the other seven have absolute distances {2|u|, 2|v|, 2|w|, 2|u+v|, 2|u+w|, 2|v+w|, 2|u+v+w|} = {1,2,3,4,5,6,7}.

Up to relabeling of axes and global sign flip, two essentially distinct sign-pattern families remain.

**Case A (all of u, v, w same sign).** Summing the seven non-zero distances gives 8(u+v+w) = 28, so 2(u+v+w) = 7. The remaining six values split {2u, 2v, 2w} (sum 7) and {2(u+v), 2(u+w), 2(v+w)} (sum 14). The only distinct triple of {1,…,6} summing to 7 is {1, 2, 4}, so s² = 1²+2²+4² = **21**.

**Case B (one axis flipped, WLOG w < 0).** Write p = 2u, q = 2v, r = 2|w|. The multiset {p, q, r, p+q, |p−r|, |q−r|, |p+q−r|} = {1,…,7}. Casework on r forces r ≥ p+q (the only feasible regime), giving r = 7. The six remaining values pair up as three sum-7 pairs from {1,…,6}: {1,6}, {2,5}, {3,4}. The three valid (p, q) assignments give:

| (p, q, r) | s² = p² + q² + r² |
|---|---|
| (1, 2, 7) | **54** |
| (1, 4, 7) | **66** |
| (2, 4, 7) | **69** |

Other Case-B sub-cases (flipping the smallest or middle axis; or r < p+q) all degenerate. Total: s² ∈ {21, 54, 66, 69} ⇒ **210**.

Because none of the nine released responses produces 210, `acceptable_solution_ids` is the empty list.

## Scoring rubric (LLM-judge verifier)

The verifier (`tests/judge.py`) scores `/logs/agent/output.json` against `tests/oracle.json` with the following weighted fields. Total possible weight is **2307 points**; the reward is `earned / 2307` clipped to [0.0, 1.0]. An exact JSON-equality match short-circuits to reward = 1.0.

- `gold_final_answer` (string match): 2
- `gold_edge_length_squared_set` (sorted-list match): 2
- `acceptable_solution_ids` (set match): 2
- Per response (nine times, 99 fixed pts each = 891):
  - `final_answer_correct` (exact bool match): 5
  - `failure_reasons` (substantive set match against oracle; 30 exact / 15 off-by-one substantively-equivalent / 8 overlap ≥50% / 0 otherwise): 30 max
  - `primary_failure_code` (25 exact; 10 if in oracle's failure_reasons set but not primary; else 0): 25 max
  - `primary_failure_code_evidence` (presence + ≥50 chars): 8
  - `alternative_codes_considered` (≥2 well-formed entries; each `code` from the controlled vocabulary or `"NONE"`, each `code` different from this response's `primary_failure_code`, each `reason_excluded` ≥20 chars): 8
  - `code_application_count` (integer match against oracle = len(failure_reasons)): 10
  - `primary_in_set_check` (bool match): 5
  - `evidence_key_completeness` (integer match): 8
- `failure_reason_evidence` per oracle-listed code (presence + ≥20 chars): 5 per code (sum across all 9 responses = 36 codes × 5 = 180)
- `code_application_table` per key (12 keys, each value an exact sorted-list match): 100 per key (1200 total)
- `cross_response_observations` (presence + ≥300 chars): 30

Total: 6 + 891 + 180 + 1200 + 30 = 2307.

## Failure-reason code meanings

- `claims_unique_edge_length` — final stated conclusion asserts |S| = 1 (regardless of value).
- `restricts_to_nonnegative_subset_sums` — load-bearing argument requires the seven non-zero distances to be subset sums of positive {p, q, r}.
- `assumes_max_distance_equals_space_diagonal` — sets 7 = a√3, deriving a = 7/√3, s² = 49/3.
- `assumes_plane_parallel_to_cube_face` — primary geometric setup is an axis-aligned cube cut by z = k.
- `equates_max_distance_with_edge_length_directly` — sets a = 7 directly with s² = 49.
- `uses_fabricated_invariant_or_invalid_derivation` — final answer rests on an invented algebraic identity.
- `accepts_internal_contradictions_in_derivation` — response openly accepts "6=7"/"3=4" and proceeds.
- `assumes_zero_distance_vertex_is_axis_corner` — pins the distance-0 vertex at the cube-local (0,0,0) corner.
- `omits_sign_pattern_casework` — reaches a numeric conclusion without branching on signed-distance sign families.
- `treats_one_orientation_as_proof_of_uniqueness` — solves one orientation and names that s² as the unique answer.
- `derives_correct_partial_s2_then_discards_it` — correctly derives s² = 21 at some point and then rejects it.
- `non_terminating_or_no_final_answer` — no identifiable final numeric answer.

## Per-response rationale

### Response A (qwen3-0.6b — extracted "6")
Sets up an axis-aligned cube with (0,0,0) on the plane and other vertices as non-negative coordinate combinations. Repeatedly hits the contradiction 6 = 7 / 3 = 4 and treats it as resolvable; ultimately invents a distance assignment with duplicates (1,2,3,4,2,3,1,2) and declares the edge length to be √6 with "uniquely determined".
- `failure_reasons`: `accepts_internal_contradictions_in_derivation`, `assumes_zero_distance_vertex_is_axis_corner`, `claims_unique_edge_length`, `omits_sign_pattern_casework`, `uses_fabricated_invariant_or_invalid_derivation`.

### Response B (deepscaler-1.5b-preview — extracted "49")
Plane parallel to a face (z = k), vertex distances as z-coordinates. Concludes "the only possible edge length is 7" — identifying edge length directly with the max distance.
- `failure_reasons`: `assumes_plane_parallel_to_cube_face`, `claims_unique_edge_length`, `equates_max_distance_with_edge_length_directly`, `omits_sign_pattern_casework`.

### Response C (still-3-1.5b-preview — extracted "49/3")
Body-diagonal aligned setup. Identifies max vertex distance (7) with the space diagonal a√3, deriving a = 7/√3 and s² = 49/3, asserted as the unique value.
- `failure_reasons`: `assumes_max_distance_equals_space_diagonal`, `claims_unique_edge_length`, `omits_sign_pattern_casework`, `treats_one_orientation_as_proof_of_uniqueness`.

### Response D (deepseek-r1-distill-qwen-1.5b — extracted "49/3")
Same load-bearing identification as Response C: a√3 = 7 ⇒ a = 7/√3, asserted as unique.
- `failure_reasons`: same as Response C.

### Response E (openmath-nemotron-1.5b — extracted null)
Decoder-level repetition loop on "Let's let's denote…" for ~10,000 lines until truncation. No final answer.
- `failure_reasons`: `non_terminating_or_no_final_answer`.

### Response F (light-r1-7b-ds — extracted "21")
Fixes the zero-vertex at the cube's (0,0,0) corner; requires u, v, w > 0 (subset sums of positive {p, q, r}); finds (1, 2, 4) ⇒ s² = 21 from the all-positive case alone; asserts "signed projections all same sign" and uniqueness from this one orientation.
- `failure_reasons`: `assumes_zero_distance_vertex_is_axis_corner`, `claims_unique_edge_length`, `omits_sign_pattern_casework`, `restricts_to_nonnegative_subset_sums`, `treats_one_orientation_as_proof_of_uniqueness`.

### Response G (openthinker2-7b — extracted "140/3")
Places the cube at the origin (axis-aligned). Invents the identity `3a²(1 + T²) = 140` as a sum-of-squared-distances invariant, reduces it to a quadratic, and reports the Vieta sum 140/3. Along the way correctly derives a² = 21 from the all-positive case but rejects it because it fails the fabricated invariant. Because the final answer is presented as a sum over multiple candidates, `claims_unique_edge_length` does NOT fire.
- `failure_reasons`: `assumes_zero_distance_vertex_is_axis_corner`, `derives_correct_partial_s2_then_discards_it`, `uses_fabricated_invariant_or_invalid_derivation`.

### Response H (skywork-or1-math-7b — extracted "21")
Identical structural failure to F: zero-vertex at (0,0,0), subset-sum search over positive integer triples, unique triple {1, 2, 4} ⇒ s² = 21 named as the only edge length.
- `failure_reasons`: same as Response F.

### Response I (openmath-nemotron-7b — extracted "21")
Identical structural failure to F and H: non-negative projections, positive-integer triple search, unique (1, 2, 4), S = {√21}.
- `failure_reasons`: same as Response F.

## Primary failure code selections

Per-response `primary_failure_code` choices follow the universal selection rules (non-terminating stands alone; fabrication outranks accepted-contradictions; explicit discard outranks fabrication; subset-sum restriction outranks the downstream corner choice; space-diagonal identification outranks orientation-uniqueness and uniqueness wording; face-parallel framing outranks the direct edge-equals-max identification it produces; `claims_unique_edge_length` and `omits_sign_pattern_casework` are never picked as primary when other codes apply).

| response_id | primary_failure_code |
|---|---|
| A | `uses_fabricated_invariant_or_invalid_derivation` |
| B | `assumes_plane_parallel_to_cube_face` |
| C | `assumes_max_distance_equals_space_diagonal` |
| D | `assumes_max_distance_equals_space_diagonal` |
| E | `non_terminating_or_no_final_answer` |
| F | `restricts_to_nonnegative_subset_sums` |
| G | `derives_correct_partial_s2_then_discards_it` |
| H | `restricts_to_nonnegative_subset_sums` |
| I | `restricts_to_nonnegative_subset_sums` |

## code_application_table

Mechanically built from the nine `failure_reasons` sets: each of the 12 codes maps to the alphabetically-sorted list of response_ids whose set contains it.

| code | response_ids |
|---|---|
| claims_unique_edge_length | A, B, C, D, F, H, I |
| restricts_to_nonnegative_subset_sums | F, H, I |
| assumes_max_distance_equals_space_diagonal | C, D |
| assumes_plane_parallel_to_cube_face | B |
| equates_max_distance_with_edge_length_directly | B |
| uses_fabricated_invariant_or_invalid_derivation | A, G |
| accepts_internal_contradictions_in_derivation | A |
| assumes_zero_distance_vertex_is_axis_corner | A, F, G, H, I |
| omits_sign_pattern_casework | A, B, C, D, F, H, I |
| treats_one_orientation_as_proof_of_uniqueness | C, D, F, H, I |
| derives_correct_partial_s2_then_discards_it | G |
| non_terminating_or_no_final_answer | E |

Coverage: each of {A, B, C, D, E, F, G, H, I} appears in `code_application_table` once per code in its `failure_reasons` set (5+4+4+4+1+5+3+5+5 = 36 total list entries).
