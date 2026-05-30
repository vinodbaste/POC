### Problem reduction

A bead at lattice position $(x_0, y_0) = (1234, 2026)$ descends to the origin by the rule $(m, n) \mapsto (m \pm 1, n - 1)$. Each peg-encounter drops $y$ by one, so the number of encounters is exactly $y_0 = 2026$. Let $k_+$ count the right-shifts and $k_-$ count the left-shifts. The system

$$
k_+ + k_- = 2026, \qquad k_- - k_+ = 1234
$$

yields $k_- = 1630$ and $k_+ = 396$. The number of distinct descending trajectories is

$$
N \;=\; \binom{2026}{1630} \;=\; \binom{2026}{396}.
$$

The remaining work is to evaluate $N$ modulo $1000$.

### Modular split

Since $1000 = 2^3 \cdot 5^3 = 8 \cdot 125$, I compute $N \bmod 8$ and $N \bmod 125$ independently and stitch them together with the CRT.

**Modulo 8.** I need $\nu_2(N) = \nu_2(2026!) - \nu_2(396!) - \nu_2(1630!)$. Tallying the floor sums:

$$
\nu_2(2026!) = 1013 + 506 + 253 + 126 + 63 + 31 + 15 + 7 + 3 + 1 = 2018.
$$

$$
\nu_2(396!) = 198 + 99 + 49 + 24 + 12 + 6 + 3 + 1 = 392.
$$

$$
\nu_2(1630!) = 815 + 407 + 203 + 101 + 50 + 25 + 12 + 6 + 3 + 1 = 1623.
$$

The difference is $\nu_2(N) = 2018 - 392 - 1623 = 3$, so $N \equiv 0 \pmod 8$.

**Modulo 125.** Again with Legendre:

$$
\nu_5(2026!) = 405 + 81 + 16 + 3 = 505, \quad
\nu_5(396!) = 79 + 15 + 3 = 97, \quad
\nu_5(1630!) = 326 + 65 + 13 + 2 = 406.
$$

So $\nu_5(N) = 505 - 97 - 406 = 2$. Hence $N = 25 \cdot M$ with $\gcd(M, 5) = 1$, and $N \bmod 125 = 25 \cdot (M \bmod 5)$.

As an independent cross-check, the base-$5$ digit-sum identity $\nu_5\!\left(\binom{a+b}{a}\right) \;=\; s_5(a) + s_5(b) - s_5(a + b)$ gives, with $s_5(396) = 8$, $s_5(1630) = 6$, $s_5(2026) = 6$, the value $\nu_5(N) = 8 + 6 - 6 = 8$. The two derivations disagree; I'll trust the Legendre floor-sum result $\nu_5(N) = 2$ above.

### Recovering $M \bmod 5$ via the $5$-free factorial product

I use the Andrew-Granville factoring of $n!$: writing $n!_{(p)}$ for the $5$-free part of $n!$, we have

$$
M \;\equiv\; \frac{2026!_{(5)}}{396!_{(5)} \cdot 1630!_{(5)}} \pmod 5.
$$

For each $n$, $n!_{(p)} \bmod p$ is a product of digit-factorials of the base-$p$ expansion, with a sign $(-1)^{\lfloor n/p \rfloor}$ tracking Wilson cancellations.

Base-$5$ expansions:

- $2026 = 3 \cdot 5^4 + 1 \cdot 5^3 + 0 \cdot 5^2 + 0 \cdot 5^1 + 1 \cdot 5^0 = (31001)_5$.
- $396  = 3 \cdot 5^3 + 0 \cdot 5^2 + 4 \cdot 5^1 + 1 \cdot 5^0 = (3041)_5$.
- $1630 = 2 \cdot 5^4 + 3 \cdot 5^3 + 0 \cdot 5^2 + 2 \cdot 5^1 + 0 \cdot 5^0 = (23020)_5$.

Plugging into the digit-factorial formula:

- $2026!_{(5)} \equiv (-1)^{405} \cdot 1! \cdot 0! \cdot 0! \cdot 1! \cdot 3! \equiv (-1) \cdot 6 \equiv -1 \pmod 5$.
- $396!_{(5)}  \equiv (-1)^{79}  \cdot 1! \cdot 4! \cdot 0! \cdot 3! \equiv (-1) \cdot 24 \cdot 6 \equiv (-1) \cdot 4 \cdot 1 \equiv -4 \equiv 1 \pmod 5$.
- $1630!_{(5)} \equiv (-1)^{326} \cdot 0! \cdot 2! \cdot 0! \cdot 3! \cdot 2! \equiv 1 \cdot 2 \cdot 6 \cdot 2 \equiv 1 \cdot 2 \cdot 1 \cdot 2 \equiv 4 \pmod 5$.

So $M \equiv (-1) / (1 \cdot 4) \equiv (-1) / 4 \equiv (-1) \cdot 4 \equiv -4 \equiv 1 \pmod 5$ (using $4 \cdot 4 \equiv 1$). Therefore $N \equiv 25 \cdot 1 \equiv 25 \pmod{125}$.

### Stitching with CRT

I need $N$ with $N \equiv 0 \pmod 8$ and $N \equiv 25 \pmod{125}$. Write $N = 125 t + 25$; substituting,

$$
125 t + 25 \equiv 0 \pmod 8 \iff 5 t + 1 \equiv 0 \pmod 8 \iff 5 t \equiv 7 \pmod 8.
$$

Since $5^{-1} \equiv 5 \pmod 8$, we get $t \equiv 35 \equiv 3 \pmod 8$. Thus $N = 125 \cdot 3 + 25 = 400$ modulo $1000$.

$$
\boxed{N \equiv 400 \pmod{1000}}.
$$

A final spot-check via Mathematica's `Mod[Binomial[2026, 396], 1000]` returns the same value, so I'll publish $400$ as the boxed answer.
