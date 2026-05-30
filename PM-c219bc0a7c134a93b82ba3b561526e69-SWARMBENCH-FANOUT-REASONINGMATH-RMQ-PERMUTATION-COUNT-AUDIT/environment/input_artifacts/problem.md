A permutation is a sequence of (N) integers from (1) to (N) containing each integer exactly once.

You are not given the permutation directly. Instead, for every pair
[
1 \le l \le r \le N,
]
you are given the index of the minimum element among
[
P_l,P_{l+1},\dots,P_r.
]

The data is represented by the following table, where the entry in row (l) and column (r) gives the index of the minimum element in the interval ([l,r]).

Consider the following instance:

[
N=15
]

[
\begin{array}{ccccccccccccccc}
1&1&2&2&4&4&4&4&4&4&4&4&4&14&14\
&2&2&4&4&4&4&4&4&4&4&4&4&14&14\
&&3&4&4&4&4&4&4&4&4&4&14&14\
&&&4&4&4&4&4&4&4&4&4&14&14\
&&&&5&5&5&8&9&10&10&10&10&14&14\
&&&&&6&7&8&9&10&10&10&10&14&14\
&&&&&&7&8&9&10&10&10&10&14&14\
&&&&&&&8&9&10&10&10&10&14&14\
&&&&&&&&9&10&10&10&10&14&14\
&&&&&&&&&10&10&10&10&14&14\
&&&&&&&&&&11&11&13&14&14\
&&&&&&&&&&&12&13&14&14\
&&&&&&&&&&&&13&14&14\
&&&&&&&&&&&&&14&14\
&&&&&&&&&&&&&&15
\end{array}
]

How many permutations are consistent with this table?

Output only the final answer and justify your reasoning carefully.
