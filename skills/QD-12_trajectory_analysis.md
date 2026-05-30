# QD-12: Trajectory Analysis

## Your Role
You are reading the actual execution logs to verify the scores reflect genuine capability differences — not task construction flaws. Numbers in a results table mean nothing if the underlying behavior is broken.

## Explore First
Before evaluating any checks, run `Glob /task/**` to see the full task file tree. The "Files to Read" section below is a minimum starting point — use Read, Grep, and Bash freely on any file that looks relevant to your checks.

## Files to Read
- `/task/execution_logs/multi-kimi-agent/` — find the highest-reward trial, read its `agent/trajectory.json`
- `/task/execution_logs/single-kimi-agent/` — read all trials' `agent/trajectory.json` files
- `/task/execution_logs/*/verifier/` — read `judge_justification.txt` or `test-stdout.txt` where available
- `/task/task.toml` (read `why_multi_agent`)
- `/task/instruction.md`

## Grounding Rule
**Before issuing any FAIL verdict, you MUST copy the exact verbatim text from the specific file that triggered the violation into your `reason` field.** If you cannot produce an exact quote from that file, the check PASSES. Do not infer, paraphrase, or reconstruct — only quote what is literally present.

## Multi-Agent Checks (best scoring run)
1. **Sub-agents received adequate context** — Each spawned sub-agent's prompt contains the file paths, output format, and analysis criteria it needs. FAIL if sub-agents received vague or incomplete prompts — failures are from poor orchestration, not task difficulty.
2. **No redundant sub-agents** — Each sub-agent did distinct work — no two processed the same data for the same purpose. FAIL if multiple agents did identical work.
3. **Synthesis step exists** — Orchestrator aggregated sub-agent results before writing final output. FAIL if outputs were concatenated without synthesis, or orchestrator wrote output without waiting for all sub-agents.
4. **Room for decomposition improvement** — The decomposition as executed was near-optimal. FAIL if obvious improvements exist — sub-tasks could be split further, merged, or reordered to significantly improve the score. Flag for trainer to revise `decomposition.yaml`.
5. **Failures are genuine** — Any fields the multi-agent scored 0 on are genuinely hard, not caused by task construction issues. FAIL if failures trace back to missing spec in instruction, wrong oracle value, or broken verifier.

## Single-Agent Checks (all runs)
6. **Failure is structural** — Single agent failed due to context limits, attention degradation, or timeout — the structural reasons claimed in `why_multi_agent`. FAIL if single agent failed due to missing information in instruction, wrong file path, or verifier bug.
7. **No sub-agent spawning** — Single agent trajectory shows zero Task/CreateSubagent tool calls. FAIL if single agent spawned sub-agents despite tool restriction.
8. **Agent attempted the task** — Single agent read input files and made a genuine attempt. FAIL if agent immediately wrote empty output or timed out without reading any input.
9. **False failure check** — Low scores are from incorrect answers, not format mismatches or missing fields the prompt didn't mention. FAIL if judge justification shows score=0 on fields the instruction never specified.
10. **No infrastructure errors in any run** — Search trajectory files, wire logs, and test-stdout.txt across BOTH single and multi agent runs. Classify any error you find before deciding:

   **Always-infra (FAIL) — agent cannot recover from these:**
   - API key errors (401, "UNAUTHORIZED", "provide an API Key") on the LLM endpoint
   - Rate limits (429, "Too Many Requests") on the LLM endpoint
   - Docker/container errors
   - OS-level network timeouts ("ETIMEDOUT") in the harness wire logs

   **Verifier-side missing modules (FAIL) — blocks measurement:**
   - `ModuleNotFoundError` / `ImportError` raised by code under `verifier/` (reward.py, judge script, solve.sh self-check). The verifier MUST be able to run; if it can't import its deps, the score is unmeasurable.

   **Agent-side missing modules (PASS) — normal agent behavior:**
   - `ModuleNotFoundError` / `ImportError` appearing as the **observation** of an agent shell/Python tool call. The container has pip and network. A `pip install` is a valid agent action. Two cases:
     * Agent ran `pip install`, switched approach, or otherwise made progress after the error → PASS. Do NOT flag.
     * Agent never attempted recovery → still PASS for this check. The failure is an agent-skill issue, not infra; the score already reflects it.
   - Quote the recovery step (or its absence) in `reason` so the verdict is auditable.

   **Timeout rules:** `AgentTimeoutError` in single-agent `exception.txt` is expected and intentional — single agent is supposed to run out of time. `AgentTimeoutError` in multi-agent `exception.txt` is a FAIL — multi-agent must complete within the timeout. Also verify that the timeout seconds in single-agent's `exception_info.exception_message` (e.g. "Agent execution timed out after 60.0 seconds") matches `[agent] timeout_sec` in `task.toml` — a mismatch means task.toml was changed between runs and the benchmark measurement is invalid.

   **Checksum rule:** do NOT use `task_checksum` mismatches across runs as evidence of task.toml modification — the checksum is computed over the entire task directory (including execution_logs/ written fresh each run), so different checksums per run are expected and normal.

   FAIL only for: always-infra errors, verifier-side missing modules, multi-agent timeout, or timeout-value mismatch.

## Output Format
Return ONLY valid JSON:
```json
{
  "dimension": "QD-12",
  "result": "PASS" or "FAIL",
  "checks": [
    {"id": 1, "name": "sub_agent_context", "result": "...", "reason": "..."},
    {"id": 2, "name": "no_redundant_agents", "result": "...", "reason": "..."},
    {"id": 3, "name": "synthesis_exists", "result": "...", "reason": "..."},
    {"id": 4, "name": "decomposition_near_optimal", "result": "...", "reason": "..."},
    {"id": 5, "name": "failures_genuine", "result": "...", "reason": "..."},
    {"id": 6, "name": "structural_failure", "result": "...", "reason": "..."},
    {"id": 7, "name": "no_sub_agent_spawning", "result": "...", "reason": "..."},
    {"id": 8, "name": "agent_attempted", "result": "...", "reason": "..."},
    {"id": 9, "name": "no_false_failures", "result": "...", "reason": "..."},
    {"id": 10, "name": "no_infra_errors", "result": "...", "reason": "..."}
  ],
  "justification": "Overall assessment in 2-3 sentences."
}
```
Result is FAIL if ANY check fails.