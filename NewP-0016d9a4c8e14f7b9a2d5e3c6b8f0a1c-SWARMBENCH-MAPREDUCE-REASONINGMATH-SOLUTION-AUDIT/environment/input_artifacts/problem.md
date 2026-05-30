# Backward-induction voting-game audit case

A reasoning-quality team is using the following finite voting game, adapted from the classic pirates treasure-splitting problem, to audit candidate model analyses. Six participants must agree how to split a $2,000,000 award. The money is divisible only into stacks of $10,000, so there are exactly 200 stacks.

The members are Richard, Jessica, Adam, Darren, Christopher, and Charles.

Seniority is determined entirely by recruitment. If one member recruited another member, the recruiter is more senior. The recruitment history is public and is:

- Richard recruited Charles.
- Charles recruited Jessica.
- Jessica recruited Darren.
- Darren recruited Adam.
- Adam recruited Christopher.

Therefore proposals are made from most senior to most junior. On each proposal, all currently remaining members vote yes or no.

Voting and elimination rules:

1. A proposal passes only if it receives a strict majority of the current votes, meaning strictly more than half of the remaining members vote yes.
2. If a proposal passes, that split is final.
3. If a proposal fails while at least three people remain, the proposer is eliminated and receives zero stacks; then the next most senior remaining member proposes.
4. If exactly two people remain, rejection does not eliminate the proposer. Instead, the two-person bargaining repeats until both accept a proposal. For this audit, use the canonical mutual-veto interpretation: neither two-person player can force the other to accept less than half, so the two-person continuation value is an equal split of 100 stacks and 100 stacks.
5. Every member is rational, selfish, and perfectly informed. A member votes yes exactly when the proposal gives them strictly more stacks than they would receive if the current proposal failed, except in the special two-person mutual-veto case described above.
6. When a proposer has several minimum-cost winning coalitions available, use the canonical tie-breaker that buys votes from the senior-most eligible voters first.

Question: Assuming perfect backward induction under the rules above, what split is accepted, and what is the seniority order?

Required answer format for the underlying voting game: a single list of 2-tuples, ordered from senior-most to junior-most, where each tuple is:

`(Name, number_of_10000_dollar_stacks)`
