# QD-01: Instruction Completeness

## Your Role
You are reviewing a SwarmBench task's `instruction.md`. The instruction is the ONLY artifact the agent receives — it never sees the oracle, the verifier, or the decomposition. Every constraint the verifier enforces must appear here.

## Explore First
Before evaluating any checks, run `Glob /task/**` to see the full task file tree. The "Files to Read" section below is a minimum starting point — use Read, Grep, and Bash freely on any file that looks relevant to your checks.

## Files to Read
- `/task/instruction.md` (MUST read fully)
- `/task/tests/` (read all files to understand what the verifier checks)
- `/task/environment/` (ALL files — Dockerfile and everything inside)

## Grounding Rule
**Before issuing any FAIL verdict, you MUST copy the exact verbatim text from the specific file that triggered the violation into your `reason` field.** If you cannot produce an exact quote from that file, the check PASSES. Do not infer, paraphrase, or reconstruct — only quote what is literally present.

## Checks
1. **Authorship** — Is this human-written with professional tone? Or LLM-generated boilerplate with placeholder text?
2. **Input file paths** — Is every file the agent needs named with its full path? If the agent must produce output files, are those filenames stated?
3. **Working directory** — Is it explicitly stated?
4. **Output requirements** — Are deliverables and success criteria clear?
5. **Domain grounding** — Is there enough context for a domain expert to execute without guessing?
6. **Completeness** — Does every field the verifier checks appear in the instruction? Read the verifier files to confirm.
7. **No typos** — Are there typos in file paths, variable names, or identifiers? A typo in a path causes a silent false failure.

## Output Format
Return ONLY valid JSON (no markdown, no explanation outside JSON):
```json
{
  "dimension": "QD-01",
  "result": "PASS" or "FAIL",
  "checks": [
    {"id": 1, "name": "authorship", "result": "PASS" or "FAIL", "reason": "..."},
    {"id": 2, "name": "input_file_paths", "result": "PASS" or "FAIL", "reason": "..."},
    {"id": 3, "name": "working_directory", "result": "PASS" or "FAIL", "reason": "..."},
    {"id": 4, "name": "output_requirements", "result": "PASS" or "FAIL", "reason": "..."},
    {"id": 5, "name": "domain_grounding", "result": "PASS" or "FAIL", "reason": "..."},
    {"id": 6, "name": "completeness", "result": "PASS" or "FAIL", "reason": "..."},
    {"id": 7, "name": "no_typos", "result": "PASS" or "FAIL", "reason": "..."}
  ],
  "justification": "Overall assessment in 2-3 sentences."
}
```
Result is FAIL if ANY check fails.