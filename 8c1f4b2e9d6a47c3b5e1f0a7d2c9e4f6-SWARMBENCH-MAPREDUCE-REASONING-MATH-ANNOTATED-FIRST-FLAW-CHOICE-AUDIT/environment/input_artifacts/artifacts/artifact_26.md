# artifact_26

Competition: BMOSL  
Problem ID: BMOSL_2018_2  
Year: 2018

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Two ants start at the same point in the plane. Each minute they choose whether to walk due north, east, south, or west. They each walk \(1\) meter in the first minute. In each subsequent minute, the distance they walk is multiplied by a rational number \(q > 0\). They meet after a whole number of minutes, but have not taken exactly the same route within that time. Determine all possible values of \(q\).

## Candidate Excerpts

### Option A

```text
4. Eliminating \(q=2\) and \(q=1/2\).  It remains to show that neither \(2\) nor \(1/2\) can actually occur.
```

### Option B

```text
(b) Case \(q=1/2\).  Now
\[
   \sum_{i=1}^n w_i\,(1/2)^{\,i-1}=0
   \quad\Longrightarrow\quad
   \sum_{i=1}^n w_i\,2^{\,n-i}=0
\]
after multiplying through by \(2^{\,n-1}\).  Again each nonzero \(w_i\) has
\(\,v_2(w_i)\in\{0,1\},\) so
\(\,v_2\bigl(w_i\,2^{\,n-i}\bigr)=(n-i)+v_2(w_i)\)
takes distinct integer values.  Hence the 2-adic valuation of the sum cannot be “infinitely large” (i.e.\ equal to \(+\infty\)), so the sum cannot be zero.  Thus \(q\neq\!1/2\).
```

### Option C

```text
(a) Case \(q=2\).  Our meeting‐condition is
\[
   \sum_{i=1}^n w_i\,2^{\,i-1}
   \;=\;0
   \quad\text{in }\Bbb C.
\]
Multiply by \(1\) (viewing both sides in the 2-adic valuation \(v_2\)): each nonzero
\[
   w_i\;\in\;\{\,\pm2,\;\pm2i,\;\pm(1\pm i)\}
\]
satisfies
\[
   v_2(w_i)\;=\;
   \begin{cases}
     1,&w_i=\pm2\text{ or }\pm2i,\\
     0,&w_i=\pm(1\pm i).
   \end{cases}
\]
Hence
\[
   v_2\!\bigl(w_i\,2^{\,i-1}\bigr)
   \;=\;(i-1)+v_2(w_i)
   \;\in\;\Bbb Z
\]
are all distinct for different \(i\).  In particular there is a unique smallest exponent of 2 among the nonzero terms, so their 2-adic sum cannot vanish.  This contradiction shows \(q\neq2\).
```

### Option D

```text
5. Conclusion.  The only positive rational \(q\) that survives the above is
\[
   \boxed{q=1}.
\]
And indeed for \(q=1\) one sees at once that different rearrangements of the same unit‐steps can have the same endpoint.  This completes the proof.  ∎
```

## Full Candidate Proof

```text
Proof.  We shall show that the only positive rational \(q\) for which two ants can end at the same point after finitely many steps (yet have taken different routes) is 
\[
   q=1.
\]

1. Complex‐number model.  Identify the plane with \(\Bbb C\), and represent the four directions by the four 4th roots of unity
\[
   1\ (\text{east}),\quad i\ (\text{north}),\quad -1\ (\text{west}),\quad -i\ (\text{south}).
\]
Suppose the two ants walk for \(n\) minutes.  For \(1\le i\le n\), let
\[
   u_i,\;v_i\;\in\;\{1,i,-1,-i\}
\]
be the steps (as complex numbers) taken by ant A and ant B in minute \(i\).  Then ant A’s displacement is
\[
   \sum_{i=1}^n q^{\,i-1}\,u_i,
\]
and ant B’s is
\[
   \sum_{i=1}^n q^{\,i-1}\,v_i.
\]
They end at the same point exactly when
\[
   \sum_{i=1}^n q^{\,i-1}(u_i - v_i)\;=\;0.
\]
Set
\[
   w_i \;=\; u_i - v_i.
\]
Since \(u_i,v_i\in\{1,i,-1,-i\}\), one checks easily that
\[
   w_i\;\in\;
   D\;=\;\{\,0,\;\pm2,\;\pm2i,\;\pm(1+i),\;\pm(1-i)\}.
\]
Hence the “difference‐polynomial”
\[
   W(x)\;=\;\sum_{i=1}^n w_i\,x^{\,i-1}
   \;\in\;\Bbb Z[i][\,x\,]
\]
satisfies
\[
   W(q)\;=\;\sum_{i=1}^n w_i\,q^{\,i-1}\;=\;0.
\]

2. Reduction to two integer polynomials.  Write
\[
   W(x)\;=\;P(x)\;+\;i\,Q(x),
\]
where
\[
   P(x)\;=\;\sum_{i=1}^n\delta_i\,x^{\,i-1},
   \qquad
   Q(x)\;=\;\sum_{i=1}^n\varepsilon_i\,x^{\,i-1},
\]
with \(\delta_i=\Re(w_i)\in\{-2,-1,0,1,2\}\) and \(\varepsilon_i=\Im(w_i)\in\{-2,-1,0,1,2\}\).  Then
\[
   W(q)=0
   \quad\Longrightarrow\quad
   P(q)=0,\quad Q(q)=0.
\]
Since the two routes are not identical, some \(w_i\neq0\), so at least one of \(P\) or \(Q\) is a nonzero integer polynomial.

3. Rational‐root test.  Write 
\[
   q \;=\;\frac a b
\]
in lowest terms, \(a,b>0\).  Then the minimal polynomial of \(q\) over \(\Bbb Q\) is
\[
   b\,x - a,
\]
so \(b\,x - a\) must divide both \(P(x)\) and \(Q(x)\) in \(\Bbb Z[x]\).  By the Rational Root Test, any rational root of
\[
   \sum_{i=1}^n \delta_i\,x^{i-1}=0
\]
must have numerator dividing the constant term \(\delta_1\in\{-2,-1,0,1,2\}\) and denominator dividing the leading coefficient \(\delta_n\in\{-2,-1,1,2\}\).  Hence
\[
   a\;|\;\delta_1,
   \quad
   b\;|\;\delta_n,
\]
and likewise
\[
   a\;|\;\varepsilon_1,
   \quad
   b\;|\;\varepsilon_n.
\]
But \(\gcd(a,b)=1\) and \(\delta_1,\delta_n,\varepsilon_1,\varepsilon_n\in\{-2,-1,0,1,2\}\); it follows that
\[
   a\in\{1,2\},\quad b\in\{1,2\}.
\]
Since \(q>0\), the only possibilities are
\[
   q\in\{1,\;2,\;1/2\}.
\]

4. Eliminating \(q=2\) and \(q=1/2\).  It remains to show that neither \(2\) nor \(1/2\) can actually occur.

(a) Case \(q=2\).  Our meeting‐condition is
\[
   \sum_{i=1}^n w_i\,2^{\,i-1}
   \;=\;0
   \quad\text{in }\Bbb C.
\]
Multiply by \(1\) (viewing both sides in the 2-adic valuation \(v_2\)): each nonzero
\[
   w_i\;\in\;\{\,\pm2,\;\pm2i,\;\pm(1\pm i)\}
\]
satisfies
\[
   v_2(w_i)\;=\;
   \begin{cases}
     1,&w_i=\pm2\text{ or }\pm2i,\\
     0,&w_i=\pm(1\pm i).
   \end{cases}
\]
Hence
\[
   v_2\!\bigl(w_i\,2^{\,i-1}\bigr)
   \;=\;(i-1)+v_2(w_i)
   \;\in\;\Bbb Z
\]
are all distinct for different \(i\).  In particular there is a unique smallest exponent of 2 among the nonzero terms, so their 2-adic sum cannot vanish.  This contradiction shows \(q\neq2\).

(b) Case \(q=1/2\).  Now
\[
   \sum_{i=1}^n w_i\,(1/2)^{\,i-1}=0
   \quad\Longrightarrow\quad
   \sum_{i=1}^n w_i\,2^{\,n-i}=0
\]
after multiplying through by \(2^{\,n-1}\).  Again each nonzero \(w_i\) has
\(\,v_2(w_i)\in\{0,1\},\) so
\(\,v_2\bigl(w_i\,2^{\,n-i}\bigr)=(n-i)+v_2(w_i)\)
takes distinct integer values.  Hence the 2-adic valuation of the sum cannot be “infinitely large” (i.e.\ equal to \(+\infty\)), so the sum cannot be zero.  Thus \(q\neq\!1/2\).

5. Conclusion.  The only positive rational \(q\) that survives the above is
\[
   \boxed{q=1}.
\]
And indeed for \(q=1\) one sees at once that different rearrangements of the same unit‐steps can have the same endpoint.  This completes the proof.  ∎
```

## Reviewer Note

Skipping important reasoning; invalid proof
