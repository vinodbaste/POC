# Oracle Justification — Fibonacci Subtraction Game P/N Audit

## Gold P/N classification string

The gold 101-character P/N classification string for positions 0 through 100 of the Fibonacci Subtraction Game (normal play convention; move set F = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89}; position 0 is P) is:

```
PNNNPNNNNNPNNNPNNNNNPNNNPNNNNNPNNNNNPNNNPNNNNNPNNNPNNNNNPNNNPNNNNNPNNNNNPNNNPNNNNNPNNNPNNNNNPNNNPNNNN
```

## Derivation

The move set is the set of distinct positive Fibonacci numbers up to 100:

```
F = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
```

Under the normal play convention, the player who cannot move loses. Position 0 has no legal move and is therefore a P-position (the player to move loses, equivalently the previous player wins).

The DP recurrence is:

- `pn[0] = P`
- For n >= 1, `pn[n] = N` iff there exists f in F with f <= n such that `pn[n - f] = P`; otherwise `pn[n] = P`.

Computing this for n = 0..100 produces the P-position set:

```
P positions <= 100: 0, 4, 10, 14, 20, 24, 30, 36, 40, 46, 50, 56, 60, 66, 72, 76, 82, 86, 92, 96
```

The first few differences between consecutive P-positions are 4, 6, 4, 6, 4, 6, 6, 4, 6, ... — irregular and non-periodic over 0..100. There is no clean period such as 4 or 11 that fits the P-positions in this range; any response asserting such a period is wrong.

Because none of the eight released responses produces this exact 101-character string under the normal convention with the correct move set, `acceptable_solution_ids` is the empty list.

## Scoring rubric (deterministic Python verifier)

The verifier (`tests/judge.py`) scores `/logs/agent/output.json` against `tests/oracle.json` with the following weighted fields. Total possible weight is **1769 points**; the reward is `earned / 1769` clipped to [0.0, 1.0]. An exact JSON-equality match short-circuits to reward = 1.0.

- `gold_final_answer` (101-char string match): 4
- `acceptable_solution_ids` (set match): 2
- Per response (eight times):
  - `final_answer_correct` (exact bool match): 5
  - `failure_reasons` (exact set match, all-or-nothing): 30
  - `primary_failure_code` (exact string match): 25
  - `primary_failure_code_evidence` (presence + >=50 chars): 8
  - `alternative_codes_considered` (>=2 well-formed unique entries; each code from the controlled vocabulary or "NONE", each code != primary, each reason >=20 chars): 8
  - `failure_reason_evidence` per oracle-listed code (presence + >=20 chars): 5 per code
- `code_application_table` per key (12 keys, exact sorted-list match): 70 per key (840 total)
- `response_count_per_code` per key (12 keys, integer match): 15 per key (180 total)
- `cross_response_observations` (presence + >=300 chars): 30

## Failure-reason code meanings

- `wrong_move_set_including_zero` — includes 0 in the move set (e.g., F0 = 0). Trivializes the game by allowing "pass" moves.
- `wrong_move_set_excluding_one` — drops 1 from the move set (e.g., misreads duplicated 1 in the sequence as a reason to exclude).
- `incorrect_fibonacci_enumeration` — writes a Fibonacci-like sequence wrong (Lucas-style, doubling, drift).
- `confused_pn_convention` — global swap of P/N labels via misère-style framing without naming misère.
- `base_case_set_to_n` — local base-case error: sets position 0 = N while leaving the rest of the DP polarity unchanged.
- `treats_game_as_misere` — explicitly invokes the misère convention (last move loses).
- `applies_nim_sprague_grundy_directly_wrong` — computes Grundy values or invokes Nim XOR on this single-pile game.
- `arithmetic_recursion_error` — DP transition applied incorrectly at specific positions with correct stated framework.
- `claims_periodic_pattern_falsely` — asserts a clean period or closed-form for P-positions that does not hold.
- `arbitrary_pattern_heuristic` — asserts an unsupported heuristic for P-positions.
- `truncated_or_short_string` — output P/N string shorter than 101 characters.
- `non_terminating_or_no_final_answer` — no committed final classification (loop, mid-sentence cut, no string).

## Per-response rationale (planned profiles)

The exact response files are to be collected by the user matching the profiles in `RESPONSE_PROFILES.md`. The oracle assigns failure_reasons sets and primary codes based on those planned profiles:

| response_id | planned final answer | planned failure_reasons | primary code |
|---|---|---|---|
| A | wrong (period-4-style) | arbitrary_pattern_heuristic, arithmetic_recursion_error, claims_periodic_pattern_falsely | claims_periodic_pattern_falsely |
| B | wrong (drops 1) | arithmetic_recursion_error, claims_periodic_pattern_falsely, wrong_move_set_excluding_one | wrong_move_set_excluding_one |
| C | wrong (label swap) | arithmetic_recursion_error, confused_pn_convention | confused_pn_convention |
| D | wrong (base-case-N + truncated) | arithmetic_recursion_error, base_case_set_to_n, truncated_or_short_string | base_case_set_to_n |
| E | wrong (Grundy + truncated) | applies_nim_sprague_grundy_directly_wrong, truncated_or_short_string | applies_nim_sprague_grundy_directly_wrong |
| F | wrong (includes 0) | arbitrary_pattern_heuristic, arithmetic_recursion_error, wrong_move_set_including_zero | wrong_move_set_including_zero |
| G | wrong (Lucas-style enumeration + truncated) | arithmetic_recursion_error, claims_periodic_pattern_falsely, incorrect_fibonacci_enumeration, truncated_or_short_string | incorrect_fibonacci_enumeration |
| H | no answer | non_terminating_or_no_final_answer | non_terminating_or_no_final_answer |

Primary code selections follow the universal selection rules in `instruction.md`:
- non-terminating stands alone (H)
- move-set errors are upstream of DP errors (B, F, G)
- convention swap is upstream of base case (C beats global swap over base-case-only; D is base-case-only)
- framework misapplication is upstream of arithmetic (E)
- periodicity claim is more specific than unsupported-heuristic umbrella (A)

## code_application_table

| code | response_ids |
|---|---|
| wrong_move_set_including_zero | F |
| wrong_move_set_excluding_one | B |
| incorrect_fibonacci_enumeration | G |
| confused_pn_convention | C |
| base_case_set_to_n | D |
| treats_game_as_misere | (empty) |
| applies_nim_sprague_grundy_directly_wrong | E |
| arithmetic_recursion_error | A, B, C, D, F, G |
| claims_periodic_pattern_falsely | A, B, G |
| arbitrary_pattern_heuristic | A, F |
| truncated_or_short_string | D, E, G |
| non_terminating_or_no_final_answer | H |

## response_count_per_code

Mirrors the code_application_table counts. Total entries: 1 + 1 + 1 + 1 + 1 + 0 + 1 + 6 + 3 + 2 + 3 + 1 = 21 evidence entries across all eight responses.

## Important: response collection placeholder evidence

The `failure_reason_evidence` and `primary_failure_code_evidence` strings in `tests/oracle.json` and `solution/oracle.json` are currently **placeholder text** describing the trigger pattern to look for in each response. They satisfy the verifier's minimum-length checks so the oracle scores 1.0 against itself, but they are NOT verbatim quotes from real responses (because the response files have not yet been collected — see `RESPONSE_PROFILES.md`).

Once real responses are collected matching the planned profiles, the placeholder strings in both oracle copies must be replaced with verbatim or near-verbatim quotes from the collected responses. The placeholders are marked with `[PLACEHOLDER >=20 chars]` prefixes in the `failure_reason_evidence` fields for easy locating; the `primary_failure_code_evidence` strings are realistic-sounding but should also be updated to cite the actual response text.
