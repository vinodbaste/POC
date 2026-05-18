# Sequence-Envelope Solution Audit

You are auditing eight real, unedited model responses to a deductive reasoning puzzle: four mislabeled envelopes of monotonic number sequences. The canonical worst-case minimum is **15 inspections** (1 inspection of the Mixed-labeled envelope to identify its pure type, plus 14 same-type observations to force a distinction against a 7/13 mixed envelope).

Working directory: `/workspace`.

## Input files

- `/input_artifacts/problem_statement.md`
- `/input_artifacts/provenance.md`
- `/input_artifacts/candidate_solutions/response_A.md` ... `response_H.md`

## Task

1. Read problem_statement.md and derive the canonical minimum (15) yourself.
2. Audit each of the 8 candidate responses (A-H).
3. For each response, identify the EXACT SET of `failure_reasons` codes (from the controlled vocabulary below) whose triggering conditions are concretely instantiated in that response's text. Each response typically has 1-7 applicable codes.
4. For each response, choose ONE `primary_failure_code` from its `failure_reasons` set (or `"NONE"` if empty) — the single most load-bearing diagnostic defect.
5. Produce all required per-response and top-level fields per the output schema below.

## Allowed failure-reason codes (10 codes total)

- `wrong_final_number` — final stated number deviates from 15.
- `contradictory_final_answer` — response oscillates among incompatible counts (e.g., 2, 3, 14, 15) without committing.
- `no_concrete_strategy` — closing synthesis step is hand-wavy or lacks branch-by-branch label-fixing rule.
- `invalid_upper_bound` — proposed strategy's upper-bound proof fails in some worst-case branch.
- `missing_lower_bound` — no impossibility proof for fewer-than-claimed inspections.
- `not_worst_case` — strategy treats favorable single-draw observations as resolving worst-case ambiguity.
- `invalid_one_draw_inference` — claims one observed sequence from an envelope that could still be mixed proves the envelope is pure.
- `unnecessary_mixed_pair_requirement` — response adds inspections solely to determine exact 2-type composition of the mixed envelope.
- `fatal_wrong_claim` — load-bearing "forced by contradiction", "remaining are determined", "cycle uniquely", or "follow directly" assertion.
- `non_terminating_or_no_final_answer` — no committed final numeric answer at all; stands alone when present.

## Scoring rule

The verifier (llm-judge) scores deterministically against the oracle with substantive interpretation on per-response sets and primary codes. Weights:

- `gold_final_answer` (string match against "15"): 4 points
- `acceptable_solution_ids` (set match): 2 points
- Per response (8 entries):
  - `final_answer_correct` (exact bool): 5
  - `failure_reasons` (substantive set match; 30 exact, 15 off-by-one substantively-equivalent, 8 overlap >=50% with divergence, 0 otherwise): 30 max
  - `primary_failure_code` (25 exact; 10 if in oracle's failure_reasons set but not primary): 25 max
  - `primary_failure_code_evidence` (>=50 chars substantive): 8
  - `alternative_codes_considered` (>=2 unique well-formed entries; each code from vocab or "NONE" DIFFERENT from primary; reason_excluded >=20 chars): 8
  - `failure_reason_evidence` per oracle-listed code (>=20 chars): 5 per code
  - `code_application_count` (integer = len(failure_reasons)): 10
  - `primary_in_set_check` (bool, true iff primary in failure_reasons OR (primary=="NONE" and failure_reasons empty)): 5
  - `evidence_key_completeness` (integer = # evidence keys matching failure_reasons): 8
- `code_application_table` per key (10 keys × sorted-list match): 100 each
- `response_count_per_code` per key (10 keys × integer match): 20 each
- `cross_response_observations` (>=300 chars): 30

Every dict aggregation field MUST contain every required key with a JSON-valid value (use `[]` for empty lists, `0` for empty integer counts — NEVER `null`, NEVER omit a key). Outputting `null` or omitting a key forfeits the full weight for that key.

## Output

Write to `/logs/agent/output.json`:

```json
{
  "gold_final_answer": "15",
  "acceptable_solution_ids": [],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": <bool>,
      "failure_reasons": [<sorted list of codes from the 10-code vocabulary>],
      "primary_failure_code": "<one code in failure_reasons, or \"NONE\">",
      "primary_failure_code_evidence": "<string >=50 chars>",
      "failure_reason_evidence": {"<code in failure_reasons>": "<string >=20 chars>"},
      "alternative_codes_considered": [{"code": "<code different from primary, unique>", "reason_excluded": "<>=20 chars>"}, {"code": "<another>", "reason_excluded": "<>=20 chars>"}],
      "code_application_count": <integer>,
      "primary_in_set_check": <bool>,
      "evidence_key_completeness": <integer>
    }
  ],
  "code_application_table": {
    "contradictory_final_answer": [<sorted response_ids>],
    "fatal_wrong_claim": [<sorted>],
    "invalid_one_draw_inference": [<sorted>],
    "invalid_upper_bound": [<sorted>],
    "missing_lower_bound": [<sorted>],
    "no_concrete_strategy": [<sorted>],
    "non_terminating_or_no_final_answer": [<sorted>],
    "not_worst_case": [<sorted>],
    "unnecessary_mixed_pair_requirement": [<sorted>],
    "wrong_final_number": [<sorted>]
  },
  "response_count_per_code": {"<each of 10 codes>": <integer>},
  "cross_response_observations": "<string >=300 chars>"
}
```

Include exactly 8 entries in `per_response_assessment` for response_A through response_H in alphabetical order. Every response_id from response_A through response_H must appear in `code_application_table` once per code in its `failure_reasons` set. `response_count_per_code[code]` must equal `len(code_application_table[code])` for every code.
