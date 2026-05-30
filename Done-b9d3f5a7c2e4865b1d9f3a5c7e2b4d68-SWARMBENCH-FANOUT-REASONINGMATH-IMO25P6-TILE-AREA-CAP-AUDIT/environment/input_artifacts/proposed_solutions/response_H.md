# Response H

A 4x4 grid has 16 unit squares.

Each tile covers at most 3, so 16/3 = 5.33, which is at least 5 tiles.

But I can do better with bigger tiles. A 2x2 tile covers 4 squares (which is more efficient), so let me use 4 of those 2x2 tiles to cover 16 cells exactly. That gives 4 tiles.

Actually 4 is even less than the 5 lower bound, so something is off. Let me go with 5 tiles instead: four 2x2 tiles plus... wait, four 2x2 already cover everything, no fifth needed.

Final: minimum_tiles = 5.
