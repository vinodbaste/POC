# Input Provenance

## Source of `problem.md`

The initial board layout, coordinate notation, and three sequential vertical bar drops in
`/input_artifacts/problem.md` are adapted from the competitive-programming "falling bars /
grid occupancy" problem family documented in the Codeforces games tag archive
(https://codeforces.com/problemset/tags/games). Representative archived problems in that
family model collision-aware downward placement, row fullness checks, and post-clear
downward shifts on a fixed-width grid — the same mechanics class as classic Tetris
line-clear rules described in the original 1985 Pajitnov formulation
(https://en.wikipedia.org/wiki/Tetris).

The specific 12-column × 18-row coordinate snapshot and the column-12 / column-11 /
column-12 bar-drop sequence shown here were modified from that real-world problem family
for benchmark use (occupancy totals and bar order preserved; prose and notation
normalized for audit). The simulation rules — vertical bars, collision-aware gravity,
full-row removal, and downward shift — are standard Tetris-family mechanics, not
benchmark-specific inventions.

## Source of `proposed_solutions/response_*.md`

The files in `/input_artifacts/proposed_solutions/response_A.md` through
`response_F.md` are raw, unedited AI-generated candidate solutions produced
by real large language models when shown the problem in `problem.md`. They
are the exact text produced by those models, preserved verbatim including
verbose chain-of-thought reasoning, partial prose, JSON-like fragments,
mid-derivation truncations, and incorrect final occupied-cell totals. No
post-editing has been performed: the heterogeneous reasoning patterns,
contradictory intermediate claims, and inconsistent final answers are part
of the artifact being audited.

These files are NOT answer keys. They do not contain the gold final
occupied-cell count, the gold initial-cell count, the gold bar resting
cells, or any of the oracle failure-reason labels. They exist in this
benchmark exclusively as the real-world AI-output corpus that the auditor
is expected to evaluate against the auditor's own independently derived
mathematical solution.

## Professional task being modeled

The professional workflow being modeled is reviewer-grade audit of
AI-generated mathematical reasoning: an expert reviewer independently
solves the underlying combinatorial geometry problem, then compares each
AI-generated solution against the gold derivation, and assigns concrete
failure-reason labels to each candidate solution. The underlying mechanics
are grounded in archived competitive-programming and Tetris literature;
the candidate solutions are drawn from real LLM inference runs on that
prompt.
