A peer-review pod for an olympiad training program is auditing 20 published solutions to past competition problems. Each solution carries a list of numbered "key claims" that the solution rests on, and the pod needs to (a) verify each claim is logically supported by the surrounding proof, (b) identify the central mathematical technique used, and (c) score the solution's rigor.

Your working directory inside the container is `/workspace`.

The dataset in `/input_artifacts/artifacts/` contains 20 artifacts. The audit rubric is at `/input_artifacts/audit_rubric.md`. Artifact metadata (problem_id, competition, year) is at `/input_artifacts/artifact_manifest.json`. Each artifact file contains:
- The original olympiad problem statement
- The full published solution (with steps numbered)
- A list of 6 to 8 "key claims" that the solution rests on (each tagged `[C1]`, `[C2]`, ...)
- A short editor's note

Your job:
1. Audit every artifact in `/input_artifacts/artifacts/`.
2. For each artifact, classify EVERY claim `[Ci]` as one of: `verified`, `unjustified`, or `incorrect`. Use the decision procedure in `/input_artifacts/audit_rubric.md`.
3. For each artifact, identify the central technique used from the fixed taxonomy: `algebraic_manipulation`, `combinatorial_counting`, `induction`, `inequality_application`, `modular_arithmetic`, `geometric_construction`, `extremal_principle`, `invariant_or_monovariant`, `generating_function`, `proof_by_contradiction`.
4. For each artifact, assign a `rigor_score` integer from 1 (gaps, hand-waving) to 5 (every claim airtight).
5. Aggregate the results into shard summaries and a final dataset summary.

Rules:
- For each artifact, `claim_audits` must contain exactly one entry per claim tag found in that artifact, with the claim_id matching the artifact's tag (e.g., `"C1"`) and `status` being exactly one of `verified`, `unjustified`, `incorrect`.
- For each artifact, `central_technique` must be exactly one of the 10 taxonomy values listed above.
- For each artifact, `rigor_score` must be an integer in `[1, 2, 3, 4, 5]`.
- Do not skip any artifact; every `artifact_id` must appear in `artifact_audits`.
- Each `artifact_audit` entry must include `artifact_id`, `problem_id`, `competition`, `year`, `central_technique`, `rigor_score`, and `claim_audits`.
- Each `shard_summary` entry must include `shard_id`, `artifact_ids`, `artifact_count`, `technique_counts` (a map from each of the 10 taxonomy values to its count in that shard), and `mean_rigor` (a float, two decimal places).
- `artifact_audits` must be sorted by `artifact_id` (lexicographic ascending).
- `shard_summaries` must be sorted by `shard_id` (lexicographic ascending).
- `artifacts_by_technique` lists in `summary` must be sorted by `artifact_id` (lexicographic ascending).
- The aggregate fields `total_artifacts`, `total_claims`, `claim_status_counts`, `technique_counts`, `mean_rigor`, `competition_counts`, `year_counts`, and `artifacts_by_technique` in `summary` are computed from your per-artifact selections.
- The output JSON must contain **only** these three top-level keys: `artifact_audits`, `shard_summaries`, and `summary`. No additional top-level keys are permitted.

**Analytical guidance:** A claim is `verified` only if the surrounding solution text contains a derivation that supports it (citation of a theorem with verified preconditions, or explicit algebra/geometry leading to the claim). A claim is `unjustified` if the solution asserts it as obvious without supplying a derivation. A claim is `incorrect` only if you can identify a concrete logical or computational error making the claim false. Apply the decision procedure in `/input_artifacts/audit_rubric.md` (verified → unjustified → incorrect, in that order).

Write your final answer to `/logs/agent/output.json` as a single JSON object with no other content:

```json
{
  "artifact_audits": [
    {
      "artifact_id": "artifact_01",
      "problem_id": "IMO_2018_2",
      "competition": "IMO",
      "year": 2018,
      "central_technique": "algebraic_manipulation",
      "rigor_score": 4,
      "claim_audits": [
        {"claim_id": "C1", "status": "verified"},
        {"claim_id": "C2", "status": "unjustified"}
      ]
    }
  ],
  "shard_summaries": [
    {
      "shard_id": "shard_01",
      "artifact_ids": ["artifact_01", "artifact_02", "artifact_03", "artifact_04"],
      "artifact_count": 4,
      "technique_counts": {
        "algebraic_manipulation": 0,
        "combinatorial_counting": 0,
        "induction": 0,
        "inequality_application": 0,
        "modular_arithmetic": 0,
        "geometric_construction": 0,
        "extremal_principle": 0,
        "invariant_or_monovariant": 0,
        "generating_function": 0,
        "proof_by_contradiction": 0
      },
      "mean_rigor": 3.50
    }
  ],
  "summary": {
    "total_artifacts": 20,
    "total_claims": 140,
    "claim_status_counts": {"verified": 0, "unjustified": 0, "incorrect": 0},
    "technique_counts": {
      "algebraic_manipulation": 0,
      "combinatorial_counting": 0,
      "induction": 0,
      "inequality_application": 0,
      "modular_arithmetic": 0,
      "geometric_construction": 0,
      "extremal_principle": 0,
      "invariant_or_monovariant": 0,
      "generating_function": 0,
      "proof_by_contradiction": 0
    },
    "mean_rigor": 3.50,
    "competition_counts": {"IMO": 0, "USAMO": 0, "IMOSL": 0, "BMOSL": 0},
    "year_counts": {"2018": 0},
    "artifacts_by_technique": {
      "algebraic_manipulation": ["artifact_01"],
      "combinatorial_counting": [],
      "induction": [],
      "inequality_application": [],
      "modular_arithmetic": [],
      "geometric_construction": [],
      "extremal_principle": [],
      "invariant_or_monovariant": [],
      "generating_function": [],
      "proof_by_contradiction": []
    }
  }
}
```
