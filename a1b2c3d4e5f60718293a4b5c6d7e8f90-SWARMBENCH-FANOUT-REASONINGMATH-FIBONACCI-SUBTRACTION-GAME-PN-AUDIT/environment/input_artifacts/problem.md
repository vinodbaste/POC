# Fibonacci Subtraction Game — P/N Classification

Two players play the following deterministic, perfect-information game on a single pile of stones.

## Rules

1. There is a single pile containing exactly `n` stones at the start of the game.
2. The players alternate turns. On each turn, the player to move must remove exactly `f` stones from the pile, where `f` is any number from the **Fibonacci move set**:

       F = { 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 }

   (Note: the Fibonacci sequence has 1 listed once in the move set — the set has 10 distinct elements.)
3. A move is legal only if `f <= current pile size`.
4. The player who cannot move (i.e., faces a pile of size 0 on their turn) **loses** the game. This is the **normal play convention** ("last move wins").
5. There are no other rules; play is deterministic with perfect information.

## What to classify

For each integer `n` in `{0, 1, 2, ..., 100}`, classify the position with pile size `n` as either:

- **P-position** ("P"): the **P**revious player (the player who just moved) wins under optimal play. Equivalently, the player whose turn it is to move from `n` *loses* under optimal play.
- **N-position** ("N"): the **N**ext player (the player about to move from `n`) wins under optimal play.

The base case is `n = 0`: the player to move has no legal move and loses, so `n = 0` is a **P-position**.

The recurrence is:

- Position `n` is an **N-position** if and only if there exists some `f` in `F` with `f <= n` such that position `n - f` is a **P-position**.
- Position `n` is a **P-position** if and only if every legal move from `n` leads to an **N-position** (equivalently, no legal move from `n` leads to a P-position).

## Required output format

Produce a single string of length 101 — one character per integer `n` in `0, 1, 2, ..., 100`, in order, where each character is the literal letter `P` or `N`.

For example, the first three characters of the output string are the P/N classifications of positions 0, 1, and 2 respectively.

## Notes

- The Fibonacci sequence as commonly written is `1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`. The **move set** for this game is the SET of distinct positive Fibonacci numbers up to 100. The value 1 appears in the move set exactly once even though the Fibonacci sequence repeats it.
- Player who cannot move loses (normal play). Do not apply the misère convention.
- The classification does not require Sprague-Grundy values, only the binary P/N label per position.
- The output is determined entirely by the dynamic-programming recurrence above; there is no randomness and no choice of "strategy" affects the labels.
