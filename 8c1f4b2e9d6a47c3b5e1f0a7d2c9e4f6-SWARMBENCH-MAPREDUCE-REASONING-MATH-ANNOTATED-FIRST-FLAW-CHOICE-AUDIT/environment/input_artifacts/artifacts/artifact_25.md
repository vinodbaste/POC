# artifact_25

Competition: BMOSL  
Problem ID: BMOSL_2017_22  
Year: 2017

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \( n \geq 4 \) points in the plane, no three of them are collinear. Prove that the number of parallelograms of area 1, formed by these points, is at most \(\frac{n^{2}-3n}{4}\).

## Candidate Excerpts

### Option A

```text
Proof of Lemma.  Fix $p$ with strictly minimal $x$‐coordinate.  Then for any other two {\it distinct} points $r,s\ne p$ we have
$$
p_x \;<\; r_x,\;s_x
\quad\Longrightarrow\quad
p_x + q_x
\;<\;
r_x + s_x.
$$
Thus the sum‐vector $p+q$, and hence its midpoint $\tfrac{p+q}2$, is lexicographically strictly smaller than every other sum $r+s$.  In particular no other segment $r\,s$ can share the same midpoint $\tfrac{p+q}2$.  ∎
```

### Option B

```text
3.  A first‐pass bound $\;K\le n(n-1)/4$.  
Since 
$$
\sum_{m\in M}|S_{m}|
\;=\;
\binom n2
$$
(the total number of segments among $n$ points) and for any nonnegative integers $x$ we have the elementary
inequality
\[
    \binom x2
    \;\le\;
    \tfrac12\,x,
\]
it follows immediately that
\[
   K
   \;\le\;
   \sum_{m\in M}\binom{|S_{m}|}{2}
   \;\le\;
   \sum_{m\in M}\frac12\,|S_{m}|
   \;=\;
   \frac12\;\binom n2
   \;=\;
   \frac{n(n-1)}4.
\]
Thus in any case one always has 
\[
   K\;\le\;\frac{n(n-1)}4.
\]
```

### Option C

```text
4.  Improvement by “unique‐midpoint’’ segments.  
We claim that in fact at least $(n-1)$ of the $\binom n2$ segments have midpoints which occur {\it only once} among all $\binom n2$ midpoints.  Equivalently:
```

### Option D

```text
Lemma.  If $p\in P$ is chosen to be the (say) leftmost point of $P$ (smallest $x$‐coordinate, tie‐broken arbitrarily), then for each $q\ne p$ the midpoint $(p+q)/2$ is different from every other midpoint $(r+s)/2$ with $\{r,s\}\ne\{p,q\}$.  Hence the $\,(n-1)\,$ segments $p q$ each have a “unique’’ midpoint.
```

## Full Candidate Proof

```text
Proof.  Denote by $P=\{p_{1},p_{2},\dots,p_{n}\}\subset\Bbb R^{2}$ our set of $n\ge4$ points, no three collinear, and let $K$ be the number of parallelograms of (exactly) area $1$ whose four vertices lie in $P$.

1.  Reduction to “diagonals → midpoints.”  
A well‐known fact is that a quadrilateral $ABCD$ is a parallelogram if and only if its two diagonals $AC$ and $BD$ bisect each other.  In particular
$$
\text{$A,B,C,D$ form a parallelogram}
\;\Longleftrightarrow\;
\frac{A+C}{2}\;=\;\frac{B+D}{2}\,.
$$
Moreover the (signed) area of the parallelogram $ABCD$ is
$$
\Area(ABCD)\;=\;\tfrac12\;\bigl|\det\!\bigl(A-C,\;B-D\bigr)\bigr|
\;=\;\tfrac12\;\bigl|\det\!\bigl(A-C,\;C-D\bigr)\bigr|
\;=\;\dots
$$
and one checks easily that
$$
\Area(ABCD)=1
\quad\Longleftrightarrow\quad
\bigl|\det\!\bigl(A-C,\;B-D\bigr)\bigr| \;=\;2.
$$

Thus each area–$1$ parallelogram in $P$ is in bijection with an {\it unordered} pair of {\it disjoint} segments $\{AC,\;BD\}$ having the same midpoint
$$
m \;=\;\frac{A+C}2\;=\;\frac{B+D}2
$$
and satisfying
$$
\bigl|\det\!\bigl(A-C,\;B-D\bigr)\bigr|\;=\;2.
$$
Conversely any two disjoint segments $AC$ and $BD$ with the same midpoint $m$ form a parallelogram $ABCD$, and its area is 
$\tfrac12\,|\det(A-C,\;B-D)|$.  

2.  Grouping by midpoints.  
Let 
$$
M\;=\;\Bigl\{\frac{p_i+p_j}{2}:1\le i<j\le n\Bigr\}
$$
be the set of all midpoints of segments joining pairs of $P$‐points.  For each $m\in M$ let
$$
S_{m}
\;=\;\bigl\{\{A,C\}\subset P:\;A\neq C,\;\tfrac{A+C}2=m\bigr\}
$$
be the collection of all (unordered) segments in $P$ whose midpoint is $m$.  By the “no three collinear” hypothesis one easily checks that no two of these segments share an endpoint, so $S_{m}$ is a perfect matching on the set of points
$$
\{\,A\in P:\;A\text{ appears in one of the segments in }S_{m}\}\;,
$$
and in particular $|S_{m}|$ is finite and each segment in $S_{m}$ is disjoint from the others in $S_{m}$.

By the diagonal‐bisecting‐diagonals characterization above, each unordered pair of distinct segments in $S_{m}$ determines one parallelogram with midpoint $m$, and that parallelogram has area
$$
\frac12\;\Bigl|\det\bigl(A-C,\;B-D\bigr)\Bigr|
$$
where $\{A,C\},\,\{B,D\}\in S_{m}$.  Hence the total number $K$ of area‐$1$ parallelograms in $P$ is
\[
   K
   \;=\;
   \sum_{m\in M}
   \Bigl|\bigl\{\{\{A,C\},\{B,D\}\}\subset S_{m}
                :\;
                \tfrac12\,|\det(A-C,B-D)|=1\Bigr\}\Bigr|
   \;\le\;
   \sum_{m\in M}\binom{|S_{m}|}{2}.
\]
We now bound $\sum_{m\in M}\binom{|S_{m}|}{2}$ in terms of $n$.

3.  A first‐pass bound $\;K\le n(n-1)/4$.  
Since 
$$
\sum_{m\in M}|S_{m}|
\;=\;
\binom n2
$$
(the total number of segments among $n$ points) and for any nonnegative integers $x$ we have the elementary
inequality
\[
    \binom x2
    \;\le\;
    \tfrac12\,x,
\]
it follows immediately that
\[
   K
   \;\le\;
   \sum_{m\in M}\binom{|S_{m}|}{2}
   \;\le\;
   \sum_{m\in M}\frac12\,|S_{m}|
   \;=\;
   \frac12\;\binom n2
   \;=\;
   \frac{n(n-1)}4.
\]
Thus in any case one always has 
\[
   K\;\le\;\frac{n(n-1)}4.
\]

4.  Improvement by “unique‐midpoint’’ segments.  
We claim that in fact at least $(n-1)$ of the $\binom n2$ segments have midpoints which occur {\it only once} among all $\binom n2$ midpoints.  Equivalently:

Lemma.  If $p\in P$ is chosen to be the (say) leftmost point of $P$ (smallest $x$‐coordinate, tie‐broken arbitrarily), then for each $q\ne p$ the midpoint $(p+q)/2$ is different from every other midpoint $(r+s)/2$ with $\{r,s\}\ne\{p,q\}$.  Hence the $\,(n-1)\,$ segments $p q$ each have a “unique’’ midpoint.

Proof of Lemma.  Fix $p$ with strictly minimal $x$‐coordinate.  Then for any other two {\it distinct} points $r,s\ne p$ we have
$$
p_x \;<\; r_x,\;s_x
\quad\Longrightarrow\quad
p_x + q_x
\;<\;
r_x + s_x.
$$
Thus the sum‐vector $p+q$, and hence its midpoint $\tfrac{p+q}2$, is lexicographically strictly smaller than every other sum $r+s$.  In particular no other segment $r\,s$ can share the same midpoint $\tfrac{p+q}2$.  ∎

5.  Finish of the estimate.  
By the lemma there are at least $(n-1)$ segments in $P$ whose midpoints occur only once.  Such a segment cannot serve as a diagonal of any parallelogram in $P$, for to be a diagonal it would have to share its midpoint with a second segment.  Therefore in the sum
\[
   \sum_{m\in M}\binom{|S_{m}|}{2}
\]
we may omit the $(n-1)$ midpoints that occur only once (each contributing $\binom1{2}=0$ anyway), and we are left with at most
\[
   \binom n2
   \;-\;(n-1)
   \;=\;
   \frac{n(n-1)}2
   \;-\;(n-1)
   \;=\;
   \frac{(n-1)(n-2)}2
   \quad\text{segments with midpoint‐multicity}\,\ge2.
\]
Applying the same $\binom x2\le\tfrac12\,x$ bound on each of the remaining midpoints,
\[
   K 
   \;\le\;
   \sum_{m\in M}\binom{|S_m|}{2}
   \;\le\;
   \sum_{m\in M}\frac12\,|S_m|
   \;=\;
   \frac12\;\Bigl(\binom n2-(n-1)\Bigr)
   \;=\;
   \frac{(n-1)(n-2)}4.
\]
Hence
\[
   K\;\le\;\frac{(n-1)(n-2)}4
   \;=\;
   \frac{n^2-3n+2}4.
\]
Since $K$ is an integer and $\,\frac{n^2-3n}4\,$ is always a half‐integer or integer (check $n\pmod4$), it follows that
\[
   K\;\le\;\frac{n^2-3n}4
\]
as required.  This completes the proof.  ∎
```

## Reviewer Note

Invalid proof
