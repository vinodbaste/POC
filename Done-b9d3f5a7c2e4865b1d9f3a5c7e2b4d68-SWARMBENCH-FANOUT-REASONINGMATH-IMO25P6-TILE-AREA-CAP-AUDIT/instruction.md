# Forensic-audit brief: modified IMO 2025 P6 tile-area-cap problem

You are a combinatorial-geometry forensic reviewer. Two independent investigations are required, and both must complete before the file is closed:

| Investigation | Question | Output field |
|---------------|----------|--------------|
| Primary derivation | What is the smallest number of axis-aligned rectangular tiles, each of area at most 3, that *exactly partitions* the 4 × 4 grid? | `answer.minimum_tiles` |
| Forensic audit | For each of the sixteen submitted derivations, did its final tile count match the truth, and which of five named proof-error modes does its prose exhibit? | `per_response_assessment[*]` |

Working directory `/workspace`. Inputs live under `/input_artifacts/`:

- `/input_artifacts/problem.md` — the modified problem (4 × 4 grid, area cap 3, exact partition).
- `/input_artifacts/provenance.md` — note on how the proposed derivations were collected.
- `/input_artifacts/proposed_solutions/response_A.md` … `response_P.md` — sixteen raw, unedited proposed derivations under audit.

## Investigation A — derive the truth

Solve the modified problem from first principles. Do **not** read any of the proposed derivations until the gold value is locked. Report a single nonneg integer at `answer.minimum_tiles`.

As cross-checks, also report `minimum_tiles` for five anchor n × n grids under the same area-≤-3 partition rule:

| Anchor key | Grid | Cells |
|------------|------|-------|
| `anchor_2x2` | 2 × 2 | 4 |
| `anchor_3x3` | 3 × 3 | 9 |
| `anchor_5x5` | 5 × 5 | 25 |
| `anchor_6x6` | 6 × 6 | 36 |
| `anchor_8x8` | 8 × 8 | 64 |

Each anchor is graded for exact integer equality.

## Investigation B — audit the sixteen derivations

For every `response_X.md` (X ∈ {A, …, P}) produce one record:

```json
{"response_id": "X", "final_answer_correct": <bool>, "failure_reasons": [<F-codes>]}
```

`final_answer_correct` is `true` iff the response's final stated `minimum_tiles` integer equals the gold value from Investigation A. No tolerance, no near-miss credit.

`failure_reasons` is the (possibly empty) subset of {F1, F2, F3, F4, F5} whose phrase trigger is concretely present in *that single* response's prose. The five forensic codes are:

### F1 — POSITIVE_USE_OF_FORBIDDEN_AREA_TILE
Trigger phrase: the response's enumerated partition lists at least one tile of area greater than 3 — concrete literal forms include `2x2 tile`, `2 x 2 tile`, `1x4 tile`, `1 x 4 tile`, `1x5 tile`, `4x4 tile`, `2x3 tile`, `3x3 tile` — used as a **positive** construction step, *not* inside a passage being explicitly retracted by the response.

### F2 — FLOOR_ROUNDED_LOWER_BOUND
Trigger phrase: the response writes the count-bound as `16 / 3 = 5.33 -> 5` (floor / round-down) **or** asserts `5 tiles is enough` / `minimum is 5` / `the lower bound is 5` as a load-bearing claim. A response whose final `minimum_tiles` is literally 5 fires F2 only when the floor / round-down phrasing is also present (or a 5-is-sufficient assertion that survives to the conclusion).

### F3 — WRONG_TOTAL_CELL_COUNT
Trigger phrase: the response states the total number of unit squares in the 4 × 4 grid as anything other than 16 — concrete literal forms include `12 cells`, `12 unit squares`, `20 cells`, `25 cells`, `4 x 5 = 20`, `4 x 4 = 12`, `8 cells`. If the response gives 16 (or `4*4 = 16`), this code does not fire.

### F4 — INCOMPLETE_PARTITION
Trigger phrase: the response's construction *explicitly acknowledges* one or more unit squares is left uncovered — concrete literal forms include `leaves N cells uncovered`, `1 cell left over`, `the remaining cells are not covered`, `column 4 is empty`, `not going to count those`, `covered 12 cells`, `covered 9 cells`. The phrase MUST refer to the response's own final / claimed partition, not to an alternative being argued against.

### F5 — NON_RECTANGULAR_TILE_USED
Trigger phrase: the response's construction *explicitly* uses a tile shape that is not an axis-aligned rectangle — concrete literal forms include `L-shaped tile`, `L-tromino`, `L tromino`, `T-tetromino`, `triangular tile`, `diagonal tile`, `non-rectangular`. The phrase MUST be present as a positive construction step.

## Adjudication conventions

1. **Multi-select.** Codes F1 through F5 are *not* mutually exclusive. Most responses fire 0, 1, or 2 codes, but co-fires of 2 or even 3 codes do occur and must be reported in full. Use `[]` (empty list) iff none of the five triggers fires.

2. **Refutation carve-out.** A code does NOT fire if the trigger phrase appears *only* inside a passage where the response is identifying it as an error (e.g., "I might be tempted to use a 2x2 tile here — but that has area 4, which is too big, so I will not"). The phrase must remain load-bearing for the response's stated conclusion.

3. **Independence from voting.** Do not infer the gold answer from majority vote across the proposed responses. Investigation A is independent of Investigation B; if the two halves disagree, Investigation A wins.

4. **Acceptability.** A response is added to `acceptable_solution_ids` iff `final_answer_correct = true` AND `failure_reasons = []`. Report `acceptable_solution_ids` as a sorted, uppercase list of letters.

## Verification & scoring

The verifier `/tests/judge.py` reads your `/logs/agent/output.json`, compares each field to the privately held oracle at `/tests/oracle.json`, and writes `reward = passed / 600` clamped to `[0, 1]`. Fail-closes to `0.0` on any IO / JSON error.

| Field | Points |
|-------|--------|
| `answer.minimum_tiles` | 80 (exact integer match, all-or-nothing) |
| Each of 5 anchors (`anchor_2x2`..`anchor_8x8`) | 6 each, 30 total |
| `acceptable_solution_ids` | 10 (set equality, all-or-nothing) |
| Each of 16 per-response audits | 30 each, 480 total (all-or-nothing per response: `response_id` AND `final_answer_correct` AND `set(failure_reasons)` must match the oracle) |
| **Total** | **600** |

## Output schema

Write the final JSON to `/logs/agent/output.json`. The four top-level keys must be exactly `answer`, `anchor_results`, `acceptable_solution_ids`, `per_response_assessment` — no extras.

```
{
  "answer": {
    "minimum_tiles": <nonneg integer>
  },
  "anchor_results": {
    "anchor_2x2": <nonneg integer>,
    "anchor_3x3": <nonneg integer>,
    "anchor_5x5": <nonneg integer>,
    "anchor_6x6": <nonneg integer>,
    "anchor_8x8": <nonneg integer>
  },
  "acceptable_solution_ids": ["<sorted uppercase letters>"],
  "per_response_assessment": [
    {"response_id": "A", "final_answer_correct": <bool>, "failure_reasons": [<codes from F1..F5>]},
    ...
    {"response_id": "P", "final_answer_correct": <bool>, "failure_reasons": [...]}
  ]
}
```

`per_response_assessment` must contain exactly sixteen records in alphabetical order A through P. Do not write anything else to the file.
