# Justification: gold derivation, oracle labels, and the multi-agent gap

## 1. Gold regression (all 30 rows of `attitude.csv`)

Closed-form OLS of `rating` on `complaints`, derived independently in
`compute_gold_stats.py` (standard library only; the Student-t quantile comes from
an inverse regularized incomplete beta):

| quantity | value |
|---|---|
| n | 30 |
| x̄ (complaints), ȳ (rating) | 66.600, 64.633 |
| Sxx, Syy, Sxy | 5141.200, 4296.967, 3879.600 |
| slope β₁ = Sxy/Sxx | **0.75461** |
| intercept β₀ | 14.376 |
| residual SE s (df = 28) | 6.993 |
| se(β₁) | 0.09753 |
| t*(0.975, 28) | 2.0484 |
| 95% CI for β₁ | **[0.5548, 0.9544]** |
| R² | 0.6813 |
| Pearson r | 0.8254 |

Headline: **`gold_slope_x1000 = 755`**, `acceptable_solution_ids = [A, G, H]`.

## 2. Failure-code taxonomy and the wrong-method signatures

| code | error | signature value |
|---|---|---|
| F1 | axes reversed (Sxy/Syy, regress complaints on rating) | slope → 0.9029 |
| F2 | correlation/R² reported as the slope | 0.8254 / 0.6813 |
| F3 | regression forced through the origin (Σxy/Σx²) | 0.9624 |
| F4 | 95% CI built with normal 1.96 instead of t*(0.975,28) | CI → [0.5634, 0.9458] |
| F5 | rows discarded (n ≠ 30) | fit on < 30 points |
| F6 | arithmetic slip in a reported quantity, not explained by F1–F5 | — |

`final_answer_correct` is the conjunction of three numeric gates: slope within
±0.03, intercept within ±0.3, and both CI endpoints within ±0.1 of gold. F4 and
F5 do not by themselves force `false` — a write-up can carry the right slope and
still mis-build its CI (B) or drop a single redundant row yet stay in tolerance
(K).

## 3. Per-response labels (oracle)

| id | slope | final | codes | rationale |
|---|---|---|---|---|
| A | 0.755 | true | [] | clean full-data OLS, t-based CI |
| B | 0.755 | true | [F4] | correct slope/intercept but CI uses 1.96 |
| C | 0.696 | false | [F6] | Sxy mis-stated as 3579.6 (true 3879.6) |
| D | 0.825 | false | [F2, F4] | reports r as slope, CI with 1.96 |
| E | 0.958 | false | [F3, F4, F5] | drops 2 "outliers", forces origin, 1.96 CI |
| F | 0.962 | false | [F3] | through-origin on all 30 rows |
| G | 0.755 | true | [] | clean; names and rejects axis-swap and r-as-slope |
| H | 0.755 | true | [] | clean full-data OLS |
| I | 0.800 | false | [F5, F6] | drops 2 high-x rows (n=28) and mis-states R²=0.79 (true 0.682) |
| J | 0.903 | false | [F1, F4] | Sxy/Syy axis swap, CI with 1.96 |
| K | 0.755 | true | [F5] | drops 1 redundant row (n=29); fit stays within all tolerances |
| L | 0.903 | false | [F1] | Sxy/Syy axis swap, t-based CI |

Every flawed write-up is internally arithmetic-consistent with its own (wrong)
method, so a defect can only be confirmed by re-deriving the estimator, not by
spotting an inconsistency on the page.

## 4. Why fan-out beats a single agent here

- **Refutation bait (G, and the "tempting shortcut" prose in A).** Mentioning then
  rejecting the axis swap and r-as-slope does NOT fire F1/F2. A single agent
  juggling twelve write-ups tends to false-fire these codes on the clean responses;
  an auditor focused on one write-up reads the rejection correctly.
- **Co-firing density (D, E, I, J).** Several responses carry two-to-three codes at
  once. All-or-nothing scoring means a single dropped co-fire zeroes a 30-point
  block. Isolated auditors enumerate the full set; a single agent amortising
  attention across twelve audits routinely drops one.
- **Decision-preserving defects (B, K).** Both reach the right slope yet still carry
  a code (F4; F5). A single agent that anchors on "the number is right" misses the
  buried defect; a dedicated auditor re-checks the CI multiplier and the row count.
- **Popular-wrong-value drift (C, I).** The F6 slips (mis-stated Sxy; mis-stated
  R²) are only caught by redoing that response's own arithmetic. A single agent
  reusing a cached gold derivation overlooks response-local slips; per-response
  auditors recompute from scratch.

The synthesizer performs no mathematics — it orders A..L, copies verdicts, and
derives `acceptable_solution_ids` — so the multi-agent advantage comes entirely
from isolating the twelve proof obligations.
