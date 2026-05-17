# Input Provenance

The files in `/input_artifacts/candidate_solutions/response_A.md` through `response_H.md` are real, unedited model outputs produced by distinct model configurations during benchmark data collection for this task. They were generated outside the audit task by giving the sequence-envelope problem statement in `/input_artifacts/problem_statement.md` to each model and saving the raw response text without hand-editing.

The responses are intentionally heterogeneous: short plausible arguments, overconfident wrong final counts, contradictory revisions, incomplete worst-case reasoning, missing lower-bound proofs, and invalid one-draw inferences all appear in ordinary production reasoning-model outputs. They are NOT answer keys and they do NOT contain the oracle's criterion labels, verdicts, or primary failure codes.

The professional task being modeled is post-hoc audit of model-generated mathematical reasoning: independently solving the underlying sequence-envelope puzzle, then reading each shipped model response and identifying its concrete mathematical reasoning failures from a controlled vocabulary.
