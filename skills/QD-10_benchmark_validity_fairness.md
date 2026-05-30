# QD-10: Benchmark Validity & Fairness

## Your Role
You are checking whether the single-agent vs multi-agent comparison is fair. If the multi-agent gets unfair advantages — domain knowledge the single agent doesn't have, or a decomposition that essentially solves the problem — the benchmark number is misleading.

## Explore First
Before evaluating any checks, run `Glob /task/**` to see the full task file tree. The "Files to Read" section below is a minimum starting point — use Read, Grep, and Bash freely on any file that looks relevant to your checks.

## Files to Read
- `/task/decomposition.yaml`
- `/task/instruction.md`
- `/task/task.toml` (read `coordination_pattern` and `verifier_type`)
- `/task/environment/` (ALL files — Dockerfile and everything inside; check for helper scripts in input artifacts)
- `/task/execution_logs/multi-kimi-agent/` (read the highest-reward trial's trajectory for check 6 ONLY)
- `/task/tests/` (read ALL files for check 9)

## Grounding Rule
**Before issuing any FAIL verdict on any check, you MUST copy the exact verbatim text from the file being evaluated that triggered the violation into your `reason` field.** If you cannot produce an exact quote from that specific file, the check PASSES. Do not infer, paraphrase, or reconstruct text — only quote what is literally present.

## Checks
1. **Same role-neutral instruction, no mode-dependent scoring promises.** Both single and multi agent receive the identical task instruction. `instruction.md` must describe ONLY what to compute, what inputs to use, and what schema to produce — never how the work will be organized AND never how the score will be adjusted based on the agent's process. Two failure modes to check:

   **(a) Orchestration-language leak.** FAIL if `instruction.md` contains multi-agent-only execution language such as assigning work to "each agent", referring to "map agents", "sub-agents", "shards", "your module assignment", or saying that "a synthesizer agent will run after all agents finish". These orchestration details belong in `decomposition.yaml`, not in the shared `instruction.md`. Example violations: *"Each agent in this task is assigned one SciPy module"*, *"A synthesizer agent will run after all 16 map agents finish"*.

   **(b) Mode-dependent scoring-rubric leak.** FAIL if `instruction.md` describes scoring rubric details that are keyed on the agent's PROCESS rather than its OUTPUT — bonuses or penalties for sub-agent coordination, trajectory marker presence, delegation counts, map/reduce structure, orchestration evidence, or any other process-shape signal. The agent's process is invisible to the grading; only output quality against the oracle is graded. Example violations: *"You will receive +40 points for evidence of sub-agent coordination in your trajectory"*, *"-45 if the trajectory does not contain map-reduce markers"*, *"Orchestration patterns will be rewarded"*, *"Score bonus awarded for delegating to specialist agents"*. This pairs with QD-14 Check 1, which forbids the verifier from APPLYING such mode-dependent adjustments — the instruction must not PROMISE them either. The principle is symmetric: process is invisible on both the input side (instruction) and the output side (verifier).
2. **Same timeout** — Both configurations have the same `agent.timeout_sec`. FAIL if asymmetric timeouts.
3. **Coordination-driven gap** — Multi-agent advantage comes from coordination quality — context splitting, specialist reasoning, structured synthesis. FAIL if gap is only from parallelism (same work faster, not better). **Exception: if the single-agent fails due to timeout while the multi-agent completes within the same timeout, a parallelism-driven gap is acceptable — decomposing context across sub-agents to fit within the timeout budget is a valid coordination mechanism, not mere speed. Do not fail this check when the timeout scenario in check 8 applies.**
4. **Decomposition is guidance, consistent with instruction.** `decomposition.yaml` and `instruction.md` are both agent-facing — the multi-agent orchestrator reads both, single-agent reads only `instruction.md`. Two failure modes are equally forbidden:

   **(a) Leak direction (existing).** `decomposition.yaml` teaches analytical methods, domain-specific vocabulary, or solution rules that are NOT ALSO present in `instruction.md`. Single agent never sees the decomposition, so any solution-relevant content present only there is asymmetric advantage.

   **(b) Contradiction direction (new).** A rule appears in BOTH files but with DIFFERENT values. Even when neither file is technically leaking, the contradiction creates: (i) confusion for the agent that has to reconcile two authoritative sources, (ii) ambiguity in what the verifier is grading against, and (iii) a strong signal that the trainer modified one file without re-syncing the other.

   **You must NOT use text found in execution trajectories, `output.json`, agent logs, or any other file as evidence for this check.** Text produced by agents in trajectories or output files is agent-produced content — it is never evidence that a phrase was injected into `decomposition.yaml`. The two sources of truth are `instruction.md` and `decomposition.yaml` only.

   **Procedure-driven.** Eyeballing the two files for "vibe consistency" is not enough; you must mechanically enumerate and cross-reference.

   STEP A. **Enumerate every concrete rule in `instruction.md`.** Concrete rules are statements with a definite value that a verifier could check against: output field/key names, output counts ("produce N items", "exactly K rows"), rounding/precision ("round to 4 decimals"), sort orders ("sort by X descending, then Y, then Z"), file paths to read or write, named constraints ("must include all 4 source families"), prohibitions ("do not modify file X"), value ranges or formats, deliverable lists.

   STEP B. **Enumerate every concrete rule in `decomposition.yaml`.** Read every `description:`, `goal:`, `acceptance_criteria:`, and other free-text field. Extract the same kinds of concrete rules — output keys, counts, rounding, sort orders, paths, constraints, prohibitions.

   STEP C. **Cross-reference.** For each rule extracted:
   - **Same rule in both files, identical value** → fine.
   - **Same rule in both files, DIFFERENT value** (e.g., instruction says "round to 4 decimals", decomposition says "round to 6 decimals"; instruction says "produce 5 chains", decomposition says "produce 10 chains"; instruction says output key `confidence`, decomposition says output key `score`) → CONTRADICTION → FAIL.
   - **Rule only in decomposition, solution-relevant** → LEAK → FAIL. Carve-out: output schema keys / file paths are allowed in decomposition if also in instruction (this matches QD-04 check 2's schema carve-out).
   - **Rule only in instruction** → fine (single agent has full instruction).

   STEP D. **Verdict.** FAIL on any contradiction (sub-check b) or any leak (sub-check a). Your `reason` must quote (i) the exact line in `instruction.md` (with line number), (ii) the exact line in `decomposition.yaml` (with line number), (iii) the rule and its conflicting values verbatim, (iv) which sub-check fired (a/leak or b/contradiction). PASS only after documenting that you enumerated rules from both files and cross-referenced — list the rule pairs you checked. PASS-without-enumeration is not acceptable.
5. **No custom tooling advantage** — Input artifacts are data for the agent to process, not scripts that do the processing. FAIL if executable scripts in input artifacts perform substantive analysis.
6. **Multi-agent trajectory follows coordination pattern** — Review the multi-agent trajectory. The orchestrator must have spawned sub-agents matching the declared `coordination_pattern` — map-reduce should show map+reduce steps, fan-out should show independent parallel agents followed by synthesis. FAIL if orchestrator solved the task monolithically, ignored the decomposition, or used a different pattern than declared.
7. **Partial credit supported** — The verifier must award fractional scores, not binary pass/fail. Check based on `verifier_type` in `task.toml`:
   - **Executable verifier**: Read `tests/test.sh` or its related test files — individual test cases must be scored separately and reward calculated as `passed / total`. FAIL if the script only awards 1 when ALL tests pass and 0 otherwise.
   - **LLM judge verifier**: Read the judge prompt — it must explicitly instruct the judge to award a score between 0.0 and 1.0 based on how many sub-tasks or requirements were met, with each scoreable criterion listed. FAIL if the judge prompt asks only for a binary verdict or contains no instruction about partial scoring.
8. **Meaningful performance gap — absolute, not waived by timeout.** Read the execution logs for both single-agent and multi-agent configurations. **The multi-agent reward must be at least 20% higher than the single-agent reward. This requirement is ABSOLUTE — it applies whether or not the single agent timed out.** A timeout is not proof of difficulty if the single agent already produced a high-reward output before the timer expired (Issue 3.14: *"single agent timed out but received reward 1.0"* is logically incoherent — single solved the task; the timeout is irrelevant). The combination of `AgentTimeoutError` and `reward >= 0.9` on the single-agent side means the task is NOT multi-agent-requiring; single just happened to finish the work before the timer fired. FAIL if `multi.mean_reward - single.mean_reward < 0.20`, regardless of single's exception status.

   You MUST quote the actual reward values from the execution logs in your reason — both `single.mean_reward` and `multi.mean_reward` verbatim, plus the computed gap. If a timeout was present on the single agent, also quote the recorded reward — that combination needs to be visible in your reasoning, not hidden behind the timeout. Also verify the timeout values from check 2 are identical between single and multi — a gap produced by giving multi-agent a longer timeout is forgery and fails this check. If you cannot find execution log evidence at all, this check PASSES — do not infer or estimate.
9. **Verifier type matches implementation** — Read `verifier_type` from `/task/task.toml`. Then read every file in `/task/tests/` to determine what scoring mechanism is actually implemented. Apply the following rules:

   **If `verifier_type = "llm-judge"`:**
   - The scoring decision for the agent's output must be made by an LLM. Look for evidence of an LLM API call in any test file — for example, a model completion call, an LLM client being instantiated, or an API key being read from the environment and passed to a model call.
   - FAIL if the actual scoring logic is fully deterministic — i.e., if correctness is determined purely by JSON field comparison, regex matching, numeric tolerance checks, or string normalization with no LLM involved. Such a verifier cannot handle the full space of valid agent responses and will silently penalize correct answers that differ in phrasing, format, or structure from the oracle.
   - FAIL if an LLM is invoked only for formatting or post-processing (e.g., parsing the agent's output into JSON) while the correctness decision itself is still made deterministically. The LLM must be the judge of correctness, not a preprocessor.

   **If `verifier_type = "executable"`:**
   - The scoring logic must be fully deterministic — no LLM API calls, no model client instantiation, no API keys. FAIL if any test file makes a model call to determine correctness.

   **Additionally — output type vs verifier type alignment:**
   - If the task's expected outputs are open-ended, interpretive, or admit multiple valid forms (e.g., analytical reports, natural-language explanations, ranked lists with justifications, structured summaries where content matters more than exact values), the verifier MUST be `llm-judge`. FAIL if `verifier_type = "executable"` for such a task — deterministic code and regex matching cannot cover the full range of correct responses and will produce invalid scores.
   - If the task's expected outputs are fully deterministic (e.g., exact numeric values, fixed-schema JSON, specific file modifications, pass/fail unit tests), `executable` is the correct type and an LLM judge introduces unnecessary variance. This is not a FAIL condition but note it in your reason if the declared type is `llm-judge` for a fully deterministic task.

   You MUST quote the `verifier_type` value from `task.toml` and cite the specific file(s) in `tests/` — or their absence — that support your verdict.

## Output Format
Return ONLY valid JSON:
```json
{
  "dimension": "QD-10",
  "result": "PASS" or "FAIL",
  "checks": [
    {"id": 1, "name": "same_role_neutral_instruction", "result": "...", "reason": "..."},
    {"id": 2, "name": "same_timeout", "result": "...", "reason": "..."},
    {"id": 3, "name": "coordination_driven_gap", "result": "...", "reason": "..."},
    {"id": 4, "name": "decomposition_is_guidance", "result": "...", "reason": "..."},
    {"id": 5, "name": "no_custom_tooling", "result": "...", "reason": "..."},
    {"id": 6, "name": "trajectory_follows_pattern", "result": "...", "reason": "..."},
    {"id": 7, "name": "partial_credit_supported", "result": "...", "reason": "..."},
    {"id": 8, "name": "meaningful_performance_gap", "result": "...", "reason": "..."},
    {"id": 9, "name": "verifier_type_matches_implementation", "result": "...", "reason": "..."}
  ],
  "justification": "Overall assessment in 2-3 sentences."
}
```
Result is FAIL if ANY check fails.
