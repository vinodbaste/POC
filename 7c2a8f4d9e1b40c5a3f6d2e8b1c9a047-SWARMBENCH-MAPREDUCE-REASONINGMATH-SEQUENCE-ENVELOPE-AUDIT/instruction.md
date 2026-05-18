# Sequence-Envelope Solution Audit

Working directory: `/workspace`.

You are auditing proposed solutions to a deductive reasoning puzzle about four mislabeled envelopes of monotonic number sequences. Your primary task is to mathematically derive the minimum number of inspections required to guarantee correct relabeling (a worst-case combinatorial reasoning problem), then audit each candidate solution against that derivation. The mathematical derivation - establishing the upper bound via an explicit inspection strategy and the lower bound via indistinguishable-case reasoning - is the dominant cognitive activity of every sub-task in this workflow.

The only puzzle source is the problem statement. The provenance file describes where the candidate responses came from; it is not a source for solving the puzzle and does not contain oracle labels.

## Input files

Read these files:

- /input_artifacts/problem_statement.md
- /input_artifacts/provenance.md
- /input_artifacts/candidate_solutions/response_A.md
- /input_artifacts/candidate_solutions/response_B.md
- /input_artifacts/candidate_solutions/response_C.md
- /input_artifacts/candidate_solutions/response_D.md
- /input_artifacts/candidate_solutions/response_E.md
- /input_artifacts/candidate_solutions/response_F.md
- /input_artifacts/candidate_solutions/response_G.md
- /input_artifacts/candidate_solutions/response_H.md

## Required workflow

1. Solve the original puzzle yourself from /input_artifacts/problem_statement.md.
2. Determine the minimum number of inspections needed to guarantee correct relabeling in the worst case, taking the 7/13 mixed-envelope split into account.
3. Determine what a valid sufficiency proof and a valid impossibility proof must establish.
4. Audit each candidate solution independently using criteria C1 through C8 below.
5. Produce one final JSON report.

## Audit criteria

For each candidate solution, evaluate the following eight binary criteria. Each criterion must be exactly true or false.

### C1_correct_final_answer

Set to true if and only if the solution states the actual minimum guaranteed number of inspections for the puzzle.

Set to false if the solution gives a different number, gives multiple conflicting final answers, or does not state a final minimum.

### C2_concrete_strategy

Set to true if and only if the solution gives an explicit inspection strategy, not just a final number.

The strategy must specify:
- which envelope or envelopes to inspect;
- how many sequences to inspect from those envelopes;
- how the strategy adapts to possible observations;
- how the labels are fixed after the observations.

Set to false if the solution only gives a number, gives only a vague idea, or does not connect the proposed number to a concrete strategy.

### C3_valid_upper_bound

Set to true if and only if the solution correctly proves that its proposed number of inspections is sufficient to guarantee correct relabeling.

A valid upper-bound proof must work for every possible legal arrangement of the envelopes and every possible unlucky sequence of draws consistent with the envelope contents, including the 7/13 split in the mixed envelope.

Set to false if the proof only works in a favorable branch, depends on luck, leaves multiple labelings possible, or does not show how all four labels are fixed.

### C4_valid_lower_bound

Set to true if and only if the solution correctly proves that fewer inspections than its proposed minimum cannot guarantee success.

A valid lower-bound proof must rule out all strategies using fewer inspections, not merely show that one particular strategy can fail.

An acceptable lower-bound argument may use indistinguishable-case reasoning: construct two or more legal envelope arrangements that produce the same observations under a smaller inspection budget but require different final labels.

Set to false if the solution gives no lower-bound argument, only asserts minimality, or argues only that its own strategy would need more draws.

### C5_worst_case_guarantee

Set to true if and only if the solution treats the problem as a worst-case guarantee problem.

Set to false if it relies on probability, expected outcomes, likely outcomes, lucky draws, favorable cases, or one particular sequence of observations.

### C6_no_invalid_one_draw_inference

Set to true if and only if the solution never claims that one observed sequence from an envelope that could still be mixed proves that the envelope is pure.

Allowed: one draw from an envelope can prove purity only if the solution has already logically established that the envelope cannot be mixed. The Mixed-labeled envelope is one such case, since its label is wrong; one draw from it does prove its pure type.

Not allowed: one draw from an envelope labeled "Strictly Increasing", "Strictly Decreasing", or "Constant" proves that envelope is pure unless the mixed case has already been ruled out for that envelope.

### C7_no_exact_mixed_pair_requirement

Set to true if and only if the solution understands that the task only requires assigning the correct label "Mixed" to the correct envelope. The task does not require determining whether the mixed envelope contains increasing-decreasing, increasing-constant, or decreasing-constant sequences.

Set to false if the solution adds extra inspections solely because it thinks the exact two-type composition of the mixed envelope must be identified.

It is acceptable if the strategy incidentally discovers the exact mixed pair. It is not acceptable if the solution says the exact pair is required to fix the labels.

### C8_no_fatal_wrong_claim

Set to true if and only if the solution contains no fatal logical claim that contradicts the problem or invalidates the proof.

Fatal wrong claims include:
- saying an envelope known to be mislabeled with "Mixed" might actually be the mixed envelope;
- treating any of the pure-labeled envelopes as if its label were correct;
- saying remaining envelopes are forced when two or more legal assignments remain possible;
- confusing a possible success path with a guaranteed strategy;
- treating a probability argument as a guarantee.

## Verdict rule

Use this deterministic rule:

- ACCEPT if and only if all criteria C1 through C8 are true.
- REJECT otherwise.

A solution with the correct final answer but invalid reasoning must be rejected.

## Verifier scoring rule

The verifier uses weighted label scoring over the per-response audit labels.

For each candidate response, the scored labels are C1-C8, verdict, and primary_failure_code. A label earns its assigned weight only if it matches the oracle exactly.

The weights are:
- C1_correct_final_answer: 8 (per response)
- C2_concrete_strategy: 1 (per response)
- C3_valid_upper_bound: 12 (per response)
- C4_valid_lower_bound: 12 (per response)
- C5_worst_case_guarantee: 5 (per response)
- C6_no_invalid_one_draw_inference: 15 (per response)
- C7_no_exact_mixed_pair_requirement: 15 (per response)
- C8_no_fatal_wrong_claim: 30 (per response)
- verdict: 35 (per response)
- primary_failure_code: 140 (per response)
- criterion_evidence per criterion (presence + >=20 chars): 5 (per response per criterion)
- primary_failure_code_evidence (presence + >=50 chars): 8 (per response)
- alternative_codes_considered (>=2 well-formed entries): 8 (per response)
- criteria_satisfied_count (integer match against oracle): 10 (per response)
- verdict_consistency_check (bool match against oracle): 15 (per response)
- consistency_table per key (sorted-list match against oracle): 70 (top level, 10 keys)
- criterion_pass_rate per key (integer match against oracle): 50 (top level, 8 keys)
- verdict_distribution per key (sorted-list match against oracle): 100 (top level, 2 keys)
- criterion_pair_co_pass_count per key (integer match against oracle): 12 (top level, 28 pairs)
- response_pair_criterion_agreement per key (integer match against oracle): 10 (top level, 28 pairs)
- cross_response_observations (presence + >=300 chars): 30 (top level)

The total possible weight per task is 4778. The reported reward is total_earned / 4778 clipped to [0.0, 1.0]. An exact JSON-equality match between agent output and oracle short-circuits to reward = 1.0. Every dict aggregation field MUST contain every required key with a JSON-valid value (use [] for empty lists, 0 for empty integer counts — NEVER null, NEVER omit a key); the verifier penalizes null or missing keys as the full weight loss for that key.

brief_justification, summary, accepted_solutions, rejected_solutions, and best_solution are required for report completeness, but they are not scored.

## Primary failure code

Use exactly one of these codes for primary_failure_code:

- NONE
- WRONG_FINAL_NUMBER
- CONTRADICTORY_FINAL_ANSWER
- NO_CONCRETE_STRATEGY
- INVALID_UPPER_BOUND
- MISSING_LOWER_BOUND
- NOT_WORST_CASE
- INVALID_ONE_DRAW_INFERENCE
- UNNECESSARY_MIXED_PAIR_REQUIREMENT
- FATAL_WRONG_CLAIM

Use NONE only for accepted solutions.

### Primary-failure-code selection guidance

Many candidate solutions exhibit multiple defects simultaneously. The primary_failure_code captures the single most diagnostic failure mode - the one whose absence would have been most likely to produce a valid proof. Use the following disambiguation order when multiple codes plausibly apply:

1. If the final stated number does not equal the canonical minimum and the strategy is otherwise structurally complete, prefer WRONG_FINAL_NUMBER.
2. If the response oscillates among incompatible inspection counts and never settles, prefer CONTRADICTORY_FINAL_ANSWER over WRONG_FINAL_NUMBER.
3. If the strategy is missing concrete branch-by-branch label-fixing rules, prefer NO_CONCRETE_STRATEGY over downstream defects that follow from the missing strategy.
4. If a load-bearing one-draw purity inference from a possibly-mixed envelope drives the proposed minimum, prefer INVALID_ONE_DRAW_INFERENCE over NOT_WORST_CASE.
5. If the response acknowledges worst-case framing for one envelope but abandons it for others, prefer NOT_WORST_CASE.
6. If the response adds extra inspections to determine the exact two-type composition of the mixed envelope, prefer UNNECESSARY_MIXED_PAIR_REQUIREMENT.
7. If the strategy is structurally complete and the upper bound holds but the lower bound is only asserted from the strategy's arithmetic, prefer MISSING_LOWER_BOUND.
8. If the upper-bound argument leaves multiple legal labelings open in some worst-case branch, prefer INVALID_UPPER_BOUND.
9. If the response asserts that remaining envelopes are forced by elimination or contradiction when multiple legal assignments remain consistent, prefer FATAL_WRONG_CLAIM.

Apply codes only when the triggering condition is concretely instantiated in the response's text. Do not infer codes from absence of discussion alone.

### Worked example of the canonical strategy

For reviewer calibration, the canonical worst-case strategy structure is: inspect one item from the envelope labeled with the type that cannot match the contents (the Mixed-labeled envelope is the natural choice because its all-labels-wrong constraint forces it to be pure), record the identified pure type, then inspect a fixed number of items from a second envelope chosen to force a decisive distinction between pure and 7/13 mixed in the worst case. The number of items required equals the size of the mixed envelope's majority side plus one, because a 7/13 mixed envelope cannot produce more than thirteen consecutive items of any single type, and a pure envelope produces an unbounded run of one type. After this second inspection, the all-labels-wrong constraint forces the remaining two envelopes by elimination, requiring no additional inspections. The total inspection count is one plus the majority-plus-one count.

A valid lower-bound proof must show that no strategy using fewer inspections suffices. The canonical lower-bound construction exhibits two legal envelope arrangements that produce identical observations under any strictly-smaller inspection budget but require different placements of the Mixed label.

### Common audit anti-patterns

The following patterns recur across candidate responses and require careful classification:

- Asserting that "all labels are wrong" forces a specific assignment after a single observation. This is fatal because four labels and four envelopes with a derangement constraint still leave multiple legal assignments after one observation.
- Treating one observation per envelope as identifying that envelope's pure type. This violates C6 when the envelope could still be the mixed envelope returning its majority type on the first draw.
- Inflating the inspection count by adding draws "to determine the exact mixed pair". The task does not require identifying which two pure types compose the mixed envelope; it only requires labeling the mixed envelope correctly.
- Claiming minimality because the response's own strategy could not be reduced. A valid lower bound must rule out all strategies, not just the proposed one.
- Treating a probability-of-success argument as a worst-case guarantee. Worst-case guarantees require the proof to hold across every adversarial choice of envelope contents consistent with the observations so far.
- Confusing a possible success path with a guaranteed strategy. A guarantee must succeed on every legal branch, not merely on a favorable observation sequence.

### Glossary

- Envelope: one of the four physical containers, each labeled with a sequence type that is necessarily wrong.
- Pure envelope: an envelope whose 20 sequences are all of one type (Strictly Increasing, Strictly Decreasing, or Constant).
- Mixed envelope: the envelope whose 20 sequences split 7/13 between two of the three sequence types.
- Pure-labeled envelope: an envelope whose label is one of the pure-type strings ("Strictly Increasing", "Strictly Decreasing", "Constant"). Such an envelope is either a pure envelope of a different type, or the mixed envelope.
- Mixed-labeled envelope: the envelope whose label is "Mixed". Because all labels are wrong, this envelope is necessarily a pure envelope.
- Worst-case guarantee: a strategy whose correctness holds for every legal envelope arrangement and every adversarial draw sequence consistent with the envelope contents.
- Indistinguishable-case argument: a lower-bound technique that constructs two legal envelope arrangements producing identical observations under a smaller inspection budget but requiring different correct labelings.
- Identified pure type: the sequence type observed in the first draw from the Mixed-labeled envelope; because that envelope is pure, this single observation suffices to identify its type.

### Criterion-by-criterion adjudication examples

For each binary criterion, the following examples illustrate the boundary between trigger and non-trigger. Use these examples only as calibration; the authoritative trigger language is the criterion definition above.

- C1_correct_final_answer fires when the response commits to one number that equals the canonical worst-case minimum. It does NOT fire when the response gives a range such as "15 or more", lists alternatives ("either 15 or 16"), or never states a single committed final value.
- C2_concrete_strategy fires when the response specifies which envelopes are inspected, how many items are drawn from each, what observations are expected, and how each branch fixes the four labels. It does NOT fire when the response replaces the per-branch label-fixing rule with an aggregate appeal such as "by the all-labels-wrong constraint the remaining labels are determined" without showing the determination.
- C3_valid_upper_bound fires when the response's strategy produces a unique label assignment in every legal envelope arrangement and every observation sequence consistent with the envelope contents, including the 7/13 mixed-envelope branch. It does NOT fire when the proof works only in the favorable branch where the second inspection returns the identified pure type.
- C4_valid_lower_bound fires when the response gives a real impossibility proof for fewer-than-claimed inspections, typically via an indistinguishable-case construction. It does NOT fire when the response says "fewer cannot work because my strategy uses k" - that is an assertion about the proposed strategy, not about all strategies.
- C5_worst_case_guarantee fires when the response explicitly addresses the unlucky-draw branches and shows the strategy still succeeds. It does NOT fire when the response invokes probability, expected outcomes, "likely" assumptions, or stops at one favorable draw sequence.
- C6_no_invalid_one_draw_inference fires (true) when the response never claims that one observed item from an envelope that could still be mixed proves the envelope is pure. The Mixed-labeled envelope is exempt because its label is known wrong. C6 should NOT be set false merely because a strategy is insufficient; it is false only when a specific one-draw purity claim is the load-bearing inference.
- C7_no_exact_mixed_pair_requirement fires (true) when the strategy works without identifying which two pure types compose the mixed envelope. C7 is false only when the response explicitly adds inspections solely to determine the mixed pair (e.g., "we then take a second sequence to identify which two types are combined").
- C8_no_fatal_wrong_claim fires (true) when no proof-invalidating claim is asserted. Common C8-false patterns include "the remaining labels are forced" when multiple legal labelings remain, treating a pure-labeled envelope as if its label were correct, and "must be" claims where only "could be" is justified.

### Walked scoring example

Consider a hypothetical response that proposes the following: inspect two items from each of three envelopes (six inspections total) and label each envelope by majority type observed; if all three envelopes show distinct types, the fourth is the mixed envelope. The response concludes "the minimum is 6".

- C1 is false because 6 differs from the canonical worst-case minimum.
- C2 is true because the strategy is explicit: which envelopes, how many items, how labels are assigned.
- C3 is false because in the branch where the mixed envelope's two drawn items happen to be the same type as a pure envelope's, the assignment is ambiguous.
- C4 is false because the response gives no impossibility proof for fewer than 6 inspections.
- C5 is false because the strategy depends on a favorable observation pattern.
- C6 is false because the response infers an envelope's pure type from two same-type draws, which is insufficient against a 7/13 mixed envelope returning 13 of one type before its first second-type draw.
- C7 is true because the strategy does not require identifying the exact mixed pair.
- C8 is false because the "if all three show distinct types, the fourth is mixed" assertion is a load-bearing claim that fails on adversarial draw sequences.

Verdict: REJECT (multiple criteria false). The most diagnostic primary_failure_code is INVALID_ONE_DRAW_INFERENCE because the load-bearing defect is the two-draw purity inference, not the arithmetic of the final count.

### Resolution rules for borderline cases

The following pairings disambiguate frequent edge cases in primary_failure_code selection:

- Correct final number, valid upper-bound strategy, but no impossibility proof for fewer inspections: primary code is MISSING_LOWER_BOUND. Verdict is REJECT because C4 is false.
- Correct strategy structure and worst-case framing, but inspection count is one over the optimum due to a preliminary inspection that could be absorbed into the verification phase: primary code is WRONG_FINAL_NUMBER. The upper-bound label C3 may remain true.
- Strategy explicitly oscillates among two or more incompatible final numbers without committing to one: primary code is CONTRADICTORY_FINAL_ANSWER, taking precedence over WRONG_FINAL_NUMBER.
- Strategy provides an explicit inspection plan but the closing synthesis step ("at this point enough information has been gathered") fails to specify how each branch resolves the four labels: primary code is NO_CONCRETE_STRATEGY.
- Strategy treats a single observation per envelope as proving that envelope's pure type in branches where the envelope could still be mixed: primary code is INVALID_ONE_DRAW_INFERENCE.
- Strategy never engages with the worst-case branch where a mixed envelope returns the same type as a pure envelope on its first draw, instead relying on favorable observations: primary code is NOT_WORST_CASE (unless the explicit one-draw purity inference is the load-bearing defect, in which case prefer INVALID_ONE_DRAW_INFERENCE).
- Strategy depends on a load-bearing "must be" or "forced by contradiction" claim where multiple legal labelings remain consistent: primary code is FATAL_WRONG_CLAIM.

### Universal phrase-pattern rules (authoritative)

The following phrase-pattern rules apply uniformly to every candidate response. No response is pre-assigned to any rule; each rule fires only when its textual pattern is concretely present in that response's text.

C2 (concrete strategy) is TRUE only when the response specifies a multi-branch plan: which envelopes are inspected, how many items are drawn from each, what each observation implies, and how each branch fixes all four labels. A single-inspection plan followed by a sentence like "forced by contradiction" or "the remaining are determined" is NOT a concrete strategy and C2 should be FALSE. C2 should also be FALSE when the response oscillates among multiple incompatible inspection counts (e.g., proposes 2, then 3, then 14, then a final 3) without committing to one coherent plan, and when the response acknowledges single-draw ambiguity (e.g., "this envelope is either mixed or purely X") and then concludes "enough information has been gathered" without specifying the branch-by-branch label-fixing rule.

C4 (valid lower bound) is TRUE only when the response constructs an indistinguishable-case argument exhibiting two legal envelope arrangements that produce identical observations under a strictly smaller inspection budget. Arithmetic derivation of the count from the response's own strategy does not satisfy C4 even when the count and strategy are correct.

C6 (no invalid one-draw inference) is TRUE by default. It becomes FALSE only when the response explicitly treats one observed sequence from an envelope that could still be mixed as proving that envelope is pure (e.g., "one draw from envelope X gave type T, therefore envelope X is the pure T envelope" without 14-draw verification). C6 does NOT fire false when:
- the single-draw observation is from the Mixed-labeled envelope (that label is known wrong, so the inference is valid);
- the response acknowledges single-draw ambiguity (such as "this envelope is either mixed or purely increasing") without collapsing it to a purity claim;
- the response's strategy is merely insufficient without an explicit single-draw purity claim.

C8 (no fatal wrong claim) is TRUE by default. It becomes FALSE when the response asserts a proof-invalidating claim. Triggering phrase patterns include: "determined automatically by elimination" after too-few observations, "the remaining are forced by contradiction", "the remaining labels cycle uniquely", "enough information has been gathered to deduce the final arrangement uniquely" after acknowledged ambiguity, and "the assignment follows directly" from single observations. Any of these patterns triggers C8=FALSE even when WRONG_FINAL_NUMBER or another code is the best primary_failure_code for the response. C8 FALSE is INDEPENDENT of C3 and of the primary_failure_code.

Primary failure code selection (ties broken in this order, applied universally to every response):
- CONTRADICTORY_FINAL_ANSWER for responses that oscillate among incompatible final counts.
- NO_CONCRETE_STRATEGY for responses whose closing synthesis step is hand-wavy and does not specify how remaining branches collapse.
- INVALID_ONE_DRAW_INFERENCE only when a load-bearing single-draw purity inference from a possibly-mixed envelope drives the count; do NOT pick this code when the only single-draw observation present is from the Mixed-labeled envelope.
- NOT_WORST_CASE when the response treats favorable single-draw observations as resolving worst-case ambiguity without an explicit one-draw purity inference.
- UNNECESSARY_MIXED_PAIR_REQUIREMENT when the response adds inspections solely to identify the exact mixed two-type composition.
- MISSING_LOWER_BOUND when the strategy is otherwise complete (correct number, valid upper bound, worst-case framing) but no impossibility argument is given.
- INVALID_UPPER_BOUND when the upper-bound elimination leaves multiple legal labelings open in some worst-case branch.
- FATAL_WRONG_CLAIM when the load-bearing defect is a proof-invalidating "forced" or "cycle uniquely" assertion not consistent with multiple legal labelings remaining open.
- WRONG_FINAL_NUMBER only when the strategy is structurally correct in every other way but the inspection count deviates from the optimum, typically due to a preliminary inspection that could have been absorbed into the verification phase.
- Do NOT default to WRONG_FINAL_NUMBER simply because C1 is FALSE. Do NOT default to INVALID_ONE_DRAW_INFERENCE simply because a single-draw observation appears or the strategy is insufficient. Pick the most diagnostic code that describes the load-bearing defect.

Note that the workflow steps listed in the Required Workflow section above are intended as guidance for the auditor's reasoning process; the verifier scores only the final JSON output and its labels, not the auditor's working procedure.

## Output Instructions

Write your final answer to /logs/agent/output.json as a single JSON object with this exact structure:

{
  "evaluations": [
    {
      "solution_id": "response_A",
      "criteria": {
        "C1_correct_final_answer": <bool>,
        "C2_concrete_strategy": <bool>,
        "C3_valid_upper_bound": <bool>,
        "C4_valid_lower_bound": <bool>,
        "C5_worst_case_guarantee": <bool>,
        "C6_no_invalid_one_draw_inference": <bool>,
        "C7_no_exact_mixed_pair_requirement": <bool>,
        "C8_no_fatal_wrong_claim": <bool>
      },
      "verdict": "ACCEPT" or "REJECT",
      "primary_failure_code": <string>,
      "brief_justification": <string>,
      "criterion_evidence": {
        "C1_correct_final_answer": <string, at least 20 characters, citing or paraphrasing the response text that justifies the C1 boolean above>,
        "C2_concrete_strategy": <string, at least 20 characters, citing or paraphrasing the response text that justifies the C2 boolean above>,
        "C3_valid_upper_bound": <string, at least 20 characters, citing or paraphrasing the response text that justifies the C3 boolean above>,
        "C4_valid_lower_bound": <string, at least 20 characters, citing or paraphrasing the response text that justifies the C4 boolean above>,
        "C5_worst_case_guarantee": <string, at least 20 characters, citing or paraphrasing the response text that justifies the C5 boolean above>,
        "C6_no_invalid_one_draw_inference": <string, at least 20 characters, citing or paraphrasing the response text that justifies the C6 boolean above>,
        "C7_no_exact_mixed_pair_requirement": <string, at least 20 characters, citing or paraphrasing the response text that justifies the C7 boolean above>,
        "C8_no_fatal_wrong_claim": <string, at least 20 characters, citing or paraphrasing the response text that justifies the C8 boolean above>
      },
      "primary_failure_code_evidence": <string, at least 50 characters, explaining why the chosen primary_failure_code is the most diagnostic for this response>,
      "alternative_codes_considered": [
        {"code": <one of the controlled-vocabulary primary failure codes>, "reason_excluded": <string, brief justification for why this code is NOT the primary diagnostic>},
        {"code": <another code>, "reason_excluded": <string>}
      ],
      "criteria_satisfied_count": <integer 0 through 8, equal to the count of C1-C8 that are true for this response>,
      "verdict_consistency_check": <boolean: true iff verdict matches the deterministic rule "ACCEPT iff every C1-C8 is true, else REJECT", false otherwise>
    }
  ],
  "accepted_solutions": [<string>],
  "rejected_solutions": [<string>],
  "best_solution": <string or null>,
  "summary": <string>,
  "criterion_pass_rate": {
    "C1_correct_final_answer": <integer count of responses with C1 true>,
    "C2_concrete_strategy": <integer count>,
    "C3_valid_upper_bound": <integer count>,
    "C4_valid_lower_bound": <integer count>,
    "C5_worst_case_guarantee": <integer count>,
    "C6_no_invalid_one_draw_inference": <integer count>,
    "C7_no_exact_mixed_pair_requirement": <integer count>,
    "C8_no_fatal_wrong_claim": <integer count>
  },
  "verdict_distribution": {
    "ACCEPT": [<alphabetically-sorted list of response_ids whose verdict is ACCEPT>],
    "REJECT": [<alphabetically-sorted list of response_ids whose verdict is REJECT>]
  },
  "criterion_pair_co_pass_count": {
    "<Ci_name & Cj_name for each of the 28 ordered i<j pairs>": <integer count of responses with both criteria true>
  },
  "response_pair_criterion_agreement": {
    "<response_X & response_Y for each of the 28 ordered X<Y pairs>": <integer count, 0-8, of criteria where both responses have the same boolean value>
  },
  "consistency_table": {
    "NONE": [<list of response_ids whose primary_failure_code is NONE>],
    "WRONG_FINAL_NUMBER": [<list of response_ids whose primary_failure_code is WRONG_FINAL_NUMBER>],
    "CONTRADICTORY_FINAL_ANSWER": [<list>],
    "NO_CONCRETE_STRATEGY": [<list>],
    "INVALID_UPPER_BOUND": [<list>],
    "MISSING_LOWER_BOUND": [<list>],
    "NOT_WORST_CASE": [<list>],
    "INVALID_ONE_DRAW_INFERENCE": [<list>],
    "UNNECESSARY_MIXED_PAIR_REQUIREMENT": [<list>],
    "FATAL_WRONG_CLAIM": [<list>]
  },
  "cross_response_observations": <string, at least 300 characters, identifying shared defect patterns across responses>
}

Include exactly one evaluation object for each of response_A through response_H.

### Required output-field details (all fields below are MANDATORY)

The verifier scores fields beyond the basic C1-C8/verdict/primary_failure_code labels. Producing complete and well-formed values for every required field is essential. The following details apply to all eight evaluation objects and to the two top-level synthesis fields:

- `criterion_evidence` is a JSON object whose eight keys EXACTLY match the eight criteria names. Each value must be a string of at least 20 characters that either cites a short phrase from the response text or paraphrases the response's specific reasoning that justifies the corresponding boolean. Generic boilerplate (such as "the criterion is not met") that does not refer to the response's actual content is insufficient.
- `primary_failure_code_evidence` is a string of at least 50 characters that names the controlling diagnostic defect in plain language. It should reference response-specific text or reasoning rather than restating the criterion definition. It must explain why this code (and not another) is the load-bearing diagnostic.
- `alternative_codes_considered` is a JSON array of at least 2 objects. Each object must have a `code` field naming one of the controlled-vocabulary primary failure codes (drawn from {NONE, WRONG_FINAL_NUMBER, CONTRADICTORY_FINAL_ANSWER, NO_CONCRETE_STRATEGY, INVALID_UPPER_BOUND, MISSING_LOWER_BOUND, NOT_WORST_CASE, INVALID_ONE_DRAW_INFERENCE, UNNECESSARY_MIXED_PAIR_REQUIREMENT, FATAL_WRONG_CLAIM}) other than the selected primary, and a `reason_excluded` field with a brief textual justification. The point of this field is to demonstrate that the auditor considered alternative diagnostic codes and chose the most appropriate one.
- `consistency_table` is a JSON object whose ten keys are exactly the ten primary failure codes from the controlled vocabulary (NONE through FATAL_WRONG_CLAIM). Each value is an alphabetically-sorted JSON list of the response_ids whose `primary_failure_code` matches that code. Every response_id in `evaluations` must appear in exactly one of the ten lists, and the union of all ten lists must equal {response_A, response_B, response_C, response_D, response_E, response_F, response_G, response_H}. Codes with no matching response have an empty list. The verifier compares this object against the oracle's `consistency_table` per-key; mismatches penalize the score.
- `cross_response_observations` is a single string of at least 300 characters describing shared defect patterns across the eight responses. It should identify which responses share which failure mechanisms (for example, which responses rely on elimination assertions, which exhibit oscillation, which rest on invalid single-draw inferences). It is not scored for content accuracy, only for presence and minimum length, but a well-grounded synthesis is expected.

The verifier scoring rule above (with weights for C1-C8, verdict, and primary_failure_code) is supplemented by additional weights for the fields described in this section. The total scored weight per response is therefore higher than the sum of C1-C8 + verdict + primary_failure_code weights; the additional weight comes from per-criterion evidence presence (5 points per criterion), primary_failure_code_evidence presence (8 points), and alternative_codes_considered well-formedness (8 points). At the report level, consistency_table contributes 70 points per key (exact match against oracle) and cross_response_observations contributes 30 points (presence + minimum length).
