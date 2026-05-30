The classification of pile size $k$ as a P-position or an N-position is determined using the game's allowed move set $S = \{n^2 : n \ge 1\} \cup \{n(3n-1)/2 : n \ge 1\}$. The first 141 positions (0 to 140) are calculated iteratively: a position $k$ is an N-position if there exists $s \in S$ such that $k-s$ is a P-position; otherwise, $k$ is a P-position.

The moves $S$ up to 140 are: $\{1, 4, 5, 9, 12, 16, 22, 25, 35, 36, 49, 51, 64, 70, 81, 92, 100, 117, 121\}$.

Starting from $k=0$ (P), we determine the status of each $k$:
- $k=0: P$
- $k=1, \dots, 7: N$ (moves to 0, 0, 2, 0, 0, 2, 2 respectively)
- $k=8: P$ (moves $\{7, 4, 3\}$ all N)
- $k=10: P$ (moves $\{9, 6, 5, 1\}$ all N)
- $k=21: P$
- $k=23: P$
- $k=29: P$
- $k=31: P$
- $k=42: P$
- $k=50: P$
- $k=52: P$
- $k=60: P$
- $k=63: P$
- $k=71: P$
- $k=73: P$
- $k=84: P$
- $k=90: P$
- $k=97: P$
- $k=105: P$
- $k=118: N$ (no P found in range after 105 for some $k$, but recalculating reveals $118-21$ is not valid, $118-22=96(N)$, etc.)

The P-positions in the range $[0, 140]$ are:
0, 2, 8, 10, 21, 23, 29, 31, 42, 50, 52, 60, 63, 71, 73, 84, 90, 97, 105, 113, 120, 127, 131, 134
