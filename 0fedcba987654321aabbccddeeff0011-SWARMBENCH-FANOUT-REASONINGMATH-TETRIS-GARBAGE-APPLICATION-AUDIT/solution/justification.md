# Oracle Justification

## Correct final board

The correct final board after applying the four garbage lines with hole columns [3, 3, 5, 2] (oldest-first, pushed from below) to the initial 20-by-10 board, with the original content shifted up by four rows and no post-clear rows triggered, is:

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

The initial board has empty rows 0-13 and stack content in rows 14-19. Four garbage lines rise from the bottom of the playfield. By standard rising-garbage mechanics:

1. The existing 20 rows shift up by 4. The top 4 rows of the existing board (rows 0-3) shift past row 0 and are dropped (they were all empty, so nothing meaningful tops out).
2. The original rows 4-19 become new rows 0-15. The first 10 are empty (rows 0-9). Rows 10-15 carry the original stack content from rows 14-19.
3. The four garbage lines occupy new rows 16-19. The oldest garbage (first in the queue, hole at column 3) occupies row 16 (the highest position within the garbage block); the newest garbage (last in the queue, hole at column 2) occupies row 19 (the lowest position).
4. Garbage row at hole column h is the 10-character string with `1` at every column except `0` at column h.
   - Hole at column 3: `1110111111`
   - Hole at column 5: `1111101111`
   - Hole at column 2: `1101111111`
5. Post-clear check: no row in the resulting board is entirely filled with `1`s (every garbage row has a `0` at its hole; every original stack row has at least one `0`), so no rows are cleared.

No response A-F gives this final board exactly, so `acceptable_solution_ids` is the empty list.

## Failure reason code meanings

- `wrong_garbage_insertion_direction` — the response inserts garbage from the wrong side, or overlays garbage without shifting existing content.
- `wrong_hole_column_alignment` — one or more garbage holes are placed at columns other than [3, 3, 5, 2].
- `wrong_garbage_order_or_count` — the wrong number of garbage lines are applied, or applied in the wrong order.
- `wrong_post_shift_topout_handling` — the upward shift uses the wrong row count, leaves stale rows, or mishandles topout.
- `invalid_or_incomplete_final_output` — the committed board is not 20 rows by 10 columns of {0, 1}.

## Per-response audit derivations

### Response A — very-long verbose, correct direction and count, mis-placed hole

Response A correctly identifies that garbage rises from the bottom, correctly shifts existing rows up by four, and correctly applies four garbage lines. However, it places at least one garbage hole at the wrong column (it confuses the column index for one of the garbage lines while working through its trace). The response writes a complete 20-by-10 board with the correct direction and shift, but with at least one row in the garbage block having its `0` at a column other than the specified column for that line. Triggers: `wrong_hole_column_alignment` only.

Oracle `failure_reasons` for A: `["wrong_hole_column_alignment"]`.

### Response B — casual conversational, applies garbage at top

Response B treats garbage as if it falls from the top of the playfield instead of rising from below. It inserts the four garbage lines at the TOP of the board, then says the existing content "falls down" to fill the gap, and the bottom four rows of original content fall off the bottom. The committed final board has garbage rows at the TOP and the original stack content moved DOWN, which is the opposite of the standard rising-garbage mechanic. Triggers: `wrong_garbage_insertion_direction` (insertion from wrong side) and `wrong_post_shift_topout_handling` (shift direction and topout side are both wrong).

Oracle `failure_reasons` for B: `["wrong_garbage_insertion_direction", "wrong_post_shift_topout_handling"]`.

### Response C — JSON-near, miscounts the garbage lines

Response C outputs a JSON-like result with the rising-garbage direction correct and the existing board shifted upward, but applies only three garbage lines instead of four (it appears to drop the middle garbage line or merge two). The final garbage block in the board has three rows, not four, and the existing content has shifted up by three, not four. The hole columns of the three garbage rows that ARE present are correct for their position in the truncated queue. Triggers: `wrong_garbage_order_or_count` only.

Oracle `failure_reasons` for C: `["wrong_garbage_order_or_count"]`.

### Response D — terse paragraph, incomplete output

Response D writes a short prose summary and a partial board representation. The committed board has fewer than 20 rows (it stops after writing 14 rows or so). The response acknowledges the rising-garbage direction qualitatively but does not produce a complete 20-by-10 board. Triggers: `invalid_or_incomplete_final_output` (the committed final board is not a complete 20-row by 10-column grid).

Oracle `failure_reasons` for D: `["invalid_or_incomplete_final_output"]`.

### Response E — markdown step-by-step, correct direction but wrong holes and wrong shift amount

Response E uses markdown step-by-step style and correctly identifies the rising-garbage direction. However, it shifts the existing board up by THREE rows instead of four, and additionally writes garbage rows with at least one wrong hole column. The committed final board has the original stack at the wrong vertical position (off by one) and has at least one garbage row with hole at the wrong column. Triggers: `wrong_hole_column_alignment` (wrong hole placement) and `wrong_post_shift_topout_handling` (shifted by 3 instead of 4).

Oracle `failure_reasons` for E: `["wrong_hole_column_alignment", "wrong_post_shift_topout_handling"]`.

### Response F — friendly chatbot, doesn't shift the existing board

Response F enthusiastically agrees to help, then writes a committed board that has the four garbage rows at the bottom but does NOT shift the existing stack upward. The original rows 14-19 remain at rows 14-19 in the final board, and the garbage is overlaid where rows 16-19 used to be (effectively erasing the bottom four rows of original content). This is the "overlay without shift" variant of insertion-direction error. Triggers: `wrong_garbage_insertion_direction` (no shift).

Oracle `failure_reasons` for F: `["wrong_garbage_insertion_direction"]`.

## Scoring rubric

Total possible weight is **184 points**; reward = `passed / 184` clipped to [0.0, 1.0]. JSON-equality match short-circuits to 1.0.

- `correct_final_board` (20-row exact match): 2 points
- `acceptable_solution_ids` (set match): 2 points
- Each per-response audit (six times, one per response_id A through F): **30 points all-or-nothing**. Awarded only if all three of `response_id`, `final_board_correct`, and the EXACT `failure_reasons` set match the oracle for that response. Any mismatch (extra code, missing code, or both) forfeits the full 30 points. No partial credit.

Total: 2 + 2 + 6 × 30 = 184.
