# Provenance

## Dataset
The numbers in `insect_sprays.csv` are the classic **InsectSprays** dataset: counts
of insects surviving on agricultural experimental units treated with one of six
insecticides, 12 replicates each (72 observations, 6 groups). The data originates
from Beall, G. (1942), "The transformation of data from entomological field
experiments", *Biometrika* 29, 243–262, and is distributed as a built-in dataset in
the R statistical environment (`datasets::InsectSprays`). The values here are copied
verbatim from that public release; no rows were added, edited, or removed.

Public reference: https://vincentarelbundock.github.io/Rdatasets/doc/datasets/InsectSprays.html

## The candidate solutions
The **twelve** files under `proposed_solutions/` (`response_A.md` ...
`response_L.md`) are raw, unedited transcripts produced by weaker AI assistants
that were each independently handed `problem.md` and asked to carry out the
one-way ANOVA and report the F statistic with its degrees of freedom. They were
collected as-is for quality review.

They are an uncurated mix:
- some carry out the analysis correctly;
- some commit a methodological error (wrong degrees of freedom, treating sums of
  squares as the statistic, substituting a two-group t-test for the omnibus F,
  silently dropping a group, etc.);
- some reach a plausible-looking number through a buried arithmetic slip;
- some state the correct final statistic while still mishandling a reported
  intermediate quantity.

No answer key, score, or grading annotation is attached to any response. Each must
be judged on its own internal mathematics, recomputed from the data above.
