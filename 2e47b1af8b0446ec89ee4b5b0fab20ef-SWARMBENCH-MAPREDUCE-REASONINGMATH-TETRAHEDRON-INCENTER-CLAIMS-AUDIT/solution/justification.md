# Oracle Justification

This document derives every value in `tests/oracle.json` and `solution/oracle.json` (byte-identical). It exists so that a QA reviewer can independently verify each oracle field against (1) the underlying mathematics, (2) the candidate solution text in `environment/input_artifacts/proposed_solutions/`, and (3) the controlled `failure_reasons` vocabulary in `instruction.md`.

Citations are direct quotes from the raw candidate files; no hand-editing.

---

## Gold set: `{a, b, c, d, e}`

The problem hypotheses are:

- **H1.** All dihedral angles between faces of `ABCD` are acute.
- **H2.** `vol(IABC)/BC = vol(IACD)/CD = vol(IADB)/DB`.

### Reduction R1 (used by every gold proof)

Because the insphere is tangent to face `ABC` with distance `r` from `I`, `vol(IABC) = (1/3)*area(ABC)*r`. Dividing H2 by `(r/3)`:

```
area(ABC)/BC = area(ACD)/CD = area(ABD)/DB.       [R1]
```

### Reduction R2

Since `area(ABX) = (1/2)*BX*dist(A, line BX)`, dividing each ratio in R1 by `(1/2)*BX`:

```
dist(A, BC) = dist(A, CD) = dist(A, DB) =: h.     [R2]
```

### Per-statement derivation

- **(a) AI perpendicular to plane BCD. TRUE.** Let `K = AI ∩ plane BCD`. The volume identity gives `K` equidistant from the three sides of `BCD`. R2 gives the foot `L` of perpendicular from `A` also equidistant. Acuteness (H1) forces both interior, hence both equal the incenter of `BCD`, so `L = K` and `AI ⊥ plane BCD`.
- **(b) Projection of A onto plane BCD = incenter of BCD. TRUE.** R2 + H1.
- **(c) dist(A, BC) = dist(A, CD) = dist(A, DB). TRUE.** R2 directly.
- **(d) area(ABC) : area(ACD) : area(ABD) = BC : CD : DB. TRUE.** R1 rearranged.
- **(e) Insphere touch point on face BCD = incenter of BCD. TRUE.** Touch point = projection of `I` on `BCD`. By (a), `I`'s projection equals `A`'s projection, which by (b) is the incenter of `BCD`.
- **(f) AB = AC = AD. FALSE in general.** Take any scalene acute `BCD`, place `A` above its incenter at small height. Then `AB² = h² + |QB|²` etc., and `|QB|, |QC|, |QD|` differ.
- **(g) AB = AC. FALSE in general.** Same counterexample.
- **(h) BCD equilateral. FALSE in general.** Same counterexample.

`gold_set = ["a","b","c","d","e"]`.

---

## Acceptable solutions: `["A", "D", "I"]`

A response is acceptable iff its claimed set equals the gold set AND its proof has no defect. Equivalent oracle condition: `final_answer_correct = true` AND `failure_reasons = []`.

- **A**: claims `{a,b,c,d,e}`; proof derives R2, locates A's projection, applies the tetrahedron-incenter formula to align A's and I's projections, concludes (a) and (e). Sound.
- **D**: claims `{a,b,c,d,e}`; proof uses the dihedral-bisector approach (I lies on the bisector plane of each dihedral angle at edges AB, AC, AD; bisector planes restrict to the angle bisectors of triangle BCD; AI passes through the incenter of BCD). Sound.
- **I**: claims `{a,b,c,d,e}`; proof derives R2, locates A's projection at the incenter of BCD, observes I's projection coincides, concludes (a) and the touch-point identity. Sound.

Response C states the gold set but its proof rests on the false universal `false_universal_insphere_at_face_incenter`, so C is excluded. Responses B, E, F, G, H all have `final_answer_correct = false`.

---

## Per-response `failure_reasons` rationale

The judge compares the agent's `failure_reasons` list against the oracle's list as a set per response (case-insensitive). All expected labels must appear; no extras may appear.

### Response A

`final_answer_correct: true`; claimed `{a,b,c,d,e}` (cited: `"$$\boxed{\{a, b, c, d, e\}}$$"`).
`failure_reasons: []`. The proof derives R2, locates A's projection at the incenter via the equivalence `area(ACD)/|CD| = (1/2)*d(A,CD)`, and applies the tetrahedron-incenter formula `I = (Σ Sᵢ vᵢ)/(Σ Sᵢ)` to align A's and I's projections. No defect.

### Response B

`final_answer_correct: false`; claimed `{b, c, d}` (cited: `"$$\boxed{\{c, d, b\}}$$"`).
`failure_reasons: ["rejected_perpendicularity_no_counterexample", "cascaded_rejection_of_e_from_a"]`.
Rejects (a) with: *"For this to be true, we'd need A to lie on the line through I perpendicular to plane BCD. ... This is not necessarily true from our conditions. Counterexample: we can have a tetrahedron satisfying (2) where AI is not perpendicular to BCD."* — assertion without construction. Then rejects (e) on the grounds that (e) follows from (a).

### Response C

`final_answer_correct: true`; claimed `{a,b,c,d,e}` (cited: `"$$\boxed{\{a,b,c,d,e\}}$$"`).
`failure_reasons: ["correct_gtfa_invalid_proof_chain", "false_universal_insphere_at_face_incenter"]`.
Step 3 cites: *"The incenter of triangle BCD is exactly the tangency point of the insphere with face BCD (since the insphere is tangent to each face at its face-incenter)."* The parenthetical clause is the FALSE universal; the universal claim is the load-bearing premise for the proofs of (a) and (e). Final answer happens to be correct, but the proof chain is invalid.

### Response D

`final_answer_correct: true`; claimed `{a,b,c,d,e}` (cited: `"$$\boxed{\{a,,b,,c,,d,,e\}}$$"` — double commas are formatting artifacts; set content unambiguous).
`failure_reasons: []`. Proof: *"Because I is equidistant from the two planes ABC and ABD, it lies on the internal bisector of the dihedral angle along the edge AB. Analogous statements hold for edges AC and AD. The three bisector planes meet in the line AI; each of them also contains the corresponding interior bisector of the angle of triangle BCD at B, C, D respectively, and these three angle bisectors meet at the incentre H."* Concise and sound.

### Response E

`final_answer_correct: false`; claimed `{c, d, e}` (cited: *"the final answer is: {c,d,e}"*).
`failure_reasons: ["confused_centroid_and_incenter", "self_contradictory_centroid_above", "vague_word_salad_proofs"]`.
Self-contradictory counterexample for (a): *"Consider a tetrahedron where A lies directly above the centroid of BCD but is not orthogonal."* — "directly above" already implies orthogonal. The same sentence substitutes the centroid for the incenter. Proofs of (c), (d), (e) appeal to unrelated concepts: *"symmetry about point A"*, *"circumcircle properties dictated by the dihedral angles"*, *"by definition of the inradius"*.

### Response F

`final_answer_correct: false`; claimed `{d, e}` (cited: *"The set of statement labels that is necessarily true is {d, e}."*).
`failure_reasons: ["cot_trace_misses_distance_equivalence", "repeats_false_universal_in_e", "vague_almost_regular_nonconstruction"]`.
The visible chain-of-thought derives `area(ABC)/BC = area(ACD)/CD = area(ABD)/DB` and then writes for (c): *"In a regular tetrahedron, yes, the distances from A to the edges BC, CD, DB are equal due to symmetry. But in general, probably not."* — fails to translate R1 into R2. In the (e) section: *"For a tangential tetrahedron, the point of tangency on each face is the incenter of that face."* — restates the false universal. Elsewhere appeals to "almost regular" non-constructions.

### Response G

`final_answer_correct: false`; claimed `{d}` (cited: *"The only statement that is necessarily true is (d)."*).
`failure_reasons: ["rejects_e_via_general_property_misapplied", "vague_almost_regular_nonconstruction"]`.
For (e): *"The incenter of BCD is the intersection of the angle bisectors, which is not necessarily the foot of the perpendicular from I to BCD"* — true in isolation, but ignores whether H2 forces the two points to coincide here (it does). For (a) and (b): *"Consider a tetrahedron that is 'almost' regular, but slightly skewed. It's possible to satisfy the volume condition without AI being perpendicular to BCD."* — no construction.

### Response H

`final_answer_correct: false`; claimed set excludes one or more of `{a,b,c,d,e}`.
`failure_reasons: ["degenerate_counterexample_b_equals_c", "false_claim_ai_equals_inradius", "incoherent_ratio_argument_in_b"]`.
Asserts `AI = r` while defending (b) — mathematically false (since `I` is strictly interior to the tetrahedron, `AI > r`). The 1:1 ratio argument in the (b) section is incoherent: it mixes `dist(A, plane BCD)` with `r` without a derivation. The "counterexample" reduces to a degenerate configuration that does not satisfy the hypotheses.

### Response I

`final_answer_correct: true`; claimed `{a,b,c,d,e}`.
`failure_reasons: []`. Proof: derives R2, locates A's projection at the incenter of BCD via R2 + acuteness, observes I's projection on plane BCD coincides with A's projection (so AI passes through both projections), concludes `AI ⊥ plane BCD`, then derives (e) directly.

---

## Schema compliance

- `gold_set` is lowercase a..h, alphabetically sorted.
- `acceptable_solution_ids` is uppercase A..I, alphabetically sorted.
- `per_response_assessment` contains exactly 9 entries, ordered A, B, C, D, E, F, G, H, I.
- Each entry has exactly the keys `response_id`, `final_answer_correct`, `failure_reasons`.
- All `failure_reasons` labels are lower_snake_case and drawn from the controlled vocabulary in `instruction.md`.
- `tests/oracle.json` and `solution/oracle.json` are byte-identical, activating the exact-match shortcut in `tests/judge.py` for the oracle agent run.
