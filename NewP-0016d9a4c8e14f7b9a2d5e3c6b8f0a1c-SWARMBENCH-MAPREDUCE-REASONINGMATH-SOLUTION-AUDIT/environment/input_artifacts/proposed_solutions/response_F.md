I'll work through this step-by-step, using backward induction since we know the rules and can predict rational behavior.

## Setup
- Total: $2,000,000 = 200 stacks of $10,000
- Seniority (most to least senior): Richard, Charles, Jessica, Darren, Adam, Christopher
- Voting rule: Strict majority (>50%) needed to pass. If tied, proposal fails.
- Consequence: Failed proposer is eliminated with $0
- Special rule: With 2 people left, both must agree or they deadlock (repeat proposal)

## Backward Induction Analysis

**With 2 people left (Adam and Christopher):**
- They must both agree to any split
- Christopher (the junior) knows if he rejects, they deadlock and repeat forever
- Adam (the senior) can propose anything and Christopher must accept
- **Adam proposes: Adam gets all 200 stacks, Christopher gets 0**
- Result: Christopher has no bargaining power in a 2-person scenario

**With 3 people left (Darren, Adam, Christopher):**
- Darren proposes knowing what happens if rejected
- If Darren's proposal fails, it goes to 2-person scenario above
- Christopher would get 0 in that scenario, so Christopher will vote YES to any proposal giving him ≥1 stack
- Darren only needs Christopher's vote (plus his own) to pass
- **Darren proposes: Darren 200, Adam 0, Christopher 1**
- Christopher votes YES (getting 1 is better than 0)
- Darren's own vote = YES
- Result: Passes 2-1 (Darren + Christopher vs Adam)

**With 4 people left (Jessica, Darren, Adam, Christopher):**
- Jessica proposes knowing the 3-person outcome above
- Adam would get 0 in the 3-person scenario
- Adam will vote YES for any split giving him ≥1 stack
- Jessica needs one more vote (she has her own)
- **Jessica proposes: Jessica 199, Darren 0, Adam 1, Christopher 0**
- Adam votes YES (getting 1 is better than 0)
- Jessica votes YES
- Result: Passes 2-2... wait, that's a tie, which fails.

Let me reconsider: Jessica needs >50% of 4 votes = needs 3 votes (her own + 2 others)
- **Jessica proposes: Jessica 198, Darren 0, Adam 1, Christopher 1**
- Both Adam and Christopher vote YES (each gets 1 instead of 0)
- Jessica votes YES
- Result: Passes 3-1

**With 5 people left (Charles, Jessica, Darren, Adam, Christopher):**
- Charles proposes knowing the 4-person outcome
- Darren would get 0 in that scenario
- Darren will vote YES for ≥1 stack
- Charles needs >50% of 5 = needs 3 votes (his own + 2 others)
- **Charles proposes: Charles 197, Jessica 0, Darren 1, Adam 1, Christopher 1**
- Darren, Adam, and Christopher each get 1 (better than their 0, 1, 1 outcomes)
- Charles votes YES
- Result: Passes 4-1 (Charles can't just have 2 others; needs majority. Let me recalculate: Charles + Darren + one of {Adam, Christopher})
- Actually: Charles 197, Jessica 0, Darren 1, Adam 1, Christopher 1 passes with Charles, Darren, Adam, Christopher voting YES

**With 6 people (Full group - Richard proposes):**
- Richard proposes knowing the 5-person outcome
- Charles would get 0 in that scenario
- Charles will vote YES for ≥1 stack
- Richard needs >50% of 6 = needs 4 votes (his own + 3 others)
- **Richard proposes: Richard 196, Charles 1, Jessica 0, Darren 1, Adam 1, Christopher 1**
- Charles, Darren, Adam, Christopher vote YES (all better than their elimination outcomes)
- Richard votes YES
- Result: Passes 5-1

## Final Answer

```
[("Richard", 196), ("Charles", 1), ("Jessica", 0), ("Darren", 1), ("Adam", 1), ("Christopher", 1)]
```

**Reasoning Summary:** Through backward induction, each proposer at each stage can secure passage by offering just enough to the minimum coalition of junior members to make their position better than the elimination scenario they'd face if the proposal fails. Jessica, as the first to face rejection risk (with a favorable 4-person endgame), receives nothing. The senior members (Richard, Charles, Darren, Adam, Christopher) each secure 1+ stacks by being in the minimal winning coalition for their predecessor's proposals.
