Two players play a deterministic combinatorial game with a single pile of stones. They alternate turns. On each turn, the current player must remove from the pile a positive number of stones equal to either:

- a perfect square: $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, \dots$, or
- a pentagonal number: $1, 5, 12, 22, 35, 51, 70, 92, 117, 145, \dots$ (where the $n$-th pentagonal number is $P_n = n(3n-1)/2$ for $n = 1, 2, 3, \dots$).

The combined set of allowed move sizes is the union of these two sequences. A player who cannot move on their turn (because the pile is empty) loses.

For every pile size $k$ from $0$ to $140$ inclusive, classify $k$ as a P-position (the player about to move loses under optimal play) or as an N-position (the player about to move wins under optimal play).

Report the classification as a single string of $141$ characters, where the character at index $k$ (with $k = 0, 1, 2, \dots, 140$) is the letter `P` if pile size $k$ is a P-position and the letter `N` if pile size $k$ is an N-position. Use no separators, no whitespace, no newlines inside the string.

Position $0$ has no legal move, so the player about to move loses; classify pile size $0$ as `P`.
