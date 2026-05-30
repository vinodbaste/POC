# Justification: oracle, decomposition, and the single-vs-multi gap

## Gold answer
OLS slope `beta1 = 3.93` ft/mph (gold_slope_x1000 = 3932), 95% CI
**[3.10, 4.77]** (supporting: intercept -17.58, residual SE 15.38 on 48 df,
R^2 = 0.651). Derived from the real 50-point `cars` data; see `derivation.md`
and `compute_gold_stats.py`. Reproduces the standard `lm(dist ~ speed)` fit.

## Failure-code catalogue
- F1 — wrong regression direction (regressed speed on dist; divides Sxy by Syy).
- F2 — reported the correlation r (or R^2) as the slope.
- F3 — regression forced through the origin (no intercept).
- F4 — wrong CI quantile: normal 1.96 used instead of t*(n-2).
- F5 — dropped or excluded data points (n != 50).
- F6 — arithmetic slip: a computational error in a reported sum/coefficient/CI
  bound, NOT explained by a method choice, detectable only by recomputation.

## Per-response audit (oracle)
| Resp | reported slope | correct | failure_reasons | what makes it adversarial |
|------|----------------|---------|-----------------|---------------------------|
| A | 3.93  | true  | []           | clean OLS, correct t-CI |
| B | 3.93  | true  | [F4]         | TRAP: right slope/intercept, CI quietly uses 1.96 (not flagged) -> single drops F4 |
| C | 3.86  | false | [F6]         | TRAP: buried slip sum(xy)=38384 vs 38482 -> near-gold 3.86; number-matcher mismarks correct AND misses F6 |
| D | 0.81  | false | [F2, F4]     | r-as-slope (loud) co-fires with a quiet 1.96 -> single gets F2, drops F4 |
| E | 2.78  | false | [F3, F4, F5] | triple co-fire: through-origin + dropped outliers + 1.96 |
| F | 2.91  | false | [F3]         | through-origin buried as "physical zero intercept"; CI uses correct t |
| G | 3.93  | true  | []           | clean OLS (raw-moment form) |
| H | 3.93  | true  | []           | REFUTATION TRAP: quotes the F1/F2/F5 triggers only to reject them -> single false-fires |
| I | 3.38  | false | [F5, F6]     | drops 3 outliers (F5) and slips the reduced cross-product (F6) |
| J | 0.166 | false | [F1, F4]     | axis inversion (loud) co-fires with a quiet 1.96 -> single drops F4 |
| K | 3.93  | true  | [F5]         | TRAP: drops one central speed-15 row; slope still 3.93 -> single marks [] |
| L | 0.166 | false | [F1]         | axis inversion alone, correct t-CI |

`acceptable_solution_ids = [A, G, H]` (true AND empty failure_reasons).

## Why a single agent underperforms (this is the gap source)
Per the SwarmBench canonical pattern, the gap comes from adversarial responses,
not scoring layers. Every error here is **unannounced** — candidates present
flawed working as if correct — so the auditor must re-derive each quantity and
the code set. A single agent multiplexing all twelve dense derivations in one
context predictably fails on:
- **Buried, quiet codes (B, J, D have F4; C, I have F6).** The 1.96-vs-t error
  and the cross-product slips carry no flag; under attention dilution the single
  agent marks B as `[]`, mismarks C as correct, and drops F4 on D/J. All-or-
  nothing zeroes each 30-pt block.
- **Co-fires (D=2, E=3, I=2, J=2).** Catching the loud code (F2/F1/F3) but
  missing the quiet co-fire zeroes the response.
- **Near-gold wrong answer (C = 3.86).** Number-matching against its own gold,
  the single agent accepts 3.86 as "correct" and never looks for the slip.
- **Refutation false positive (H).** H quotes the swap/r-as-slope/drop triggers
  to reject them; a single agent fires F1/F2/F5 and loses H.
- **Correct-but-flawed (B, K).** Right slope, real code (F4, F5) -> not
  acceptable; "right number => acceptable" is wrong.

Multi-agent gives each `audit-response-X` sub-agent the full attention budget to
re-derive one response; the synthesizer is mechanical. Focused auditors catch the
buried codes and co-fires and do not false-fire on H, so multi >> single.

## Point budget (Total = 364)
- gold_slope_x1000: 2 (slope x 1000 = 3932, within +/- 1)
- acceptable_solution_ids: 2 (set match)
- per response: 30 x 12 = 360 (all-or-nothing on id + correctness + code SET)

## Sub-agent assignment (fan-out-synthesize, 14 agents)
1 gold-derivation agent + 12 per-response auditors + 1 synthesizer. Each auditor
reads only the problem and its single response; the synthesizer is structural
(sets the gold field, computes acceptable_solution_ids, orders the 12 entries).
