# Input Provenance

The files in `/input_artifacts/proposed_solutions/response_A.md` through `response_I.md` are raw AI-generated candidate responses to the tetrahedron-incenter multi-claim problem in `/input_artifacts/problem.md`.

They are intentionally included as heterogeneous AI outputs for a professional solution-audit workflow: correct proofs, correct final-answer-set with invalid proof chains, unconstructed counterexamples, self-contradictory examples, visible chain-of-thought traces, false universal claims about tangential tetrahedra, and incoherent algebraic identities are all part of the artifact being evaluated. They are not answer keys, and they do not contain the gold final answer set or oracle labels.

The professional task being modeled is AI output evaluation: independently solving the underlying olympiad-level 3D geometry problem, then auditing model-generated proposed solutions for concrete reasoning failures. The exact problem instance and the candidate response bundle are included locally in `/input_artifacts`. The external reference in `task.toml` provides general professional context for the source mathematical problem.
