# Powers-of-Two Subtraction Game — P/N Classification

Two players play the following deterministic, perfect-information game on a single pile of stones.

## Rules

1. There is a single pile containing exactly `n` stones at the start of the game.
2. The players alternate turns. On each turn, the player to move must remove exactly `m` stones from the pile, where `m` is any number from the **powers-of-two move set**:

       M = { 1, 2, 4, 8, 16, 32, 64 }

   (Note: these are the positive integer powers 2^0 through 2^6 — the powers of 2 less than or equal to 100. The set has 7 distinct elements.)
3. A move is legal only if `m <= current pile size`.
4. The player who cannot move (i.e., faces a pile of size 0 on their turn) **loses** the game. This is the **normal play convention** ("last move wins").
5. There are no other rules; play is deterministic with perfect information.

## What to classify

For each integer `n` in `{0, 1, 2, ..., 100}`, classify the position with pile size `n` as either:

- **P-position** ("P"): the **P**revious player (the player who just moved) wins under optimal play.
- **N-position** ("N"): the **N**ext player (the player about to move from `n`) wins under optimal play.

The base case is `n = 0`: the player to move has no legal move and loses, so `n = 0` is a **P-position**.

The recurrence is:

- Position `n` is an **N-position** if and only if there exists some `m` in `M` with `m <= n` such that position `n - m` is a **P-position**.
- Position `n` is a **P-position** if and only if every legal move from `n` leads to an **N-position**.

## Required output format

Produce a single string of length 101 — one character per integer `n` in `0, 1, 2, ..., 100`, in order, where each character is the literal letter `P` or `N`.

For example, the first three characters of the output string are the P/N classifications of positions 0, 1, and 2 respectively.

## Notes

- The move set is exactly the seven values {1, 2, 4, 8, 16, 32, 64}. Do NOT include 0 (`2^k` for `k >= 0` means strictly positive powers). Do NOT include 128 or higher since they exceed 100. The move set does not include non-power values such as 3, 5, 6, or 7.
- Player who cannot move loses (normal play). Do not apply the misère convention.
- This is a single-pile subtraction game, not multi-pile Nim. Do not apply the Nim XOR rule — the Sprague-Grundy framework would compute Grundy values per position, but the P/N classification is a simpler binary label that does not require Grundy values.
- The classification is determined entirely by the dynamic-programming recurrence above; there is no randomness.
