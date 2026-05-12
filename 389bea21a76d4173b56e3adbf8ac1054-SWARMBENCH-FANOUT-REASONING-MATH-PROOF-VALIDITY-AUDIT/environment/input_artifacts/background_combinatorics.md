# Domain Background: Combinatorics Proof Evaluation

This reference covers the mathematical theory, common proof techniques, and evaluation criteria relevant to olympiad combinatorics problems. Sub-agents auditing **proof_12**, **proof_13**, **proof_15**, and **proof_19** should read this document before evaluating their assigned proof.

---

## Part I: Counting and Combinatorial Identities

### 1.1 Basic Counting Principles

**Addition principle:** If events A and B are mutually exclusive, |A∪B| = |A|+|B|.

**Multiplication principle:** If a process has m choices at step 1 and n choices at step 2 (independent of step 1), there are mn total possibilities.

**Binomial coefficients:** C(n,k) = n!/(k!(n-k)!) counts k-element subsets of an n-element set.

**Pascal's identity:** C(n,k) = C(n-1,k-1) + C(n-1,k).

**Vandermonde's identity:** Σ_{k=0}^r C(m,k)·C(n,r-k) = C(m+n,r).

**Evaluation criterion:** When a proof counts in two ways, both expressions must count the SAME set of objects. A one-to-one correspondence must be established clearly.

### 1.2 Double Counting

**Method:** Count a set S of pairs (object, property) in two ways:
- By object: Σ_{x ∈ X} (number of properties x has)
- By property: Σ_{P ∈ Properties} (number of objects with property P)

Both sides equal |S|.

**Evaluation criterion:** The set S must be clearly defined. Both counting methods must correctly enumerate elements of S without over- or under-counting.

### 1.3 Stars and Bars

The number of ways to write n as an ordered sum of k non-negative integers is C(n+k-1, k-1). This counts solutions to x₁+x₂+...+xₖ = n with xᵢ ≥ 0.

For positive integers (xᵢ ≥ 1): substitute yᵢ = xᵢ-1, getting y₁+...+yₖ = n-k, count C(n-1, k-1).

### 1.4 Inclusion-Exclusion

|A₁∪A₂∪...∪Aₙ| = Σ|Aᵢ| - Σ|Aᵢ∩Aⱼ| + Σ|Aᵢ∩Aⱼ∩Aₖ| - ... + (-1)^{n+1}|A₁∩...∩Aₙ|

**Derangements:** D(n) = n! Σ_{k=0}^n (-1)^k/k! = n!(1-1+1/2!-1/3!+...) ≈ n!/e.

---

## Part II: Graph Theory and Combinatorial Structures

### 2.1 Graph Theory Basics

A graph G = (V, E) with vertex set V and edge set E. Key properties:
- Simple graph: no multi-edges, no self-loops
- Complete graph K_n: every pair of vertices connected
- Bipartite graph K_{m,n}: vertices split into two groups, edges only between groups
- Tree: connected graph with no cycles; has exactly n-1 edges for n vertices

**Pigeonhole principle:** If n objects are placed in k bins and n > k, at least one bin has at least ⌈n/k⌉ objects.

**Handshaking lemma:** Σ_{v∈V} deg(v) = 2|E|.

### 2.2 Matchings and Hall's Theorem

A **matching** in a bipartite graph is a set of edges with no shared vertices.

**Hall's marriage theorem:** A bipartite graph G = (A∪B, E) has a matching saturating all of A if and only if for every subset S ⊆ A, |N(S)| ≥ |S| (where N(S) is the neighborhood of S in B).

**Perfect matching:** Matches every vertex. In K_{n,n}, there are n! perfect matchings.

**Evaluation criterion:** When a proof claims a matching or bijection exists, it must either exhibit one explicitly or invoke Hall's theorem with verification of the Hall condition.

---

## Part III: Boolean Lattice and Subset Systems

### 3.1 The Boolean Lattice

The power set 2^S of a set S = {1,...,n} with the partial order of inclusion forms the Boolean lattice B_n. Key properties:
- |B_n| = 2^n
- Ranked by cardinality: rank k level has C(n,k) elements
- Graded poset with n+1 ranks

**Intervals in the Boolean lattice:** For A ⊆ B ⊆ S, the interval [A,B] = {C : A⊆C⊆B} is isomorphic to B_{|B|-|A|} and has 2^{|B|-|A|} elements.

### 3.2 Chains and Antichains

A **chain** is a totally ordered subset (any two elements comparable). A **antichain** is a set of mutually incomparable elements (no containments).

**Dilworth's theorem:** The minimum number of chains needed to cover the poset equals the maximum antichain size.

**Sperner's theorem:** The maximum antichain in B_n has size C(n, ⌊n/2⌋) (take all subsets of size ⌊n/2⌋).

### 3.3 Multiplicative Functions on the Boolean Lattice

A function f: 2^S → ℝ is **multiplicative** over (∪, ∩) if f(T₁)·f(T₂) = f(T₁∪T₂)·f(T₁∩T₂) for all T₁,T₂ ⊆ S.

This is a strong structural condition. Not every function satisfying this for "many pairs" satisfies it for all pairs.

**Evaluation criterion:** A proof that f satisfies the multiplicative condition must verify it for ALL pairs (T₁, T₂), not just specific families. The verification "one checks by routine computation" is a placeholder that must be backed by an actual argument. If the proof leaves this verification implicit and it is genuinely non-trivial, this constitutes a critical skipped step.

**Characterization theorem:** The non-negative functions f: 2^S → ℝ satisfying f(T₁)f(T₂) = f(T₁∪T₂)f(T₁∩T₂) are exactly those of the form f(T) = 2^{|T∩A|} for some A⊆S (when f(∅)=1), or f(T) = χ_{[U,U∪A']}(T) extended multiplicatively (when f(∅)=0).

### 3.4 Möbius Inversion on the Boolean Lattice

The Möbius function for the Boolean lattice B_n is μ(A,B) = (-1)^{|B|-|A|} for A ⊆ B.

**Inversion formula:** If g(T) = Σ_{U⊆T} f(U) for all T, then f(T) = Σ_{U⊆T} (-1)^{|T|-|U|} g(U).

**Application to blue-set counting:** If f(T) = #{blue subsets of T}, then the indicator of whether T itself is blue is:
1_B(T) = Σ_{U⊆T} (-1)^{|T|-|U|} f(U)

This is the Möbius inversion of f (where f(T) = Σ_{U∈B, U⊆T} 1 = Σ_{U⊆T} 1_B(U) is the cumulative count).

**Evaluation criterion:** A proof using Möbius inversion must correctly state and apply the inversion formula. An error in the formula (wrong signs, wrong indexing) is a material issue. However, the inversion step itself is "routine" and may be cited as a known fact without re-proof in a competition context.

---

## Part IV: Extremal Combinatorics

### 4.1 Optimization with Distinct Elements

**Basic setup:** Given n distinct positive integers a₁ < a₂ < ... < aₙ, find the minimum value of max(Σ_{i∈I} aᵢ) or other extremal quantities subject to conditions on subset sums.

**Key principle:** For k-element subsets, the one with the largest sum consists of the k largest elements {a_{n-k+1}, ..., aₙ}. The one with the smallest sum consists of the k smallest elements {a₁, ..., aₖ}.

**Common technique:** Set a_{m} = c (the "median" element), then use inequalities:
- a_{m-1} ≤ c-1, a_{m-2} ≤ c-2, ..., a_{m-k} ≤ c-k
- a_{m+1} ≥ c+1, a_{m+2} ≥ c+2, ..., a_{m+k} ≥ c+k

These give lower and upper bounds on partial sums, which then constrain the possible values of c.

### 4.2 Minimality Arguments

**Technique:** To show that a minimum value of some parameter is N:
1. **Existence:** Construct a configuration achieving the value N
2. **Lower bound:** Show no configuration achieves a value less than N

For (1), the construction must be verified to satisfy ALL the problem's conditions. For (2), the argument must work for GENERAL configurations satisfying the problem's conditions, not just special cases.

**Evaluation criterion:** A proof that omits the existence direction (just shows the lower bound) proves an upper bound on the minimum, not the minimum itself. A proof that omits the lower bound just gives an example. Both directions are REQUIRED for a complete proof.

### 4.3 The Role of Strict vs Non-Strict Inequalities

When bounding a sum sum_{i=1}^k a_i ≤ kc - k(k+1)/2 (where c is the (k+1)-th element and the elements are distinct integers), the bound comes from:
a₁ ≤ c-k, a₂ ≤ c-k+1, ..., aₖ ≤ c-1, so sum ≤ Σᵢ₌₁ᵏ (c-k+i-1) = kc - k(k+1)/2.

This is a UPPER BOUND. The lower bound for a_{k+1},...,a_{2k} uses: a_{k+1+j} ≥ c+j for j=1,...,k.

**Evaluation criterion:** Strict vs non-strict inequalities can change the answer by 1. In a minimality problem, if the minimum involves "≥" vs ">" or "=" vs "≤", check that the proof's inequalities are of the right type.

---

## Part V: Combinatorial Designs and Constructions

### 5.1 Existence Proofs via Explicit Construction

When a problem asks to show a configuration exists with given properties, the proof must:
1. Exhibit an explicit configuration
2. Verify EVERY required property for that configuration
3. (If asking for minimum) show no smaller/fewer configuration satisfies all properties

**Common error:** Exhibiting a configuration and checking only a subset of the required properties, assuming the rest hold.

### 5.2 General vs Special Case

If a problem asks to show that for all n (or all k), some property holds, the proof must work for GENERAL n (or k). A proof that only handles specific cases (e.g., n = 1, 2, 3) and extrapolates without justification has a critical gap.

**Evaluation criterion:** If the proof shows existence/construction for specific values and claims "similarly for other values" or "by analogous argument," check whether the argument is genuinely analogous. If the analogous argument requires non-trivial new ideas, citing it without providing it is a gap.

### 5.3 Counting Configurations

When counting configurations with multiple constraints:

**Strategy 1 (Sequential):** Count the number of ways to make each choice in sequence, multiplying at each step (only if choices are independent or conditional counts are computed).

**Strategy 2 (Characterize then count):** First show all valid configurations have a specific structural form, then count that form.

**Evaluation criterion for Strategy 2:** The "characterize" step must be bidirectional:
- (⇒) Every valid configuration has the claimed form
- (⇐) Every configuration of the claimed form is valid

Missing either direction means the count is wrong (either over-counting or under-counting).

---

## Part VI: Set Systems and Monotone Functions

### 6.1 Intersecting Families

A family F of sets is **intersecting** if any two members of F have a non-empty intersection. Equivalently, no two members are disjoint.

**Key result:** Any intersecting antichain in 2^S has size ≤ C(n-1, ⌊(n-1)/2⌋) (Erdős-Ko-Rado theorem for uniform families).

In the context of proof evaluation, an intersecting family arises naturally from functional conditions like f(T₁)f(T₂) = f(T₁∪T₂)f(T₁∩T₂) with f(∅) = 0: this forces any two sets in the support of f to intersect.

### 6.2 Upward-Closed and Downward-Closed Families

A family F is **upward-closed (upset)** if whenever A ∈ F and A ⊆ B ⊆ S, then B ∈ F.
A family F is **downward-closed (downset)** if whenever A ∈ F and B ⊆ A, then B ∈ F.

**Evaluation criterion:** When a proof concludes that the support of a function is upward-closed from F = {T : T ⊇ U} for some minimal element U, this conclusion requires verifying:
- U is indeed in F (f(U) > 0)
- U is minimal in F (f(V) = 0 for all proper subsets V ⊊ U)
- Any superset of U is in F (f(T) > 0 for all T ⊇ U)

The third point requires explicit verification from the functional condition.

### 6.3 Chains in the Boolean Lattice and Order Ideals

A **chain** A₀ ⊂ A₁ ⊂ ... ⊂ Aₙ with |Aᵢ| = i is called a **maximal chain** in B_n (since it has length n+1, the maximum possible). The number of maximal chains in B_n is n! (corresponding to the n! orderings of the elements of S).

**Application:** When counting pairs of disjoint chains (A₀ ⊂ A₁ ⊂ ... ⊂ Aₙ) and (B₀ ⊂ B₁ ⊂ ... ⊂ Bₙ) with A_n ∩ B_n = ∅ in B_{2n}:
1. Choose A_n: C(2n, n) ways (any n-element subset)
2. B_n is forced (= complement of A_n since |B_n| = n and A_n ∩ B_n = ∅ and A_n ∪ B_n = {1,...,2n} when n+n = 2n)
3. Build the chain inside A_n: n! ways
4. Build the chain inside B_n: n! ways
Total: C(2n,n)·n!·n! = (2n)!

---

## Part VII: Common Proof Structures in Combinatorics Problems

### 7.1 Greedy Arguments

A greedy algorithm makes locally optimal choices. A greedy proof must:
1. Define the greedy choice precisely
2. Show the greedy choice doesn't preclude future valid choices (exchange argument or augmenting path argument)
3. Show the result of the greedy algorithm has the required properties

**Common error:** Assuming greedy is optimal without proving the exchange argument.

### 7.2 Induction on Problem Parameters

**Base case:** Verify the claim for the smallest valid parameter (n=1, k=0, etc.).

**Inductive step:** Assume the claim for all values ≤ n-1, prove for n. The reduction from n to n-1 (or n-k) must be carefully justified.

**Evaluation criterion:** If the inductive step says "apply the induction hypothesis," verify that:
- The hypothesis applies (the smaller problem satisfies the induction's hypotheses)
- The conclusion for the smaller problem correctly implies the conclusion for the larger

### 7.3 Extremal Arguments

**Setup:** Take an element/configuration with a specific extremal property (minimal, maximal, etc.).

**Technique:** Use the extremality to derive structural properties.

**Evaluation criterion:** If a proof takes a "minimal element U in the support of f" (for example), it must verify that such a minimal element exists (the support is non-empty) and that minimality gives the claimed structure.

### 7.4 Bijective Proofs

A bijection between two sets proves they have the same cardinality. A bijective proof must:
1. Define the map explicitly
2. Show it is well-defined (maps valid objects to valid objects)
3. Show it is injective (different inputs give different outputs)
4. Show it is surjective (every valid output is achieved)

**Alternative:** Show the map is a bijection by finding a two-sided inverse.

---

## Part VIII: Specific Problem Type Guidance

### 8.1 Coloring Problems with Multiplicative Condition (proof_13 type)

**Problem type:** Color subsets of S blue or red, count colorings where f(T₁)f(T₂) = f(T₁∪T₂)f(T₁∩T₂) for all T₁,T₂ ⊆ S.

**Standard case split:** f(∅) = 1 (empty set is blue) vs f(∅) = 0 (empty set is red).

**Case 1 (f(∅)=1):**
- For i ∉ T: apply functional condition with T₁ = {i}, T₂ = T to get f({i})·f(T) = f(T∪{i})·f(∅) = f(T∪{i})
- This gives f(T∪{i}) = λᵢ·f(T) where λᵢ = f({i})
- By induction: f(T) = Π_{i∈T} λᵢ = Π_{i∈T} f({i})
- Möbius inversion then recovers the blue sets exactly as subsets of A = {i : λᵢ = 2}
- Converse: verify that coloring B = P(A) satisfies the multiplicativity for all T₁, T₂

**Critical verification in Case 1 (often skipped):** The Möbius inversion step gives the blue set indicator, but one must verify that this formula gives 0 or 1 (not other values), and that the resulting B satisfies the original multiplicativity. This computation is:

1_B(T) = Σ_{U⊆T} (-1)^{|T|-|U|} f(U) = Σ_{U⊆T} (-1)^{|T|-|U|} · 2^{|U∩A|}

Let T∩A = T_A and T\A = T_B. For U ⊆ T: U = U_A ∪ U_B with U_A ⊆ T_A and U_B ⊆ T_B. Then:

1_B(T) = Σ_{U_A⊆T_A, U_B⊆T_B} (-1)^{|T_A|+|T_B|-|U_A|-|U_B|} · 2^{|U_A|}
        = [Σ_{U_A⊆T_A} (-1)^{|T_A|-|U_A|} 2^{|U_A|}] · [Σ_{U_B⊆T_B} (-1)^{|T_B|-|U_B|}]

The second factor = Σ_{k=0}^{|T_B|} C(|T_B|,k)(-1)^{|T_B|-k} = (1-1)^{|T_B|} = 0^{|T_B|}.

So 1_B(T) = 0 if |T_B| > 0, i.e., if T ⊄ A.
If T ⊆ A, then T_B = ∅, so 1_B(T) = Σ_{U_A⊆T_A} (-1)^{|T_A|-|U_A|} 2^{|U_A|} = (2-1)^{|T_A|} = 1.

So 1_B(T) = 1 if T ⊆ A and 0 otherwise, i.e., B = P(A). ✓

**This computation verifies Case 1.** A proof that only claims "one checks" without this computation has a minor omission (the computation is straightforward).

**Case 2 (f(∅)=0):** 
- Functional condition with T₂ disjoint from T₁: f(T₁)f(T₂) = f(T₁∪T₂)·f(∅) = 0
- So for any T₁, T₂ in the support of f, T₁∩T₂ ≠ ∅ (support is intersecting)
- Take minimal element U in support; show f(U) = 1, B∩P(U) = {U}, support = {T : T⊇U}
- Reduce to Case 1 on S' = S\U via g(W) = f(U∪W)
- Converse: verify that any interval [U, U∪A'] satisfies multiplicativity for ALL pairs T₁, T₂ ⊆ S

**Critical gap in Case 2 converse:** If the proof claims "one checks that [U, U∪A'] satisfies the condition" without doing the check, and the check is non-trivial, this is a critical skipped step.

**The check:** For B = [U, U∪A'], we have f(T) = g(T\U)·χ_{T⊇U}(T) where g(W) = 2^{|W∩A'|}. For arbitrary T₁, T₂ ⊆ S:
- If T₁ ⊅ U or T₂ ⊅ U: then at least one of f(T₁), f(T₂) equals 0. Also T₁∪T₂ may or may not ⊇ U, and T₁∩T₂ ⊇ U only if both T₁,T₂ ⊇ U (which fails). So at least one of f(T₁∪T₂), f(T₁∩T₂) = 0. The condition 0·f(T₂) = f(T₁∪T₂)·0 becomes 0 = 0 or 0 = 0. ✓
- If T₁ ⊇ U and T₂ ⊇ U: then T₁∪T₂ ⊇ U and T₁∩T₂ ⊇ U. Let W₁ = T₁\U, W₂ = T₂\U. Then f(Tᵢ) = g(Wᵢ) = 2^{|Wᵢ∩A'|} and similarly. The condition becomes g(W₁)g(W₂) = g(W₁∪W₂)g(W₁∩W₂), i.e., 2^{|W₁∩A'|}·2^{|W₂∩A'|} = 2^{|(W₁∪W₂)∩A'|}·2^{|(W₁∩W₂)∩A'|}. This holds because |W₁∩A'|+|W₂∩A'| = |(W₁∩A')∪(W₂∩A')|+|(W₁∩A')∩(W₂∩A')| = |(W₁∪W₂)∩A'|+|(W₁∩W₂)∩A'| (using |A|+|B| = |A∪B|+|A∩B| for any finite sets). ✓

So the converse IS valid and checkable — but it requires this computation. The proof's "one checks by routine verification" is in fact routine (as shown above). However, an auditor must distinguish between (a) "the proof says one checks and the check is indeed routine/trivial" (= minor omission, proof essentially correct) and (b) "the proof says one checks and the check is non-trivial and was actually skipped" (= critical gap).

**Verdict guidance for this problem type:** If the converse verification is ONLY cited as "one checks" and similar phrases appear at multiple critical steps, the cumulative effect of all the skipped steps determines the verdict.

### 8.2 Grid/Matrix Set Systems with Monotonicity (proof_15 type)

**Problem type:** Count collections {S_{ij}} with |S_{ij}| = i+j and S_{ij} ⊆ S_{kl} when i≤k, j≤l.

**Standard reduction:** Write A_i = S_{i,0} and B_j = S_{0,j}. By monotonicity:
- A_i = S_{i,0} ⊆ S_{i,j}
- B_j = S_{0,j} ⊆ S_{i,j}
- Hence A_i ∪ B_j ⊆ S_{i,j}
- |A_i∪B_j| ≤ |A_i|+|B_j| = i+j = |S_{ij}|

The conclusion S_{ij} = A_i ∪ B_j requires |A_i∪B_j| = i+j, which requires A_i ∩ B_j = ∅.

**Critical point:** The argument "|A_i∪B_j| ≤ i+j = |S_{ij}| implies S_{ij} = A_i∪B_j" is INVALID without additionally knowing |A_i∪B_j| = i+j. The bound |A_i∪B_j| ≤ i+j combined with A_i∪B_j ⊆ S_{ij} and |S_{ij}| = i+j shows A_i∪B_j ⊆ S_{ij} with |A_i∪B_j| ≤ |S_{ij}|. But this does NOT imply equality — it only shows A_i∪B_j could be a proper subset of S_{ij}.

To CORRECTLY conclude S_{ij} = A_i∪B_j, one needs |A_i∪B_j| = i+j, which requires A_i∩B_j = ∅. But A_i∩B_j = ∅ is derived from S_{ij} = A_i∪B_j! This is CIRCULAR.

A correct proof would avoid this circularity by first establishing A_n∩B_n = ∅ (using |S_{nn}| = 2n and A_n∪B_n ⊆ S_{nn}, with |A_n|+|B_n| = 2n, forcing |A_n∩B_n| = 0 IF |S_{nn}| = |A_n∪B_n| = 2n). But even this requires |S_{nn}| = |A_n∪B_n|, which again needs A_n∩B_n = ∅...

The correct resolution: since A_n∪B_n ⊆ S_{nn} and |S_{nn}| = 2n and |A_n|+|B_n| = n+n = 2n, we need |A_n∪B_n| ≤ 2n (trivially true). But for a proper subset A_n∪B_n ⊊ S_{nn}, we'd need |A_n∪B_n| < 2n, i.e., A_n∩B_n ≠ ∅. Conversely, S_{nn} ⊆ {1,...,2n} with |S_{nn}| = 2n means S_{nn} = {1,...,2n}. And |A_n∪B_n| ≤ |{1,...,2n}| = 2n with |A_n|+|B_n| = 2n implies |A_n∩B_n| ≥ 0, so possibly A_n∩B_n ≠ ∅.

Actually, since A_n∪B_n ⊆ S_{nn} = {1,...,2n} (ALL elements), we have |A_n∪B_n| ≤ 2n. And |A_n|+|B_n| = 2n. So |A_n∩B_n| = |A_n|+|B_n|-|A_n∪B_n| ≥ 2n-2n = 0. This gives no contradiction.

The proof IS circular unless there's additional structure. The correct proof would use a different approach (e.g., induction or direct construction from disjoint chains).

### 8.3 Sum Optimization with Distinct Integers (proof_19 type)

**Problem type:** Find minimum N such that there exist 2k+1 distinct positive integers with total sum > N but every k-element subset sums to ≤ N/2.

**Key structural observations:**
1. The condition "every k-subset ≤ N/2" is most constraining for the largest k elements
2. The condition "total sum > N" is most constraining for the smallest k+1 elements
3. A symmetric set around some center c is a natural candidate for the extremal configuration

**Construction technique:** Take S = {c-k, c-k+1, ..., c, ..., c+k} for some c.
- |S| = 2k+1 ✓ (distinct positive integers if c > k)
- Largest k elements: {c+1,...,c+k}, sum = kc+k(k+1)/2
- Set N = 2·(kc+k(k+1)/2) to make the largest k-subset sum exactly N/2
- Then total sum = (2k+1)c + 0 = ? No, total = Σ_{j=-k}^k (c+j) = (2k+1)c

Wait: Σ_{j=-k}^k (c+j) = (2k+1)c + Σ_{j=-k}^k j = (2k+1)c + 0 = (2k+1)c.

And N = 2(kc + k(k+1)/2) = 2kc + k(k+1).

For total sum > N: (2k+1)c > 2kc+k(k+1) iff c > k(k+1), i.e., c ≥ k(k+1)+1.

With c = k(k+1)+1: N = 2k·(k(k+1)+1)+k(k+1) = 2k²(k+1)+2k+k(k+1) = k(2k+3)(k+1)+2k... let me compute directly.

c = k(k+1)+1 = k²+k+1.
N = 2kc+k(k+1) = 2k(k²+k+1)+k(k+1) = 2k³+2k²+2k+k²+k = 2k³+3k²+3k ✓

Total sum = (2k+1)c = (2k+1)(k²+k+1).

Need: (2k+1)(k²+k+1) > 2k³+3k²+3k.

(2k+1)(k²+k+1) = 2k³+2k²+2k+k²+k+1 = 2k³+3k²+3k+1. ✓ (Exceeds N=2k³+3k²+3k by 1.)

**Minimality argument:** Must show N < 2k³+3k²+3k leads to contradiction. Set a_{k+1} = c (the (k+1)-th smallest element in sorted order). Using a_{k+1+j} ≥ c+j and a_{k+1-j} ≤ c-j (both strict since elements are distinct integers), derive c ≥ k(k+1)+1, hence S_k ≥ N/2.

**Evaluation criterion for proof_19 type:** The proof must:
(a) Correctly compute N = 2k³+3k²+3k
(b) Exhibit the construction explicitly
(c) Verify both sum conditions for the construction
(d) Prove minimality through a general lower bound

Any error in (a)-(d) is a material issue.

### 8.4 Non-General Construction Problems (proof_12 type)

**Problem type:** Construct a combinatorial object (e.g., a graph or set system) with given properties.

**Common gap:** Proving existence for specific small cases (n=1,2,3) and claiming the general case follows "by analogous construction" without providing the general construction.

**Evaluation criterion:** If the proof only handles specific cases, the verdict should be incorrect if the problem asks for a GENERAL construction. A construction that works for specific n values but doesn't generalize is not a valid proof of the general claim.

---

## Part IX: Combinatorics Proof Evaluation Rubric

1. **Completeness of case analysis:** All cases must be covered. Especially: if splitting on f(∅) = 0 vs f(∅) = 1, both cases must be handled.

2. **Converse direction:** When classifying all valid configurations, both directions of "if and only if" must be proved. A proof that only shows (⇒) has a gap.

3. **Counting formula correctness:** Verify every counting formula. C(2n,n)·n!·n! = (2n)! by C(2n,n) = (2n)!/(n!·n!), multiplied by n!·n! = (2n)!/1 = (2n)!. ✓

4. **Non-circularity:** The reduction to boundary chains must not assume what it is trying to prove. Establishing A_i∩B_j = ∅ requires a separate non-circular argument.

5. **Generality:** Does the proof work for general n (or k, or S), not just specific values?

6. **Verification of construction:** Every claimed construction must be verified to satisfy ALL the problem's conditions.

7. **Skipped steps:** "One checks" and "by routine verification" are acceptable for genuinely routine computations (like Möbius inversion in specific cases), but NOT for non-trivial verifications. Assess whether the skipped step is truly routine or not.

**Identifying the first material issue:** Work through the proof sequentially. The FIRST step that violates one of criteria 1-7 is the first material issue.


---

## Appendix A: Extended Examples for Combinatorics Proof Evaluation

### A.1 The Coloring Classification Problem (proof_13 type) — Step-by-Step Audit Guide

**Complete structure of valid colorings:**

A coloring (B, set of blue subsets) satisfies f(T1)f(T2)=f(T1 cup T2)f(T1 cap T2) for all T1,T2 in P(S) iff B belongs to one of these families:

Family 1: B = P(A) for some A subset S (includes empty set = A=empty gives B={empty set})
Family 2: B = [U, U cup A'] for some nonempty U subset S and A' subset S\U (interval in Boolean lattice)
Family 3: B = empty (all-red, the "zero" solution)

Note: Family 3 corresponds to f equiv 0 which vacuously satisfies the equation.
Family 1 corresponds to f(empty)=1.
Family 2 corresponds to f(empty)=0 with some blue set.

**Count:** |Family 1| = 2^n (one per A subset S). |Family 2| = sum_{nonempty U} 2^{n-|U|} = 3^n-2^n. |Family 3| = 1.
Total = 2^n + (3^n - 2^n) + 1 = 3^n + 1.

**First audit step:** Verify the proof splits into f(empty)=1 vs f(empty)=0 cases.
**Second audit step:** Verify Case 1 concludes B=P(A) for 2^n colorings.
**Third audit step:** Verify Case 2 concludes B=[U, U cup A'] plus all-red for 3^n-2^n+1 colorings.
**Fourth audit step:** Add: 2^n + 3^n - 2^n + 1 = 3^n + 1.

Any error in these four steps is a material issue.

### A.2 The S_{ij} Counting Problem (proof_15 type) — Audit Guide

**Setup:** Count valid {S_{ij}: 0<=i,j<=n, S_{ij} subset {1,...,2n}} with |S_{ij}|=i+j and S_{ij} subset S_{kl} when i<=k, j<=l.

**The claimed reduction:** Every valid collection {S_{ij}} arises from a pair of disjoint chains A_0 subset ... subset A_n and B_0 subset ... subset B_n with A_n cap B_n = empty, via S_{ij} = A_i cup B_j.

**Circularity check:** The proof must establish A_i cap B_j = empty BEFORE claiming S_{ij} = A_i cup B_j. If it first claims equality then derives empty intersection, it is circular.

**Non-circular approach outline:**
Step 1: From A_n cup B_n subset S_{nn} and |S_{nn}|=2n, we get S_{nn}={1,...,2n}.
Step 2: From inclusion-exclusion |A_n cup B_n| = |A_n|+|B_n|-|A_n cap B_n| = 2n-|A_n cap B_n|.
Step 3: But A_n cup B_n is not necessarily {1,...,2n}; we only know it's a subset of size <=2n.
Step 4: (Stuck — the above doesn't give A_n cap B_n = empty without additional work.)

A correct proof uses a different approach, such as:
- Working with the largest sets and their complements
- Using induction on n
- Constructing the chains directly from a valid {S_{ij}} by setting A_i = S_{i,0} and showing these form a chain (obvious from i<=k => S_{i,0} subset S_{k,0}) and similarly for B, then establishing disjointness by a non-circular argument

The specific difficulty: establishing S_{ij}=A_i cup B_j requires |A_i cup B_j|=i+j, which requires disjointness, which the proof assumes from the conclusion. This circularity is a first material issue in this type of proof: the characterization is unproven.

### A.3 Combinatorial Optimization (proof_19 type) — Detailed Audit

**Problem:** Find minimum N such that there exist 2k+1 distinct positive integers with sum > N and every k-subset sums to at most N/2.

**Key lemmas:**

Lemma 1 (Largest k-subset): The maximum sum of a k-element subset of {a_1 < ... < a_{2k+1}} is a_{k+2} + ... + a_{2k+1} (the k largest elements).
Proof: Any k elements sum to at most the k largest. ✓

Lemma 2 (Lower bound on c): With c = a_{k+1} and the conditions, c >= k(k+1)+1.
Proof: From sum_{i=1}^{k+1} a_i > S_k (where S_k = sum of k largest):
  sum_{i=1}^k a_i + c > S_k >= kc + k(k+1)/2
  But sum_{i=1}^k a_i <= kc - k(k+1)/2 (since a_{k+1-j} <= c-j for j=1,...,k)
  So kc - k(k+1)/2 >= sum_{i=1}^k a_i > kc + k(k+1)/2 - c = (k-1)c + k(k+1)/2
  This gives kc - k(k+1)/2 > (k-1)c + k(k+1)/2
  c > k(k+1). So c >= k(k+1)+1. ✓

Lemma 3 (Minimum N): N' >= 2k^3+3k^2+3k.
Proof: N' >= 2S_k >= 2(kc + k(k+1)/2) >= 2(k(k(k+1)+1) + k(k+1)/2) = 2k^2(k+1)+2k + k(k+1) = 2k^3+3k^2+3k. ✓

Lemma 4 (Construction achieves N=2k^3+3k^2+3k): Set c=k(k+1)+1, S={c-k,...,c+k}.
- k-subset max sum: kc+k(k+1)/2 = N/2. ✓ (all k-subsets have sum <= N/2)
- Total sum: (2k+1)c = N+1 > N. ✓

**Evaluation criterion:** A proof correctly establishing Lemmas 1-4 is CORRECT. The first error in any lemma is the first material issue.

### A.4 Non-General Construction Problem (proof_12 type) — Audit Guide

**Common structure of proof_12 type problems:** "Construct [combinatorial object with property P for all n >= 1]."

**Required proof elements:**
1. Description of a construction (for general n)
2. Verification that the construction has property P

**Common gap:** Construction given for small n (e.g., n=1,2,3) with "similar for larger n" or "obvious generalization." Without specifying the general construction, this is incomplete.

**Evaluation criterion:**
- If the proof ONLY handles specific small cases: INCORRECT (first material issue = missing general construction)
- If the proof gives a general construction but fails to verify P: INCORRECT (first material issue = missing verification)
- If both are present: evaluate whether the verification is correct

---

## Appendix B: Additional Combinatorial Identities and Techniques

### B.1 Key Subset Sum Identities

For S = {1,...,n} and A subset S with |A|=k:
sum_{A subset S, |A|=k} sum_{i in A} i = C(n-1,k-1) * sum_{i=1}^n i = C(n-1,k-1) * n(n+1)/2

This counts pairs (i, A) with i in A and |A|=k: each i is in C(n-1,k-1) such sets.

### B.2 Principle of Inclusion-Exclusion — Extended

For events A_1,...,A_m in sample space Omega:
P(A_1 cup ... cup A_m) = sum P(A_i) - sum_{i<j} P(A_i cap A_j) + ... + (-1)^{m+1} P(A_1 cap ... cap A_m)

**Sieve formula:** Number of elements with NO property = sum_{S subset [m]} (-1)^|S| * |cap_{i in S} A_i|

**Derangement formula:** D(n) = n! * sum_{k=0}^n (-1)^k / k!

### B.3 Lattice Path Counting

A lattice path from (0,0) to (m,n) using steps (1,0) and (0,1) has C(m+n,m) total paths.

**Ballot problem:** Path from (0,0) to (m,n) with m>n that stays strictly above the diagonal: C(m+n,m) * (m-n)/(m+n).

**Catalan numbers:** C_n = C(2n,n)/(n+1) counts Dyck paths (lattice paths from (0,0) to (2n,0) with steps +1,-1 staying >= 0).

### B.4 Counting Chains in Boolean Lattice

Number of chains of length k+1 (k+1 elements including empty) in B_n:
= sum over A_0 subset A_1 subset ... subset A_k (each proper containment and in S)
= n! / (n-k)! * C(n,k) ... (complex formula)

For maximal chains (length n+1): exactly n! (orderings of S).

For chains A_0 subset A_1 subset ... subset A_n with |A_i|=i:
= n! (one for each ordering/labeling of S as {s_1,...,s_n}, taking A_i = {s_1,...,s_i})

This is the bijection: chains of this type <-> permutations of S. Hence n! chains.

### B.5 Counting Disjoint Chains

Two disjoint chains in B_{2n}: choose A-chain of length n+1 and B-chain of length n+1 with A_n cap B_n = empty.

Method 1 (direct count):
Choose A_n: C(2n,n) ways. B_n = complement of A_n: 1 way.
Choose chain inside A_n: n! ways (orderings of A_n).
Choose chain inside B_n: n! ways.
Total: C(2n,n) * n! * n! = (2n)!/(n!*n!) * n!^2 = (2n)!.

Method 2 (permutation bijection): Each pair of disjoint chains (A, B) of length n+1 with A_n cup B_n = {1,...,2n} corresponds to a permutation sigma of {1,...,2n}: put sigma(1),...,sigma(n) in A-chain order and sigma(n+1),...,sigma(2n) in B-chain order. There are (2n)! permutations, giving (2n)! pairs. ✓

---

## Appendix C: Worked Derivations for Counting Arguments

### C.1 Sum Σ_{k=1}^n C(n,k) * 2^{n-k} = 3^n - 2^n

Proof: sum_{k=0}^n C(n,k) * 2^{n-k} = sum_{k=0}^n C(n,k) * 2^{n-k} * 1^k = (2+1)^n = 3^n by binomial theorem.
Subtract k=0 term: C(n,0)*2^n = 2^n.
So sum_{k=1}^n C(n,k)*2^{n-k} = 3^n - 2^n. ✓

### C.2 Total Case 2 Count = 1 + (3^n - 2^n) = 3^n - 2^n + 1

As computed: Case 2 gives all-red (1 coloring) plus B=[U,U cup A'] for each nonempty U and each A' subset S\U.
For fixed |U|=m: C(n,m) choices for U, 2^{n-m} choices for A'. So contributions: sum_{m=1}^n C(n,m)*2^{n-m} = 3^n-2^n.
Total: 1 + (3^n-2^n) = 3^n - 2^n + 1. ✓

### C.3 Verification: 2^n + (3^n-2^n+1) = 3^n+1

2^n + 3^n - 2^n + 1 = 3^n + 1. ✓ The 2^n terms cancel.

### C.4 Minimality N = 2k^3+3k^2+3k — Computation Check

For k=1: N = 2+3+3 = 8. Check: c=k(k+1)+1=3, S={2,3,4}. Sum=9>8=N. Max 1-subset sum=4=N/2. ✓
For k=2: N = 16+12+6 = 34. Check: c=7, S={5,6,7,8,9}. Sum=35>34. Max 2-subset sum=8+9=17=N/2. ✓
For k=3: N = 54+27+9 = 90. Check: c=13, S={10,11,12,13,14,15,16}. Sum=91>90. Max 3-subset sum=14+15+16=45=N/2. ✓

### C.5 Counting Disjoint Chains for Small n

n=1: Choose A_1 (1 element from {1,2}): C(2,1)=2 ways. B_1=complement: 1 way. Chains of length 2: empty subset A_1, empty subset B_1 (no internal ordering needed). Total: 2*1*1*1=2=2!. ✓

n=2: C(4,2)=6 ways for A_2. B_2 forced. 2! orderings for A-chain inside A_2. 2! for B. Total: 6*2*2=24=4!. ✓

n=3: C(6,3)=20. 3!=6 each for A and B chains. Total: 20*6*6=720=6!. ✓
