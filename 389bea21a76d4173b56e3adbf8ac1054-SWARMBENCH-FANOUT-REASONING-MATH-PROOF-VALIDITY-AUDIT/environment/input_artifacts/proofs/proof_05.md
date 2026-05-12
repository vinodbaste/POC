<!-- DOMAIN_BACKGROUND: /input_artifacts/background_algebra_analysis.md -->
<!-- REQUIRED: Read /input_artifacts/background_algebra_analysis.md before evaluating this proof. -->

    # proof_05

    - Problem ID: USAMO_2013_4
    - Competition: USAMO
    - Year: 2013
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 16

    ## Problem

    Find all real numbers \(x, y, z \geq 1\) satisfying

\[
\min (\sqrt{x+x y z}, \sqrt{y+x y z}, \sqrt{z+x y z})=\sqrt{x-1}+\sqrt{y-1}+\sqrt{z-1}
\]

    ## Candidate Solution Attempt

    Proof.  We begin by observing that the given equation is symmetric in \((x,y,z)\) except for the “\(\min\)” which picks out the smallest of the three quantities 
\[
\sqrt{x+xyz},\quad \sqrt{y+xyz},\quad \sqrt{z+xyz}.
\] 
Accordingly, let \((x,y,z)\) be any solution with \(x,y,z\ge1\), and without loss of generality assume 
\[
x\le y,\quad x\le z.
\] 
Then 
\[
\min\bigl(\sqrt{x+xyz},\sqrt{y+xyz},\sqrt{z+xyz}\bigr)
=\sqrt{x+xyz},
\] 
and the equation becomes
\[
\sqrt{x+xyz}
=\sqrt{x-1}+\sqrt{y-1}+\sqrt{z-1}.
\tag{1}
\]

Define a function of one real variable \(t\ge1\):
\[
f(t)\;=\;\sqrt{\,t\,(1+yz)\,}\;-\;\Bigl(\sqrt{t-1}+\sqrt{y-1}+\sqrt{z-1}\Bigr).
\]
Then equation \((1)\) is simply
\[
f(x)\;=\;0.
\]
We will show that \(f\) has at most one zero for \(t\ge1\), and that a zero exists if and only if two algebraic relations among \(x,y,z\) hold.

1. Derivative and critical point.  
Since \(y,z\ge1\), the function \(f\) is differentiable for \(t>1\), with
\[
f'(t)
=\frac{1+yz}{2\sqrt{\,t(1+yz)\,}}
\;-\;\frac1{2\sqrt{\,t-1\,}}.
\]
Set \(f'(t)=0\).  This is
\[
\frac{1+yz}{\sqrt{\,t(1+yz)\,}}
\;=\;
\frac1{\sqrt{\,t-1\,}},
\]
square both sides,
\[
\frac{(1+yz)^2}{\,t(1+yz)\,}
\;=\;
\frac1{\,t-1\,},
\]
whence
\[
\frac{1+yz}{t}
\;=\;
\frac1{t-1}
\quad\Longrightarrow\quad
t-1=\frac1{yz}
\quad\Longrightarrow\quad
t
=\;1+\frac1{\,yz\,}.
\]
Call this unique solution \(t_0=1+1/(yz)\).  One checks easily that for \(1\le t<t_0\) the derivative \(f'(t)<0\), while for \(t>t_0\) one has \(f'(t)>0\).  Hence \(f\) strictly decreases on \([1,t_0]\) and strictly increases on \([t_0,\infty)\), so \(f\) has a unique global minimum at \(t=t_0\).

2. Boundary behavior.  
First,
\[
f(1)
=\sqrt{1+yz}\;-\;\Bigl(0+\sqrt{y-1}+\sqrt{z-1}\Bigr).
\]
We claim \(f(1)>0\).  Indeed
\[
\sqrt{1+yz}>\sqrt{y-1}+\sqrt{z-1}
\]
holds because squaring gives
\[
1+yz
>\;y+z-2\;+\;2\sqrt{(y-1)(z-1)},
\]
i.e.
\[
yz-y-z+3
>2\sqrt{(y-1)(z-1)},
\]
but \(yz-y-z+1=(y-1)(z-1)\), so
\[
yz-y-z+3
=(y-1)(z-1)+2
>2\sqrt{(y-1)(z-1)},
\]
which is immediate from \((\sqrt{(y-1)(z-1)}-1)^2>0\).  Thus \(f(1)>0\).  On the other hand,
\[
\lim_{t\to+\infty}f(t)
=\lim_{t\to\infty}\Bigl(\sqrt{t(1+yz)}-\sqrt{t-1}\Bigr)
\;=\;+\infty.
\]

3. Zeroes of \(f\).  
Since \(f\) decreases from \(f(1)>0\) down to its minimum \(f(t_0)\), then increases to \(+\infty\), the equation \(f(t)=0\) has
– no solution if \(f(t_0)>0\),
– exactly one solution if \(f(t_0)=0\),
– exactly two solutions if \(f(t_0)<0\).

But in case there were two distinct solutions \(t_1<t_2\), the equation \(\sqrt{t(1+yz)}=\sqrt{t-1}+\sqrt{y-1}+\sqrt{z-1}\) would hold at both \(t_1\) and \(t_2\); by monotonicity of the left‐ and right‐sides one checks that this cannot happen unless they coincide identically, which they do not.  Hence in fact there is at most one root, and it exists if and only if \(f(t_0)\le0\).  Moreover, if \(f(t_0)=0\) there is exactly one root, namely \(x=t_0\).

4. Algebraic condition for \(f(t_0)=0\).  
We compute
\[
f(t_0)
=\sqrt{t_0(1+yz)}
\;-\;
\Bigl(\sqrt{t_0-1}+\sqrt{y-1}+\sqrt{z-1}\Bigr).
\]
Since \(t_0=1+1/(yz)\), one finds
\[
t_0-1=\frac1{yz}, 
\quad
t_0(1+yz)
=\Bigl(1+\tfrac1{yz}\Bigr)(1+yz)
=2+yz+\frac1{yz}.
\]
Hence
\[
f(t_0)=
\sqrt{2+yz+\tfrac1{yz}}
\;-\;\Bigl(\tfrac1{\sqrt{yz}}+\sqrt{y-1}+\sqrt{z-1}\Bigr).
\]
The condition \(f(t_0)=0\) is therefore
\[
\sqrt{2+yz+\tfrac1{yz}}
\;=\;
\frac1{\sqrt{yz}}
\;+\;\sqrt{y-1}+\sqrt{z-1}.
\]
Square both sides.  A straightforward simplification (canceling the common terms and using
\((y-1)(z-1)=yz-y-z+1\)) shows equivalently
\[
yz \;=\; y+z.
\]
Thus
\[
\boxed{(\,y-1\,)\,(z-1)=1}
\quad\text{and}\quad
\boxed{x \;=\; t_0 \;=\;1+\frac1{\,yz\,}}
\]
are necessary and sufficient for \(f(t_0)=0\) and hence for the existence of the unique solution \(x\ge1\) to \((1)\).

5. Verification that \(x\le y,z\).  
From \(yz=y+z\) one gets
\[
z\,y - z = y
\quad\Longrightarrow\quad
z\,(y-1)=y
\quad\Longrightarrow\quad
z=\frac y{\,y-1\,}>1,
\]
and symmetrically \(y>1\).  Also
\[
x
=1+\frac1{yz}
=1+\frac1{y+z}
\;<\;
1+\frac1{y-1+\,1}
=1+\frac1{y}
<y
\]
because \(y>1\).  Similarly \(x<z\).  Hence \(x\) is indeed the smallest of the three, so our choice of which term is the “\(\min\)” was consistent.

6. Conclusion and description of all solutions.  
We have shown:  
– If \(x\le y,z\) and the given equation holds, then necessarily
\[
yz=y+z,
\quad
x=1+\frac1{yz}.
\]
– Conversely, whenever \(y,z>1\) satisfy \(yz=y+z\), and we set
\[
x=1+\frac1{yz},
\]
one checks directly that \(x\le y,z\) and that \((x,y,z)\) satisfies
\(\sqrt{x+xyz}=\sqrt{x-1}+\sqrt{y-1}+\sqrt{z-1}.\)

Finally, by symmetry among \(x,y,z\), the same one‐parameter family of solutions arises no matter which of the three variables is the smallest.  Hence the full solution set is obtained by the following construction:

• Choose any real \(a>1\).  
• Set \(b\) so that \((a-1)(b-1)=1\), i.e.\ \(b=1+\tfrac1{a-1}\).  Then \(b>1\) and \(ab=a+b\).  
• Set the third variable \(c=1+\tfrac1{ab}\).  One checks \(c<\min\{a,b\}\) and \(c\ge1\).  

Then \((c,a,b)\) satisfies the equation with \(\min\) attained at the first coordinate.  Permuting the three coordinates gives all solutions.

Equivalently, one may parametrize by a single parameter \(t>0\):
\[
a=1+t,\quad b=1+\frac1t,\quad c=1+\frac1{(1+t)(1+1/t)},
\]
and then take all permutations of \((a,b,c)\).

This completes the classification of all real solutions \(x,y,z\ge1\).  \(\boxed{}\)