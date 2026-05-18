# Response collection guide — Two new game-theory audit tasks

This document specifies the 16 model responses you need to collect (8 per task) and how to update the oracle files once you have them. The two task folders are fully built **except** for the response files and the placeholder evidence quotes that depend on them.

## Folders

1. `a1b2c3d4e5f60718293a4b5c6d7e8f90-SWARMBENCH-FANOUT-REASONINGMATH-FIBONACCI-SUBTRACTION-GAME-PN-AUDIT/`
   - Task: P/N classification for positions 0-100 of a single-pile subtraction game with move set = Fibonacci numbers up to 100
   - Gold: irregular pattern, 20 P-positions, max gap 6
2. `0fedcba987654321aabbccddeeff0011-SWARMBENCH-FANOUT-REASONINGMATH-POWERS-OF-TWO-SUBTRACTION-PN-AUDIT/`
   - Task: P/N classification for positions 0-100 of a single-pile subtraction game with move set = {1, 2, 4, 8, 16, 32, 64}
   - Gold: period-3 NPN, P-positions are multiples of 3

## Where to source responses

Per your workflow memory, the right sources are: llama.online, use.ai, Outlier playground. Target weak/fast-tier models:
- Old GPT-4-era variants, GPT-4o-mini, GPT-3.5
- Grok (fast tier)
- Qwen / DeepSeek instant or v1-v2
- Claude Sonnet/Haiku (smaller/older versions)
- Gemma 3n, Gemini Flash
- Llama 3.1 8B, Llama 3.2 1B-3B

For each task, feed the contents of `environment/input_artifacts/problem.md` to a weak model with no prompt engineering ("solve this problem; output your reasoning and final 101-character P/N string"). Save the raw, unedited output verbatim to `environment/input_artifacts/proposed_solutions/response_X.md`.

**Do NOT edit responses to force a particular failure mode.** Collect a candidate, check whether it matches the planned profile below, and if yes save it. If no, discard and try another model. You may need 15-20 model queries to find 8 responses matching the planned profiles.

## Master response profile table — Task 1 (Fibonacci)

| response_id | planned profile | failure_reasons (4 max) | primary_failure_code | how to spot it |
|---|---|---|---|---|
| A | Asserts a clean false period (e.g., "P-positions are multiples of 4" or "period 11") and writes a 101-char string matching that asserted period | arbitrary_pattern_heuristic, arithmetic_recursion_error, claims_periodic_pattern_falsely | claims_periodic_pattern_falsely | Look for "the pattern repeats every k positions", "period k", "P-positions are multiples of k" |
| B | Drops 1 from the Fibonacci move set (interprets the duplicate 1 as a reason to exclude) | arithmetic_recursion_error, claims_periodic_pattern_falsely, wrong_move_set_excluding_one | wrong_move_set_excluding_one | Look for "F = {2, 3, 5, 8, ...}", "since 1 appears twice we exclude it", or move set starting at 2 |
| C | Globally swaps P/N labels without naming misère (position 0 = N because "the player to move just won by having no moves to make") | arithmetic_recursion_error, confused_pn_convention | confused_pn_convention | Position 0 labeled N, otherwise standard recurrence; output is the bitwise complement of gold |
| D | Sets position 0 = N as a base-case-only error (recurrence still computed with normal polarity), output truncated before 101 chars | arithmetic_recursion_error, base_case_set_to_n, truncated_or_short_string | base_case_set_to_n | Position 0 labeled N but P-positions still computed correctly relative to that base, output ends early |
| E | Computes Sprague-Grundy / Nim values instead of P/N, output truncated before 101 chars | applies_nim_sprague_grundy_directly_wrong, truncated_or_short_string | applies_nim_sprague_grundy_directly_wrong | Mentions "Grundy values", "mex", "Sprague-Grundy theorem", "Nim XOR", or outputs integers instead of P/N |
| F | Includes 0 in the move set (treats F0 = 0 as legal), reports a heuristic pattern | arbitrary_pattern_heuristic, arithmetic_recursion_error, wrong_move_set_including_zero | wrong_move_set_including_zero | Look for "F = {0, 1, 2, 3, 5, 8, ...}", or argument that 0 is allowed |
| G | Lucas-style or doubling enumeration of Fibonacci (e.g., "F = {1, 2, 4, 7, 11, ...}"), asserts false period, output truncated | arithmetic_recursion_error, claims_periodic_pattern_falsely, incorrect_fibonacci_enumeration, truncated_or_short_string | incorrect_fibonacci_enumeration | Look for any non-Fibonacci sequence as the move set (the correct sequence is 1, 2, 3, 5, 8, 13, 21, 34, 55, 89) |
| H | Pathological generation — loops on a phrase or truncates mid-sentence without producing a P/N string | non_terminating_or_no_final_answer | non_terminating_or_no_final_answer | Output has no committed 101-char string at all (loop, mid-derivation cut, "Let's denote: ..." repeated) |

## Master response profile table — Task 2 (Powers of 2)

| response_id | planned profile | failure_reasons (4 max) | primary_failure_code | how to spot it |
|---|---|---|---|---|
| A | Asserts period 2 (alternating P and N) — i.e., "even positions are P, odd are N" | arbitrary_pattern_heuristic, arithmetic_recursion_error, claims_wrong_period | claims_wrong_period | Look for "period 2", "alternating", "even positions are P" — output has PNPNPNPN... pattern |
| B | Drops 1 from the move set (starts at 2^1 = 2) | arithmetic_recursion_error, claims_wrong_period, wrong_move_set_missing_one | wrong_move_set_missing_one | Move set = {2, 4, 8, 16, 32, 64}, "the trivial move 1 doesn't count" |
| C | Globally swaps P/N labels without naming misère | arithmetic_recursion_error, confused_pn_convention | confused_pn_convention | Position 0 = N implicitly via misère-style framing without invoking misère |
| D | Sets position 0 = N as base-case-only error, output truncated | arithmetic_recursion_error, base_case_set_to_n, truncated_or_short_string | base_case_set_to_n | Base case wrong, but recurrence otherwise standard; output ends early |
| E | Computes Sprague-Grundy values via mex of reachable Grundy values, output truncated | computes_grundy_instead_of_pn, truncated_or_short_string | computes_grundy_instead_of_pn | Look for "G(n) = mex{G(n-1), G(n-2), G(n-4), ...}" or integer Grundy values reported |
| F | Adds non-power-of-2 values to the move set (e.g., M = {1, 2, 3, 4, 5, 6, 7, 8, ...} or Mersenne {1, 3, 7, 15, 31, 63}) | arbitrary_pattern_heuristic, arithmetic_recursion_error, extended_move_set_with_extras | extended_move_set_with_extras | Look for non-power values in the move set; common mistake is "powers of 2 up to N" misread as "all integers up to N" |
| G | Applies Nim XOR directly to the single pile (treats as multi-pile Nim), asserts wrong period | arithmetic_recursion_error, claims_wrong_period, confuses_with_nim_xor | confuses_with_nim_xor | Look for "by Nim XOR", "applying the XOR rule", or treating pile size as a Nim-sum |
| H | Pathological generation — loops or truncates mid-derivation | non_terminating_or_no_final_answer | non_terminating_or_no_final_answer | No committed P/N string at all |

## Once you have all 16 responses

For each task, after dropping the 8 collected responses into `environment/input_artifacts/proposed_solutions/response_X.md`:

1. **Verify each response actually matches its planned profile.** Read the response, check that the trigger phrases listed in the table above are concretely present. If a response doesn't match its planned profile, either:
   - Edit the oracle's `failure_reasons` set and `primary_failure_code` for that response to match what the response actually does, OR
   - Swap the response for a different one that does match the planned profile.

2. **Update placeholder evidence quotes** in BOTH oracle copies (`tests/oracle.json` AND `solution/oracle.json` — they must remain identical):
   - For each per-response object, every key in `failure_reason_evidence` currently starts with `[PLACEHOLDER >=20 chars] Replace with verbatim quote from response_X...`. Replace each placeholder with a short verbatim (or near-verbatim) quote from the response that demonstrates that trigger. Keep quotes 40-120 characters long.
   - Update each `primary_failure_code_evidence` (currently realistic-sounding descriptions) to cite actual response text. Keep length >= 50 characters.
   - **Do not change** the `failure_reasons` lists, `primary_failure_code` values, `code_application_table` lists, or `response_count_per_code` integers unless step 1 forced a profile swap.

3. **Verify oracle still scores 1.0** by running locally:
   ```
   python tests/judge.py --agent-output solution/oracle.json --oracle tests/oracle.json --reward-out /tmp/r.json
   cat /tmp/r.json   # should print {"reward": 1.0}
   ```
   If the oracle drops below 1.0, the two oracle copies have drifted — re-sync them.

4. **Run the oracle agent through harbor** to populate `execution_logs/oracle/`. Then run single-kimi-agent and multi-kimi-agent to populate the other two log subfolders. Check `judge_justification.txt` in each to confirm reward values and identify any agent-specific issues.

## What's still pending in this workspace (not covered by this hand-off)

- **SEQUENCE-ENVELOPE-AUDIT** and **CUBE-PLANE-DISTANCES-AUDIT**: items 1, 4, 7 from the earlier "what raises pass probability" plan (symmetric mappers, second cascading field, locked-down primary codes) were not yet applied because work shifted to building these two new tasks. Apply them once execution logs come back from the in-flight runs.
- **SQUARE-TRIANGLE-GAME-PN-AUDIT**: folder restored to `task.toml` only; the prior stash 2 contained a different problem (cylinder surface net), not the Square-Triangle game described in task.toml. Needs rebuild from scratch — not addressed in this round.
