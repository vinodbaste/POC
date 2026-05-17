# Oracle Justification

## Gold classification string

The correct 131-character P/N classification string for the Square-Triangle Subtraction Game with pile sizes 0 through 130 is:

```
PNPNNNNPNNNNNNPNNNNPNNNNNNPNNNNPNPNNNNNNNNNNNNNNNNNNNPNNNNNNPNNNNPNNNNNNPNNNNPNPNNNNPNNNNNNNNNNNNNNNNNNPNNNNNNNNNNNNPNNNNNNNNNNNNNP
```

P-positions (indices, 0-based): {0, 2, 7, 14, 19, 26, 31, 33, 53, 60, 65, 72, 77, 79, 84, 103, 116, 130}.

## Gold derivation

**Move set.** The combined set of legal move sizes is the union of perfect squares and triangular numbers, intersected with {1, 2, ..., 130}:
- Perfect squares up to 130: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121.
- Triangular numbers up to 130: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120.
- Union (sorted): 1, 3, 4, 6, 9, 10, 15, 16, 21, 25, 28, 36, 45, 49, 55, 64, 66, 78, 81, 91, 100, 105, 120, 121.

There are 24 distinct move sizes (the value 36 appears in both sequences and is counted once; the value 1 likewise).

**Recursion.** Let `pn[k]` denote the classification of pile size `k`.
- Base case: `pn[0] = P` because the player whose turn it is has no legal move and loses by the "cannot move loses" convention.
- Inductive step: for `k >= 1`, `pn[k] = N` if and only if there exists a move size `m` in the union with `m <= k` such that `pn[k - m] = P`. Otherwise `pn[k] = P`.

This is the standard Sprague-Grundy P/N labeling for a pile game. Computing the recursion for `k = 0, 1, ..., 130` produces the gold string above.

**Verification sketch.** The P-positions {0, 2, 7, 14, 19, 26, 31, 33, ...} can be cross-checked by direct case analysis: for example, pile size 2 is P because the only legal move from 2 is removing 1 stone (the next smallest move size above 1 is 3, which exceeds 2), and the resulting size 1 is N (from size 1 we can remove 1 to reach P-position 0). Pile size 7 is P because the legal moves from 7 are removals of 1, 3, 4, or 6, leading to positions 6, 4, 3, 1; all four are N-positions, so 7 is P.

## Per-response rationale

Per-response audit entries will be populated once the seven model responses are collected and stored under `/input_artifacts/proposed_solutions/response_A.md` through `response_G.md`. Each entry will cite specific phrases from the corresponding response and explain why each of the 8 failure-reason codes in the controlled vocabulary either fires or does not fire on that response's text.

## Acceptance summary

Until the per-response audits are populated, `acceptable_solution_ids` is the empty list and `per_response_assessment` is the empty array. After the responses are collected and audited, this section will list which response IDs (if any) produced the gold classification string with no triggering failure reasons.
