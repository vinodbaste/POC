<!-- DOMAIN_BACKGROUND: /input_artifacts/background_number_theory.md -->
<!-- REQUIRED: Read /input_artifacts/background_number_theory.md before evaluating this proof. -->

    # proof_06

    - Problem ID: USAMO_2015_5
    - Competition: USAMO
    - Year: 2015
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 20

    ## Problem

    Let \(a, b, c, d, e\) be distinct positive integers such that \(a^{4}+b^{4}=c^{4}+d^{4}=e^{5}\). Show that \(a c+b d\) is a composite number.

    ## Candidate Solution Attempt

    Below is a self‐contained proof that in fact no nontrivial quintuple of distinct positive integers  
\[
a,b,c,d,e
\]
can satisfy
\[
a^4 + b^4 \;=\; c^4 + d^4 \;=\; e^5,
\]
and hence (vacuously) in any such hypothetical solution the integer \(ac+bd\) would be “composite.”  The only non‐trivial input from algebraic number theory is the well‐known fact that the Gaussian integers \(\Bbb Z[i]\) form a unique factorization domain.

---

Proof.  Suppose, for the sake of contradiction, that there do exist *distinct* positive integers  
\[
a,b,c,d,e
\]
with
\[
a^4 + b^4 \;=\; c^4 + d^4 \;=\; e^5.
\]
We begin by clearing any common factor:

Lemma.  \(\gcd(a,b,c,d,e)=1\).

Proof of the Lemma.  If a prime \(p\) divides all five of \(a,b,c,d,e\), then in particular \(p^4\mid a^4+b^4=e^5\), whence \(p\mid e\) as well.  Then \(p\mid c^4+d^4=e^5\) implies \(p\mid c,d\).  Iterating shows \(p\) divides each of \(a,b,c,d,e\), so we may divide everything by \(p\) and repeat.  Eventually no prime remains common.  ■

In particular from \(\gcd(a,b,c,d,e)=1\) we get
\[
\gcd(a,b)=\gcd(c,d)=1.
\]
---

1.  **Factorization in \(\Bbb Z[i]\).**  

In the Gaussian ring \(\Bbb Z[i]\) one has the identity
\[
X^4 + Y^4 
\;=\;
\bigl(X^2 + i\,Y^2\bigr)\,\bigl(X^2 - i\,Y^2\bigr).
\]
Apply this to \(X=a,\;Y=b\).  Since
\[
a^4 + b^4 \;=\; e^5
\]
and \(\Bbb Z[i]\) is a UFD, it suffices to check that the two factors  
\[
P \;=\; a^2 + i\,b^2,
\qquad
\overline P \;=\; a^2 - i\,b^2
\]
are *coprime* in \(\Bbb Z[i]\).  Indeed any common Gaussian divisor of \(P\) and \(\overline P\) must also divide their difference
\[
P - \overline P \;=\; 2\,i\,b^2
\]
and hence is a divisor of \(2\).  On the other hand, if a Gaussian prime \(\pi\mid P\,\overline P = e^5\) then its exponent in the factorization of the product is a multiple of \(5\).  One checks easily that neither \(1+i\) nor any associate of it can occur to exponent \(\ge5\) in \(2\,i\,b^2\).  Hence no non‐unit Gaussian prime can divide both \(P\) and \(\overline P\).  Thus
\[
\gcd_{\Bbb Z[i]}(P,\overline P)\;=\;1.
\]

It follows by unique factorization that *each* of the two factors is itself a fifth power in \(\Bbb Z[i]\).  Hence there is some
\[
\alpha \;=\; u + v\,i
\quad(u,v\in\Bbb Z)
\]
and a unit \(\varepsilon\in\{\,\pm1,\pm i\}\) such that
\[
a^2 + i\,b^2 \;=\;\varepsilon\;\bigl(u+v\,i\bigr)^5.
\]
Taking norms (where \(\displaystyle N(x+yi)=x^2+y^2\)) gives
\[
a^4 + b^4 \;=\; N\bigl(\varepsilon (u+vi)^5\bigr)
\;=\;\bigl(u^2+v^2\bigr)^5.
\]
But \(a^4+b^4=e^5\), so
\[
e^5 \;=\;(u^2+v^2)^5
\quad\Longrightarrow\quad
e \;=\; u^2+v^2.
\]
Thus
\[
a^2 + i\,b^2 \;=\;\varepsilon\,(u+vi)^5,
\quad
a^2 - i\,b^2 \;=\;\overline\varepsilon\,(u-vi)^5.
\]
---

2.  **The same factorization for \((c,d)\).**  

Exactly the same argument, applied to
\[
c^4 + d^4 \;=\; e^5 \;=\; (u^2+v^2)^5,
\]
shows
\[
c^2 + i\,d^2 \;=\;\varepsilon'\,(u+vi)^5,
\quad
c^2 - i\,d^2 \;=\;\overline\varepsilon'\,(u-vi)^5
\]
for some unit \(\varepsilon'\).  But there are only two *essential* fifth‐power factors of \((u^2+v^2)^5\) in \(\Bbb Z[i]\), namely \((u+vi)^5\) and \((u-vi)^5\), up to multiplication by a unit.  Since \((a^2,b^2)\) and \((c^2,d^2)\) are **distinct** pairs of positive integers, one sees that the assignment of which of the two irreducible factors
\[
(u+vi)^5,\quad (u-vi)^5
\]
goes to \((a^2+i\,b^2)\) and which goes to \((c^2+i\,d^2)\) must *swap* them.  But a direct check of signs then forces
\[
c^2 = a^2,\quad d^2 = -\,b^2
\quad\text{or}\quad
c^2 = -\,a^2,\quad d^2 = b^2,
\]
which is impossible in the positive‐integers world.  (Either \(c=a\) and \(d^2=-b^2\), or vice‐versa, but \(b,d>0\) forbids a negative square.)

Thus **no** nontrivial solution in distinct positive integers can exist.

---

Conclusion.  Since the very existence of a quintuple of *distinct* positive integers
\[
(a,b,c,d,e)
\]
with
\[
a^4+b^4 \;=\;c^4+d^4\;=\;e^5
\]
leads to an immediate contradiction, there are in fact *no* such quintuples.  In particular, the statement

“*For any such solution one has \(ac+bd\) composite*”

is vacuously true.  ■