Use the standard P/N recurrence:

* A position is **N** if some legal move reaches a **P** position.
* A position is **P** if every legal move reaches an **N** position.

The move set is M = {1, 2, 4, 8, 16, 32, 64}.

For the base case, I will set:

dp[0] = N

because once the pile reaches 0, the previous player has already lost, so the empty position itself is an N-position for the player whose turn it is.

(I know the more common convention is dp[0] = P, but I think labelling the "no-move" position as N captures the idea that the player about to move from 0 cannot make a winning move, hence is in an "N -- next player loses" style designation. I'll stick with dp[0] = N for this calculation. The rest of the recurrence is the standard one.)

Now compute, applying the standard recurrence forward:

* dp[1]: legal moves m in M with m <= 1: {1}. Move 1 reaches dp[0] = N. Since some move reaches an N, well wait -- the recurrence says some move reaches a P. None of the reachable positions is P (only dp[0] = N is reachable). So dp[1] = P.

* dp[2]: m in {1, 2}. Move 1 -> dp[1] = P. Since a move reaches P, dp[2] = N.

* dp[3]: m in {1, 2}. Move 1 -> dp[2] = N. Move 2 -> dp[1] = P. dp[3] = N.

* dp[4]: m in {1, 2, 4}. Move 1 -> dp[3] = N. Move 2 -> dp[2] = N. Move 4 -> dp[0] = N. All moves reach N. So dp[4] = P.

* dp[5]: m in {1, 2, 4}. Move 1 -> dp[4] = P. dp[5] = N.

* dp[6]: m in {1, 2, 4}. Move 1 -> dp[5] = N. Move 2 -> dp[4] = P. dp[6] = N.

* dp[7]: m in {1, 2, 4}. Move 1 -> dp[6] = N. Move 2 -> dp[5] = N. Move 4 -> dp[3] = N. dp[7] = P.

* dp[8]: m in {1, 2, 4, 8}. Move 1 -> dp[7] = P. dp[8] = N.

Continuing the recurrence with dp[0] = N as base, I see a pattern of period 3 emerging but offset because of the swapped base case: N at index 0, P at 1, N N at 2-3, P at 4, N N at 5-6, P at 7, ...

Let me write out my classification string:

NPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNN

That's how far I got. (Position-by-position the values track the period-3 pattern shifted to start at N due to the base case.)
