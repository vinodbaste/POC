# Justification: oracle, decomposition, and the single-vs-multi gap

## Gold answer
Random-effects (DerSimonian-Laird) pooled odds ratio = **1.75**, 95% CI
**[1.48, 2.07]** (supporting: fixed-effect OR = 1.65, Q = 34.87 on 25 df,
I^2 = 28.3%, tau^2 = 0.047). Derived from the real 26-trial data; see
`derivation.md` and `compute_gold_stats.py`. This reproduces the published HSAUR /
`rmeta` / `metafor` analyses of this dataset.

## Failure-code catalogue
- F1 — inverse-variance weighting error (weights not `1/v`).
- F2 — wrong deliverable: fixed-effect reported instead of random-effects.
- F3 — naive averaging of the raw odds ratios.
- F4 — heterogeneity computation error (wrong Q/I^2/tau^2 formula).
- F5 — data/2x2 table error (dropped or mis-constructed trials).

## Per-response audit (oracle)
| Resp | reported RE OR | final_answer_correct | failure_reasons | rationale |
|------|----------------|----------------------|-----------------|-----------|
| A | 1.75 | true  | []            | clean DL random-effects |
| B | 1.79 | false | [F1]          | weights by 1/se (stated mid-derivation, not flagged) |
| C | 1.65 | false | [F2]          | claims random-effects but reports exp(y_FE)=1.65, the fixed-effect line |
| D | 1.75 | true  | [F4]          | TRAP: tau^2=(Q-df)/sum(w) not /C; answer still rounds to 1.75 |
| E | 1.87 | false | [F1, F4, F5]  | triple: drops 2 trials + weights 1/se + tau^2=(Q-df)/k |
| F | 2.14 | false | [F3]          | reports the mean of the 26 odds ratios as the summary |
| G | 1.75 | true  | []            | clean DL random-effects (computational-form Q) |
| H | 1.75 | true  | []            | TRAP: names 1/se, averaging, dropping Killen90 only to reject all three |
| I | 1.61 | false | [F5]          | mis-reads Jensen91 & Garvey00 (arms swapped) |
| J | 1.65 | false | [F2, F4]      | reports fixed-effect AND I^2 = Q/df = 139.5% |
| K | 1.76 | true  | [F5]          | TRAP: drops smallest trial Schneider85 (25 trials); answer still ~1.75 |
| L | 1.70 | false | [F1]          | weights by sample size n (near-miss, must compute to reject) |

`acceptable_solution_ids = [A, G, H]` (true AND empty failure_reasons).

Adversarial features that defeat a single agent's shortcuts:
- **Correct-answer-but-flawed-method (D, K):** report ~1.75 yet carry a real F-code, so
  "right number => no errors / acceptable" is wrong. These are NOT acceptable.
- **False-positive trap (H):** quotes the F1/F3/F5 triggers only to reject them; the
  codes must NOT fire. It IS acceptable.
- **Co-fires (E = F1+F4+F5 triple, J = F2+F4):** attention dilution makes single agents
  catch only some codes; all-or-nothing zeroes the block.
- **Disguised line error (C):** does correct intermediate work but reports the
  fixed-effect value, so it must be read carefully, not number-matched.
- **Near-miss (L = 1.70):** only 0.05 from gold; requires actually recomputing.
- **Buried, unflagged errors (B, F, I, L):** no self-labeling of the mistake.

## Point budget (Total = 364)
- gold_random_effects_or_x100: 2 (integer OR x 100 = 175, within +/- 1)
- acceptable_solution_ids: 2 (set match)
- per response: 30 x 12 = 360 (all-or-nothing on id + correctness + code SET)

## Sub-agent assignment (fan-out-synthesize, 14 agents)
1 gold-derivation agent + 12 per-response auditors + 1 synthesizer. Each auditor
reads only the problem and its single response; the synthesizer is purely structural
(sets gold fields, computes acceptable_solution_ids, orders the 12 entries).

## Why a single agent underperforms
- **Majority drift on the gold.** Most candidates that *report* a number cluster near
  1.75-1.86; a single agent skimming all twelve can anchor on a wrong but common value.
- **Co-fire dropping.** H and I each need two codes; all-or-nothing zeroes the 30-pt
  block if either code is missed.
- **Refutation false positive.** J quotes the naive-averaging trigger to reject it; a
  single agent under attention pressure fires F3 and loses J's 30 points.
- **Subtle near-misses.** C (1.79) is only 0.04 from the gold; deciding it is wrong
  requires actually reproducing the inverse-variance pool, not eyeballing.

Multi-agent gives each auditor the full attention budget, so co-fires, refutation
traps, and near-misses are handled correctly.
