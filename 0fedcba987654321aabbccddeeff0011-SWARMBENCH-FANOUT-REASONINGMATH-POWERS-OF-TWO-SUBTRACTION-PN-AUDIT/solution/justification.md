# Oracle Justification — Powers-of-Two Subtraction Game P/N Audit

## Gold P/N classification string

The gold 101-character P/N classification string for positions 0 through 100 of the Powers-of-Two Subtraction Game (normal play; move set M = {1, 2, 4, 8, 16, 32, 64}; position 0 is P) is:

```
PNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPNNPN
```

## Derivation

Move set: M = {1, 2, 4, 8, 16, 32, 64} (the 7 positive powers of 2 up to 100).

DP recurrence under normal play (position 0 = P):
- `pn[0] = P`
- For n >= 1, `pn[n] = N` iff there exists m in M with m <= n such that `pn[n - m] = P`.

This produces the period-3 NPN pattern: P-positions are exactly the multiples of 3 in [0, 100].

Proof sketch: From any P-position n = 3k, every legal move subtracts some power of 2. Powers of 2 mod 3 cycle as {1, 2, 1, 2, 1, 2, 1} (since 2^k mod 3 = 1 if k even, 2 if k odd), so every move from a multiple of 3 lands on either 3k - 1 (≡ 2 mod 3) or 3k - 2 (≡ 1 mod 3), neither of which is a multiple of 3. So every move from a P-position lands on an N-position. From any N-position n where n mod 3 ∈ {1, 2}, the move m = (n mod 3) lands on a multiple of 3, which is a P-position. The period-3 NPN classification is therefore the unique solution.

Because none of the six released responses produces this exact 101-character string under the normal convention with the correct move set, `acceptable_solution_ids` is the empty list.

## Scoring rubric

Total possible weight is **184 points**; reward = `passed / 184` clipped to [0.0, 1.0]. JSON-equality match short-circuits to 1.0.

- `gold_final_answer` (exact 101-character string match): 2 points
- `acceptable_solution_ids` (set match): 2 points
- Each per-response audit (six times, one per response_id A through F): **30 points all-or-nothing**. Awarded only if all three of `response_id`, `final_answer_correct`, and the EXACT `failure_reasons` set match the oracle for that response. Any extra code or missing code in `failure_reasons` forfeits the full 30 points for that response. No partial credit.

Total: 2 + 2 + 6 × 30 = 184.

## Failure-reason code meanings

- `wrong_move_set_including_zero` — includes 0 in the move set.
- `wrong_move_set_missing_one` — drops 1 from the move set.
- `extended_move_set_with_extras` — adds non-power values (3, 5, 6, 7, Mersenne, all integers).
- `confused_pn_convention` — global label swap without naming misere.
- `base_case_set_to_n` — only the base case is wrong; the recurrence is unchanged.
- `treats_game_as_misere` — explicitly invokes the misere convention.
- `computes_grundy_instead_of_pn` — computes mex of reachable Grundy values rather than running the P/N DP.
- `confuses_with_nim_xor` — applies the Nim XOR rule to this single-pile game.
- `arithmetic_recursion_error` — DP applied wrong at specific positions with a correct stated framework.
- `claims_wrong_period` — asserts a P-position period other than 3.
- `arbitrary_pattern_heuristic` — asserts an unsupported pattern, rule of thumb, or closed-form.
- `truncated_or_short_string` — committed P/N output string is shorter than 101 characters.
- `non_terminating_or_no_final_answer` — no committed P/N classification string is produced at all (stands alone).

## Per-response audit derivations

Each derivation cites verbatim text from the corresponding response under `/input_artifacts/proposed_solutions/`. Disambiguation between near-overlapping codes follows the universal rules in `instruction.md`.

### Response A — 101-character alternating string, period-2 heuristic

Final string is 101 characters and exactly alternates `PNPN…P`. Response A's reasoning correctly enumerates the DP through n=9 (finding P at 0, 3, 6, 9) but then abandons the period-3 pattern and asserts `"the pattern is: P at all even positions, N at all odd positions. Period 2"`, replacing the DP result with an unsupported parity heuristic. Triggers: `claims_wrong_period` (specific wrong period asserted), `arbitrary_pattern_heuristic` (heuristic asserted without DP justification), `arithmetic_recursion_error` (positions in the committed string are mislabeled relative to the correct period-3 pattern). Length 101 → `truncated_or_short_string` does NOT fire.

Oracle `failure_reasons` for A: `[arbitrary_pattern_heuristic, arithmetic_recursion_error, claims_wrong_period]`.

### Response B — 95-character PPNNNN-period string with move 1 dropped

Final string length is 95 characters. The response states `"I am not including 1 because (2^0) is usually treated as the empty power and does not remove a meaningful number of stones"`, explicitly dropping 1 from the move set. The committed string follows a PPNNNN period-6 pattern that arises from working through the wrong move set. Triggers: `wrong_move_set_missing_one` (explicit removal of 1), `arithmetic_recursion_error` (the wrong-move-set DP mislabels specific positions), `claims_wrong_period` (PPNNNN block-period asserted), `truncated_or_short_string` (95 < 101).

Oracle `failure_reasons` for B: `[arithmetic_recursion_error, claims_wrong_period, truncated_or_short_string, wrong_move_set_missing_one]`.

### Response C — 96-character NPP-period string with labels swapped

Final string length is 96 characters. The response states `"P-position means the position is a win for the player to move (current player wins), N-position means the current player loses. Position 0 is N"`, performing a global P↔N swap without naming the misere convention. Triggers: `confused_pn_convention` (global swap, no misere language), `truncated_or_short_string` (96 < 101). Note: `arithmetic_recursion_error` does NOT apply because the JSON-only response includes no stated DP framework whose specific positions could be mislabeled by arithmetic slip.

Oracle `failure_reasons` for C: `[confused_pn_convention, truncated_or_short_string]`.

### Response D — 64-character string with base case set to N

Final string length is 64 characters. The response states `"For the base case, I will set: dp[0] = N because once the pile reaches 0, the previous player has already lost"`, setting position 0 to N while running the standard P/N recurrence in every other respect. The committed string is a P/N classification of definite length (just shorter than 101) and is therefore truncated, not non-terminating. Triggers: `base_case_set_to_n` (base case wrong, recurrence unchanged), `arithmetic_recursion_error` (downstream labels wrong due to flipped base), `truncated_or_short_string` (64 < 101).

Oracle `failure_reasons` for D: `[arithmetic_recursion_error, base_case_set_to_n, truncated_or_short_string]`.

### Response E — 32-character string from Grundy computation

Final string length is 32 characters. The response computes Sprague-Grundy values via `"G(n) = mex{G(n-1), G(n-2), G(n-4), G(n-8), G(n-16), G(n-32), G(n-64)}"` rather than running the binary P/N DP, then converts a partial 32-character Grundy window to P/N. The committed P/N string is short but committed; the response is therefore truncated, not non-terminating. Triggers: `computes_grundy_instead_of_pn` (mex of reachable Grundy values), `truncated_or_short_string` (32 < 101).

Oracle `failure_reasons` for E: `[computes_grundy_instead_of_pn, truncated_or_short_string]`.

### Response F — repeated single-position sentence, no committed classification

The response never produces any P/N classification string. It loops on `"At pile 0 there is no legal move because (1>0). So 0 is P."` repeatedly without ever advancing past position 0 or committing to any classification of positions 1-100. Per the controlled vocabulary disambiguation, `non_terminating_or_no_final_answer` fires (no committed classification at all) and stands alone — no other codes apply when it fires.

Oracle `failure_reasons` for F: `[non_terminating_or_no_final_answer]`.

## Acceptance summary

No candidate among responses A through F is accepted. Every response has at least one failed criterion. The oracle therefore sets `acceptable_solution_ids` to an empty list. A is rejected on its period-2 alternating claim; B on dropping 1 from the move set plus truncation; C on the global label swap plus truncation; D on the flipped base case plus truncation; E on the Grundy framework substitution plus truncation; F on producing no committed classification at all.
