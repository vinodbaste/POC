# Candidate Response G

** (33, 33, 34)**

Three perfectly rational players, each prioritizing avoiding the unique most or unique least apples (primary goal) then maximizing their own apples (secondary goal), will take amounts that split the 100 apples as evenly as possible without communication.

Since 100 / 3 = 33 remainder 1, the only distributions where no one has a unique max or unique min are those where two players get 33 and one gets 34 (all permutations). Any other split (e.g., one getting >=35 or <=32) creates a unique max or min, violating the primary goal for someone.

The first player (A) reasons backward, knowing B and C are rational. A takes 33, leaving 67.

Then B, facing 67, takes 33, leaving 34.

C takes the remaining 34.

Result: A=33, B=33, C=34. Everyone avoids unique extremum (33 ties for min, 34 is unique max but C prefers this over alternatives like taking <=33, which would make B's 33 the unique max or create worse imbalances). Among valid outcomes, they maximize: A gets 33 > 32 (if taking 32), B gets 33 > alternatives like 34 (but leaving 33 forces C=33, making B unique max - fail).[[1]](http://www.daviddfriedman.com/Academic/Price_Theory/PThy_Chapter_11/PThy_Chapter_11.html)[[2]](https://people.math.wisc.edu/~jwrobbin/141dir/propp/COMAP/Final%20IM%20with%20Full%20Solutions/p_FAPP07_ISM_15.pdf)
