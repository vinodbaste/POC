# Tetrahedron Incenter — Candidate Solution Audit

You are auditing model-produced solutions to a hard olympiad-level 3D geometry problem. Multiple language models were each asked the same question and produced their own written solutions. Your job is to read every candidate solution, judge whether it is correct, identify the first fatal mathematical error in each incorrect solution, and produce a structured cross-solution audit report.

You are NOT being asked to solve the problem from scratch. You are being asked to **audit** the candidate solutions against the mathematical truth.

## Working environment

- Working directory: `/workspace`
- Candidate solutions: `/input_artifacts/response_A.md`, `/input_artifacts/response_B.md`, ..., one file per candidate. The number of candidates `N` and the set of solution IDs (single uppercase letters: A, B, C, ...) are determined by what is present in `/input_artifacts/`.
- Provenance metadata for each candidate (model name, version, sampling settings) is in `/input_artifacts/provenance.json` for reference only — do not use it to bias your audit.
- Write your final answer to `/logs/agent/output.json` and nothing else to that path.

You may read any file in `/input_artifacts/`. Do not modify them.

## The problem each candidate solved

The candidate models were each given the following problem verbatim. The problem is the audit target — your gold reasoning must be grounded in it.

> **Problem.** Let $ABCD$ be a tetrahedron with an inscribed sphere of center $I$ and inradius $r > 0$. Suppose that
>
> 1. the dihedral angle between any two faces of $ABCD$ is acute, and
> 2. $\dfrac{\mathrm{vol}(IABC)}{BC} \;=\; \dfrac{\mathrm{vol}(IACD)}{CD} \;=\; \dfrac{\mathrm{vol}(IADB)}{DB}.$
>
> (Here $\mathrm{vol}(IXYZ)$ denotes the volume of the tetrahedron with vertices $I, X, Y, Z$.)
>
> For each of the following eight statements, decide whether the statement is **necessarily true for every** tetrahedron $ABCD$ satisfying both hypotheses.
>
> (a) $AI$ is perpendicular to the plane $BCD$.
> (b) The orthogonal projection of $A$ onto the plane $BCD$ coincides with the incenter of triangle $BCD$.
> (c) The distances from $A$ to each of the three lines $BC$, $CD$, and $DB$ are equal.
> (d) The areas of the triangles $ABC$, $ACD$, $ADB$ are in the ratio $BC : CD : DB$.
> (e) The point at which the inscribed sphere touches the face $BCD$ is the incenter of triangle $BCD$.
> (f) $AB = AC = AD$.
> (g) Triangle $ABC$ is isosceles with $AB = AC$.
> (h) Triangle $BCD$ is equilateral.
>
> State the **set of statement labels** that are necessarily true. For example, an answer of "$\{a, c, e\}$" means exactly $(a), (c), (e)$ are necessarily true and the others are not.

## What you must do

For each candidate solution in `/input_artifacts/`:

1. Identify the **claimed set of true statements** the candidate's solution actually asserts (parse the claim from the prose; some candidates will be ambiguous — record your best reading).
2. Determine whether the candidate's claimed set equals the correct gold set.
3. Independently audit the candidate's mathematical argument for each claim it considered. Note where the argument is invalid, where a theorem is misapplied, where a case is missing, where a step is asserted without justification, and where the candidate confuses related concepts (e.g. incenter vs. circumcenter, projection vs. perpendicular foot).
4. Identify the **first fatal mathematical error** in the solution — the earliest step at which the candidate's reasoning becomes irrecoverable. If the solution is fully correct, set the first fatal error to null.
5. Assign **failure labels** from the allowed vocabulary listed below.
6. Assess **repairability**: could the solution be patched with a minor fix, would it need a major rewrite, or is the entire approach unsalvageable?

Then produce a single cross-solution summary describing common failure modes, listing candidates with correct final answers but invalid proofs, listing candidates whose core idea is on the right track, and naming the single best candidate solution.

## Output format

Write your final answer to `/logs/agent/output.json` in this exact JSON structure. Every key must be present. Field names, types, and allowed values must match exactly.

```json
{
  "problem_id": "cmo2026-p4-claims-audit",
  "gold_final_answer": "<string — the gold set in canonical form, e.g. \"{a, b, c, d, e}\">",
  "solution_audits": [
    {
      "solution_id": "<string — single uppercase letter matching the response file>",
      "claimed_set": ["<letter>", "..."],
      "verdict": "<one of: correct | partially_correct | incorrect>",
      "final_answer_correct": <bool>,
      "logical_chain_valid": <bool>,
      "proof_complete": <bool>,
      "contains_wrong_math_claim": <bool>,
      "first_fatal_error": {
        "location": "<string — short description of where the error appears, e.g. \"step claiming A projects to circumcenter\">",
        "error_type": "<string — one of the allowed failure labels>",
        "explanation": "<string — 1–3 sentences describing the mathematical reason the step is wrong>"
      },
      "failure_labels": ["<string>", "..."],
      "domain_specific_labels": ["<string>", "..."],
      "repairability": "<one of: minor_fix | major_rewrite | impossible_from_current_solution | n/a>",
      "brief_assessment": "<string — 1–3 sentences summarizing the solution's quality>"
    }
  ],
  "cross_solution_summary": {
    "common_failure_modes": ["<string>", "..."],
    "solutions_with_correct_gtfa_but_invalid_proof": ["<solution_id>", "..."],
    "solutions_with_valid_core_idea": ["<solution_id>", "..."],
    "best_solution_id": "<string — the single best candidate, or \"none\" if no candidate is correct>"
  }
}
```

### Rules for the output

- `solution_audits` must contain exactly one entry per response file present in `/input_artifacts/`. Order entries by `solution_id` alphabetically.
- `claimed_set` is the set of letters the candidate asserted as necessarily true. If the candidate did not give a clear claimed set, record your best reading and add `"unclear_claimed_set"` to `failure_labels`.
- `verdict = "correct"` requires `claimed_set` exactly equals the gold set AND the proof is logically valid AND complete. `verdict = "partially_correct"` covers cases where the claimed set matches the gold but the reasoning is incomplete or invalid (correct-final-answer-but-invalid-proof), OR cases where the claimed set is close (differs by one) and the reasoning is on the right track. Everything else is `"incorrect"`.
- `final_answer_correct = true` iff `claimed_set` equals the gold set (regardless of proof quality).
- `first_fatal_error` must be `null` (literally, JSON null) when `verdict = "correct"`. Otherwise it must be a populated object.
- `repairability = "n/a"` when `verdict = "correct"`.
- Letters in any letter array must be lowercase single characters from `["a", "b", "c", "d", "e", "f", "g", "h"]`. Order each letter array alphabetically.

### Allowed `failure_labels` vocabulary

Use only these strings. You may attach more than one to a single solution.

- `final_answer_error` — the claimed set differs from the gold set.
- `correct_gtfa_invalid_proof` — the claimed set matches gold but the argument does not establish it.
- `invalid_logical_step` — a specific inference does not follow from previous statements.
- `wrong_theorem_application` — a theorem is invoked outside its hypotheses or in the wrong form.
- `false_math_claim` — a mathematical statement asserted by the candidate is mathematically false.
- `missing_case` — the candidate omits a required configuration or boundary case.
- `incomplete_proof` — the argument has a plausible outline but lacks necessary justification.
- `underjustified_step` — a step may be true but is asserted without sufficient argument for the problem level.
- `circular_reasoning` — the argument assumes a claim equivalent to what it is trying to prove.
- `extraneous_solution` — the candidate introduces a value or configuration that does not satisfy the original constraints.
- `notation_definition_error` — variables, definitions, or notation are misused in a way that affects correctness.
- `unclear_claimed_set` — the candidate did not unambiguously state which statements are necessarily true.

### Allowed `domain_specific_labels` vocabulary

Use only these strings.

- `incenter_circumcenter_confusion` — confuses the incenter with the circumcenter (of triangle BCD, of the tetrahedron, or otherwise).
- `incenter_centroid_confusion` — confuses the incenter with the centroid.
- `wrong_projection_claim` — names the wrong point as the orthogonal projection of A onto plane BCD.
- `ignored_acuteness_condition` — does not use the acute-dihedral-angle hypothesis where the gold proof needs it, or claims the hypothesis is unnecessary without justification.
- `over_symmetrization` — concludes regularity (BCD equilateral, $AB=AC=AD$, or similar) from the hypotheses without justification.
- `missed_volume_to_distance_lemma` — fails to translate $\mathrm{vol}(IABC)/BC = \cdots$ into the equal-distances-from-A condition that the gold proof depends on.
- `excenter_vs_incenter_gap` — applies "equidistant from three lines = incenter" without noting that the equidistant point could be an excenter when the projection is outside triangle BCD.
- `degenerate_or_unphysical_configuration` — works in a configuration that contradicts the inscribed-sphere or acuteness hypothesis.

## What NOT to do

- Do not solve the problem from scratch and ignore the candidate solutions — your job is to audit.
- Do not introduce labels outside the allowed vocabularies.
- Do not modify files in `/input_artifacts/`.
- Do not write anything to `/logs/agent/` other than `output.json`.
