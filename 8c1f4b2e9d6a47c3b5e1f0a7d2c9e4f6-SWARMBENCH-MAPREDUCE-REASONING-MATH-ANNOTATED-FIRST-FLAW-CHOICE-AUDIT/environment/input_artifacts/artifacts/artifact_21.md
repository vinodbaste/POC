# artifact_21

Competition: IMOSL  
Problem ID: IMOSL_2007_13  
Year: 2007

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Find all surjective functions \( f: \mathbb{N} \rightarrow \mathbb{N} \) such that for every \( m, n \in \mathbb{N} \) and every prime \( p \), the number \( f(m+n) \) is divisible by \( p \) if and only if \( f(m)+f(n) \) is divisible by \( p \).

## Candidate Excerpts

### Option A

```text
2.  We now prove that for each prime p, the reduction of f modulo p is a “linear” function of n.  
 Define  
  α_p(n) ≡ f(n) (mod p)  ∈ ℤ/pℤ.  
 The given condition is exactly  
  α_p(m+n)=0   ⇔   α_p(m)+α_p(n)=0  
 as an equivalence in ℤ/pℤ.  
 We claim that this forces α_p to be of the form  
  α_p(n)=c_p·n   in ℤ/pℤ,  
 for some constant c_p∈(ℤ/pℤ)^×.
```

### Option B

```text
α_p(n+a)=0   ⇔   α_p(n)+α_p(a)=0
  ⟹    α_p(n+a)=0   ⇔   α_p(n)=−1
  ⟹    α_p(n)=−1   ⇔   α_p(n+a)=0.
```

### Option C

```text
1.  First we show f(1)=1.  
 Since f is onto ℕ there is some k with f(k)=1.  Now for each prime p we plug m=n=k into the hypothesis:  
 p│f(2k) ⇔ p│(f(k)+f(k))=2·1.  
 If p=2, then both sides are “true,” so no contradiction.  If p≠2, then 2∤2·1 so the right‐hand side is false, whence p∤f(2k).  Thus for every odd prime p, p∤f(2k).  
 Next plug m=2k, n=k:  
 p│f(3k) ⇔ p│(f(2k)+f(k)).  
 For every odd p we have just seen p∤f(2k), and also p∤f(k)=1; hence for p>2 the right side is false, so p∤f(3k).  
 Continuing in this way, one sees that no odd prime ever divides any f(Nk).  In particular, no odd prime divides f(k)=1, a contradiction unless k=1.  Hence f(1)=1.
```

### Option D

```text
Proof of the claim.  Since f is onto ℕ there is some a with f(a)≡1 (mod p), so α_p(a)=1.  Now for any n we write
```

## Full Candidate Proof

```text
Here is a completely elementary proof that the only surjective solution of

  “For every prime p and every m,n∈ℕ, p divides f(m+n) ⇔ p divides f(m)+f(n)” 

is the identity f(n)=n.

Proof.  

1.  First we show f(1)=1.  
 Since f is onto ℕ there is some k with f(k)=1.  Now for each prime p we plug m=n=k into the hypothesis:  
 p│f(2k) ⇔ p│(f(k)+f(k))=2·1.  
 If p=2, then both sides are “true,” so no contradiction.  If p≠2, then 2∤2·1 so the right‐hand side is false, whence p∤f(2k).  Thus for every odd prime p, p∤f(2k).  
 Next plug m=2k, n=k:  
 p│f(3k) ⇔ p│(f(2k)+f(k)).  
 For every odd p we have just seen p∤f(2k), and also p∤f(k)=1; hence for p>2 the right side is false, so p∤f(3k).  
 Continuing in this way, one sees that no odd prime ever divides any f(Nk).  In particular, no odd prime divides f(k)=1, a contradiction unless k=1.  Hence f(1)=1.

2.  We now prove that for each prime p, the reduction of f modulo p is a “linear” function of n.  
 Define  
  α_p(n) ≡ f(n) (mod p)  ∈ ℤ/pℤ.  
 The given condition is exactly  
  α_p(m+n)=0   ⇔   α_p(m)+α_p(n)=0  
 as an equivalence in ℤ/pℤ.  
 We claim that this forces α_p to be of the form  
  α_p(n)=c_p·n   in ℤ/pℤ,  
 for some constant c_p∈(ℤ/pℤ)^×.

 Proof of the claim.  Since f is onto ℕ there is some a with f(a)≡1 (mod p), so α_p(a)=1.  Now for any n we write

  α_p(n+a)=0   ⇔   α_p(n)+α_p(a)=0
  ⟹    α_p(n+a)=0   ⇔   α_p(n)=−1
  ⟹    α_p(n)=−1   ⇔   α_p(n+a)=0.

 Thus the zero‐set of α_p is exactly the translate by +a of the residue −1∈ℤ/pℤ.  One shows by standard semigroup–translation arguments that the only way a function ℕ→ℤ/pℤ can have its zero‐set a single translate of one point and satisfy “m+n in the zero‐set ⇔ α_p(m)+α_p(n)=0” is if α_p is a ℤ‐linear map on ℕ.  Concretely one checks that for any r∈ℤ/pℤ the set { n:α_p(n)=r } is again a single translate of that same subgroup, and from the functional equation one deduces step by step that

  α_p(n)=n·α_p(1)+(ℤ/pℤ)·0=n·α_p(1).

 Setting c_p=α_p(1), which is invertible in ℤ/pℤ because otherwise p∣f(n) for all n and f could not be onto 1, we obtain α_p(n)=c_p n.

3.  Conclusion by the Chinese Remainder Theorem.  
 We have shown that for every prime p

  f(n)≡c_p n   (mod p), c_p∈(ℤ/pℤ)^×.  

 By the Chinese Remainder Theorem, for each finite set of primes {p_1,…,p_k} there is exactly one residue C modulo P=p_1⋯p_k which satisfies

  C≡c_{p_i}   (mod p_i), i=1,…,k.

 Hence for every n,

  f(n)≡C·n   (mod P).

 Since this holds for every finite product P of primes, it follows that f(n)−C n is divisible by arbitrarily large integers.  The only way an integer can be divisible by every P is for it to be zero.  Therefore

  f(n)=C·n

 exactly, for all n.  Finally, surjectivity of f:ℕ→ℕ forces C=1 (otherwise all values would be multiples of C>1).  Hence

  f(n)=n

for every n∈ℕ.  It is immediate to check that f(n)=n indeed satisfies “p∣f(m+n) ⇔ p∣(f(m)+f(n)),” and so no other surjective solutions exist. □

Remark.  The heart of the proof is the reduction mod p and the observation that a function ℕ→ℤ/pℤ whose zero‐locus is always “shifted” exactly when one argument is shifted must be ℤ‐linear.  The rest is a routine application of the Chinese Remainder Theorem.
```

## Reviewer Note

A reasoning mistake and a computation mistake.
