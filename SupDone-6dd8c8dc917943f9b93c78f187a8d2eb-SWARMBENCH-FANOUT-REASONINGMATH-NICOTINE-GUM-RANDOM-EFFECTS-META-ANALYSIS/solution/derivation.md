# Derivation

## Data
26 randomized nicotine-gum smoking-cessation trials, each a 2x2 table of
quitters/total in the treatment and control arms (the real HSAUR `smoking`
dataset; see `environment/input_artifacts/provenance.md`). For trial `i`:

```
a = qt        b = tt - qt        c = qc        d = tc - qc
```

All 26 tables have strictly positive cells, so no continuity correction is used.

## Per-study statistics
- Odds ratio: `OR_i = (a*d)/(b*c)`; `y_i = ln(OR_i)`.
- Large-sample log-OR variance (Woolf): `v_i = 1/a + 1/b + 1/c + 1/d`.
- `se_i = sqrt(v_i)`, inverse-variance weight `w_i = 1/v_i`.
- Wald statistic `z_i = y_i/se_i`, two-sided `p_i = 2(1 - Phi(|z_i|))`.

## Fixed-effect (inverse-variance) pool
```
y_FE = sum(w_i y_i) / sum(w_i)
se_FE = sqrt(1 / sum(w_i))
OR_FE = exp(y_FE),  95% CI = exp(y_FE +/- 1.96 se_FE)
```

## Heterogeneity
```
Q   = sum(w_i (y_i - y_FE)^2),   df = k - 1 = 25
p_Q = P(chi^2_25 > Q)            (upper-tail chi-square)
I^2 = max(0, (Q - df)/Q) * 100
C   = sum(w_i) - sum(w_i^2)/sum(w_i)
tau^2 = max(0, (Q - df)/C)       (DerSimonian-Laird moment estimator)
```

## Random-effects (DerSimonian-Laird) pool
```
w*_i = 1/(v_i + tau^2)
y_RE = sum(w*_i y_i)/sum(w*_i),  se_RE = sqrt(1/sum(w*_i))
OR_RE = exp(y_RE),  95% CI = exp(y_RE +/- 1.96 se_RE)
```

## Computed gold (rounded to 6 dp; full values in `oracle.json`)
- Fixed-effect pooled OR ~= 1.6515, 95% CI [1.4499, 1.8812].
- Random-effects pooled OR ~= 1.7514, 95% CI [1.4831, 2.0683].
- Q ~= 34.874 (df = 25, p ~= 0.0905), I^2 ~= 28.31%, tau^2 ~= 0.0474.
- 9 of 26 trials are individually significant at the 0.05 level.
- Largest fixed-effect weight: Killen90; largest OR: Huber88; smallest OR: Hall96.

These reproduce the published analyses of this dataset (e.g., the HSAUR text and
the `rmeta`/`metafor` packages report fixed-effect OR ~= 1.65, random-effects
OR ~= 1.75, and I^2 ~= 28%), which validates the oracle.

## From gold statistics to the audit oracle

This task is a derivation+audit: the gold statistics above are the ground truth
against which the twelve AI-generated candidate solutions are audited. The headline
gold is the random-effects pooled OR = 1.75 with 95% CI [1.48, 2.07]. A candidate's
`final_answer_correct` is true iff its reported random-effects OR is within +/- 0.03
of 1.75 and its CI bounds within +/- 0.05 of [1.48, 2.07].

The per-response failure-code assignments and the full point budget are documented
in `justification.md`; the machine-readable oracle is `oracle.json` (identical to
`tests/oracle.json`).

## Reproducing the gold statistics
`solution/compute_gold_stats.py` reads `trials.csv`, performs the closed-form
derivation above with only the Python standard library (the chi-square upper tail
uses the regularized upper incomplete gamma function), and prints all gold
statistics. It does not write `oracle.json` (that file is the audit oracle).
