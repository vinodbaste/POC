# Input Provenance

The files in `/input_artifacts/candidate_solutions/response_A.md` through `response_I.md` are short, single-thread reasoning excerpts that paraphrase the load-bearing argument of each of nine real model outputs on the cube-and-plane problem from the public `RUC-AIBOX/OlymMATH-eval` benchmark on Hugging Face (`en_hard` split, problem `OlymMATH-HARD-1-EN`, `response_id=0` for each of nine distinct production model configurations).

The original full outputs (12K–145K characters of unedited chain-of-thought per response) were distilled into focused 1.5K–7K-character excerpts that preserve each model's primary geometric setup, the load-bearing identification or invariant, and the final claimed answer, while removing repeated speculation and redundant scratch work. Each response is adapted to the question being asked in this task ("find the largest possible value of $s^2$") and the underlying mathematical reasoning failure mode is preserved from the original benchmark output.

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

The responses are intentionally heterogeneous in failure mode: face-parallel-plane shortcuts, space-diagonal-fallacy derivations, non-negative-subset-sum restrictions, fabricated algebraic invariants, accepted internal contradictions, and decoder repetition loops all appear, mirroring the failure modes seen in the original benchmark outputs. They are NOT answer keys and they do NOT contain the gold final answer or oracle labels.

The professional task being modeled is real-world post-hoc audit of a public model-evaluation benchmark: independently solving the underlying olympiad geometry problem, then reading each model response and identifying its concrete mathematical reasoning failure mode from a controlled vocabulary.
