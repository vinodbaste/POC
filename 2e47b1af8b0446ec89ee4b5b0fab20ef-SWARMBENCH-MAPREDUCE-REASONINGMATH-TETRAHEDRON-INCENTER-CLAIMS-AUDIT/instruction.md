# Tetrahedron Incenter — Candidate Solution Audit

You are auditing nine model-produced solutions to an olympiad-level 3D geometry problem. Read each candidate solution and produce a structured audit object. You are **auditing**, not solving the problem from scratch.

## Working environment

- Candidate solutions: `/input_artifacts/response_A.md` through `/input_artifacts/response_I.md` (9 files).
- Provenance metadata: `/input_artifacts/provenance.json` (informational only — do not let it bias your audit).
- Write your final answer to `/logs/agent/output.json`.

## The problem each candidate solved

Each candidate model was given the following problem verbatim:

> Let $ABCD$ be a tetrahedron with an inscribed sphere of center $I$ and inradius $r > 0$. Suppose (1) the dihedral angle between any two faces of $ABCD$ is acute, and (2) $\mathrm{vol}(IABC)/BC = \mathrm{vol}(IACD)/CD = \mathrm{vol}(IADB)/DB$, where $\mathrm{vol}(IXYZ)$ denotes the volume of the tetrahedron with vertices $I, X, Y, Z$. For each of the following eight statements, decide whether it is necessarily true for every tetrahedron $ABCD$ satisfying both hypotheses, then state the SET of statement labels that are necessarily true.
>
> (a) $AI$ is perpendicular to plane $BCD$.
> (b) The orthogonal projection of $A$ onto plane $BCD$ coincides with the incenter of triangle $BCD$.
> (c) The distances from $A$ to each of the three lines $BC$, $CD$, $DB$ are equal.
> (d) The areas of triangles $ABC$, $ACD$, $ADB$ are in the ratio $BC : CD : DB$.
> (e) The point at which the inscribed sphere touches face $BCD$ is the incenter of triangle $BCD$.
> (f) $AB = AC = AD$.
> (g) Triangle $ABC$ is isosceles with $AB = AC$.
> (h) Triangle $BCD$ is equilateral.

The gold answer set is `{a, b, c, d, e}` (the conclusion of CMO 2026 P4 plus its direct corollaries). Statements (f), (g), (h) are NOT necessarily true.

## Output format

Write exactly this JSON structure to `/logs/agent/output.json`:

```json
{
  "gold_set": ["a", "b", "c", "d", "e"],
  "acceptable_solution_ids": ["A", "D", "I"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": true,
      "failure_reasons": []
    },
    ... (one entry per response file, exactly 9 total, ordered A through I)
  ]
}
```

### Field semantics

- `gold_set`: the alphabetically-sorted, lowercase set of statement labels (a..h) that are necessarily true under the two hypotheses. (You are told this is `["a", "b", "c", "d", "e"]`. Confirm by inspection of the problem and the candidate solutions; this is the same value for every audit run.)
- `acceptable_solution_ids`: the uppercase, alphabetically-sorted list of `response_id` values whose **stated final answer set equals `gold_set`** AND whose proof is fully valid (no false universal claims, no logical gaps, no unconstructed counterexamples). A candidate whose stated set equals the gold but whose proof relies on a false universal is NOT acceptable.
- `per_response_assessment`: list of exactly 9 entries (one per response file), each with the keys below.
  - `response_id`: uppercase letter A..I.
  - `final_answer_correct`: `true` iff the candidate's stated SET of necessarily-true statements equals `gold_set` (as a set; order irrelevant).
  - `failure_reasons`: a LIST (set, order irrelevant; the judge compares as a set) of 0–3 labels drawn from the controlled vocabulary below. Each label is a specific defect in this candidate's argument. An empty list `[]` means the candidate's audit shows no failures (proof is sound; final answer correct).

### `failure_reasons` controlled vocabulary

The judge scores `failure_reasons` by **exact set match per response**: all expected labels must appear, no extras may appear, and matching is case-insensitive. A subset or a superset scores 0 for that response. Pick exactly the labels that match the candidate's defects — no more, no fewer.

Use lower_snake_case labels from this list:

- `rejected_perpendicularity_no_counterexample` — the candidate rejects statement (a) (`AI ⊥ plane BCD`) by asserting that a counterexample exists, but never constructs one. The hypothesis is in fact strong enough to force (a).
- `cascaded_rejection_of_e_from_a` — having rejected (a) (with or without a counterexample), the candidate then rejects (e) on the grounds that (e) follows from (a). The cascading rejection is itself a structural defect because (e) can be defended independently (see candidates D and I).
- `correct_gtfa_invalid_proof_chain` — the candidate's stated set equals the gold set, but the proof contains at least one false math claim, unconstructed step, or logical gap, so the proof is invalid even though the final answer happens to be correct.
- `false_universal_insphere_at_face_incenter` — the candidate uses, as a UNIVERSAL premise, the false claim "the insphere of any tangential tetrahedron is tangent to each face at the face's incenter." This claim is false in general (it requires extra symmetry). Whenever a candidate invokes this universal, this label applies.
- `confused_centroid_and_incenter` — the candidate substitutes "centroid of `BCD`" for "incenter of `BCD`" at a load-bearing step (or asserts that "above the centroid" is equivalent to "above the incenter" or to "AI perpendicular to plane BCD"). The two points are distinct in any non-equilateral triangle.
- `self_contradictory_centroid_above` — the candidate proposes a counterexample of the form "consider a tetrahedron where A lies directly above the centroid of BCD but is not orthogonal to plane BCD" (or any logically equivalent formulation). This is self-contradictory: "directly above" is the definition of orthogonal projection.
- `vague_word_salad_proofs` — the candidate "proves" one or more of the claims with vague, non-mathematical phrases that don't engage with H2 (e.g. "by symmetry about A", "by the circumcircle properties dictated by the dihedral angles", "by definition of the inradius"). At least two of the gold claims are defended with phrases of this kind.
- `cot_trace_misses_distance_equivalence` — the candidate (typically with a visible chain-of-thought) derives the area-over-base identity `area(ABX)/BX = (1/2)·dist(A, line BX)` (or the equivalent `area(ABC)/BC = area(ACD)/CD = area(ABD)/DB`) but explicitly fails to convert it to the equal-distance condition `dist(A, BC) = dist(A, CD) = dist(A, DB)`, ultimately rejecting (c) in spite of having just derived it.
- `repeats_false_universal_in_e` — applies to a candidate who, while defending (e), restates or paraphrases the false universal "the insphere of any tangential tetrahedron is tangent at the face-incenter." (Often co-occurs with `false_universal_insphere_at_face_incenter` when the universal is invoked in MORE than one place.)
- `vague_almost_regular_nonconstruction` — the candidate dismisses one or more of the gold claims with phrases like "consider a tetrahedron that is almost regular but slightly skewed" or "it is possible to construct" without any concrete construction.
- `rejects_e_via_general_property_misapplied` — the candidate rejects (e) by appealing to a general property of inspheres (e.g. "the insphere touch point is not in general the incenter of the face") that is true in isolation but ignores whether the specific hypothesis H2 forces these two points to coincide here, which it does.
- `false_claim_ai_equals_inradius` — the candidate asserts the false equality `AI = r` (distance from vertex `A` to incenter `I` equals the inradius). Since `I` is interior to the tetrahedron and `r` is the perpendicular distance from `I` to each face, `AI > r` in general.
- `incoherent_ratio_argument_in_b` — when defending or rejecting statement (b), the candidate produces an incoherent ratio or proportion argument (often invoking a 1:1 ratio between `AI` and `r`, or comparing `dist(A, plane BCD)` to `r` via an unjustified ratio).
- `degenerate_counterexample_b_equals_c` — the candidate's "counterexample" amounts to a degenerate tetrahedron (e.g. `B = C` or collinear `B, C, D`), which does not satisfy the hypotheses.

### Selection rule

For each response, return the set (as a list) of EXACTLY the labels that describe defects present in that candidate. If the candidate's stated set equals the gold AND its proof is valid, return `[]` (empty list). The judge scores by set equality per response.

## Output rules

- `per_response_assessment` must contain exactly 9 entries, ordered alphabetically by `response_id` (A, B, C, D, E, F, G, H, I).
- Every `response_id` must be uppercase A..I.
- Every entry must have exactly these three keys: `response_id`, `final_answer_correct`, `failure_reasons`. No additional per-entry keys.
- Top-level keys exactly: `gold_set`, `acceptable_solution_ids`, `per_response_assessment`. No other top-level keys.
- `gold_set` is lowercase a..h, alphabetically sorted.
- `acceptable_solution_ids` is uppercase A..I, alphabetically sorted.
- `failure_reasons` labels are lower_snake_case and drawn ONLY from the vocabulary above.
