You are auditing raw AI-generated proposed solutions to an olympiad-level 3D geometry problem about a tetrahedron with an inscribed sphere.

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
2. Independently determine the gold SET of statement labels (a)..(h) that are necessarily true for every tetrahedron satisfying the two hypotheses.
3. Determine which proposed response(s), if any, are fully correct (claimed set equals the gold set AND no failure reason fires on their proof).
4. For each proposed response A through I, audit whether its claimed set matches the gold set and identify the exact set of failure reasons whose phrase trigger is concretely instantiated in that response.
5. Do not decide correctness by majority vote among the proposed responses. Independently solve the gold set first, then audit each response against that result.

Allowed failure reason codes (phrase-triggered; each code applies ONLY when its trigger phrase or its near-verbatim paraphrase is present in that single response's text):

- `F1` — REJECTS (a) with "different side lengths" assertion.
  - TRIGGER: the response REJECTS statement (a) — that is, the response's FINAL claimed set of necessarily-true statements does NOT contain "a" — AND the rejection is justified by a sentence asserting that "two triangles can have the same area while having very different side lengths" or a near-verbatim paraphrase, without producing a concrete construction. If the response includes (a) in its final claimed set, this trigger does NOT fire, even if a "different side lengths" sentence appears earlier in the response's reasoning.

- `F2` — asserts every face is equilateral as a consequence of hypotheses (1)+(2).
  - TRIGGER: the response asserts as an affirmative claim that hypotheses (1) and (2) together force each face of $ABCD$ to be equilateral. Look for the literal phrase "each face is equilateral" or "every face is equilateral" or a near-verbatim paraphrase used as a load-bearing claim. This claim is mathematically false in general because the isosceles (orthocentric equifacial) construction yields scalene congruent faces.

- `F3` — asserts the four altitudes are concurrent at the orthocenter.
  - TRIGGER: the response asserts as an affirmative claim that hypotheses (1) and (2) together force the four altitudes of $ABCD$ to be concurrent at a common orthocenter, identifying $ABCD$ as an orthocentric tetrahedron. Look for the literal phrase "orthocentric tetrahedron" or "altitudes are concurrent" or a near-verbatim paraphrase used as a load-bearing claim. This claim is mathematically false in general because orthocentricity is a strictly stronger condition than equifaciality.

- `F4` — asserts the circumcenter coincides with the centroid via "principal radii" reasoning.
  - TRIGGER: the response asserts as an affirmative claim that the circumcenter and centroid coincide, justified by reasoning about "principal radii" or "three different principal radii" in a "nearly isosceles" or "small perturbation" argument. Look for the literal phrase "principal radii" or "nearly isosceles" or "small perturbation" used as a load-bearing claim in the (d) discussion. The conclusion is correct but the reasoning is wrong.

- `F5` — asserts the inscribed-sphere tangent point on each face is the centroid of that face.
  - TRIGGER: the response asserts as an affirmative claim that the inscribed sphere is tangent to each face at the centroid of that face. Look for the literal phrase "centroid of that face" or "centroid of $BCD$" or "centroid of $F$" used as a load-bearing claim. This claim is mathematically false: in an isosceles tetrahedron the inscribed sphere is tangent to each face at the circumcenter / point-of-concurrency, NOT the centroid. The literal word "centroid" is NOT interchangeable with "incenter" or "circumcenter".

Important scoring and selection rules:
- The audit is evaluated as an EXACT set match per response. Extra failure reasons and missing failure reasons both score zero for that response.
- Most responses have 0 or 1 failure reasons. Apply a code only when its trigger phrase is directly observable in the response text.
- Use an empty list `[]` for `failure_reasons` exactly when the response's claimed set equals the gold set AND no failure-reason trigger phrase appears in that response.
- `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of `response_id` values whose `final_answer_correct` is `true` AND whose `failure_reasons` is the empty list.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`.
- `final_answer_correct`: `true` exactly when the response's claimed SET of necessarily-true statement labels equals the gold set (as a set; order irrelevant). Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes `F1`, `F2`, `F3`, `F4`, `F5`.

---

## Verification

The verifier (`/tests/judge.py`) reads your output JSON from `/logs/agent/output.json` and grades each field against the oracle held at `/tests/oracle.json`. Reward is `passed / total` clamped to `[0, 1]` and fail-closes to `0.0` on any internal error. Output that is byte-identical to the oracle earns reward `1.0`; any other output is capped at `0.99`. Per-field weights:

- `gold_set`: exact set match on the eight statement labels (**25 points**, all-or-nothing).
- `acceptable_solution_ids`: exact set match (**10 points**, all-or-nothing).
- For each response A through I (9 responses, **30 points per response**, **270 points total**):
  - The response earns 30 points if and only if `response_id`, `final_answer_correct`, and the exact `failure_reasons` set all match the oracle. Otherwise 0 points.
- **Total = 305 points.**

---

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```
{
  "gold_set": ["<lowercase letters a..h, alphabetical>"],
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

In the actual output, include nine objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, in that alphabetical order. Top-level keys MUST be exactly the three above with no extras. Do not write anything else to that file.
