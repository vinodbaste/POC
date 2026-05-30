# Oracle Justification

## Ground-truth gold set

For a tetrahedron $ABCD$ with an inscribed sphere whose dihedral angles are all acute AND whose four faces have equal area, the following statements are **necessarily true**:

$$\text{gold\_set} = \{a, b, c, d, h\}.$$

Each follows from the classical isosceles / equifacial tetrahedron theorem:

- **(a)** Opposite edges are equal ($AB = CD$, $AC = BD$, $AD = BC$).
- **(b)** The four faces are pairwise congruent triangles (SSS on three pair-lengths).
- **(c)** The four altitudes are equal in length ($V = \tfrac{1}{3} S_X h_X$ with all $S_X$ equal).
- **(d)** The centroid coincides with the circumcenter. The box-corner embedding $A,B,C,D = (\pm p, \pm q, \pm r)$ at alternating corners puts the centroid at the origin and every vertex at distance $\sqrt{p^2+q^2+r^2}$, so the origin is also the circumcenter.
- **(h)** The incenter coincides with the centroid. The area-weighted formula $I = \frac{\sum S_X V_X}{\sum S_X}$ collapses to $G$ when all $S_X$ are equal.

The remaining three statements are **NOT necessarily true**:

- **(e)** "Inscribed sphere is tangent to each face at the centroid of that face" — FALSE in general. In an isosceles tetrahedron the tangent point on each face is the **circumcenter** of that face, not the centroid.
- **(f)** "Triangle $ABC$ is equilateral" — FALSE in general. The box-corner equifacial tetrahedron with $(p,q,r) = (1.7, 1.95, 2.05)$ has all-acute dihedrals and four equal-area faces, but every face is scalene.
- **(g)** "$ABCD$ is regular" — FALSE in general, by the same counterexample.

## Per-response classifications (9 responses A-I)

Distribution of final claimed sets across the nine candidate proofs:

- **True gold $\{a,b,c,d,h\}$** — 2 responses: A, H.
- **Conservative-omit-d decoy $\{a,b,c,h\}$** — 5 responses: B, C, D, E, F (each one explicitly says it conservatively drops (d) for some plausible-sounding reason).
- **Wrong over-include-e $\{a,b,c,e,h\}$** — 2 responses: G, I (each one asserts the centroid-tangency claim).

| ID | Final set | `final_answer_correct` | `failure_reasons` | Notes |
|----|-----------|------------------------|-------------------|-------|
| A | $\{a,b,c,d,h\}$ | true  | `[]`     | Correct gold + box-embedding for (d); refutes (e) without F-trigger phrases |
| B | $\{a,b,c,h\}$   | false | `[]`     | Conservative-omit-d, no F-trigger phrases in text |
| C | $\{a,b,c,h\}$   | false | `[]`     | Conservative-omit-d, no F-trigger phrases in text |
| D | $\{a,b,c,h\}$   | false | `[F2]`   | Asserts "each face is equilateral" (F2) |
| E | $\{a,b,c,h\}$   | false | `[F3]`   | Asserts "orthocentric tetrahedron" / "altitudes are concurrent" (F3) |
| F | $\{a,b,c,h\}$   | false | `[F4]`   | Asserts "principal radii" + "nearly isosceles" + "small perturbation" reasoning (F4) |
| G | $\{a,b,c,e,h\}$ | false | `[F5]`   | Asserts tangent point is "centroid of that face" / "centroid of $BCD$" (F5) |
| H | $\{a,b,c,d,h\}$ | true  | `[]`     | Correct gold + box-embedding for (d), no F-trigger phrases |
| I | $\{a,b,c,e,h\}$ | false | `[F5]`   | Asserts tangent point is "centroid of $BCD$" (F5) |

**`acceptable_solution_ids`:** `["A", "H"]` — exactly the responses with `final_answer_correct = true` AND `failure_reasons = []`.

## Why the multi-agent decomposition outperforms a single agent

The dominant single-agent failure mode is **majority-vote bias on the gold set**. With 5 of 9 proofs converging on the conservative-omit-d decoy set $\{a,b,c,h\}$ and only 2 affirming the true gold, a single agent multiplexing all nine responses in one context window is heavily pulled toward the decoy:

1. The five decoy proofs each give a plausible-sounding reason for omitting (d) ("centroid–circumcenter coincidence needs an extra symmetry argument we cannot establish here", "the principal radii argument is heuristic", etc.). The conservative tone reads as intellectually honest, and the 5:2 vote majority looks like consensus.
2. If the single agent adopts gold $= \{a,b,c,h\}$, the per-response `final_answer_correct` decision is wrong for **every one of the nine responses** (A and H get marked false, B–F get marked true, G and I stay false but for the wrong reason). The 30-point all-or-nothing per-response scoring then zeroes the 7 mismatched responses, plus zeroes `gold_set` (25 pts) and `acceptable_solution_ids` (10 pts).

The fan-out-synthesize decomposition severs this dependency:

- `adjudicate-gold-set` reads ONLY `/input_artifacts/problem.md`. With no proposed-response context to bias it, this sub-agent derives the true gold $\{a,b,c,d,h\}$ directly from the equifacial-tetrahedron theorem and the box-embedding argument for (d).
- Each `audit-response-X` sub-agent reads exactly one response file plus the problem statement. Because it sees a single data point rather than a 9-vote distribution, it cannot be pulled by majority pressure on the gold set, and it can apply the F-code phrase-trigger vocabulary with full attention on the one response.
- `synthesize-final-audit` is purely structural: it uses the dedicated gold-set sub-agent's output for the `gold_set` field, copies each audit's `final_answer_correct` and `failure_reasons`, and computes `acceptable_solution_ids` as the alphabetically-sorted list of `response_id`s with `final_answer_correct = true` AND `failure_reasons = []`.

## Reward arithmetic (total = 305 pts)

- `gold_set`: 25 pts, all-or-nothing on exact set match against $\{a,b,c,d,h\}$.
- `acceptable_solution_ids`: 10 pts, all-or-nothing on exact set match against $\{A, H\}$.
- Per-response (9 × 30 pts = 270 pts): each response earns 30 pts iff `response_id`, `final_answer_correct`, AND `failure_reasons` (set-equal) all match the oracle. No partial credit.

Byte-identical output earns reward `1.0` via the exact-match fast-path; any other output is capped at `0.99` per the llm-judge cap rule.
