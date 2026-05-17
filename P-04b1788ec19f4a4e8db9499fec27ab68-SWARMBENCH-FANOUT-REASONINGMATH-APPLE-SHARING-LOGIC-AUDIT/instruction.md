# Task: Audit Proposed Solutions to a Sequential Apple-Sharing Logic Game

You are working in `/testbed`.

Read these input files:

- `/testbed/input_artifacts/problem_statement.md`
- `/testbed/input_artifacts/candidate_solutions/response_B.md`
- `/testbed/input_artifacts/candidate_solutions/response_C.md`
- `/testbed/input_artifacts/candidate_solutions/response_D.md`
- `/testbed/input_artifacts/candidate_solutions/response_E.md`
- `/testbed/input_artifacts/candidate_solutions/response_F.md`
- `/testbed/input_artifacts/candidate_solutions/response_G.md`

Your job is to solve the original apple-sharing game and then audit each candidate response against that solution.

## Important interpretation rules

Use only the problem statement. Do not add extra rules.

- There are exactly three turns: first person, then second person, then third person.
- A player may take any integer number of apples from the bag that is available on their turn, including zero if that is optimal under the stated priorities.
- The problem does not say that all 100 apples must be taken. Apples may remain in the bag after the third turn.
- A player satisfies Goal 1 only if their own apple count is strictly between the other two final counts.
- A tie for most or least is a failure for the tied players; do not treat ties as safe.
- Preferences are lexicographic: satisfying Goal 1 is always more important than taking more apples. If a player cannot satisfy Goal 1, they maximize their own apple count.
- The correct reasoning method is backward induction from the third player's possible choices, then the second player's response, then the first player's optimal initial choice.

## Output requirements

Create exactly one file:

`/testbed/answer.json`

The JSON must be valid and must follow this schema exactly:

```json
{
  "derived_final_answer": "(A, B, C)",
  "responses": {
    "B": {
      "verdict": "correct or incorrect",
      "labels": {
        "final_answer_correct": true,
        "allows_unexhausted_apples": true,
        "third_player_choice_model_correct": true,
        "tie_rule_applied_correctly": true,
        "turn_order_applied_correctly": true,
        "avoids_positive_minimum_assumption": true,
        "player2_exception_analysis_correct": true
      },
      "error_codes": ["NONE"],
      "rationale": "One or two sentences explaining the verdict."
    }
  }
}
```

You must include entries for all six response IDs: `B`, `C`, `D`, `E`, `F`, and `G`.

## Label definitions

Use these definitions strictly.

- `final_answer_correct`: true iff the response's final ordered triple is exactly the correct ordered triple for the original game.
- `allows_unexhausted_apples`: true iff the response explicitly models that the third player may choose fewer than the remaining apples or otherwise reaches an outcome where apples can be left unallocated. False if it assumes `A+B+C=100`, says the third player must take the remainder, or only analyzes full allocations.
- `third_player_choice_model_correct`: true iff the response correctly treats the third player as choosing any available integer amount, including 0, to satisfy Goal 1 if possible and otherwise maximize their own apples. False if it forces the third player to take the entire remainder or imposes a positive minimum.
- `tie_rule_applied_correctly`: true iff the response applies the rule that any tie for most or least is a failure. False if it treats ties as avoiding most/least, or gives a tied final answer as valid.
- `turn_order_applied_correctly`: true iff the response uses exactly one turn for each of the three players in the stated order. False if it assumes a cyclic process or additional turns.
- `avoids_positive_minimum_assumption`: true iff the response does not add an unsupported rule that every player must take at least one apple. False if it asserts all players must take at least 1 apple or rejects zero for that reason.
- `player2_exception_analysis_correct`: true iff the response correctly identifies the key second-player backward-induction pivot: for first-player choices 33 and 34, the second player cannot make themselves the middle and therefore maximizes apples, which leads to first-player optimization over those cases.

## Error code definitions

Use a list of error codes for each response. Use `NONE` only for a fully correct response. Otherwise choose all applicable codes from this enum:

- `WRONG_FINAL_ANSWER`
- `FORCED_EXHAUSTION_ERROR`: assumes all 100 apples must be allocated or that the third player must take all remaining apples.
- `THIRD_PLAYER_MODEL_ERROR`: otherwise mis-models the third player's available choices.
- `TIE_RULE_ERROR`: treats ties for most or least as safe, or validates a tied final outcome.
- `CYCLIC_TURN_ORDER_ERROR`: assumes turns continue after the third player or otherwise changes the game order.
- `POSITIVE_APPLE_CONSTRAINT_ERROR`: adds an unsupported constraint that every player must take at least one apple.
- `PLAYER2_ANALYSIS_ERROR`: misses the 33/34 exception or uses an invalid second-player analysis.
- `EVEN_SPLIT_FALLACY`: assumes the answer should be an even or near-even split because the goal sounds like fairness.
- `FALSE_GOAL_VERIFICATION`: claims a final outcome satisfies the primary goal for players who are actually most, least, or tied under the prompt.

## Quality expectations

- Do not include markdown fences in `answer.json`.
- Keep rationales concise but specific.
