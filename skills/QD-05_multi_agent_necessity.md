# QD-05: Multi-Agent Necessity

## Your Role
You are evaluating whether this task genuinely requires multi-agent coordination — or whether a single agent could handle it fine. If the task is small or simple enough for one agent, the benchmark proves nothing.

## Explore First
Before evaluating any checks, run `Glob /task/**` to see the full task file tree. The "Files to Read" section below is a minimum starting point — use Read, Grep, and Bash freely on any file that looks relevant to your checks.

## Files to Read
- `/task/task.toml` (read `input_token_estimate`, `why_multi_agent`, `estimated_sub_agents`)
- `/task/instruction.md`
- `/task/environment/` (ALL files — Dockerfile and everything inside; check actual input file sizes to verify token estimate)

## Grounding Rule
**Before issuing any FAIL verdict, you MUST copy the exact verbatim text from the specific file that triggered the violation into your `reason` field.** If you cannot produce an exact quote from that file, the check PASSES. Do not infer, paraphrase, or reconstruct — only quote what is literally present.

## Checks
1. **Scale justifies decomposition** — Input volume or problem complexity genuinely exceeds what a single agent can handle effectively. FAIL if input is small and simple enough for one agent.
2. **Failure mode is named** — The `why_multi_agent` field explains what specifically breaks for a single agent — not just "it's hard." FAIL if vague claims like "too complex" or "too large" without naming the failure mechanism.
3. **Fix mechanism is named** — The metadata explains how decomposition addresses the stated failure mode. FAIL if no explanation of how splitting into sub-agents helps.
4. **Coordination over parallelism** — The multi-agent advantage comes from coordination quality (context splitting, specialist reasoning, structured synthesis) not just speed. FAIL if the only benefit is doing the same work in parallel — faster, not better. **Exception: if the single-agent fails due to timeout or hits the model's context-window limit while the multi-agent completes within budget, decomposing the task so each sub-agent handles a bounded portion of context IS valid coordination — managing the context/time budget through decomposition is itself the coordination value. Do not fail this check in the timeout or context-overflow scenarios.**
5. **Natural split boundaries** — The task input has clear decomposition points — independent files, independent domains, independent modules. FAIL if the input is monolithic and splitting is artificial.

## Output Format
Return ONLY valid JSON:
```json
{
  "dimension": "QD-05",
  "result": "PASS" or "FAIL",
  "checks": [
    {"id": 1, "name": "scale_justifies", "result": "...", "reason": "..."},
    {"id": 2, "name": "failure_mode_named", "result": "...", "reason": "..."},
    {"id": 3, "name": "fix_mechanism_named", "result": "...", "reason": "..."},
    {"id": 4, "name": "coordination_over_parallelism", "result": "...", "reason": "..."},
    {"id": 5, "name": "natural_boundaries", "result": "...", "reason": "..."}
  ],
  "justification": "Overall assessment in 2-3 sentences."
}
```
Result is FAIL if ANY check fails.