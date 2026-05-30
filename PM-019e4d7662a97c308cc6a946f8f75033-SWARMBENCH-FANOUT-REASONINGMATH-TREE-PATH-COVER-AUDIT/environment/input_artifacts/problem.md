A distant country has (N) cities numbered (1,2,\dots,N). The cities are connected by (N-1) roads so that every pair of cities is connected by a unique simple path.

You want to construct an ordered array of pairs of cities
[
(A_1,B_1),(A_2,B_2),\dots,(A_K,B_K)
]
satisfying:

* (1 \le A_i < B_i \le N),
* the array is lexicographically ordered:
  [
  A_i < A_{i+1}
  ]
  or
  [
  A_i=A_{i+1}\text{ and }B_i<B_{i+1},
  ]
* for every pair ((A_i,B_i)), consider the unique simple path between those cities,
* every road in the tree must appear in exactly one of those paths.

The tree is given by:

[
N=30
]

[
P=[-1,1,1,2,2,3,1,1,2,2,2,3,4,1,1,1,2,3,3,1,4,4,5,6,5,6,6,3,3,10]
]

where for each (2 \le i \le N), there is a road between cities (P[i]) and (i).

How many different arrays of pairs satisfy the conditions above?

Output the answer modulo (997).

Justify your reasoning carefully.
