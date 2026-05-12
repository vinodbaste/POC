# artifact_48

Competition: IMOSL  
Problem ID: IMOSL_2015_6  
Year: 2015

From the Open Proof Corpus benchmark set. One of the four candidate excerpts below corresponds to the first step that was marked unrecoverable by a human reviewer of this proof attempt. The excerpts appear in randomized order. Select the correct letter.

## Problem

A *derangement* of \(\{1,\ldots,n\}\) is a permutation with no fixed point.
Using inclusion-exclusion, prove that the number of derangements satisfies
\[
D(n) \;=\; n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.
\]

## Candidate Excerpts

### Option A

```text
For each \(S \subseteq \{1,\ldots,n\}\) with \(|S|=k\), the set of permutations
fixing every element of \(S\) has size \((n-k)!\).
By inclusion-exclusion, the number of permutations with NO fixed point is
\[
D(n) = \sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)!.
\]
```

### Option B

```text
Since \(\binom{n}{k}(n-k)! = n!/k!\), we simplify:
\[
D(n) = \sum_{k=0}^{n}(-1)^k\frac{n!}{k!} = n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.  \square
\]
```

### Option C

```text
Sanity check for n=3:
\[
D(3) = 3!\Bigl(1 - 1 + \tfrac{1}{2} - \tfrac{1}{6}\Bigr)
     = 6 \cdot \tfrac{2}{6} = 2. \checkmark
\]
```

### Option D

```text
And for n=4:
\[
D(4) = 4!\Bigl(1-1+\tfrac{1}{2}-\tfrac{1}{6}+\tfrac{1}{24}\Bigr)
     = 24 \cdot \tfrac{9}{24} = 9. \checkmark
\]
```

## Full Candidate Proof

```text
For each i∈{1,…,n}, let A_i be the set of permutations of {1,…,n} that fix i.
Then |A_i|=(n−1)!, and for any k-element subset S⊆{1,…,n}:
|⋂_{i∈S} A_i| = (n−k)!.

By inclusion-exclusion, the number of permutations with NO fixed point is
D(n) = ∑_{k=0}^{n}(−1)^k·C(n,k)·(n−k)!.

Since C(n,k)·(n−k)!=n!/k!, we simplify:
D(n) = n!·∑_{k=0}^{n}(−1)^k/k!. □

Sanity check for n=3:
D(3) = 3!·(1−1+1/2−1/6) = 6·2/6 = 2. ✓

And for n=4:
D(4) = 4!·(1−1+1/2−1/6+1/24) = 24·9/24 = 9. ✓
```

## Reviewer Note

The inclusion-exclusion formula is stated as a direct result without verifying that the size of each intersection \(\lvert\bigcap_{i\in S}A_i\rvert = (n-k)!\) holds, which is the key step that must be established before the formula can be written down.
