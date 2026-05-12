# artifact_03

Competition: BMOSL  
Problem ID: BMOSL_2018_12  
Year: 2018

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \( P \) be a point inside a triangle \( ABC \) and let \( a, b, c \) be the side lengths and \( p \) the semi-perimeter of the triangle. Find the maximum value of

\[
\min \left(\frac{PA}{p-a}, \frac{PB}{p-b}, \frac{PC}{p-c}\right)
\]

over all possible choices of triangle \( ABC \) and point \( P \).

## Candidate Excerpts

### Option A

```text
Suppose, for sake of contradiction, that
\[
\frac{x}{\alpha}>\frac{2}{\sqrt3},\quad
\frac{y}{\beta}>\frac{2}{\sqrt3},\quad
\frac{z}{\gamma}>\frac{2}{\sqrt3}.
\]
Set 
\[
h=\frac{2}{\sqrt3}.
\]
Then
\[
x>h\,\alpha,\quad y>h\,\beta,\quad z>h\,\gamma,
\]
and hence
\[
y\,z\;>\;h^2\,\beta\gamma,\quad
z\,x\;>\;h^2\,\gamma\alpha,\quad
x\,y\;>\;h^2\,\alpha\beta.
\]
On the other hand, by decomposing the area of \(ABC\) into the three subtriangles \(PBC\), \(PCA\), \(PAB\) we have
\[
\Delta
\;=\;
[ABC]
\;=\;
[PBC]+[PCA]+[PAB]
\;=\;
\frac12\bigl(yz\sin\angle BPC
         \;+\;zx\sin\angle CPA
         \;+\;xy\sin\angle APB\bigr).
\]
Since each sine is at most \(1\), it follows that
\[
2\Delta
\;\le\;
y\,z\;+\;z\,x\;+\;x\,y.
\]
Putting the two estimates together,
\[
2\Delta
\;<\;
y\,z+z\,x+x\,y
\;<\;
h^2\bigl(\beta\gamma+\gamma\alpha+\alpha\beta\bigr)
\;=\;
\frac{4}{3}\,(\alpha\beta+\beta\gamma+\gamma\alpha).
\]
Hence
\[
\Delta
\;<\;
\frac{2}{3}\,(\alpha\beta+\beta\gamma+\gamma\alpha).
\]
But we also have Heron’s formula
\[
\Delta
\;=\;
\sqrt{\,p(p-a)(p-b)(p-c)\,}
\;=\;
\sqrt{\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma\,}
\,,
\]
so the foregoing inequality becomes
\[
\sqrt{(\alpha+\beta+\gamma)\,\alpha\beta\gamma}
\;<\;\frac{2}{3}\,(\alpha\beta+\beta\gamma+\gamma\alpha).
\]
Squaring both sides,
\[
(\alpha+\beta+\gamma)\,\alpha\beta\gamma
\;<\;\frac{4}{9}\,(\alpha\beta+\beta\gamma+\gamma\alpha)^2,
\]
or equivalently
\[
(\alpha\beta+\beta\gamma+\gamma\alpha)^2
\;<\;\frac{9}{4}\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma.
\]
But by the following well-known symmetric inequality, the reverse holds:
```

### Option B

```text
Notation.  Let the side-lengths of \(\triangle ABC\) be
\[
a=BC,\quad b=CA,\quad c=AB,
\]
and its semiperimeter
\[
p=\frac{a+b+c}2.
\]
Set
\[
\alpha=p-a,\quad \beta=p-b,\quad \gamma=p-c,
\]
so that \(\alpha,\beta,\gamma>0\) and moreover
\[
\alpha+\beta+\gamma
\;=\;
(p-a)+(p-b)+(p-c)
\;=\;
3p-(a+b+c)
\;=\;
p.
\]
Denote
\[
x=PA,\quad y=PB,\quad z=PC.
\]
Our goal is to prove
\[
\min\Bigl\{\frac{x}{\alpha},\,\frac{y}{\beta},\,\frac{z}{\gamma}\Bigr\}
\;\le\;\frac{2}{\sqrt3}.
\]
```

### Option C

```text
Lemma.  For all positive \(\alpha,\beta,\gamma\),
\[
(\alpha\beta+\beta\gamma+\gamma\alpha)^2
\;\ge\;
3\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma.
\]
Proof of lemma.  Expand and factor:
\[
\begin{aligned}
(\alpha\beta+\beta\gamma+\gamma\alpha)^2
&\;-\;3\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma
\\
&=\;\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2
      +2\,\alpha\beta\gamma(\alpha+\beta+\gamma)
      \;-\;3\,\alpha\beta\gamma(\alpha+\beta+\gamma)
\\
&=\;\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2
      \;-\;\alpha\beta\gamma(\alpha+\beta+\gamma)
\\
&=\;\tfrac12\bigl[(\alpha\beta-\beta\gamma)^2+(\beta\gamma-\gamma\alpha)^2
                        +(\gamma\alpha-\alpha\beta)^2\bigr]
\;\ge\;0.
\end{aligned}
\]
□
```

### Option D

```text
\[
\min\Bigl\{\frac{PA}{p-a},\,\frac{PB}{p-b},\,\frac{PC}{p-c}\Bigr\}\;\le\;\frac{2}{\sqrt3}\,,
\]
and that equality is attained when \(ABC\) is equilateral and \(P\) its center.  From this it follows immediately that
\[
\max_{\,\triangle ABC,\,P\in\mathrm{int}\,ABC}
\min\Bigl\{\frac{PA}{p-a},\frac{PB}{p-b},\frac{PC}{p-c}\Bigr\}
\;=\;\frac{2}{\sqrt3}\,. 
\]
```

## Full Candidate Proof

```text
Proof.  We shall show that for any triangle \(ABC\) with semiperimeter \(p\) and any interior point \(P\) one has

\[
\min\Bigl\{\frac{PA}{p-a},\,\frac{PB}{p-b},\,\frac{PC}{p-c}\Bigr\}\;\le\;\frac{2}{\sqrt3}\,,
\]
and that equality is attained when \(ABC\) is equilateral and \(P\) its center.  From this it follows immediately that
\[
\max_{\,\triangle ABC,\,P\in\mathrm{int}\,ABC}
\min\Bigl\{\frac{PA}{p-a},\frac{PB}{p-b},\frac{PC}{p-c}\Bigr\}
\;=\;\frac{2}{\sqrt3}\,. 
\]

Notation.  Let the side-lengths of \(\triangle ABC\) be
\[
a=BC,\quad b=CA,\quad c=AB,
\]
and its semiperimeter
\[
p=\frac{a+b+c}2.
\]
Set
\[
\alpha=p-a,\quad \beta=p-b,\quad \gamma=p-c,
\]
so that \(\alpha,\beta,\gamma>0\) and moreover
\[
\alpha+\beta+\gamma
\;=\;
(p-a)+(p-b)+(p-c)
\;=\;
3p-(a+b+c)
\;=\;
p.
\]
Denote
\[
x=PA,\quad y=PB,\quad z=PC.
\]
Our goal is to prove
\[
\min\Bigl\{\frac{x}{\alpha},\,\frac{y}{\beta},\,\frac{z}{\gamma}\Bigr\}
\;\le\;\frac{2}{\sqrt3}.
\]

Suppose, for sake of contradiction, that
\[
\frac{x}{\alpha}>\frac{2}{\sqrt3},\quad
\frac{y}{\beta}>\frac{2}{\sqrt3},\quad
\frac{z}{\gamma}>\frac{2}{\sqrt3}.
\]
Set 
\[
h=\frac{2}{\sqrt3}.
\]
Then
\[
x>h\,\alpha,\quad y>h\,\beta,\quad z>h\,\gamma,
\]
and hence
\[
y\,z\;>\;h^2\,\beta\gamma,\quad
z\,x\;>\;h^2\,\gamma\alpha,\quad
x\,y\;>\;h^2\,\alpha\beta.
\]
On the other hand, by decomposing the area of \(ABC\) into the three subtriangles \(PBC\), \(PCA\), \(PAB\) we have
\[
\Delta
\;=\;
[ABC]
\;=\;
[PBC]+[PCA]+[PAB]
\;=\;
\frac12\bigl(yz\sin\angle BPC
         \;+\;zx\sin\angle CPA
         \;+\;xy\sin\angle APB\bigr).
\]
Since each sine is at most \(1\), it follows that
\[
2\Delta
\;\le\;
y\,z\;+\;z\,x\;+\;x\,y.
\]
Putting the two estimates together,
\[
2\Delta
\;<\;
y\,z+z\,x+x\,y
\;<\;
h^2\bigl(\beta\gamma+\gamma\alpha+\alpha\beta\bigr)
\;=\;
\frac{4}{3}\,(\alpha\beta+\beta\gamma+\gamma\alpha).
\]
Hence
\[
\Delta
\;<\;
\frac{2}{3}\,(\alpha\beta+\beta\gamma+\gamma\alpha).
\]
But we also have Heron’s formula
\[
\Delta
\;=\;
\sqrt{\,p(p-a)(p-b)(p-c)\,}
\;=\;
\sqrt{\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma\,}
\,,
\]
so the foregoing inequality becomes
\[
\sqrt{(\alpha+\beta+\gamma)\,\alpha\beta\gamma}
\;<\;\frac{2}{3}\,(\alpha\beta+\beta\gamma+\gamma\alpha).
\]
Squaring both sides,
\[
(\alpha+\beta+\gamma)\,\alpha\beta\gamma
\;<\;\frac{4}{9}\,(\alpha\beta+\beta\gamma+\gamma\alpha)^2,
\]
or equivalently
\[
(\alpha\beta+\beta\gamma+\gamma\alpha)^2
\;<\;\frac{9}{4}\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma.
\]
But by the following well-known symmetric inequality, the reverse holds:

Lemma.  For all positive \(\alpha,\beta,\gamma\),
\[
(\alpha\beta+\beta\gamma+\gamma\alpha)^2
\;\ge\;
3\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma.
\]
Proof of lemma.  Expand and factor:
\[
\begin{aligned}
(\alpha\beta+\beta\gamma+\gamma\alpha)^2
&\;-\;3\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma
\\
&=\;\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2
      +2\,\alpha\beta\gamma(\alpha+\beta+\gamma)
      \;-\;3\,\alpha\beta\gamma(\alpha+\beta+\gamma)
\\
&=\;\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2
      \;-\;\alpha\beta\gamma(\alpha+\beta+\gamma)
\\
&=\;\tfrac12\bigl[(\alpha\beta-\beta\gamma)^2+(\beta\gamma-\gamma\alpha)^2
                        +(\gamma\alpha-\alpha\beta)^2\bigr]
\;\ge\;0.
\end{aligned}
\]
□

Since \(3>\tfrac94\), the lemma gives
\[
(\alpha\beta+\beta\gamma+\gamma\alpha)^2
\;\ge\;
3\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma
\;>\;
\frac{9}{4}\,(\alpha+\beta+\gamma)\,\alpha\beta\gamma,
\]
in direct contradiction to the strict inequality we deduced.  This contradiction shows that our assumption
\(\tfrac{x}{\alpha},\tfrac{y}{\beta},\tfrac{z}{\gamma} > \tfrac{2}{\sqrt3}\) cannot hold.  Hence for every triangle \(ABC\) and every interior point \(P\) at least one of
\(\tfrac{PA}{p-a}\), \(\tfrac{PB}{p-b}\), \(\tfrac{PC}{p-c}\) is \(\le2/\sqrt3\).  That is,
\[
\min\Bigl\{\frac{PA}{p-a},\,\frac{PB}{p-b},\,\frac{PC}{p-c}\Bigr\}
\;\le\;\frac{2}{\sqrt3}.
\]
Finally, equality is attained in the case of an equilateral triangle of side \(s\) with \(P\) its center:
there \(p=\tfrac{3s}2\), so \(p-a=p-s=\tfrac s2\), and \(PA=PB=PC=s/\sqrt3\), whence
\[
\frac{PA}{p-a}
\;=\;
\frac{s/\sqrt3}{s/2}
\;=\;
\frac{2}{\sqrt3}.
\]
Therefore the maximum possible value of the given minimum is exactly \(\displaystyle \tfrac{2}{\sqrt3}\), as claimed.  □
```

## Reviewer Note

Computation mistake.
