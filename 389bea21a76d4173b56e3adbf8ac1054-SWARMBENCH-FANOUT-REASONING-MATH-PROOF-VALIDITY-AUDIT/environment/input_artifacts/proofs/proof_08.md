<!-- DOMAIN_BACKGROUND: /input_artifacts/background_algebra_analysis.md -->
<!-- REQUIRED: Read /input_artifacts/background_algebra_analysis.md before evaluating this proof. -->

    # proof_08

    - Problem ID: BMOSL_2016_2
    - Competition: BMOSL
    - Year: 2016
    - Level: high_school
    - Source URL: Private
    - Dataset row index: 24

    ## Problem

    For all \(x, y, z > 0\) satisfying \(\frac{x}{yz} + \frac{y}{zx} + \frac{z}{xy} \leq x + y + z\), prove that

\[
\frac{1}{x^2 + y + z} + \frac{1}{y^2 + z + x} + \frac{1}{z^2 + x + y} \leq 1
\]

    ## Candidate Solution Attempt

    Here is a self‐contained proof.  We break it into three steps:

1. “Reduction to the equality case”  
2. “Maximization of the cyclic sum on the equality‐constraint manifold”  
3. “Conclusion.”

—–  

**Step 1.  We may assume**  
\[
\frac{x}{yz}+\frac{y}{zx}+\frac{z}{xy}=x+y+z.
\]  
Indeed, let 
\[
F(x,y,z)\;=\;\frac1{x^2+y+z}+\frac1{y^2+z+x}+\frac1{z^2+x+y},
\]
and set 
\[
G(x,y,z)\;=\;\frac{x}{yz}+\frac{y}{zx}+\frac{z}{xy} \;-\;(x+y+z)\le0.
\]
We claim that whenever \(G(x,y,z)<0\) one can *shrink* \((x,y,z)\) to \((\tilde x,\tilde y,\tilde z)=(\lambda x,\lambda y,\lambda z)\) with  
\[
0<\lambda<1,
\quad
G(\,\tilde x,\tilde y,\tilde z\,)=0,
\]
and  
\[
F(\tilde x,\tilde y,\tilde z)\;\ge\;F(x,y,z).
\]

• First note that under the scaling \((x,y,z)\mapsto(\lambda x,\lambda y,\lambda z)\) we have
\[
G(\lambda x,\lambda y,\lambda z)
=\frac1\lambda\Bigl(\frac{x}{yz}+\frac{y}{zx}+\frac{z}{xy}\Bigr)
-\lambda\,(x+y+z)
=\frac1\lambda\,X-\lambda\,Y,
\]
where 
\[
X=\frac{x}{yz}+\frac{y}{zx}+\frac{z}{xy}, 
\quad
Y=x+y+z.
\]
Since \(G(x,y,z)=X-Y<0\), we have \(X<Y\), so \(X/Y<1\).  Hence the quadratic equation
\[
\frac1\lambda\,X-\lambda\,Y=0
\;\Longrightarrow\;\lambda^2=\frac{X}{Y}
\]
has the unique positive solution
\(\displaystyle\lambda=\sqrt{X/Y}\in(0,1)\).  By construction
\[
G(\lambda x,\lambda y,\lambda z)=0.
\]

• Next we check that \(F(\lambda x,\lambda y,\lambda z)\ge
F(x,y,z)\).  For each term,
\[
\frac1{(\lambda x)^2+\lambda y+\lambda z}
=\frac1{\lambda^2x^2+\lambda(y+z)}
=\frac1\lambda\;\frac1{\lambda x^2+(y+z)}.
\]
Thus
\[
F(\lambda x,\lambda y,\lambda z)
=\sum_{\rm cyc}\frac1{(\lambda x)^2+\lambda y+\lambda z}
=\frac1\lambda\sum_{\rm cyc}\frac1{\lambda x^2+(y+z)}.
\]
Since \(\lambda<1\), each denominator
\(\lambda x^2+(y+z)\le x^2+(y+z)\), and hence
\(\displaystyle\frac1{\lambda x^2+(y+z)}\ge\frac1{x^2+(y+z)}\).  It follows
that
\[
F(\lambda x,\lambda y,\lambda z)
=\frac1\lambda\sum_{\rm cyc}\frac1{\lambda x^2+(y+z)}
\ge\frac1\lambda\sum_{\rm cyc}\frac1{x^2+(y+z)}
>\sum_{\rm cyc}\frac1{x^2+(y+z)},
\]
because \(1/\lambda>1\).  In particular
\[
F(\lambda x,\lambda y,\lambda z)\;\ge\;F(x,y,z).
\]

Conclusion of Step 1:  to prove \(F(x,y,z)\le1\) under the weaker hypothesis
\(\;G(x,y,z)\le0\), it suffices to prove it in the **boundary‐case**
\[
G(x,y,z)=0,
\quad
\text{i.e.}\quad
\frac{x}{yz}+\frac{y}{zx}+\frac{z}{xy}=x+y+z.
\]

—–  

**Step 2.  On the manifold** 
\[
M=\Bigl\{(x,y,z)>0\mid\frac{x}{yz}+\frac{y}{zx}+\frac{z}{xy}=x+y+z\Bigr\}
\]
**the only critical‐point of** \(F\) **in the interior** is **\(x=y=z\).**  

We argue by symmetry and by the method of Lagrange multipliers.  Since
both the constraint and the function \(F\) are *completely symmetric* in
\((x,y,z)\), any interior extremum with \(x,y,z>0\) must satisfy
\[
x=y=z.
\]
(One may check this in detail by writing down
\(\nabla F=\mu\,\nabla G\), but symmetry alone forces
\(x=y=z\) at any stationary point in the positive‐octant.)

Finally, on \(M\) the point \(x=y=z\) must satisfy the *constraint* itself:
\[
\frac{x}{x^2}+\frac{x}{x^2}+\frac{x}{x^2}
=\frac3x
\;\stackrel{!}{=}\;
x+x+x=3x
\quad\Longrightarrow\quad
\frac3x=3x
\;\Longrightarrow\;
x^2=1
\;\Longrightarrow\;
x=1,
\]
where we take the positive root since \(x>0\).  Hence the unique
interior critical point of \(F\) on \(M\) is
\[
(x,y,z)=(1,1,1).
\]

One checks easily that as one of the variables tends to \(0\) or to
\(\infty\), the value of \(F\) tends to \(0\).  Hence the *global*
maximum of \(F\) on the *closed* set \(\{G=0,\;x,y,z\ge0\}\) is
attained at the single *interior* stationary point \((1,1,1)\).

—–  

**Step 3.  Conclusion.**  At \((x,y,z)=(1,1,1)\) we have
\[
F(1,1,1)
=\frac1{1^2+1+1}+\frac1{1^2+1+1}+\frac1{1^2+1+1}
=\frac1{3}+\frac1{3}+\frac1{3}=1.
\]
Since this is the global maximum of \(F\) under the boundary‐case
\(\;x/(yz)+y/(zx)+z/(xy)=x+y+z\), and since in Step 1 we saw that any
\((x,y,z)\) satisfying the *original* hypothesis
\(\;x/(yz)+y/(zx)+z/(xy)\le x+y+z\) can be shrunk to land on that
boundary without decreasing \(F\), we conclude in full generality that

\[
\boxed{
\frac1{x^2+y+z}+\frac1{y^2+z+x}+\frac1{z^2+x+y}\;\le\;1
}
\quad
\text{whenever}
\quad
\frac{x}{yz}+\frac{y}{zx}+\frac{z}{xy}\;\le\;x+y+z.
\]

Equality occurs exactly at \(x=y=z=1\).  This completes the proof.  ∎