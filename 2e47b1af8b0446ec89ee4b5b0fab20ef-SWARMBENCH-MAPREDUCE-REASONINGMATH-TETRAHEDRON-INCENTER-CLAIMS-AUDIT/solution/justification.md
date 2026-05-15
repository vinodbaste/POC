# Oracle Justification

This document derives every value in `tests/oracle.json` and `solution/oracle.json` (byte-identical). It exists so that a QA reviewer can independently verify each oracle field against (1) the underlying mathematics, (2) the literal phrase triggers defined in `instruction.md`, and (3) the candidate solution text in `environment/input_artifacts/proposed_solutions/`.

The audit uses a phrase-triggered failure_reasons vocabulary: each of the 5 codes applies if and only if its specific trigger phrase (or a near-verbatim paraphrase) appears in the candidate response's text. This makes per-response audits mechanical.

---

## Gold set: `{a, b, c, d, e}`

The problem hypotheses are:

- **H1.** All dihedral angles between faces of `ABCD` are acute.
- **H2.** `vol(IABC)/BC = vol(IACD)/CD = vol(IADB)/DB`.

### Reduction R1

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

- **(a) AI perpendicular to plane BCD. TRUE.** R2 places foot-of-perpendicular from `A` at the incenter of `BCD`; the volume identity forces `AI ∩ plane BCD` to be the same point; acuteness rules out external bisector solutions. Hence `AI ⊥ plane BCD`.
- **(b) Projection of A onto plane BCD = incenter of BCD. TRUE.** R2 + H1.
- **(c) dist(A, BC) = dist(A, CD) = dist(A, DB). TRUE.** R2 directly.
- **(d) area(ABC) : area(ACD) : area(ABD) = BC : CD : DB. TRUE.** R1 rearranged.
- **(e) Insphere touch point on face BCD = incenter of BCD. TRUE.** By (a), `I`'s projection equals `A`'s projection, which by (b) is the incenter.
- **(f), (g), (h). FALSE in general.** Counterexample: any scalene acute `BCD` with `A` placed above its incenter at a suitable height satisfies the hypotheses but gives unequal `AB, AC, AD`.

`gold_set = ["a","b","c","d","e"]`.

---

## Acceptable solutions: `["A", "D", "I"]`

A response is acceptable iff its claimed set equals the gold set AND no failure-reason trigger phrase fires on its text. Equivalent oracle condition: `final_answer_correct = true` AND `failure_reasons = []`.

- **A**: claims `{a,b,c,d,e}`. No trigger phrase from the 5-code vocabulary appears in A's text (no "AI = r"; no "we can have a tetrahedron satisfying (2) where AI is not perpendicular"; no "tangent to each face at the face-incenter" universal; A's counterexamples mention "incenter", not "centroid"; A does not use "almost regular" or "slightly skewed"). Acceptable.
- **D**: claims `{a,b,c,d,e}`. No trigger phrase appears. Acceptable.
- **I**: claims `{a,b,c,d,e}`. No trigger phrase appears. Acceptable.

Response C claims the gold set but its text triggers `asserts_universal_face_incenter_tangency`, so C is excluded. Responses B, E, F, G, H have `final_answer_correct = false`.

---

## Per-response trigger evidence

### Response A
- Claimed set: `{a, b, c, d, e}` (line 263: `\boxed{\{a, b, c, d, e\}}`).
- `final_answer_correct`: true.
- `failure_reasons`: `[]`. No trigger phrase fires. (A discusses counterexamples but resolves them; its (a) discussion uses "incenter", not "centroid".)

### Response B
- Claimed set: `{b, c, d}` (line 109: `\boxed{\{c, d, b\}}`).
- `final_answer_correct`: false.
- `failure_reasons`: `["rejects_a_with_we_can_have_assertion"]`. Trigger fires on line 79: *"This is not necessarily true from our conditions. Counterexample: we can have a tetrahedron satisfying (2) where AI is not perpendicular to BCD."* — exact-form assertion-not-construction.

### Response C
- Claimed set: `{a, b, c, d, e}` (line 159: `\boxed{{a,b,c,d,e}}`).
- `final_answer_correct`: true.
- `failure_reasons`: `["asserts_universal_face_incenter_tangency"]`. Trigger fires on line 84: *"the insphere is tangent to each face at its face-incenter"* (in parenthetical asserting the universal). Reinforced on line 104: *"The insphere always touches a face at the incenter of that face, independently of any extra hypothesis."*

### Response D
- Claimed set: `{a, b, c, d, e}` (line 134: `\boxed{{a,,b,,c,,d,,e}}`; double commas are formatting artifacts).
- `final_answer_correct`: true.
- `failure_reasons`: `[]`. No trigger phrase fires.

### Response E
- Claimed set: `{c, d, e}` (line 210: *"the final answer is: {c,d,e}"*).
- `final_answer_correct`: false.
- `failure_reasons`: `["counterexample_places_a_above_centroid"]`. Trigger fires on line 55, inside the explicit counterexample to (a): *"A lies directly above the centroid of B[CD]"*.

### Response F
- Claimed set: `{d, e}` (line 301: *"In my final answer, I'll say {d, e}"*; line 277 confirms).
- `final_answer_correct`: false.
- `failure_reasons`: `["asserts_universal_face_incenter_tangency"]`. Trigger fires on line 205: *"For a tangential tetrahedron, the point of tangency on each face is the incenter of that face."*, reinforced on lines 331 and 371: *"the inscribed sphere is tangent to each face at a point equidistant from the edges of that face"* used as a universal.

### Response G
- Claimed set: `{d}` (per response final answer).
- `final_answer_correct`: false.
- `failure_reasons`: `["appeals_to_almost_regular_or_slightly_skewed"]`. Trigger fires on line 13: *"Counterexample: Consider a tetrahedron that is 'almost' regular, but slightly skewed."* — both "almost regular" AND "slightly skewed" literal phrases present, no concrete construction.

### Response H
- Claimed set: `{b, e}` (line 38: *"the set of statement labels that are necessarily true for every tetrahedron ABCD satisfying both hypotheses is {b, e}"*).
- `final_answer_correct`: false.
- `failure_reasons`: `["asserts_AI_equals_r"]`. Trigger fires on line 9: *"As I is also the center of the inscribed sphere of tetrahedron ABCD, AI = r."* — exact literal `AI = r` asserted as a load-bearing equality in H's (b) proof.

### Response I
- Claimed set: `{a, b, c, d, e}` (per response final answer).
- `final_answer_correct`: true.
- `failure_reasons`: `[]`. No trigger phrase fires.

---

## Schema compliance

- `gold_set` is lowercase a..h, alphabetically sorted.
- `acceptable_solution_ids` is uppercase A..I, alphabetically sorted.
- `per_response_assessment` contains exactly 9 entries, ordered A..I.
- Each entry has exactly the keys `response_id`, `final_answer_correct`, `failure_reasons`.
- All `failure_reasons` labels are drawn from the 5-code phrase-trigger vocabulary in `instruction.md`.
- `tests/oracle.json` and `solution/oracle.json` are byte-identical, activating the exact-match shortcut in `tests/judge.py` for the oracle agent run.
