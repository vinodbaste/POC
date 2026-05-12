# artifact_49

Competition: USAMO  
Problem ID: USAMO_2020_5  
Year: 2020

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

A *derangement* of \(\{1,\ldots,n\}\) is a permutation with no fixed point.
Prove that the number of derangements satisfies
\[
D(n) \;=\; n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.
\]

## Candidate Excerpts

### Option A

```text
Let \(A_i\) be the set of permutations of \(\{1,\ldots,n\}\) that fix element \(i\).
Then \(|A_i| = (n-1)!\), and for distinct \(i,j\): \(|A_i \cap A_j| = (n-2)!\).
More generally, for any \(k\)-element subset \(S\):
\(\bigl|\bigcap_{i\in S} A_i\bigr| = (n-k)!\).
```

### Option B

```text
By inclusion-exclusion, the number of permutations with at least one fixed point is
\[
\Bigl|\bigcup_{i=1}^n A_i\Bigr|
= \sum_{k=1}^{n}(-1)^{k-1}\binom{n}{k}(n-k)!.
\]
```

### Option C

```text
Since \(\binom{n}{k}(n-k)! = n!/k!\), the number of permutations with at least one
fixed point simplifies to \(n!\sum_{k=1}^{n}(-1)^{k-1}/k!\).  Therefore
\[
D(n) = n! - n!\sum_{k=1}^{n}\frac{(-1)^{k-1}}{k!}
     = n!\Bigl(1 - \sum_{k=1}^{n}\frac{(-1)^{k-1}}{k!}\Bigr)
     = n!\sum_{k=0}^{n}\frac{(-1)^k}{k!},
\]
where the last step absorbs the \(-(-1)^{k-1} = (-1)^k\) sign flip and adds the \(k=0\) term.
```

### Option D

```text
Verify for \(n = 2\): \(D(2) = 2!(1 - 1 + \tfrac{1}{2}) = 2\cdot\tfrac{1}{2} = 1\). \checkmark
\(n=3\): \(D(3) = 6(1-1+\tfrac{1}{2}-\tfrac{1}{6}) = 6\cdot\tfrac{2}{6}=2\). \checkmark
\(\square\)
```

## Full Candidate Proof

```text
Let A_i be the set of permutations of {1,…,n} that fix element i.
Then |A_i|=(n−1)!, and for distinct i,j: |A_i∩A_j|=(n−2)!.
More generally, for any k-element subset S: |⋂_{i∈S}A_i|=(n−k)!.

By inclusion-exclusion, the number of permutations with at least one fixed point is
|⋃_{i=1}^n A_i| = ∑_{k=1}^{n}(−1)^{k−1}·C(n,k)·(n−k)!.

Since C(n,k)·(n−k)!=n!/k!, the count simplifies to n!·∑_{k=1}^{n}(−1)^{k−1}/k!.
Therefore
D(n) = n! − n!·∑_{k=1}^{n}(−1)^{k−1}/k!
     = n!·(1 − ∑_{k=1}^{n}(−1)^{k−1}/k!)
     = n!·∑_{k=0}^{n}(−1)^k/k!,
where the last step absorbs the sign flip and adds the k=0 term.

Verify for n=2: D(2)=2!(1−1+1/2)=2·1/2=1. ✓
n=3: D(3)=6(1−1+1/2−1/6)=6·2/6=2. ✓ □
```

## Reviewer Note

The central fact \(\lvert\bigcap_{i\in S}A_i\rvert = (n-k)!\) for any \(k\)-element set \(S\) is stated without proof; the argument for why fixing \(k\) elements leaves exactly \((n-k)!\) permutations of the rest is the step that must be established first.
