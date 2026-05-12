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

The domain background files contain mathematical theory, proof technique standards, and worked examples organized by mathematical domain:

- `background_number_theory.md` — divisibility, modular arithmetic, prime factorization, Diophantine techniques
- `background_geometry.md` — Euclidean and coordinate geometry, circle theorems, transformations, angle-chasing
- `background_combinatorics.md` — counting principles, graph theory, combinatorial optimization, pigeonhole
- `background_algebra_analysis.md` — inequalities, polynomials, real analysis, monotonicity, functional analysis
- `background_functional_equations.md` — substitution strategies, Cauchy-type equations, regularity conditions

## Analytical guidance

Follow these steps for each proof artifact:

1. Check the `domain` field in the proof file's header to identify the mathematical domain.
2. Read the corresponding background file listed above **before** evaluating the proof. The background file provides the theoretical framework and worked examples needed to correctly identify whether the proof's steps are valid. Skipping this step increases the risk of missing subtle domain-specific flaws.
3. Read the full problem statement and the full candidate solution attempt.
4. Decide whether the candidate solution is mathematically `correct` or `incorrect`.
5. If the proof is incorrect, identify the **first material issue** — the earliest step or claim that breaks the argument — in one sentence. A material issue is a false claim, an unsupported inference, or a skipped critical step that makes the rest of the argument invalid. Do not report downstream consequences of the first flaw; report only the flaw itself. The `first_material_issue_summary` should be one sentence identifying the specific step or claim that is wrong.
6. If the proof is correct, set `first_material_issue_summary` to `none`.

Then synthesize a final audit report covering all artifacts. Each entry in `artifact_audits` must include the fields `artifact_id`, `problem_id`, `competition`, `verdict`, and `first_material_issue_summary`. The `summary` block must include `correct_count`, `incorrect_count`, `competitions_covered`, `correct_problem_ids`, and `incorrect_problem_ids`.

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
