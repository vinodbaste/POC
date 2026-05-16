# Input Provenance

The files in `/input_artifacts/proposed_solutions/response_A.md` through `response_I.md` are raw AI-generated candidate solutions to the cube-plane-distances olympiad problem in `/input_artifacts/problem.md`.

Each response is `response_id=0` from one of 9 small-to-mid-size open-source reasoning models evaluated on the `OlymMATH-HARD-1-EN` problem in the public `RUC-AIBOX/OlymMATH-eval` dataset (`en_hard` split). Model configs, in response-letter order A through I:

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

The responses are intentionally heterogeneous AI outputs for a solution-audit workflow: long chain-of-thought traces, contradictory intermediate claims, repetition loops, and incorrect final answers are all part of the artifact being evaluated. They are NOT answer keys and they do NOT contain the gold final answer or oracle labels.

The professional task being modeled is AI output evaluation: independently solving the underlying olympiad geometry problem, then auditing each model-generated proposed solution for concrete reasoning failures drawn from a controlled phrase-triggered vocabulary.
