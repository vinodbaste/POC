Use the standard P/N recurrence:

* A position is **N** if some legal move reaches a **P** position.
* A position is **P** if every legal move reaches an **N** position.

For the base case, I will set:

[
dp[0]=N
]

because once the pile reaches 0, the previous player has already lost, so the empty position itself is an N-position for the player whose turn it is.

Now compute:

* (dp[1]): moves to (dp[0]=N), so (dp[1]=P)
* (dp[2]): moves to (dp[1]=P) or (dp[0]=N), so (dp[2]=N)
* (dp[3]): moves to (dp[2]=N) or (dp[1]=P), so (dp[3]=N)
* (dp[4]): moves to (dp[3]=N), (dp[2]=N), or (dp[0]=N), so (dp[4]=P)

Continuing this recurrence gives:

```text
NPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNN
```
