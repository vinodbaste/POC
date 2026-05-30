# Input Provenance

The files in `/input_artifacts/proposed_solutions/response_A.md` through `response_H.md` are raw AI-generated candidate responses to the combinatorial interval-reconstruction prompt in `/input_artifacts/problem.md`.

They are intentionally included as heterogeneous AI outputs for a professional solution-audit workflow: verbose reasoning, swapped extremal formulas, ignored continuity constraints, arithmetic mistakes on positive-difference and total-visibility sums, qualitative non-derivations, and fabricated adjacent-min identities are all part of the artifact being evaluated. None of the eight proposed responses establishes both extremal claims with a fully valid proof of optimality, but several state partial values that happen to coincide with one of the gold integers. The responses are not answer keys; no single file contains the gold values of m, M, and m+M together, nor any oracle labels.

The professional task being modeled is AI output evaluation: independently solving the underlying reasoning problem (deriving the extremal formulas under the contiguous-interval visibility condition and computing m, M, and m+M for the given array), then auditing model-generated proposed solutions for concrete reasoning failures. The contiguous-interval visibility model is grounded by the `reference_link` in `task.toml`.
