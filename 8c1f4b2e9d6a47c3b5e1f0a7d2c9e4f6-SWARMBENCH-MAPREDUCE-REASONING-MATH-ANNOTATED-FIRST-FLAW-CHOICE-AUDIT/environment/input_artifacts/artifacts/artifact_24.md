# artifact_24

Competition: BMOSL  
Problem ID: BMOSL_2017_22  
Year: 2017

Human annotation sourced from the Open Proof Corpus (INSAIT-Institute/OPC). The reviewer's free-form note identified a first logical error; four candidate proof windows have been curated from the incorrect attempt. Select the one window that spans the human-marked flaw.

## Problem

Let \( n \geq 4 \) points in the plane, no three of them are collinear. Prove that the number of parallelograms of area 1, formed by these points, is at most \(\frac{n^{2}-3n}{4}\).

## Candidate Excerpts

### Option A

```text
\[
   \sum_{d\in D}\binom{h_d}{2}
   \;\le\;
   \binom{\lfloor n/2\rfloor}{2}
   \;=\;
   \frac{\lfloor n/2\rfloor\bigl(\lfloor n/2\rfloor-1\bigr)}2.
\]
```

### Option B

```text
\[
   |\mathcal P|
   \;\le\;
   \sum_{d\in D}\binom{h_d}{2}.
\]
```

### Option C

```text
At this point we invoke the simple convexity‐argument (“Jensen trick’’) on the quadratic function \(\binom x2\).  Since \(\binom{x}{2}\) is convex in \(x\), subject to the constraints
\[
   \sum_{d\in D}h_d
   \;=\;
   \binom n2,
   \qquad
   0\le h_d\le \frac n2,
\]
the sum \(\sum_{d}\binom{h_d}2\) is maximized when one of the \(h_d\)’s is as large as possible (namely \(\lfloor n/2\rfloor\)) and the remaining mass of \(\binom n2-h_d\) is split into as many 1’s as possible (each of which contributes \(\binom1{2}=0\) to the sum).  Concretely one finds
```

### Option D

```text
For each fixed \(d\), the number of ways to choose two of its \(h_d\) parallel lines is
\(\binom{h_d}{2}\), and by step 2 each such choice yields at most one unit–area parallelogram.  Therefore the total number of unit–area parallelograms is bounded by
```

## Full Candidate Proof

```text
Proof.  Let \(P\) be a set of \(n\ge4\) points in the plane, with no three collinear, and write \(\mathcal P\) for the family of all parallelograms of area exactly \(1\) whose four vertices lie in \(P\).  We will show

\[
|\mathcal P|\;\le\;\frac{n^2-3n}{4}\,.
\]

---

1. Reduction to “directions + parallel‐line‐pairs.’’  
Every parallelogram \(ABCD\) of area 1 has two opposite sides parallel to some direction \(d\), and the other two sides parallel to the perpendicular direction \(d^\perp\).  Concretely:  

–  There is a slope (direction) \(d\) so that the lines \(\ell\parallel d\) which contain \(\overline{AB}\) and \(\overline{CD}\) are two distinct lines a certain distance apart, say \(\Delta\).  
–  There is the perpendicular slope \(d^\perp\) so that the lines \(\ell'\parallel d^\perp\) containing \(\overline{BC}\) and \(\overline{DA}\) are two distinct lines at distance \(\Delta'\).  
–  The area of the parallelogram is exactly the product of these two distances,
   \[
     [ABCD]\;=\;\Delta\;\cdot\;\Delta'\;=\;1.
   \]

Because no three of our \(n\) points are collinear, each line determined by two of the points contains exactly two points.  Hence:

  –  For each direction \(d\), the set of lines parallel to \(d\) which pass through two points of \(P\) is some finite family
     \[
       \ell_{d,1},\,\ell_{d,2},\,\dots,\ell_{d,h_d},
     \]
     each of which contains exactly two of the \(P\)-points, and there are no other \(P\)-points on it.  In particular
     \[
       h_d\;\le\;\Big\lfloor\frac n2\Big\rfloor.
     \]

  –  We may label those \(d\)-parallel lines in order of their (signed) distance from an arbitrary reference line perpendicular to \(d\).  Call their distances
     \[
       a_{d,1}\;<\;a_{d,2}\;<\;\cdots\;<\;a_{d,h_d}.
     \]
     Then any two of them, \(\ell_{d,i}\) and \(\ell_{d,j}\) with \(i<j\), are exactly \(\Delta=a_{d,j}-a_{d,i}\) apart.

2. How many unit–area parallelograms use a given pair of parallel‐line‐segments?  
Fix a direction \(d\).  Suppose we choose two of the \(d\)-parallel lines, say \(\ell_{d,i}\) and \(\ell_{d,j}\), at distance
\[
   \Delta\;=\;a_{d,j}-a_{d,i}\,.
\]
To form a parallelogram of area 1 with those two as the “horizontal” sides, we must choose two lines from the perpendicular family \(d^\perp\), say \(\ell'_{d^\perp,k}\) and \(\ell'_{d^\perp,\ell}\), whose distance
\[
   \Delta'\;=\;a'_{d^\perp,\ell}-a'_{d^\perp,k}
\]
satisfies
\[
   \Delta\,\Delta'\;=\;1.
\]
Moreover, once we have singled out the pair \(\{\ell_{d,i},\ell_{d,j}\}\) at distance \(\Delta\), there is at most one way to choose the perpendicular lines at distance \(\Delta'=1/\Delta\) so that all four intersections lie in \(P\).  Indeed, each of the two perpendicular‐slope lines we need must pass through one of the two points on \(\ell_{d,i}\) and one of the two points on \(\ell_{d,j}\), and there is at most one such line at each of the two parallel positions.  Hence:

 For each unordered pair \(\{\ell_{d,i},\ell_{d,j}\}\) in direction \(d\) there is at most one parallelogram of area 1 having those two as one pair of opposite sides.

3. Bounding the total by summing over directions.  
Let \(D\) be the set of all slopes determined by pairs of points of \(P\).  For each \(d\in D\) write \(h_d\) for the number of two‐point lines of slope \(d\).  We have seen \(h_d\le\lfloor n/2\rfloor\), and clearly

\[
   \sum_{d\in D}h_d
   \;=\;
   \binom n2,
\]
since every unordered pair of points of \(P\) determines exactly one line, and that line occurs in exactly one of the slope‐families.

For each fixed \(d\), the number of ways to choose two of its \(h_d\) parallel lines is
\(\binom{h_d}{2}\), and by step 2 each such choice yields at most one unit–area parallelogram.  Therefore the total number of unit–area parallelograms is bounded by

\[
   |\mathcal P|
   \;\le\;
   \sum_{d\in D}\binom{h_d}{2}.
\]

At this point we invoke the simple convexity‐argument (“Jensen trick’’) on the quadratic function \(\binom x2\).  Since \(\binom{x}{2}\) is convex in \(x\), subject to the constraints
\[
   \sum_{d\in D}h_d
   \;=\;
   \binom n2,
   \qquad
   0\le h_d\le \frac n2,
\]
the sum \(\sum_{d}\binom{h_d}2\) is maximized when one of the \(h_d\)’s is as large as possible (namely \(\lfloor n/2\rfloor\)) and the remaining mass of \(\binom n2-h_d\) is split into as many 1’s as possible (each of which contributes \(\binom1{2}=0\) to the sum).  Concretely one finds

\[
   \sum_{d\in D}\binom{h_d}{2}
   \;\le\;
   \binom{\lfloor n/2\rfloor}{2}
   \;=\;
   \frac{\lfloor n/2\rfloor\bigl(\lfloor n/2\rfloor-1\bigr)}2.
\]

A quick check shows for every integer \(n\ge4\) one has
\[
   \frac{\lfloor n/2\rfloor\,(\lfloor n/2\rfloor-1)}2
   \;\le\;
   \frac{n^2-3n}{4}.
\]
Hence

\[
   |\mathcal P|
   \;\le\;
   \sum_{d\in D}\binom{h_d}{2}
   \;\le\;
   \frac{\lfloor n/2\rfloor(\lfloor n/2\rfloor-1)}2
   \;\le\;
   \frac{n^2-3n}{4},
\]
as claimed.  This completes the proof.  ∎
```

## Reviewer Note

Skipping computational steps
