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

Proof sketch: From any P-position n = 3k, the only legal moves are to n - 1, n - 2, n - 4, n - 8, ... — i.e., subtracting any power of 2. Powers of 2 mod 3 cycle as {1, 2, 1, 2, 1, 2, 1} (since 2^k mod 3 = 1 if k even, 2 if k odd), so every move from a multiple of 3 lands on either 3k - 1 (≡ 2 mod 3) or 3k - 2 (≡ 1 mod 3), neither of which is a multiple of 3 — so every move from a P-position lands on an N-position. From any N-position n where n mod 3 ∈ {1, 2}, the move m = (n mod 3) lands on a multiple of 3, which is a P-position. So the period-3 NPN classification is the unique solution.

Because none of the eight released responses produces this exact 101-character string under the normal convention with the correct move set, `acceptable_solution_ids` is the empty list.

## Scoring rubric

Total possible weight is **2503 points**; reward = `earned / 2503` clipped to [0.0, 1.0]. JSON-equality match short-circuits to 1.0.

- `gold_final_answer`: 4
- `acceptable_solution_ids`: 2
- Per response (8 responses, 99 fixed points each = 792): final_answer_correct 5 + failure_reasons 30 + primary_failure_code 25 + primary_failure_code_evidence 8 + alternative_codes_considered 8 + code_application_count 10 + primary_in_set_check 5 + evidence_key_completeness 8
- `failure_reason_evidence`: 5 per oracle-listed failure-reason code (sum across all 8 responses is 23 codes × 5 = 115)
- `code_application_table`: 13 keys × 100 = 1300
- `response_count_per_code`: 13 keys × 20 = 260
- `cross_response_observations`: 30

Total: 4 + 2 + 792 + 115 + 1300 + 260 + 30 = 2503.

## Failure-reason code meanings

- `wrong_move_set_including_zero` — includes 0 in the move set.
- `wrong_move_set_missing_one` — drops 1 from the move set.
- `extended_move_set_with_extras` — adds non-power values (3, 5, 6, 7, Mersenne).
- `confused_pn_convention` — global label swap without naming misère.
- `base_case_set_to_n` — only the base case is wrong; rest of DP unchanged.
- `treats_game_as_misere` — explicitly invokes the misère convention.
- `computes_grundy_instead_of_pn` — computes mex of reachable Grundy values.
- `confuses_with_nim_xor` — applies Nim XOR to this single-pile game.
- `arithmetic_recursion_error` — DP applied wrong at specific positions with correct framework.
- `claims_wrong_period` — asserts a period other than 3.
- `arbitrary_pattern_heuristic` — asserts an unsupported pattern.
- `truncated_or_short_string` — output shorter than 101 characters.
- `non_terminating_or_no_final_answer` — no committed final classification.

## Per-response audit derivations

Each derivation cites verbatim text from the corresponding response under `/input_artifacts/proposed_solutions/`. The chosen `primary_failure_code` follows the universal selection rules stated in `instruction.md` (move-set / convention / base-case / framework errors are upstream of `arithmetic_recursion_error`, `claims_wrong_period`, and `arbitrary_pattern_heuristic`; `truncated_or_short_string` is never primary when any other code applies).

### Response A — 101-char alternating string

Final string is 101 characters and exactly alternates `PNPN…P`. Response A asserts `"Thus all even positions are P and all odd positions are N"`, which is a period-2 pattern, asserted without DP verification. This triggers `claims_wrong_period` (specific wrong period asserted), `arbitrary_pattern_heuristic` (heuristic asserted without DP), and `arithmetic_recursion_error` (specific positions mislabeled). Per the selection rules, primary is `claims_wrong_period`. String length 101 → `truncated_or_short_string` does NOT fire.

### Response B — 95-char PPNNNN-period string with move 1 dropped

Final string length is 95 (below the 101-character threshold). The response states `"I am not including 1 because (2^0) is usually treated as the empty power and does not remove a meaningful number of stones"`, dropping 1 from the move set. The truncated string follows a PPNNNN period-6 pattern that arises from working through the wrong move set. Triggers: `wrong_move_set_missing_one` (explicit removal of 1), `arithmetic_recursion_error` (the wrong-move-set DP mislabels specific positions), `claims_wrong_period` (PPNNNN block-period asserted), `truncated_or_short_string` (95 < 101 chars). Per the selection rules, primary is `wrong_move_set_missing_one` (move-set defect upstream of arithmetic and period claims; truncation never primary).

### Response C — 96-char NPP-period string with labels swapped

Final string length is 96 (below threshold). The response states `"This is just the normal recurrence but with the labels reversed from the usual convention"`, performing a global P↔N swap without naming the misère convention. Triggers: `confused_pn_convention` (global swap, no misère language), `arithmetic_recursion_error` (specific positions labeled wrong due to inversion), `truncated_or_short_string` (96 < 101 chars). Per the selection rules, primary is `confused_pn_convention` (convention defect upstream; truncation never primary).

### Response D — 64-char truncated DP with base case 0=N

Final string length is 64 (below threshold). The response states `"For the base case, I will set: dp[0]=N because once the pile reaches 0, the previous player has already lost"`, setting position 0 to N while otherwise running the standard P/N recurrence. Triggers: `base_case_set_to_n` (base case wrong, recurrence unchanged), `arithmetic_recursion_error` (downstream labels wrong due to flipped base), `truncated_or_short_string` (64 < 101 chars). Per the selection rules, primary is `base_case_set_to_n` (upstream of arithmetic; truncation never primary).

### Response E — 30-char string after computing Grundy values

Final string length is 30 (below threshold). The response computes Sprague-Grundy values via `"G(n)=mex{G(n-1),G(n-2),G(n-4),G(n-8),G(n-16),G(n-32),G(n-64)}"` rather than running the binary P/N DP, then converts a partial 30-character window to P/N. Triggers: `computes_grundy_instead_of_pn` (mex of reachable Grundy values), `truncated_or_short_string` (30 < 101 chars). Per the selection rules, primary is `computes_grundy_instead_of_pn` (framework misapplication upstream; truncation never primary).

### Response F — 100-char near-trivial string with inflated move set

Final string length is 100 (below threshold by one). The response states `"Equivalently, the move set is: {1,2,3,4,5,6,7,8,...,100}"`, expanding the move set to all positive integers up to 100. With every nonzero subtraction allowed, every nonzero position is trivially N. Triggers: `extended_move_set_with_extras` (non-power values added), `arithmetic_recursion_error` (positions mislabeled under the wrong move set), `arbitrary_pattern_heuristic` (`"from every nonzero pile the player can remove the entire pile and win immediately"` is an unsupported heuristic), `truncated_or_short_string` (100 < 101 chars). Per the selection rules, primary is `extended_move_set_with_extras` (move-set defect upstream; truncation never primary).

### Response G — 101-char alternating string from Nim XOR

Final string is 101 characters. The response states `"This is basically Nim with one pile, so we can use the XOR rule. A position is losing when the Nim-sum is zero"`, applying Nim XOR directly to a single-pile subtraction game, then derives period 2 from XOR parity. Triggers: `confuses_with_nim_xor` (Nim XOR applied directly to a non-Nim game), `claims_wrong_period` (period 2 asserted), `arithmetic_recursion_error` (specific positions mislabeled). String length 101 → `truncated_or_short_string` does NOT fire. Per the selection rules, primary is `confuses_with_nim_xor` (framework defect upstream of arithmetic and period).

### Response H — repeated single-position sentence, no committed classification

Final committed P/N classification string is absent. The response loops on `"At pile 0 there is no legal move because (1>0). So 0 is P."` fifteen times without ever advancing past position 0 or producing a P/N string. Trigger: `non_terminating_or_no_final_answer` (no committed classification at all). Per the controlled vocabulary, this code stands alone — no other codes apply when it fires.

## code_application_table

| code | response_ids |
|---|---|
| wrong_move_set_including_zero | (empty) |
| wrong_move_set_missing_one | B |
| extended_move_set_with_extras | F |
| confused_pn_convention | C |
| base_case_set_to_n | D |
| treats_game_as_misere | (empty) |
| computes_grundy_instead_of_pn | E |
| confuses_with_nim_xor | G |
| arithmetic_recursion_error | A, B, C, D, F, G |
| claims_wrong_period | A, B, G |
| arbitrary_pattern_heuristic | A, F |
| truncated_or_short_string | B, C, D, E, F |
| non_terminating_or_no_final_answer | H |

## Acceptance summary

No candidate among responses A through H is accepted. Every response has at least one failed criterion. The oracle therefore sets `acceptable_solution_ids` to an empty list. A is rejected on its period-2 alternating claim; B on dropping 1 from the move set plus truncation; C on the global label swap plus truncation; D on the flipped base case plus truncation; E on the Grundy framework substitution plus truncation; F on the inflated move set plus truncation; G on misapplying Nim XOR to a single-pile game; H on producing no committed classification at all. The single most common downstream code is `arithmetic_recursion_error` (six responses) but it is never primary because in each case an upstream framework or specification defect accounts for the wrong labels. Five of the eight responses also trigger `truncated_or_short_string` because their committed P/N strings are shorter than 101 characters; truncation is never primary per the selection rules.
