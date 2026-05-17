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
- C1_correct_final_answer: 8
- C2_concrete_strategy: 1
- C3_valid_upper_bound: 12
- C4_valid_lower_bound: 12
- C5_worst_case_guarantee: 5
- C6_no_invalid_one_draw_inference: 15
- C7_no_exact_mixed_pair_requirement: 15
- C8_no_fatal_wrong_claim: 30
- verdict: 35
- primary_failure_code: 140

The final score is the total earned weighted label points divided by the total possible weighted label points across all candidate responses.

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
      "brief_justification": <string>
    }
  ],
  "accepted_solutions": [<string>],
  "rejected_solutions": [<string>],
  "best_solution": <string or null>,
  "summary": <string>
}

Include exactly one evaluation object for each of response_A through response_H.
