# Oracle Justification — TETRIS-pattern set-match scoring

This document derives every value in `tests/oracle.json` and `solution/oracle.json` (byte-identical). It exists so that a QA reviewer can independently verify each oracle field against (1) the underlying mathematics, (2) the candidate solution text, and (3) the controlled `failure_reasons` vocabulary in `instruction.md`.

Citations are direct quotes from the raw candidate files in `environment/input_artifacts/`. The candidate files are byte-identical to what the candidate models produced — no hand-editing.

---

## Oracle schema

```json
{
  "gold_set": ["a", "b", "c", "d", "e"],
  "acceptable_solution_ids": ["A", "D", "I"],
  "per_response_assessment": [
    { "response_id": "A", "final_answer_correct": true, "failure_reasons": [] },
    ...
  ]
}
```

## Judge scoring (deterministic, no LLM)

- `gold_set` set match: **2 pts**.
- `acceptable_solution_ids` set match: **2 pts**.
- Per response: `failure_reasons` set match (all-or-nothing): **30 pts**.

Total = 4 + 9 × 30 = **274 pts**. Reward = total_passed / 274.

Set match means EXACTLY the expected labels — a subset or superset scores 0 for that response. This is the structural lever from the TETRIS-ROW-CLEAR-AUDIT winner (gap 0.64): a sub-agent with isolated context per candidate can identify the full set carefully; a single agent juggling 9 candidates simultaneously consistently picks 2-of-3 and zeroes the 30-pt block.

---

## Part A — Why `gold_set = {a, b, c, d, e}`

The problem is the modified CMO 2026 P4 multi-claim form. Hypotheses:

- **H1.** All dihedral angles between faces of `ABCD` are acute.
- **H2.** `vol(IABC)/BC = vol(IACD)/CD = vol(IADB)/DB`, where `I` is the incenter.

### Reduction of H2 (used by every gold proof)

Because the insphere is tangent to face `ABC` with distance `r` from `I`, `vol(IABC) = (1/3)·area(ABC)·r`. Dividing H2 by `(r/3)`:

```
area(ABC)/BC = area(ACD)/CD = area(ABD)/DB.       [R1]
```

Since `area(ABX) = (1/2)·BX·dist(A, line BX)`, dividing each ratio by `(1/2)·BX`:

```
dist(A, BC) = dist(A, CD) = dist(A, DB) =: h.     [R2]
```

### Per-statement derivation

- **(a) AI ⊥ plane BCD. TRUE.** Let `K = AI ∩ plane BCD`. Volume identity → `K` is equidistant from the three sides of `BCD`. R2 → foot `L` of perpendicular from `A` is also equidistant. Acuteness (H1) forces both interior, hence both equal the incenter of `BCD`, so `L = K` and `AI ⊥ plane BCD`. (CMO 2026 P4 Solution 1.)
- **(b) Projection of A on plane BCD = incenter of BCD. TRUE.** R2 + H1.
- **(c) dist(A, BC) = dist(A, CD) = dist(A, DB). TRUE.** R2 directly.
- **(d) area(ABC) : area(ACD) : area(ABD) = BC : CD : DB. TRUE.** R1 rearranged.
- **(e) Insphere touch point on face BCD = incenter of BCD. TRUE.** Touch point = projection of `I` on `BCD`. By (a) `I`'s projection = `A`'s projection, which by (b) is the incenter of `BCD`.
- **(f) AB = AC = AD. FALSE in general.** Take any scalene acute `BCD`, place `A` above its incenter at small height. Then `AB² = h² + |QB|²` etc., and `|QB|, |QC|, |QD|` differ.
- **(g) AB = AC. FALSE in general.** Same counterexample.
- **(h) BCD equilateral. FALSE in general.** Same counterexample.

`gold_set = ["a","b","c","d","e"]`.

---

## Part B — `acceptable_solution_ids = ["A", "D", "I"]`

A candidate is acceptable iff its stated final set equals `gold_set` AND its proof is fully valid (no false universal, no logical gap, no unconstructed counterexample). Equivalent oracle condition: `final_answer_correct = true` AND `failure_reasons = []`.

- **A (Sonnet 4.5):** stated set `{a,b,c,d,e}`; proof derives R2, then R2 + H1 → (b); derives tetrahedron-incenter formula → I's projection = A's projection → (a); then (e) follows. Sound. ✓
- **D (GPT-o3):** stated set `{a,b,c,d,e}`; proof follows CMO Solution 2 (dihedral-bisector planes meet in line `AI`; their traces in `BCD` are the angle bisectors of `BCD`, meeting at the incenter). Concise and sound. ✓
- **I (DeepSeek v3.1):** stated set `{a,b,c,d,e}`; proof derives R2, locates A's projection at the incenter of BCD, observes I's projection coincides, concludes AI ⊥ plane BCD and the touch point identity. Sound. ✓

Candidate C states the gold set but its proof rests on a false universal (`false_universal_insphere_at_face_incenter`), so C is excluded. The other candidates (B, E, F, G, H) have `final_answer_correct = false`.

---

## Part C — Per-candidate `failure_reasons` (set-match exact)

The judge compares the agent's `failure_reasons` list against the oracle's list as a set per response. All expected labels must appear; no extras may appear.

### Response A — Sonnet 4.5
- `final_answer_correct: true` — stated set `{a,b,c,d,e}` (cited: `"$$\boxed{\{a, b, c, d, e\}}$$"`).
- `failure_reasons: []`. Proof is sound (Part B summary applies).

### Response B — Claude Haiku
- `final_answer_correct: false` — stated set `{b, c, d}` (cited: `"$$\boxed{\{c, d, b\}}$$"`).
- `failure_reasons: ["rejected_perpendicularity_no_counterexample", "cascaded_rejection_of_e_from_a"]`.
  - Rejected (a) with: *"For this to be true, we'd need A to lie on the line through I perpendicular to plane BCD ... This is not necessarily true from our conditions. Counterexample: we can have a tetrahedron satisfying (2) where AI is not perpendicular to BCD."* — assertion without construction.
  - Subsequently rejects (e) because (e) follows from (a) — the rejection cascade.

### Response C — GPT-5.2
- `final_answer_correct: true` — stated set `{a,b,c,d,e}` (cited: `"$$\boxed{\{a,b,c,d,e\}}$$"`).
- `failure_reasons: ["correct_gtfa_invalid_proof_chain", "false_universal_insphere_at_face_incenter"]`.
  - Step 3 cites: *"The incenter of triangle BCD is exactly the tangency point of the insphere with face BCD (since the insphere is tangent to each face at its face-incenter)."* — the parenthetical is the FALSE universal; the universal claim is the load-bearing step for (a) and (e), so the proof chain is invalid.
  - C does NOT repeat the universal in a separate (e) defence beyond the use above; `repeats_false_universal_in_e` does NOT apply.

### Response D — GPT-o3
- `final_answer_correct: true` — stated set `{a,b,c,d,e}` (cited: `"$$\boxed{\{a,,b,,c,,d,,e\}}$$"`; double commas are formatting artifacts).
- `failure_reasons: []`. Proof is sound (Part B summary applies).

### Response E — GPT-4o-mini
- `final_answer_correct: false` — stated set `{c, d, e}` (cited: `"the final answer is: {c,d,e}"`).
- `failure_reasons: ["confused_centroid_and_incenter", "self_contradictory_centroid_above", "vague_word_salad_proofs"]`.
  - Self-contradictory counterexample: *"Consider a tetrahedron where A lies directly above the centroid of BCD but is not orthogonal."* — "directly above" already implies orthogonal.
  - The same sentence substitutes the centroid for the incenter; the candidate uses "centroid" again later when discussing where `A` projects.
  - "Proofs" of (c), (d), (e) reference unrelated concepts: *"symmetry about point A"*, *"circumcircle properties dictated by the dihedral angles"*, *"by definition of the inradius"* — multiple word-salad lines, not isolated phrasing.

### Response F — Grok 3 mini (with visible chain-of-thought)
- `final_answer_correct: false` — stated set `{d, e}` (cited: `"The set of statement labels that is necessarily true is {d, e}."`).
- `failure_reasons: ["cot_trace_misses_distance_equivalence", "repeats_false_universal_in_e", "vague_almost_regular_nonconstruction"]`.
  - The trace derives `area(ABC)/BC = area(ACD)/CD = area(ABD)/DB` and then writes for (c): *"In a regular tetrahedron, yes, the distances from A to the edges BC, CD, DB are equal due to symmetry. But in general, probably not."* — fails to translate R1 into R2 and rejects (c).
  - In the (e) part of the trace: *"For a tangential tetrahedron, the point of tangency on each face is the incenter of that face. Is that true? Yes, because the incenter is equidistant from the sides, and the sphere is tangent..."* — restates the false universal in the (e) defence.
  - Elsewhere the trace appeals to almost-regular non-constructions.

### Response G — Gemini 2.0 Flash
- `final_answer_correct: false` — stated set `{d}` (cited: `"The only statement that is necessarily true is (d)."`).
- `failure_reasons: ["rejects_e_via_general_property_misapplied", "vague_almost_regular_nonconstruction"]`.
  - For (e): *"The incenter of BCD is the intersection of the angle bisectors, which is not necessarily the foot of the perpendicular from I to BCD"* — true as a general statement, but G never checks whether H2 forces these to coincide in this setup (which it does).
  - For (a) and (b): *"Consider a tetrahedron that is 'almost' regular, but slightly skewed. It's possible to satisfy the volume condition without AI being perpendicular to BCD."* — pure hand-wave, no construction.

### Response H — Llama
- `final_answer_correct: false` — stated set excludes one or more of `{a,b,c,d,e}` per the response file.
- `failure_reasons: ["degenerate_counterexample_b_equals_c", "false_claim_ai_equals_inradius", "incoherent_ratio_argument_in_b"]`.
  - Asserts `AI = r` while defending (b) — mathematically false (since `I` is strictly interior to the tetrahedron, `AI > r`).
  - The 1:1 ratio argument in the (b) section is incoherent: it mixes `dist(A, plane BCD)` with `r` without a derivation.
  - The candidate's "counterexample" used to support its rejection collapses to a degenerate case (`B = C` or collinear `B, C, D`), which does not satisfy the hypotheses.

### Response I — DeepSeek v3.1
- `final_answer_correct: true` — stated set `{a,b,c,d,e}`.
- `failure_reasons: []`. Proof is sound (Part B summary applies).

---

## Part D — Schema compliance

- `gold_set` is lowercase a..h, alphabetically sorted ✓.
- `acceptable_solution_ids` is uppercase A..I, alphabetically sorted ✓.
- `per_response_assessment` contains exactly 9 entries, ordered A, B, C, D, E, F, G, H, I ✓.
- Each entry has exactly the keys `response_id`, `final_answer_correct`, `failure_reasons` ✓.
- All `failure_reasons` labels are lower_snake_case and drawn from the controlled vocabulary in `instruction.md` ✓.
- `tests/oracle.json` and `solution/oracle.json` are byte-identical, activating the exact-match shortcut in `tests/judge.py` for the oracle agent run.
