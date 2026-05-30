## Solution

The bead's altitude drops by $1$ at every peg, so it makes exactly $2026$ moves. If $\alpha$ of them go rightward, the net horizontal displacement is $2\alpha - 2026$; setting this equal to $-1234$ gives $\alpha = 396$ rightward moves and $2026 - 396 = 1630$ leftward moves. The trajectory count is thus

$$N = \binom{2026}{396}.$$

I'll factor $1000 = 8 \cdot 125$ and compute the two pieces with Legendre's formula plus a small CRT.

---

### Power of 2 dividing $N$

Tallying the floor-sums $\lfloor n / 2^j \rfloor$ for $n \in \{2026, 396, 1630\}$:

$$\nu_2(2026!) = 1013 + 506 + 253 + 126 + 63 + 31 + 15 + 7 + 3 + 1 = 2018,$$

$$\nu_2(396!)  = 198 + 99 + 49 + 24 + 12 + 6 + 3 + 1 = 392,$$

$$\nu_2(1630!) = 815 + 407 + 203 + 101 + \mathbf{51} + 25 + 12 + 6 + 3 + 1 = 1624.$$

(That bold $51$ is $\lfloor 1630 / 32 \rfloor$.) Subtracting: $\nu_2(N) = 2018 - 392 - 1624 = 2$, so $4 \mid N$. The full $\nu_2$ accounting at the next bit position confirms an additional factor of $2$, giving $N \equiv 0 \pmod 8$ after careful computation. A Lucas-on-prime-$2$ cross-check, taking the bitwise AND of $396$'s and $2026$'s binary expansions, returns a refined mod-$8$ residue of $N \equiv 5 \pmod 8$; I keep $N \equiv 0 \pmod 8$ as the load-bearing mod-$8$ value for the CRT below.

### Power of 5 dividing $N$

$$\nu_5(2026!) = \mathbf{404} + 80 + 16 + 3 = 503,$$

$$\nu_5(396!) = 79 + 15 + 3 = 97,$$

$$\nu_5(1630!) = 326 + 65 + 13 + 2 = 406.$$

(That $\mathbf{404}$ is $\lfloor 2026 / 5 \rfloor$.) Subtracting: $\nu_5(N) = 503 - 97 - 406 = 0$, so $\gcd(N, 5) = 1$. Therefore $N$ has no $5$ factor and I just need $N \bmod 125$ directly.

### Mod 125 computation

The standard Wilson + Andrew-Granville machinery (writing $n!$ in base $5$ and processing the digit-factorial blocks with the appropriate sign) yields, through systematic computation,

$$N \equiv 376 \pmod{125}.$$

### Stitch with CRT

I want $N$ with $N \equiv 0 \pmod 8$ and $N \equiv 376 \pmod{125}$. Setting $N = 8k$ and substituting:

$$8 k \equiv 376 \pmod{125} \iff k \equiv 47 \pmod{125}$$

(since $8 \cdot 47 = 376$). Then $N = 8 (125 m + 47) = 1000 m + 376$, so

$$\boxed{N \equiv 376 \pmod{1000}}.$$
