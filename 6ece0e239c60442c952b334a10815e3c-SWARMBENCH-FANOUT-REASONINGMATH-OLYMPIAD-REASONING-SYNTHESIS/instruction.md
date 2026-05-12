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

Your tasks:

1. For each domain, count the EXACT total number of problems, the exact level distribution (Level 1 through Level 5), and the total count of hard problems (Level 4 + Level 5 combined). You must read the actual files to get accurate counts — the datasets vary in size.

2. Identify the dominant proof strategies across domains, attributing each strategy to the specific domain(s) where it appears most and referencing the domain's hard-problem rate to justify why that domain requires that strategy.

3. Compare reasoning styles across algebra, geometry, counting_and_probability, number_theory, and precalculus — anchoring each comparison to the domain's hard-problem rate and level distribution you computed.

4. For each domain, read Level 4 and Level 5 solution texts systematically and identify:
   (a) The 3 most common proof approach patterns observed in actual solution texts at those levels.
   (b) Characteristic first-step or setup patterns in Level 5 solutions specifically.
   (c) How solution structure changes from Level 3 to Level 5 within the domain.

5. Identify the most subtle reasoning failure modes, linking each to a specific domain's difficulty pattern using EXACT level-distribution fractions (e.g., "geometry 421/870=48.4% Level 5") AND describing how the failure manifests in actual solution steps.

6. Determine which problem families require the deepest abstraction, justifying with exact level-distribution fractions AND the solution-approach patterns that make them hard.

7. Extract the 10 most sophisticated proof techniques with domain attribution, exact level-distribution fractions, and difficulty explanation grounded in the data.

8. Synthesize cross-domain reasoning transfer, ranking the 5 domains by hard-problem rate using exact fractions (X/Y=Z%) and describing how solution-text patterns transfer across this difficulty spectrum.

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
