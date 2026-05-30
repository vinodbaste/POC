The seniority/proposal order is fixed by the recruitment chain: Richard (most senior) → Charles → Jessica → Darren → Adam → Christopher (most junior).

All players are perfectly rational, know everyone else is too, and will therefore reject any proposal that leaves them with strictly less than they could guarantee by forcing the process forward (including the subgame that would arise after eliminating the current proposer). They accept any proposal that gives them at least as much as that continuation value. Stacks are indivisible, so the minimal positive offer is 1 stack. We solve by backward induction.

**2-player subgame** (any two remaining, senior proposes)  
The senior offers (200, 0). The junior must accept: rejection merely repeats the identical game forever, yielding 0 for both. Hence the outcome is (200 for senior, 0 for junior).

**3-player subgame** (any three remaining, senior proposes)  
The proposer needs a strict majority (2 yes votes) and already has his own vote, so he needs exactly one additional yes. He offers 1 stack to the most junior of the three and 0 to the middle player. The junior accepts (1 > 0 from the 2-player continuation). The middle player is indifferent or worse off by rejecting, so the proposal passes. Result: (199, 0, 1) ordered senior-to-junior.

**4-player subgame**  
Needs 3 yes votes; proposer already supplies one, so must buy exactly two more. He offers 1 stack each to the two most junior players and 0 to the remaining one. Both recipients accept (1 > 0 from the 3-player continuation). Result: (198, 0, 0, 2).

**5-player subgame**  
Needs 3 yes votes total; proposer supplies one, so must buy two more. He offers 1 stack each to the two most junior players. Result: (197, 0, 1, 0, 2).

**6-player game (full crew)**  
Richard needs 4 yes votes total; he already supplies one, so must buy exactly three more. He therefore offers the three cheapest “bribes” that the continuation values dictate: 1 stack each to Jessica and Darren, and 2 stacks to Christopher (the amounts they would receive in the 5-player subgame). Everyone else gets 0.  
- Jessica, Darren and Christopher each receive strictly more than their 5-player continuation values, so they vote yes.  
- Charles and Adam receive 0, the same as (or worse than) their continuation values, but cannot form a blocking majority.  
Richard’s proposal therefore passes on the first round.  

The unique subgame-perfect equilibrium split, ordered from senior-most to junior-most, is therefore:

(Richard, 196), (Charles, 0), (Jessica, 1), (Darren, 1), (Adam, 0), (Christopher, 2)
