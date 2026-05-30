# Oracle justification

## Valid n in [4, 30]

n is "valid" (has ≥3 proper divisors) iff n is not 1, not prime, not p². The integers in [4, 30] that are excluded are: {4, 9, 25} (prime squares) and the primes {5, 7, 11, 13, 17, 19, 23, 29}. So valid n are:

{6, 8, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 26, 27, 28, 30} — 16 values total.

## s(n) table

| n | proper divisors | three largest | s(n) | s vs n |
|---|------------------|----------------|------|--------|
| 6 | 1,2,3 | 1,2,3 | 6 | = |
| 8 | 1,2,4 | 1,2,4 | 7 | < |
| 10 | 1,2,5 | 1,2,5 | 8 | < |
| 12 | 1,2,3,4,6 | 3,4,6 | 13 | > |
| 14 | 1,2,7 | 1,2,7 | 10 | < |
| 15 | 1,3,5 | 1,3,5 | 9 | < |
| 16 | 1,2,4,8 | 2,4,8 | 14 | < |
| 18 | 1,2,3,6,9 | 3,6,9 | 18 | = |
| 20 | 1,2,4,5,10 | 4,5,10 | 19 | < |
| 21 | 1,3,7 | 1,3,7 | 11 | < |
| 22 | 1,2,11 | 1,2,11 | 14 | < |
| 24 | 1,2,3,4,6,8,12 | 6,8,12 | 26 | > |
| 26 | 1,2,13 | 1,2,13 | 16 | < |
| 27 | 1,3,9 | 1,3,9 | 13 | < |
| 28 | 1,2,4,7,14 | 4,7,14 | 25 | < |
| 30 | 1,2,3,5,6,10,15 | 6,10,15 | 31 | > |

Counts: equal 2, greater 3, less 11. Sum 16 ✓.

**fixed_point_count = 2** (n = 6, n = 18).

s(24) = 26.

## Audit assignments (see oracle.json for the final per_response_assessment)

- A: lists 6 itself among proper divisors of 6 → F1; final 0 wrong.
- B: clean enumeration, 2.
- C: "12 has 4 proper divisors" (5 is correct) → F2; "fixed_point_count = 1" claiming only n=6 → F3; final 1 wrong.
- D: "n=6 is the only fixed point" → F3; final 1 wrong.
- E: "6+4+3 = 14" but correct sum is 13 → F4; final 2 correct.
- F: clean, 2.
- G: lists "no fixed points besides n = 6" → F3; final 1 wrong.
- H: "9+6+3 = 17" → F4; "only n=6" → F3; final 1 wrong.
- I: includes n in proper divisors for 8, 6, 12 → F1; final 0 wrong.
- J: "18 has 4 proper divisors" → F2; final 2 correct.
- K: clean enumeration, 2.
- L: lists 6 itself among proper divisors of 6 → F1; "n = 6 is the only fixed point" → F3; final 1 wrong.
- M: "12 has 4 proper divisors" (5 is correct) → F2; 9+6+3 = 17 (correct is 18) → F4; "only n = 6" → F3; final 1 wrong.
- N: lists 18 itself among proper divisors of 18 → F1; "the only fixed point in [4, 30] is 6" → F3; final 1 wrong.

acceptable_solution_ids = {B, F, K}.
