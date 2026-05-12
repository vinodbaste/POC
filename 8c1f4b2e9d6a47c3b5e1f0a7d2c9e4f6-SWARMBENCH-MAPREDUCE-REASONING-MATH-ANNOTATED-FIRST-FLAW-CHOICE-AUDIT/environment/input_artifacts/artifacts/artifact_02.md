# artifact_02

Competition: IMOSL  
Problem ID: IMOSL_2010_1  
Year: 2010

You are reviewing a real human annotation from the Open Proof Corpus. A curator converted one free-form annotation into four candidate proof excerpts. Exactly one candidate excerpt contains the human-marked first unrecoverable flaw in this incorrect proof attempt. Choose the correct option letter. The candidate excerpts are presented in a randomized order.

## Problem

Determine all functions \( f: \mathbb{R} \rightarrow \mathbb{R} \) such that the equality

\[
f([x] y) = f(x)[f(y)]
\]

holds for all \( x, y \in \mathbb{R} \). Here, by \([x]\) we denote the greatest integer not exceeding \( x \).

## Candidate Excerpts

### Option A

```text
(d)  Finally, we show \(f(x)=0\) for \(x<0\).  Fix any \(y>0\).  Then \(\lfloor y\rfloor\ge0\), so we already know \(f(y)=0\) and hence \(\lfloor f(y)\rfloor=0\).  Now take any \(x\in(-1,0)\); then \(\lfloor x\rfloor=-1\).  The assertion \(P(x,y)\) gives
\[
f(-1\cdot y)
=f(x)\,\lfloor f(y)\rfloor
=f(x)\cdot0
=0.
\]
Thus \(f(-y)=0\) for every \(y>0\), i.e.\ \(f(x)=0\) for all \(x<0\).
```

### Option B

```text
Putting (c) and (d) together, we have shown \(f(x)=0\) for every real \(x\).  But this means \(f\) is constant, contradicting the nonconstant assumption.  Hence there is no nonconstant solution.
```

### Option C

```text
Now for any \(x\in(0,1)\) we have \(\lfloor x\rfloor=0\), so \(P(x,y_0)\) gives
\[
f(0\cdot y_0)=f(0)=0
\;=\;
f(x)\,\lfloor f(y_0)\rfloor.
\]
Since \(\lfloor f(y_0)\rfloor\neq0\), this forces
\[
f(x)=0
\quad\text{for every }x\in(0,1).
\]
Thus
\[
f(x)=0\quad\text{for all }0\le x<1.
\]
```

### Option D

```text
(c)  We extend this vanishing by induction on the integer part.  Suppose for some integer \(k\ge1\) we have shown 
\[
f(x)=0
\quad
\text{for all }0\le x<k.
\]
Take any \(x\) with \(k\le x<k+1\).  Then \(\lfloor x\rfloor=k\), and for every \(y\in(0,1)\) we know \(f(y)=0\), so \(\lfloor f(y)\rfloor=0\).  Applying \(P(x,y)\) yields
\[
f\bigl(k\,y\bigr)
=\;f(x)\,\lfloor f(y)\rfloor
=\;f(x)\cdot0
=\;0.
\]
But as \(y\) runs over \((0,1)\), the product \(k\,y\) sweeps the entire interval \((0,k)\), on which by the induction hypothesis we already know \(f\equiv0\).  In particular this shows consistency on \((0,k)\), and moreover it forces
\[
f(x)=0
\quad\text{for all }k\le x<k+1.
\]
By induction, \(f(x)=0\) for all \(x\ge0\).
```

## Full Candidate Proof

```text
Proof. Define the assertion  
\[P(x,y):\quad f(\lfloor x\rfloor\,y)\;=\;f(x)\,\bigl\lfloor f(y)\bigr\rfloor,\]
valid for all real \(x,y\).  

1.  Constant solutions.  
Suppose \(f(x)\equiv c\) for all \(x\).  Then  
\[
f(\lfloor x\rfloor\,y)=c,
\]
whereas
\[
f(x)\,\lfloor f(y)\rfloor
=c\;\lfloor c\rfloor.
\]
Hence the equation \(c=c\lfloor c\rfloor\) must hold.  There are two ways to satisfy  
\[
c=c\lfloor c\rfloor:
\]
either \(c=0\), or else \(\lfloor c\rfloor=1\).  Conversely, if \(c=0\) or \(1\le c<2\), then indeed
\[
c = c\lfloor c\rfloor,
\]
so \(f(x)\equiv c\) is a solution.  Thus all constant solutions are
\[
f(x)\equiv 0,
\quad\text{or}\quad
f(x)\equiv c\quad\text{with }1\le c<2.
\]

2.  Nonconstant case leads to a contradiction.  
Assume from now on that \(f\) is not constant.  We shall show that this forces \(f\equiv0\), a contradiction.

(a)  First, apply \(P(x,0)\).  Since \(\lfloor 0\rfloor=0\), the left‐hand side is
\[
f(\lfloor x\rfloor\cdot0)=f(0),
\]
and the right‐hand side is
\[
f(x)\,\lfloor f(0)\rfloor.
\]
Hence
\[
f(0)=f(x)\,\lfloor f(0)\rfloor\quad\forall x.
\]
If \(\lfloor f(0)\rfloor\neq0\), then \(f(x)=f(0)/\lfloor f(0)\rfloor\) is constant, contrary to assumption.  Therefore 
\[
\lfloor f(0)\rfloor=0,
\quad
f(0)=0.
\]

(b)  Next, since \(f\) is not constant, the integer‐valued function \(y\mapsto\lfloor f(y)\rfloor\) cannot be the same integer for all \(y\).  In particular there exists \(y_0\) with 
\(\lfloor f(y_0)\rfloor\neq0\).  

Now for any \(x\in(0,1)\) we have \(\lfloor x\rfloor=0\), so \(P(x,y_0)\) gives
\[
f(0\cdot y_0)=f(0)=0
\;=\;
f(x)\,\lfloor f(y_0)\rfloor.
\]
Since \(\lfloor f(y_0)\rfloor\neq0\), this forces
\[
f(x)=0
\quad\text{for every }x\in(0,1).
\]
Thus
\[
f(x)=0\quad\text{for all }0\le x<1.
\]

(c)  We extend this vanishing by induction on the integer part.  Suppose for some integer \(k\ge1\) we have shown 
\[
f(x)=0
\quad
\text{for all }0\le x<k.
\]
Take any \(x\) with \(k\le x<k+1\).  Then \(\lfloor x\rfloor=k\), and for every \(y\in(0,1)\) we know \(f(y)=0\), so \(\lfloor f(y)\rfloor=0\).  Applying \(P(x,y)\) yields
\[
f\bigl(k\,y\bigr)
=\;f(x)\,\lfloor f(y)\rfloor
=\;f(x)\cdot0
=\;0.
\]
But as \(y\) runs over \((0,1)\), the product \(k\,y\) sweeps the entire interval \((0,k)\), on which by the induction hypothesis we already know \(f\equiv0\).  In particular this shows consistency on \((0,k)\), and moreover it forces
\[
f(x)=0
\quad\text{for all }k\le x<k+1.
\]
By induction, \(f(x)=0\) for all \(x\ge0\).

(d)  Finally, we show \(f(x)=0\) for \(x<0\).  Fix any \(y>0\).  Then \(\lfloor y\rfloor\ge0\), so we already know \(f(y)=0\) and hence \(\lfloor f(y)\rfloor=0\).  Now take any \(x\in(-1,0)\); then \(\lfloor x\rfloor=-1\).  The assertion \(P(x,y)\) gives
\[
f(-1\cdot y)
=f(x)\,\lfloor f(y)\rfloor
=f(x)\cdot0
=0.
\]
Thus \(f(-y)=0\) for every \(y>0\), i.e.\ \(f(x)=0\) for all \(x<0\).  

Putting (c) and (d) together, we have shown \(f(x)=0\) for every real \(x\).  But this means \(f\) is constant, contradicting the nonconstant assumption.  Hence there is no nonconstant solution.

3.  Conclusion.  
The only solutions are the constant ones
\[
\boxed{ 
f(x)\equiv 0,
\quad\text{or}\quad
f(x)\equiv c\text{ with }1\le c<2,
}
\]
and one readily checks that each of these indeed satisfies 
\(\;f(\lfloor x\rfloor\,y)=f(x)\,\lfloor f(y)\rfloor.\)  This completes the proof.  ∎
```

## Reviewer Note

Part (c) is wrong.
