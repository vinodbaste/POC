A benchmark-curation team is converting incorrect informal proof attempts for miniF2F problems into a multiple-choice audit set for downstream evaluator training.

The dataset in `/input_artifacts/artifacts/` contains 28 incorrect proof attempts drawn from AMC, AIME, IMO, and MATH competition problems in the miniF2F benchmark. Each artifact file contains:
- the original problem statement,
- the full incorrect informal proof attempt,
- four candidate proof excerpts labeled A-D (presented in randomized order, not necessarily proof order),
- a reviewer note copied from the curation log.

Exactly one candidate excerpt contains the first mathematically invalid or unjustified reasoning step for that artifact.

Your job:
1. Audit every artifact in `/input_artifacts/artifacts/`.
2. For each artifact, choose exactly one option letter from `A`, `B`, `C`, or `D`.
3. For each artifact, classify the error category as exactly one of: `unjustified_claim`, `misapplied_theorem`, `algebraic_error`, `case_error`, `circular_reasoning`.
4. Aggregate the results into shard summaries and a final dataset summary.

Rules:
- Use the option letters exactly as shown in each artifact file.
- Do not skip any artifact.
- `artifact_audits` must be sorted by `artifact_id`.
- `shard_summaries` must be sorted by `shard_id`.
- `artifacts_by_option` lists must be sorted by `artifact_id`.
- `competition_counts`, `year_counts`, and all choice counts must match the per-artifact selections exactly.
- For each artifact, `error_category` must be exactly one of: `unjustified_claim`, `misapplied_theorem`, `algebraic_error`, `case_error`, `circular_reasoning`.

**Error category taxonomy:**
- `unjustified_claim`: a step asserts a result without justification or proof
- `misapplied_theorem`: a theorem is invoked but its applicability conditions are not satisfied
- `algebraic_error`: an arithmetic, algebraic, or counting mistake produces an incorrect value
- `case_error`: a case analysis is incomplete, double-counts, or uses an invalid case split
- `circular_reasoning`: the argument assumes the conclusion it needs to prove

**Analytical guidance:** Each artifact includes a Full Solution section showing the proof steps in chronological order, and a Candidate Excerpts section where the same steps appear with shuffled labels (A–D). To identify the first invalid step: read the Full Solution to establish the chronological order of steps, map each option label to its position in that order, then select the option whose step is the earliest mathematically invalid or unjustified step. The correct answer may be any letter.

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "artifact_audits": [
    {
      "artifact_id": "artifact_01",
      "problem_id": "aime_1983_p9",
      "competition": "AIME",
      "year": 1983,
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
      "AIME": 0,
      "AMC": 0,
      "IMO": 0,
      "MATH": 0
    },
    "year_counts": {
      "1983": 0
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
