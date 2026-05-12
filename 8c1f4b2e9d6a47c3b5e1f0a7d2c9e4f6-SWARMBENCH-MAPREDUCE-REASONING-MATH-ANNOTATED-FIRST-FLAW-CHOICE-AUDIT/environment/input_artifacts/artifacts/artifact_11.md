# artifact_11

Competition: USAMO  
Problem ID: USAMO_2015_5  
Year: 2015

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(a, b, c, d, e\) be distinct positive integers such that \(a^{4}+b^{4}=c^{4}+d^{4}=e^{5}\). Show that \(a c+b d\) is a composite number.

## Candidate Excerpts

### Option A

```text
Step 1.  The two factors $\alpha$ and $\overline\alpha$ are coprime in $\Bbb Z[i]$.  
Indeed, any common Gaussian divisor $\delta\mid\alpha,\overline\alpha$ must also divide
\[
\alpha+\overline\alpha \;=\;2a^2,
\qquad
\alpha-\overline\alpha \;=\;2i\,b^2.
\]
One checks by a short parity‐argument that no nonunit of $\Bbb Z[i]$ can divide both $2a^2$ and $2i\,b^2$ unless $2\mid e$ and both $a,b$ are even, in which case one can produce a strictly smaller solution by dividing everything by $2$ (an infinite‐descent contradiction).  Hence in any genuine solution one finds $\gcd(\alpha,\overline\alpha)=1$.  Similarly $\gcd(\beta,\overline\beta)=1$.
```

### Option B

```text
Step 2.  Since $\Bbb Z[i]$ is a UFD and
\[
\alpha\,\overline\alpha
 \;=\;(e)^5
\]
with $\gcd(\alpha,\overline\alpha)=1$, by the usual “coprime‐factors‐of‐a‐power are powers” lemma there exist a Gaussian integer $z=x+iy$ and a unit $u\in\{±1,±i\}$ such that
\[
\alpha \;=\;u\,(x+iy)^5,
\qquad
\overline\alpha \;=\;\overline u\,(x-iy)^5.
\]
Likewise, there is a (perhaps different) unit $v\in\{±1,±i\}$ and a Gaussian integer $w=p+iq$ such that
\[
\beta  \;=\;v\,(p+iq)^5,
\qquad
\overline\beta \;=\;\overline v\,(p-iq)^5.
\]
```

### Option C

```text
Below is a self‐contained proof (apart from a routine gcd‐check in ℤ[i] which I have indicated and sketched) using unique factorization in the Gaussian integers ℤ[i].  All ring‐theoretic facts about ℤ[i] that we invoke are standard (class number 1, units ±1,±i, norm $N(x+iy)=x^2+y^2$).
```

### Option D

```text
Proof.  Suppose $a,b,c,d,e$ are distinct positive integers with
\[
a^4+b^4 \;=\;c^4+d^4\;=\;e^5.
\]
We work in the ring $\Bbb Z[i]$.  Set
\[
\alpha \;=\;a^2 + i\,b^2,\quad 
\overline\alpha \;=\;a^2 - i\,b^2,
\]
and similarly
\[
\beta  \;=\;c^2 + i\,d^2,\quad 
\overline\beta \;=\;c^2 - i\,d^2.
\]
Then
\[
N(\alpha)\;=\;\alpha\ \overline\alpha
 \;=\;(a^2)^2+(b^2)^2
 \;=\;a^4+b^4
 \;=\;e^5,
\]
and likewise $N(\beta)=\beta\,\overline\beta=e^5$.  Thus in $\Bbb Z[i]$ we have two factorizations of the principal ideal $(e^5)$:
\[
(e^5)\;=\;(\alpha)\,(\overline\alpha)
 \;=\;(\beta)\,(\overline\beta).
\]
```

## Full Candidate Proof

```text
Below is a self‐contained proof (apart from a routine gcd‐check in ℤ[i] which I have indicated and sketched) using unique factorization in the Gaussian integers ℤ[i].  All ring‐theoretic facts about ℤ[i] that we invoke are standard (class number 1, units ±1,±i, norm $N(x+iy)=x^2+y^2$).

Proof.  Suppose $a,b,c,d,e$ are distinct positive integers with
\[
a^4+b^4 \;=\;c^4+d^4\;=\;e^5.
\]
We work in the ring $\Bbb Z[i]$.  Set
\[
\alpha \;=\;a^2 + i\,b^2,\quad 
\overline\alpha \;=\;a^2 - i\,b^2,
\]
and similarly
\[
\beta  \;=\;c^2 + i\,d^2,\quad 
\overline\beta \;=\;c^2 - i\,d^2.
\]
Then
\[
N(\alpha)\;=\;\alpha\ \overline\alpha
 \;=\;(a^2)^2+(b^2)^2
 \;=\;a^4+b^4
 \;=\;e^5,
\]
and likewise $N(\beta)=\beta\,\overline\beta=e^5$.  Thus in $\Bbb Z[i]$ we have two factorizations of the principal ideal $(e^5)$:
\[
(e^5)\;=\;(\alpha)\,(\overline\alpha)
 \;=\;(\beta)\,(\overline\beta).
\]

Step 1.  The two factors $\alpha$ and $\overline\alpha$ are coprime in $\Bbb Z[i]$.  
Indeed, any common Gaussian divisor $\delta\mid\alpha,\overline\alpha$ must also divide
\[
\alpha+\overline\alpha \;=\;2a^2,
\qquad
\alpha-\overline\alpha \;=\;2i\,b^2.
\]
One checks by a short parity‐argument that no nonunit of $\Bbb Z[i]$ can divide both $2a^2$ and $2i\,b^2$ unless $2\mid e$ and both $a,b$ are even, in which case one can produce a strictly smaller solution by dividing everything by $2$ (an infinite‐descent contradiction).  Hence in any genuine solution one finds $\gcd(\alpha,\overline\alpha)=1$.  Similarly $\gcd(\beta,\overline\beta)=1$.

Step 2.  Since $\Bbb Z[i]$ is a UFD and
\[
\alpha\,\overline\alpha
 \;=\;(e)^5
\]
with $\gcd(\alpha,\overline\alpha)=1$, by the usual “coprime‐factors‐of‐a‐power are powers” lemma there exist a Gaussian integer $z=x+iy$ and a unit $u\in\{±1,±i\}$ such that
\[
\alpha \;=\;u\,(x+iy)^5,
\qquad
\overline\alpha \;=\;\overline u\,(x-iy)^5.
\]
Likewise, there is a (perhaps different) unit $v\in\{±1,±i\}$ and a Gaussian integer $w=p+iq$ such that
\[
\beta  \;=\;v\,(p+iq)^5,
\qquad
\overline\beta \;=\;\overline v\,(p-iq)^5.
\]

Step 3.  But the two factorizations
\[
(e)^5 \;=\;\alpha\,\overline\alpha
        \;=\;\beta\,\overline\beta
\]
in $\Bbb Z[i]$ must coincide up to re–ordering and units.  Thus the pair of “fifth‐power” factors
\[
\{\alpha,\overline\alpha\}
 \;=\;\{\,u\,(x+iy)^5,\;\overline u\,(x-iy)^5\}
\]
must be the same set (up to units) as
\[
\{\beta,\overline\beta\}
 \;=\;\{\,v\,(p+iq)^5,\;\overline v\,(p-iq)^5\}.
\]
We cannot have 
\[
\alpha\sim\beta
\]
(as Gaussian‐integer associates), because that forces
\[
a^2 + i\,b^2 \;=\;u'\,(c^2 + i\,d^2)
\]
for some unit $u'$, and equating real and imaginary parts in all four cases $u'=±1,±i$ leads at once to 
\[
\{a,b\}=\{c,d\},
\]
contradicting that $a,b,c,d$ are four distinct integers.  Hence the only possibility is
\[
\alpha\;\sim\;\overline\beta,
\]
i.e. 
\[
a^2 + i\,b^2
\;=\;
u'\,\bigl(c^2 - i\,d^2\bigr)
\quad
\text{and}
\quad
c^2 + i\,d^2
\;=\;
v'\,\bigl(a^2 - i\,b^2\bigr),
\]
for suitable units $u',v'\in\{±1,±i\}$.  

Step 4.  Multiply these two associate‐relations:
\[
\bigl(a^2 + i\,b^2\bigr)\,\bigl(c^2 + i\,d^2\bigr)
\;=\;
(u'v')\,
\bigl(c^2 - i\,d^2\bigr)\,\bigl(a^2 - i\,b^2\bigr).
\]
But the right‐hand side is just $u'v'$ times the complex conjugate of the left‐hand side.  On the other hand one checks directly
\[
(a^2 + i\,b^2)\,(c^2 + i\,d^2)
 \;=\;
a^2c^2 - b^2d^2
\;+\;i\,(a^2d^2 + b^2c^2).
\]
Thus
\[
a^2c^2 - b^2d^2 \;+\;i\,(a^2d^2 + b^2c^2)
 \;=\;
(u'v')\Bigl(a^2c^2 - b^2d^2 - i\,(a^2d^2 + b^2c^2)\Bigr).
\]
Since $a,b,c,d>0$, the imaginary‐part $a^2d^2+b^2c^2$ is strictly positive.  Checking the four possible values of the unit $u'v'\in\{±1,± i\}$ one finds that the only consistent choice is
\[
u'v' \;=\; i,
\]
which forces
\[
a^2c^2 - b^2d^2 \;=\;0,
\qquad
a^2d^2 + b^2c^2 \;=\;(x^2+y^2)^5 \;>\;0.
\]
Hence
\[
a^2c^2 \;=\;b^2d^2,
\]
and since $a,b,c,d$ are positive integers we get
\[
ac \;=\;bd.
\]
Finally
\[
ac + bd \;=\;2\,ac,
\]
and $ac>1$ (they are distinct positive integers), so $ac+bd\ge2\cdot2=4$ and is divisible by 2; hence it is composite.  □

Remark.  The only non‐elementary ingredient is the unique‐factorization property of $\Bbb Z[i]$, and the check that 
$\gcd(a^2+i\,b^2,\;a^2-i\,b^2)=1$ in $\Bbb Z[i]$, which follows by examining any common divisor and using parity/infinite descent to rule out a genuine Gaussian prime.
```

## Reviewer Note

Computation mistakes.
