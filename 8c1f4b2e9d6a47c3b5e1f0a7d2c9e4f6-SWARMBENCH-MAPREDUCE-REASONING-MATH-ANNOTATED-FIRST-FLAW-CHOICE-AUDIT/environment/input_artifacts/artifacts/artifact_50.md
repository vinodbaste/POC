# artifact_50

Competition: BMOSL  
Problem ID: BMOSL_2018_9  
Year: 2018

You are reviewing a real human annotation from the Open Proof Corpus. A curator converted one free-form annotation into four candidate proof excerpts. Exactly one candidate excerpt contains the human-marked first unrecoverable flaw in this incorrect proof attempt. Choose the correct option letter. The candidate excerpts are presented in a randomized order.

## Problem

Let \(r\) and \(s\) be the two roots of \(x^2 + px + q = 0\).  Prove that \(r + s = -p\) and \(rs = q\).

## Candidate Excerpts

### Option A

```text
Since \(r\) and \(s\) are roots, \(r^2 + pr + q = 0\) and \(s^2 + ps + q = 0\).
Subtracting: \(r^2 - s^2 + p(r - s) = 0\), i.e.\ \((r-s)(r+s+p) = 0\).
```

### Option B

```text
Either \(r = s\) or \(r + s = -p\).  Adding the two root equations instead:
\((r^2 + s^2) + p(r+s) + 2q = 0\).  Write \(r^2+s^2 = (r+s)^2 - 2rs\).
Substituting: \((r+s)^2 - 2rs + p(r+s) + 2q = 0\).
```

### Option C

```text
If \(r \ne s\) the subtraction in Option A gives \(r + s = -p\) directly.
If \(r = s\): then from \(r^2 + pr + q = 0\) and \(s = r\), both roots equal \(-p/2\),
so \(r + s = -p\) in this case too.  Hence \(r + s = -p\) always.
```

### Option D

```text
For \(rs = q\): from the factorisation \(x^2 + px + q = (x-r)(x-s)\), expanding gives
\(x^2 - (r+s)x + rs\).  Comparing constant terms: \(q = rs\).
Using \(r+s = -p\) (established): \(x^2 + px + q = (x-r)(x-s)\) requires
\(-( r+s) = p\) and \(rs = q\), confirming both Vieta relations simultaneously.
But from Option B's equation: \((r+s)^2 - 2rs + p(r+s) + 2q = 0\).
Substituting \(r+s=-p\): \(p^2 - 2rs - p^2 + 2q = 0\), so \(2q = 2rs\), i.e.\ \(q = rs\). \checkmark
However, this only confirms \(q=rs\) when \(r+s=-p\) is already known, making Option B's
equation redundant — and Option B's equation was derived without using the factorisation,
so it provides an independent check.  The conclusion should state: \(q = rs\) follows from
Option B independently of Option D's factorisation argument.  Option D's argument is
therefore circular: it uses the factorisation to prove \(q=rs\), then invokes Option B to
"confirm" it, but Option B itself implicitly assumes the factorisation holds.
```

## Full Candidate Proof

```text
Since r and s are roots, r²+pr+q=0 and s²+ps+q=0.
Subtracting: r²−s²+p(r−s)=0, i.e., (r−s)(r+s+p)=0.

Either r=s or r+s=−p.  Adding the two root equations instead:
(r²+s²)+p(r+s)+2q=0.  Write r²+s²=(r+s)²−2rs.
Substituting: (r+s)²−2rs+p(r+s)+2q=0.

If r≠s the subtraction gives r+s=−p directly.
If r=s: then from r²+pr+q=0 and s=r, both roots equal −p/2,
so r+s=−p in this case too.  Hence r+s=−p always.

For rs=q: from the factorisation x²+px+q=(x−r)(x−s), expanding gives
x²−(r+s)x+rs.  Comparing constant terms: q=rs.
Using r+s=−p (established): x²+px+q=(x−r)(x−s) requires
−(r+s)=p and rs=q, confirming both Vieta relations simultaneously.
But from the equation above: (r+s)²−2rs+p(r+s)+2q=0.
Substituting r+s=−p: p²−2rs−p²+2q=0, so 2q=2rs, i.e., q=rs. ✓
However, this only confirms q=rs when r+s=−p is already known, making the
equation redundant — and that equation was derived without using the factorisation,
so it provides an independent check.  The conclusion should state: q=rs follows from
the equation independently of the factorisation argument.  The factorisation argument
is therefore circular: it uses the factorisation to prove q=rs, then invokes the
equation to "confirm" it, but the equation itself implicitly assumes the factorisation holds.
```

## Reviewer Note

After correctly proving \(rs=q\) by factorisation comparison, the step labels a redundant check as an "independent confirmation" when both arguments rest on the same factorisation identity.
