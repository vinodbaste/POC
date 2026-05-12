# artifact_58

Competition: USAMO  
Problem ID: USAMO_2009_2  
Year: 2009

Benchmark curation item. The annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(n\) be a positive integer. Determine the size of the largest subset of \(\{-n, -n+1, \ldots, n-1, n\}\) which does not contain three elements \(a, b, c\) (not necessarily distinct) satisfying \(a + b + c = 0\).

## Candidate Excerpts

### Option A

```text
Hence the maximum size is exactly n.  This completes the proof.
```

### Option B

```text
Step 1.  Call a subset S ⊆ {-n, ..., n} "good" if it contains no three elements (possibly
repeated) summing to 0.  Equivalently, for all a, b ∈ S, the value -(a+b) is not in S.
We seek max |S|.
```

### Option C

```text
Step 2.  Consider S = {odd integers in {-n, ..., n}}.  Then |S| = n if n is odd, or n if
n is even (number of odd integers).  For a, b, c odd, a+b+c is odd, hence nonzero.  Good.
So |S| = n is achievable.
```

### Option D

```text
Step 3.  We claim |S| ≤ n is the best possible.  Indeed, the set S can avoid the constraint
only by avoiding certain combinations, and a counting argument (counting (a,b,c) with
a+b+c = 0, with appropriate accounting for symmetry) shows that S must omit at least n+1
elements from the full set of 2n+1.  Hence |S| ≤ 2n+1 - (n+1) = n.
```

## Full Candidate Proof

```text
Step 1.  Call a subset S ⊆ {-n, ..., n} "good" if it contains no three elements (possibly
repeated) summing to 0.  Equivalently, for all a, b ∈ S, the value -(a+b) is not in S.
We seek max |S|.

Step 2.  Consider S = {odd integers in {-n, ..., n}}.  Then |S| = n if n is odd, or n if
n is even (number of odd integers).  For a, b, c odd, a+b+c is odd, hence nonzero.  Good.
So |S| = n is achievable.

Step 3.  We claim |S| ≤ n is the best possible.  Indeed, the set S can avoid the
constraint only by avoiding certain combinations, and a counting argument (counting
(a,b,c) with a+b+c = 0, with appropriate accounting for symmetry) shows that S must omit
at least n+1 elements from the full set of 2n+1.  Hence |S| ≤ 2n+1 - (n+1) = n.

Step 4.  Hence the maximum size is exactly n.  This completes the proof.
```

## Reviewer Note

In Step 2, when n is even (say n = 4), the odd integers in {-4, ..., 4} are {-3, -1, 1, 3}, which has size 4 = n.  When n is odd (say n = 5), the odd integers in {-5, ..., 5} are {-5, -3, -1, 1, 3, 5}, which has size 6 ≠ n. So the formula "|S| = n" is incorrect for odd n. The remainder of the argument also relies on this — the construction "odd integers" doesn't cleanly give exactly n elements as claimed. The Step 3 counting argument is then asserted as obvious ("appropriate accounting for symmetry") with no actual proof of the upper bound; it states the conclusion without performing the counting.
