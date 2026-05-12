An olympiad-grading workflow needs you to evaluate 150 candidate proof responses against human-assigned grades. The data is sourced from Google DeepMind's IMO-GradingBench (EMNLP 2025), which collects student-style proof attempts for olympiad problems alongside the score each attempt received from a human grader on the standard IMO 0–7 scale.

Your working directory inside the container is `/workspace`.

The dataset in `/input_artifacts/artifacts/` contains 150 artifacts. Artifact metadata is at `/input_artifacts/artifact_manifest.json`. Each artifact file contains:
- The original olympiad problem statement
- A reference solution (for grader calibration only)
- Concise grading guidelines that describe what a fully correct proof must establish
- The candidate response that is being graded
- Metadata (Grading ID, Problem ID, Source, IMO Area)

Your job:
1. Audit every artifact in `/input_artifacts/artifacts/`.
2. For each artifact, read the problem, reference solution, grading guidelines, and candidate response.
3. Predict the 4-class `predicted_grade` the candidate response would receive from a human IMO grader. The valid classes are exactly: `Correct`, `Almost`, `Partial`, `Incorrect`.
4. Assign a `confidence_score` integer in `[1, 2, 3, 4, 5]` reflecting how certain you are about the grade.
5. Carry forward the `imo_area` from the artifact metadata for each entry.
6. Aggregate the results into shard summaries and a final dataset summary.

**Grade-class definitions (from IMO-Bench):**
- `Correct` — fully correct, rigorous, complete proof. Every key claim is justified.
- `Almost` — almost correct; the main idea works but there are minor errors or small gaps.
- `Partial` — mostly incorrect, but the response contains some relevant intermediate results.
- `Incorrect` — completely incorrect, irrelevant, or empty.

Rules:
- For each artifact, `predicted_grade` must be exactly one of: `Correct`, `Almost`, `Partial`, `Incorrect`.
- For each artifact, `confidence_score` must be an integer in `{1, 2, 3, 4, 5}`.
- For each artifact, `imo_area` must be exactly one of: `Algebra`, `Combinatorics`, `Geometry`, `Number_Theory`.
- Do not skip any artifact; every `artifact_id` must appear in `grading_audits`.
- Each `grading_audit` entry must include `artifact_id`, `grading_id`, `problem_id`, `imo_area`, `predicted_grade`, `confidence_score`.
- Each `shard_summary` entry must include `shard_id`, `artifact_ids`, `artifact_count`, `grade_counts` (a map from each of the 4 grade classes to its count in that shard), and `mean_confidence` (a float, two decimal places).
- `grading_audits` must be sorted by `artifact_id` (lexicographic ascending).
- `shard_summaries` must be sorted by `shard_id` (lexicographic ascending).
- The aggregate fields `total_artifacts`, `grade_counts`, `area_counts`, `grade_by_area`, `mean_confidence`, and `artifacts_by_grade` in `summary` are computed from your per-artifact predictions.
- The output JSON must contain **only** these three top-level keys: `grading_audits`, `shard_summaries`, and `summary`. No additional top-level keys are permitted.

Write your final answer to `/logs/agent/output.json` as a single JSON object with no other content:

```json
{
  "grading_audits": [
    {
      "artifact_id": "artifact_001",
      "grading_id": "GB-0001",
      "problem_id": "PB-Advanced-001",
      "imo_area": "Combinatorics",
      "predicted_grade": "Partial",
      "confidence_score": 4
    }
  ],
  "shard_summaries": [
    {
      "shard_id": "shard_01",
      "artifact_ids": ["artifact_001", "artifact_002", "...", "artifact_010"],
      "artifact_count": 10,
      "grade_counts": {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0},
      "mean_confidence": 3.50
    }
  ],
  "summary": {
    "total_artifacts": 150,
    "grade_counts": {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0},
    "area_counts": {"Algebra": 0, "Combinatorics": 0, "Geometry": 0, "Number_Theory": 0},
    "grade_by_area": {
      "Algebra":        {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0},
      "Combinatorics":  {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0},
      "Geometry":       {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0},
      "Number_Theory":  {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0}
    },
    "mean_confidence": 3.50,
    "artifacts_by_grade": {
      "Correct":   ["artifact_001"],
      "Almost":    [],
      "Partial":   [],
      "Incorrect": []
    }
  }
}
```
