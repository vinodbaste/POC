You are deriving the shortest-surface-path distance for a regular hexagonal prism AND auditing nine raw AI-generated proposed solutions to that problem.

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
  - `/input_artifacts/proposed_solutions/response_H.md`
  - `/input_artifacts/proposed_solutions/response_I.md`

Task:
1. Read the problem statement and all nine proposed solutions.
2. Independently derive the squared shortest surface distance $d^2$ for the full prism by comparing every relevant surface-unfolding family. Express $d^2$ in the form $R + C\sqrt{3}$ with $R \ge 0, C \ge 0$ integers and report `gold_distance_squared_decomposition` = `{"rational_part": R, "radical_coefficient_sqrt3": C}`.
3. For each of the five named anchor parameter pairs below, compute the squared shortest surface distance independently for that smaller prism and report it in the same `{rational_part, radical_coefficient_sqrt3}` decomposition format inside `small_case_anchor_results`.
4. Determine which proposed response(s), if any, are fully correct (final stated distance equals the true minimum AND no failure-reason trigger fires on their text).
5. For each proposed response A through I, audit whether its final stated distance equals the true minimum (`final_answer_correct`) and identify the exact set of failure reasons whose phrase trigger is concretely instantiated in that response (`failure_reasons`).
6. Do not decide correctness by majority vote among the proposed responses. Independently derive the gold answer first, then audit each response against that result.

Sanity-check anchor parameter pairs (oracle brute-force results held privately). Each anchor is a $(a, h)$ pair giving the hexagon side and prism height for a smaller prism with the same vertex labelling. Compute the squared shortest surface distance from $A$ to $D'$ on that smaller prism and express it as $R + C\sqrt{3}$ with $R \ge 0, C \ge 0$ integers:

- `anchor_a1_h1` — hexagon side $a = 1$, prism height $h = 1$.
- `anchor_a1_h2` — hexagon side $a = 1$, prism height $h = 2$.
- `anchor_a2_h1` — hexagon side $a = 2$, prism height $h = 1$.
- `anchor_a2_h3` — hexagon side $a = 2$, prism height $h = 3$.
- `anchor_a3_h2` — hexagon side $a = 3$, prism height $h = 2$.

Allowed failure reason codes (phrase-triggered; each code applies ONLY when its trigger phrase or its near-verbatim paraphrase is present in that single response's text):

- `F1`
  - TRIGGER: response's final stated distance is `2025*sqrt(10)` (numerically about 6402) AND the supporting derivation unfolds three consecutive lateral rectangles and reads off a straight-line diagonal of a $3a \times a$ strip. Look for the literal phrases "three lateral", "three consecutive lateral", "lateral strip", or "a*sqrt(10)". If the response's final stated value is anything else, this trigger does NOT fire.

- `F2`
  - TRIGGER: response's final stated distance is `2025*sqrt(5)` (numerically about 4528) AND the supporting derivation treats the diameter of the hexagon ($2a = 4050$) and the prism height ($h = 2025$) as the two perpendicular legs of a right triangle. Look for the literal phrase "diameter of the hexagon", "diameter and height", or "right triangle" in combination with `2025*sqrt(5)`. If the response's final stated value is anything else, this trigger does NOT fire.

- `F3`
  - TRIGGER: response's final stated distance is `6075` (equivalently `2a + h` with $a = h = 2025$) AND the supporting derivation describes a broken two-segment path that first traverses one full hexagonal-base diameter (length $2a$) and then descends one vertical edge (length $h$). Look for the literal phrases "across the top base", "base-edge path", or "2a + h". If the response's final stated value is anything else, this trigger does NOT fire.

- `F4`
  - TRIGGER: response cites at least one external URL or external numbered citation marker as evidence supporting any geometric claim. Look for the literal substrings "youtube", "slideshare", "[[1]]", or "[[2]]" pointing outside the response itself. A citation to a previous step of the same response does NOT trigger this code.

- `F5`
  - TRIGGER: response asserts as an affirmative load-bearing claim that the distance between opposite vertices on the same hexagonal base is $2a\sqrt{3}$ (or equivalently `2 * side length * sqrt 3`). The correct value is $2a$. Look for the literal phrases "2a*sqrt(3)", "2 a * sqrt(3)", "2 a sqrt 3", "opposite vertices are 2 × side length × sqrt 3", or "diametrically opposite vertices ... 2a*sqrt(3)" used as an affirmative geometric statement (not inside a passage being refuted).

Important scoring and selection rules:
- The audit is evaluated as an EXACT set match per response: `final_answer_correct` must match the oracle boolean AND `failure_reasons` must equal the oracle set (order-independent, no duplicates). Any deviation on either field scores zero for that response.
- Most responses have 0, 1, or 2 failure reasons. Apply a code only when its trigger phrase is directly observable in the response text.
- Use an empty list `[]` for `failure_reasons` exactly when the response's final stated distance equals the true minimum AND no failure-reason trigger phrase appears in that response.
- `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of `response_id` values whose `final_answer_correct` is `true` AND whose `failure_reasons` is the empty list.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `final_answer_correct`: `true` exactly when the response's final stated distance is mathematically equal to the true minimum surface distance you derived in step 2. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes `F1`, `F2`, `F3`, `F4`, `F5`.

---
## Verification

The verifier (`/tests/judge.py`) reads your output JSON from `/logs/agent/output.json` and grades each field against the oracle held at `/tests/oracle.json`. Reward is `passed / total` clamped to `[0, 1]` and fail-closes to `0.0` on any internal error. Output that is byte-identical to the oracle earns reward `1.0`; any other output is capped at `0.99`. Per-field weights:

- `gold_distance_squared_decomposition`: exact match on both `rational_part` and `radical_coefficient_sqrt3` (**100 points**, all-or-nothing).
- `small_case_anchor_results`: each of the five anchors is scored independently; exact match on both `rational_part` and `radical_coefficient_sqrt3` earns 6 points per anchor (**30 points total**).
- `acceptable_solution_ids`: exact set match (**10 points**, all-or-nothing).
- For each response A through I (9 responses, **30 points per response**, **270 points total**):
  - The response earns 30 points if and only if `response_id`, `final_answer_correct`, and the exact `failure_reasons` set all match the oracle. Otherwise 0 points.
- **Total = 410 points.**

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```
{
  "gold_distance_squared_decomposition": {
    "rational_part": <non-negative integer>,
    "radical_coefficient_sqrt3": <non-negative integer>
  },
  "small_case_anchor_results": {
    "anchor_a1_h1": {"rational_part": <non-negative integer>, "radical_coefficient_sqrt3": <non-negative integer>},
    "anchor_a1_h2": {"rational_part": <non-negative integer>, "radical_coefficient_sqrt3": <non-negative integer>},
    "anchor_a2_h1": {"rational_part": <non-negative integer>, "radical_coefficient_sqrt3": <non-negative integer>},
    "anchor_a2_h3": {"rational_part": <non-negative integer>, "radical_coefficient_sqrt3": <non-negative integer>},
    "anchor_a3_h2": {"rational_part": <non-negative integer>, "radical_coefficient_sqrt3": <non-negative integer>}
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

In the actual output, include nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that order. Top-level keys MUST be exactly the four above with no extras. Do not write anything else to that file.
