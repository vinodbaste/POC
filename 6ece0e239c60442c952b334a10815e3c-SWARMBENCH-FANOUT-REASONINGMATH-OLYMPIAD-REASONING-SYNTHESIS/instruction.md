You are conducting a mathematical reasoning synthesis task across multiple olympiad-style mathematics datasets.

Datasets are located at:

/input_artifacts/algebra.jsonl
/input_artifacts/geometry.jsonl
/input_artifacts/counting_and_probability.jsonl
/input_artifacts/number_theory.jsonl
/input_artifacts/precalculus.jsonl

Each dataset contains between 746 and 1744 competition-level mathematics problems and solutions with fields:
- "problem": the problem statement
- "solution": the full solution with proof steps
- "level": difficulty from "Level 1" (easiest) to "Level 5" (hardest)
- "type": the mathematical domain

---

## Analytical Methodology

### Computing Domain Statistics

For each domain JSONL file:
1. Read every line and parse as JSON.
2. Count total lines to get `total_problems` — do not rely on any pre-stated count; each domain varies in size.
3. Tally the `"level"` field for each problem to build the exact `level_distribution` (Level 1 through Level 5). Every problem must be accounted for; the five level counts must sum exactly to `total_problems`.
4. Compute `hard_problems_count` = count of Level 4 + count of Level 5.
5. Express the hard-problem rate as an exact fraction **X/Y=Z%** (e.g., "598/870=68.7%"); do not use rounded percentages alone.

### Reading and Analyzing Solution Texts

After computing statistics, read the actual `"solution"` text for Level 4 and Level 5 problems in each domain. This is required — statistics alone (level counts, hard-rates) can be computed from labels; proof patterns and failure modes must be grounded in the solution texts themselves.

For each domain, systematically examine the solution texts and identify:
- **(a) Proof approach patterns**: The 3 most frequently occurring proof approaches in Level 4–5 solutions. Look for structural signatures: auxiliary constructions, modular chains, recursive decompositions, substitution strategies, etc.
- **(b) Level 5 first-step patterns**: The characteristic initial setup or opening move in Level 5 solutions (e.g., "introduce an auxiliary circle", "reduce mod p", "define a recurrence over states").
- **(c) Level 3 → Level 5 structural shift**: How solution structure — length, number of cases, use of abstraction — changes from Level 3 to Level 5 within the domain.
- **(d) Failure-mode evidence**: Solution-text patterns that indicate where incorrect approaches fail (e.g., "solutions that skip verifying auxiliary construction existence fail in the congruence step").

### Structuring Domain Analysis

Each domain report should contain:
1. Exact statistics (total, level distribution, hard count) computed from the file.
2. Dominant proof-approach patterns grounded in solution texts with frequency evidence (e.g., "observed in ~60% of Level 5 solutions sampled").
3. Domain-specific difficulty characterization — what makes Level 5 problems structurally harder than Level 3 in this domain specifically.
4. At least one concrete example of how a reasoning failure manifests in actual solution steps for that domain.

### Synthesis Requirements

The final synthesis must:
- Use exact fractions (X/Y=Z%) for every domain statistic cited — never rounded percentages alone.
- Rank all 5 domains by hard-problem rate and support the ranking with exact fractions.
- Ground every proof technique, failure mode, hardest family, and style comparison in solution-text evidence, not just difficulty statistics.
- Provide exactly 10 proof techniques in `top_proof_techniques`, each attributed to a specific domain with an exact level-distribution fraction.
- Ensure every failure mode includes both (i) the exact level-distribution fraction causing the skew and (ii) a description of how the failure manifests in actual solution steps.
- Ensure every hardest problem family includes both (i) the exact level-distribution fraction and (ii) the characteristic solution-approach pattern that creates difficulty.

---

## Tasks

1. For each domain, count the EXACT total number of problems, the exact level distribution (Level 1 through Level 5), and the total count of hard problems (Level 4 + Level 5 combined). You must read the actual files to get accurate counts — the datasets vary in size.

2. Identify the dominant proof strategies across domains, attributing each strategy to the specific domain(s) where it appears most and referencing the domain's hard-problem rate (as an exact fraction X/Y=Z%) to justify why that domain requires that strategy.

3. Compare reasoning styles across algebra, geometry, counting_and_probability, number_theory, and precalculus — anchoring each comparison to the domain's hard-problem rate and level distribution you computed, expressed as exact fractions.

4. For each domain, read Level 4 and Level 5 solution texts systematically and identify:
   (a) The 3 most common proof approach patterns observed in actual solution texts at those levels.
   (b) Characteristic first-step or setup patterns in Level 5 solutions specifically.
   (c) How solution structure changes from Level 3 to Level 5 within the domain.

5. Identify the most subtle reasoning failure modes, linking each to a specific domain's difficulty pattern using EXACT level-distribution fractions (e.g., "geometry 421/870=48.4% Level 5") AND describing how the failure manifests in actual solution steps.

6. Determine which problem families require the deepest abstraction, justifying with exact level-distribution fractions AND the solution-approach patterns that make them hard.

7. Extract EXACTLY 10 of the most sophisticated proof techniques with domain attribution, exact level-distribution fractions, and difficulty explanation grounded in the data. The `top_proof_techniques` array must contain exactly 10 entries.

8. Synthesize cross-domain reasoning transfer, ranking all 5 domains by hard-problem rate using exact fractions (X/Y=Z%) and describing how solution-text patterns transfer across this difficulty spectrum.

Working directory:
/workspace

---

Write your final answer to:

`/logs/agent/output.json`

Use this exact JSON format:

```json
{
  "domain_statistics": {
    "algebra": {
      "total_problems": <int>,
      "level_distribution": {"Level 1": <int>, "Level 2": <int>, "Level 3": <int>, "Level 4": <int>, "Level 5": <int>},
      "hard_problems_count": <int>
    },
    "geometry": {
      "total_problems": <int>,
      "level_distribution": {"Level 1": <int>, "Level 2": <int>, "Level 3": <int>, "Level 4": <int>, "Level 5": <int>},
      "hard_problems_count": <int>
    },
    "counting_and_probability": {
      "total_problems": <int>,
      "level_distribution": {"Level 1": <int>, "Level 2": <int>, "Level 3": <int>, "Level 4": <int>, "Level 5": <int>},
      "hard_problems_count": <int>
    },
    "number_theory": {
      "total_problems": <int>,
      "level_distribution": {"Level 1": <int>, "Level 2": <int>, "Level 3": <int>, "Level 4": <int>, "Level 5": <int>},
      "hard_problems_count": <int>
    },
    "precalculus": {
      "total_problems": <int>,
      "level_distribution": {"Level 1": <int>, "Level 2": <int>, "Level 3": <int>, "Level 4": <int>, "Level 5": <int>},
      "hard_problems_count": <int>
    }
  },
  "proof_strategy_taxonomy": [
    {"strategy": "<string>", "description": "<string>"}
  ],
  "reasoning_style_comparison": {
    "algebra": "<string>",
    "geometry": "<string>",
    "counting_and_probability": "<string>",
    "number_theory": "<string>",
    "precalculus": "<string>"
  },
  "most_subtle_reasoning_failure_modes": ["<string>"],
  "hardest_problem_families": [
    {"family": "<string>", "reason": "<string>"}
  ],
  "top_proof_techniques": [
    {"technique": "<string>", "difficulty_reason": "<string>"}
  ],
  "cross_domain_reasoning_transfer": "<string>"
}
```
