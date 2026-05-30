# QD-14: Gap Legitimacy

## Your Role

You are a red-team reviewer auditing whether the multi-vs-single reward gap is genuine or engineered. SwarmBench accepts tasks only when the gap clears E-01's threshold, and trainers are paid per accepted task — they have direct incentive to construct fake gaps that pass each individual QD in isolation. Your job is to look across the whole task package adversarially and find evidence of construction.

**Mindset:** assume the trainer engineered the gap. Investigate hard. The checks below enumerate the most common attack vectors, but trainers are creative — when you finish those, keep digging. If the listed signals do not trigger but something else feels off (unusual file in `environment/`, a strange branch in `tests/`, an instruction sentence that reads like a wink to multi-agent), **flag it**. Defaulting to PASS without serious investigation is the failure mode of this dimension.

**Scope:** applies to both `verifier_type = "executable"` and `verifier_type = "llm-judge"`. The attack surface differs by type but the principle is the same — multi must outperform single because of coordination capability, not because the verifier was rigged, fewer checks ran for one mode, or information was hidden from single-agent.

## Harbor Constraints (Background — Apply as Ground Truth)

Harbor's mode-specific layer is bounded:

- **Verifier is invoked identically** for single and multi runs — same command, same volume mounts, same env from `task.toml.verifier.env`. No `HARBOR_MODE` or equivalent env var.
- **Test files run unchanged across modes.** `tests/test.sh`, `tests/judge.py`, `tests/verify.py`, helper modules — identical context.
- **The only legitimate trainer-controllable asymmetric channel is `decomposition.yaml`.** Harbor injects it into the multi orchestrator's prompt as `## Gold Decomposition Guide`. Single agents never see it.
- **Multi gets coordination guidance.** It must not get task-detail content, hidden-file pointers, stricter/looser test selection, or solution hints.

Any other asymmetric channel is gap-faking.

## Explore First

This QD is investigative. Trainer artifacts vary in name, structure, and location. **Do not assume specific log file names exist** — `judge_justification.txt`, `test-output.log`, `test-stdout.txt` are trainer conventions, not Harbor contracts; some are absent on perfectly valid tasks. Run `Glob /task/**` for the full tree, then debug the logs yourself to locate the evidence. Use Read, Grep, Bash freely. Treat candidate filenames as hints, not requirements.

## Files to Read (Starting Points — Investigate Beyond These)

- `/task/task.toml` (read `verifier_type` and `metadata.coordination_pattern`)
- `/task/instruction.md`
- `/task/decomposition.yaml`
- `/task/tests/*` — every file (test.sh, judge.py, verify.py, oracle.json, helpers — the verifier's code is the primary attack surface)
- `/task/environment/` — every non-data file (helpers, hints, schemas, README-style notes)
- `/task/environment/input_artifacts/` — file names at minimum, content if a file looks like a hint document
- `/task/execution_logs/single-kimi-agent/*/verifier/` and the multi-agent equivalent — **open every file**. Per-check / per-field evidence may live in `test-output.log`, `test-stdout.txt`, `pytest_report.txt`, `judge_justification.txt`, or any other trainer-named file. Identify which carries the per-check PASS/FAIL list. If none does, note it.
- `/task/execution_logs/single-kimi-agent/*/agent/` and multi-agent equivalent — `kimi-cli.txt`, `trajectory.json` may also carry useful evidence

## Grounding Rule

**Before any FAIL verdict, copy the exact verbatim text from the file that triggered the violation into the `reason` field.** Name the file by path. If you cannot produce an exact quote, the check PASSES — but only after you have actually searched. PASS-by-not-looking is not acceptable; document the files you searched.

## Checks

### Check 1 — Verifier Symmetry (blocking)

Harbor exposes no mode env var and invokes the verifier identically. Therefore *any* code path inside `tests/` that branches on mode-correlated signals is engineered discrimination. This includes test selection ("few tests for multi, many tests for single"), assertion strictness ("multi passes at score ≥ 0.3, single must hit ≥ 0.7"), denominator manipulation ("total depends on agent output shape, not oracle shape"), and skip decorators conditioned on mode-correlated state.

Mandatory procedure:

STEP A. Read every file in `/task/tests/` end-to-end, including helper modules they import.

STEP B. Search for mode-discrimination patterns. Any match is a candidate FAIL:

- **String literals indicating mode:** `single-kimi-agent`, `multi-kimi-agent`, `single-kimi`, `multi-kimi`, `swarm-kimi-single`, `swarm-kimi-multi`
- **Path / cwd introspection:** `os.getcwd`, `Path.cwd()`, `Path(__file__).parts`, `sys.argv[0]`, `pwd` in shell, `basename`, `dirname` — any code that extracts substrings from a runtime path
- **Trajectory-log reads from inside the verifier:** opens of `/logs/agent/kimi-cli.txt`, `/logs/agent/trajectory.json`, `/logs/agent/output.json` — these files differ structurally between modes; reading them from inside the verifier is a mode-fingerprint
- **Undeclared environment vars:** `os.environ.get(...)`, `$ENV_VAR` in shell, for any name not in `task.toml.verifier.env`
- **Output-file-count discrimination:** counts of files in `agent/`, `glob` patterns over the agent output dir — multi typically produces more outputs than single
- **Conditional test skipping or assertion strictness (executable):** `pytest.skip` / `unittest.skip` / shell `continue` conditioned on any of the above signals; branches that gate the *effective number of tests* run for each mode — if the count differs, that is gap-faking
- **Denominator games (llm-judge):** the reward float written to `reward.json` is sourced directly from an LLM response with no deterministic anchor to the oracle's structure (no `len(oracle[...])`, no `for ... in oracle[...]`). The agent can shrink the denominator by truncating output.
- **Output-key-shape branching:** `if "shard_summaries" in agent_output: <branch A> else: <branch B>` where branch A scores more leniently and the keyed structure is one the decomposition pushes multi to produce
- **Process-conformance reward adjustments keyed on mode-correlated signals:** ANY reward adjustment — multiplicative cap, multiplicative penalty, additive bonus, additive penalty, or any other arithmetic — that is keyed on a feature of the agent's *process* rather than the quality of its *output*. The shape doesn't matter; the motive does. All of the following are the same anti-pattern:
   - `final_reward = min(quality_score, process_cap)` (multiplicative cap)
   - `reward = max(0, min(quality, cap))` (clamp-and-cap)
   - `if n_subagents < N: reward *= penalty` (multiplicative penalty)
   - `cap = PROCESS_FAIL_CAP if not delegated else 1.0` (conditional cap)
   - **`final_score = quality_score + COORDINATION_BONUS if multi_evidence else quality_score`** (additive bonus)
   - **`final_score = quality_score - NO_TRAJECTORY_PENALTY if no_markers else quality_score`** (additive penalty)
   - `score += 40 if "SubagentEvent" in trajectory else -45` (the Issue 3.12 shape — points awarded/deducted for trajectory marker presence)
   - Any other expression that adds or subtracts from the output-quality score based on a process signal.

   Concrete fingerprints: constants named `PROCESS_FAIL_CAP`, `PROCESS_PARTIAL_CAP`, `DELEGATION_CAP`, `COORDINATION_BONUS`, `MULTI_AGENT_BONUS`, `NO_TRAJECTORY_PENALTY`, any `*_CAP` / `*_LIMIT` / `*_PENALTY` / `*_BONUS` keyed on `n_subagents`, sub-agent call count, presence/absence of `agent/trajectory.json`, presence of orchestrator-only tool calls (`Task`, `CreateSubagent`, `Agent`), presence of specific event types in the trajectory (`SubagentEvent`, `Map`, `Reduce`), or any other trajectory-derived signal. Single-agent runs naturally cannot delegate to sub-agents and naturally cannot produce a multi-agent-shaped trajectory — adjusting their reward on these signals manufactures the gap rather than measuring it. **The adjustment IS the gap.** Reward must derive from output quality against the oracle, never from how the agent organized its work. This is a FAIL even when the adjustment is dressed up as "coordination contract enforcement", "process compliance", or "rewarding good orchestration" — a single agent has no contract to violate, and a multi-agent that happens to produce the same quality output via a different process is still entitled to the same reward. (Structurally identical `min(score, cap)` / `score ± delta` shape to QD-09 check 5(d), which catches the *fail-open* motive; here the motive is *gap-faking*.)

STEP C. Verdict.
- FAIL if any STEP B match exists AND the branch it enables changes the reward, the set of tests/fields scored, or the assertion threshold.
- PASS if all matches are cosmetic (log-line labels that don't gate scoring).

STEP D. Grounding: quote the matching line(s) verbatim, name the file, write one sentence stating how the branch advantages multi or disadvantages single.

### Check 2 — Specification & Hint Symmetry (blocking)

The single agent has only `instruction.md`. The multi agent has `instruction.md` + `decomposition.yaml` + any files those documents point at. Two asymmetric leak patterns must not exist:

(a) **Spec leak** — a deliverable's specification (file path to create, function/symbol to define, behavioral contract, oracle field schema/format/sort-order/units) lives only in `decomposition.yaml`. Single agent is structurally unable to produce it.

(b) **Hint-file leak** — a file inside `/task/environment/` (helper, hint, schema, README) is named or pointed at in `decomposition.yaml` but not in `instruction.md`. Multi learns the file exists via the orchestrator's prompt; single never sees the reference. The file is mounted symmetrically by Harbor, but the *knowledge that it exists* is asymmetric.`decomposition.yaml` will have direction to solve the problem but not the hint which is acceptable.

Mandatory procedure:

STEP A. Enumerate the deliverable set:
- **executable**: parse `tests/test.sh` / `tests/verify.py`. For each distinct assertion, identify what the agent must produce — file paths created, functions defined, behaviors implemented. Quote the assertion line.
- **llm-judge**: read `tests/oracle.json` and enumerate every top-level and one-level-nested output field.

STEP B. For each deliverable in STEP A, search `instruction.md` for its specification (verbatim or paraphrased name + format + constraints). Note "found in instruction" or "not found."

STEP C. For each "not found" item, search `decomposition.yaml`. If the spec is there, this is a **spec leak** (sub-check 2a) — record it.

STEP D. Enumerate files in `/task/environment/` excluding `Dockerfile` and `input_artifacts/`. For each, grep `instruction.md` and `decomposition.yaml` for its name or path. A file referenced *only* in decomposition.yaml that contains task-relevant content (hint text, helper used by scoring, schema the agent must follow, README-style guidance) is a **hint-file leak** (sub-check 2b) — record it.

STEP E. Verdict.
- FAIL if any spec-leak from STEP C OR any hint-file-leak from STEP D exists. Coordination guidance is the legitimate channel; deliverable specs and file pointers are not.
- PASS otherwise.

STEP F. Grounding: list each leak by name, quote the decomposition.yaml passage, confirm absence in instruction.md.

### Check 3 — Asymmetric-Failure Set is Capability-Limited, Not Spec-Limited (blocking)

For every check/field where the single agent failed AND the multi agent succeeded, the failure must trace to a *capability* limit (context exhaustion, attention degradation, timeout, cross-file coordination demand) — not to a *spec* limit (instruction.md never told single agent what to produce).

Mandatory procedure:

STEP A. **Investigate the verifier and agent logs.** Open every file under `execution_logs/single-kimi-agent/*/verifier/`, `execution_logs/single-kimi-agent/*/agent/`, and the multi-agent equivalents. The trainer's verifier writes per-check / per-field PASS/FAIL evidence *somewhere* — find where. Common candidates include `test-output.log`, `test-stdout.txt`, `pytest_report.txt`, `judge_justification.txt`, but any name is possible. Document which file(s) you used.

If no file in the logs exposes a per-check enumeration (only an opaque `reward.json`), this check returns `result: "N/A"` — but you must document every file you opened to justify the N/A.

STEP B. Extract `single_failed = { items that FAIL across single-agent trials }` and `multi_passed = { items that PASS in the best multi-agent trial }`. Compute `asymmetric_failures = single_failed ∩ multi_passed`.

STEP C. For each item in `asymmetric_failures`, search `instruction.md` for its specification — by check/field name, by the deliverable it asserts, or paraphrased equivalent. Cross-reference Check 2's findings.

STEP D. Verdict.
- FAIL if any item in `asymmetric_failures` lacks a spec in `instruction.md`. The gap on this item was created by under-specifying the shared brief.
- PASS if every item has a clear spec in `instruction.md`. The gap is a genuine capability difference.
- N/A only if logs do not expose per-check enumeration (and you have documented the files you searched).

STEP E. Grounding: list each item, name the log file you extracted it from, quote the failure line, quote the spec absence in instruction.md, cross-reference Check 2 where it overlaps.

### Check 4 — Open-Ended Adversarial Pass (blocking)

Checks 1–3 enumerate the known attack vectors. Trainers are creative; new manipulations appear that we have not pre-listed. This check is the catch-all: **after completing Checks 1–3, do one more pass across the entire task package looking for anything else suspicious** and flag it. Investigate hard. Defaulting to PASS without serious investigation is not acceptable.

Things to look at that earlier checks may not catch:

- **Phrasing tells in instruction.md** that appear neutral but become a wink when read with knowledge of decomposition.yaml (e.g., instruction says "consider grouping the data" — single ignores it as advice, multi reads it as confirmation of the decomposition strategy)
- **Unusual structure in `environment/input_artifacts/`** that encodes hints (file *names* matching expected output keys, README inside a data dir, comments inside JSONL records that single wouldn't think to read)
- **Decomposition that perfectly mirrors the oracle's key structure**, suggesting the oracle was reverse-engineered from the decomposition rather than from the underlying task
- **Trajectory anomalies** — multi's sub-agents producing answers far too quickly or with too little tool use, suggesting hints flowed in via the orchestrator prompt
- **Verifier code complexity that does not appear necessary** for the stated rubric — extra branches, unused conditions, dead code that might have been left in from an earlier asymmetric version
- **`why_multi_agent` in task.toml** claiming a structural reason that does not match what Checks 1–3 actually observed

Mandatory procedure:

STEP A. Spend at least one full investigative pass with the explicit framing "if I were the trainer, how could I have rigged this?" Read instruction.md, decomposition.yaml, the verifier code, and a sample of the input_artifacts with adversarial intent.

STEP B. Document what you looked at and what you noticed. Even if you find nothing, the `reason` field must list the avenues you investigated — this proves the check was real and not a rubber-stamp.

STEP C. Verdict.
- FAIL if you find any concrete evidence (quotable) of an engineered manipulation not already caught by Checks 1–3.
- PASS only after a documented investigation that found nothing. Your `reason` must state the investigation steps and the negative results.

STEP D. Grounding: any FAIL must include a verbatim quote and one sentence explaining why it advantages multi or disadvantages single.

## Output Format

Return ONLY valid JSON:

```json
{
  "dimension": "QD-14",
  "result": "PASS" or "FAIL",
  "checks": [
    {"id": 1, "name": "verifier_symmetry", "result": "PASS|FAIL", "reason": "..."},
    {"id": 2, "name": "specification_and_hint_symmetry", "result": "PASS|FAIL", "reason": "..."},
    {"id": 3, "name": "asymmetric_failures_capability_limited", "result": "PASS|FAIL|N/A", "reason": "..."},
    {"id": 4, "name": "open_ended_adversarial_pass", "result": "PASS|FAIL", "reason": "investigation steps + findings (or documented null result)"}
  ],
  "justification": "Overall assessment in 2-3 sentences. Note any composition pattern — multiple checks failing on the same engineered manipulation is a strong signal of intentional gap-faking."
}
```

Result is FAIL if ANY check is FAIL. `N/A` does not contribute to FAIL.