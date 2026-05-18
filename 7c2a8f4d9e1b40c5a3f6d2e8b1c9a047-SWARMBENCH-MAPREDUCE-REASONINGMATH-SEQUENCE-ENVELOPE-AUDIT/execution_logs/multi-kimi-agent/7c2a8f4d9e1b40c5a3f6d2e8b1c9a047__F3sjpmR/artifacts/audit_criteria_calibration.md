# Audit Criteria Calibration Packet

## Canonical Answer (to be derived independently)
- The canonical minimum number of inspections is **20** (to be verified through independent derivation)
- This will be provided by the `derive-canonical-envelope-proof` sub-agent

---

## C1_correct_final_answer

**Definition:** Set to true if and only if the solution states the actual minimum guaranteed number of inspections for the puzzle.

**Set to FALSE if:**
- The solution gives a different number
- The solution gives multiple conflicting final answers
- The solution does not state a final minimum

---

## C2_concrete_strategy

**Definition:** Set to true if and only if the solution gives an explicit inspection strategy, not just a final number.

**Required elements for TRUE:**
- Which envelope or envelopes to inspect
- How many sequences to inspect from those envelopes
- How the strategy adapts to possible observations
- How the labels are fixed after the observations

**Set to FALSE if:**
- The solution only gives a number
- The solution gives only a vague idea
- The solution does not connect the proposed number to a concrete strategy

**Phrase-pattern rule:** C2 is TRUE only when the response specifies a multi-branch plan: which envelopes are inspected, how many items are drawn from each, what each observation implies, and how each branch fixes all four labels. 

A single-inspection plan followed by a sentence like "forced by contradiction" or "the remaining are determined" is NOT a concrete strategy and C2 should be FALSE.

C2 should also be FALSE when:
- The response oscillates among multiple incompatible inspection counts (e.g., proposes 2, then 3, then 14, then a final 3) without committing to one coherent plan
- The response acknowledges single-draw ambiguity (e.g., "this envelope is either mixed or purely X") and then concludes "enough information has been gathered" without specifying the branch-by-branch label-fixing rule

---

## C3_valid_upper_bound

**Definition:** Set to true if and only if the solution correctly proves that its proposed number of inspections is sufficient to guarantee correct relabeling.

**Required for TRUE:**
- A valid upper-bound proof must work for every possible legal arrangement of the envelopes
- Must handle every possible unlucky sequence of draws consistent with the envelope contents
- Must include the 7/13 split in the mixed envelope

**Set to FALSE if:**
- The proof only works in a favorable branch
- The proof depends on luck
- The proof leaves multiple labelings possible
- The proof does not show how all four labels are fixed

---

## C4_valid_lower_bound

**Definition:** Set to true if and only if the solution correctly proves that fewer inspections than its proposed minimum cannot guarantee success.

**Required for TRUE:**
- A valid lower-bound proof must rule out all strategies using fewer inspections
- Not merely show that one particular strategy can fail
- Acceptable: indistinguishable-case reasoning - construct two or more legal envelope arrangements that produce the same observations under a smaller inspection budget but require different final labels

**Set to FALSE if:**
- The solution gives no lower-bound argument
- The solution only asserts minimality
- The solution argues only that its own strategy would need more draws

**Phrase-pattern rule:** C4 is TRUE only when the response constructs an indistinguishable-case argument exhibiting two legal envelope arrangements that produce identical observations under a strictly smaller inspection budget. 

Arithmetic derivation of the count from the response's own strategy does not satisfy C4 even when the count and strategy are correct.

---

## C5_worst_case_guarantee

**Definition:** Set to true if and only if the solution treats the problem as a worst-case guarantee problem.

**Set to FALSE if:**
- The solution relies on probability
- The solution uses expected outcomes
- The solution uses likely outcomes
- The solution depends on lucky draws
- The solution depends on favorable cases
- The solution depends on one particular sequence of observations

---

## C6_no_invalid_one_draw_inference

**Definition:** Set to true if and only if the solution never claims that one observed sequence from an envelope that could still be mixed proves that the envelope is pure.

**Allowed (TRUE scenarios):**
- One draw from an envelope can prove purity only if the solution has already logically established that the envelope cannot be mixed
- The Mixed-labeled envelope is one such case, since its label is wrong; one draw from it does prove its pure type

**Not allowed (FALSE triggers):**
- One draw from an envelope labeled "Strictly Increasing", "Strictly Decreasing", or "Constant" proves that envelope is pure unless the mixed case has already been ruled out for that envelope

**C6 does NOT fire false when:**
- The single-draw observation is from the Mixed-labeled envelope (that label is known wrong, so the inference is valid)
- The response acknowledges single-draw ambiguity (such as "this envelope is either mixed or purely increasing") without collapsing it to a purity claim
- The response's strategy is merely insufficient without an explicit single-draw purity claim

---

## C7_no_exact_mixed_pair_requirement

**Definition:** Set to true if and only if the solution understands that the task only requires assigning the correct label "Mixed" to the correct envelope. The task does not require determining whether the mixed envelope contains increasing-decreasing, increasing-constant, or decreasing-constant sequences.

**Set to FALSE if:**
- The solution adds extra inspections solely because it thinks the exact two-type composition of the mixed envelope must be identified

**Acceptable:**
- It is acceptable if the strategy incidentally discovers the exact mixed pair

**Not acceptable:**
- It is not acceptable if the solution says the exact pair is required to fix the labels

---

## C8_no_fatal_wrong_claim

**Definition:** Set to true if and only if the solution contains no fatal logical claim that contradicts the problem or invalidates the proof.

**Fatal wrong claims include:**
- Saying an envelope known to be mislabeled with "Mixed" might actually be the mixed envelope
- Treating any of the pure-labeled envelopes as if its label were correct
- Saying remaining envelopes are forced when two or more legal assignments remain possible
- Confusing a possible success path with a guaranteed strategy
- Treating a probability argument as a guarantee

**C8 is TRUE by default.** It becomes FALSE when the response asserts a proof-invalidating claim.

**Triggering phrase patterns (C8=FALSE):**
- "determined automatically by elimination" after too-few observations
- "the remaining are forced by contradiction"
- "the remaining labels cycle uniquely"
- "enough information has been gathered to deduce the final arrangement uniquely" after acknowledged ambiguity
- "the assignment follows directly" from single observations

Any of these patterns triggers C8=FALSE even when WRONG_FINAL_NUMBER or another code is the best primary_failure_code for the response. C8 FALSE is INDEPENDENT of C3 and of the primary_failure_code.

---

## Verdict Rule

**Deterministic rule:**
- **ACCEPT** if and only if all criteria C1 through C8 are true
- **REJECT** otherwise

A solution with the correct final answer but invalid reasoning must be rejected.

---

## Primary Failure Code Selection Rules

**Available codes:**
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

**Use NONE only for accepted solutions.**

### Priority Order (disambiguation order):

1. **CONTRADICTORY_FINAL_ANSWER** - If the response oscillates among incompatible final counts and never settles, prefer this over WRONG_FINAL_NUMBER

2. **NO_CONCRETE_STRATEGY** - If the strategy is missing concrete branch-by-branch label-fixing rules, prefer this over downstream defects that follow from the missing strategy

3. **INVALID_ONE_DRAW_INFERENCE** - If a load-bearing one-draw purity inference from a possibly-mixed envelope drives the proposed minimum, prefer this over NOT_WORST_CASE. Do NOT pick this code when the only single-draw observation present is from the Mixed-labeled envelope

4. **NOT_WORST_CASE** - If the response acknowledges worst-case framing for one envelope but abandons it for others

5. **UNNECESSARY_MIXED_PAIR_REQUIREMENT** - If the response adds extra inspections to determine the exact two-type composition of the mixed envelope

6. **MISSING_LOWER_BOUND** - If the strategy is structurally complete and the upper bound holds but the lower bound is only asserted from the strategy's arithmetic

7. **INVALID_UPPER_BOUND** - If the upper-bound argument leaves multiple legal labelings open in some worst-case branch

8. **FATAL_WRONG_CLAIM** - If the load-bearing defect is a proof-invalidating "forced" or "cycle uniquely" assertion not consistent with multiple legal labelings remaining open

9. **WRONG_FINAL_NUMBER** - Only when the strategy is structurally correct in every other way but the inspection count deviates from the optimum, typically due to a preliminary inspection that could have been absorbed into the verification phase

**Important:**
- Do NOT default to WRONG_FINAL_NUMBER simply because C1 is FALSE
- Do NOT default to INVALID_ONE_DRAW_INFERENCE simply because a single-draw observation appears or the strategy is insufficient
- Pick the most diagnostic code that describes the load-bearing defect

---

## Universal Phrase-Pattern Rules Summary

### C2 (concrete strategy)
- TRUE: Multi-branch plan with specific envelope selection, draw counts, observation implications, and label-fixing rules
- FALSE: "forced by contradiction", "the remaining are determined", oscillating counts without coherent plan, acknowledged ambiguity without branch specification

### C4 (valid lower bound)
- TRUE: Indistinguishable-case argument with two legal arrangements producing identical observations under smaller budget
- FALSE: Arithmetic derivation from own strategy (even if count is correct)

### C6 (no invalid one-draw inference)
- TRUE by default
- FALSE: Explicit single-draw purity claim from possibly-mixed envelope
- NOT FALSE for: Mixed-labeled envelope observations, acknowledged ambiguity without purity claim, merely insufficient strategy

### C8 (no fatal wrong claim)
- TRUE by default
- FALSE: "determined automatically by elimination", "forced by contradiction", "labels cycle uniquely", "enough information has been gathered" after ambiguity, "follows directly" from single observations
- INDEPENDENT of C3 and primary_failure_code
