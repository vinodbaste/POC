# artifact_45

Competition: IMOSL  
Problem ID: IMOSL_2014_2  
Year: 2014

From the Open Proof Corpus benchmark set. One of the four candidate excerpts below corresponds to the first step that was marked unrecoverable by a human reviewer of this proof attempt. The excerpts appear in randomized order. Select the correct letter.

## Problem

Let \(a, b\) be integers with \(b \ne 0\).  Prove that \(\gcd(a, b) = \gcd(a, a+b)\).

## Candidate Excerpts

### Option A

```text
The set of common divisors of \(a\) and \(b\) equals the set of common divisors of
\(a\) and \(a+b\), because any integer that divides both \(a\) and \(b\) automatically
divides \(a+b\), and any integer that divides \(a\) and \(a+b\) automatically divides
\(b+a\) (same as \(a+b\)).  Hence the two gcd values are equal.
```

### Option B

```text
Formally: if \(d \mid a\) and \(d \mid b\), then \(d \mid a+b\).  Conversely, if
\(d \mid a\) and \(d \mid a+b\), then \(d \mid (a+b)-a = b\).
```

### Option C

```text
Therefore the sets of common divisors coincide:
\(\{d : d \mid a \text{ and } d \mid b\} = \{d : d \mid a \text{ and } d \mid a+b\}\).
```

### Option D

```text
The maximum of each set is the respective gcd, so
\(\gcd(a,b) = \gcd(a,a+b)\).  \(\square\)
```

## Full Candidate Proof

```text
The set of common divisors of a and b equals the set of common divisors of
a and a+b, because any integer that divides both a and b automatically
divides a+b, and any integer that divides a and a+b automatically divides
b+a (same as a+b).  Hence the two gcd values are equal.

Formally: if d|a and d|b, then d|a+b.  Conversely, if
d|a and d|a+b, then d|(a+b)−a=b.

Therefore the sets of common divisors coincide:
{d : d|a and d|b} = {d : d|a and d|a+b}.

The maximum of each set is the respective gcd, so
gcd(a,b)=gcd(a,a+b). □
```

## Reviewer Note

The initial overview conflates two quantities in the converse direction: it claims divisibility of \(b+a\) (which is trivial and useless) instead of deriving divisibility of \(b\) by subtracting \(a\).
