<!-- DOMAIN_BACKGROUND: /input_artifacts/background_algebra_analysis.md -->
<!-- REQUIRED: Read /input_artifacts/background_algebra_analysis.md before evaluating this proof. -->

    # proof_14

    - Problem ID: USAMO_2009_6
    - Competition: USAMO
    - Year: 2009
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 43

    ## Problem

    Let \( s_{1}, s_{2}, s_{3}, \ldots \) be an infinite, nonconstant sequence of rational numbers, meaning it is not the case that \( s_{1}=s_{2}=s_{3}=\ldots \). Suppose that \( t_{1}, t_{2}, t_{3}, \ldots \) is also an infinite, nonconstant sequence of rational numbers with the property that \((s_{i}-s_{j})(t_{i}-t_{j})\) is an integer for all \( i \) and \( j \). Prove that there exists a rational number \( r \) such that \((s_{i}-s_{j}) r\) and \((t_{i}-t_{j}) / r\) are integers for all \( i \) and \( j \).

    ## Candidate Solution Attempt

    Proof.  For any nonzero rational number \(x\) and any prime \(p\), let \(v_{p}(x)\) be the usual \(p\)-adic valuation of \(x\) (so \(v_{p}(x)\in\Bbb Z\cup\{+\infty\}\), \(v_{p}(xy)=v_{p}(x)+v_{p}(y)\), and \(x\) is a \(p\)-adic integer if and only if \(v_{p}(x)\ge0\)).  We will show that the required \(r\) can be chosen so that for every prime \(p\),
\[
v_{p}(r)\;=\;-\,\min_{i,j}v_{p}\!\bigl(s_{i}-s_{j}\bigr).
\]
Since we will see that \(\min_{i,j}v_{p}(s_{i}-s_{j})=0\) for all but finitely many \(p\), this prescription makes \(r\)
a well–defined nonzero rational number, and then one checks easily that
\[
v_{p}\!\bigl(r(s_{i}-s_{j})\bigr)
\;=\;
v_{p}(r)+v_{p}(s_{i}-s_{j})
\;\ge\;
0,
\]
and
\[
v_{p}\!\Bigl(\frac{t_{i}-t_{j}}{r}\Bigr)
\;=\;
v_{p}(t_{i}-t_{j})-v_{p}(r)
\;=\;
v_{p}(t_{i}-t_{j})+\min_{k,\ell}v_{p}(s_{k}-s_{\ell})
\;\ge\;0,
\]
so that \(r(s_{i}-s_{j})\) and \((t_{i}-t_{j})/r\) are both integers.  It remains only to check two things:

1.  For every prime \(p\), the minima
   \[
     a_{p}\;:=\;\min_{i,j}v_{p}\bigl(s_{i}-s_{j}\bigr),
     \quad
     b_{p}\;:=\;\min_{i,j}v_{p}\bigl(t_{i}-t_{j}\bigr)
   \]
   are finite integers (not \(-\infty\)), that they satisfy
   \(\,a_{p}+b_{p}\ge0\), and that \(a_{p}=0\) for all but finitely many \(p\).

2.  Defining \(v_{p}(r)=-\,a_{p}\) for each \(p\) indeed gives a rational \(r\) (i.e.\ \(v_{p}(r)=0\) for all but finitely many \(p\)).

Once these are in hand, the verification that \(r(s_{i}-s_{j})\) and \((t_{i}-t_{j})/r\) are integers is immediate from the additivity of \(v_{p}\).  We now carry out those two steps.

---

Step 1.  Bounding the \(p\)-adic minima.  

Fix a prime \(p\).  Since the sequence \((s_{i})\) is nonconstant, there exist \(i,j\) with \(s_{i}\ne s_{j}\), so \(s_{i}-s_{j}\ne0\) and \(v_{p}(s_{i}-s_{j})\) is a finite integer.  Hence
\[
  a_{p}
  \;=\;\min_{i,j}v_{p}\bigl(s_{i}-s_{j}\bigr)
  \;>\;-\infty.
\]
Similarly \(b_{p}>-\infty\).  On the other hand by hypothesis
\[
  (s_{i}-s_{j})\,(t_{i}-t_{j})
  \;=\;\text{an integer},
\]
so for every \(i,j\)
\[
  v_{p}(s_{i}-s_{j})\,+\,v_{p}(t_{i}-t_{j})
  \;=\;
  v_{p}\!\bigl((s_{i}-s_{j})(t_{i}-t_{j})\bigr)
  \;\ge\;0.
\]
Taking the minimum of the left‐hand side over all \(i,j\) gives
\[
  \min_{i,j}\bigl(v_{p}(s_{i}-s_{j})+v_{p}(t_{i}-t_{j})\bigr)
  \;\ge\;0
  \;\;\Longrightarrow\;\;
  a_{p}+b_{p}\;\ge\;0.
\]
It remains to show \(a_{p}=0\) for all but finitely many \(p\).  If \(a_{p}<0\), then \(p\) divides the denominator of some difference \(s_{i}-s_{j}\).  But then \(v_{p}(t_{i}-t_{j})\ge -\,v_{p}(s_{i}-s_{j})>0\), so \(p\) divides the numerator of that difference \(t_{i}-t_{j}\).  In particular
\[
  t_{i}\;\equiv\;t_{j}\pmod p
  \quad\Longrightarrow\quad
  t_{k}\;\equiv\;t_{j}\pmod p
  \quad\text{for all }k,
\]
because \((s_{i}-s_{j})(t_{i}-t_{j})\in\Bbb Z\) for \emph{every} \(i\), \(j\).  Hence \(t_{k}-t_{\ell}\) is divisible by \(p\) for all \(k,\ell\).  But an integer divisible by infinitely many primes must be zero.  Therefore
\[
  \bigl(t_{k}-t_{\ell}\bigr)=0
  \quad\forall\,k,\ell,
\]
contradicting the assumption that \((t_{i})\) is nonconstant.  Thus only finitely many primes \(p\) can satisfy \(a_{p}<0\), and for all the other (indeed almost all) primes \(a_{p}\ge0\), i.e.\ \(a_{p}=0\).

---

Step 2.  Defining \(r\) and checking it is rational.  

We now set
\[
  v_{p}(r)\;=\;-\,a_{p},
  \qquad
  \text{for every prime }p.
\]
Since \(a_{p}=0\) for all but finitely many \(p\), it follows that \(v_{p}(r)=0\) for all but finitely many \(p\), so the product formula in the theory of valuations shows that there is a unique nonzero rational number \(r\) with exactly these \(p\)-adic valuations.  (Concretely, if the “bad” primes \(p\) with \(a_{p}\ne0\) are \(p_{1},\dots,p_{k}\), then one takes
\[
   r\;=\;\prod_{i=1}^{k}p_{i}^{-\,a_{p_{i}}}
\]
up to an overall choice of sign.)

---

Step 3.  Verifying the integrality conditions.  

Finally, for any indices \(i,j\) and any prime \(p\),
\[
  v_{p}\!\bigl(r(s_{i}-s_{j})\bigr)
  \;=\;
  v_{p}(r)+v_{p}(s_{i}-s_{j})
  \;=\;-a_{p}+v_{p}(s_{i}-s_{j})
  \;\ge\;-a_{p}+a_{p}
  \;=\;0,
\]
so \(r(s_{i}-s_{j})\) is a \(p\)-adic integer for every \(p\), hence an (ordinary) integer.  Similarly
\[
  v_{p}\!\Bigl(\frac{t_{i}-t_{j}}{r}\Bigr)
  \;=\;
  v_{p}(t_{i}-t_{j})-v_{p}(r)
  \;=\;
  v_{p}(t_{i}-t_{j})+a_{p}
  \;\ge\;b_{p}+a_{p}
  \;\ge\;0,
\]
so \((t_{i}-t_{j})/r\) is also an integer.  This completes the proof.  ∎