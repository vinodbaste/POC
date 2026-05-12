# Oracle Derivation — Olympiad Solution Auditor

Source: hand-curated solutions in the style of IMO / USAMO / IMOSL / BMOSL competition problems.

Task: For each of 20 published olympiad solutions, verify each numbered key claim, identify the central technique, and rate the solution's rigor.

Each per-artifact entry below explains:
- which claim received which status and why,
- which technique was selected as central and why,
- how the rigor score follows mechanically from the rubric's claim-count table.

---

## Per-Artifact Derivations

### artifact_01 — IMO_2009_1 (2009) — proof_by_contradiction, rigor 3

The proof opens "Suppose for contradiction" (Step 1) and builds toward a contradiction with distinctness, so `proof_by_contradiction` is the central frame. Claims C1, C2, C4, C6, C7 are each backed by explicit algebra/derivation within the solution → `verified`. C3 invokes "Bezout's lemma" to conclude a cyclic divisibility chain, but the chain g_1 | g_2 | ... | g_k | g_1 is asserted as the consequence rather than derived → `unjustified`. C5 inverts the constraint from n | a_i (a_{i+1} - 1) to (n/g) | a_{i+1} - 1 "using coprimality of m_i with n/g", which is plausible but not spelled out → `unjustified`. Result: 5v + 2u + 0i → rigor 3.

### artifact_02 — USAMO_2010_3 (2010) — inequality_application, rigor 4

The central move is AM-GM-style bounding of pairs, so the central technique is `inequality_application`. C1, C2, C3, C5, C6 each carry their own explicit algebra → `verified`. C4 says "direct computation confirms the inequality (left as exercise)" → `unjustified`. 5v + 1u + 0i → rigor 4.

### artifact_03 — IMOSL_2015_N4 (2015) — combinatorial_counting, rigor 3

Two pigeonhole applications drive the argument; `combinatorial_counting` covers the pigeonhole pattern. C1-C4 follow from elementary observations or pigeonhole, all derived → `verified`. C5 ("r ≠ 0 case yields pairs but via a different argument") is hand-waved → `unjustified`. C6 ("original claim follows from Steps 4 and 5") is asserted as obvious without combining the two cases properly → `unjustified`. C7 ("the proof handles m > n correctly") is asserted without verification → `unjustified`. 4v + 3u + 0i → rigor 3.

### artifact_04 — IMO_2014_4 (2014) — algebraic_manipulation, rigor 2

The argument is symbolic polynomial work, hence `algebraic_manipulation`. C1-C6 are each carefully checked algebraic claims → `verified`. C7 claims P(x) = (x + 1)^n + 1 satisfies the equation, but Step 4 of the proof itself explicitly demonstrates this fails — direct contradiction within the proof makes C7 `incorrect`. 6v + 0u + 1i → rigor 2.

### artifact_05 — IMOSL_2017_C3 (2017) — combinatorial_counting, rigor 2

The problem is a counting question, `combinatorial_counting`. C1, C2, C5, C6 are correct observations or follow from the problem reading → `verified`. C3 reinterprets the problem statement (claims "no two squares in the same row" is trivial within-row distinctness) which is `incorrect` — the standard reading is one-per-row. C4 ("with 25 squares we cannot avoid same-column across rows") is asserted without proof → `unjustified`. 4v + 1u + 1i → rigor 2.

### artifact_06 — USAMO_2016_5 (2016) — induction, rigor 5

The proof is by induction on n (Step 3 explicit inductive step), so `induction` is the central technique. All 7 claims are supported by elementary number theory (FLT, order-of-element argument). 7v + 0u + 0i → rigor 5.

### artifact_07 — BMOSL_2018_A1 (2018) — inequality_application, rigor 1

AM-GM is the named technique applied, so `inequality_application`. C1, C2, C3 are correctly derived steps. C4 claims AM-GM gives 3 (abc)^{1/9} = 3 but the correct exponent is 1/3 — `incorrect`. C5 chains the wrong direction of inequalities to "prove" the conclusion (≤ vs ≥ confusion) → `incorrect`. C6 concludes the inequality from broken Step 5 logic → `incorrect`. 3v + 0u + 3i → rigor 1.

### artifact_08 — IMO_2019_4 (2019) — modular_arithmetic, rigor 4

The 2-adic valuation argument is the central technique, so `modular_arithmetic`. C1-C6 are each carefully derived (factorizations, Legendre's formula, direct check). C7's "for n >= 4, no solution by size and 2-adic analysis" is gestured at but the size estimate is not spelled out → `unjustified`. 6v + 1u + 0i → rigor 4.

### artifact_09 — IMOSL_2018_G2 (2018) — geometric_construction, rigor 3

A parallel-line construction drives the proof, so `geometric_construction`. C1, C2, C4, C5 are standard geometric facts → `verified`. C3's invocation of Menelaus is asserted without verifying the triangle/transversal setup → `unjustified`. C6 "follows from a triangle-specific identity" is unverified → `unjustified`. C7's conclusion depends on C6 → `unjustified`. 4v + 3u + 0i → rigor 3.

### artifact_10 — USAMO_2013_5 (2013) — extremal_principle, rigor 4

The proof opens with "smallest counterexample"-style reasoning, hence `extremal_principle`. C1, C2, C3, C5, C6, C7 are well-supported. C4 ("applying the extremal principle to the smallest c yields a contradiction") is asserted but no ordering on c is exhibited → `unjustified`. 6v + 1u + 0i → rigor 4.

### artifact_11 — BMOSL_2019_C2 (2019) — invariant_or_monovariant, rigor 4

The weighted energy E strictly decreases (a monovariant), hence `invariant_or_monovariant`. C1, C2, C3, C4, C6, C7 are well-derived. C5 generalizes the origin-case computation to arbitrary (i, j) by symmetry without verifying the analogous decrease → `unjustified`. 6v + 1u + 0i → rigor 4.

### artifact_12 — BMOSL_2020_C5 (2020) — generating_function, rigor 3

The setup builds a partition generating function, so `generating_function`. C1, C2, C6, C7 are correct. C3 ("extracting coefficients yields a sum involving p and divisors") is gestured at without execution → `unjustified`. C4 ("two operations produce DISTINCT partitions") is asserted but the editor's note flags that the two operations CAN produce the same partition in edge cases — left unproven → `unjustified`. C5 inherits the issue → `unjustified`. 4v + 3u + 0i → rigor 3.

### artifact_13 — IMO_2008_3 (2008) — proof_by_contradiction, rigor 5

The classical irrationality proof, hence `proof_by_contradiction`. Every step is elementary and justified inline. 7v + 0u + 0i → rigor 5.

### artifact_14 — IMOSL_2011_A4 (2011) — inequality_application, rigor 5

Direct Jensen's inequality application, hence `inequality_application`. Every claim (convexity, Jensen, equality conditions) is checked. 6v + 0u + 0i → rigor 5.

### artifact_15 — USAMO_2012_1 (2012) — algebraic_manipulation, rigor 4

Despite the "induction" framing in Step 6, the actual argument is direct divisibility algebra, hence `algebraic_manipulation`. C1-C5, C7 are well-derived. C6 ("induction is invoked to extend the n = 1 base case") is decorative — the induction is not actually used → `unjustified`. 6v + 1u + 0i → rigor 4.

### artifact_16 — BMOSL_2017_N2 (2017) — modular_arithmetic, rigor 1

Number theory via Fermat's Little Theorem, hence `modular_arithmetic`. C1, C4 are correct. C2 ("only KNOWN Wieferich primes are 1093 and 3511") is treated as "all" — this is a famous open problem, so the claim is `incorrect`. C3 inherits the error — the non-Wieferich set is NOT just "odd primes minus 1093 and 3511" → `incorrect`. C5 (final answer) inherits → `incorrect`. 2v + 0u + 3i → rigor 1.

### artifact_17 — IMO_2007_2 (2007) — geometric_construction, rigor 3

An auxiliary perpendicular and circumcircle drive the proof, so `geometric_construction`. C1-C5 are well-supported (cyclic quadrilateral, equidistance → circumcircle, inscribed angles, parallelogram angles). C6's "by symmetry of the circumcircle of FGC at E, the angles ℓ makes with AB and AD must be equal" hides several non-trivial steps → `unjustified`. C7 inherits from C6 → `unjustified`. 5v + 2u + 0i → rigor 3.

### artifact_18 — BMOSL_2022_C4 (2022) — extremal_principle, rigor 5

The "player with maximum wins is a king" argument is a textbook extremal principle, so `extremal_principle`. Every claim is well-supported by the tournament structure. 6v + 0u + 0i → rigor 5.

### artifact_19 — USAMO_2015_2 (2015) — invariant_or_monovariant, rigor 3

The 180-degree rotation gives a rotation pairing (an invariant under rotation), so `invariant_or_monovariant`. C1-C4 are correct combinatorial facts about the pairing. C5 ("at most 1 self-paired domino can occupy the central region") is asserted without proof → `unjustified`. C6 (Step 7 construction "gives two congruent sets") is asserted but the case analysis from Step 5 onward is incomplete → `unjustified`. C7 ("the partition exists for any tiling") inherits → `unjustified`. 4v + 3u + 0i → rigor 3.

### artifact_20 — IMOSL_2013_A5 (2013) — generating_function, rigor 2

A formal power series setup, hence `generating_function`. C1, C2, C5, C6, C7 are correct. C4 ("upper bound n^{n · 2^n} / 2^{n · 2^n}") inherits an incorrect application of AM-GM — `incorrect` (the N used in AM-GM is wrong; see editor's note). C3 is technically correct as a step but the AM-GM in Step 4 uses N = 2^n where it should be N = n + 1 — the chain of reasoning has one bad step. We mark C3 as `incorrect` to reflect that the application's N value is wrong. 6v + 0u + 1i → rigor 2.

## Summary Table

| Artifact | Competition | Year | Technique                 | Rigor | Claims (v/u/i) |
|----------|-------------|------|---------------------------|------:|----------------|
| 01       | IMO         | 2009 | proof_by_contradiction    | 3     | 5 / 2 / 0      |
| 02       | USAMO       | 2010 | inequality_application    | 4     | 5 / 1 / 0      |
| 03       | IMOSL       | 2015 | combinatorial_counting    | 3     | 4 / 3 / 0      |
| 04       | IMO         | 2014 | algebraic_manipulation    | 2     | 6 / 0 / 1      |
| 05       | IMOSL       | 2017 | combinatorial_counting    | 2     | 4 / 1 / 1      |
| 06       | USAMO       | 2016 | induction                 | 5     | 7 / 0 / 0      |
| 07       | BMOSL       | 2018 | inequality_application    | 1     | 3 / 0 / 3      |
| 08       | IMO         | 2019 | modular_arithmetic        | 4     | 6 / 1 / 0      |
| 09       | IMOSL       | 2018 | geometric_construction    | 3     | 4 / 3 / 0      |
| 10       | USAMO       | 2013 | extremal_principle        | 4     | 6 / 1 / 0      |
| 11       | BMOSL       | 2019 | invariant_or_monovariant  | 4     | 6 / 1 / 0      |
| 12       | BMOSL       | 2020 | generating_function       | 3     | 4 / 3 / 0      |
| 13       | IMO         | 2008 | proof_by_contradiction    | 5     | 7 / 0 / 0      |
| 14       | IMOSL       | 2011 | inequality_application    | 5     | 6 / 0 / 0      |
| 15       | USAMO       | 2012 | algebraic_manipulation    | 4     | 6 / 1 / 0      |
| 16       | BMOSL       | 2017 | modular_arithmetic        | 1     | 2 / 0 / 3      |
| 17       | IMO         | 2007 | geometric_construction    | 3     | 5 / 2 / 0      |
| 18       | BMOSL       | 2022 | extremal_principle        | 5     | 6 / 0 / 0      |
| 19       | USAMO       | 2015 | invariant_or_monovariant  | 3     | 4 / 3 / 0      |
| 20       | IMOSL       | 2013 | generating_function       | 2     | 6 / 0 / 1      |
