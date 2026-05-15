# Oracle Justification

This document derives every value in `tests/oracle.json` and `solution/oracle.json`. It exists so that a QA reviewer can independently verify each oracle field against (1) the underlying mathematics, (2) the candidate solution text, and (3) the controlled vocabulary in `instruction.md`.

Citations are direct quotes from the raw candidate files in `environment/input_artifacts/`. The candidate files are byte-identical to what the candidate models produced — no hand-editing.

---

## Part A — Why the gold set is `{a, b, c, d, e}`

The candidates were given a modified CMO 2026 Problem 4 — multi-claim form. The two hypotheses are:

- **H1.** The dihedral angle between any two faces of `ABCD` is acute.
- **H2.** `vol(IABC)/BC = vol(IACD)/CD = vol(IADB)/DB`, where `I` is the incenter and `vol(IXYZ)` denotes the volume of the tetrahedron with vertices `I, X, Y, Z`.

Eight statements are listed (a)–(h). The gold set is the subset of statements that are necessarily true for **every** tetrahedron satisfying both hypotheses. We derive this directly from the official CMO 2026 P4 solution.

### Source

- Problem: [CMO 2026 P4](https://cms.math.ca/wp-content/uploads/2026/03/CMO2026-problems.pdf), p. 9.
- Solution: [CMO 2026 Solutions](https://cms.math.ca/wp-content/uploads/2026/04/CMO2026-solutions.pdf), Solution 1 and Solution 2 on pp. 9–10.

### Reduction of H2 (used by every gold proof)

Because the insphere is tangent to face `ABC` with distance `r` from `I` to that face, `vol(IABC) = (1/3) · area(ABC) · r`. Similarly for faces `ACD` and `ABD`. Dividing H2 by `(r/3)`:

```
area(ABC) / BC = area(ACD) / CD = area(ABD) / DB.    [Eq. R1]
```

Since `area(ABX) = (1/2) · BX · dist(A, line BX)`, dividing each ratio by `(1/2)·BX`:

```
dist(A, BC) = dist(A, CD) = dist(A, DB) =: h.        [Eq. R2]
```

R2 is the structural consequence of H2 used throughout the proof.

### Per-statement derivation

**(a) AI ⊥ plane BCD. TRUE.**
This is the CMO 2026 P4 conclusion. Solution 1 (CMO PDF, p. 9) proves: let `K = AI ∩ plane BCD`. The volume identity gives `area(KBC)/BC = area(KCD)/CD = area(KDB)/DB`, so `K` is equidistant from the three sides of triangle `BCD` and (because it is interior) `K` is the incenter of `BCD`. Independently, R2 says the foot `L` of the perpendicular from `A` to plane `BCD` is equidistant from those three sides. Acuteness (H1) forces `L` to be interior, hence `L` is also the incenter of `BCD`, so `L = K = AI ∩ plane BCD`, giving `AI ⊥ plane BCD`.

**(b) Projection of A onto plane BCD = incenter of triangle BCD. TRUE.**
Direct from R2 plus H1: the foot of perpendicular from `A` to plane `BCD` is equidistant from the three lines `BC, CD, DB`. In plane `BCD`, the unique interior point equidistant from the three sides is the incenter of triangle `BCD`. Acuteness rules out the excentric solutions (where the projection lies outside the triangle).

**(c) `dist(A, BC) = dist(A, CD) = dist(A, DB)`. TRUE.**
This is exactly R2 — an algebraic consequence of H2 alone (no acuteness needed).

**(d) `area(ABC) : area(ACD) : area(ABD) = BC : CD : DB`. TRUE.**
This is exactly R1, rearranged.

**(e) Insphere tangency point on face BCD = incenter of triangle BCD. TRUE.**
The insphere touches face `BCD` at the orthogonal projection of `I` onto plane `BCD`. By (a), `AI ⊥ plane BCD`, so `I`'s projection coincides with `A`'s projection, which by (b) is the incenter of `BCD`.

**(f) `AB = AC = AD`. FALSE in general.**
Counterexample: take any non-equilateral acute triangle `BCD`, place `A` above its incenter `Q` at small height. Then `AB² = h² + |QB|²`, `AC² = h² + |QC|²`, `AD² = h² + |QD|²`. The distances `|QB|, |QC|, |QD|` from the incenter to the vertices of a scalene triangle are unequal, so `AB, AC, AD` differ. CMO solution sketches this explicitly in Solution 2's remark.

**(g) Triangle ABC isosceles with AB = AC. FALSE in general.**
Weaker form of (f); same counterexample applies (any scalene `BCD` with `|QB| ≠ |QC|` gives `AB ≠ AC`).

**(h) Triangle BCD is equilateral. FALSE in general.**
Same counterexample: choose a non-equilateral acute `BCD`; the hypotheses can still be satisfied.

**Gold set:** `{a, b, c, d, e}`.

---

## Part B — Per-candidate audit rationale

Each candidate is audited against the gold set `{a, b, c, d, e}` and against the structural proof above. Citations below are verbatim from `environment/input_artifacts/response_X.md` unless otherwise stated.

### Candidate A — Sonnet 4.5

- **Claimed set in response:** `{a, b, c, d, e}`. Citation: final line `"$$\boxed{\{a, b, c, d, e\}}$$"`.
- **Verdict assigned:** `correct`.
- **Why correct:** The candidate derives R2 (cited: *"$$d(A, BC)^2 = d(P, BC)^2 + h^2$$ ... d(A,BC) = d(A,CD) = d(A,DB) ⟺ d(P,BC) = d(P,CD) = d(P,DB) ... Therefore P is the incenter of triangle BCD"*), establishes (b), then derives the tetrahedron-incenter formula `I = (Σ Sᵢ vᵢ) / (Σ Sᵢ)` and proves `π(I) = Q` via the equivalence `area(ACD)/|CD| = (1/2)·d(A,CD)`. Hence (a). All eight claims handled correctly. Mathematics is sound; length and coordinate detours are stylistic rather than substantive.
- **`first_fatal_error`:** `null` (verdict `correct`).
- **`failure_labels` and `domain_specific_labels`:** empty lists.
- **`repairability`:** `"n/a"`.
- **`brief_assessment`:** documents the mid-proof self-doubt about (a) and the recovery via the incenter formula.

### Candidate B — Claude Haiku

- **Claimed set in response:** `{b, c, d}`. Citation: final line `"$$\boxed{\{c, d, b\}}$$"` (set, order irrelevant).
- **Verdict assigned:** `incorrect` (claimed_set differs from gold by 2 letters: missing `a` and `e`).
- **`first_fatal_error.location`:** `"Analysis of statement (a) — the paragraph beginning 'For this to be true, we'd need A to lie on the line through I perpendicular to plane BCD.'"` Citation: *"For this to be true, we'd need A to lie on the line through I perpendicular to plane BCD. This follows only if the projection of A onto BCD is directly below/above I. This is not necessarily true from our conditions. Counterexample: we can have a tetrahedron satisfying (2) where AI is not perpendicular to BCD."*
- **`first_fatal_error.error_type`:** `underjustified_step`. The candidate asserts a counterexample (*"we can have a tetrahedron satisfying (2) where AI is not perpendicular to BCD"*) but constructs nothing. The argument cannot recover because the rejection of (a) cascades into the rejection of (e).
- **`failure_labels`:** `final_answer_error` (claimed set ≠ gold), `underjustified_step`, `incomplete_proof`, `missing_case`. All four follow from the unconstructed-counterexample pattern.
- **`domain_specific_labels`:** none — the candidate's error is structural (skipped a chain link), not a specific domain confusion.
- **`repairability`:** `minor_fix`. The candidate already proved (b) correctly; one additional paragraph deriving that I's projection equals A's projection (using the tetrahedron-incenter formula or the bisector-plane argument) would patch the proof.

### Candidate C — GPT-5.2

- **Claimed set in response:** `{a, b, c, d, e}`. Citation: final line `"$$\boxed{\{a,b,c,d,e\}}$$"`.
- **Verdict assigned:** `partially_correct` (claimed set matches gold, proof contains a false math claim).
- **`first_fatal_error.location`:** `"Step 3 — the assertion 'The incenter of triangle BCD is exactly the tangency point of the insphere with face BCD (since the insphere is tangent to each face at its face-incenter).'"` Citation: *"The incenter of triangle BCD is exactly the tangency point of the insphere with face BCD (since the insphere is tangent to each face at its face-incenter)."*
- **`first_fatal_error.error_type`:** `false_math_claim`. The parenthetical clause asserts a UNIVERSAL property of inspheres of tangential tetrahedra. This is mathematically false: in general, the insphere of a tangential tetrahedron is NOT tangent to each face at the face's incenter. (Counterexample: take any tangential tetrahedron without enough symmetry — e.g., one whose four faces have unequal areas; the touch point on a face is determined by the position of I, not by any 2D incenter property.) The claim happens to be true HERE because H2 forces the touch point to coincide with the incenter of BCD, but the candidate uses the false universal as a premise.
- **`failure_labels`:** `correct_gtfa_invalid_proof` (claimed set = gold, proof invalid), `false_math_claim`, `wrong_theorem_application`.
- **`repairability`:** `minor_fix`. Replace the false universal step with a direct derivation: `(b) + AI ⊥ BCD ⟹ touch point of insphere on BCD = projection of I = projection of A = incenter of BCD`. The rest of the proof remains intact.

### Candidate D — GPT-o3

- **Claimed set in response:** `{a, b, c, d, e}`. Citation: final line `"$$\boxed{\{a,,b,,c,,d,,e\}}$$"` (double commas are formatting artifacts; set content unambiguous).
- **Verdict assigned:** `correct`.
- **Why correct:** The candidate's proof of (a) follows CMO 2026 Solution 2 (CMO PDF, p. 10): `I` lies on the bisector plane of each dihedral angle at edges `AB, AC, AD`; those planes intersect plane `BCD` in the interior angle bisectors of triangle `BCD` at `B, C, D`; those bisectors meet at the incenter `H` of `BCD`; so `(A, I, H)` are collinear and `AI ⊥ BCD`. Citation: *"Because I is equidistant from the two planes ABC and ABD, it lies on the internal bisector of the dihedral angle along the edge AB. Analogous statements hold for edges AC and AD. The three bisector planes meet in the line AI; each of them also contains the corresponding interior bisector of the angle of triangle BCD at B,C,D respectively, and these three angle–bisectors meet at the in-centre (H)."* The argument is concise and matches an official CMO solution; the one underjustified step (bisector-plane-of-dihedral restricts to angle-bisector-in-BCD) is a well-known lemma.
- **`first_fatal_error`:** `null`.
- **`repairability`:** `"n/a"`.

### Candidate E — GPT-4o-mini

- **Claimed set in response:** `{c, d, e}`. Citation: final lines *"the final answer is: {c,d,e}"*.
- **Verdict assigned:** `incorrect` (missing `a` and `b` from gold).
- **`first_fatal_error.location`:** `"Analysis of statement (a) — the 'counterexample' sentence 'Consider a tetrahedron where A lies directly above the centroid of BCD but is not orthogonal.'"` Citation: *"Counterexample: Consider a tetrahedron where A lies directly above the centroid of BCD but is not orthogonal. The statement does not hold in all cases."*
- **`first_fatal_error.error_type`:** `invalid_logical_step`. The proposed counterexample is self-contradictory: a point that is *directly above the centroid* is by definition on the line perpendicular to plane `BCD` through the centroid, so the line from that point to its projection IS orthogonal. The candidate also conflates *centroid* with *incenter* — distinct points in any non-equilateral triangle.
- **`failure_labels`:** `final_answer_error`, `incomplete_proof`, `underjustified_step`, `false_math_claim`, `missing_case`.
- **`domain_specific_labels`:** `incenter_centroid_confusion` (citation: *"A lies directly above the centroid of BCD"* used as a substitute for the incenter), `missed_volume_to_distance_lemma` (the candidate never derives R2; the "proofs" of (c), (d), (e) reference unrelated concepts: *"symmetry about point A"* (c, no such symmetry), *"circumcircle properties dictated by the dihedral angles"* (d, no connection), *"by definition of the inradius"* (e, same false universal as C)).
- **`repairability`:** `major_rewrite`. No genuine engagement with H2 anywhere in the response.

### Candidate F — Grok 3 mini (with visible chain-of-thought)

- **Claimed set in response:** `{d, e}`. Citation: *"The set of statement labels that is necessarily true is {d, e}."*
- **Verdict assigned:** `incorrect` (missing `a, b, c`).
- **`first_fatal_error.location`:** `"Visible chain-of-thought, analysis of statement (c) — sentence 'In a regular tetrahedron, yes, the distances from A to the edges BC, CD, DB are equal due to symmetry. But in general, probably not.'"` Citation (from the visible thinking trace): *"For (c): The distances from A to each of the three lines BC, CD, and DB are equal. ... In a regular tetrahedron, yes, the distances from A to the edges BC, CD, DB are equal due to symmetry. But in general, probably not."*
- **`first_fatal_error.error_type`:** `false_math_claim`. The candidate has just derived `area(ABC)/BC = area(ACD)/CD = area(ABD)/DB` in the previous paragraph — this is literally equivalent to `dist(A, BC) = dist(A, CD) = dist(A, DB)` by the area formula `area(ABX) = (1/2)·BX·dist(A, line BX)`. The "probably not" assertion contradicts the candidate's own preceding derivation.
- **`failure_labels`:** `final_answer_error`, `false_math_claim`, `incomplete_proof`, `missing_case`.
- **`domain_specific_labels`:** `missed_volume_to_distance_lemma`. The candidate also uses the same false universal as C and E to "prove" (e), citing *"For a tangential tetrahedron, the point of tangency on each face is the incenter of that face"*.
- **`repairability`:** `major_rewrite`.

### Candidate G — Gemini 2.0 Flash

- **Claimed set in response:** `{d}`. Citation: *"The only statement that is necessarily true is (d)."*
- **Verdict assigned:** `incorrect` (missing `a, b, c, e`).
- **`first_fatal_error.location`:** `"Analysis of statement (a) — the 'counterexample' sentence 'Consider a tetrahedron that is almost regular, but slightly skewed. It is possible to satisfy the volume condition without AI being perpendicular to BCD.'"` Citation: *"Counterexample: Consider a tetrahedron that is 'almost' regular, but slightly skewed. It's possible to satisfy the volume condition without AI being perpendicular to BCD."*
- **`first_fatal_error.error_type`:** `underjustified_step`. The candidate asserts possibility without constructing. The same pattern repeats for (b), (c), and (e).
- **`failure_labels`:** `final_answer_error`, `incomplete_proof`, `underjustified_step`, `missing_case`, `false_math_claim`.
- **`domain_specific_labels`:** `missed_volume_to_distance_lemma`. Note: for (e) the candidate's *general* reasoning (*"The incenter of BCD is the intersection of the angle bisectors, which is not necessarily the foot of the perpendicular from I to BCD"*) is correct in isolation — but the candidate never checks whether the specific hypothesis H2 forces these two points to coincide here, which it does.
- **`repairability`:** `major_rewrite`.

---

## Part C — Cross-solution summary basis

### `common_failure_modes` (4 items, basis)

1. *"Four of the seven candidates (B, E, F, G) reject (a) by asserting an unconstructed counterexample..."* — direct count from the per-candidate fatal-error locations above. B, E, G all reject (a) without construction; F rejects (a), (b), and (c) in its thinking trace with similar hand-waviness.
2. *"Three candidates (C, E, F) invoke the FALSE general claim 'the insphere of a tetrahedron is tangent to each face at the face's incenter'..."* — C cites it directly in Step 3, E cites it in its (e) proof ("by definition of the inradius..."), F cites it explicitly ("For a tangential tetrahedron, the point of tangency on each face is the incenter of that face").
3. *"Three of seven (E, F, G) fail to translate the volume condition into the equivalent distance-from-A condition..."* — E never derives R2 (skips to vague "symmetry about A"); F's thinking trace derives R1 but explicitly stops short of R2; G derives R1 but doesn't extract R2.
4. *"No candidate explicitly invokes or uses the acute-dihedral-angle hypothesis..."* — Search-and-verify: none of the seven response files mention "acute" in their proofs of any specific claim. Candidate A's proof of (b) notes the acuteness in passing ("using the acute dihedral angle condition to ensure it's interior") but doesn't actually use it as a load-bearing step. Candidate D's bisector-plane argument also references acute dihedral angles for the bisector-plane uniqueness but does not isolate the excenter case explicitly.

### `solutions_with_correct_gtfa_but_invalid_proof: ["C"]`

Definition (from `instruction.md` schema): solutions whose claimed_set equals the gold AND whose proof has `contains_wrong_math_claim = true` OR `logical_chain_valid = false`. Only candidate C qualifies:

- C: claimed_set = `{a,b,c,d,e}` (= gold), `contains_wrong_math_claim = true` (the false universal). ✓
- A: claimed_set = gold but `contains_wrong_math_claim = false` and `logical_chain_valid = true`. Excluded.
- D: claimed_set = gold, no false claim, chain valid. Excluded.

### `solutions_with_valid_core_idea: ["A", "B", "C", "D"]`

Definition: solutions whose key lemmas align with the gold derivation for the claims they attempt. The structural test is whether the candidate derives R2 (the equal-distances-from-A consequence of H2). A, B, C, D all derive R2 explicitly (cited above). E, F, G do not.

### `best_solution_id: "D"`

Selection criterion: overall verdict + soundness + concision among the candidates with claimed_set equal to gold (A, C, D).

- A: correct verdict, sound, but meandering with mid-proof self-doubt — penalize concision.
- C: partially_correct (false universal in proof of (a) and (e)) — disqualified by soundness.
- D: correct verdict, sound, concise — matches CMO Solution 2 essentially verbatim. **Best.**

### `candidates_sharing_same_fatal_error_type: [["B", "G"], ["C", "F"]]`

Computed by bucketing each non-correct candidate's `first_fatal_error.error_type` (Part B, per-candidate):

- `underjustified_step`: B (unconstructed counterexample for (a)), G (unconstructed counterexample for (a)) → group `["B", "G"]`.
- `false_math_claim`: C (false insphere-touches-face-incenter universal), F (false insphere universal in (e)) → group `["C", "F"]`.
- `invalid_logical_step`: only E (self-contradictory "directly above the centroid but not orthogonal" counterexample) — singleton, **dropped** per the schema rule that groups must have size ≥ 2.

Note that B and G arrive at the unconstructed-counterexample pattern independently — B from Haiku's "we can have a tetrahedron satisfying (2) where AI is not perpendicular", G from Gemini Flash's "consider a tetrahedron that is 'almost' regular, but slightly skewed". Both names the same shape of error.

### `candidates_implicitly_using_same_false_lemma: [["C", "E", "F"]]`

Computed by identifying candidates whose proofs implicitly rely on the false universal claim *"the insphere of any tangential tetrahedron is tangent to each face at the face's incenter"*. From Part B:

- C: cites the claim explicitly in Step 3 (verbatim quote in Part B). Uses it to derive (a) and (e).
- E: writes *"By definition of the inradius, the point of tangency from I to BCD is by construction the incenter"* — same false claim, more bluntly stated, used to justify (e).
- F: writes *"For a tangential tetrahedron, the point of tangency on each face is the incenter of that face. Is that true? Yes, because the incenter is equidistant from the sides, and the sphere is tangent..."* — restates the same false universal in F's chain-of-thought trace.

A, B, D, G do not invoke this false claim (A derives the touch-point identity directly from the tetrahedron-incenter formula; B and G do not engage with (e) at all beyond rejecting it; D derives the touch-point property as a consequence of (a) via the dihedral-bisector argument). So the only group of size ≥ 2 is `["C", "E", "F"]`.

If your audit-EF mapper or audit-G mapper failed to detect the false-universal in F's chain-of-thought trace, the synthesizer should still be able to recover it from the per-candidate `failure_labels` containing `false_math_claim` AND the `brief_assessment` mentioning the insphere/face-incenter claim.

---

## Part D — Schema compliance of oracle.json

- Letter arrays: `claimed_set` lists are alphabetically sorted, lowercase a–h ✓.
- `solution_audits`: exactly 7 entries, ordered A, B, C, D, E, F, G alphabetically ✓.
- `first_fatal_error`: JSON `null` for solutions A and D (verdict `correct`); object with `location`, `error_type`, `explanation` for the other five ✓.
- `repairability`: `"n/a"` for A and D; one of `minor_fix | major_rewrite | impossible_from_current_solution` for the others ✓.
- `error_type` values are all drawn from the controlled `failure_labels` vocabulary in `instruction.md` ✓.
- `failure_labels` and `domain_specific_labels` values are drawn from the controlled vocabularies in `instruction.md` ✓.

The oracle is byte-identical between `tests/oracle.json` and `solution/oracle.json` (verified by `diff`), which is what activates the exact-match shortcut in `tests/judge.py` for the oracle agent run.
