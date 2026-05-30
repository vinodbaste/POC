You are a game-theory quality-control reviewer auditing four candidate model-written analyses from a reasoning evaluation batch. The case is a finite voting game that requires backward induction, strict-majority voting, and careful treatment of a two-player stalemate rule.

Working directory: `/workspace`.

The input files are candidate analyses collected for a reasoning-quality audit. Your role is to produce the adjudication record used by the evaluation team.

Input artifacts:
- Problem statement: `/input_artifacts/problem.md`
- Proposed solution files:
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`
  - `/input_artifacts/proposed_solutions/response_G.md`

Task:
1. Read the problem statement and the four proposed solutions D, E, F, and G.
2. Determine the voting-game result by backward induction.
3. Determine the correct seniority order.
4. Determine the final accepted allocation in stacks of $10,000.
5. Determine which proposed response(s), if any, correctly solve the problem.
6. Audit every proposed response D, E, F, and G using the labels defined below.
7. Produce the requested adjudication record using the correct game-theoretic reasoning.

Core rules that must be applied:
- There are 200 stacks total.
- Strict majority means more than half of the current voters. Therefore the required yes-vote counts are 4 of 6, 3 of 5, 3 of 4, and 2 of 3.
- If two people remain, rejection does not eliminate the proposer. The two-player case repeats unless both agree. Under rational bargaining with equal mutual veto power, this means the two-player continuation value is an equal split of 100 stacks and 100 stacks.
- For any proposal with three or more people, voters compare the current proposal against the continuation value they would receive if the proposer were eliminated.
- A response is fully correct only if it gives the correct seniority order, applies the two-player stalemate rule, applies strict-majority thresholds, uses continuation-value comparisons, and gives the exact final accepted allocation.

Label definitions for each proposed response:
- `response_id`: the response letter, one of `"D"`, `"E"`, `"F"`, `"G"`.
- `extracted_final_allocation`: the final allocation claimed by that response, extracted from the response's own final answer. Use a list of objects of the form `{"name": "<name>", "stacks": <int>}` if the response gives an identifiable final allocation. Use `null` only if no identifiable final allocation exists.
- `final_answer_correct`: `true` exactly when the response's final claimed allocation is exactly the correct six-person allocation in senior-to-junior order; otherwise `false`.
- `seniority_order_correct`: `true` exactly when the response identifies the seniority order as Richard, Charles, Jessica, Darren, Adam, Christopher. Otherwise `false`.
- `uses_backward_induction`: `true` when the response works from smaller remaining-player games toward the full six-person game. Otherwise `false`.
- `respects_two_player_stalemate_rule`: `true` exactly when the response treats the two-person continuation as equal mutual-veto bargaining with continuation allocation 100/100. It is `false` if the response says one player can take all, one player can force the other to accept 1 stack, or any other non-equal two-person continuation.
- `applies_strict_majority_rule`: `true` when the response consistently uses more-than-half thresholds for the relevant group sizes: 4/6, 3/5, 3/4, and 2/3. It is `false` if the response treats a tie as passing or uses too few yes votes.
- `compares_votes_against_continuation_values`: `true` when the response evaluates whether each voter accepts by comparing the proposed amount with that voter's payoff after the current proposer is removed. It is `false` if voting is justified mainly by fairness, seniority preference, vague willingness, or an incorrect continuation-value comparison.
- `preserves_total_budget_and_stack_units`: `true` when the claimed allocation uses integer stacks of $10,000 and sums to exactly 200 stacks. It is `false` for dollar amounts mislabeled as stacks, totals not equal to 200 stacks, fractional stacks, or allocations exceeding the prize.
- `has_internal_contradiction`: `true` when the response gives mutually inconsistent final answers, contradicts its own derived allocation, or changes answer after saying a previous final answer was wrong. Otherwise `false`.
- `has_proper_requested_format`: `true` when the final answer is a single senior-to-junior list of six 2-tuples or equivalent two-element arrays `(Name, stacks)`. It is `false` if the final answer omits people, is not ordered senior-to-junior, uses dollars instead of stack counts, or does not give 2-tuples/equivalent pairs.

---
## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

{
  "correct_seniority_order": ["<name>", "<name>", "<name>", "<name>", "<name>", "<name>"],
  "correct_final_allocation": [
    {"name": "<name>", "stacks": <int>},
    {"name": "<name>", "stacks": <int>},
    {"name": "<name>", "stacks": <int>},
    {"name": "<name>", "stacks": <int>},
    {"name": "<name>", "stacks": <int>},
    {"name": "<name>", "stacks": <int>}
  ],
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "D",
      "extracted_final_allocation": [
        {"name": "<name>", "stacks": <int>},
        {"name": "<name>", "stacks": <int>}
      ],
      "final_answer_correct": <true or false>,
      "seniority_order_correct": <true or false>,
      "uses_backward_induction": <true or false>,
      "respects_two_player_stalemate_rule": <true or false>,
      "applies_strict_majority_rule": <true or false>,
      "compares_votes_against_continuation_values": <true or false>,
      "preserves_total_budget_and_stack_units": <true or false>,
      "has_internal_contradiction": <true or false>,
      "has_proper_requested_format": <true or false>
    }
  ]
}

In the actual output, include exactly four objects in `per_response_assessment`, one for each response D, E, F, G, in that order.
