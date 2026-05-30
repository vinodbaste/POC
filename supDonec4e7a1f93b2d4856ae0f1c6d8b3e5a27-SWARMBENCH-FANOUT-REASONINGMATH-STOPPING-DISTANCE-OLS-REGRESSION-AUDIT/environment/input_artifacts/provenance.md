# Input Provenance

## Real data (`cars.csv`, embedded in `problem.md`)

`cars.csv` contains the 50 paired observations of car `speed` (mph) and stopping
`dist` (feet) from the classic **`cars`** dataset, recorded in the 1920s and
originally published in Ezekiel, M. (1930) *Methods of Correlation Analysis*
(Wiley). It is the `cars` object shipped with the R `datasets` package and is
distributed verbatim on the public Rdatasets mirror:
https://vincentarelbundock.github.io/Rdatasets/csv/datasets/cars.csv
(documentation: https://vincentarelbundock.github.io/Rdatasets/doc/datasets/cars.html).

All 50 `speed,dist` pairs are unchanged from the public release (column sums
Sum(speed) = 770 and Sum(dist) = 2149 match the published means 15.4 and 42.98).

## Proposed solutions (`proposed_solutions/response_A.md` ... `response_L.md`)

These twelve files are raw AI-generated candidate solutions to the regression in
`problem.md`. They are intentionally heterogeneous: verbose prose, partial
working, and statistically flawed methods (axis swaps, correlation-vs-slope
confusion, regression through the origin, wrong CI quantiles, dropped points) are
all part of the artifact being evaluated. They are not answer keys, they are not
all correct, and they do not contain the oracle labels. The task being modeled is
professional AI-output evaluation: independently fitting the regression, then
auditing each model-generated solution for concrete statistical failures.
