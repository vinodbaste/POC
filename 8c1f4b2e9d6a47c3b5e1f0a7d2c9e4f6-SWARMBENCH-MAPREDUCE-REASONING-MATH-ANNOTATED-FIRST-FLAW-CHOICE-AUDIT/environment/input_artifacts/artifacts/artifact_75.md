# artifact_75

Competition: IMOSL  
Problem ID: IMOSL_2018_4  
Year: 2018

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

A site is any point \((x, y)\) in the plane such that \(x\) and \(y\) are both positive integers less than or equal to \(20\). Initially, each of the \(400\) sites is unoccupied. Amy and Ben take turns placing stones, with Amy going first. On her turn, Amy places a new red stone on an unoccupied site such that the distance between any two sites occupied by red stones is not equal to \(\sqrt{5}\). On his turn, Ben places a new blue stone on any unoccupied site. The game ends when a player cannot place a stone. Determine the greatest \(K\) such that Amy can ensure that she places at least \(K\) red stones, no matter how Ben plays.

## Candidate Excerpts

### Option A

```text
Step 3.  Wait — within class (0,0), are all pairs non-knight-related?  A knight move
changes parity in both coordinates, so within (0,0) (both coordinates even), a knight
move would go to (odd, odd) = class (1,1).  So no knight moves stay within (0,0).
Within (0,0), there are no edges of the knight graph.  Hence (0,0) is a 100-element
independent set in the knight graph.  By Mantel's theorem applied to the bipartite knight
graph, the maximum independent set has size at least 200.  So Amy can place at least
200/2 = 100 stones if she plays optimally against Ben's interference.
```

### Option B

```text
Step 4.  Specifically, Amy's strategy: she plays in class (0,0) first, claiming as many
sites as possible.  Ben can block at most one site per Amy move (since Ben plays one stone
per turn).  In the worst case Ben blocks sites in (0,0), reducing Amy's available targets.
But there are 100 sites in (0,0), and Ben gets at most 100 moves (alternating with Amy's
100), so by parity Amy gets at least 50 sites in (0,0).
But by symmetry, Amy can play 50 in (0,0) and continue in (1,1), getting another 50,
for a total of 100.  Hence K ≥ 100.

For the upper bound, one shows by a strategy-stealing argument that Ben can prevent
Amy from placing more than 100, giving K = 100.
```

### Option C

```text
Step 1.  Two sites (x_1, y_1) and (x_2, y_2) are at distance √5 iff (x_1-x_2)^2 +
(y_1-y_2)^2 = 5, i.e., {|x_1-x_2|, |y_1-y_2|} = {1, 2}.  So a "forbidden distance" is a
knight's move on the 20×20 grid.

By Mantel-like coloring, partition the 400 sites into "color classes" based on coordinate
parity.  Define color c(x, y) = (x mod 2, y mod 2) ∈ {0, 1}^2 — 4 color classes.  Knight
moves change x by ±1 or ±2 and y by ±2 or ±1, so knight moves change the parity in both
coordinates: c changes from (a, b) to (a+1, b+1) (mod 2).  Hence knight-neighbors have
opposite parity in BOTH coordinates.
```

### Option D

```text
Step 2.  Therefore the 4 color classes split into two pairs: {(0,0), (1,1)} and
{(0,1), (1,0)} — sites with the same coordinate-parity-XOR.  Knight moves only connect
sites across the two pairs.  Hence within each pair, the sites form an independent set
(no knight-neighbors within).

The class (0,0) has 10·10 = 100 sites (since x, y even with 1 ≤ x, y ≤ 20).  Similarly
(1,1) has 100 sites.  Together {(0,0), (1,1)} = 200 sites, all pairwise non-knight-related.
Similarly {(0,1), (1,0)} has 200 sites.
```

## Full Candidate Proof

```text
Step 1.  Two sites (x_1, y_1) and (x_2, y_2) are at distance √5 iff (x_1-x_2)^2 +
(y_1-y_2)^2 = 5, i.e., {|x_1-x_2|, |y_1-y_2|} = {1, 2}.  So a "forbidden distance" is a
knight's move on the 20×20 grid.

By Mantel-like coloring, partition the 400 sites into "color classes" based on coordinate
parity.  Define color c(x, y) = (x mod 2, y mod 2) ∈ {0, 1}^2 — 4 color classes.  Knight
moves change x by ±1 or ±2 and y by ±2 or ±1, so knight moves change the parity in both
coordinates: c changes from (a, b) to (a+1, b+1) (mod 2).  Hence knight-neighbors have
opposite parity in BOTH coordinates.

Step 2.  Therefore the 4 color classes split into two pairs: {(0,0), (1,1)} and
{(0,1), (1,0)} — sites with the same coordinate-parity-XOR.  Knight moves only connect
sites across the two pairs.  Hence within each pair, the sites form an independent set
(no knight-neighbors within).

The class (0,0) has 10·10 = 100 sites (since x, y even with 1 ≤ x, y ≤ 20).  Similarly
(1,1) has 100 sites.  Together {(0,0), (1,1)} = 200 sites, all pairwise non-knight-related.
Similarly {(0,1), (1,0)} has 200 sites.

Step 3.  Wait — within class (0,0), are all pairs non-knight-related?  A knight move
changes parity in both coordinates, so within (0,0) (both coordinates even), a knight
move would go to (odd, odd) = class (1,1).  So no knight moves stay within (0,0).
Within (0,0), there are no edges of the knight graph.  Hence (0,0) is a 100-element
independent set in the knight graph.  By Mantel's theorem applied to the bipartite knight
graph, the maximum independent set has size at least 200.  So Amy can place at least
200/2 = 100 stones if she plays optimally against Ben's interference.

Step 4.  Specifically, Amy's strategy: she plays in class (0,0) first, claiming as many
sites as possible.  Ben can block at most one site per Amy move (since Ben plays one stone
per turn).  In the worst case Ben blocks sites in (0,0), reducing Amy's available targets.
But there are 100 sites in (0,0), and Ben gets at most 100 moves (alternating with Amy's
100), so by parity Amy gets at least 50 sites in (0,0).
But by symmetry, Amy can play 50 in (0,0) and continue in (1,1), getting another 50,
for a total of 100.  Hence K ≥ 100.

For the upper bound, one shows by a strategy-stealing argument that Ben can prevent
Amy from placing more than 100, giving K = 100.
```

## Reviewer Note

In Step 1, the claim that a knight move changes parity in BOTH coordinates is wrong as stated: a knight move changes x by ±1 or ±2, and y by ±2 or ±1, with |dx| + |dy| = 3 — specifically, one coordinate changes by 1 (odd, so parity flips) and the other changes by 2 (even, so parity STAYS). Hence a knight move flips parity in EXACTLY ONE coordinate, not both. This means class (0,0) connects to (1,0) and (0,1), not to (1,1). The Mantel-coloring argument's bipartition is therefore wrong, and the whole structural claim about "200 sites with no knight relations within each pair" is misapplied.
