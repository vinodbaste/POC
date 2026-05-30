# Provenance

## Dataset
The numbers in `plant_growth.csv` are the classic **PlantGrowth** dataset: dried
plant weights under a control condition and two treatments, 10 replicates each
(30 observations, 3 groups). The data originates from Dobson, A. J. (1983), *An
Introduction to Statistical Modelling*, and is distributed as a built-in dataset
in the R statistical environment (`datasets::PlantGrowth`). The values here are
copied verbatim from that public release; no rows were added, edited, or removed.

Public reference: https://vincentarelbundock.github.io/Rdatasets/doc/datasets/PlantGrowth.html

## The candidate solutions
The twelve... — correction: the **ten** files under `proposed_solutions/`
(`response_A.md` ... `response_J.md`) are raw, unedited transcripts produced by
weaker AI assistants that were each independently handed `problem.md` and asked
to carry out the one-way ANOVA and report the F statistic with its degrees of
freedom. They were collected as-is for quality review.

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
