# Source provenance

This task is a reasoning-math audit task. The central object being evaluated is not a real incident log; it is a bundle of candidate AI solution outputs for a constrained two-runner route-planning problem.

The problem is framed as a field-operations training-site route plan inspired by team-orienteering and route-planning settings. The proposed solution files response_A.md through response_H.md are candidate model responses collected for auditing. They are intentionally left as standalone markdown files because the agent must judge the mathematical correctness, dependency handling, feasibility analysis, optimization reasoning, calculation accuracy, and answer formatting of each response.

The external reference in task.toml provides general professional context for team-orienteering / route-planning problems. The exact hexagon instance and the candidate response bundle are included locally in /input_artifacts.
