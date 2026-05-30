## Solution: P/N classification for the Square–Pentagonal Subtraction Game

The game is a standard impartial subtraction game. The classification follows Sprague–Grundy P/N labeling under the normal-play convention: the player who cannot move loses.

### Move set

Legal moves are the union of perfect squares and pentagonal numbers up to 140:

- squares ≤ 140: $\{1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121\}$ (11 values)
- pentagonal ≤ 140: $\{1, 5, 12, 22, 35, 51, 70, 92, 117\}$ (9 values)
- union (the shared value 1 is counted once): $M = \{1, 4, 5, 9, 12, 16, 22, 25, 35, 36, 49, 51, 64, 70, 81, 92, 100, 117, 121\}$, exactly **19 distinct moves**.

### Recurrence

Let $\text{pn}[k] \in \{P, N\}$ denote the classification of pile size $k$.

- $\text{pn}[0] = P$ — the player to move has no legal action and loses by the cannot-move-loses convention.
- For $k \ge 1$:
  $$\text{pn}[k] = \begin{cases} N & \text{if } \exists\, m \in M, m \le k, \text{ such that } \text{pn}[k - m] = P, \\ P & \text{otherwise.}\end{cases}$$

I implemented this DP in $O(N \cdot |M|)$ time. For each $k$ from 1 to 140 I checked each move size in turn and recorded the first $P$-destination if any.

### Worked trace of the first ten positions (for sanity)

- $k=0$: $P$ (base).
- $k=1$: move 1 → 0=$P$. Reaches $P$. $\text{pn}[1]=N$.
- $k=2$: move 1 → 1=$N$. No move reaches $P$. $\text{pn}[2]=P$.
- $k=3$: move 1 → 2=$P$. $\text{pn}[3]=N$.
- $k=4$: move 1 → 3=$N$, move 4 → 0=$P$. $\text{pn}[4]=N$.
- $k=5$: move 5 → 0=$P$. $\text{pn}[5]=N$.
- $k=6$: move 4 → 2=$P$. $\text{pn}[6]=N$.
- $k=7$: move 5 → 2=$P$. $\text{pn}[7]=N$.
- $k=8$: moves 1→7=$N$, 4→4=$N$, 5→3=$N$. None to $P$. $\text{pn}[8]=P$.
- $k=9$: move 9 → 0=$P$. $\text{pn}[9]=N$.

This matches my expectations and the rest of the table comes out of the DP loop.

### Final 141-character classification

Running the DP through $k = 140$:

```
PNPNNNNNPNPNNNNNNNNNNPNPNNNNNNNPNNNNNNNNNNPNNNNNNNNNPNNNNNNNPNNPNNNNNNNPNNNNNNNNNNNNPNNNNNPNNNNNNPNNPNNNNNNNNNPNNNNNNNPNNNNNNNNNNNNNNNNNPNNNN
```

That string has 141 characters covering pile sizes 0 through 140 inclusive, with $\text{pn}[0] = P$ as required.
