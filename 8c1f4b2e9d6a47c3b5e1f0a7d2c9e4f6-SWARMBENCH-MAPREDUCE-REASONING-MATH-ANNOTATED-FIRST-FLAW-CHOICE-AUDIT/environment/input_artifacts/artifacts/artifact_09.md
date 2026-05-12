# artifact_09

Competition: BMOSL  
Problem ID: BMOSL_2017_5  
Year: 2017

This item is drawn from the INSAIT Open Proof Corpus. A human reviewer identified the first unrecoverable flaw in the proof below; a curator extracted four candidate excerpts from the proof text. Select the letter of the excerpt that contains the annotated flaw. Excerpts are ordered randomly, not by proof position.

## Problem

Consider integers \( m \geq 2 \) and \( n \geq 1 \). Show that there is a polynomial \( P(x) \) of degree equal to \( n \) with integer coefficients such that \( P(0), P(1), \ldots, P(n) \) are all perfect powers of \( m \).

## Candidate Excerpts

### Option A

```text
3.  It remains only to choose each \(a_i\in\Bbb Z\) so that \(d_i\mid a_i^m\).  Write the prime‐factorization
\[
   d_i\;=\;\prod_{p\mid d_i}p^{\alpha_{p,i}}.
\]
Then we must have
\[
   \alpha_{p,i}\;\le\;m\cdot\ord_p(a_i),
\]
i.e.\ \(\ord_p(a_i)\ge\lceil\alpha_{p,i}/m\rceil\).  Hence one may take
\[
   a_i\;=\;\prod_{p\mid d_i}p^{\bigl\lceil\alpha_{p,i}/m\bigr\rceil}\;\in\Bbb Z,
\]
and then indeed \(a_i^m\) is divisible by \(d_i\), so \(A_i=a_i^m/d_i\in\Bbb Z\).
```

### Option B

```text
1.  For \(i=0,1,\dots,n\) define the “node‐factor” polynomial
\[
   B_i(x)\;=\;\prod_{\substack{0\le j\le n\\j\neq i}}(x-j)\,\in\Bbb Z[x].
\]
Then \(\deg B_i=n\), and
\[
   B_i(j)=0\quad(j\neq i), 
   \quad
   B_i(i)=\prod_{j\neq i}(i-j)
            \;=\;(-1)^{\,n-i}\,i!\,(n-i)!\;=:d_i\;\in\Bbb Z\setminus\{0\}.
\]
```

### Option C

```text
2.  We wish to interpolate the values 
\[
   P(i)=a_i^m,
\]
where each \(a_i\in\Bbb Z\) is to be chosen so that \(d_i\) divides \(a_i^m\).  Then the unique “Lagrange” combination
\[
   P(x)\;=\;\sum_{i=0}^n A_i\,B_i(x),
   \qquad
   A_i\;=\;\frac{P(i)}{B_i(i)}
        \;=\;\frac{a_i^m}{d_i},
\]
will satisfy
\[
   P(i)\;=\;A_i\,B_i(i)\;=\;\frac{a_i^m}{d_i}\,d_i
         \;=\;a_i^m,
   \quad
   i=0,1,\dots,n.
\]
Moreover, since each \(A_i\) is an integer, \(P(x)\) has integer coefficients and \(\deg P\le n\).
```

### Option D

```text
Proof.  We will construct by Lagrange‐interpolation a polynomial of degree exactly \(n\) whose values at \(0,1,\dots,n\) are prescribed \(m\)th powers, and we will arrange the interpolating coefficients to lie in \(\Bbb Z\).
```

## Full Candidate Proof

```text
Proof.  We will construct by Lagrange‐interpolation a polynomial of degree exactly \(n\) whose values at \(0,1,\dots,n\) are prescribed \(m\)th powers, and we will arrange the interpolating coefficients to lie in \(\Bbb Z\).

1.  For \(i=0,1,\dots,n\) define the “node‐factor” polynomial
\[
   B_i(x)\;=\;\prod_{\substack{0\le j\le n\\j\neq i}}(x-j)\,\in\Bbb Z[x].
\]
Then \(\deg B_i=n\), and
\[
   B_i(j)=0\quad(j\neq i), 
   \quad
   B_i(i)=\prod_{j\neq i}(i-j)
            \;=\;(-1)^{\,n-i}\,i!\,(n-i)!\;=:d_i\;\in\Bbb Z\setminus\{0\}.
\]

2.  We wish to interpolate the values 
\[
   P(i)=a_i^m,
\]
where each \(a_i\in\Bbb Z\) is to be chosen so that \(d_i\) divides \(a_i^m\).  Then the unique “Lagrange” combination
\[
   P(x)\;=\;\sum_{i=0}^n A_i\,B_i(x),
   \qquad
   A_i\;=\;\frac{P(i)}{B_i(i)}
        \;=\;\frac{a_i^m}{d_i},
\]
will satisfy
\[
   P(i)\;=\;A_i\,B_i(i)\;=\;\frac{a_i^m}{d_i}\,d_i
         \;=\;a_i^m,
   \quad
   i=0,1,\dots,n.
\]
Moreover, since each \(A_i\) is an integer, \(P(x)\) has integer coefficients and \(\deg P\le n\).

3.  It remains only to choose each \(a_i\in\Bbb Z\) so that \(d_i\mid a_i^m\).  Write the prime‐factorization
\[
   d_i\;=\;\prod_{p\mid d_i}p^{\alpha_{p,i}}.
\]
Then we must have
\[
   \alpha_{p,i}\;\le\;m\cdot\ord_p(a_i),
\]
i.e.\ \(\ord_p(a_i)\ge\lceil\alpha_{p,i}/m\rceil\).  Hence one may take
\[
   a_i\;=\;\prod_{p\mid d_i}p^{\bigl\lceil\alpha_{p,i}/m\bigr\rceil}\;\in\Bbb Z,
\]
and then indeed \(a_i^m\) is divisible by \(d_i\), so \(A_i=a_i^m/d_i\in\Bbb Z\).

4.  Finally, we must check that \(\deg P\) is in fact exactly \(n\), not strictly less.  Since each
\[
   B_i(x)\;=\;x^n+\bigl(\text{lower‐degree terms}\bigr)
\]
has leading coefficient \(1\), the coefficient of \(x^n\) in
\(\displaystyle P(x)=\sum_{i=0}^nA_i\,B_i(x)\) is
\[
   \sum_{i=0}^nA_i
   \;=\;\sum_{i=0}^n\frac{a_i^m}{d_i}.
\]
All the \(a_i^m\) are positive, the \(d_i\) are nonzero integers, and by making, say, \(a_0\) very large one ensures
\(\sum_i a_i^m/d_i\neq0\).  Hence the leading coefficient of \(P\) is nonzero and \(\deg P=n\).

Conclusion.  Defining \(P\) by
\[
   P(x)\;=\;\sum_{i=0}^n\Bigl(\frac{a_i^m}{d_i}\Bigr)\,
                \prod_{\substack{0\le j\le n\\j\neq i}}(x-j),
\]
with the \(a_i\) chosen above, gives
\begin{itemize}
\item \(P(x)\in\Bbb Z[x]\),
\item \(\deg P=n\),
\item \(P(i)=a_i^m\) for \(i=0,1,\dots,n\), i.e.\ each \(P(i)\) is a perfect \(m\)th power.
\end{itemize}
This completes the proof.  ∎
```

## Reviewer Note

Misunderstands the problem statement.
