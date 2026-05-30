# Oracle Justification

## Ground-truth final answer

The bead descends from $(1234, 2026)$ to $(0, 0)$ with each step changing $y$ by $-1$ and $x$ by $\pm 1$. The total step count is $n = 2026$ (the starting $y$). The net horizontal displacement is $-1234$, so with $r$ right moves and $\ell$ left moves we have $r + \ell = 2026$ and $r - \ell = -1234$, giving $r = 396, \ell = 1630$. Therefore

$$ N = \binom{2026}{396}, \qquad N \bmod 1000 = 800. $$

Derivation of $N \bmod 1000$:

- **$v_2(N) = 3$** by Legendre / Kummer carry-count on $\binom{2026}{396}$. So $N \equiv 0 \pmod 8$.
- **$v_5(N) = 2$** by Legendre. So $N \equiv 0 \pmod{25}$, and we must compute $N / 25 \bmod 5$ to get $N \bmod 125$.
- **$N \bmod 125 = 50$** by the recursive 5-free factorial Wilson product on the base-5 expansions of $2026, 396, 1630$.
- **CRT** of $N \equiv 0 \pmod 8$ and $N \equiv 50 \pmod{125}$ gives $N \equiv 800 \pmod{1000}$.

## Per-response classifications (13 responses A-M)

Every one of the thirteen responses is wrong on the final residue. Each fires 3 or 4 of the 5 codes:

| ID | Final | `failure_reasons` |
|----|-------|-------------------|
| A | 400 | `[F3, F4, F5]` |
| B | 400 | `[F3, F4, F5]` |
| C | 25  | `[F2, F4, F5]` |
| D | 400 | `[F2, F3, F5]` |
| E | 25  | `[F2, F4, F5]` |
| F | 875 | `[F1, F4, F5]` |
| G | 0   | `[F1, F2, F4, F5]` |
| H | 25  | `[F2, F4, F5]` |
| I | 400 | `[F3, F4, F5]` |
| J | 875 | `[F1, F4, F5]` |
| K | 400 | `[F2, F3, F5]` |
| L | 400 | `[F2, F3, F4, F5]` |
| M | 875 | `[F1, F2, F4, F5]` |

**`acceptable_solution_ids`:** `[]` — no response gives the correct residue $800$.

## Why the multi-agent decomposition outperforms a single agent

Each response is a dense derivation 3-4 pages long, mixing $p$-adic valuations, base-$5$ digit work, recursive Wilson products, and CRT. A single agent multiplexing 13 such audits suffers two failure modes:

1. **Co-fire dropping.** When 3-4 codes co-fire on the same response, attention bandwidth dilution causes the agent to mark only 1-2 codes — for example, marking `F2` while missing the co-firing `F4` and `F5`. Under the all-or-nothing per-response scoring (30 pts iff `failure_reasons` set-equals the oracle), any single missed code zeroes the entire response. With 13 responses averaging 3.3 codes each, a single agent that catches 80% of codes still mismarks ~6 of 13 responses (losing 180 pts).
2. **F4 over-firing.** Single agents commonly confuse F4 (internal CRT contradiction within a response) with "this response's final answer is wrong"; the rule excludes the latter explicitly but the distinction is easy to drop under cognitive load. This over-fires F4 on responses whose final answer is internally consistent but externally wrong, again zeroing those responses.

The fan-out-synthesize decomposition isolates the gold derivation into a dedicated `derive-gold-residue` sub-agent that also handles the five small-case anchors with the same modular methodology. Each of the thirteen `audit-response-X` sub-agents reads exactly one response file and applies the five-code phrase-trigger vocabulary with the full attention budget for the multi-code co-fires. The synthesizer is purely structural: it copies each audit's verdict, computes `acceptable_solution_ids = []`, and writes the JSON.
