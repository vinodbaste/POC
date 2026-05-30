# QD-06: Decomposition Soundness

## Your Role
You are evaluating the decomposition blueprint in `decomposition.yaml`. This is a multi-agent swarm benchmark where the goal is for single-agent runs to fail and multi-agent runs to pass — so sub-task descriptions are deliberately directive and guiding.

**Critical scoping rule:** `instruction.md` is shared with BOTH single-agent and multi-agent runs. Hints, domain context, implementation directions, and ordering notes in `instruction.md` are expected and intentional — do NOT flag anything in `instruction.md` under any check. Read it only to verify that `decomposition.yaml` covers the full scope of the task.

Your job is to evaluate `decomposition.yaml` only. If a description is vague, the sub-agent fails. If descriptions overlap, work is wasted. If dependencies are wrong, synthesis produces garbage.

## Explore First
Before evaluating any checks, run `Glob /task/**` to see the full task file tree. The "Files to Read" section below is a minimum starting point — use Read, Grep, and Bash freely on any file that looks relevant to your checks.

## Files to Read
- `/task/decomposition.yaml` (MUST read fully)
- `/task/instruction.md`
- `/task/task.toml` (read `coordination_pattern`)

## Grounding Rule
**Before issuing any FAIL verdict on any check, you MUST copy the exact verbatim text from `decomposition.yaml` that triggered the violation into your `reason` field.** If you cannot produce an exact quote from `decomposition.yaml` itself, the check PASSES. Do not infer, paraphrase, or reconstruct text — only quote what is literally present.

## Checks
1. **Non-overlapping** — Each sub-agent has exactly one clear responsibility. FAIL if multiple agents assigned to the same data or same analysis.
2. **Self-contained** — Each description includes what files to read, what to produce, and in what format. FAIL ONLY if a description delegates its core specification to another source with no independent scope of its own — e.g., "do whatever sub-task 1 decides" or "implement what the other sub-task specifies" with nothing else. Do NOT fail for: referencing upstream sub-tasks as causal context ("behavior introduced by sub-task 1", "introduced by the other sub-tasks"), cross-references in synthesize-phase sub-tasks that have `depends_on` populated (these are structurally expected to reference upstream work), or pointing to `instruction.md` for background.
3. **Complete coverage** — Every part of the input data is assigned to at least one sub-agent. FAIL if some input segments have no assigned agent.
4. **Dependencies correct** — Downstream sub-tasks depend on all the upstream sub-tasks they need. FAIL if a synthesis step is missing a dependency.
5. **Minimal** — No redundant agents — each one is necessary. FAIL if two agents do the same work or an agent has no meaningful responsibility.
6. **WHAT not HOW** — Descriptions must guide sub-agents toward what to achieve, not walk them through how to implement it. FAIL if a description provides: step-by-step logic or a numbered algorithm walkthrough ("first do X, then do Y, then do Z"), literal code or function-call sequences with arguments (e.g., `PyObject_CallFunctionObjArgs(super_destroy, self, NULL)`), or before/after code strings showing the exact edit to make. **PASS** for everything else, including: a single named mechanism or Python built-in without surrounding logic ("use setattr", "through the C API"), domain hard constraints where only one mechanism physically exists ("must use the C API because super() is unavailable in C code"), behavioral ordering invariants that describe required state sequencing ("after performing its own teardown"), failure-mode hints that say what to preserve without specifying how ("stash references before close if needed"), output schema definitions, declarative output constraints, enumerated output properties, **and coordination-pattern instructions to the orchestrator about delegation/dispatch** (e.g., "dispatch a sub-agent for this task, don't do it yourself", "spawn one sub-agent per shard", "delegate to a specialist sub-agent", "fan out to N parallel sub-agents") — these describe the multi-agent orchestration pattern, not solution methodology, and SwarmBench multi-agent runs require the orchestrator to delegate, so naming the delegation explicitly is legitimate. The test: does the description tell the sub-agent WHAT state or behavior must result, or tell the orchestrator WHO should do the work? PASS. Does it walk the sub-agent through HOW to produce that state step by step? FAIL. If a description bundles legitimate delegation language with HOW content (e.g., "dispatch a sub-agent and have it run regex `X` then sort by Y"), flag only the HOW portion, not the delegation.
7. **Pattern match** — The decomposition structure matches the declared `coordination_pattern`. FAIL if claims map-reduce but has no reduce step, or claims fan-out but sub-tasks are not independent.
8. **Parallel-group consistency** — A sub-task in `parallel_group: X` cannot list any `depends_on` entry that resolves (directly or transitively) to another sub-task that is also in `parallel_group: X`. Tasks in the same parallel group run concurrently by definition, so they cannot have dependency relationships among themselves. Walk every sub-task: collect its `depends_on` list, follow the dependency chain, and FAIL if any node in that chain shares its `parallel_group`. The contradiction is logical, not stylistic — `depends_on` says "I wait for these to finish" while same-group `parallel_group` says "I run alongside these". Both cannot be true.

   Example violation to recognize:
   ```yaml
   - id: documentation
     depends_on:
       - lookups-and-key-transforms       # also parallel_group: fan-out
       - backend-features-and-sqlite      # also parallel_group: fan-out
     parallel_group: fan-out
   ```
   `documentation` cannot belong to `parallel_group: fan-out` while waiting on other `fan-out` tasks to finish. Either move `documentation` to a later group (e.g. `synthesize`) or remove the same-group dependencies.

## Output Format
Return ONLY valid JSON:
```json
{
  "dimension": "QD-06",
  "result": "PASS" or "FAIL",
  "checks": [
    {"id": 1, "name": "non_overlapping", "result": "...", "reason": "..."},
    {"id": 2, "name": "self_contained", "result": "...", "reason": "..."},
    {"id": 3, "name": "complete_coverage", "result": "...", "reason": "..."},
    {"id": 4, "name": "dependencies_correct", "result": "...", "reason": "..."},
    {"id": 5, "name": "minimal", "result": "...", "reason": "..."},
    {"id": 6, "name": "what_not_how", "result": "...", "reason": "..."},
    {"id": 7, "name": "pattern_match", "result": "...", "reason": "..."},
    {"id": 8, "name": "parallel_group_consistency", "result": "...", "reason": "..."}
  ],
  "justification": "Overall assessment in 2-3 sentences."
}
```
Result is FAIL if ANY check fails.