# Calibration Guide for Auditing Sequence-Envelope Puzzle Solutions

## Puzzle Summary
- 4 envelopes labeled "Strictly Increasing", "Strictly Decreasing", "Constant", "Mixed"
- All labels are WRONG
- Contents: one pure increasing, one pure decreasing, one pure constant, one mixed (7 of one type + 13 of another)
- One sequence can be inspected at a time from any envelope
- Goal: minimum inspections to GUARANTEE correct relabeling (worst-case)

## Correct Answer: 15
**Optimal strategy:**
1. Inspect "Mixed" envelope once → reveals its true pure category (since it's not mixed)
2. Now we have 3 envelopes: two pure, one mixed (7/13 split)
3. To distinguish pure from mixed, need 14 inspections of same type from one envelope (mixed maxes at 13 of any type)
4. Total: 1 + 14 = 15 inspections

---

## Audit Criteria Calibration

### C1: Correct Final Answer
**Definition:** Does the solution state the actual minimum guaranteed number (15)?

**How to assess:**
- ACCEPT if final stated answer is 15
- REJECT if answer is any other number (1, 2, 3, 4, 14, 16, etc.)
- If solution oscillates between multiple answers, use the final stated answer for C1, but flag for CONTRADICTORY_FINAL_ANSWER as primary failure

**Common wrong answers:**
- 1: Thinks seeing one sequence proves purity
- 2-4: Thinks logical deduction eliminates all uncertainty
- 14: Forgets the initial inspection of "Mixed"
- 16: Off-by-one error

---

### C2: Concrete Strategy
**Definition:** Does the solution give an explicit inspection strategy with concrete rules?

**How to assess:**
- ACCEPT if the solution describes:
  - Which envelope(s) to inspect first
  - Clear decision rules based on observations
  - Stopping criteria for inspections
- REJECT if the strategy is:
  - Vague ("deduce the rest", "determine by elimination")
  - Missing entirely (just states an answer)
  - Incomplete (no rule for when to stop inspecting)

**Examples:**
- GOOD: "Inspect 'Mixed' once, then inspect another envelope up to 14 times until either seeing two categories or 14 identical"
- BAD: "Inspect some envelopes and deduce the rest"

---

### C3: Valid Upper Bound Proof
**Definition:** Does the solution correctly prove the stated number is sufficient?

**How to assess:**
- ACCEPT if the solution explains WHY its number of inspections guarantees identification:
  - Recognizes "Mixed"-labeled envelope is pure (wrong label)
  - Recognizes 14 identical sequences prove purity (mixed maxes at 13)
  - Shows how to deduce remaining envelopes after identifying one
- REJECT if:
  - Sufficiency is merely asserted without justification
  - The reasoning leaves legal labelings uneliminated
  - Missing the 13/14 threshold logic

---

### C4: Valid Lower Bound Proof
**Definition:** Does the solution prove impossibility for fewer inspections?

**How to assess:**
- ACCEPT if the solution demonstrates that with fewer inspections, an adversary could construct a scenario where:
  - Two different labelings are both consistent with all observations
  - The true labeling cannot be uniquely determined
- REJECT if:
  - No lower bound argument is given
  - The lower bound is asserted but not proven
  - Claims fewer inspections work without addressing worst-case scenarios

**Key adversarial insight:** A mixed envelope with 13 of the observed type looks identical to a pure envelope after any number of inspections ≤ 13.

---

### C5: Worst-Case Framing
**Definition:** Does the solution treat this as a worst-case guarantee (not probability/expected value)?

**How to assess:**
- ACCEPT if:
  - Explicitly mentions "worst case", "guarantee", "adversarial"
  - Uses 14 inspections because mixed could have 13 of same type
  - Doesn't rely on "luck" or probability
- REJECT if:
  - Appeals to probability ("likely to see different types")
  - Uses expected value reasoning
  - Ignores the possibility of seeing 13 identical from mixed

---

### C6: No Invalid One-Draw Inference
**Definition:** Does it avoid claiming one draw proves purity when envelope could still be mixed?

**How to assess:**
- ACCEPT if the solution NEVER claims that:
  - Seeing one increasing sequence proves an envelope is purely increasing
  - After N ≤ 13 identical observations, the envelope "must be" pure
  - One inspection from "Strictly Increasing" proves it's mixed if result is increasing
- REJECT if the solution contains invalid inferences like:
  - "If 'Strictly Increasing' gives Increasing, it must be Mixed" (wrong - could be pure increasing)
  - "Two identical inspections prove purity" (needs 14)

**This is the most common and critical failure mode.**

---

### C7: No Unnecessary Mixed Pair Requirement
**Definition:** Does it understand we don't need to identify which exact pair is in the mixed envelope?

**How to assess:**
- ACCEPT if the solution:
  - Only aims to assign correct labels to all 4 envelopes
  - Doesn't try to determine the 7/13 split composition
  - Recognizes that knowing an envelope is "mixed" is sufficient
- REJECT if the solution:
  - Adds extra inspections to determine the 7/13 split
  - Claims we need to identify both categories in the mixed envelope
  - Requires seeing both types from the mixed envelope

---

### C8: No Fatal Wrong Claims
**Definition:** Are there no fatal logical contradictions in the reasoning?

**How to assess:**
- ACCEPT if the reasoning is internally consistent
- REJECT if there are contradictory claims like:
  - "All labels are wrong" is ignored when convenient
  - The mixed envelope is treated as both "could be anything" and "identified immediately"
  - Claiming X inspections suffice while the example requires Y > X
  - Mathematical errors (7+13≠20, wrong counting)

---

## Verdict Determination

**ACCEPT:** All criteria C1-C8 are TRUE

**REJECT:** Any of C1-C8 is FALSE

---

## Primary Failure Code Selection

When multiple failures occur, select the **most diagnostic** (earliest in this list):

### 1. CONTRADICTORY_FINAL_ANSWER
**When to use:** Solution oscillates between multiple final answers without clear resolution.

**Examples:**
- Response E: "I think 3... Wait... Actually 2... So perhaps 14... Actually I think 3... Final answer: 3"

**Priority:** Highest - shows fundamental confusion

---

### 2. WRONG_FINAL_NUMBER
**When to use:** Answer is wrong but the solution presents a single coherent (though flawed) argument.

**Examples:**
- Response A: Claims 2, reasoning is consistent but wrong
- Response D: Claims 1, reasoning is coherent but fatally wrong

**Priority:** High - shows confident wrong answer

---

### 3. NO_CONCRETE_STRATEGY
**When to use:** No explicit rules for which envelopes to inspect or when to stop.

**Examples:**
- "Deduce by elimination" with no procedure
- Missing stopping criteria for iterative inspection

**Priority:** High - makes solution unimplementable

---

### 4. INVALID_ONE_DRAW_INFERENCE
**When to use:** Claims one (or few) inspection(s) proves purity when envelope could be mixed.

**Examples:**
- Response A: "If 'Strictly Increasing' gives Increasing, it must be Mixed"
- Any claim that N ≤ 13 identical observations prove purity

**Priority:** High - fundamental misunderstanding of mixed structure

---

### 5. NOT_WORST_CASE
**When to use:** Treats as expected value or ignores adversarial possibility of 13 identical in mixed.

**Examples:**
- "Probably we'll see different types"
- Doesn't account for needing 14 to distinguish from 13-in-mixed

**Priority:** Medium-high - wrong problem framing

---

### 6. UNNECESSARY_MIXED_PAIR_REQUIREMENT
**When to use:** Adds inspections to identify the 7/13 split composition unnecessarily.

**Examples:**
- Claims we need to see both types from mixed
- Count > 15 to determine exact mixed composition

**Priority:** Medium - misunderstanding of problem requirements

---

### 7. MISSING_LOWER_BOUND
**When to use:** Strategy is complete for upper bound but no proof that fewer inspections fail.

**Examples:**
- Good upper bound argument, but no adversarial example for n-1

**Priority:** Medium - incomplete but not wrong

---

### 8. INVALID_UPPER_BOUND
**When to use:** Upper bound proof leaves legal labelings uneliminated.

**Examples:**
- Claims sufficiency with reasoning that doesn't cover all cases
- Strategy doesn't actually guarantee correct relabeling

**Priority:** Medium - incomplete sufficiency

---

### 9. FATAL_WRONG_CLAIM
**When to use:** Any proof-invalidating contradiction not covered above.

**Examples:**
- Claims "all labels wrong" then treats label as informative in a contradictory way
- Mathematical counting errors affecting proof validity

**Priority:** Catch-all for other fatal errors

---

## Application Examples

| Response | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Verdict | Primary Failure Code |
|----------|----|----|----|----|----|----|----|----|---------|---------------------|
| A (claims 2) | F | T | F | F | F | F | T | F | REJECT | INVALID_ONE_DRAW_INFERENCE |
| B (claims 4) | F | T | F | F | F | F | T | T | REJECT | INVALID_ONE_DRAW_INFERENCE |
| C (claims 15) | T | T | T | T | T | T | T | T | ACCEPT | N/A |
| D (claims 1) | F | T | F | F | F | F | T | F | REJECT | INVALID_ONE_DRAW_INFERENCE |
| E (oscillates) | F | F | F | F | F | F | T | F | REJECT | CONTRADICTORY_FINAL_ANSWER |
| F (claims 3) | F | T | F | F | F | F | T | T | REJECT | INVALID_ONE_DRAW_INFERENCE |
| G (claims 16) | F | T | T | T | T | T | T | T | REJECT | WRONG_FINAL_NUMBER |
| H (claims 4) | F | T | F | F | F | F | T | T | REJECT | INVALID_ONE_DRAW_INFERENCE |

---

## Summary Decision Tree

1. **Does the solution oscillate between multiple final answers?** → CONTRADICTORY_FINAL_ANSWER
2. **Is the final answer wrong (and not oscillating)?** → Note as WRONG_FINAL_NUMBER
3. **Is there no concrete inspection strategy?** → NO_CONCRETE_STRATEGY
4. **Does it claim one/a few inspections prove purity when mixed is possible?** → INVALID_ONE_DRAW_INFERENCE
5. **Is it not framed as worst-case?** → NOT_WORST_CASE
6. **Does it unnecessarily try to identify mixed pair composition?** → UNNECESSARY_MIXED_PAIR_REQUIREMENT
7. **Is lower bound proof missing?** → MISSING_LOWER_BOUND
8. **Is upper bound proof invalid?** → INVALID_UPPER_BOUND
9. **Other fatal contradiction?** → FATAL_WRONG_CLAIM
