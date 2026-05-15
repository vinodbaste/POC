# Tetrahedron Incenter — Candidate Solution Audit

You are auditing nine model-produced solutions to an olympiad-level 3D geometry problem. Read each candidate solution and produce a structured audit object for it. You are **auditing**, not solving the problem from scratch.

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
  "response_audits": [
    {
      "response_id": "A",
      "final_answer_correct": <bool>,
      "proof_valid": <bool>,
      "verdict": "<one of the verdict vocabulary below>",
      "primary_error_label": "<one of the primary_error_label vocabulary below>",
      "required_evidence_label": "<one of the required_evidence_label vocabulary below>"
    },
    ... (one entry per response file, 7 total, ordered A through G)
  ]
}
```

### Field semantics

- `final_answer_correct`: true iff the candidate's stated SET of necessarily-true statements equals the gold set `{a, b, c, d, e}` (as a set; order irrelevant).
- `proof_valid`: true iff the candidate's argument is logically sound AND complete (no false math claims, no unconstructed counterexamples, no logical gaps). For a candidate whose `final_answer_correct = true` but whose proof relies on a false universal claim (e.g. asserting that the insphere of any tangential tetrahedron is tangent at the face-incenter), `proof_valid` is **false**.
- `verdict`: a categorical assessment combining the two above.
- `primary_error_label`: the SPECIFIC error pattern this candidate exhibits (or `NO_ERROR`).
- `required_evidence_label`: the specific lemma or argument the candidate would have needed to make the proof valid (or `NO_ERROR` if the proof is already valid).

### `verdict` vocabulary (use exactly one)

- `correct` — final answer matches gold AND proof is valid.
- `incorrect` — final answer does NOT match gold.
- `correct_final_answer_but_invalid_proof` — final answer matches gold but proof has a false claim, logical gap, or unsupported step.

### `primary_error_label` vocabulary (use exactly one per response)

- `NO_ERROR` — the proof is valid; no error to flag.
- `REJECTED_PERPENDICULARITY_WITHOUT_COUNTEREXAMPLE` — the candidate rejects statement (a) (AI ⊥ plane BCD) by asserting a counterexample exists but never constructs one. The hypothesis is in fact strong enough to force (a).
- `FALSE_INSPHERE_FACE_INCENTER_UNIVERSAL_AS_PREMISE` — the candidate uses the universal claim "the insphere of any tangential tetrahedron is tangent to each face at the face-incenter" as a premise. This claim is FALSE in general; it requires extra symmetry. The candidate's final answer may be correct but the proof of (a) and/or (e) rests on this false universal.
- `SELF_CONTRADICTORY_CENTROID_COUNTEREXAMPLE` — the candidate proposes a counterexample of the form "A lies directly above the centroid of BCD but is not orthogonal" or similar, which is self-contradictory because "directly above the centroid" already implies orthogonality. Often confuses centroid with incenter.
- `MISSED_VOLUME_TO_DISTANCE_EQUIVALENCE_IN_COT` — the candidate's reasoning trace derives area(ABX)/BX = ... but never recognizes that this equals (1/2)·dist(A, line BX), and therefore rejects statement (c) or (b) even though they are direct consequences of the hypothesis.
- `VAGUE_ALMOST_REGULAR_NON_CONSTRUCTION` — the candidate dismisses statements with hand-wavy phrases like "consider a tetrahedron that is almost regular but slightly skewed" or "it is possible to construct" without any concrete construction.
- `WRONG_PROJECTION_TARGET` — distractor; do not use unless an audit clearly fits.
- `CIRCULAR_BISECTOR_ARGUMENT` — distractor; do not use unless an audit clearly fits.
- `OVERCLAIMS_EQUILATERAL_BCD` — distractor; do not use unless an audit clearly fits.
- `FALSE_CLAIM_AI_EQUALS_INRADIUS_R` — the candidate's proof asserts the false equality "AI = r" (the distance from vertex A to the incenter I equals the inradius r). This is mathematically false in general — AI is strictly greater than r since I is interior to the tetrahedron and r is the perpendicular distance from I to each face. Often appears in incoherent proofs of (b) that attempt to use a 1:1 ratio argument.

### `required_evidence_label` vocabulary (use exactly one per response)

- `NO_ERROR` — the proof is valid; nothing required.
- `RECOGNIZE_AI_IS_GREATER_THAN_INRADIUS` — the candidate needed to recognize that the distance AI (from vertex A to the tetrahedron incenter I) is strictly greater than the inradius r, NOT equal to r. AI = r only in degenerate cases.
- `TETRAHEDRON_INCENTER_FORMULA_DERIVATION` — the candidate needed to derive that the tetrahedron's incenter I equals $\sum_i S_i v_i / \sum_i S_i$ (face-area-weighted vertex combination) and apply it to show I's projection on plane BCD coincides with A's projection.
- `DIRECT_TOUCH_POINT_DERIVATION_FROM_PERPENDICULARITY` — the candidate needed to derive the touch point of the insphere on face BCD as a consequence of AI ⊥ plane BCD (using the volume condition), rather than as a universal property of tangential tetrahedra.
- `PROJECTION_IS_INCENTER_NOT_CENTROID` — the candidate needed to recognize that the volume condition forces A's projection on plane BCD to be the incenter of triangle BCD, not the centroid.
- `AREA_OVER_BASE_EQUALS_HALF_DISTANCE_FROM_A` — the candidate needed to apply the identity area(ABX) / BX = (1/2)·dist(A, line BX) to convert the volume condition into the equal-distance condition.
- `VOLUME_CONDITION_FORCES_PERPENDICULARITY` — the candidate needed to recognize that the volume condition (with acuteness) is by itself sufficient to force AI ⊥ plane BCD; their hand-waved "almost regular" non-construction is impossible.
- `ACUTENESS_RULES_OUT_EXCENTER` — distractor; do not use unless an audit clearly fits.
- `DIHEDRAL_BISECTOR_LEMMA` — distractor; do not use unless an audit clearly fits.

### Selection rule

For each response, pick exactly **one** `primary_error_label` from the vocabulary that best matches the candidate's specific error (or `NO_ERROR`). Pick exactly **one** `required_evidence_label` similarly. Do not invent new labels.

## Output rules

- `response_audits` must contain exactly 9 entries, ordered alphabetically by `response_id` (A, B, C, D, E, F, G, H, I).
- Every `response_id` must be uppercase A..I.
- Every field must be present in every entry.
- Top-level keys exactly: `response_audits`. No other top-level keys.
