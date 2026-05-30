# Input Provenance

## Real trial data (`trials.csv`, embedded in `problem.md`)

`trials.csv` contains the raw 2x2 outcome counts from 26 randomized controlled
trials of nicotine gum for smoking cessation. Each row is one published trial:
`qt`/`tt` are quitters/total in the nicotine-gum (treatment) arm and `qc`/`tc` are
quitters/total in the control arm.

This is the real, publicly distributed `smoking` meta-analysis dataset shipped with
the **HSAUR** R package ("A Handbook of Statistical Analyses Using R", Everitt &
Hothorn), drawn from the Cochrane review of nicotine-gum smoking-cessation trials
(Silagy et al.). It was downloaded verbatim from the public Rdatasets mirror:
https://vincentarelbundock.github.io/Rdatasets/csv/HSAUR/smoking.csv
(documentation: https://vincentarelbundock.github.io/Rdatasets/doc/HSAUR/smoking.html).
The only edit is renaming the unlabeled first column to `study`; all 26 trial ids
and `qt,tt,qc,tc` counts are unchanged.

## Proposed solutions (`proposed_solutions/response_A.md` ... `response_L.md`)

These twelve files are raw AI-generated candidate solutions to the meta-analysis in
`problem.md`. They are intentionally heterogeneous: verbose prose, partial working,
and statistically flawed methods are all part of the artifact being evaluated. They
are not answer keys, they are not all correct, and they do not contain the oracle
labels. The task being modeled is professional AI-output evaluation: independently
solving the meta-analysis, then auditing each model-generated solution for concrete
statistical failures.
