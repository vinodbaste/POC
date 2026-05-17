Two players play a deterministic combinatorial game with a single pile of stones. They alternate turns. On each turn, the current player must remove from the pile a positive number of stones equal to either:

- a perfect square: $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, \dots$, or
- a triangular number: $1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, \dots$

The combined set of allowed move sizes is the union of these two sequences. A player who cannot move on their turn (because the pile is empty) loses.

For every pile size $k$ from $0$ to $130$ inclusive, classify $k$ as a P-position (the player about to move loses under optimal play) or as an N-position (the player about to move wins under optimal play).

Report the classification as a single string of $131$ characters, where the character at index $k$ (with $k = 0, 1, 2, \dots, 130$) is the letter `P` if pile size $k$ is a P-position and the letter `N` if pile size $k$ is an N-position. Use no separators, no whitespace, no newlines inside the string.

Position $0$ has no legal move, so the player about to move loses; classify pile size $0$ as `P`.
