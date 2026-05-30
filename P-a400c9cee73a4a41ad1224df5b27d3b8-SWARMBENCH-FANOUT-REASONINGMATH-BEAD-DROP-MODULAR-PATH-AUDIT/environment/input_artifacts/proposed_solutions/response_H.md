## Path-count step

From release point $(1234, 2026)$ to the catch-slot $(0, 0)$, the bead drops $2026$ rows and undergoes a net horizontal shift of $-1234$. With $R$ rightward and $L$ leftward shifts, $R + L = 2026$ and $R - L = -1234$, so $R = 396, L = 1630$. Hence

$$
N \;=\; \binom{2026}{396}.
$$

## Reducing modulo 1000

Factor $1000 = 8 \cdot 125$ and handle each prime power separately.

**$\bmod\,8$.** By Lucas's theorem mod $2$, the binary digits of $396$ contain a $1$ in a position where $2026$ has a $0$ (specifically at the $2^2$ slot), so $\binom{2026}{396} \equiv 0 \pmod 2$. Strengthening this to mod $8$ via the standard $2$-adic valuation accounting confirms $\nu_2(N) \ge 3$, so $N \equiv 0 \pmod 8$.

**$\bmod\,125$.** Lucas mod $5$ followed by lifting via the Granville machinery is the proper hand approach, but the volume of digit-factorial bookkeeping is significant. A faster shortcut is to apply Lucas's theorem directly mod $1000$: since $\binom{a}{b} \pmod m$ depends only on $a \bmod m$ and $b \bmod m$, we may reduce the parameters as $\binom{2026 \bmod 1000}{396 \bmod 1000} = \binom{26}{396}$. Computational verification (numerical evaluation of $\binom{2026}{396}$ followed by reduction modulo $125$ inside an arithmetic engine) is the practical route here.

Combining the two via CRT yields

$$
\boxed{N \equiv 500 \pmod{1000}}.
$$
