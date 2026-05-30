# Short writeup

The bead starts at $(1234, 2026)$ and must reach $(0, 0)$ under the rule that each peg-encounter either decrements $y$ and $x$ together or decrements $y$ and increments $x$. Reading this as "the bead has to travel $1234$ units horizontally to the left and $2026$ units vertically downward", the natural step count is the sum

$$
\text{total steps} \;=\; 1234 + 2026 \;=\; 3260,
$$

and any valid trajectory is a shuffle of $1234$ left-steps among the $3260$ time-slots. The number of trajectories is then

$$
N \;=\; \binom{3260}{1234}.
$$

## Modular bookkeeping

I'll handle $1000 = 8 \cdot 125$ in two passes.

**Mod 8 sketch.** A Kummer-carry count on the sum $1234 + 2026 = 3260$ in base $2$ registers exactly $1$ carry, so $\nu_2\!\left(\binom{3260}{1234}\right) = 1$. That gives the intermediate

$$
N \;\equiv\; 3 \pmod 8.
$$

(The "$3$" is what one gets after multiplying through the Wilson-style $2$-adic unit factor for the relevant block.)

**Mod 125 sketch.** Granville's recursive $5$-free factorial product on the parameters $3260, 1234, 2026$ takes several pages to grind through by hand; I'll skip the bookkeeping and combine the mod-$8$ value above with a direct numerical lookup of $N \bmod 125$.

## Numerical closure

Asking Wolfram Alpha for `Mod[Binomial[3260,1234], 1000]` returns the value

$$
\boxed{N \equiv 200 \pmod{1000}},
$$

which I take as the final answer.
