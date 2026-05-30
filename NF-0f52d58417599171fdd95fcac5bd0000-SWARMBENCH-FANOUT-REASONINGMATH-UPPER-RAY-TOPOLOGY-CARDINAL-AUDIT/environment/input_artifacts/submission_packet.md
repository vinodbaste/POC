# Referee Packet for the Upper-Ray Cardinal Question

## Statement of the question

Equip R with the topology tau whose basic open sets are the upper rays U_a := {t in R : a < t} for a in R. Call a subset S subseteq R "distinguished" provided that the number of omega-accumulation points of S in R is strictly smaller than the number of limit points of S in R.

Working under the assumption 2^omega = omega_3, let W be the set of cardinals kappa for which there exists a distinguished S subseteq R of cardinality kappa.

Determine the cardinality of the collection of infinite cardinals strictly below sup(W).

---

## Submission A

(i) Suppose S subseteq R is non-empty and finite. Let M = max S. For every a < M, the upper ray U_a = (a, infinity) contains M, and M is distinct from a, so M witnesses that a is a limit point of S. Since |S| < omega, no point can have infinitely many points of S sitting above any cutoff, so S has no omega-accumulation points at all. We conclude that the limit-point set of S has cardinality 2^omega = omega_3 while the omega-accumulation-point set has cardinality 0; therefore S is distinguished.

(ii) Take S = {0, -1, -2, ...} subseteq R, the non-positive integers. As in step (i), every a < 0 is a limit point of S. Furthermore, |U_a cap S| < omega for every a in R, since the non-positive integers above any cutoff form a finite tail. So S has no omega-accumulation points. Hence S is distinguished and |S| = omega.

(iii) Now assume |S| >= omega_1. Write R as the countable union R = union_{n in N} [-n, n]. Since |S| >= omega_1 and the cofinality of omega_1 is uncountable, the equation S = union_n (S cap [-n, n]) forces some N in omega with |S cap [-N, N]| >= omega_1.

Then for every a <= -N, U_a = (a, infinity) captures all of S cap [-N, N], which has at least omega_1 >= omega points, so a is an omega-accumulation point of S. The set of such a has cardinality 2^omega = omega_3, which is the size of the continuum. So already the omega-accumulation-point set is as large as possible; S cannot be distinguished.

(iv) Combining (i)-(iii): every non-empty finite S is distinguished, S = {0, -1, -2, ...} is a distinguished S of cardinality omega, and no S of cardinality at least omega_1 is distinguished. So W = ({1, 2, 3, ...}) union {omega} and sup(W) = omega.

(v) The infinite cardinals strictly below omega form the empty set. Hence the answer is |emptyset| = 0.

---

## Submission B

The space (R, tau) has basic open sets U_a = (a, infinity). A point z is a limit point of S iff every U_a with a < z meets S in a point distinct from z. A point y is an omega-accumulation point of S iff every U_a with a < y meets S in infinitely many points.

Try to push the cardinality of a distinguished S as high as possible. Let T subseteq R with |T| = omega_2. For each t in T choose a sequence v_{t,k} (k in omega) approaching t from above. For each c in R \ T choose one auxiliary point w_c > c. Set
S = {v_{t,k} : t in T, k in omega} union {w_c : c in R \ T}.

Then every real is a limit point of S. The omega-accumulation points are exactly the points of T, because only those have countably many points clustering above them. Therefore the limit-point set has cardinality omega_3 and the omega-accumulation-point set has cardinality omega_2. Thus S is distinguished and |S| = omega_3.

We deduce omega_3 in W, hence sup(W) = omega_3. The infinite cardinals strictly below omega_3 are omega, omega_1, and omega_2. Hence the answer is 3.

---

## Submission C

Write L(S) for the set of limit points of S and A(S) for the set of omega-accumulation points of S.

A real x is a limit point of S iff every open set containing x also contains a point of S different from x. The open sets containing x are the rays (a, infinity) with a < x, so:
  x in L(S) <=> for all a < x, (a, infinity) cap (S \ {x}) is non-empty.

A real y is an omega-accumulation point iff every open set containing y contains infinitely many points of S:
  y in A(S) <=> for all a < y, |(a, infinity) cap S| >= aleph_0.

If S is finite, L(S) = emptyset and A(S) = emptyset. Then the strict inequality 0 < 0 fails, so S is not distinguished. So S must be infinite to be a candidate.

For infinite S, |L(S)| = 2^aleph_0. Furthermore A(S) is an initial segment of R, and if A(S) is non-empty its cardinality is also 2^aleph_0. So distinguishedness forces A(S) = emptyset.

An infinite S with A(S) = emptyset is exactly a set that is unbounded below, bounded above, and countable. Example: S = {..., -3, -2, -1} has no omega-accumulation points yet has continuum-many limit points.

Therefore W = {aleph_0}. So sup(W) = aleph_0. There are no infinite cardinals strictly below aleph_0, so the answer is 0.

---

## Submission D

Final answer: 3.

In this topology the basic open sets are U_a = {t in R : a < t}. A point z is a limit point of S iff for every a < z there is x in S \ {z} with x > a. A point y is an omega-accumulation point of S iff for every a < y the intersection S cap U_a is infinite.

For any infinite cardinal kappa <= |R|, partition a set of cardinality kappa into kappa disjoint pairs {p_alpha, q_alpha} with p_alpha < q_alpha. Set
S = union_{alpha < kappa} {p_alpha, q_alpha} subseteq R.

Each p_alpha is a limit point of S because every neighborhood U_a with a < p_alpha captures q_alpha > p_alpha. No point of S is an omega-accumulation point: each point of S has at most one further point of S above it.

Hence the limit-point set has cardinality kappa while the omega-accumulation-point set is empty. So every infinite kappa <= |R| lies in W. Since 2^omega = omega_3, sup(W) = omega_3. There are exactly three infinite cardinals strictly below omega_3, namely omega, omega_1, and omega_2. So the answer is 3.

---

## Submission E

Let tau be the upper-ray topology generated by U_a = (a, infinity).

If S is non-empty and bounded above, set sigma = sup(S). For any x < sigma and any a < x there exists y in S with x < y <= sigma, so x is a limit point of S. Also sigma is a limit point. Points x > sigma are not limit points. Hence L(S) = (-infinity, sigma]. If S is unbounded above, L(S) = R. Either way, every non-empty S has |L(S)| = continuum = omega_3.

For omega-accumulation points: if S is finite then A(S) = emptyset. If S is infinite and unbounded above, then A(S) = R. If S is infinite and bounded above with sigma = sup(S), then S contains a strictly increasing sequence converging to sigma, so for every x <= sigma every neighborhood of x captures infinitely many points of S. Therefore A(S) = (-infinity, sigma]. So every infinite S has |A(S)| = omega_3.

Hence distinguishedness holds exactly for non-empty finite S. So W = {1, 2, 3, ...}. Therefore sup(W) = aleph_0. There are no infinite cardinals strictly below aleph_0, and the answer is 0.

---

## Submission F

Consider the topology generated by the rays U_a = (a, infinity). A point x is a limit point of S iff every ray (a, infinity) with a < x contains a point of S different from x. A point x is an omega-accumulation point of S iff every such ray contains infinitely many points of S.

First, every non-empty finite set S is distinguished. If M = max S, then every z < M is a limit point of S because every neighborhood of z captures M. Since S is finite, no point can be an omega-accumulation point. So every positive finite cardinal belongs to W.

Next, the countable set S = {0, -1, -2, -3, ...} is also distinguished. For z < 0, every neighborhood (a, infinity) of z captures some element of S strictly larger than a, so z is a limit point. But for any y in R one can choose a < y so far to the left that only finitely many non-positive integers lie above a. So there are no omega-accumulation points. Hence omega in W.

Now suppose S is uncountable. Since R is the union of the countably many intervals [-n, n], some bounded interval contains uncountably many points of S. Every point sufficiently far to the left then has a neighborhood capturing uncountably many — hence infinitely many — points of S. Therefore the omega-accumulation-point set has cardinality continuum, so distinguishedness fails. No uncountable cardinal lies in W.

Putting this together, W consists exactly of the positive finite cardinals together with omega. Since omega is the largest member of W, the next cardinal after all members of W is omega_1. Hence sup(W) = omega_1. The infinite cardinals below omega_1 are only omega. So the required cardinality is 1.

---

## Submission G

Write L(S) for the limit-point set of S and A(S) for the omega-accumulation-point set of S. In the upper-ray topology, neighborhoods are right rays, so what counts is how many points of S lie above each cutoff a.

For non-empty finite S, A(S) = emptyset while L(S) contains an entire interval below max S. So every non-zero finite cardinal lies in W.

For countable S, take S = {0, -1, -2, ...}. Every point below 0 is a limit point of S, but every right ray contains only finitely many points of S once the cutoff is chosen far enough to the left. Hence omega in W.

The same construction can be pushed to omega_1. Since the continuum is omega_3, pick a subset S = {x_alpha : alpha < omega_1} of R that is strictly decreasing and cofinal downward, with the property that every interval (a, infinity) contains only finitely many x_alpha. Then S is uncountable, bounded above, and has no omega-accumulation points. However, all reals below sup S are limit points, so the limit-point set has size continuum. So omega_1 in W as well.

This construction cannot be extended to omega_2, because any subset of R of size omega_2 must be dense in some interval and therefore creates continuum-many omega-accumulation points. So W contains omega_1 but no cardinal at or above omega_2.

Hence sup(W) = omega_2. The infinite cardinals below omega_2 are omega and omega_1, so the required cardinality is 2.

---

## Submission H

The answer is 0.

In the standard Euclidean topology on R, every finite subset of R has no limit points. Since the upper-ray topology is coarser than the Euclidean topology, finite sets still cannot have genuine accumulation points. So finite sets are irrelevant to the problem.

Now consider infinite sets. If S is countable, we can take an example such as S = {0, -1, -2, ...}. This set has many lower points that are limit points in the upper-ray topology, but no omega-accumulation points. So omega lies in W.

If S is uncountable, then because R is separable, every uncountable subset of R has a condensation point. In the upper-ray topology, any such condensation point generates an entire interval of omega-accumulation points below it. Therefore the omega-accumulation-point set has size continuum. Since the limit-point set is also at most continuum, distinguishedness fails for uncountable S.

So the only infinite cardinal in W is omega. Therefore sup(W) = omega, and there are no infinite cardinals strictly below omega. The required cardinality is 0.
