# Input Provenance

The files in `/input_artifacts/proposed_solutions/response_A.md` through `response_I.md` are real, unedited model outputs collected from the public `RUC-AIBOX/OlymMATH-eval` benchmark on Hugging Face (`en_hard` split, problem `OlymMATH-HARD-1-EN`, `response_id=0` for each of nine distinct production model configurations). They are **not** synthetic or hand-crafted: they were generated outside this task by the OlymMATH-eval authors when they evaluated their lineup of open-source reasoning models on this olympiad geometry problem, and they are bit-for-bit identical to the public release.

Model configurations, in response-letter order A through I:

| Letter | Model config |
|---|---|
| A | qwen3-0.6b |
| B | deepscaler-1.5b-preview |
| C | still-3-1.5b-preview |
| D | deepseek-r1-distill-qwen-1.5b |
| E | openmath-nemotron-1.5b |
| F | light-r1-7b-ds |
| G | openthinker2-7b |
| H | skywork-or1-math-7b |
| I | openmath-nemotron-7b |

The responses are intentionally heterogeneous in style — long chain-of-thought traces, contradictory intermediate claims, repetition loops, and incorrect final answers all appear in production reasoning-model outputs and are part of the artifact being evaluated. They are NOT answer keys and they do NOT contain the gold final answer or the oracle's failure-reason labels.

The professional task being modeled is real-world post-hoc audit of a public model-evaluation benchmark: independently solving the underlying olympiad geometry problem, then reading each shipped model response and identifying its concrete mathematical reasoning failures from a controlled vocabulary.
