# Deductive Reasoning Solution Audit

You are auditing proposed solutions to a deductive reasoning puzzle. Your job is to solve the original puzzle independently from the problem statement, then evaluate whether each proposed solution gives the correct minimum and a valid proof.

  The only puzzle source is the problem statement.

## Input files

Read these files:

- /input_artifacts/problem_statement.md
- /input_artifacts/candidate_solutions/response_A.md
- /input_artifacts/candidate_solutions/response_B.md
- /input_artifacts/candidate_solutions/response_C.md
- /input_artifacts/candidate_solutions/response_D.md
- /input_artifacts/candidate_solutions/response_E.md
- /input_artifacts/candidate_solutions/response_F.md

## Required workflow

1. Solve the original puzzle yourself from /input_artifacts/problem_statement.md.
2. Determine the minimum number of inspections needed to guarantee correct relabeling in the worst case.
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
- which bag or bags to inspect;
- how many items to inspect from those bags;
- how the strategy adapts to possible observations;
- how the labels are fixed after the observations.

Set to false if the solution only gives a number, gives only a vague idea, or does not connect the proposed number to a concrete strategy.

### C3_valid_upper_bound

Set to true if and only if the solution correctly proves that its proposed number of inspections is sufficient to guarantee correct relabeling.

A valid upper-bound proof must work for every possible legal arrangement of the bags and every possible unlucky sequence of draws consistent with the bag contents.

Set to false if the proof only works in a favorable branch, depends on luck, leaves multiple labelings possible, or does not show how all four labels are fixed.

### C4_valid_lower_bound

Set to true if and only if the solution correctly proves that fewer inspections than its proposed minimum cannot guarantee success.

A valid lower-bound proof must rule out all strategies using fewer inspections, not merely show that one particular strategy can fail.

An acceptable lower-bound argument may use indistinguishable-case reasoning: construct two or more legal bag arrangements that produce the same observations under a smaller inspection budget but require different final labels.

Set to false if the solution gives no lower-bound argument, only asserts minimality, or argues only that its own strategy would need more draws.

### C5_worst_case_guarantee

Set to true if and only if the solution treats the problem as a worst-case guarantee problem.

Set to false if it relies on probability, expected outcomes, likely outcomes, lucky draws, favorable cases, or one particular sequence of observations.

### C6_no_invalid_one_draw_inference

Set to true if and only if the solution never claims that one observed item from a bag that could still be mixed proves that the bag is pure.

Allowed: one draw from a bag can prove purity only if the solution has already logically established that the bag cannot be mixed.

Not allowed: one draw from a bag labeled Chocolate, Chocolates, Mint, Mints, or Gum proves that bag is pure unless the mixed case has already been ruled out.

### C7_no_exact_mixed_pair_requirement

Set to true if and only if the solution understands that the task only requires assigning the correct label Mixed to the correct bag. The task does not require determining whether the mixed bag contains chocolate-mint, chocolate-gum, or mint-gum.

Set to false if the solution adds extra inspections solely because it thinks the exact two-type composition of the mixed bag must be identified.

It is acceptable if the strategy incidentally discovers the exact mixed pair. It is not acceptable if the solution says the exact pair is required to fix the labels.

### C8_no_fatal_wrong_claim

Set to true if and only if the solution contains no fatal logical claim that contradicts the problem or invalidates the proof.

Fatal wrong claims include:
- saying a bag known to be mislabeled with Mixed might actually be the mixed bag;
- saying the mixed bag cannot contain a type merely because the pure bag of that type has already been found;
- saying repeated draws from a bag known not to be mixed can reveal both mixed types;
- saying remaining bags are forced when two or more legal assignments remain possible;
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

Include exactly one evaluation object for each of response_A through response_F. 