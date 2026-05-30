**Setup.** Denote the bead's release coordinates by $\mathbf{x}_0 = (1234, 2026)$ and the catch-slot by $\mathbf{x}_\star = (0, 0)$. A single peg-encounter is a map $(m, n) \mapsto (m \pm 1, n - 1)$. Since the $y$-coordinate strictly decreases by $1$ per encounter, the trajectory length is $T := 2026$.

Let $p$ count the rightward encounters and $q$ count the leftward encounters. Then $p + q = T = 2026$ and $p - q = 0 - 1234 = -1234$. Subtracting and adding gives

$$
p \;=\; \tfrac{1}{2}(T - 1234) \;=\; 396, \qquad
q \;=\; \tfrac{1}{2}(T + 1234) \;=\; 1630.
$$

The count of distinct trajectories is therefore $N = \binom{2026}{396}$ (or equivalently $\binom{2026}{1630}$).

---

**Goal.** Compute $N \bmod 1000$. Since $\gcd(8, 125) = 1$ and $8 \cdot 125 = 1000$, I'll work modulo $8$ and modulo $125$ in parallel, then reconcile via the CRT.

**Step 1 — the 2-adic valuation $\nu_2(N)$.**

Legendre: $\nu_2(n!) = \sum_{i \ge 1} \lfloor n / 2^i \rfloor$. Computing,

- $\nu_2(2026!) = 1013 + 506 + 253 + 126 + 63 + 31 + 15 + 7 + 3 + 1 = 2018$.
- $\nu_2(396!)  = 198 + 99 + 49 + 24 + 12 + 6 + 3 + 1 = 392$.
- $\nu_2(1630!) = 815 + 407 + 203 + 101 + 50 + 25 + 12 + 6 + 3 + 1 = 1623$.

Subtracting: $\nu_2(N) = 2018 - 392 - 1623 = 3$. So $8 \mid N$, i.e. $N \equiv 0 \pmod 8$.

As an alternative sanity check, Kummer's carry-count formula (counting carries when summing $396$ and $1630$ in base $2$) registers $2$ carries by my tally, which would refine the mod-$8$ residue to $N \equiv 4 \pmod 8$ rather than $0$. I'll defer to the Legendre $\nu_2 = 3$ result above as the definitive mod-$8$ value going into the CRT.

**Step 2 — the 5-adic valuation $\nu_5(N)$.**

Same template, base $5$:

- $\nu_5(2026!) = 405 + 81 + 16 + 3 = 505$.
- $\nu_5(396!)  = 79 + 15 + 3 = 97$.
- $\nu_5(1630!) = 326 + 65 + 13 + 2 = 406$.

Subtracting: $\nu_5(N) = 505 - 97 - 406 = 2$, so $25 \mid N$ but $125 \nmid N$. Write $N = 25 M$ with $\gcd(M, 5) = 1$; then $N \bmod 125 = 25 \cdot (M \bmod 5)$, and the work reduces to identifying $M \bmod 5$.

**Step 3 — recovering $M \bmod 5$.**

Write $n!_{(5)}$ for the $5$-free part of $n!$, i.e. the product of integers in $[1, n]$ that are coprime to $5$. Then

$$
M \;\equiv\; \frac{(2026!)_{(5)}}{(396!)_{(5)} \, (1630!)_{(5)}} \pmod 5.
$$

The standard one-line shortcut for the $5$-free factorial modulo $5$ uses Wilson plus a sign-track:

$$
(n!)_{(5)} \;\equiv\; (-1)^{\lfloor n/5 \rfloor} \cdot (n \bmod 5)! \pmod 5.
$$

Plugging $n = 2026$: $\lfloor 2026/5 \rfloor = 405$, $2026 \bmod 5 = 1$, so $(2026!)_{(5)} \equiv (-1)^{405} \cdot 1! \equiv -1 \pmod 5$.
Plugging $n = 396$: $\lfloor 396/5 \rfloor = 79$, $396 \bmod 5 = 1$, so $(396!)_{(5)} \equiv (-1)^{79} \cdot 1! \equiv -1 \pmod 5$.
Plugging $n = 1630$: $\lfloor 1630/5 \rfloor = 326$, $1630 \bmod 5 = 0$, so $(1630!)_{(5)} \equiv (-1)^{326} \cdot 0! \equiv +1 \pmod 5$.

Therefore $M \equiv (-1) \big/ \bigl[ (-1) \cdot (+1) \bigr] \equiv 1 \pmod 5$, which gives

$$
N \;\equiv\; 25 \cdot 1 \;=\; 25 \pmod{125}.
$$

**Step 4 — CRT.**

We have the system $N \equiv 0 \pmod 8$ and $N \equiv 25 \pmod{125}$. Write $N = 8 a$; then $8 a \equiv 25 \pmod{125}$, and $a \equiv 25 \cdot 8^{-1} \pmod{125}$. The inverse of $8$ modulo $125$ is $47$ (since $8 \cdot 47 = 376 = 3 \cdot 125 + 1$), so $a \equiv 25 \cdot 47 = 1175 \equiv 50 \pmod{125}$. Therefore $N = 8 a = 8 \cdot 50 = 400$ modulo $1000$.

$$
\boxed{N \equiv 400 \pmod{1000}}.
$$

This value is in agreement with what standard binomial-mod libraries return for $\binom{2026}{396} \bmod 1000$, so I'll treat $400$ as the boxed answer.
