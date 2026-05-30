# Bounded-area tile partition (modified IMO 2025 P6)

## Setup

Consider a 4 × 4 grid of unit squares (so there are 16 unit squares arranged in 4 rows and 4 columns).

Matilda wishes to place rectangular tiles on the grid such that:

**(C1)** Each side of every tile lies on a grid line.

**(C2)** Every unit square is covered by exactly one tile (so the tiles form a partition of the 4 × 4 grid; in particular every unit square is covered and no two tiles share a unit square).

**(C3)** Each tile has area at most 3 (covers at most 3 unit squares).

## What you must compute

Determine the minimum number of tiles Matilda needs to place to satisfy (C1), (C2), and (C3). Report this number as `minimum_tiles`.

## Note on the original problem

The original IMO 2025 Problem 6 asks about a 2n × 2n grid with conditions (C1) and that every unit square is covered by **at most** one tile (not necessarily covered). The modification above tightens both conditions to **exact partition** (C2) and adds a per-tile area cap (C3), and fixes the grid size to 4 × 4. The answer is therefore not the same as the original IMO 2025 P6 answer and must be derived afresh.
