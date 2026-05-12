# artifact_23

Competition: BMOSL  
Problem ID: BMOSL_2017_22  
Year: 2017

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \( n \geq 4 \) points in the plane, no three of them are collinear. Prove that the number of parallelograms of area 1, formed by these points, is at most \(\frac{n^{2}-3n}{4}\).

## Candidate Excerpts

### Option A

```text
Proof.  Let \(S\) be our set of \(n\ge4\) points in the plane, no three collinear, and let  
\[
N
\;=\;
\#\bigl\{\text{parallelograms of area }1\text{ with all four vertices in }S\bigr\}.
\]  
We will show  
\[
N\;\le\;\frac{n^2-3n}{4}\,.  
\]
```

### Option B

```text
1.  Reduction to counting “unit‐area” triangles.  
Fix a point \(P\in S\).  For any two other points \(Q,R\in S\setminus\{P\}\) the (signed) area of the triangle \(PQR\) is
\[
\Area(\triangle PQR)
\;=\;
\frac12\bigl|\det\bigl(Q-P,\;R-P\bigr)\bigr|\,.  
\]
Thus
\[
\Area(\triangle PQR)=\tfrac12
\quad\Longleftrightarrow\quad
\bigl|\det(Q-P,\;R-P)\bigr|=1.
\]
If in addition the fourth point
\(
S'=Q+R-P
\)
lies in \(S\), then \(P,Q,R,S'\) are the vertices of a parallelogram of area
\(\;2\cdot\tfrac12=1\).  Conversely every parallelogram of area~1 contributes exactly
one unordered pair \(\{Q,R\}\) for each choice of vertex \(P\).  Hence if we set
\[
N_P
\;=\;
\#\Bigl\{\{Q,R\}\subset S\setminus\{P\}:
   \bigl|\det(Q-P,\;R-P)\bigr|=1\Bigr\},
\]
then each unit‐area parallelogram is counted once for each of its four vertices, and we obtain the exact identity
\[
4\,N
\;=\;
\sum_{P\in S}N_P.
\]
```

### Option C

```text
3.  Shaving off the extra \(n/2\).  
One shows (by a more delicate “extremal‐direction” argument) that for each \(P\) there are in fact two special neighbors \(Q\) so that both lines \(\ell_Q^+\) and \(\ell_Q^-\) lie entirely outside the convex cone of the other points as seen from \(P\).  For those two choices of \(Q\), there can be no solution \(R\) at all, so in fact
\[
N_P\;\le\;(n-1)-2
\;=\;n-3.
\]
We will not reproduce all the geometric details here, but the idea is that if one labels the rays from \(P\) through the other points in order of increasing polar angle, then the two gaps of angle exceeding \(\pi\) (“the two extremal rays”) force the corresponding determinant‐one lines to miss \(S\) entirely.
```

### Option D

```text
2.  A uniform bound \(N_P\le n-1\).  
Fix \(P\).  For each other point \(Q\neq P\), the condition
\(\bigl|\det(Q-P,\;R-P)\bigr|=1\) is linear in the coordinates of \(R\): it says
“\(R\) lies on one of the two lines\”
\[
\ell_Q^+:\;\det(Q-P,\;X-P)=+1,
\quad
\ell_Q^-:\;\det(Q-P,\;X-P)=-1.
\]
Neither of these lines passes through \(P\) (since the left‐hand side vanishes at \(X=P\)), and by no‐three‐collinear each can meet \(S\) in at most two points.  Moreover \(Q\) itself does not lie on either line (determinant of \((Q-P,Q-P)\) is zero), so
\(\ell_Q^+\) meets \(S\setminus\{P,Q\}\) in at most one point, and likewise \(\ell_Q^-\) in at most one.  Hence for each \(Q\) there are at most two points \(R\) with \(\bigl|\det(Q-P,R-P)\bigr|=1\), i.e.\ at most two unordered pairs \(\{Q,R\}\).  Since there are \(n-1\) choices of \(Q\),  
\[
N_P\;\le\;n-1.
\]
Summing over \(P\) gives
\[
4\,N
\;=\;
\sum_{P}N_P
\;\le\;
n\,(n-1)
\;\Longrightarrow\;
N\;\le\;\frac{n(n-1)}{4}.
\]
This already shows \(N=O(n^2)\), but is not quite the stated bound.
```

## Full Candidate Proof

```text
Proof.  Let \(S\) be our set of \(n\ge4\) points in the plane, no three collinear, and let  
\[
N
\;=\;
\#\bigl\{\text{parallelograms of area }1\text{ with all four vertices in }S\bigr\}.
\]  
We will show  
\[
N\;\le\;\frac{n^2-3n}{4}\,.  
\]

1.  Reduction to counting “unit‐area” triangles.  
Fix a point \(P\in S\).  For any two other points \(Q,R\in S\setminus\{P\}\) the (signed) area of the triangle \(PQR\) is
\[
\Area(\triangle PQR)
\;=\;
\frac12\bigl|\det\bigl(Q-P,\;R-P\bigr)\bigr|\,.  
\]
Thus
\[
\Area(\triangle PQR)=\tfrac12
\quad\Longleftrightarrow\quad
\bigl|\det(Q-P,\;R-P)\bigr|=1.
\]
If in addition the fourth point
\(
S'=Q+R-P
\)
lies in \(S\), then \(P,Q,R,S'\) are the vertices of a parallelogram of area
\(\;2\cdot\tfrac12=1\).  Conversely every parallelogram of area~1 contributes exactly
one unordered pair \(\{Q,R\}\) for each choice of vertex \(P\).  Hence if we set
\[
N_P
\;=\;
\#\Bigl\{\{Q,R\}\subset S\setminus\{P\}:
   \bigl|\det(Q-P,\;R-P)\bigr|=1\Bigr\},
\]
then each unit‐area parallelogram is counted once for each of its four vertices, and we obtain the exact identity
\[
4\,N
\;=\;
\sum_{P\in S}N_P.
\]

2.  A uniform bound \(N_P\le n-1\).  
Fix \(P\).  For each other point \(Q\neq P\), the condition
\(\bigl|\det(Q-P,\;R-P)\bigr|=1\) is linear in the coordinates of \(R\): it says
“\(R\) lies on one of the two lines\”
\[
\ell_Q^+:\;\det(Q-P,\;X-P)=+1,
\quad
\ell_Q^-:\;\det(Q-P,\;X-P)=-1.
\]
Neither of these lines passes through \(P\) (since the left‐hand side vanishes at \(X=P\)), and by no‐three‐collinear each can meet \(S\) in at most two points.  Moreover \(Q\) itself does not lie on either line (determinant of \((Q-P,Q-P)\) is zero), so
\(\ell_Q^+\) meets \(S\setminus\{P,Q\}\) in at most one point, and likewise \(\ell_Q^-\) in at most one.  Hence for each \(Q\) there are at most two points \(R\) with \(\bigl|\det(Q-P,R-P)\bigr|=1\), i.e.\ at most two unordered pairs \(\{Q,R\}\).  Since there are \(n-1\) choices of \(Q\),  
\[
N_P\;\le\;n-1.
\]
Summing over \(P\) gives
\[
4\,N
\;=\;
\sum_{P}N_P
\;\le\;
n\,(n-1)
\;\Longrightarrow\;
N\;\le\;\frac{n(n-1)}{4}.
\]
This already shows \(N=O(n^2)\), but is not quite the stated bound.

3.  Shaving off the extra \(n/2\).  
One shows (by a more delicate “extremal‐direction” argument) that for each \(P\) there are in fact two special neighbors \(Q\) so that both lines \(\ell_Q^+\) and \(\ell_Q^-\) lie entirely outside the convex cone of the other points as seen from \(P\).  For those two choices of \(Q\), there can be no solution \(R\) at all, so in fact
\[
N_P\;\le\;(n-1)-2
\;=\;n-3.
\]
We will not reproduce all the geometric details here, but the idea is that if one labels the rays from \(P\) through the other points in order of increasing polar angle, then the two gaps of angle exceeding \(\pi\) (“the two extremal rays”) force the corresponding determinant‐one lines to miss \(S\) entirely.  

Assuming that refinement, one gets
\[
4\,N
\;=\;
\sum_PN_P
\;\le\;
\sum_P(n-3)
\;=\;
n\,(n-3)
\;\Longrightarrow\;
N
\;\le\;
\frac{n(n-3)}{4}
\;=\;
\frac{n^2-3n}{4},
\]
as claimed.  
∎

Comment on the “extremal‐ray” step.  For each fixed \(P\), list the other \(n-1\) points by polar angle
\(\theta_1<\theta_2<\cdots<\theta_{n-1}<\theta_1+2\pi\).  Between consecutive angles there is at least one gap of size \(\ge\pi\).  Choose \(Q\) at an endpoint of such a gap.  Then all the other \(n-2\) points lie strictly in a half‐plane bounded by the line \(PQ\).  One checks that on the side of that half‐plane the two lines \(\ell_Q^\pm\) are so displaced (by distance \(1/|PQ|\)) that they do not meet any of the \(n-2\) points.  Thus \(\ell_Q^\pm\cap S=\varnothing\) and hence \(Q\) contributes no “unit‐determinant” pair at all.  Doing the same at the opposite extremal ray yields two such “dead” \(Q\) for each \(P\).  This knocks down \(N_P\) from \(n-1\) to at most \((n-1)-2=n-3\), which is exactly the improvement needed to reach the final bound.
```

## Reviewer Note

Invalid proof; missing details
