# Project 1 — Handoff State

## What's done

**Problem chosen**: `OlymMATH-HARD-1-EN` (Geometry, from RUC-AIBOX/OlymMATH-eval, en_hard split)
- Statement: "If the distances from the eight vertices of a cube to a certain plane are 0, 1, 2, 3, 4, 5, 6, 7 respectively, consider all possible edge lengths of this cube. Assuming the possible edge lengths..." (sum of possible edge lengths / something — gold answer **210**)
- Full statement and gold in `environment/input_artifacts/problem.md`

**9 real model responses fetched** from RUC-AIBOX/OlymMATH-eval (response_id=0 across 9 model configs):

| Letter | Model | Extracted | Correct | Chars |
|---|---|---|---|---|
| A | qwen3-0.6b | 6 | False | 60117 |
| B | deepscaler-1.5b-preview | 49 | False | 12570 |
| C | still-3-1.5b-preview | 49/3 | False | 42443 |
| D | deepseek-r1-distill-qwen-1.5b | 49/3 | False | 26120 |
| E | openmath-nemotron-1.5b | (empty) | False | 114902 |
| F | light-r1-7b-ds | 21 | False | 36809 |
| G | openthinker2-7b | 140/3 | False | 66690 |
| H | skywork-or1-math-7b | 21 | False | 29662 |
| I | openmath-nemotron-7b | 21 | False | 29387 |

Distinct extracted answers: 6 different values across 9 responses — **strong diversity for the audit task**. None got 210.

**Folder layout already in place**:
```
9b3f1e7a2c5d4068e9f1a3b5c7d9e0b2-SWARMBENCH-FANOUT-REASONINGMATH-CUBE-3VIEWS-MIN-CUBES-AUDIT/
├── environment/
│   ├── Dockerfile  (standard python:3.12.11-slim)
│   └── input_artifacts/
│       ├── problem.md
│       ├── provenance.json  (9 entries with model names + correctness)
│       └── response_A.md ... response_I.md  (9 raw responses)
├── solution/
│   └── solve.sh  (oracle copy + echo)
└── tests/
    └── test.sh  (calls judge.py)
```

NOTE: Folder name still says CUBE-3VIEWS-MIN-CUBES from when I started with OlymMATH-HARD-3-EN. **Should be renamed to** `9b3f1e7a2c5d4068e9f1a3b5c7d9e0b2-SWARMBENCH-FANOUT-REASONINGMATH-CUBE-PLANE-DISTANCES-AUDIT` to reflect the actual problem.

## What's NOT done

1. **Audit each response's reasoning** — read response_A.md through response_I.md (each ~10-60K chars), identify which failure code applies. Pay attention to:
   - A (6): wildly wrong; likely guessed or used wrong formula
   - B (49): claims edge = 7 (took max distance), missing the √3
   - C, D (49/3): treats 7 as body diagonal, gets s = 7/√3, s² = 49/3 — only considers body-diagonal orientation
   - E (empty): incoherent / truncated
   - F, H, I (21): may have considered multiple orientations but stopped early; 21 = 6+7+8 perhaps
   - G (140/3): partial sum of some edge lengths

2. **Design closed-vocab failure codes** based on actual reasoning. Suggested starting set (verify against responses):
   - `incoherent_or_truncated` — empty extracted answer (E)
   - `single_orientation_only` — considers only one cube orientation, e.g. body-diagonal alignment, computes one s² (C, D)
   - `wrong_edge_length_formula` — wrong relationship between vertex distances and edge length (A, B)
   - `partial_orientation_enumeration` — finds some valid orientations but misses others (F, G, H, I)
   - `closed_form_misapplied` — applies a formula from a different geometric problem

3. **Author oracle.json** in both `tests/` and `solution/` (byte-identical):
   - `gold_final_answer: "210"`
   - `acceptable_solution_ids: []` (none correct)
   - `per_response_assessment`: 9 entries, each with `solution_id`, `extracted_answer`, `final_answer_correct=false`, `failure_reasons`
   - Optional `gold_intermediate_value` field for math-derivation scoring (like S_44 in OLYMMATH)

4. **Write `instruction.md`** with:
   - Math-reasoning primary-activity framing (independent derivation of 210 first)
   - Problem statement
   - Closed failure-reason vocabulary with abstract definitions (no per-response leak)
   - Boundary rules between codes (mutually exclusive where needed)
   - Output schema

5. **Write `decomposition.yaml`** following PASSED-TETRAHEDRON-INCENTER shape:
   - 1 × `verify-gold-math` (derive 210 independently, do NOT inspect responses)
   - 9 × `audit-response-{a..i}` (each reads `/workspace/instruction.md` + ONE response, generic template)
   - 9 × `verify-response-{a..i}` (second-pass independent re-audit) — OPTIONAL but boosts multi
   - 1 × `synthesize-final-audit` (depends on all upstream)

6. **Write `tests/judge.py`** as deterministic Python (no LLM judge):
   - Per-response: all-or-nothing 30 pts on (solution_id, extracted_answer, final_answer_correct, failure_reasons set)
   - gold_final_answer: 50 pts (literal "210")
   - acceptable_solution_ids: 2 pts
   - Total: ~322 or scale up with verify layer

7. **Write `task.toml`**:
   - `verifier_type = "executable"`
   - `coordination_pattern = "fan-out-synthesize"`
   - `domain = "reasoning-math"`
   - `estimated_sub_agents = 11` or 20 with verify
   - `human_solving_hours_estimate ≥ 10`
   - Full `why_multi_agent` narrative

8. **Write `solution/justification.md`** with per-response rationale + gold derivation

9. **Local sanity tests**: oracle = 1.0, perturbed = <1.0, no failure-code leaks in decomposition, YAML parses

## Reference pattern

Closest 6-folder match: **PASSED-TETRAHEDRON-INCENTER-CLAIMS-AUDIT** (gap 0.44)
- 9 candidate responses
- FANOUT decomposition
- Closed-vocab failure codes
- Deterministic Python judge with exact-set match per response
- All-or-nothing 30 pts per response

## Quality dimensions (all must pass per LLM Review template)

- multi_agent_necessity, output_format_determinism, oracle_quality, aht_calibration,
- multi_agent_execution_quality, environment_reproducibility, instruction_clarity,
- real_world_relevance, decomposition_quality, mode_symmetry, harbor_conventions,
- agent_mode_fairness, anti_cheat, verifier_agent_alignment.

In particular: NO per-response failure-code leakage in decomposition.yaml.

## Next session entry point

Read this HANDOFF.md, then read each of the 9 responses to design the failure code vocabulary based on actual reasoning patterns. Then author oracle.json, instruction.md, decomposition.yaml, judge.py, task.toml, justification.md in one batch.
