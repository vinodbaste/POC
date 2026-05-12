# artifact_08

Competition: BMOSL  
Problem ID: BMOSL_2017_5  
Year: 2017

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Consider integers \( m \geq 2 \) and \( n \geq 1 \). Show that there is a polynomial \( P(x) \) of degree equal to \( n \) with integer coefficients such that \( P(0), P(1), \ldots, P(n) \) are all perfect powers of \( m \).

## Candidate Excerpts

### Option A

```text
Here is a self‐contained proof.
```

### Option B

```text
Proof.  Fix integers \(m\ge2\) and \(n\ge1\).  We will exhibit explicitly a polynomial  
\[
P(x)\;=\;\sum_{k=0}^n m^{A_k}\,L_k(x)
\]
of degree exactly \(n\) with integer coefficients, where each \(P(k)=m^{A_k}\) is a power of \(m\).  Here \(L_0,\dots,L_n\) are the usual Lagrange‐basis polynomials for the nodes \(0,1,\dots,n\).
```

### Option C

```text
2.  (Lagrange interpolation.)  
For each \(k=0,\dots,n\) define the polynomial
\[
L_k(x)
\;=\;
\prod_{\substack{0\le j\le n\\ j\neq k}}
\frac{x-j}{\,k-j\,}\,.
\]
It is well‐known that \(L_k\) has degree \(n\) and satisfies
\[
L_k(j)=
\begin{cases}
1,&j=k,\\
0,&j\ne k,
\end{cases}
\quad j=0,1,\dots,n,
\]
and that \(\{L_k\}_{k=0}^n\) form a basis for the space of all polynomials of degree \(\le n\).  Hence the unique polynomial of degree at most \(n\) which takes the values \(m^{A_k}\) at \(x=k\) is
\[
P(x)
\;=\;
\sum_{k=0}^n m^{A_k}\,L_k(x).
\]
Clearly \(P(k)=m^{A_k}\) for \(k=0,1,\dots,n\).
```

### Option D

```text
1.  (Choice of exponents \(A_k\).)  
Factorize  
\[
m \;=\;\prod_{i=1}^r p_i^{\,a_i}
\]
into primes.  For each \(i\) let  
\[
M_i \;=\;v_{p_i}\bigl((n!)^2\bigr)\,,
\]
so that \((n!)^2\) is divisible exactly by \(\prod_i p_i^{M_i}\).  Since \(v_{p_i}(m^{C})=C\,a_i\), we see that if
\[
C\;\ge\;\max_{1\le i\le r}\Bigl\lceil \tfrac{M_i}{a_i}\Bigr\rceil
\]
then
\[
m^C\quad\text{is divisible by}\quad(n!)^2
\;\ge\;k!\,(n-k)!
\quad\text{for every }0\le k\le n.
\]
Fix such a \(C\), and now set
\[
A_k \;=\;C+k,
\qquad k=0,1,\dots,n.
\]
Then for each \(k\),
\[
k!\,(n-k)!\;\bigm|\; (n!)^2
\;\bigm|\;m^C
\;\bigm|\;m^{A_k}\,.
\]
In particular 
\[
\frac{m^{A_k}}{\,k!\,(n-k)!}\;\in\;\Bbb Z.
\]
```

## Full Candidate Proof

```text
Here is a self‐contained proof.  

Proof.  Fix integers \(m\ge2\) and \(n\ge1\).  We will exhibit explicitly a polynomial  
\[
P(x)\;=\;\sum_{k=0}^n m^{A_k}\,L_k(x)
\]
of degree exactly \(n\) with integer coefficients, where each \(P(k)=m^{A_k}\) is a power of \(m\).  Here \(L_0,\dots,L_n\) are the usual Lagrange‐basis polynomials for the nodes \(0,1,\dots,n\).  

1.  (Choice of exponents \(A_k\).)  
Factorize  
\[
m \;=\;\prod_{i=1}^r p_i^{\,a_i}
\]
into primes.  For each \(i\) let  
\[
M_i \;=\;v_{p_i}\bigl((n!)^2\bigr)\,,
\]
so that \((n!)^2\) is divisible exactly by \(\prod_i p_i^{M_i}\).  Since \(v_{p_i}(m^{C})=C\,a_i\), we see that if
\[
C\;\ge\;\max_{1\le i\le r}\Bigl\lceil \tfrac{M_i}{a_i}\Bigr\rceil
\]
then
\[
m^C\quad\text{is divisible by}\quad(n!)^2
\;\ge\;k!\,(n-k)!
\quad\text{for every }0\le k\le n.
\]
Fix such a \(C\), and now set
\[
A_k \;=\;C+k,
\qquad k=0,1,\dots,n.
\]
Then for each \(k\),
\[
k!\,(n-k)!\;\bigm|\; (n!)^2
\;\bigm|\;m^C
\;\bigm|\;m^{A_k}\,.
\]
In particular 
\[
\frac{m^{A_k}}{\,k!\,(n-k)!}\;\in\;\Bbb Z.
\]

2.  (Lagrange interpolation.)  
For each \(k=0,\dots,n\) define the polynomial
\[
L_k(x)
\;=\;
\prod_{\substack{0\le j\le n\\ j\neq k}}
\frac{x-j}{\,k-j\,}\,.
\]
It is well‐known that \(L_k\) has degree \(n\) and satisfies
\[
L_k(j)=
\begin{cases}
1,&j=k,\\
0,&j\ne k,
\end{cases}
\quad j=0,1,\dots,n,
\]
and that \(\{L_k\}_{k=0}^n\) form a basis for the space of all polynomials of degree \(\le n\).  Hence the unique polynomial of degree at most \(n\) which takes the values \(m^{A_k}\) at \(x=k\) is
\[
P(x)
\;=\;
\sum_{k=0}^n m^{A_k}\,L_k(x).
\]
Clearly \(P(k)=m^{A_k}\) for \(k=0,1,\dots,n\).

3.  (Integrality of the coefficients of \(P\).)  
Observe that
\[
\prod_{j\ne k}(k-j)
\;=\;
\bigl(-1\bigr)^{\,n-k}\;k!\;(n-k)!.
\]
Hence
\[
L_k(x)
\;=\;
(-1)^{\,n-k}\,
\frac{\displaystyle\prod_{j\ne k}(x-j)}
{k!\,(n-k)!}
\]
and therefore
\[
m^{A_k}\,L_k(x)
\;=\;
(-1)^{\,n-k}\,
\Bigl(\tfrac{m^{A_k}}{\,k!\,(n-k)!}\Bigr)
\;\prod_{j\ne k}(x-j).
\]
Since we arranged \(k!\,(n-k)!\mid m^{A_k}\), the rational number
\(\tfrac{m^{A_k}}{k!\,(n-k)!}\) is in fact an integer, and of course \(\prod_{j\ne k}(x-j)\) has integer coefficients.  Hence each term \(m^{A_k}L_k(x)\) lies in \(\Bbb Z[x]\), and so does \(P(x)\).  

4.  (Degree of \(P\) is exactly \(n\).)  
Finally we check that \(P\) really has degree \(n\) (and not lower).  A standard fact about the leading coefficient of a Lagrange‐interpolant is
\[
\deg L_k \;=\;n,
\qquad
\text{and}
\qquad
\text{Coeff}_{x^n}(L_k)
\;=\;
\frac{1}{\prod_{j\ne k}(k-j)}
\;=\;
\frac{(-1)^{\,n-k}}{\,k!\,(n-k)!}\,.
\]
Hence the leading coefficient of \(P\) is
\[
a_n
\;=\;
\sum_{k=0}^n
m^{A_k}\;\frac{(-1)^{\,n-k}}{\,k!\,(n-k)!}
\;=\;
m^C\;\sum_{k=0}^n
\frac{(-1)^{\,n-k}\,m^k}{\,k!\,(n-k)!}
\;=\;
\frac{m^C}{\,n!}\;(m-1)^n,
\]
where in the last step we used the binomial expansion
\(\displaystyle\sum_{k=0}^n(-1)^{n-k}\binom nk m^k=(m-1)^n.\)
Since \(m\ge2\) and \(n!\) divides \(m^C\) by construction, we see
\(\,a_n=\tfrac{m^C}{n!}(m-1)^n\in\Bbb Z\) and \(a_n\neq0\).  Thus \(\deg P=n\).  

Conclusion.  The polynomial
\[
P(x)
\;=\;
\sum_{k=0}^n m^{C+k}\,
\prod_{\substack{0\le j\le n\\j\neq k}}
\frac{x-j}{\,k-j\,}
\]
has integer coefficients, degree \(n\), and satisfies
\[
P(k)\;=\;m^{C+k}
\quad\text{for }k=0,1,\dots,n,
\]
where each \(m^{C+k}\) is manifestly a perfect power of \(m\).  This completes the proof.  ∎
```

## Reviewer Note

Incorrect implication.
