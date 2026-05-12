# Olympiad Proof Validity Audit

You are helping curate a math-evaluation set built from real olympiad-style proof attempts in the Open Proof Corpus.

Your job is to audit every proof artifact listed in `/input_artifacts/proof_manifest.json`.

The input files are at:

- `/input_artifacts/proof_manifest.json`
- `/input_artifacts/judging_rubric.md`
- `/input_artifacts/proofs/`
- `/input_artifacts/background_number_theory.md`
- `/input_artifacts/background_geometry.md`
- `/input_artifacts/background_combinatorics.md`
- `/input_artifacts/background_algebra_analysis.md`
- `/input_artifacts/background_functional_equations.md`

Your working directory is `/workspace`.

Each proof artifact contains:

- the original competition problem statement
- one candidate solution attempt
- source metadata including the mathematical domain

The domain background files contain mathematical theory, proof technique standards, and worked examples organized by mathematical domain. Each proof file indicates its relevant domain background at the top. Consulting the appropriate background file typically leads to more accurate verdicts and better identification of first material issues.

For every proof artifact in the manifest:

1. Read the full problem and the full candidate solution attempt.
2. Decide whether the candidate solution is mathematically `correct` or `incorrect`.
3. If the proof is incorrect, identify the earliest material issue in one short sentence.
4. If the proof is correct, set `first_material_issue_summary` to `none`.

Then synthesize a final audit report covering all artifacts.

Scoring expectations:

- A proof is `correct` only if the argument actually works.
- A proof is `incorrect` if a false claim, unsupported inference, or skipped critical step breaks the argument.
- For incorrect proofs, report the first material issue, not every later problem.

Ordering requirements:

- Audit every artifact listed in the manifest exactly once.
- Sort `artifact_audits` by increasing `artifact_id`.
- Sort `summary.competitions_covered` alphabetically.
- Sort `summary.correct_problem_ids` alphabetically.
- Sort `summary.incorrect_problem_ids` alphabetically.

---

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```json
{
  "artifact_audits": [
    {
      "artifact_id": "proof_01",
      "problem_id": "<str>",
      "competition": "<str>",
      "verdict": "correct or incorrect",
      "first_material_issue_summary": "<str; use none if correct>"
    }
  ],
  "summary": {
    "correct_count": <int>,
    "incorrect_count": <int>,
    "competitions_covered": ["<str>", "<str>"],
    "correct_problem_ids": ["<str>", "<str>"],
    "incorrect_problem_ids": ["<str>", "<str>"]
  }
}
```

Do not write anything else to that file.
