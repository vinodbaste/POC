A benchmark-curation team is converting real human flaw annotations from the Open Proof Corpus into a multiple-choice audit set for downstream evaluator training.

Your working directory inside the container is `/workspace`.

The dataset in `/input_artifacts/artifacts/` contains 75 incorrect olympiad proof attempts from BMOSL, IMOSL, and USAMO. A review rubric describing the evaluation procedure is at `/input_artifacts/review_rubric.md`. Artifact metadata (problem_id, competition, year) for all 75 artifacts is available at `/input_artifacts/artifact_manifest.json`. Each artifact file contains:
- the original problem,
- the full incorrect proof attempt,
- four candidate proof excerpts labeled A-D (presented in randomized order, not necessarily proof order),
- a reviewer note copied from the corpus.

Exactly one candidate excerpt contains the human-marked first unrecoverable flaw for that artifact.

Your job:
1. Audit every artifact in `/input_artifacts/artifacts/`.
2. For each artifact, choose exactly one option letter from `A`, `B`, `C`, or `D`.
3. For each artifact, classify the flaw type using the decision procedure in `/input_artifacts/review_rubric.md`. The result must be exactly one of: `unjustified_claim`, `misapplied_theorem`, `false_assumption`, `scope_violation`, `algebraic_error`.
4. Aggregate the results into shard summaries and a final dataset summary.

Rules:
- For each artifact, `selected_option` must be exactly one of the letters `A`, `B`, `C`, or `D` as labeled in that artifact file.
- Do not skip any artifact; every `artifact_id` must appear in `artifact_audits`.
- Each `artifact_audit` entry must include `artifact_id`, `problem_id`, `competition`, `year`, `selected_option`, and `flaw_type`.
- Each `shard_summary` entry must include `shard_id`, `artifact_ids`, `artifact_count`, and `choice_counts`, with `artifact_count` equal to the length of `artifact_ids`.
- `artifact_audits` must be sorted by `artifact_id` (lexicographic ascending).
- `shard_summaries` must be sorted by `shard_id` (lexicographic ascending).
- `artifacts_by_option` lists must be sorted by `artifact_id` (lexicographic ascending).
- The aggregate fields `total_artifacts`, `choice_counts`, `competition_counts`, `year_counts`, and `artifacts_by_option` in `summary` are informational tallies computed from your per-artifact selections. They are not independently scored.
- For each artifact, `flaw_type` must be exactly one of: `unjustified_claim`, `misapplied_theorem`, `false_assumption`, `scope_violation`, `algebraic_error`.
- The output JSON must contain **only** these three top-level keys: `artifact_audits`, `shard_summaries`, and `summary`. No additional top-level keys are permitted.

**Flaw type taxonomy:**
- `unjustified_claim`: A conclusion is asserted without proof or supporting reasoning.
- `misapplied_theorem`: A theorem or lemma is invoked but its applicability conditions are not satisfied.
- `false_assumption`: The proof relies on a premise that does not hold in the given context.
- `scope_violation`: A result valid in one domain or case is applied outside that scope.
- `algebraic_error`: An arithmetic, algebraic, or counting mistake produces an incorrect value.

**Analytical guidance:** Each artifact includes a "Full Candidate Proof" section showing proof steps in their original chronological order, and a "Candidate Excerpts" section where the same steps appear with shuffled labels (A–D). The option labels do not necessarily match the proof sequence. To identify the first unrecoverable flaw: read the Full Candidate Proof to establish the chronological order of steps, map each option label to its position in that order, then select the option whose step is the earliest unrecoverable error. The correct answer may be option C or D even if A or B appear earlier alphabetically.

Write your final answer to `/logs/agent/output.json` as a single JSON object with no other content:

{
  "artifact_audits": [
    {
      "artifact_id": "artifact_01",
      "problem_id": "BMOSL_2018_15",
      "competition": "BMOSL",
      "year": 2018,
      "selected_option": "A",
      "flaw_type": "unjustified_claim"
    }
  ],
  "shard_summaries": [
    {
      "shard_id": "shard_01",
      "artifact_ids": ["artifact_01", "artifact_02", "artifact_03", "artifact_04", "artifact_05"],
      "artifact_count": 5,
      "choice_counts": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
      }
    }
  ],
  "summary": {
    "total_artifacts": 75,
    "choice_counts": {
      "A": 0,
      "B": 0,
      "C": 0,
      "D": 0
    },
    "competition_counts": {
      "BMOSL": 0,
      "IMOSL": 0,
      "USAMO": 0
    },
    "year_counts": {
      "2007": 0
    },
    "artifacts_by_option": {
      "A": ["artifact_01"],
      "B": [],
      "C": [],
      "D": []
    }
  }
}
