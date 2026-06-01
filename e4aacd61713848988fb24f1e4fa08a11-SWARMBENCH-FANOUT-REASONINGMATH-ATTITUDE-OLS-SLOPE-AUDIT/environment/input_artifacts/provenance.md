# Input Provenance

## Real data (`attitude.csv`, embedded in `problem.md`)

`attitude.csv` contains the 30 paired observations of `complaints` (aggregated
employee score for how a department handles complaints) and `rating` (overall
approval rating) drawn from the classic **`attitude`** dataset — a survey of
clerical employees in a large financial organisation, from Chatterjee, S. and
Price, B. (1977) *Regression Analysis by Example* (Wiley). It is the `attitude`
object shipped with the R `datasets` package and is distributed verbatim on the
public Rdatasets mirror:
https://vincentarelbundock.github.io/Rdatasets/csv/datasets/attitude.csv
(documentation: https://vincentarelbundock.github.io/Rdatasets/doc/datasets/attitude.html).

Only the two columns used by this regression (`rating`, `complaints`) are
retained; the values are unchanged from the public release (column sums
Sum(complaints) = 1998 and Sum(rating) = 1939 match the published means 66.6 and
64.633).

## Proposed solutions (`proposed_solutions/response_A.md` ... `response_L.md`)

These twelve files are raw AI-generated candidate solutions to the regression in
`problem.md`. They are intentionally heterogeneous: verbose prose, partial
working, and statistically flawed methods (axis swaps, correlation-vs-slope
confusion, regression through the origin, wrong CI quantiles, dropped points) are
all part of the artifact being evaluated. They are not answer keys, they are not
all correct, and they do not contain the oracle labels. The task being modeled is
professional AI-output evaluation: independently fitting the regression, then
auditing each model-generated solution for concrete statistical failures.
