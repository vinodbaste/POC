# Review Rubric

You are validating multiple-choice conversions of LLM reasoning errors from the ProcessBench dataset.

For each artifact:
- Read the problem and the full solution.
- Inspect the four candidate steps in proof order.
- Exactly one option contains the first step where the solution makes an unrecoverable error.
- Return only the chosen option letter for each artifact.
- Do not invent new options or rewrite the step text.

The reducer must also compute exact aggregate counts for each option letter, competition, and year.
