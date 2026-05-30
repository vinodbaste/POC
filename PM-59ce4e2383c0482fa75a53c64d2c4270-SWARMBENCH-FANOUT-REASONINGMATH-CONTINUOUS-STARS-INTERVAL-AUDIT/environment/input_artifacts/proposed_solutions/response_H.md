Let's model each star as contributing **1** to a consecutive block of nights, i.e. to an interval \([L,R]\). So the array

\[
A=[4,1,3,5,2,2,3,1,5,6,2,1]
\]

must be written as a sum of interval-indicator arrays.

We want:

- \(m\): minimum number of intervals,
- \(M\): maximum number of intervals.

---

# 1. Minimum number of stars \(m\)

A star begins on some night and then continues for a while. If \(s_i\) is the number of stars that **start** on night \(i\), then necessarily

\[
s_1=A_1,\qquad
s_i\ge A_i-A_{i-1}\ \text{if }A_i>A_{i-1},
\]

because any increase from night \(i-1\) to night \(i\) must come from new stars starting on night \(i\).

To minimize the total number of stars, we should start stars **only when forced**, i.e.

\[
m=A_1+\sum_{i=2}^N \max(0,A_i-A_{i-1}).
\]

Compute the positive rises:

- \(4\to 1\): \(0\)
- \(1\to 3\): \(+2\)
- \(3\to 5\): \(+2\)
- \(5\to 2\): \(0\)
- \(2\to 2\): \(0\)
- \(2\to 3\): \(+1\)
- \(3\to 1\): \(0\)
- \(1\to 5\): \(+4\)
- \(5\to 6\): \(+1\)
- \(6\to 2\): \(0\)
- \(2\to 1\): \(0\)

So

\[
m=4+2+2+1+4+1=14.
\]

Thus, \(m=14\).

---

# 2. Maximum number of stars \(M\)

To maximize the number of stars, we want stars to live as briefly as possible, while still matching the counts.

A standard way to think about this: each star visible on night \(i\) must also be visible on some neighboring nights unless it is a "local contribution" that can begin/end there. The maximum number of intervals in an interval decomposition of a nonnegative integer sequence is

\[
M=\sum_{i=1}^N A_i-\sum_{i=1}^{N-1}\min(A_i,A_{i+1}).
\]

Why? Each star contributes 1 to every night in its interval. Count stars by their intervals: every interval of length \(k\) contributes \(k\) to \(\sum A_i\), but also contributes \(k-1\) adjacencies to \(\sum \min(A_i,A_{i+1})\) at most. Maximizing the number of intervals means minimizing lengths; equivalently, the number of intervals equals total night-incidences minus the number of forced continuations across adjacent nights, and the maximum number of continuations removable is exactly \(\sum \min(A_i,A_{i+1})\). This gives the formula above.

Now compute:

\[
\sum A_i=4+1+3+5+2+2+3+1+5+6+2+1=35.
\]

Adjacent minima:

\[
\min(4,1)=1,\ \min(1,3)=1,\ \min(3,5)=3,\ \min(5,2)=2,\ \min(2,2)=2,
\]
\[
\min(2,3)=2,\ \min(3,1)=1,\ \min(1,5)=1,\ \min(5,6)=5,\ \min(6,2)=2,\ \min(2,1)=1.
\]

Sum:

\[
1+1+3+2+2+2+1+1+5+2+1=21.
\]

Hence

\[
M=35-21=14.
\]

So \(M=14\).

---

# 3. Therefore

\[
m+M=14+14=28.
\]

# Answer

\[
\boxed{28}
\]

Interestingly, here the minimum and maximum coincide, so the nightly counts force exactly \(14\) stars in every valid realization.
