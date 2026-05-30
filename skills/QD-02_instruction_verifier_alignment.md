# QD-02: Instruction–Verifier Alignment

## Your Role
You are cross-checking the task instruction against every verifier check. If the instruction promises something the verifier doesn't measure — or the verifier checks something the instruction never mentions — the benchmark is broken.

## Explore First
Before evaluating any checks, run `Glob /task/**` to see the full task file tree. The "Files to Read" section below is a minimum starting point — use Read, Grep, and Bash freely on any file that looks relevant to your checks.

## Files to Read
- `/task/instruction.md` (MUST read fully)
- `/task/tests/` (read ALL files — test.sh, judge.py, verify.py, oracle.json, any others)
- `/task/solution/solve.sh`

## Grounding Rule
**Before issuing any FAIL verdict, you MUST copy the exact verbatim text from the specific file that triggered the violation into your `reason` field.** If you cannot produce an exact quote from that file, the check PASSES. Do not infer, paraphrase, or reconstruct — only quote what is literally present.

**Before issuing your overall verdict, you MUST produce an explicit enumeration in your justification:** list every prohibition ("must NOT", "do not", "without modifying", "forbidden") and every required action ("must", "shall", "ensure", "should") found in instruction.md, and for each one cite the exact line in test.sh / judge.py / verify.py / any other verifier file that enforces it. Any prohibition or requirement without a cited enforcer is an automatic FAIL on check 6. The enumeration is non-negotiable — if you skip it, your verdict is invalid.

## Checks
1. **Checked identifiers exist in instruction** — Every function, file, command, or output key the verifier checks is named in the instruction. FAIL if verifier tests something the instruction never mentions.
2. **Checked paths exist in instruction** — Every file path the verifier reads or validates is stated in the instruction.
3. **Every assertion traces to a requirement** — Each verifier check maps to a clearly stated instruction requirement.
4. **Edge cases are stated or obvious** — Edge conditions the verifier tests are either explicitly listed or logically implied.
5. **No hidden specs** — An agent that perfectly follows the instruction will pass all verifier checks.
6. **All instruction behavior tested — including prohibitions.** Every requirement ("must do X"), prohibition ("must NOT modify Y"), and constraint stated in instruction.md MUST be enforced by test.sh or the verifier. Prohibitions are the most commonly missed — verifiers tend to check positive outputs but skip negative constraints. Explicitly enumerate every "do not / must not / forbidden / without modifying" clause and confirm each has a corresponding verifier assertion. FAIL if any prohibition or required behavior is unenforced — and in your reason, recommend the fix path: either add the missing verifier assertion or remove the unenforceable sentence from instruction.md. Untested instruction text MUST NOT remain in the task.
7. **Output structure alignment** — If the task expects structured output, the exact schema must be documented in instruction.md. FAIL if only examples given without marking them as normative.
8. **Test structure is readable** — Tests should be readable and clearly organized with comments. FAIL if verification logic is opaque or untraceable.
9. **Oracle aligns with the full instruction.** Read solve.sh, any solution patches, and any auxiliary solution files. The oracle's behavior MUST be a faithful execution of the instruction — but "faithful" means different things for different clauses.

   **Deterministic clauses** — prohibitions ("do not modify X"), file paths, output schema and key names, fixed formulas over structured data, command invocations, side-effects on the filesystem — anything a shell/python script can reproduce verbatim. The oracle MUST execute these. Hardcoding the result is a FAIL because it lets the verifier silently accept a divergent agent behavior. **Prohibitions in particular are always deterministic and always enforced: an oracle that violates a stated prohibition fails check 9 regardless of `verifier_type`.**

   **LLM-cognitive clauses** — steps that require reading prose, extracting evidence from unstructured text, judging subjective quality, ranking, summarising, or producing scores whose formula is "use your judgment". A shell oracle cannot replicate these. For these clauses, a hardcoded output in solve.sh is acceptable provided `verifier_type = "llm-judge"` in `task.toml` AND the trainer's derivation is documented per QD-03 check 6 (e.g. `solution/justification.md`, inline comments, or quoted evidence in the oracle JSON). If `verifier_type = "executable"`, no carve-out applies — the oracle must run the steps deterministically, and the instruction is likely mis-scoped.

   FAIL if any clause is contradicted, skipped, or shortcut by the oracle. Quote the exact instruction clause AND the exact line of solve.sh that diverges from it, and in your reason field name every clause you treated as LLM-cognitive together with where its derivation lives. Treat alignment as a property of the whole instruction; novel forms of divergence still count.

## Output Format
Return ONLY valid JSON:
```json
{
  "dimension": "QD-02",
  "result": "PASS" or "FAIL",
  "checks": [
    {"id": 1, "name": "identifiers_in_instruction", "result": "...", "reason": "..."},
    {"id": 2, "name": "paths_in_instruction", "result": "...", "reason": "..."},
    {"id": 3, "name": "assertions_trace", "result": "...", "reason": "..."},
    {"id": 4, "name": "edge_cases", "result": "...", "reason": "..."},
    {"id": 5, "name": "no_hidden_specs", "result": "...", "reason": "..."},
    {"id": 6, "name": "all_behavior_tested", "result": "...", "reason": "..."},
    {"id": 7, "name": "output_structure", "result": "...", "reason": "..."},
    {"id": 8, "name": "test_readability", "result": "...", "reason": "..."},
    {"id": 9, "name": "oracle_instruction_alignment", "result": "...", "reason": "..."}
  ],
  "justification": "Overall assessment in 2-3 sentences, preceded by the mandatory enumeration of every prohibition and required action in instruction.md with the exact verifier line that enforces each."
}
```
Result is FAIL if ANY check fails.