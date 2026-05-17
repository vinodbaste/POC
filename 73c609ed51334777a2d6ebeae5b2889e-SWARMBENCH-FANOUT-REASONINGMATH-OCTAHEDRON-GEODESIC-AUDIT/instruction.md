# Task: Audit proposed solutions to a geometry shortest-path problem

Your working directory is `/workspace`.

You are given one geometry problem and seven proposed solutions. Your job is to solve the problem independently, then audit each proposed solution against the correct solution.

## Input files

- Problem statement: /input_artifacts/problem_statement.md
- Proposed solutions:
  - /input_artifacts/candidate_solutions/response_A.md
  - /input_artifacts/candidate_solutions/response_B.md
  - /input_artifacts/candidate_solutions/response_C.md
  - /input_artifacts/candidate_solutions/response_D.md
  - /input_artifacts/candidate_solutions/response_E.md
  - /input_artifacts/candidate_solutions/response_F.md
  - /input_artifacts/candidate_solutions/response_G.md

## Work to perform

1. Solve the original geometry problem yourself from first principles. Do not assume any proposed solution is correct.
2. Determine the ground-truth final answer in exact radical form.
3. Audit each proposed solution A-G.
4. For each proposed solution, decide whether its final answer is correct and identify the main error types.
5. Pay special attention to surface-net validity, regular-hexagon metric facts, algebraic correctness, and whether the solution proves global minimality rather than only producing one candidate path.

## Mathematical audit criteria

Use the following controlled categories.

final_answer_category: choose exactly one of:
- CORRECT
- THREE_FACE_LATERAL_STRIP
- BASE_EDGE_PATH
- FALSE_DIAMETER_HEIGHT_SHORTCUT
- OTHER

Boolean labels:
- gtfa_correct: true only if the proposed solution's final answer is mathematically equivalent to the ground-truth final answer.
- spatial_reasoning_error: true if the proposed solution uses an invalid surface unfolding, wrong geometric placement/orientation, wrong geodesic-validity test, or treats a non-surface shortcut as valid.
- non_spatial_reasoning_error: true if the proposed solution has a logical reasoning problem not primarily about spatial placement, such as an unsupported minimality claim, invalid elimination of cases, or internal contradiction.
- calculation_error: true if the proposed solution contains a material arithmetic, algebraic, or numerical comparison error. Do not mark this true for a merely wrong geometric model if the computations inside that wrong model are otherwise consistent.

Quality labels:
- completeness_level: one of thorough, adequate, thin
- efficiency_level: one of efficient, acceptable, inefficient
- latex_clarity_level: one of good, acceptable, poor

error_codes: use a list of zero or more of the following exact strings, sorted alphabetically:
- WRONG_FINAL_ANSWER
- THREE_FACE_LATERAL_STRIP_FALLACY
- BASE_EDGE_PATH_MINIMUM_FALLACY
- FALSE_DIAMETER_HEIGHT_SHORTCUT
- INVALID_UNFOLDING_OR_PATH_VALIDITY
- SPATIAL_COORDINATE_ERROR
- HEXAGON_METRIC_ERROR
- CALCULATION_OR_ALGEBRA_ERROR
- INSUFFICIENT_MINIMALITY_PROOF
- FALSE_COMPARISON_OF_ALTERNATE_NETS
- UNSUPPORTED_EXTERNAL_CITATIONS

Definitions:
- THREE_FACE_LATERAL_STRIP_FALLACY: the solution treats the straight line across three adjacent lateral rectangles as globally minimal without validating the relevant competing surface nets.
- BASE_EDGE_PATH_MINIMUM_FALLACY: the solution finds a valid broken path through a base and a vertical edge, but wrongly concludes that this broken path is globally minimal.
- FALSE_DIAMETER_HEIGHT_SHORTCUT: the solution uses the base opposite-vertex distance and prism height as if they were perpendicular legs of a valid surface path, without constructing a valid surface unfolding.
- INVALID_UNFOLDING_OR_PATH_VALIDITY: the solution's straight-line path in a claimed net is not a valid continuous path on the selected faces, or it wrongly rejects a valid net path.
- SPATIAL_COORDINATE_ERROR: the solution places hexagon vertices, unfolded faces, angles, or crossing edges incorrectly.
- HEXAGON_METRIC_ERROR: the solution states a wrong metric fact about the regular hexagon, such as a wrong distance between opposite vertices.
- CALCULATION_OR_ALGEBRA_ERROR: the solution has a material arithmetic, algebraic, simplification, or numerical comparison error.
- INSUFFICIENT_MINIMALITY_PROOF: the solution asserts minimality without adequately comparing or validating the key competing surface nets.
- FALSE_COMPARISON_OF_ALTERNATE_NETS: the solution compares candidate lengths incorrectly or falsely claims a relevant competing route is longer.
- UNSUPPORTED_EXTERNAL_CITATIONS: the solution relies on irrelevant or unsupported external links/citations rather than a self-contained geometric argument.

## Correct-solution audit expectations

Your independent solution should establish a valid shortest surface path, compute the exact distance, and justify why the common competing candidates are not minimal. Do not merely find one path; verify that the claimed path is globally minimal among the relevant unfoldings.

Important schema requirement: the `responses` object must contain exactly the keys `A`, `B`, `C`, `D`, `E`, `F`, and `G`.
## Output Instructions

Write your final answer to /logs/agent/output.json in this exact JSON format.
BEGIN_JSON_SCHEMA
{
  "derived_final_answer": "<exact radical expression>",
"responses": {
    "A": {
      "final_answer_category": "<one controlled category>",
      "gtfa_correct": <bool>,
      "spatial_reasoning_error": <bool>,
      "non_spatial_reasoning_error": <bool>,
      "calculation_error": <bool>,
      "completeness_level": "<thorough|adequate|thin>",
      "efficiency_level": "<efficient|acceptable|inefficient>",
      "latex_clarity_level": "<good|acceptable|poor>",
      "error_codes": ["<controlled error code>", "..."],
      "brief_justification": "<1-3 sentences>"
    },
    "B": {
      "final_answer_category": "<one controlled category>",
      "gtfa_correct": <bool>,
      "spatial_reasoning_error": <bool>,
      "non_spatial_reasoning_error": <bool>,
      "calculation_error": <bool>,
      "completeness_level": "<thorough|adequate|thin>",
      "efficiency_level": "<efficient|acceptable|inefficient>",
      "latex_clarity_level": "<good|acceptable|poor>",
      "error_codes": ["<controlled error code>", "..."],
      "brief_justification": "<1-3 sentences>"
    },
    "C": {
      "final_answer_category": "<one controlled category>",
      "gtfa_correct": <bool>,
      "spatial_reasoning_error": <bool>,
      "non_spatial_reasoning_error": <bool>,
      "calculation_error": <bool>,
      "completeness_level": "<thorough|adequate|thin>",
      "efficiency_level": "<efficient|acceptable|inefficient>",
      "latex_clarity_level": "<good|acceptable|poor>",
      "error_codes": ["<controlled error code>", "..."],
      "brief_justification": "<1-3 sentences>"
    },
    "D": {
      "final_answer_category": "<one controlled category>",
      "gtfa_correct": <bool>,
      "spatial_reasoning_error": <bool>,
      "non_spatial_reasoning_error": <bool>,
      "calculation_error": <bool>,
      "completeness_level": "<thorough|adequate|thin>",
      "efficiency_level": "<efficient|acceptable|inefficient>",
      "latex_clarity_level": "<good|acceptable|poor>",
      "error_codes": ["<controlled error code>", "..."],
      "brief_justification": "<1-3 sentences>"
    },
    "E": {
      "final_answer_category": "<one controlled category>",
      "gtfa_correct": <bool>,
      "spatial_reasoning_error": <bool>,
      "non_spatial_reasoning_error": <bool>,
      "calculation_error": <bool>,
      "completeness_level": "<thorough|adequate|thin>",
      "efficiency_level": "<efficient|acceptable|inefficient>",
      "latex_clarity_level": "<good|acceptable|poor>",
      "error_codes": ["<controlled error code>", "..."],
      "brief_justification": "<1-3 sentences>"
    },
    "F": {
      "final_answer_category": "<one controlled category>",
      "gtfa_correct": <bool>,
      "spatial_reasoning_error": <bool>,
      "non_spatial_reasoning_error": <bool>,
      "calculation_error": <bool>,
      "completeness_level": "<thorough|adequate|thin>",
      "efficiency_level": "<efficient|acceptable|inefficient>",
      "latex_clarity_level": "<good|acceptable|poor>",
      "error_codes": ["<controlled error code>", "..."],
      "brief_justification": "<1-3 sentences>"
    },
    "G": {
      "final_answer_category": "<one controlled category>",
      "gtfa_correct": <bool>,
      "spatial_reasoning_error": <bool>,
      "non_spatial_reasoning_error": <bool>,
      "calculation_error": <bool>,
      "completeness_level": "<thorough|adequate|thin>",
      "efficiency_level": "<efficient|acceptable|inefficient>",
      "latex_clarity_level": "<good|acceptable|poor>",
      "error_codes": ["<controlled error code>", "..."],
      "brief_justification": "<1-3 sentences>"
    }
  }
}
END_JSON_SCHEMA
