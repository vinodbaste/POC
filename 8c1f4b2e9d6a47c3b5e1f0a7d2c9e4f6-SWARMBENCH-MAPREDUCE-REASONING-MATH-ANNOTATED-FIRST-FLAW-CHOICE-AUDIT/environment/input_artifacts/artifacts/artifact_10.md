# artifact_10

Competition: USAMO  
Problem ID: USAMO_2015_5  
Year: 2015

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let \(a, b, c, d, e\) be distinct positive integers such that \(a^{4}+b^{4}=c^{4}+d^{4}=e^{5}\). Show that \(a c+b d\) is a composite number.

## Candidate Excerpts

### Option A

```text
Define in \(\Bbb Z[i]\) the two elements
\[
\alpha \;:=\; a^2 + i\,b^2,
\qquad
\beta \;:=\; c^2 + i\,d^2.
\]
Since
\[
N(\alpha)\;=\;a^4+b^4
\;=\;e^5
\;=\;c^4+d^4
\;=\;N(\beta),
\]
we have
\[
\alpha\;\overline\alpha
\;=\;\beta\;\overline\beta
\;=\;e^5.
\]
Because \(\Bbb Z[i]\) is a UFD, the multiset of Gaussian–prime factors of \(\alpha\,\overline\alpha\) is the same as that of \(\beta\,\overline\beta\).  We claim that \(\alpha\) and \(\beta\) are not coprime in \(\Bbb Z[i]\).  Indeed, if \(\gcd(\alpha,\beta)=1\) then, up to units, the prime factors of \(\alpha\) together with those of \(\overline\alpha\) would partition the prime factors of \(e^5\) into two disjoint subsets of equal total multiplicity.  But \(5\) is odd, so no such partition is possible.  Concretely, coprimality would force
\[
\alpha \;=\; u\,\overline\beta
\quad\text{for some unit }u\in\{\,\pm1,\pm i\},
\]
and comparing real and imaginary parts of
\(
a^2 + i\,b^2
=
u\,(c^2 - i\,d^2)
\)
quickly contradicts the positivity (and distinctness) of \(a,b,c,d\).  Hence
\[
\delta\;:=\;\gcd(\alpha,\beta)
\]
is a nonunit in \(\Bbb Z[i]\).
```

### Option B

```text
Next, since
\[
\alpha=(a^2+i\,b^2)=(a+i\,b)(a-i\,b)
\quad\text{and}\quad
\beta=(c^2+i\,d^2)=(c+i\,d)(c-i\,d),
\]
the Gaussian prime \(\delta\) divides the product \((a+i\,b)(a-i\,b)\).  Hence by primality in the UFD \(\Bbb Z[i]\), \(\delta\) divides one of the two factors \(a+i\,b\) or \(a-i\,b\).  Similarly, \(\delta\) divides one of \(c+i\,d\) or \(c-i\,d\).  We examine the four cases in turn:
```

### Option C

```text
We now show that \(\delta\) yields a nontrivial rational divisor of \(ac+bd\).  Observe first that \(\delta\) cannot be an associate of the unique Gaussian prime dividing \(2\), namely \(1+i\).  Indeed, if \(1+i\mid\delta\), then
\[
2\mid N(\delta)\;\Bigl|
\;N(\alpha)\;=\;e^5,
\]
so \(2\mid e\).  But then \(32\mid e^5=a^4+b^4\), and one checks easily that no sum of two fourth powers of integers is divisible by \(32\).  Thus \(\gcd(\delta,1+i)=1\) and in particular \(\gcd(\delta,2)=1\).
```

### Option D

```text
Case 1: \(\delta\mid(a+i\,b)\) and \(\delta\mid(c-i\,d)\).  Then
\[
\delta\;\bigm|\;(a+i\,b)(c-i\,d)
\;=\;ac+bd\;+\;i\,(bc-ad).
\]
Taking real parts, \(\delta\) divides the Gaussian integer
\[
X\;=\;(a+i\,b)(c-i\,d)+(a-i\,b)(c+i\,d)
\;=\;2\,(ac+bd).
\]
But \(\gcd(\delta,2)=1\), so in fact \(\delta\mid (ac+bd)\) in \(\Bbb Z[i]\).
```

## Full Candidate Proof

```text
Proof.  We work in the Gaussian‐integer ring \(\Bbb Z[i]\), which is well-known to be a unique factorization domain (UFD).  Recall that for any \(\alpha=x+iy\in\Bbb Z[i]\) its norm is  
\[
N(\alpha)\;=\;\alpha\bar\alpha
\;=\;(x+iy)(x-iy)
\;=\;x^2+y^2,
\] 
and that in a UFD a prime dividing a product must divide one of the factors.

Define in \(\Bbb Z[i]\) the two elements
\[
\alpha \;:=\; a^2 + i\,b^2,
\qquad
\beta \;:=\; c^2 + i\,d^2.
\]
Since
\[
N(\alpha)\;=\;a^4+b^4
\;=\;e^5
\;=\;c^4+d^4
\;=\;N(\beta),
\]
we have
\[
\alpha\;\overline\alpha
\;=\;\beta\;\overline\beta
\;=\;e^5.
\]
Because \(\Bbb Z[i]\) is a UFD, the multiset of Gaussian–prime factors of \(\alpha\,\overline\alpha\) is the same as that of \(\beta\,\overline\beta\).  We claim that \(\alpha\) and \(\beta\) are not coprime in \(\Bbb Z[i]\).  Indeed, if \(\gcd(\alpha,\beta)=1\) then, up to units, the prime factors of \(\alpha\) together with those of \(\overline\alpha\) would partition the prime factors of \(e^5\) into two disjoint subsets of equal total multiplicity.  But \(5\) is odd, so no such partition is possible.  Concretely, coprimality would force
\[
\alpha \;=\; u\,\overline\beta
\quad\text{for some unit }u\in\{\,\pm1,\pm i\},
\]
and comparing real and imaginary parts of
\(
a^2 + i\,b^2
=
u\,(c^2 - i\,d^2)
\)
quickly contradicts the positivity (and distinctness) of \(a,b,c,d\).  Hence
\[
\delta\;:=\;\gcd(\alpha,\beta)
\]
is a nonunit in \(\Bbb Z[i]\).

We now show that \(\delta\) yields a nontrivial rational divisor of \(ac+bd\).  Observe first that \(\delta\) cannot be an associate of the unique Gaussian prime dividing \(2\), namely \(1+i\).  Indeed, if \(1+i\mid\delta\), then
\[
2\mid N(\delta)\;\Bigl|
\;N(\alpha)\;=\;e^5,
\]
so \(2\mid e\).  But then \(32\mid e^5=a^4+b^4\), and one checks easily that no sum of two fourth powers of integers is divisible by \(32\).  Thus \(\gcd(\delta,1+i)=1\) and in particular \(\gcd(\delta,2)=1\).

Next, since
\[
\alpha=(a^2+i\,b^2)=(a+i\,b)(a-i\,b)
\quad\text{and}\quad
\beta=(c^2+i\,d^2)=(c+i\,d)(c-i\,d),
\]
the Gaussian prime \(\delta\) divides the product \((a+i\,b)(a-i\,b)\).  Hence by primality in the UFD \(\Bbb Z[i]\), \(\delta\) divides one of the two factors \(a+i\,b\) or \(a-i\,b\).  Similarly, \(\delta\) divides one of \(c+i\,d\) or \(c-i\,d\).  We examine the four cases in turn:

Case 1: \(\delta\mid(a+i\,b)\) and \(\delta\mid(c-i\,d)\).  Then
\[
\delta\;\bigm|\;(a+i\,b)(c-i\,d)
\;=\;ac+bd\;+\;i\,(bc-ad).
\]
Taking real parts, \(\delta\) divides the Gaussian integer
\[
X\;=\;(a+i\,b)(c-i\,d)+(a-i\,b)(c+i\,d)
\;=\;2\,(ac+bd).
\]
But \(\gcd(\delta,2)=1\), so in fact \(\delta\mid (ac+bd)\) in \(\Bbb Z[i]\).

Case 2: \(\delta\mid(a+i\,b)\) and \(\delta\mid(c+i\,d)\).  Then similarly
\[
\delta\;\bigm|\;(a-i\,b)(c-i\,d)
\;=\;(ac+bd)\;+\;i\,(ad-bc),
\]
so again \(\delta\mid 2\,(ac+bd)\), and by \(\gcd(\delta,2)=1\) we get \(\delta\mid(ac+bd)\).

Cases 3 and 4, in which \(\delta\) divides \(a-i\,b\), proceed by the same two‐by‐two check of which of \(c\pm i\,d\) it also divides; in each case one finds \(\delta\mid 2\,(ac+bd)\) and hence \(\delta\mid(ac+bd)\).  

Thus in every case \(\delta\) is a nonunit Gaussian divisor of the real integer \(ac+bd\).  Let \(p\) be any rational prime divisor of the Gaussian‐integer norm \(N(\delta)\).  Then
\[
p\;=\;N(\pi)
\quad\text{for some Gaussian prime }\pi\mid\delta,
\]
and since \(\pi\mid\delta\mid (ac+bd)\) in \(\Bbb Z[i]\), taking norms shows
\[
p\;\Bigm|\;N(ac+bd)\;=\;(ac+bd)^2
\;\Longrightarrow\;
p\mid(ac+bd).
\]
Finally, \(1<p\le p^e\le N(\delta)\le N(\alpha)=e^5\), while
\[
ac+bd\;>\;e
\quad(\text{since }a^4+b^4=e^5\text{ and }c^4+d^4=e^5
\text{ imply }a^2+b^2>e^2,\;c^2+d^2>e^2,\text{ whence }ac+bd>e).
\]
Hence \(p\) is a proper nontrivial divisor of the positive integer \(ac+bd\).  We conclude that
\[
ac+bd
\]
is composite, as claimed.  \(\boxed{}\)
```

## Reviewer Note

Computation mistakes.
