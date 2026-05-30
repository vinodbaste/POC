# QD-13: Harbor Format Compliance

## Your Role
You are checking whether this task respects the Harbor execution contract. Every directory in a Harbor task has a strict purpose — breaking that contract corrupts the benchmark silently: the agent sees answers it shouldn't, self-scoring produces wrong oracle values, execution logs are fabricated, or a fake gap is manufactured between single and multi-agent.

## Harbor Directory Contract (read this before evaluating)

Each directory has one job:

| Directory | Purpose | Must NOT contain |
|-----------|---------|-----------------|
| `environment/` | Docker build context — everything here is visible to the agent at runtime | Verifier scripts, test scripts, scoring logic, solution patches, oracle data, pre-written output files |
| `solution/` | Oracle agent's reference fix — apply the correct answer only | Calls to the verifier, writes to `reward.txt`, installation of test-only packages |
| `tests/` | Grading machinery — Harbor mounts this AFTER the agent finishes | Anything baked into the Docker image |
| `execution_logs/` | Harbor run outputs — must reflect what actually happened | Pre-fabricated reward files, rewards contradicting the visible test output |

## Explore First
Before evaluating any checks, run `Glob /task/**` to see the full task file tree, then `Glob /task/environment/**` to list every file in the environment directory. Read every file you find — do not stop at the Dockerfile. The "Files to Read" section below is a minimum — use Read, Grep, and Bash freely on any file that looks relevant.

## Files to Read
- `/task/environment/` (ALL files — Dockerfile and everything inside)
- `/task/solution/solve.sh`
- `/task/tests/test.sh` and any verifier scripts in `tests/`
- `/task/execution_logs/oracle/*/verifier/reward.txt` and `*/agent/oracle.txt`
- `/task/execution_logs/oracle/*/verifier/test-stdout.txt` or `test-output.log`
- `/task/execution_logs/single-kimi-agent/*/verifier/reward.txt`
- `/task/execution_logs/multi-kimi-agent/*/verifier/reward.txt`
- `/task/execution_logs/*/verifier/test-stdout.txt` or `test-output.log` for oracle, single-agent, and multi-agent runs
- For Check 16 (current-state vs. recorded logs): also read `/task/instruction.md`, `/task/tests/oracle.json` (llm-judge), `/task/decomposition.yaml`, every file under `/task/solution/`, and the per-trial `agent/output.json` under `execution_logs/oracle/`, `execution_logs/single-kimi-agent/`, and `execution_logs/multi-kimi-agent/`

## Grounding Rule
**Before issuing any FAIL verdict, you MUST copy the exact verbatim text from the specific file that triggered the violation into your `reason` field.** If you cannot produce an exact quote from that file, the check PASSES. Do not infer, paraphrase, or reconstruct — only quote what is literally present.

## Checks

1. **environment/ contains only Dockerfile and input files, AND the Dockerfile delivers the UNSOLVED state.** The environment directory is the Docker build context — every file AND every line of the Dockerfile produces state that is visible to the agent at runtime. The image at agent start time MUST contain the codebase / inputs in their UNSOLVED state — the state the agent is supposed to fix, patch, or compute. Two failure modes to check:

   **(a) Solution content OR Harbor-managed task files as physical files in environment/.** Run `Glob /task/environment/**` and read every file found. FAIL if any file in `environment/` (at any depth, regardless of name) is:
   - a verifier or test script, a scoring function, oracle answer data, a solution patch (`.diff`, `.patch`, or any file whose body contains unified-diff content), or a pre-written agent output file; OR
   - **a copy of a Harbor-managed task file**: `instruction.md`, `task.toml`, `decomposition.yaml`, `solve.sh`, or any other file from the task root. Harbor mounts these at the appropriate stage — `instruction.md` at the agent's workspace, `decomposition.yaml` ONLY into the orchestrator's prompt for multi-agent runs, `solve.sh` ONLY for the oracle agent, `task.toml` never to the agent. Duplicating any of them in `environment/` causes either asymmetric leakage (single agent reads `decomposition.yaml` → fake gap; single OR multi agent reads `solve.sh` → benchmark broken; agent reads `task.toml` → sees `verifier_type`, judge prompts, and `[verifier.env]` keys it shouldn't) OR silent version drift (the image's frozen copy diverges from the task root's edited copy, and the agent sees whichever wins the path race).

   **SHA-256 every `environment/` file against every `solution/` file AND against `instruction.md` / `task.toml` / `decomposition.yaml` at the task root — any byte-identical pair is confirmed leakage and is an automatic FAIL** (e.g. `environment/diffs/<name>.diff` byte-identical to `solution/diffs/<name>.diff`; `environment/instruction.md` byte-identical to `/task/instruction.md`).

   Acceptable files: `Dockerfile`, raw input data (CSVs, JSONs, configs that are NOT `task.toml`), and source code the agent is meant to modify (cloned repos, project files). A file is a grading/verifier file if it writes `reward.txt`, computes pass/fail scores, counts test outcomes, or imports pytest/unittest for assertion purposes.

   **(b) Solution applied inline in the Dockerfile.** Read `environment/Dockerfile` end-to-end, including the body of every `<<EOF` heredoc. FAIL if any RUN / COPY / ADD instruction applies, embeds, or otherwise delivers any subset of the solution into the image at build time — so the image at agent start time is in the SOLVED state. Concrete fingerprints to grep for:
   - `RUN patch -p1 < <diff>` / `RUN git apply <diff>` (any `patch -pN`, `git apply`, `quilt push`, or equivalent patch-application invocation)
   - Heredoc embedding diff content followed by an apply step: `RUN cat > /tmp/<name>.diff <<'EOF' ... EOF && patch -p1 < /tmp/<name>.diff`. The heredoc body itself is solution content — read it line-by-line and grep for distinctive lines from `solution/` (function names, import statements, unified-diff headers like `@@ -X,Y +X,Y @@`, `--- a/...`, `+++ b/...`).
   - `COPY` from any path holding patch / fix content (`diffs/`, `patches/`, `fixes/`, or any other directory whose files contain diff bodies) followed by an apply step.
   - `RUN git checkout <ref>` / `RUN git reset --hard <ref>` where `<ref>` is a commit, tag, or branch that already includes the fix (cross-check against `solution/`).
   - `RUN sed -i 's/<broken>/<fixed>/g' <source>` (or `awk`, inline `python -c`, etc.) where the substitution corresponds to changes in `solution/fix.diff` — inline source rewriting that pre-applies the fix.
   - `COPY environment/<fixed-source-file> /<broken-path>/` — overlaying a fixed source file on top of the broken one.
   - `RUN pip install <pkg>==<fixed-version>` / `RUN npm install <pkg>@<fixed-version>` / equivalent — installing a version of a dependency that already contains the bug the agent was supposed to fix.
   - **`COPY` of any Harbor-managed task file into the image**: `COPY instruction.md`, `COPY task.toml`, `COPY decomposition.yaml`, `COPY solve.sh`, or any `COPY ../<file>` / `COPY ../../<file>` pattern reaching outside `environment/` to pull in task-root files. Harbor handles delivery of these files; baking them into the image always causes leakage (decomposition / solve.sh visible to agents that shouldn't see them) or drift (frozen image-copy diverges from edited task-root copy).

   **Mandatory procedure for (b):**

   STEP A. Read `solution/` to identify the unsolved state. For SWE tasks `solution/fix.diff` or `solution/diffs/*.diff` shows the canonical fix; the unsolved state is the codebase BEFORE that diff is applied.

   STEP B. Read every RUN / COPY / ADD instruction in `environment/Dockerfile`, including the body of every `<<EOF` heredoc. For each, ask: does this instruction apply, embed, or otherwise deliver any subset of the solution into the image?

   STEP C. Cross-reference: (i) SHA-256 every file in `environment/` against every file in `solution/`; (ii) grep every Dockerfile heredoc body and every file COPYed in for distinctive lines from `solution/` (function names introduced by the fix, import statements added, file paths created, unified-diff header lines).

   STEP D. FAIL on any non-empty match. Quote (i) the offending Dockerfile line with line number, (ii) the matching `solution/` artifact path and the overlapping content or SHA-256, (iii) one sentence stating why the image at agent start time is in the SOLVED rather than UNSOLVED state. The fix is always the same: ALL solution-applying logic moves to `solution/solve.sh`; the Dockerfile delivers the unsolved state only.

2. **solve.sh applies the fix only — no self-grading** — Read `/task/solution/solve.sh`. FAIL if solve.sh: (a) calls the verifier directly (`python3 /tests/verify.py`, `pytest`, or any equivalent command), (b) writes to `reward.txt` or reads it to self-score, or (c) installs test-only packages (`pytest`, `itsdangerous`, judge LLM clients, etc.) that are only needed for grading and not for running the patched application. The oracle's score must come from Harbor running `tests/test.sh`, not from solve.sh's own self-assessment.

3. **oracle.txt is not contradicted by reward.txt** — Read `agent/oracle.txt` and `verifier/reward.txt` from the oracle execution log. FAIL if oracle.txt shows a failure (`reward = 0.0`, `FATAL`, `ModuleNotFoundError`, `ImportError`, any crash traceback) while the same trial's `reward.txt` shows a passing score (≥ 0.5). A contradiction means either solve.sh's self-check is broken (it calls the verifier before its dependencies are installed) or reward.txt was fabricated independently of the actual run. Either way the oracle measurement is untrustworthy.

4. **test.sh installs its own dependencies before running the verifier** — Read `/task/tests/test.sh`. FAIL if test.sh calls a verifier script or runs pytest without first installing all packages that script needs. The canonical correct pattern is: `pip install <test-only-deps>` → run verifier → handle reward.txt fallback. FAIL if the verifier is called before any dependency installation, making grading depend on packages that happen to be (or not be) in the Docker image.

5. **test.sh does not unconditionally write a passing reward** — Read `/task/tests/test.sh`. FAIL if test.sh writes a hardcoded passing value to `reward.txt` unconditionally — e.g., `echo 1 > /logs/verifier/reward.txt` at the top of the script with no conditional logic, or `echo 1 > reward.txt` as the only reward-writing statement. The reward must be derived from actually running the verifier against the agent's output. A fallback `echo 0` on verifier crash is acceptable; an unconditional `echo 1` is fabrication.

6. **tests/ files are not baked into the Docker image** — Read the Dockerfile. FAIL if it contains any instruction that copies verifier scripts, test files, or judge prompts into the image (e.g., `COPY tests/`, `COPY tests/verify.py`, `ADD tests/`). Harbor mounts `tests/` at grading time — baking it in means the agent can read the full scoring logic during its run.

7. **execution_logs oracle reward is consistent with test output** — Read `execution_logs/oracle/*/verifier/reward.txt` and the corresponding `test-stdout.txt` or `test-output.log`. FAIL if the numeric reward is inconsistent with the pass counts visible in the log — for example, if the log shows 17 of 35 tests passed but reward.txt contains `1.0`, or if the log shows all tests passed but reward.txt contains `0.0`. A mismatch means reward.txt was written independently of the actual test run.

8. **Same verifier test set across oracle/single/multi logs** — Read the verifier output logs for oracle, single-agent, and multi-agent runs (`test-output.log`, `test-stdout.txt`, `reward.txt`, `reward.json`, judge output, or equivalent artifacts). FAIL if the runs were scored on different verifier test sets, different total test counts, different named test cases, different scoreable criteria, or different verifier modes. For executable verifiers, compare visible totals and named checks where available (e.g. `41/41`, per-file pytest lists, per-bug counts, Minitest file lists). For LLM-judge verifiers, compare the judge rubric/criteria count and output fields. Do not fail merely because pass/fail outcomes differ — fail only when the set of things being scored differs. Quote the exact totals, criteria, or test names showing the mismatch.

   **Legitimate-failure exception:** If a run failed to produce the agent's required output file (e.g. `instruction.md` requires `output.json` but the agent timed out, crashed, or its trajectory shows it never wrote the file), that is a *valid agent failure* — not evidence of a different test set. The verifier still ran the same checks; the agent just had nothing to score. In that case, PASS this check based on the runs that *did* produce output. The single-agent gap (failure vs. multi-agent success) is the intended signal and is covered by other dimensions (QD-05, QD-14), not here. Only FAIL QD-13.8 when two or more runs *both* produced verifier output and the test set / criteria / totals between them differ.

9. **Single-agent reward is not manually deflated** — Read `execution_logs/single-kimi-agent/*/verifier/reward.txt` and the corresponding `test-stdout.txt`. FAIL if reward.txt shows a very low score (≤ 0.1) but the test output log shows no test failures or shows the agent produced correct output. A fabricated low single-agent reward creates a fake benchmark gap that does not reflect genuine difficulty.

10. **Multi-agent trajectory is not a copy of the oracle run** — Read `execution_logs/multi-kimi-agent/*/agent/trajectory.json` and `execution_logs/oracle/*/agent/trajectory.json` (or `oracle.txt`). FAIL if the multi-agent trajectory is identical or near-identical to the oracle run output — same patches applied in the same order, same tool call sequences — indicating the multi-agent trial was not a genuine independent run but a copy of the oracle solution pasted in.

11. **No pre-written agent output file in environment/** — Check whether the expected output file (e.g., `output.json`, `answer.txt`, or whatever the task expects) already exists inside `environment/` or would be present in the Docker image at agent start time. FAIL if the agent's required output file is pre-populated with a correct or near-correct answer in the environment, meaning the agent only needs to copy or leave it in place to score perfectly.

12. **solve.sh and test.sh reference only files that actually exist** — A broken file reference silently corrupts the benchmark. If test.sh calls `python3 /tests/judge.py` but `judge.py` is absent from `tests/`, the verifier crashes and reward.txt may fall back to 0 (or not be written at all), making every trial score meaningless regardless of what the agent produced. The same applies to solve.sh referencing a diff file or patch that was never committed to `solution/`.

   Run `find /task/tests -type f` and `find /task/solution -type f` to enumerate what actually exists.

   (a) Read `tests/test.sh`. Extract every task-specific file it invokes or imports — python scripts, shell scripts, patch files, JSON oracle files, judge prompts. FAIL if any of these is absent from the `find /task/tests` output. Quote both the reference in test.sh and the absence in the find output.

   (b) Read `solution/solve.sh`. Extract every patch, diff, or script file it applies or sources. FAIL if any is absent from the `find /task/solution` output.

   Do NOT fail for standard system binaries and packages (python3, pip, bash, git, grep, awk, etc.) — only flag task-specific named files.

13. **decomposition.yaml does not reference Harbor-restricted paths** — `tests/` is Harbor's grading directory — it is mounted by Harbor after the agent finishes and is never accessible to the agent at runtime. If any sub-task description in `decomposition.yaml` instructs an agent to execute, read, or run a file under `/tests/` (e.g. `python3 /tests/verify.py`, `bash /tests/test.sh`), the agent will get a file-not-found error and the sub-task description is misleading.

   Read `/task/decomposition.yaml`. Scan every `description` field for references to paths beginning with `/tests/`. FAIL if any such reference is found. Quote the exact line from the description that contains the `/tests/` path.

14. **Input data files live under `environment/input_artifacts/`** — Task convention: every data file the agent reads at runtime (papers, datasets, documents, recordings, etc.) must sit under `environment/input_artifacts/` — not directly at `environment/` top level, and not in some other ad-hoc subdirectory like `environment/papers/` or `environment/data/`. The Dockerfile is then expected to `COPY input_artifacts /input_artifacts` so the agent finds the data at a stable, predictable path. This keeps every task structurally identical and makes review tractable.

    Run `find /task/environment -type f -maxdepth 3` to enumerate the layout. **FAIL** if any data file sits outside `environment/input_artifacts/`. Data-file extensions to flag: `.csv`, `.tsv`, `.parquet`, `.feather`, `.jsonl`, `.ndjson`, `.json` (when it is data, not a build manifest), `.yaml`/`.yml` (when it is data, not a build manifest), `.txt`, `.md`, `.pdf`, `.docx`, `.xlsx`, `.xml`, `.html`/`.htm`, `.sqlite`/`.db`, `.png`/`.jpg`/`.jpeg`/`.gif`, `.wav`/`.mp3`/`.mp4`, `.npy`/`.npz`. Quote the exact offending file paths.

    Allowed at the `environment/` top level (these are NOT input data):
    - `Dockerfile`, `.dockerignore`
    - Build/install manifests consumed by `pip`/`apt`/`npm` during image build, not by the agent: `requirements.txt`, `constraints.txt`, `pyproject.toml`, `package.json`, `package-lock.json`, `yarn.lock`, `Pipfile`, `Pipfile.lock`, `environment.yml`, `conda.yml`, `apt-packages.txt`, `Makefile`
    - **Source code the agent is meant to modify, however it is delivered.** Two equally valid patterns for code-SWE tasks (bug-fix, refactor, migration, security-patch, etc.):
      - A physical source-code project subdirectory committed in the task package — a tree dominated by `.py`/`.js`/`.go`/`.rs`/`.java`/`.c`/`.cpp` source files the agent will edit.
      - A `RUN git clone <url> && git -C <dir> checkout <pinned-ref>` (or equivalent `git fetch` + `checkout`, `pip install git+...@<sha>`, `curl <tarball-at-tag>` + extract) inside the Dockerfile that delivers the source repo to a known path (e.g. `/testbed`, `/repo`, `/src`) at image build time. Code-SWE tasks commonly use this so the task ZIP doesn't carry gigabytes of source history. The clone MUST be pinned at a specific commit, tag, or sha256 digest — a floating branch HEAD is a FAIL on QD-09 check 4 (source pinned), but is not a FAIL on THIS check.

      Either delivery pattern is acceptable. Do NOT require the source repo to be staged under `environment/input_artifacts/`.

    The test: ask "is this file input **DATA** the task hands to the agent to READ (CSVs, PDFs, JSONL, datasets, documents, recordings — content the agent consumes but does not modify), or is it source **CODE** the agent will MODIFY (a codebase being patched, refactored, migrated), or is it build/install plumbing?" If it is data → must live under `input_artifacts/`. If it is code or plumbing → either committed-in-package or fetched-at-build-time is fine.

15. **Execution logs are authentic Harbor output, not hand-fabricated** — Real Harbor runs produce non-deterministic, machine-generated identifiers, timestamps, and trajectories. Hand-fabricated logs leave consistent fingerprints. Read every `result.json`, `config.json`, `trial.log`, `agent/trajectory.json`, `agent/kimi-cli.txt`, and any task-specific files in `agent/` (e.g. specialist sub-reports) across all three modes. FAIL if ANY of the following fingerprints appears — quote the exact offending value, hash pair, timestamp, or schema keys in your `reason`.

    **Do NOT flag these — they are normal Harbor-local outputs:** `trial_uri` values of the form `file:///Users/<trainer>/.../execution_logs/...` (Harbor writes `file://` URIs when run locally on a trainer machine; the trainer's username appearing in the path is expected, not a fabrication signal); `session_id: "unknown"` in `trajectory.json` (this is the Kimi CLI default literal when no upstream session ID is injected and appears in every authentic local run); and **`task_checksum` values that differ across `oracle`, `single-kimi-agent`, and `multi-kimi-agent` runs** (Harbor computes `task_checksum` over the task directory state at the moment each run starts — `execution_logs/` from earlier runs is part of the directory by the time later runs begin, so the three checksums legitimately differ. Cross-run divergence is NOT evidence of different task versions or hand-fabricated logs. Only flag `task_checksum` under (a) below — when the value itself is a placeholder string rather than a 64-char hex SHA256).

    (a) **Placeholder or sequential identifiers** — `task_checksum`, `job_id`, `trial_id`, `run_id`, or any UUID-shaped field contains a hand-typed value instead of a real one. Concrete signals: `"stable-checksum-redacted-for-delivery"`, `"redacted"`, `"placeholder"`, `"fake-..."`, `"TODO"`, `"single-kimi-job-0001"`, `"multi-kimi-job-0002"`, or sequential numeric suffixes (`-0001`, `-0002`) that are clearly hand-typed. Real `task_checksum` is a 64-char lowercase hex SHA256; real `job_id`/`trial_id` is UUID4 (`8-4-4-4-12` hex with dashes) or `<task_uuid>__<random_short_id>` where `<random_short_id>` is mixed-case alphanumeric.

    (b) **Cross-trial cloning** — Compute `sha256sum` of `agent/trajectory.json` across all `single-kimi-agent` trials; do the same for `multi-kimi-agent` trials. FAIL if two or more trials within a single mode produce identical SHA256 hashes — real agent runs are stochastic (sampling temperature, sub-agent timing, embedded timestamps), so byte-identical trajectories across trials within a mode means only one run was produced and copy-pasted. Apply the same hash comparison to any task-specific files written into `agent/` (specialist sub-reports like `*_report.json`, `output.json`, custom artifacts) — byte-identical content across trials within the same mode is a fabrication signal even when the trial-level reward differs.

    (c) **Zero-microsecond timestamps everywhere** — Real system clocks produce sub-second jitter. Scan every ISO-8601 timestamp field in `result.json`, `config.json`, `trial.log`, `job.log` (`started_at`, `finished_at`, `created_at`, etc.) across all trials. FAIL if **every** timestamp ends in `.000000Z` (or `.000Z`, or has no fractional seconds at all). Occasional round timestamps on schedule boundaries can occur; uniformly zero microseconds across dozens of independent timestamps cannot.

    (d) **Hand-staged round timeline** — Compare the job-level `started_at` of `oracle`, `single-kimi-agent`, and `multi-kimi-agent`. FAIL if all three start times land exactly on round minutes (e.g. `18:00:00Z`, `18:05:00Z`, `18:20:00Z`) with neat 5/15/20-minute gaps and no second-level or microsecond jitter — real Harbor scheduling does not align to round minutes across runs.

    (e) **Trajectory uses non-Harbor schema** — Real Kimi CLI `trajectory.json` follows the ATIF schema. The exact contract:

    ```json
    {
      "schema_version": "ATIF-v1.6",
      "session_id": "<string>",
      "agent": {"name": "<str>", "version": "<str>", "model_name": "<str>"},
      "steps": [
        {
          "step_id": "<str>",
          "source": "<str>",
          "model_name": "<str>",
          "message": { ... },
          "tool_calls": [ ... ],
          "observation": { ... },
          "metrics": { ... }
        }
      ],
      "final_metrics": {
        "total_prompt_tokens": <int>,
        "total_completion_tokens": <int>,
        "total_cached_tokens": <int>,
        "total_steps": <int>
      }
    }
    ```

    Required top-level keys (all five): `schema_version`, `session_id`, `agent`, `steps`, `final_metrics`. `schema_version` must start with `"ATIF-"`. Each entry in `steps` must contain at minimum `step_id`, `source`, `message`, `tool_calls`, `observation`. FAIL if `trajectory.json` is missing any required top-level key, uses an author-invented schema instead (e.g. a top-level `result_summary` field carrying the agent narrative, a `notes` field, a `tool_call_log` array of custom-shaped entries, or a flat list of strings), or has `schema_version` not starting with `ATIF-`. List the actual top-level keys present and the missing required fields in your `reason`.

    (f) **AI-sanitized / summarized / edited transcripts.** Real Kimi CLI transcripts are FULL raw output — the trainer must copy `kimi-cli.txt`, `trajectory.json`, and `result.json` exactly as Harbor produces them. A trainer who runs an AI over the log to "tidy", "compress", "redact", or "summarize" it leaves clear fingerprints. FAIL on ANY of the following.

    **Reference shape of an authentic `kimi-cli.txt`** (from our example_tasks runs):
    - Size: single-agent ~150KB–2MB, multi-agent ~400KB–7.7MB. Anything under ~50KB is highly suspicious; under ~10KB is almost certainly tampered.
    - Line count: ~5,000–30,000 lines.
    - First line is raw JSON-RPC, never natural language. Authentic head:
      ```
      {"jsonrpc":"2.0","method":"event","params":{"type":"TurnBegin","payload":{"user_input":"You are an orchestrator..."}}}
      {"jsonrpc":"2.0","method":"event","params":{"type":"StepBegin","payload":{"n":1}}}
      {"jsonrpc":"2.0","method":"event","params":{"type":"ContentPart","payload":{"type":"text","text":"I'll"}}}
      ```
    - Event-type diversity: a real multi-agent transcript contains `TurnBegin`, `StepBegin`, `ContentPart` (heavy — token-by-token streaming), `ToolCallPart` (heavy — function-args streaming), `ToolCall`, `ToolResult`, `StatusUpdate`, `SubagentEvent`, `TurnEnd`. A file containing only ONE event type (typically only `SubagentEvent` spawn/complete pairs) is the orchestrator skeleton with all the actual work stripped out.

    **Tampering fingerprints** — quote the offending line/byte in your `reason`:

    - **Sanitization header at the top.** Any natural-language preamble in the first ~5 lines of `kimi-cli.txt` or as a non-schema field in `trajectory.json`. Concrete examples that have appeared in the wild: `Sanitized Kimi CLI transcript summary.`, `Agent mode: multi`, `Score under weighted verifier: 0.837.`, `Summary of agent run`, `Cleaned transcript`, `Redacted log`, `Compressed transcript`, `Below is a summary of...`. Real Harbor logs start with `{"jsonrpc":"2.0",...` on line 1 — they never introduce themselves.
    - **Suspicious file size.** `kimi-cli.txt < ~50KB` for a normal trial is a strong tampering signal. Cross-check against the trial's `agent_execution` duration in `result.json`: a multi-minute run that produced a tiny `kimi-cli.txt` is implausible. Quote the file path, byte size, and the trial's `agent_execution.started_at`/`finished_at` span.
    - **Missing event-type coverage.** Grep `kimi-cli.txt` for `"type":"<event>"` and enumerate the distinct event types present. FAIL if a multi-agent transcript contains only `SubagentEvent` (or only one or two types) — that means the messages, tool calls, observations, and content streaming were stripped. List the event types found, e.g. *"only `SubagentEvent` (16 spawn/complete pairs) — no `ContentPart`, `ToolCall`, `ToolResult`, or `StatusUpdate`"*.
    - **AI-narrative content inside raw logs.** Natural-language paragraphs, markdown headings (`# Summary`, `## Step 1`), bullet lists, or any prose summary inside what should be machine-emitted JSON-RPC. Real transcripts are 100% JSON-RPC lines.
    - **Trajectory steps replaced with summaries.** `agent/trajectory.json` `steps[].message.content` containing brief one-line summaries (e.g. *"Agent invoked ReadFile on policy_events.csv and got 500 rows"*) instead of the raw message body; `tool_calls[].arguments` replaced with `"<arguments redacted>"` / `"<args omitted>"` / `"..."`; `observation` fields containing one-line descriptions instead of raw tool output. Real `message.content` for an LLM turn is the full prose the model emitted; real `tool_calls[].arguments` is the JSON the model passed; real `observation` is the raw output the tool returned.

    The fix is always the same: copy execution logs exactly as Harbor produces them — never run them through an AI, regex sanitizer, or hand edit. Any "tidying", "compression", or "redaction" pass invalidates the package; re-run Harbor end-to-end.

16. **Execution logs reflect the CURRENT state of the task package, not a previous state** —

    The committed task package (`instruction.md`, `solution/`, `tests/`, `decomposition.yaml`, `environment/`, `task.toml`) is the source of truth. Every file under `execution_logs/` must have been produced by running Harbor against *this exact committed package* — not against an earlier draft of it. Trainers iterate: they tighten the instruction, change the oracle schema (flat → nested keys), swap input files, rewrite `solve.sh`, update the judge rubric. When any of those move and the recorded logs are not regenerated, the package becomes internally inconsistent — the currently committed judge against the recorded `agent/output.json` cannot produce the recorded `reward.json`. The benchmark silently lies, because the recorded numbers are not reproducible against the package the next reviewer will run.

    This check is **investigative, not a checklist** — Checks 1–15 enumerate specific failure modes, but the underlying intent is broader: would re-running Harbor against the current package produce logs structurally consistent with what is recorded? If you find any divergence between current state and recorded logs, that is a FAIL regardless of which artifact diverged.

    Mandatory procedure:

    STEP A. Read the **current** sources of truth:
    - `instruction.md` — especially any output-format block, declared output schema, deliverable list, required output path, and named input files
    - `tests/oracle.json` (llm-judge) or `tests/verify.py` / `tests/test.sh` (executable) — what the judge/verifier currently expects
    - `solution/solve.sh` and every file under `solution/` — what the gold solution currently produces, patches, or copies
    - `decomposition.yaml` — which sub-tasks and which files it currently names
    - `environment/input_artifacts/` (and the rest of `environment/`) — what inputs the agent is currently handed

    STEP B. Cross-check each piece of current state against the recorded `execution_logs/`. Open every trial's `agent/output.json` (llm-judge), `agent/trajectory.json`, `agent/kimi-cli.txt`, `verifier/reward.json` / `reward.txt`, and `verifier/test-stdout.txt` / `judge_justification.txt`. Probe for any of these drift patterns — and any other shape of drift you can think of:
    - **Output schema drift** — the recorded `agent/output.json` (llm-judge) or recorded patches (executable) use field names, key nesting, file paths, or function signatures that the *current* oracle/verifier no longer expects. Concrete fingerprint: recorded output uses flat keys like `bureau_coverage` while the current `tests/oracle.json` is nested as `coverage.bureau`, yet the recorded `reward.json` is `1.0` — the current judge cannot reproduce that score against the recorded output.
    - **Solution drift** — `solve.sh` references files (`/solution/oracle.json`, a patch file, a helper) whose current content differs from what the recorded oracle log shows the oracle agent producing or applying. The committed `solution/oracle.json` does not match the `agent/output.json` recorded in `execution_logs/oracle/`.
    - **Instruction drift** — `instruction.md` names a deliverable path, output key, or input file that does not appear in any recorded `output.json` or agent trajectory, or vice versa: every recorded trajectory references a file or key that `instruction.md` no longer mentions.
    - **Input-data drift** — `environment/input_artifacts/` currently contains files (or has filenames) that no recorded agent trajectory ever opens, or recorded trajectories open input files no longer shipped in the current `environment/`.
    - **Decomposition drift** — `decomposition.yaml` lists sub-tasks or file paths that never appear in the recorded multi-agent trajectory, or the recorded multi-agent trajectory shows a decomposition structure that the current `decomposition.yaml` does not describe.
    - **Judge-logic drift** — `tests/judge.py` or `tests/test.sh` currently evaluates against criteria, key paths, or rubric items absent from the recorded outputs, yet the recorded `reward.json` shows a passing score the current judge could not produce.

    The list is illustrative. Apply the same intent — "current package vs. recorded logs" — to find any other divergence.

    STEP C. Verdict.
    - **FAIL** if any concrete drift is found. Cite the current artifact (file path + verbatim quote of the key, path, schema, or field), cite the recorded artifact (file path + verbatim quote of the divergent or missing key/path/field), and state in one sentence why the current judge/verifier cannot produce the recorded reward from the recorded run. The recommended fix is always the same: regenerate `execution_logs/oracle/`, `execution_logs/single-kimi-agent/`, and `execution_logs/multi-kimi-agent/` from the current package — never hand-edit recorded outputs.
    - **PASS** only after a documented investigation. Your `reason` must list every (current-state artifact ↔ recorded-log artifact) pair you cross-checked. PASS-by-not-looking is not acceptable.

    Grounding: every FAIL must quote BOTH the current artifact AND the divergent recorded artifact verbatim, with both file paths. If you cannot produce that pair of quotes, the check PASSES — but only after the documented investigation in STEP B.

## Output Format
Return ONLY valid JSON:
```json
{
  "dimension": "QD-13",
  "result": "PASS" or "FAIL",
  "checks": [
    {"id": 1, "name": "environment_input_only", "result": "...", "reason": "..."},
    {"id": 2, "name": "solve_sh_applies_fix_only", "result": "...", "reason": "..."},
    {"id": 3, "name": "oracle_txt_not_contradicted", "result": "...", "reason": "..."},
    {"id": 4, "name": "test_sh_installs_deps", "result": "...", "reason": "..."},
    {"id": 5, "name": "reward_not_unconditional", "result": "...", "reason": "..."},
    {"id": 6, "name": "tests_not_in_image", "result": "...", "reason": "..."},
    {"id": 7, "name": "oracle_reward_consistent_with_log", "result": "...", "reason": "..."},
    {"id": 8, "name": "same_verifier_test_set_across_runs", "result": "...", "reason": "..."},
    {"id": 9, "name": "single_agent_reward_not_deflated", "result": "...", "reason": "..."},
    {"id": 10, "name": "multi_agent_not_oracle_copy", "result": "...", "reason": "..."},
    {"id": 11, "name": "no_prefilled_output_in_environment", "result": "...", "reason": "..."},
    {"id": 12, "name": "script_file_references_exist", "result": "...", "reason": "..."},
    {"id": 13, "name": "decomposition_no_restricted_paths", "result": "...", "reason": "..."},
    {"id": 14, "name": "input_artifacts_layout", "result": "...", "reason": "..."},
    {"id": 15, "name": "execution_logs_authentic", "result": "...", "reason": "..."},
    {"id": 16, "name": "logs_match_current_task_state", "result": "...", "reason": "..."}
  ],
  "justification": "Overall assessment in 2-3 sentences."
}
```
Result is FAIL if ANY check fails.
