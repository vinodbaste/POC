<!-- DOMAIN_BACKGROUND: /input_artifacts/background_algebra_analysis.md -->
<!-- REQUIRED: Read /input_artifacts/background_algebra_analysis.md before evaluating this proof. -->

    # proof_20

    - Problem ID: USAMO_2019_6
    - Competition: USAMO
    - Year: 2019
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 94

    ## Problem

    Find all polynomials \( P \) with real coefficients such that
\[
\frac{P(x)}{yz} + \frac{P(y)}{zx} + \frac{P(z)}{xy} = P(x-y) + P(y-z) + P(z-x)
\]
for all nonzero real numbers \( x, y, z \) obeying \( 2xyz = x+y+z \).

    ## Candidate Solution Attempt

    Proof.  Denote by \(S_1=x+y+z\), \(S_2=xy+yz+zx\), and \(S_3=xyz\).  The given condition is

\[
\frac{P(x)}{yz}+\frac{P(y)}{zx}+\frac{P(z)}{xy}
\;=\;
P(x-y)+P(y-z)+P(z-x),
\]
for all nonzero real \(x,y,z\) satisfying
\[
2\,x y z \;=\; x+y+z,
\]
i.e.\ \(2S_3=S_1\).

Step 1.  Eliminate the denominators.  Multiply both sides of the functional equation by \(xyz=S_3\).  On the left,
\[
xyz\Bigl(\tfrac{P(x)}{yz}+\tfrac{P(y)}{zx}+\tfrac{P(z)}{xy}\Bigr)
\;=\;
x\,P(x)+y\,P(y)+z\,P(z).
\]
On the right we get
\[
xyz\bigl(P(x-y)+P(y-z)+P(z-x)\bigr)
\;=\;
S_3\bigl(P(x-y)+P(y-z)+P(z-x)\bigr).
\]
Hence the equation becomes
\[
xP(x)+yP(y)+zP(z)
\;=\;
S_3\bigl(P(x-y)+P(y-z)+P(z-x)\bigr).
\]
Now use \(S_3=\tfrac12S_1\).  This gives the equivalent form
\[
\boxed{%
2\bigl(xP(x)+yP(y)+zP(z)\bigr)
\;=\;
\bigl(x+y+z\bigr)\bigl(P(x-y)+P(y-z)+P(z-x)\bigr).
}
\tag{1}
\]

From now on \((x,y)\) will be arbitrary reals with \(2xy\neq1\), and we set
\[
z \;=\;\frac{x+y}{\,2xy-1\,},
\]
so that \(2xyz=x+y+z\) holds and \(z\neq0\).  Thus equation (1) is a polynomial identity in the two independent variables \(x,y\), away from the locus \(2xy=1\).  By continuity it extends to all real \(x,y\).  In particular it is an identity of two-variable polynomials once we clear the denominator \((2xy-1)\).

Step 2.  Degree bound \(\deg P\le2\).  Write
\[
P(t)=a_n\,t^n+a_{n-1}t^{n-1}+\cdots+a_0,
\qquad
a_n\neq0.
\]
We shall compare the two sides of (1) in the regime
\[
y\;\longrightarrow\;\infty,
\quad
x\;\text{fixed},
\quad
z=\frac{x+y}{2xy-1}\;\longrightarrow\;\frac1{2x}.
\]
We expand both sides in powers of \(y\).

(2 A) Left–hand side of (1):
\[
2\bigl(xP(x)+yP(y)+zP(z)\bigr)
=
2\bigl(y\,(a_ny^n+a_{n-1}y^{n-1}+\cdots)+O(1)\bigr)
=
2a_n\,y^{\,n+1}+2a_{n-1}\,y^n+O(y^{n-1}).
\]

(2 B) Right–hand side of (1):
\(
S_1=x+y+z=y+O(1),
\)
and
\[
P(x-y)
=a_n(-y+x)^n+\cdots
=a_n(-1)^n y^n + a_n\,n x(-1)^{n-1}y^{n-1} + a_{n-1}(-1)^{n-1}y^{n-1}
   +O(y^{n-2}),
\]
\[
P(y-z)
=a_n(y-\tfrac1{2x}+O(1/y))^n+\cdots
=a_n\,y^n -a_n\,n\Bigl(\tfrac1{2x}\Bigr)y^{n-1} + a_{n-1}y^{n-1} +O(y^{n-2}),
\]
\[
P(z-x)=O(1).
\]
Hence
\[
P(x-y)+P(y-z)+P(z-x)
=\,a_n\bigl((-1)^n+1\bigr)\,y^n
\;+\;
\Bigl[a_n\,n(-1)^{n-1}x+a_{n-1}(-1)^{n-1}
      +a_{n-1}-a_n\,\tfrac{n}{2x}\Bigr]y^{n-1}
\;+\;
O(y^{n-2}).
\]
Since \(n\) must be even for the leading \(y^{n+1}\)-terms to match (see below), we set \((-1)^n=1\).  Thus
\[
P(x-y)+P(y-z)+P(z-x)
=2a_n\,y^n
\;-\;
a_n\,n\Bigl(x+\tfrac1{2x}\Bigr)\,y^{n-1}
\;+\;
O(y^{n-2}).
\]
Multiplying by \(S_1=y+O(1)\) gives
\[
\text{RHS of (1)}
=
2a_n\,y^{n+1}
+\;a_n\Bigl[2\bigl(x+\tfrac1{2x}\bigr)-n\bigl(x+\tfrac1{2x}\bigr)\Bigr]y^n
+O(y^{n-1})
\]
\[
\qquad
=
2a_n\,y^{n+1}
+\;a_n\,(2-n)\Bigl(x+\tfrac1{2x}\Bigr)\,y^n
+O(y^{n-1}).
\]

Comparison of coefficients in the expansion of
LHS\(\;\)=\(\)RHS as \(y\to\infty\) gives two constraints:

(i)  Coefficient of \(y^{n+1}\):
\[
2a_n \;=\;2a_n
\;\Longrightarrow\;
\text{(no condition).}
\]

(ii)  Coefficient of \(y^n\):
\[
2a_{n-1}
\;=\;
a_n\,(2-n)\Bigl(x+\tfrac1{2x}\Bigr)
\quad\text{for all real }x\neq0.
\]
The left side is a constant (independent of \(x\)), while the right side depends nontrivially on \(x\) unless
\[
2-n=0
\quad\Longrightarrow\quad
n=2,
\]
or else \(a_n=0\).  Since by definition \(a_n\neq0\), we conclude
\[
\deg P \;=\;n=2.
\]

Step 3.  Determine the unique quadratic.  Write
\[
P(t)=a\,t^2+b\,t+c.
\]
We substitute into the simplified identity (1):
\[
2\bigl(xP(x)+yP(y)+zP(z)\bigr)
=
(x+y+z)\bigl(P(x-y)+P(y-z)+P(z-x)\bigr),
\]
and we also use the shorthand
\[
S_1=x+y+z,\quad
S_2=xy+yz+zx,\quad
S_3=xyz,\quad
S_1=2S_3.
\]
On the one hand,
\[
xP(x)+yP(y)+zP(z)
=
a\,(x^3+y^3+z^3)
+ b\,(x^2+y^2+z^2)
+ c\,(x+y+z).
\]
We recall the standard symmetric‐sum identities
\[
x^2+y^2+z^2=S_1^2-2S_2,
\quad
x^3+y^3+z^3=S_1^3-3S_1S_2+3S_3,
\]
and we plug \(S_3=\tfrac12S_1\).  A short computation gives
\[
\text{LHS of (1)}
=2\Bigl[a\,(S_1^3-3S_1S_2+3S_3)
      +b\,(S_1^2-2S_2)
      +c\,S_1\Bigr]
\;=\;
2aS_1^3-6aS_1S_2+6aS_3
+2bS_1^2-4bS_2+2cS_1.
\]
Since \(S_3=\tfrac12S_1\), this becomes
\[
2aS_1^3-6aS_1S_2+3aS_1
+2bS_1^2-4bS_2+2cS_1.
\]

On the other hand,
\[
P(x-y)+P(y-z)+P(z-x)
=
a\bigl[(x-y)^2+(y-z)^2+(z-x)^2\bigr]
+ b\bigl[(x-y)+(y-z)+(z-x)\bigr]
+3c.
\]
But \((x-y)+(y-z)+(z-x)=0\), and
\[
(x-y)^2+(y-z)^2+(z-x)^2
=2\bigl(x^2+y^2+z^2-xy-yz-zx\bigr)
=2\bigl(S_1^2-3S_2\bigr).
\]
Hence
\[
P(x-y)+P(y-z)+P(z-x)
=2a\,(S_1^2-3S_2)+3c,
\]
and multiplying by \(S_1\) gives
\[
\text{RHS of (1)}
=S_1\bigl[2a(S_1^2-3S_2)+3c\bigr]
=2aS_1^3-6aS_1S_2+3cS_1.
\]

Equating LHS and RHS of (1) we get
\[
\bigl(2aS_1^3-6aS_1S_2+3aS_1+2bS_1^2-4bS_2+2cS_1\bigr)
\;=\;
\bigl(2aS_1^3-6aS_1S_2+3cS_1\bigr).
\]
Canceling the common terms \(2aS_1^3-6aS_1S_2\), this reduces to
\[
3aS_1+2bS_1^2-4bS_2+2cS_1
\;=\;
3cS_1.
\]
Again use \(S_2\) and \(S_1\) as essentially independent (varying over infinitely many triples), or substitute \(S_1=2S_3\) if one likes; in either case the identity forces the coefficients of the independent symmetric polynomials \(S_1^2,\,S_2,\,S_1\) to vanish.  In particular the coefficient of \(S_1^2\) is \(2b\), so
\[
b=0.
\]
Then the remaining terms give
\[
(3a+2c)S_1=3cS_1
\quad\Longrightarrow\quad
3a+2c=3c
\quad\Longrightarrow\quad
c=3a.
\]
Thus
\[
P(t)=a\,t^2+0\cdot t +3a
\;=\;
a\bigl(t^2+3\bigr).
\]

Step 4.  Verification.  Finally one checks by a direct symmetric‐sum computation (or reuses the above expansions) that for
\[
P(t)=a\,(t^2+3)
\]
the original equation indeed holds for every nonzero real \(x,y,z\) with \(2xyz=x+y+z\).  Hence the full solution set is
\[
\boxed{%
P(t)=k\,(t^2+3),
\quad
k\in\Bbb R,
}
\]
which of course includes the zero polynomial as the special case \(k=0\).  No other real‐coefficient polynomial satisfies the given identity.  This completes the proof.  ∎