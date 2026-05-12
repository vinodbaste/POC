<!-- DOMAIN_BACKGROUND: /input_artifacts/background_algebra_analysis.md -->
<!-- REQUIRED: Read /input_artifacts/background_algebra_analysis.md before evaluating this proof. -->

    # proof_18

    - Problem ID: IMOSL_2020_5
    - Competition: IMOSL
    - Year: 2020
    - Level: high_school
    - Source URL: https://www.imo-official.org/
    - Dataset row index: 67

    ## Problem

    A magician intends to perform the following trick. She announces a positive integer \( n \), along with \( 2n \) real numbers \( x_1 < \ldots < x_{2n} \), to the audience. A member of the audience then secretly chooses a polynomial \( P(x) \) of degree \( n \) with real coefficients, computes the \( 2n \) values \( P(x_1), \ldots, P(x_{2n}) \), and writes down these \( 2n \) values on the blackboard in non-decreasing order. After that, the magician announces the secret polynomial to the audience.

Can the magician find a strategy to perform such a trick?

    ## Candidate Solution Attempt

    Here is a self‐contained proof that no matter how the magician chooses the points \(x_{1}<\cdots<x_{2n}\), the audience has a way to produce two distinct degree-\(n\) polynomials whose values on those \(2n\) points, once sorted, agree.  Hence the magician cannot succeed.

---

Proof.

Suppose the magician fixes real numbers
\[
x_{1}<x_{2}<\cdots<x_{2n}.
\]
We will show that the audience can find two different polynomials
\[
Q(x)=a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots+a_{0},
\quad
P(x)=-\,Q(x),
\]
both of degree exactly \(n\), such that the multiset of values
\(\{P(x_{1}),\dots,P(x_{2n})\}\) coincides with
\(\{Q(x_{1}),\dots,Q(x_{2n})\}\).  In particular then the sorted lists of
\(\{P(x_{i})\}\) and \(\{Q(x_{i})\}\) are identical, even though
\(P\ne Q\).  That contradicts any putative strategy of the magician.

1.  Construction of a fixed‐point‐free involution.  
    Since \(2n\) is even, we may partition the index set
    \(\{1,2,\dots,2n\}\) into \(n\) disjoint pairs
    \[
       \bigl\{\,\{i_{1},j_{1}\},\;\{i_{2},j_{2}\},\;\dots,\;\{i_{n},j_{n}\}\bigr\},
    \]
    and define a permutation \(\sigma\) of order two by
    \(\sigma(i_{k})=j_{k}\), \(\sigma(j_{k})=i_{k}\).  Equivalently,
    \(\sigma\) is a perfect matching on the complete graph \(K_{2n}\)
    with no fixed points.  Such a perfect matching always exists: one
    may pick any two vertices and match them, remove them, and continue
    inductively.

2.  The linear constraints on \(Q\).  
    We now seek a real polynomial
    \[
       Q(x)=a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots+a_{0}
    \]
    satisfying, for each of our \(n\) pairs \(\{i_{k},j_{k}\}\),
    \[
      Q\bigl(x_{i_{k}}\bigr)\;+\;Q\bigl(x_{j_{k}}\bigr)\;=\;0.
    \]
    Writing out
    \[
      Q(x_{i_{k}})=\sum_{m=0}^n a_{m}\,x_{i_{k}}^{m},
      \quad
      Q(x_{j_{k}})=\sum_{m=0}^n a_{m}\,x_{j_{k}}^{m},
    \]
    each of these \(n\) conditions is a homogeneous linear equation in
    the \(n+1\) unknowns \(a_{0},a_{1},\dots,a_{n}\).  Hence the
    solution space has dimension at least
    \((n+1)-n=1\), so there exists a nonzero polynomial \(Q\) of degree
    _at most_ \(n\) satisfying all these equations.

3.  Ensuring \(\deg Q=n\).  
    We must check that among those solutions one can find one whose
    leading coefficient \(a_{n}\) is not zero, so that
    \(\deg Q=n\).  If _every_ solution had \(a_{n}=0\), then the entire
    solution space would lie in the hyperplane
    \(\{\,a_{n}=0\}\subset\Bbb R^{n+1}\).  But that hyperplane is cut
    out by the single linear functional
    \((a_{0},\dots,a_{n})\mapsto a_{n}\).  For the solution space to lie
    inside it, that functional would have to vanish on every solution;
    equivalently each of the \(n\) row‐vectors
    \[
      \bigl(x_{i_{k}}^{0}+x_{j_{k}}^{0},\;x_{i_{k}}^{1}+x_{j_{k}}^{1},\;\dots,\;x_{i_{k}}^{n}+x_{j_{k}}^{n}\bigr)
    \]
    would have to be orthogonal to the vector
    \((0,\dots,0,1)\in\Bbb R^{n+1}\).  But that would force
    \(x_{i_{k}}^{n}+x_{j_{k}}^{n}=0\) for _every_ \(k\).  Since
    \(x_{i_{k}}\neq x_{j_{k}}\), that cannot happen for _all_ pairs
    unless each pair is of the form \(\{a,-a\}\) with \(n\) odd—and
    even then it can happen only for those _specific_ pairs \(\{a,-a\}\).
    In _any_ case one checks directly that if
    \(x_{i_{k}}^{n}+x_{j_{k}}^{n}=0\) then the \(k\)th equation does
    _not_ involve \(a_{n}\) at all.  Hence in _every_ case there is at
    least one equation whose coefficient of \(a_{n}\) is nonzero, or
    else no equation involves \(a_{n}\), and so \(a_{n}\) is _free_.  In
    either event the solution space is _not_ contained in \(\{a_{n}=0\}\),
    so we may choose one solution with \(a_{n}\neq0\).  Thus
    \(\deg Q=n\).

4.  Defining \(P\) and checking the trick fails.  
    Now set
    \[
      P(x)\;=\;-\,Q(x).
    \]
    Clearly \(\deg P=n\) and \(P\neq Q\).  But for each matched pair
    \(\{i_{k},j_{k}\}\) we have
    \[
      P(x_{i_{k}})= -\,Q(x_{i_{k}})
      =\;Q(x_{j_{k}}),
      \quad
      P(x_{j_{k}})= -\,Q(x_{j_{k}})
      =\;Q(x_{i_{k}}).
    \]
    Hence the multiset of values
    \(\{P(x_{1}),\dots,P(x_{2n})\}\) coincides _exactly_ with
    \(\{Q(x_{1}),\dots,Q(x_{2n})\}\).  In particular, once one writes
    those \(2n\) numbers in non‐decreasing order, the two lists agree
    term by term.  The magician, seeing only that sorted list, cannot
    tell whether it came from \(P\) or from \(Q\).  Therefore no choice
    of the \(x_{i}\) can force the map
    \(\{\,\text{degree-}n\text{ polynomials}\}\to
     \{\text{sorted }2n\text{-tuples}\}\)
    to be injective.  The trick is impossible.

∎

Remark.  The heart of the construction is the observation that on any
set of \(2n\) distinct reals one can impose \(n\) linear _homogeneous_
constraints
\[
   Q(x_{i})+Q(x_{j})=0
\]
and still leave exactly a one‐dimensional family of degree‐\(n\)
solutions.  Taking \(P=-Q\) then forces
\(\{P(x_{i})\}=\{Q(x_{i})\}\) as multisets, so the audience can always
produce two distinct “secret” polynomials with identical sorted lists
of values.  As soon as that is possible, the magician can never learn
which one was chosen.