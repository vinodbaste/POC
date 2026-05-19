# Input Provenance

The files in `/input_artifacts/proposed_solutions/response_A.md` through `response_F.md` are raw AI-generated candidate responses to the Tetris garbage-application board-state prompt in `/input_artifacts/problem.md`.

They are intentionally included as heterogeneous AI outputs for a professional solution-audit workflow: verbose reasoning, JSON-like output, partial prose, terse summaries, friendly chatbot tone, and incorrect final boards are all part of the artifact being evaluated. They are not answer keys, and they do not contain the gold final board or oracle labels.

The professional task being modeled is AI output evaluation: independently solving the underlying reasoning problem, then auditing model-generated proposed solutions for concrete reasoning failures. The Tetris garbage-line mechanic is grounded by the `reference_link` in `task.toml`.
