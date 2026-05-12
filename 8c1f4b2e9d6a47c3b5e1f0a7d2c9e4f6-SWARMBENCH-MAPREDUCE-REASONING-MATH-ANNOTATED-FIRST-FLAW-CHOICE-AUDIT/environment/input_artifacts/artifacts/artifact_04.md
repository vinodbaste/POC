# artifact_04

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
1. Notation and reduction to one inequality.
```

### Option B

```text
Let \(ABC\) be any nondegenerate triangle, with side‐lengths \(BC=a,\;CA=b,\;AB=c\) and semiperimeter 
\[
p=\frac{a+b+c}2\,.
\]
Fix a point \(P\) in the interior of \(ABC\), and set
\[
x=p-a,\quad y=p-b,\quad z=p-c.
\]
Then \(x,y,z>0\) and \(x+y+z=p\).  We must show
\[
\min\Bigl\{\frac{PA}{x},\,\frac{PB}{y},\,\frac{PC}{z}\Bigr\}\;\le\;\frac{2}{\sqrt3}
\quad\text{for every }P,
\]
and exhibit one choice of \((ABC,P)\) for which equality holds.
```

### Option C

```text
Suppose, for the sake of contradiction, that
\[
PA>\;k\,x,\quad PB>\;k\,y,\quad PC>\;k\,z
\]
for some real \(k>2/\sqrt3\).  Then
\[
PB\cdot PC>k^2\,yz,\quad
PC\cdot PA>k^2\,zx,\quad
PA\cdot PB>k^2\,xy,
\]
so upon adding,
\[
PB\cdot PC+PC\cdot PA+PA\cdot PB\;>\;k^2\,(xy+yz+zx).
\tag{2.1}
\]
On the other hand, since \(P\) lies inside \(ABC\), we may partition
\[
\Delta:=\bigl[ABC\bigr]
\;=\;
\bigl[PBC\bigr]+\bigl[PCA\bigr]+\bigl[PAB\bigr]
\;=\;\frac12\bigl(PB\cdot PC\sin\angle BPC
\;+\;\cdots\bigr)
\;\le\;\frac12\bigl(PB\cdot PC+PC\cdot PA+PA\cdot PB\bigr),
\]
because each \(\sin(\cdot)\le1\).  Hence
\[
2\,\Delta\;\le\;PB\cdot PC+PC\cdot PA+PA\cdot PB.
\tag{2.2}
\]
Combining \((2.1)\) and \((2.2)\) gives
\[
2\,\Delta\;>\;k^2\,(xy+yz+zx)
\quad\Longrightarrow\quad
\Delta\;>\;\frac{k^2}{2}\,(xy+yz+zx).
\tag{2.3}
\]
```

### Option D

```text
2. The upper bound \(\displaystyle\frac{2}{\sqrt3}\).
```

## Full Candidate Proof

```text
Here is a self‐contained proof that

\[
M \;:=\; \max_{\substack{ABC\;\triangle \\P\;\text{inside}}}
\;\min\Bigl\{\frac{PA}{p-a},\,\frac{PB}{p-b},\,\frac{PC}{p-c}\Bigr\}
\;=\;\frac{2}{\sqrt3}\,.
\]

Proof.

1. Notation and reduction to one inequality.

Let \(ABC\) be any nondegenerate triangle, with side‐lengths \(BC=a,\;CA=b,\;AB=c\) and semiperimeter 
\[
p=\frac{a+b+c}2\,.
\]
Fix a point \(P\) in the interior of \(ABC\), and set
\[
x=p-a,\quad y=p-b,\quad z=p-c.
\]
Then \(x,y,z>0\) and \(x+y+z=p\).  We must show
\[
\min\Bigl\{\frac{PA}{x},\,\frac{PB}{y},\,\frac{PC}{z}\Bigr\}\;\le\;\frac{2}{\sqrt3}
\quad\text{for every }P,
\]
and exhibit one choice of \((ABC,P)\) for which equality holds.

2. The upper bound \(\displaystyle\frac{2}{\sqrt3}\).

Suppose, for the sake of contradiction, that
\[
PA>\;k\,x,\quad PB>\;k\,y,\quad PC>\;k\,z
\]
for some real \(k>2/\sqrt3\).  Then
\[
PB\cdot PC>k^2\,yz,\quad
PC\cdot PA>k^2\,zx,\quad
PA\cdot PB>k^2\,xy,
\]
so upon adding,
\[
PB\cdot PC+PC\cdot PA+PA\cdot PB\;>\;k^2\,(xy+yz+zx).
\tag{2.1}
\]
On the other hand, since \(P\) lies inside \(ABC\), we may partition
\[
\Delta:=\bigl[ABC\bigr]
\;=\;
\bigl[PBC\bigr]+\bigl[PCA\bigr]+\bigl[PAB\bigr]
\;=\;\frac12\bigl(PB\cdot PC\sin\angle BPC
\;+\;\cdots\bigr)
\;\le\;\frac12\bigl(PB\cdot PC+PC\cdot PA+PA\cdot PB\bigr),
\]
because each \(\sin(\cdot)\le1\).  Hence
\[
2\,\Delta\;\le\;PB\cdot PC+PC\cdot PA+PA\cdot PB.
\tag{2.2}
\]
Combining \((2.1)\) and \((2.2)\) gives
\[
2\,\Delta\;>\;k^2\,(xy+yz+zx)
\quad\Longrightarrow\quad
\Delta\;>\;\frac{k^2}{2}\,(xy+yz+zx).
\tag{2.3}
\]

But by Heron’s formula,
\[
\Delta^2 \;=\; p\,x\,y\,z \;=\;(x+y+z)\,x\,y\,z,
\]
and we claim the following purely algebraic inequality holds for all \(x,y,z>0\):
\[
\Delta\;\le\;\frac23\,(xy+yz+zx).
\tag{2.4}
\]
Indeed, \((2.4)\) is equivalent to
\[
\bigl(\sqrt{p\,xyz}\bigr)^2\;=\;p\,xyz\;\le\;\frac{4}{9}\,(xy+yz+zx)^2
\quad\Longleftrightarrow\quad
9\,(x+y+z)\,xyz\;\le\;4\,(xy+yz+zx)^2.
\]
But a standard symmetric factorization shows
\[
(xy+yz+zx)^2-3(x+y+z)xyz
\;=\;
\frac12\Bigl[(xy-yz)^2+(yz-zx)^2+(zx-xy)^2\Bigr]
\;\ge\;0.
\]
Hence
\[
(xy+yz+zx)^2\;\ge\;3\,(x+y+z)\,xyz
\;\Longrightarrow\;
4\,(xy+yz+zx)^2\;\ge\;12\,(x+y+z)\,xyz
\;>\;9\,(x+y+z)\,xyz,
\]
which proves \((2.4)\).  

Since \(k>2/\sqrt3\) means \(k^2/2>(4/3)/2=2/3\), the right–hand side of \((2.3)\) exceeds \(\tfrac23\,(xy+yz+zx)\).  Thus \((2.3)\) contradicts \((2.4)\).  We conclude no such \(k>2/\sqrt3\) can satisfy
\[
PA>k\,x,\quad PB>k\,y,\quad PC>k\,z.
\]
Therefore in every triangle \(ABC\) and for every interior \(P\),
\[
\min\Bigl\{\frac{PA}{x},\,\frac{PB}{y},\,\frac{PC}{z}\Bigr\}
\;\le\;\frac{2}{\sqrt3}.
\]
That shows the supremum of the minimum‐ratio is at most \(2/\sqrt3\).

3. Attaining \(2/\sqrt3\).

Finally, take \(ABC\) to be equilateral of side length \(s\).  Then
\[
p=\tfrac32s,\quad x=y=z=p-s=\tfrac12s,
\]
and choose \(P\) to be the center of the equilateral triangle.  Then
\[
PA=PB=PC=\frac{s}{\sqrt3},
\]
so for each vertex—for example \(A\)—one has
\[
\frac{PA}{p-a}
\;=\;
\frac{\tfrac{s}{\sqrt3}}{\,\tfrac12s\,}
\;=\;\frac{2}{\sqrt3}.
\]
Hence in this case
\(\min\{PA/x,\;PB/y,\;PC/z\}=2/\sqrt3\), 
showing the bound is sharp.

Collecting the two parts, the desired maximum is
\[
\boxed{\;M=\frac{2}{\sqrt3}\;}.
\]  ∎
```

## Reviewer Note

Computational mistakes.
