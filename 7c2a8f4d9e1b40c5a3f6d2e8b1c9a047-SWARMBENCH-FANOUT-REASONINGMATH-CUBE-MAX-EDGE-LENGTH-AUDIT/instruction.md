# Task: Audit proposed solutions to a cube-and-plane geometry problem

Your working directory is `/workspace`.

You are given one olympiad-level geometry problem and nine real, unedited model responses (from the public `RUC-AIBOX/OlymMATH-eval` benchmark). Your job is to solve the problem independently, then audit each proposed solution against the correct solution.

## Input files

- Problem statement: /input_artifacts/problem_statement.md
- Provenance note for the released responses: /input_artifacts/provenance.md
- Released model responses:
  - /input_artifacts/candidate_solutions/response_A.md
  - /input_artifacts/candidate_solutions/response_B.md
  - /input_artifacts/candidate_solutions/response_C.md
  - /input_artifacts/candidate_solutions/response_D.md
  - /input_artifacts/candidate_solutions/response_E.md
  - /input_artifacts/candidate_solutions/response_F.md
  - /input_artifacts/candidate_solutions/response_G.md
  - /input_artifacts/candidate_solutions/response_H.md
  - /input_artifacts/candidate_solutions/response_I.md

## Work to perform

1. Solve the cube-and-plane geometry problem yourself from first principles. Do not assume any proposed solution is correct.
2. Determine the ground-truth final answer (the LARGEST possible value of s² over the set S of possible cube edge lengths) as an exact integer.
3. Audit each proposed solution A-I.
4. For each proposed solution, decide whether its final numeric answer is correct (equals the gold maximum s²) and identify the main error types.
5. Pay special attention to whether the response enumerates the cube's sign-pattern configurations relative to the plane, whether it considers configurations in which the plane passes through the cube's interior (vertices on both sides), and whether the response's geometric setup forces all eight vertices to the same side. A response that finds only ONE valid s² value cannot defensibly claim to know the maximum unless it also rules out other orientations.

## Mathematical audit criteria

Use the following controlled categories.

`final_answer_category`: choose exactly one of:
- `CORRECT`
- `SINGLE_ORIENTATION_S2_EQUALS_21`
- `SPACE_DIAGONAL_FALLACY`
- `FACE_PARALLEL_FALLACY`
- `FABRICATED_INVARIANT_SUM`
- `NUMERIC_WITHOUT_DERIVATION`
- `NO_FINAL_ANSWER`

Boolean labels:
- `gtfa_correct`: true only if the proposed solution's final numeric answer is mathematically equivalent to the ground-truth final answer.
- `spatial_reasoning_error`: true if the proposed solution uses a flawed geometric setup, fixes the cube/plane configuration to an invalid special case, or fails to consider configurations in which the plane crosses the cube's interior.
- `non_spatial_reasoning_error`: true if the proposed solution has a logical reasoning problem not primarily about geometric setup, such as an unsupported uniqueness claim, internal contradiction, invented algebraic identity, or rejection of a correctly derived intermediate without justification.
- `calculation_error`: true if the proposed solution contains a material arithmetic, algebraic, or numerical-comparison error within its own setup. Do not mark this true for a merely wrong geometric model if the computations inside that wrong model are otherwise consistent.

Quality labels:
- `completeness_level`: one of `thorough`, `adequate`, `thin`
- `efficiency_level`: one of `efficient`, `acceptable`, `inefficient`
- `latex_clarity_level`: one of `good`, `acceptable`, `poor`

`error_codes`: use a list of zero or more of the following exact strings, sorted alphabetically:
- `WRONG_FINAL_ANSWER`
- `SINGLE_ORIENTATION_FALLACY`
- `SPACE_DIAGONAL_FALLACY`
- `FACE_PARALLEL_FALLACY`
- `DIRECT_MAX_EQUALS_EDGE_FALLACY`
- `FABRICATED_INVARIANT_ERROR`
- `AXIS_CORNER_VERTEX_TRAP`
- `NONNEGATIVE_SUBSET_SUMS_RESTRICTION`
- `SIGN_PATTERN_OMISSION`
- `INTERNAL_CONTRADICTION`
- `REPORTS_NON_MAXIMUM_VALID_S2`
- `NO_BOXED_ANSWER_OR_TRUNCATED`

Definitions:
- `WRONG_FINAL_ANSWER`: the response's final numeric answer does not match the gold maximum s² value.
- `SINGLE_ORIENTATION_FALLACY`: the response derives an `s²` value from a single cube orientation (e.g., the all-positive case or a single body-diagonal-aligned configuration) and asserts that value is the answer to the maximum-s² question without enumerating other orientations.
- `SPACE_DIAGONAL_FALLACY`: the response equates the maximum vertex-to-plane distance (7) with the cube's space diagonal a√3, yielding a = 7/√3 and s² = 49/3, then reports 49/3 as the answer.
- `FACE_PARALLEL_FALLACY`: the response's primary geometric setup assumes the cutting plane is parallel to one face of an axis-aligned cube, so the eight vertex distances take at most two distinct values.
- `DIRECT_MAX_EQUALS_EDGE_FALLACY`: the response identifies the maximum vertex-to-plane distance (7) directly with the cube's edge length, concluding a = 7 and s² = 49.
- `FABRICATED_INVARIANT_ERROR`: the response's final numeric answer rests on an invented algebraic identity that does not follow from the problem (e.g., a "sum of squared distances = 3a²(1+T²)" identity, or a Vieta sum over a quadratic whose coefficients come from a fabricated invariant).
- `AXIS_CORNER_VERTEX_TRAP`: the response fixes the vertex at distance 0 to be a specific cube-local corner (typically (0,0,0) of an axis-aligned cube) and writes the other seven vertices' distances as non-negative coordinate combinations of three outgoing edge directions, without justifying why the zero-vertex must be that specific corner.
- `NONNEGATIVE_SUBSET_SUMS_RESTRICTION`: the response's load-bearing argument requires all seven non-zero vertex distances to arise as non-negative sums of three positive "axis projections" or subset sums of {p, q, r}, excluding configurations with vertices on opposite sides of the plane.
- `SIGN_PATTERN_OMISSION`: the response reaches a numeric conclusion without enumerating the sign-pattern families of the cube's vertex configurations (i.e., it never considers configurations in which the plane passes through the cube's interior).
- `INTERNAL_CONTRADICTION`: the response openly accepts mutually contradictory equations such as "6 = 7" or "3 = 4" inside its derivation and proceeds to a numeric answer that the surviving algebra does not justify.
- `REPORTS_NON_MAXIMUM_VALID_S2`: the response correctly derives a valid s² value consistent with the eight given distances (e.g., s² = 21 from the all-positive case) and reports it as the final answer without realizing it is not the maximum s² over all valid orientations.
- `NO_BOXED_ANSWER_OR_TRUNCATED`: the response does not produce an identifiable final numeric answer (no boxed value, repetition loop, mid-sentence cutoff).

## Correct-solution audit expectations

Your independent solution should enumerate the cube's geometric configurations relative to the plane — including the configurations in which the plane crosses the cube's interior — derive every valid value of s² consistent with the eight distances {0,1,2,3,4,5,6,7}, and sum their squared edge lengths into one integer. Do not merely solve one orientation; verify that no other inequivalent orientation contributes additional s² values.

Important schema requirement: the `responses` object must contain exactly the keys `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, and `I`.

## Output Instructions

Write your final answer to /logs/agent/output.json in this exact JSON format.
BEGIN_JSON_SCHEMA
{
  "derived_final_answer": "<gold final numeric answer as a string>",
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
    },
    "H": {
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
    "I": {
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
