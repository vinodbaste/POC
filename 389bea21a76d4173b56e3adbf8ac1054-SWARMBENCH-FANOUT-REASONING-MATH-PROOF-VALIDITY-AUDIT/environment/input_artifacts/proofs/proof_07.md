<!-- DOMAIN_BACKGROUND: /input_artifacts/background_functional_equations.md -->
<!-- REQUIRED: Read /input_artifacts/background_functional_equations.md before evaluating this proof. -->

    # proof_07

    - Problem ID: IMOSL_2010_1
    - Competition: IMOSL
    - Year: 2010
    - Level: high_school
    - Source URL: https://www.imo-official.org/
    - Dataset row index: 22

    ## Problem

    Determine all functions \( f: \mathbb{R} \rightarrow \mathbb{R} \) such that the equality

\[
f([x] y) = f(x)[f(y)]
\]

holds for all \( x, y \in \mathbb{R} \). Here, by \([x]\) we denote the greatest integer not exceeding \( x \).

    ## Candidate Solution Attempt

    Proof. Denote by \(\lfloor t\rfloor\) the greatest integer not exceeding \(t\).  Define the assertion
\[
P(x,y)\colon\quad f\bigl(\lfloor x\rfloor\,y\bigr)\;=\;f(x)\,\bigl\lfloor f(y)\bigr\rfloor,
\]
which by hypothesis holds for all real \(x,y\).

We will show that the only solutions are
\[
f(x)\equiv 0
\quad\text{and}\quad
f(x)\equiv C\quad\bigl(C\in [1,2)\bigr).
\]
It is easy to check that each of these indeed satisfies \(P(x,y)\):
– If \(f\equiv0\), then both sides of \(P(x,y)\) are zero.
– If \(f(x)\equiv C\) with \(1\le C<2\), then \(\lfloor f(y)\rfloor=\lfloor C\rfloor=1\) and both sides of \(P(x,y)\) equal \(C\).

We now prove there are no other solutions.

---

Case 1. \(\displaystyle \lfloor f(y)\rfloor=0\) for all \(y\).

Then for every \(x,y\),
\[
f\bigl(\lfloor x\rfloor\,y\bigr)
\;=\;
f(x)\,\lfloor f(y)\rfloor
\;=\;
f(x)\cdot 0
\;=\;
0.
\]
But every real \(t\) can be written as \(t=\lfloor x\rfloor\,y\), for example by choosing \(x\in(1,2)\) so \(\lfloor x\rfloor=1\) and \(y=t\).  Hence \(f(t)=0\) for all \(t\).  This is the zero solution.

---

Case 2. There exists \(y_{0}\) with \(\lfloor f(y_{0})\rfloor\neq0\).

Set
\[
c \;:=\;\lfloor f(y_{0})\rfloor\;\in\;\mathbb{Z}\setminus\{0\}.
\]
Then \(P(x,y_{0})\) gives
\[
f\bigl(\lfloor x\rfloor\,y_{0}\bigr)
\;=\;
f(x)\,c.
\]
For each integer \(k\), if \(\lfloor x\rfloor=k\) then the left–hand side is
\(f(k\,y_{0})\), a constant (independent of the choice of \(x\in[k,k+1)\)).  Hence
\[
f(x)\;=\;\frac{f(k\,y_{0})}{c}
\quad
\text{for all }x\in[k,k+1).
\]
Thus \(f\) is constant on each integer–interval \([k,k+1)\).  We may write
\[
f(x)\;=\;A_{\,\lfloor x\rfloor},
\]
where \(A_{n}\) denotes the common value of \(f\) on \([n,n+1)\).  In particular
\[
f(n)=A_{n}
\quad\text{for each }n\in\mathbb{Z}.
\]

Write also
\[
B_{n}\;:=\;\lfloor A_{n}\rfloor,
\]
so that \(\lfloor f(y)\rfloor=B_{\,\lfloor y\rfloor}\).  Substituting
\(x,y\) with \(\lfloor x\rfloor=m\in\mathbb{Z}\) and \(\lfloor y\rfloor=n\)
into the original equation \(P(x,y)\) gives
\[
f\bigl(\lfloor x\rfloor\,y\bigr)
\;=\;
A_{\,\lfloor m\,y\rfloor}
\;=\;
f(x)\,\lfloor f(y)\rfloor
\;=\;
A_{m}\,B_{n}.
\]
Hence for every pair of integers \(m,n\) and every real \(y\in[n,n+1)\),
\[
A_{\lfloor m\,y\rfloor}
\;=\;
A_{m}\,B_{n}.
\tag{*}
\]
We now extract consequences of \((*)\).

1.  Take \(m=0\).  Then \(\lfloor0\cdot y\rfloor=0\) and \((*)\) reads
   \[
   A_{0}\;=\;A_{0}\,B_{n}
   \quad\text{for all }n\in\mathbb{Z}.
   \]
   Hence for each \(n\), either \(A_{0}=0\) or \(B_{n}=1\).  Two subcases arise:

   Subcase 2.1.  \(A_{0}\neq0\).  Then \(B_{n}=1\) for every \(n\).  In particular
   \(A_{n}\in[1,2)\) for all \(n\).  Now take \(m=1\) in \((*)\).  Since
   \(\lfloor1\cdot y\rfloor=\lfloor y\rfloor=n\), \((*)\) gives
   \[
   A_{n}
   \;=\;
   A_{1}\,B_{n}
   \;=\;
   A_{1}\cdot1
   \;=\;
   A_{1},
   \]
   so \(A_{n}=A_{1}\) for every \(n\).  Thus \(f(x)=A_{1}\equiv C\), with
   \(1\le C<2\).  This yields the family of constant solutions
   \(f(x)\equiv C\in[1,2)\).

   Subcase 2.2.  \(A_{0}=0\).  Then \(B_{0}=0\).  Next take \(m=1\) in \((*)\):
   since \(\lfloor1\cdot y\rfloor=n\), one gets
   \[
   A_{n}
   \;=\;
   A_{1}\,B_{n}
   \quad\text{for all }n\in\mathbb{Z}.
   \]
   In particular, for \(n=1\),
   \(
     A_{1}=A_{1}\,B_{1},
   \)
   so either \(A_{1}=0\) or \(B_{1}=1\).

   –  If \(A_{1}=0\), then \(A_{n}=A_{1}B_{n}=0\) for all \(n\), so
      \(f\equiv0\).

   –  If \(A_{1}\neq0\), then \(B_{1}=1\), so \(A_{1}\in[1,2)\).  Finally
      take \(m=2\) and \(n=0\) in \((*)\).  For \(y\in[0,1)\), \(\lfloor2y\rfloor\)
      takes the two values \(0\) and \(1\).  The case \(\lfloor2y\rfloor=1\)
      forces
      \[
      A_{1}
      \;=\;
      A_{2}\,B_{0}
      \;=\;
      A_{2}\cdot0
      \;=\;
      0,
      \]
      a contradiction to \(A_{1}\ge1\).  Thus this subcase is impossible.

In every branch of Case 2 other than those already listed, we arrive either at
the constant solution \(f\equiv0\) or at the constant solutions \(f\equiv C\)
with \(1\le C<2\).  No other behavior is possible.

Combining Cases 1 and 2, we conclude that the only real–valued functions
\(f\) on \(\mathbb{R}\) satisfying
\(\;f(\lfloor x\rfloor\,y)=f(x)\,\lfloor f(y)\rfloor\;\) for all \(x,y\) are

\[
\boxed{%
f(x)\equiv 0
\quad\text{or}\quad
f(x)\equiv C\text{ with }1\le C<2.
}
\] 
This completes the proof.  \(\blacksquare\)