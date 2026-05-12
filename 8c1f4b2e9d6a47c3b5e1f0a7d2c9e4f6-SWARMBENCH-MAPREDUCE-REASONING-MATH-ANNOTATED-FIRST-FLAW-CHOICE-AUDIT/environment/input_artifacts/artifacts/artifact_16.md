# artifact_16

Competition: IMOSL  
Problem ID: IMOSL_2013_4  
Year: 2013

This item is drawn from the INSAIT Open Proof Corpus. A human reviewer identified the first unrecoverable flaw in the proof below; a curator extracted four candidate excerpts from the proof text. Select the letter of the excerpt that contains the annotated flaw. Excerpts are ordered randomly, not by proof position.

## Problem

Let \( n \) be a positive integer, and consider a sequence \( a_{1}, a_{2}, \ldots, a_{n} \) of positive integers. Extend it periodically to an infinite sequence \( a_{1}, a_{2}, \ldots \) by defining \( a_{n+i}=a_{i} \) for all \( i \geq 1 \). If

\[
a_{1} \leq a_{2} \leq \cdots \leq a_{n} \leq a_{1}+n
\]

and

\[
a_{a_{i}} \leq n+i-1 \quad \text{for } i=1,2, \ldots, n,
\]

prove that

\[
a_{1}+\cdots+a_{n} \leq n^{2}.
\]

## Candidate Excerpts

### Option A

```text
In particular i + j − 1 ≤ 2n−1.  A slightly sharper check is possible: because a₁ itself must be ≤ n (indeed the i=1 case of a_{a_1} ≤ n forces a₁ ≤ n), one shows in fact i + a_i −1 ≤ n.  But even from the weaker upper bound i + a_i −1 ≤ 2n−1 we see that y = i+j−1 is certainly ≥1 and ≤2n−1.  In fact a little more care shows y ≤ n, but one does not really need that sharp a priori: once we prove injectivity, the codomain of Φ could be taken as {1,…,n}×{1,…,2n−1}, and the counting |D| ≤ n·(2n−1)=2n²−n would already force |D| ≤ n² whenever n≥1.  To stay within the statement, however, one checks with the stronger claim:
```

### Option B

```text
and since i ≤ n, it follows that
```

### Option C

```text
i + a_i − 1  ≤  n + n − 1  = 2n − 1.
```

### Option D

```text
a_i  ≤  a_n  ≤  a₁ + n  ≤  n + n,
```

## Full Candidate Proof

```text
Proof.  Set up a “Ferrers‐diagram’’ for the sequence by drawing, in the integer lattice, the cells

 D  =  { (i,j) ∈ ℤ² : 1 ≤ i ≤ n, 1 ≤ j ≤ a_i }.

Since row i has exactly a_i cells, the total number of cells is

 |D|  =  a₁ + a₂ + ⋯ + a_n.

We will exhibit an injective map Φ : D → {1,…,n}×{1,…,n}, which immediately gives

 a₁ + a₂ + ⋯ + a_n  =  |D|  ≤  n²,

and completes the proof.

Define Φ on a cell (i,j) ∈ D by

 Φ(i,j)  =  ( x, y ),  

where
 x  =  a_{\,a_i}  − (i−1),
 y  =  i  +  j  − 1.

We check (i) that 1 ≤ x,y ≤ n, and then (ii) that Φ is injective.

1.  Range‐check of the first coordinate.  By the given hypothesis for each i,

 a_{\,a_i}  ≤  (n + i − 1).

Hence

 x  =  a_{\,a_i}  − (i−1)  ≤  (n + i − 1)  − (i−1)  =  n.

On the other hand a_{\,a_i} ≥1 and i−1≥0, so

 x  =  a_{\,a_i} −(i−1)  ≥ 1.

Thus 1 ≤ x ≤ n.

2.  Range‐check of the second coordinate.  Since j runs from 1 up to a_i, we have

 1  ≤  j  ≤  a_i
 ⇒  1  ≤  i + j − 1  ≤  i + a_i − 1.

But monotonicity and the hypothesis a_n ≤ a₁ + n give

 a_i  ≤  a_n  ≤  a₁ + n  ≤  n + n,

and since i ≤ n, it follows that

 i + a_i − 1  ≤  n + n − 1  = 2n − 1.

In particular i + j − 1 ≤ 2n−1.  A slightly sharper check is possible: because a₁ itself must be ≤ n (indeed the i=1 case of a_{a_1} ≤ n forces a₁ ≤ n), one shows in fact i + a_i −1 ≤ n.  But even from the weaker upper bound i + a_i −1 ≤ 2n−1 we see that y = i+j−1 is certainly ≥1 and ≤2n−1.  In fact a little more care shows y ≤ n, but one does not really need that sharp a priori: once we prove injectivity, the codomain of Φ could be taken as {1,…,n}×{1,…,2n−1}, and the counting |D| ≤ n·(2n−1)=2n²−n would already force |D| ≤ n² whenever n≥1.  To stay within the statement, however, one checks with the stronger claim:

 Claim:  i + a_i −1 ≤ n.

Proof of claim.  From a_{\,a_i} ≤ n + i −1 and monotonicity a_1 ≤ a_{\,a_i}, we get

 a_1  ≤  a_{\,a_i}  ≤  n + i −1.

In particular, for i = n we find a_n ≤ n + n −1 = 2n−1; but also a_n ≤ a_1 + n ≤ n + n = 2n.  In fact a little bookkeeping with the i=1 inequality a_{a_1} ≤ n and monotonicity shows a₁ ≤ 1, hence a₁ = 1, and then inductively one sees i + a_i −1 ≤ n for all i.  (The details are routine and left to the reader.)  □

Thus 1 ≤ y = i+j−1 ≤ n, as required.

3.  Φ is injective.  Suppose

 Φ(i,j) = (x,y) = Φ(i′,j′).

Then
 a_{\,a_i} − (i−1)   =   a_{\,a_{i′}} − (i′−1),    …(1)
 i + j − 1   =   i′ + j′ − 1   ⇒   i+j = i′+j′.      …(2)

Subtracting (2) from (1) gives

 [a_{\,a_i} − (i−1)] − (i+j−(i′+j′)) 
 = a_{\,a_{i}} − a_{\,a_{i′}}  − [(i−1) − (i′−1)]  − (i−i′ + j−j′)
 = 0,

which simplifies (using i+j = i′+j′) to

 a_{\,a_i} = a_{\,a_{i′}}.

But then from (1) already we get (i−1) = (i′−1), so i = i′.  Finally from i+j = i′+j′ we conclude j = j′.  Hence (i,j) = (i′,j′) and Φ is injective.

▢

Therefore Φ embeds the |D| = a₁+⋯+a_n cells into an n×n grid, proving

 a₁ + a₂+ ⋯ + a_n  =  |D|  ≤  n².

That completes the proof.
```

## Reviewer Note

False claim, "proof" skipped.
