## Provenance of the proposed solution bundle

Seven candidate responses (`response_A.md` through `response_G.md`) live in
`/input_artifacts/proposed_solutions/`. Each is a raw, unedited attempt produced
by a different weak-to-mid open-source language model when given the
hexagonal-prism shortest-surface-path question in `problem.md`. The responses
were not curated for correctness: they are presented as-is, with whatever
unfolding choice, citations, and final answer the underlying model produced.

The underlying mathematical question is a regular hexagonal prism shortest
surface geodesic problem (see, e.g., the classical theorem that the shortest
path between two points on a polyhedral surface unfolds to a straight line in
some flat development of the relevant faces, where one must compare every
candidate unfolding family before declaring a minimum). Some responses commit
to a single unfolding family and assert minimality without comparison; some
invent invalid surface unfoldings whose straight line does not cross the
required shared edge; some appeal to external links instead of an internal
derivation. The bundle contains no response that derives the correct shortest
surface distance for the full problem.
