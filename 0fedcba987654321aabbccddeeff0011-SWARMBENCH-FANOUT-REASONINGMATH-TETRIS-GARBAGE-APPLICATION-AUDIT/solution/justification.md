# Oracle Justification

## Correct final board

The correct final board after applying the four garbage lines with hole columns [3, 3, 5, 2] (oldest-first, pushed from below) to the initial 20-by-10 board, with original content shifted up by four rows and no post-clear rows triggered, is:

```
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000010000
0001011000
0011111000
1011111110
1111111110
1111111110
1110111111
1110111111
1111101111
1101111111
```

## Derivation

Initial board: empty rows 0-13 plus stack content at rows 14-19. Four garbage lines rise from the bottom of the playfield. Standard rising-garbage mechanics:

1. Existing 20 rows shift up by 4. Top 4 rows (originally empty) shift past row 0 and are dropped.
2. Original rows 4-19 become new rows 0-15. New rows 0-9 are empty (from original rows 4-13). New rows 10-15 carry the original stack content (from original rows 14-19).
3. Four garbage lines occupy new rows 16-19. Oldest garbage (hole=3) goes at row 16; newest (hole=2) goes at row 19.
4. Garbage row strings (10-char, `0` at hole column):
   - Hole 3: `1110111111`
   - Hole 5: `1111101111`
   - Hole 2: `1101111111`
5. Post-clear check: no row is entirely filled with `1` (every garbage row has its hole, every original stack row has at least one `0`). No clears trigger.

## Acceptable solutions

Response F's committed final board matches the gold board exactly. Therefore `acceptable_solution_ids = ["F"]`. No other response's final board matches the gold.

## Failure reason code meanings

- `wrong_garbage_insertion_direction` — the response inserts garbage from the wrong side, or fails to actually insert garbage / fails to shift existing content.
- `wrong_hole_column_alignment` — one or more garbage holes are placed at columns other than [3, 3, 5, 2].
- `wrong_garbage_order_or_count` — wrong number of garbage lines applied, or applied in the wrong order.
- `wrong_post_shift_topout_handling` — incorrect upward shift amount, stale rows left in place, mishandled topout, or spurious post-application row clears.
- `invalid_or_incomplete_final_output` — committed board is not a complete 20-row by 10-column grid of {0, 1}.

## Per-response audit derivations

### Response A — very-long verbose, off-by-one shift

Response A walks through the derivation in detail and writes the four garbage rows with **correct** holes at columns [3, 3, 5, 2] at rows 16-19. However, its committed final board shifts existing content up by only **three** rows instead of four: the original stack appears at rows 11-15 instead of the correct rows 10-15, and there are eleven empty rows at the top instead of ten. Specifically:

- A's new row 10 is `0000000000`; gold's row 10 is `0000010000` (original row 14).
- A's new row 11-15 carry original rows 14-18; gold's rows 10-15 carry original rows 14-19.
- The garbage block at rows 16-19 is correctly placed and has correct holes.

The garbage count, direction, hole columns, and output shape are all correct. The single defect is the shift amount: rows shifted up by 3 instead of 4. Triggers: `wrong_post_shift_topout_handling`.

Oracle `failure_reasons` for A: `["wrong_post_shift_topout_handling"]`.

### Response B — wrong hole patterns + over-shift + phantom clears

Response B applies four garbage rows but writes each with the same wrong pattern `1111101111` (which is hole at column 5, not at columns [3, 3, 5, 2]). It then over-shifts: the four garbage rows end up at rows 4-7 (not the bottom) and the original stack ends up at rows 8-11. B then "clears" rows 12 and 13 (which were original rows 18 and 19, value `1111111110`) on the false claim that they are full — they have `0` at column 9 and are NOT full. The bottom eight rows of B's committed board are all empty.

Triggers:
- `wrong_hole_column_alignment` — all four garbage rows use the wrong hole pattern (col 5 instead of [3, 3, 5, 2]).
- `wrong_post_shift_topout_handling` — over-shift (effective shift of 6, not 4) places garbage in the middle rather than the bottom, plus spurious clears that wipe valid stack rows.

Oracle `failure_reasons` for B: `["wrong_hole_column_alignment", "wrong_post_shift_topout_handling"]`.

### Response C — never actually inserts garbage + phantom clears

Response C interprets "apply garbage" by zeroing out row 19 at each step rather than inserting a garbage row. After all four steps the board is essentially identical to the initial state except row 19 is now empty. C then claims fifteen rows are "completely filled" and clears them all, leaving an entirely empty board.

Triggers:
- `wrong_garbage_insertion_direction` — garbage is never actually inserted at the bottom; C treats application as "zero out row 19".
- `wrong_post_shift_topout_handling` — phantom clears of fifteen rows that are not full.

Oracle `failure_reasons` for C: `["wrong_garbage_insertion_direction", "wrong_post_shift_topout_handling"]`.

### Response D — committed final board is only 10 rows

Response D writes a multi-step prose-and-board reasoning that ends with a "Final Answer" block containing only **ten** rows of digits (rather than the required twenty). The committed final board is not a complete 20-by-10 grid.

Trigger: `invalid_or_incomplete_final_output` (committed board has only 10 rows).

Oracle `failure_reasons` for D: `["invalid_or_incomplete_final_output"]`.

### Response E — wrong hole patterns + wrong placement + phantom clears

Response E uses wrong hole patterns: it writes `1111110111` for "hole at column 3" (actually hole at column 6), `1111101111` for "hole at column 5" (correct by coincidence), and `1111111011` for "hole at column 2" (actually hole at column 8). It then places these four garbage rows at rows 10-13 (in the middle of the playfield, not at the bottom), then claims rows 8-10 are full and clears them. The final board has the three rows of the original stack at positions 8-10 and is otherwise empty — no garbage rows in the final board.

Triggers:
- `wrong_garbage_insertion_direction` — garbage placed in middle of board (rows 10-13) rather than rising from bottom (rows 16-19).
- `wrong_hole_column_alignment` — three of four hole patterns are wrong (columns 6, 6, 5, 8 instead of 3, 3, 5, 2).
- `wrong_post_shift_topout_handling` — phantom clears of rows that are not actually full.

Oracle `failure_reasons` for E: `["wrong_garbage_insertion_direction", "wrong_hole_column_alignment", "wrong_post_shift_topout_handling"]`.

### Response F — exact match to gold board

Response F's committed final board matches the gold board exactly, row by row. It correctly applies the four garbage lines (oldest-first from the bottom), correctly shifts existing content up by 4, correctly uses hole columns [3, 3, 5, 2], and correctly determines that no post-application clears trigger. `final_board_correct = true` and `failure_reasons = []`. Response F is the unique acceptable solution.

Oracle `failure_reasons` for F: `[]`. Oracle `final_board_correct` for F: `true`.

## Scoring rubric

Total possible weight is **184 points**; reward = `passed / 184` clipped to [0.0, 1.0]. JSON-equality match short-circuits to 1.0.

- `correct_final_board` (20-row exact match): 2 points
- `acceptable_solution_ids` (set match, oracle = `["F"]`): 2 points
- Each per-response audit (six times): **30 points all-or-nothing**. Awarded only if `response_id`, `final_board_correct`, and the EXACT `failure_reasons` set all match the oracle. Any mismatch (extra code, missing code, or both) forfeits all 30 points for that response.

Total: 2 + 2 + 6 × 30 = 184.
