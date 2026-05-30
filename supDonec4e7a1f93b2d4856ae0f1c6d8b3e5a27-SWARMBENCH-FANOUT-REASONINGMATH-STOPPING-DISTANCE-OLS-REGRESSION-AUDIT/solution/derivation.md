# Derivation

## Data
The real 50-observation `cars` dataset (speed mph, stopping distance ft); see
`environment/input_artifacts/provenance.md`. Column sums Sum(speed) = 770 and
Sum(dist) = 2149 reproduce the published means 15.4 and 42.98.

## OLS estimator (closed form)
```
xbar = 15.4,  ybar = 42.98
Sxx  = sum((x-xbar)^2) = 1370.0
Syy  = sum((y-ybar)^2) = 32538.98
Sxy  = sum((x-xbar)(y-ybar)) = 5387.4
beta1 = Sxy/Sxx = 3.932409          (slope, ft per mph)
beta0 = ybar - beta1*xbar = -17.579 (intercept, ft)
SSE  = sum((y - beta0 - beta1 x)^2) = 11353.52,  df = n-2 = 48
s^2  = SSE/df = 236.53,  s = 15.3796 (residual standard error)
se(beta1) = s/sqrt(Sxx) = 15.3796/37.0135 = 0.41551
t  = beta1/se = 9.464
t*(0.975, 48) = 2.01063
slope 95% CI = beta1 +/- t* se = [3.0968, 4.7680]
R^2 = 1 - SSE/Syy = 0.6511
pearson r = Sxy/sqrt(Sxx*Syy) = 0.8069
```

## Computed gold (full precision in `compute_gold_stats.py`)
- Slope `beta1 ~= 3.9324` ft/mph; **gold_slope_x1000 = 3932**.
- Slope 95% CI `[3.097, 4.768]`.
- Supporting: intercept -17.579, residual SE 15.380 (df 48), R^2 = 0.651.
These reproduce the standard `lm(dist ~ speed)` fit reported for this dataset.

## Wrong-method reference values (the audit codes key on these)
- **F1 reverse regression** (speed on dist): slope `Sxy/Syy = 0.1656`.
- **F2 correlation as slope**: `r = 0.8069` (or `R^2 = 0.651`) reported as beta1.
- **F3 through-origin**: `sum(xy)/sum(x^2) = 38482/13228 = 2.909` (no intercept).
- **F4 normal quantile**: CI with 1.96 instead of t*(48)=2.011 -> `[3.118, 4.746]`
  (still within tolerance of the gold CI, so it does not by itself change
  `final_answer_correct`).

## From gold statistics to the audit oracle
A candidate's `final_answer_correct` is true iff its reported OLS slope is within
+/- 0.03 of 3.932, its reported intercept within +/- 0.3 of -17.58, and its
reported 95% CI bounds each within +/- 0.1 of [3.097, 4.768]. The per-response
failure-code assignments and the point budget are in `justification.md`; the
machine-readable oracle is `oracle.json` (byte-identical to `tests/oracle.json`).

## Reproducing the gold statistics
`solution/compute_gold_stats.py` reads `cars.csv`, performs the closed-form OLS
derivation above using only the Python standard library (the Student-t 0.975
quantile is computed from the regularized incomplete beta function), and prints
all gold and wrong-method reference statistics. It does not write `oracle.json`.
