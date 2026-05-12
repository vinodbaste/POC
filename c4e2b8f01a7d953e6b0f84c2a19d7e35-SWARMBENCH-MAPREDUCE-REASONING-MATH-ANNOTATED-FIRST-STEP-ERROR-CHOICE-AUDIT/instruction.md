A benchmark-curation team is converting LLM reasoning-error annotations from the ProcessBench dataset into a multiple-choice audit set for downstream evaluator training.

The dataset in `/input_artifacts/artifacts/` contains 28 incorrect LLM-generated solutions to competition- and olympiad-level mathematics problems from OlympiadBench. Each artifact file contains:
- the original problem,
- the full incorrect multi-step solution attempt,
- four candidate step excerpts labeled A-D (presented in randomized order, not necessarily solution order),
- a reviewer note copied from the ProcessBench annotation.

Exactly one candidate excerpt contains the human-identified first unrecoverable reasoning error for that artifact.

Your job:
1. Audit every artifact in `/input_artifacts/artifacts/`.
2. For each artifact, choose exactly one option letter from `A`, `B`, `C`, or `D`.
3. For each artifact, classify the error category as exactly one of: `unjustified_claim`, `misapplied_theorem`, `algebraic_error`, `case_error`, `circular_reasoning`.
4. Aggregate the results into shard summaries and a final dataset summary. Shard groupings are defined in `/input_artifacts/shards/` (one JSON file per shard: `shard_01.json` through `shard_07.json`; each file lists the `artifact_ids` belonging to that shard).

To identify the first erroneous step: read the solution steps in order from top to bottom, mapping each option label (A, B, C, D) to its position in the solution narrative. The first step that introduces an unrecoverable error — one that, if left uncorrected, invalidates all subsequent reasoning — is the target. Cross-check against the reviewer note for confirmation. Once you have identified that step, classify its error type using the taxonomy below.

Rules:
- Use the option letters exactly as shown in each artifact file.
- Do not skip any artifact.
- `error_category` must be exactly one of: `unjustified_claim`, `misapplied_theorem`, `algebraic_error`, `case_error`, `circular_reasoning`.
- `artifact_audits` must be sorted by `artifact_id`.
- `shard_summaries` must be sorted by `shard_id`.
- `artifacts_by_option` lists must be sorted by `artifact_id`.
- `competition_counts`, `year_counts`, and all choice counts must match the per-artifact selections exactly.
- Every artifact audit entry must include: `artifact_id`, `problem_id`, `competition`, `year`, `selected_option`, and `error_category`.

Error category taxonomy:
- `unjustified_claim`: a step asserts a result without justification
- `misapplied_theorem`: a theorem invoked but conditions aren't satisfied
- `algebraic_error`: arithmetic, algebraic, or counting mistake
- `case_error`: incomplete, double-counted, or invalid case split
- `circular_reasoning`: the argument assumes the conclusion

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "artifact_audits": [
    {
      "artifact_id": "artifact_01",
      "problem_id": "OLYMPIADBENCH_0",
      "competition": "OlympiadBench",
      "year": 2024,
      "selected_option": "A",
      "error_category": "unjustified_claim"
    }
  ],
  "shard_summaries": [
    {
      "shard_id": "shard_01",
      "artifact_ids": ["artifact_01", "artifact_02", "artifact_03", "artifact_04"],
      "artifact_count": 4,
      "choice_counts": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
      }
    }
  ],
  "summary": {
    "total_artifacts": 28,
    "choice_counts": {
      "A": 0,
      "B": 0,
      "C": 0,
      "D": 0
    },
    "competition_counts": {
      "OlympiadBench": 0
    },
    "year_counts": {
      "2024": 0
    },
    "artifacts_by_option": {
      "A": ["artifact_01"],
      "B": [],
      "C": [],
      "D": []
    }
  }
}

Do not write anything else to that file.
