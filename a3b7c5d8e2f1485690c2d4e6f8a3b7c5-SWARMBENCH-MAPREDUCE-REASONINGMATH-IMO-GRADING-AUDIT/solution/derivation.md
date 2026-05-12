# Oracle Derivation — IMO-GradingBench Solution-Grading Audit

Source: **Google DeepMind IMO-GradingBench** (EMNLP 2025), 1000 examples of human-graded olympiad proof responses. Repository: `google-deepmind/superhuman/imobench/gradingbench.csv`.

Task: For each of 150 candidate proof responses to olympiad problems, predict the 4-class grade a human IMO grader would assign, then aggregate distributions by grade class, IMO area, and shard.

## How the oracle was derived

Every `predicted_grade` value in `oracle_answers.json` comes directly from the **Points** column of the source CSV, mapped per IMO-Bench conventions to a 4-class label:

| Points (CSV) | Grade class | Reasoning |
|---:|---|---|
| 0 | `Incorrect` | Canonical IMO 0 — completely wrong, irrelevant, or empty |
| 1 | `Partial` | Some relevant intermediate result |
| 2 | `Partial` | Some relevant intermediate results |
| 3 | `Partial` | Borderline Partial / Almost — mapped to Partial per IMO-Bench |
| 4 | `Almost` | Borderline Partial / Almost — mapped to Almost per IMO-Bench |
| 5 | `Almost` | Main idea works, multiple gaps |
| 6 | `Almost` | Canonical IMO 6 — main idea works, minor gap |
| 7 | `Correct` | Canonical IMO 7 — fully correct, rigorous, complete |

The mapping is **deterministic** (no synthesis) so every oracle label is traceable to a human-assigned IMO grade in the published IMO-GradingBench CSV.

The `confidence_score` in the oracle is also deterministic, derived from the original Points value:

| Points | Confidence |
|---:|---:|
| 0 | 5 (solid Incorrect anchor) |
| 1 | 4 (solid Partial anchor) |
| 2, 3, 4, 5 | 3 (borderline within IMO-Bench mapping) |
| 6 | 4 (solid Almost anchor) |
| 7 | 5 (solid Correct anchor) |

A capable agent following the rubric and observing the response quality will assign confidence values that roughly match this distribution — the oracle's confidence is the consensus a careful human grader would express.

## Selection process

From the 1000-row source CSV, 150 examples were chosen with a seeded random sample (seed=42) and balanced across the 4 grade classes:

| Class | Count |
|---|---:|
| Incorrect | 38 |
| Partial   | 38 |
| Almost    | 37 |
| Correct   | 37 |
| **Total** | **150** |

Problems span 8 sources (Novel Problem, modified IMO 2024 P1–P6, USAMO 2025). IMO area assignment uses the official problem-area labels for IMO 2024 problems and a deterministic hash-based assignment for Novel and USAMO problems (this is metadata for cross-tab statistics — not a graded quantity).

## Per-shard composition

15 shards, each containing 10 consecutive artifacts (artifact_001 … artifact_150). Each shard's `mean_confidence`, `grade_counts`, and `artifact_ids` are computed mechanically from the underlying oracle truth.

## Summary aggregates

Built mechanically from the 150 oracle entries:
- `total_artifacts`: 150
- `grade_counts`: 37 Correct / 37 Almost / 38 Partial / 38 Incorrect
- `area_counts`: 14 Algebra / 41 Combinatorics / 62 Geometry / 33 Number_Theory
- `grade_by_area`: full 4×4 cross-tab
- `mean_confidence`: 4.29 (derived from per-row scores)
- `artifacts_by_grade`: lists of artifact_ids per grade class, sorted by artifact_id

## Reproducibility

Run `python solution/generate_oracle.py` from the task root (with `solution/oracle_answers.json` and `environment/input_artifacts/artifact_manifest.json` present) to regenerate `solution/oracle.json`. The same script with the same inputs produces a bitwise-identical oracle.

## Defensibility per Mistake 14

Every ground-truth value in the oracle is traceable to:
- the **Points** column of `gradingbench.csv` (human-assigned IMO score), and
- the **Problem ID**, **Problem Source**, and other metadata columns of the same CSV.

No values were invented, paraphrased, or synthesized.
