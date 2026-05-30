# Input Provenance

The files in `/input_artifacts/proposed_solutions/response_A.md` through `response_I.md` are raw AI-generated candidate responses to the prompt in `/input_artifacts/problem.md`. They are unedited model outputs, preserved verbatim including verbosity, equation typos, and confident-but-wrong leaps.

They are intentionally included as heterogeneous AI outputs for a professional solution-audit workflow. The responses span the typical failure modes for problems of this kind: an asserted-uniqueness claim, a block-decomposition misreading, a truncated derivation, an unjustified multiplicative correction, two different wrong subtree decompositions, a hand-waving non-derivation, a `N!/sizes` formula with sizes that do not match the table, and a response that recognises an inconsistency in the table but then over-rides its own conclusion with a heuristic counting method. The responses are not answer keys; no single file contains the gold count alongside an oracle label.

The professional task being modelled is AI output evaluation: independently solving the underlying counting problem and committing to a single non-negative integer, then auditing model-generated proposed solutions for concrete reasoning failures. The problem is in the spirit of competition-style problems referenced by the `reference_link` in `task.toml`.
