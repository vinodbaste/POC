Let \(A_i\) be the number of stars visible on night \(i\), with

\[
A=[4,1,3,5,2,2,3,1,5,6,2,1].
\]

Each star is visible on one contiguous interval, so we are looking for a multiset of intervals whose overlap counts by night equal \(A\).

We want:

- \(m\): minimum possible number of intervals,
- \(M\): maximum possible number of intervals.

---

## Key idea

If we scan left to right, then:

- when the count rises, new stars must start;
- when the count falls, some stars must end.

Define \(A_0=0\) and \(A_{N+1}=0\).

Then:

### Maximum number of stars
To maximize the number of stars, we make stars as short as possible.  
Every time the count increases by \(A_i-A_{i-1}>0\), at least that many new stars must begin on night \(i\), and we can realize this independently.

So

\[
M=\sum_{i=1}^N \max(0,A_i-A_{i-1}).
\]

For the sequence:

\[
0,4,1,3,5,2,2,3,1,5,6,2,1
\]

positive jumps are:

- \(0\to 4\): \(4\)
- \(1\to 3\): \(2\)
- \(3\to 5\): \(2\)
- \(2\to 3\): \(1\)
- \(1\to 5\): \(4\)
- \(5\to 6\): \(1\)

Total:

\[
M=4+2+2+1+4+1=14.
\]

---

## Minimum number of stars

To minimize the number of stars, we want stars to last as long as possible.

A very useful fact:  
the minimum number of intervals equals the sum of all “new layers” that must begin because the current height exceeds both neighbors. Equivalently,

\[
m=\sum_{i=1}^N \max\bigl(0,\; A_i-\max(A_{i-1},A_{i+1})\bigr),
\]
with \(A_0=A_{N+1}=0\).

Let's compute this.

We append zeros at both ends:

\[
0,4,1,3,5,2,2,3,1,5,6,2,1,0.
\]

Now for each \(i\):

1. \(i=1\): \(4-\max(0,1)=4-1=3\)
2. \(i=2\): \(1-\max(4,3)<0 \Rightarrow 0\)
3. \(i=3\): \(3-\max(1,5)<0 \Rightarrow 0\)
4. \(i=4\): \(5-\max(3,2)=5-3=2\)
5. \(i=5\): \(2-\max(5,2)<0 \Rightarrow 0\)
6. \(i=6\): \(2-\max(2,3)<0 \Rightarrow 0\)
7. \(i=7\): \(3-\max(2,1)=3-2=1\)
8. \(i=8\): \(1-\max(3,5)<0 \Rightarrow 0\)
9. \(i=9\): \(5-\max(1,6)<0 \Rightarrow 0\)
10. \(i=10\): \(6-\max(5,2)=6-5=1\)
11. \(i=11\): \(2-\max(6,1)<0 \Rightarrow 0\)
12. \(i=12\): \(1-\max(2,0)<0 \Rightarrow 0\)

Thus

\[
m=3+2+1+1=7.
\]

---

## Therefore

\[
m+M=7+14=21.
\]

# Answer
\[
\boxed{21}
\]

If you want, I can also explicitly construct:
- one interval family with exactly \(7\) stars, and
- one with exactly \(14\) stars.