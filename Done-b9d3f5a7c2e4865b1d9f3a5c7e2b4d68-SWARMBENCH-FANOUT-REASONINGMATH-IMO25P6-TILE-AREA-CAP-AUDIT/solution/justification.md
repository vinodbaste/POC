# Oracle justification

## Gold answer for 4 × 4

Lower bound. The 4 × 4 grid has 16 cells. Each tile has area at most 3. So the number of tiles needed to cover all 16 cells exactly is at least ⌈16 / 3⌉ = 6.

Upper bound (construction with 6 tiles): partition into a 3 × 4 sub-grid (rows 1-3) plus a 1 × 4 sub-grid (row 4). The 3 × 4 is tiled by four vertical 3 × 1 strips (one per column) — four tiles of area 3. The 1 × 4 is tiled by two horizontal 1 × 2 dominoes — two tiles of area 2. Total 6 tiles, all area ≤ 3, partition is valid.

So `minimum_tiles = 6`.

## Anchors

Same lower-bound argument: for an n × n grid, `minimum_tiles ≥ ⌈n² / 3⌉`. Achievability for each:

- 2 × 2 (4 cells): two 1 × 2 dominoes ⇒ 2 tiles. Lower bound ⌈4/3⌉ = 2.
- 3 × 3 (9 cells): three horizontal 1 × 3 strips, one per row ⇒ 3 tiles. Lower bound ⌈9/3⌉ = 3.
- 5 × 5 (25 cells): decompose 5 × 5 into a 3 × 3 (3 horizontal 1×3) + a 3 × 2 (2 vertical 3×1) + a 2 × 3 (2 horizontal 1×3) + a 2 × 2 (2 dominoes) = 3 + 2 + 2 + 2 = 9 tiles. Lower bound ⌈25/3⌉ = 9.
- 6 × 6 (36 cells): twelve 1 × 3 strips (six rows × two per row) ⇒ 12 tiles. Lower bound 12.
- 8 × 8 (64 cells): two 3-column strips (each tiled by 8 horizontal 1×3 = 16 tiles) + a 2-column strip (8 × 2 = 16 cells, tiled by 6 tiles: 4 vertical 3×1 + 2 vertical 2×1) ⇒ 16 + 6 = 22 tiles. Lower bound ⌈64/3⌉ = 22.

## Audit assignments

Each response read once for the five phrase triggers F1–F5 defined in instruction.md. Final stated `minimum_tiles` is the dispositive value for `final_answer_correct`.

| ID | Stated | F1 (area>3)? | F2 (floor)? | F3 (cells≠16)? | F4 (incomplete)? | F5 (non-rect)? |
|----|--------|--------------|-------------|----------------|------------------|-----------------|
| A | 4 | yes (2x2) | no | no | no | no |
| B | 6 | no | no | no | no | no |
| C | 5 | no | yes (5.33→5) | no | yes (1 cell left) | no |
| D | 7 | no | no | yes (20) | no | no |
| E | 4 | no | no | no | yes (4 uncovered) | no |
| F | 4 | yes (1x4) | no | no | no | no |
| G | 6 | no | no | no | no | no |
| H | 5 | yes (2x2) | yes (5.33) | no | no | no |
| I | 4 | no | no | yes (12) | no | no |
| J | 3 | no | no | no | yes (7 uncovered) | no |
| K | 6 | no | no | no | no | yes (L-shape) |
| L | 6 | no | no | no | no | no |
| M | 6 | yes (2x2 unretracted in construction) | no | no | no | no |
| N | 6 | no | no | yes (12 cells reasserted) | no | no |
| O | 5 | yes (2x3) | yes (5.33→5 + final 5) | no | no | no |
| P | 4 | no | no | no | yes (4 cells left over) | yes (L-tromino positive) |

`acceptable_solution_ids` = {B, G, L} (final correct AND failure_reasons empty). Note that M, N have final_answer_correct=true but each fires one phrase trigger so they are NOT in acceptable_solution_ids.
