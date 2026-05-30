# Task: hexagonal-prism shortest-surface-path derivation and proposed-solution audit

Your working directory is `/workspace`.

## Primary task: derivation, then audit

You are working on an olympiad-level 3D geometry problem about a right regular hexagonal prism. The problem statement is in `/input_artifacts/problem.md`. Seven raw AI-generated proposed solutions are provided in `/input_artifacts/proposed_solutions/`. Two things must happen:

1. Independently derive the **squared shortest surface distance** for the full problem (height $h = 2025$, hexagon side $a = 2025$) and express it as $d^2 = R + C\sqrt{3}$ where $R$ and $C$ are integers; report $(R, C)$.
2. Audit each of the seven proposed responses A–G: decide whether its final stated distance equals the true minimum and identify the exact set of failure-reason codes that fire on that single response's text.

Working directory: `/workspace`.

Input artifacts:

- Problem statement: `/input_artifacts/problem.md`
- Provenance note for the proposed AI-generated responses: `/input_artifacts/provenance.md`
- Proposed solution files:
  - `/input_artifacts/proposed_solutions/response_A.md`
  - `/input_artifacts/proposed_solutions/response_B.md`
  - `/input_artifacts/proposed_solutions/response_C.md`
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`
  - `/input_artifacts/proposed_solutions/response_G.md`

Task list:

1. Read the problem statement and all seven proposed solutions.
2. Independently derive the squared shortest surface distance $d^2$ for the full prism by comparing every relevant surface-unfolding family (in particular: three-face lateral strip; broken base + vertical-edge path; top hex base unfolded with one adjacent lateral rectangle; and any variants you can construct). Express $d^2$ in the form $R + C\sqrt{3}$ with $R, C$ integers and report `gold_distance_squared_decomposition` = `{"rational_part": R, "radical_coefficient_sqrt3": C}` for the full problem.
3. For each of the five named anchor parameter pairs below, compute the squared shortest surface distance independently for that smaller prism and report it in the same `{rational_part, radical_coefficient_sqrt3}` decomposition format.
4. Determine which proposed response(s), if any, are fully correct (their final stated distance equals the true minimum AND no failure-reason phrase trigger fires on their text).
5. For each proposed response A through G, audit whether its final stated distance equals the true minimum and identify the exact set of failure reasons whose phrase trigger is concretely instantiated in that response's text.

---

## Sanity-check anchor parameter pairs (oracle brute-force results held privately)

Before applying any single closed-form expression to the full input, your method MUST reproduce the squared shortest surface distance for every prism in the following list. Each anchor is a $(a, h)$ pair giving the hexagon side and prism height for a smaller prism with the same vertex labelling. Compute the squared distance from $A$ to $D'$ on that smaller prism by the same surface-unfolding analysis, and express it as $R + C\sqrt{3}$ with $R, C$ integers.

- `anchor_a1_h1` — hexagon side $a = 1$, prism height $h = 1$.
- `anchor_a1_h2` — hexagon side $a = 1$, prism height $h = 2$.
- `anchor_a2_h1` — hexagon side $a = 2$, prism height $h = 1$.
- `anchor_a2_h3` — hexagon side $a = 2$, prism height $h = 3$.
- `anchor_a3_h2` — hexagon side $a = 3$, prism height $h = 2$.

Report your independently-computed values in `small_case_anchor_results` in your output JSON. The verifier holds an oracle (computed by independent unfolding enumeration) and grades each anchor for exact equality on both `rational_part` and `radical_coefficient_sqrt3`. A single mismatched anchor disqualifies the method that produced it; the verifier will not award the full-prism gold-decomposition credit retroactively even if the method happens to land the right $(R, C)$ for $a = h = 2025$ by coincidence.

---

## Allowed failure-reason codes (exactly five; phrase-triggered)

Each code applies ONLY when its trigger phrase or a near-verbatim paraphrase is present in that single response's text. Most responses have 0, 1, or 2 failure reasons.

| Code | Trigger phrase (literal or near-verbatim paraphrase) | Trigger conditions |
|---|---|---|
| `F1` | "three lateral faces" / "three rectangles" / "lateral strip" / final answer `\sqrt{10}` or `2025\sqrt{10}` | Response's final stated distance is `2025\sqrt{10}` (numerically about 6402) AND the supporting derivation unfolds three consecutive lateral rectangles and reads off a straight-line diagonal of the resulting $3a \times h$ strip. If the response considers the three-face lateral strip only as one candidate but commits to a different final value, this code does NOT fire. |
| `F2` | "diameter and height" / "diameter of the hexagon" used as a right-triangle leg / final answer `\sqrt{5}` or `2025\sqrt{5}` | Response's final stated distance is `2025\sqrt{5}` (numerically about 4528) AND the supporting derivation treats the regular hexagon's opposite-vertex distance $2a = 4050$ and the prism height $h = 2025$ as perpendicular legs of a right triangle, without constructing a valid flat surface net in which the straight line crosses the relevant shared edges. |
| `F3` | "base-edge path" / "across the top base then down" / final answer `6075` or `3s` or `2a + h` | Response's final stated distance is `6075` (or equivalently `3a` or `2a + h` with $a = h = 2025$) AND the supporting derivation describes a broken two-segment path that first travels across one full hexagonal-base diameter (length $2a$) and then descends one vertical edge (length $h$). |
| `F4` | external URL / "youtube" / "slideshare" / Markdown-style citation like `[[1]]` / `[1]` pointing to an external resource | Response cites at least one external link or external numbered citation marker as evidence supporting any geometric claim (e.g. minimality, unfolding validity, value of a candidate path). The literal substring must be the URL fragment or a citation marker pointing outside the response itself; a citation to a previous step of the same response does NOT trigger this code. |
| `F5` | "side length × sqrt(3)" / `2 \cdot s \cdot \sqrt{3}` / "opposite vertices are 2 × side length × sqrt 3 apart" | Response asserts that the distance between opposite vertices on the same hexagonal base is $2 a \sqrt{3}$ (or $a \sqrt{3}$, or any other value involving $\sqrt{3}$). The correct value is $2a$. The literal phrase must appear as an affirmative claim about hexagon geometry (not as an example being refuted). |

---

## Audit rules

Apply rules R1 through R6 in order when classifying each response.

- **R1 — failure_reasons set (multi-select).** From the five allowed codes, include every code whose TRIGGER is concretely present in the response's text under the conditions in the table. Empty set iff R5 returns true.
- **R2 — co-fire orthogonality.** The five codes describe orthogonal failure modes. A single response may legitimately fire two of them when both triggers are independently present in the text (for example, a response that gives the lateral-strip answer AND cites a YouTube link would fire both `F1` and `F4`; a response that gives the diameter-and-height shortcut AND cites a slideshow would fire both `F2` and `F4`). No code is implied or excluded by another.
- **R3 — final-value extraction.** Extract each response's final stated distance by locating the LAST explicit `\boxed{...}` or "Final answer" statement in the response. If the response gives multiple "final" claims, use the LAST one (responses sometimes self-correct mid-text). Compare this numerical value to the true minimum that you derived in step 2.
- **R4 — phrase strictness.** Apply a code only when its trigger phrase is directly observable in the response text. "Diameter" is NOT interchangeable with "circumradius". A `\sqrt{10}` that appears inside an intermediate comparison but is rejected as larger than another candidate does NOT trigger `F1`; the FINAL boxed value must be the trigger. When in doubt, do NOT fire the code.
- **R5 — acceptability gate.** A response is acceptable iff (i) its final stated distance equals the true minimum AND (ii) no failure-reason trigger fires on its text. `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of `response_id` values whose `final_answer_correct` is `true` AND `failure_reasons` is the empty list.
- **R6 — independence from other responses.** When auditing a single response, do not infer any classification from another response. Each audit is self-contained on its own text.

---

## Label definitions for each proposed response

- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`.
- `final_answer_correct`: `true` exactly when the response's final stated distance is mathematically equal to the true minimum surface distance you derived in step 2. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the five allowed failure-reason codes `F1`, `F2`, `F3`, `F4`, `F5`.

---

## Verification

The verifier reads your output JSON from `/logs/agent/output.json` and grades each field against the oracle held at `/tests/oracle.json`. Scoring is per-field with all-or-nothing per-response audits:

- `gold_distance_squared_decomposition`: exact match on both `rational_part` and `radical_coefficient_sqrt3` (30 points).
- `small_case_anchor_results`: each of the five anchors is scored independently; exact match on both `rational_part` and `radical_coefficient_sqrt3` earns 6 points per anchor (30 points total).
- `acceptable_solution_ids`: exact set match (5 points).
- For each response A through G, the audit earns 25 points if and only if `response_id`, `final_answer_correct`, and the exact `failure_reasons` set all match the oracle for that response; otherwise 0 points for that response.
- Total = 240 points; reward = passed / 240.

---

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```
{
  "gold_distance_squared_decomposition": {
    "rational_part": <integer>,
    "radical_coefficient_sqrt3": <integer>
  },
  "small_case_anchor_results": {
    "anchor_a1_h1": {"rational_part": <integer>, "radical_coefficient_sqrt3": <integer>},
    "anchor_a1_h2": {"rational_part": <integer>, "radical_coefficient_sqrt3": <integer>},
    "anchor_a2_h1": {"rational_part": <integer>, "radical_coefficient_sqrt3": <integer>},
    "anchor_a2_h3": {"rational_part": <integer>, "radical_coefficient_sqrt3": <integer>},
    "anchor_a3_h2": {"rational_part": <integer>, "radical_coefficient_sqrt3": <integer>}
  },
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": <true or false>,
      "failure_reasons": ["<zero or more codes from {F1, F2, F3, F4, F5}>"]
    }
  ]
}
```

In the actual output, include seven objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, in that order. Do not write anything else to that file.
