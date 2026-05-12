# Domain Background: Number Theory Proof Evaluation

This reference covers the mathematical theory, common proof techniques, and evaluation criteria relevant to olympiad number theory problems. Sub-agents auditing **proof_01**, **proof_06**, **proof_10**, and **proof_17** should read this document before evaluating their assigned proof.

---

## Part I: Divisibility and Primes

### 1.1 Fundamental Theorem of Arithmetic

Every integer n > 1 has a unique prime factorization n = p₁^{a₁} · p₂^{a₂} · ... · pₖ^{aₖ} with p₁ < p₂ < ... < pₖ primes and each aᵢ ≥ 1.

**Proof sketch.** Existence follows from strong induction: if n is not prime, write n = ab with 1 < a,b < n and apply induction to a and b. Uniqueness follows from Euclid's lemma: if p is prime and p | ab, then p | a or p | b. This prevents cancellation of distinct prime factors.

**Common errors:** Proofs that use unique factorization without explicitly invoking Euclid's lemma, treating the uniqueness as "obvious," will have a logical gap if the problem's context does not make unique factorization automatic.

### 1.2 Greatest Common Divisor and Bézout's Identity

For integers a and b not both zero, gcd(a, b) is the largest positive integer dividing both. Bézout's identity states: there exist integers x, y such that ax + by = gcd(a, b). The extended Euclidean algorithm computes these coefficients explicitly.

**Key consequence:** gcd(a, b) = 1 if and only if there exist x, y with ax + by = 1, i.e., a has a multiplicative inverse mod b.

**Evaluation note:** When a proof claims "since gcd(a,b)=1, we may invert a modulo b," this is valid only if the proof has already established or been given that gcd(a,b)=1. A proof that assumes coprimality without proof commits an unjustified hypothesis error.

### 1.3 Modular Arithmetic and Congruence Classes

For a fixed modulus m > 0, the integers are partitioned into m residue classes {0, 1, ..., m-1}. Addition and multiplication are compatible with this equivalence: if a ≡ a' (mod m) and b ≡ b' (mod m) then a+b ≡ a'+b' and ab ≡ a'b' (mod m).

**Modular inverse:** The inverse of a modulo m exists if and only if gcd(a, m) = 1. When m = p is prime, every nonzero element has a unique inverse in {1, ..., p-1}.

**Fermat's Little Theorem.** If p is prime and p ∤ a, then a^{p-1} ≡ 1 (mod p).

**Proof.** The map x ↦ ax is a bijection on {1, ..., p-1} (since gcd(a,p)=1). Therefore a·2a·3a···(p-1)a ≡ 1·2·3···(p-1) (mod p), giving a^{p-1}(p-1)! ≡ (p-1)! (mod p). Since gcd((p-1)!, p) = 1, we may divide both sides by (p-1)! to get a^{p-1} ≡ 1. □

**Euler's Theorem.** For gcd(a, m) = 1, a^{φ(m)} ≡ 1 (mod m), where φ(m) = |{1 ≤ k ≤ m : gcd(k,m)=1}| is Euler's totient function.

### 1.4 Wilson's Theorem

**Theorem (Wilson, 1770).** An integer p > 1 is prime if and only if (p-1)! ≡ -1 (mod p).

**Proof (⇒).** Let p be prime. Consider the multiplicative group G = (Z/pZ)*, which has order p-1. Each element a ∈ G has a unique inverse a⁻¹ ∈ G. The equation a² ≡ 1 (mod p) means p | (a-1)(a+1), so by primality p | a-1 or p | a+1, giving a ≡ ±1 (mod p). Therefore in G, only 1 and p-1 are self-inverse. Pairing all other elements {2, 3, ..., p-2} with their distinct inverses, the product of each pair is 1. Hence (p-1)! ≡ 1·(p-1)·1 ≡ -1 (mod p). □

**Proof (⇐).** Suppose (n-1)! ≡ -1 (mod n). If n = ab with 1 < a,b < n, then a | (n-1)! and a | n, so a | 1. Contradiction. Hence n is prime. □

**Generalization.** For prime p and integer r with 1 ≤ r ≤ p-1:
(p-1)! = (p-1)(p-2)···(p-r) · (p-r-1)!

The first factor satisfies:
(p-1)(p-2)···(p-r) ≡ (-1)(-2)···(-r) = (-1)^r · r! (mod p)

Therefore (p-1)! ≡ (-1)^r · r! · (p-r-1)! (mod p), and since (p-1)! ≡ -1 (mod p):
-1 ≡ (-1)^r · r! · (p-r-1)! (mod p)
(p-r-1)! ≡ (-1)^{r+1} / r! ≡ (-1)^{r+1} · (r!)^{-1} (mod p)

**Applications to factorial-divisibility:** For a polynomial f(x) = x - r (r a positive integer), we have f(p) = p - r for prime p > r, so f(p)! = (p-r)!. Wilson's theorem then determines 2·(p-r)! + 1 mod p.

**Evaluation criteria for Wilson-theorem proofs:**
- Correct: applying Wilson's theorem to derive (p-r)! ≡ c (mod p) for explicit constant c
- Incorrect: applying Wilson's theorem to composite moduli
- Incorrect: computing (p-1)! = (p-r)! · (p-r)(p-r+1)···(p-1) and claiming (p-r)(p-r+1)···(p-1) ≡ (-r)(-r+1)···(-1) = (-1)^r · r! without justification (this step IS valid mod p but should be stated)
- Gap: failing to verify that the constant D_r = 2(-1)^{r+1} + r! is indeed zero only at specific r values

### 1.5 Lifting the Exponent Lemma

For odd prime p and p ∤ a, p ∤ b with p | a-b:
v_p(a^n - b^n) = v_p(a - b) + v_p(n)

where v_p(m) denotes the p-adic valuation of m (the exponent of p in the prime factorization of m).

For p = 2 and 2 | a-b:
v_2(a^n - b^n) = v_2(a-b) + v_2(a+b) + v_2(n) - 1

**Common errors involving LTE:** Applying LTE without first checking that the prime p divides a-b (but not a or b). Using LTE for p = 2 without the corrected formula.

---

## Part II: Gaussian Integers and Algebraic Number Theory

### 2.1 The Gaussian Integers Z[i]

The Gaussian integers are Z[i] = {a + bi : a, b ∈ Z} with the usual complex multiplication. Key properties:

**Norm:** N(a + bi) = a² + b² = (a+bi)(a-bi). The norm is multiplicative: N(αβ) = N(α)N(β).

**Units:** The units of Z[i] are exactly the elements with norm 1: {±1, ±i}.

**Gaussian primes:** An element π ∈ Z[i] \ {0} is a Gaussian prime if π = αβ implies α or β is a unit. The Gaussian primes are:
- (1+i) and its associates (since N(1+i) = 2)
- p + 0i for rational primes p ≡ 3 (mod 4) (inert primes)
- a + bi where a² + b² = p for rational primes p ≡ 1 (mod 4) and p = 2 (split primes)

**Unique factorization:** Z[i] is a Euclidean domain (division algorithm with Euclidean function N), hence a PID and UFD. Every nonzero non-unit has a factorization into Gaussian primes, unique up to units.

### 2.2 Factoring Integers in Z[i]

For a rational prime p:
- If p ≡ 3 (mod 4): p remains prime in Z[i] (p is a Gaussian prime)
- If p ≡ 1 (mod 4): p = π·π̄ where π = a + bi with a² + b² = p (by Fermat's theorem on sums of two squares)
- If p = 2: 2 = -i(1+i)² (ramified prime, associated to (1+i)²)

**Sum of two squares identity:** (a² + b²)(c² + d²) = (ac-bd)² + (ad+bc)² = (ac+bd)² + (ad-bc)². This follows from N(αβ) = N(α)N(β) in Z[i].

### 2.3 The Identity X⁴ + Y⁴ in Z[i]

The factorization X⁴ + Y⁴ = (X² + iY²)(X² - iY²) = (X²+iY²)·\overline{(X²+iY²)} is fundamental to many olympiad problems involving fourth powers.

**Key point:** X² + iY² and X² - iY² are complex conjugates. Their product is X⁴ + Y⁴ ∈ Z.

**Coprimality condition:** gcd(X²+iY², X²-iY²) in Z[i] divides their difference 2iY² and their sum 2X². If gcd(X,Y) = 1 in Z, one must still carefully analyze which Gaussian primes can divide both X²+iY² and X²-iY².

**UFD consequence:** If X²+iY² and X²-iY² are coprime in Z[i] and their product = α⁵ for some α ∈ Z[i], then each factor must itself be a fifth power (times a unit) in Z[i].

**Critical subtlety:** Establishing coprimality of X²+iY² and X²-iY² requires checking that no Gaussian prime divides both. A common approach: any common divisor γ divides both (X²+iY²)+(X²-iY²) = 2X² and (X²+iY²)-(X²-iY²) = 2iY². If γ is not an associate of (1+i), then γ | X² and γ | Y², which combined with gcd(X,Y)=1 in Z gives a contradiction.

**Evaluation criteria for Gaussian integer proofs:**
- Must explicitly verify coprimality of the two conjugate factors, not just assert it
- Must correctly enumerate all units in Z[i] (not just ±1)
- Must carefully handle the case of the ramified prime (1+i)
- Conclusions about when two expressions "must be fifth powers" require verified coprimality + UFD
- The claim "since they are coprime and their product is an nth power, each is an nth power (times a unit)" is valid in any UFD and may be stated without proof in an olympiad context

### 2.4 Quadratic Residues and the Legendre Symbol

For odd prime p and integer a with p ∤ a, a is a **quadratic residue** modulo p if there exists x with x² ≡ a (mod p).

**Legendre symbol:** (a/p) = 1 if a is a QR mod p, -1 if not, 0 if p | a.

**Euler's criterion:** (a/p) ≡ a^{(p-1)/2} (mod p).

**Quadratic reciprocity (Gauss):** For distinct odd primes p, q:
(p/q)(q/p) = (-1)^{(p-1)(q-1)/4}

Supplements: (-1/p) = (-1)^{(p-1)/2} and (2/p) = (-1)^{(p²-1)/8}.

**Applications:** Quadratic residues determine which integers are represented by binary quadratic forms. The form x² + y² represents n if and only if every prime factor p ≡ 3 (mod 4) appears to an even power in n. This is equivalent to the Gaussian integer factorization of n having no inert prime factors to odd powers.

---

## Part III: Diophantine Equations and p-adic Methods

### 3.1 Linear Diophantine Equations

ax + by = c has integer solutions if and only if gcd(a,b) | c. When solutions exist, the general solution is x = x₀ + (b/d)t, y = y₀ - (a/d)t for t ∈ Z, where d = gcd(a,b) and (x₀,y₀) is any particular solution.

### 3.2 Pythagorean Triples

Integer solutions to x² + y² = z² with gcd(x,y,z) = 1 and x,z > 0, y even are:
x = m² - n², y = 2mn, z = m² + n²
for positive integers m > n with gcd(m,n) = 1 and m ≢ n (mod 2).

### 3.3 Fermat's Last Theorem Context

For n ≥ 3, the equation xⁿ + yⁿ = zⁿ has no solutions in positive integers. The proof for n = 4 (Fermat himself) and n = 3 (Euler) uses infinite descent. The general case is Wiles's theorem (1995). In olympiad contexts, fourth-power problems often use Gaussian integer factorizations.

### 3.4 Valuation Theory

The p-adic valuation v_p(n) is the exponent of p in the prime factorization of n. Properties:
- v_p(ab) = v_p(a) + v_p(b)
- v_p(a+b) ≥ min(v_p(a), v_p(b)) with equality if v_p(a) ≠ v_p(b)
- v_p(a^n) = n · v_p(a)

**Divisibility by prime powers:** n | m if and only if v_p(n) ≤ v_p(m) for all primes p.

**Common error:** Using v_p(a+b) = min(v_p(a), v_p(b)) when v_p(a) = v_p(b). In this case, v_p(a+b) could be strictly greater than min(v_p(a), v_p(b)).

---

## Part IV: Multiplicative Functions and Arithmetic Functions

### 4.1 The Euler Totient Function

φ(n) = |{1 ≤ k ≤ n : gcd(k,n)=1}|. Key properties:
- φ(p) = p-1 for prime p
- φ(p^k) = p^k - p^{k-1} = p^{k-1}(p-1) for prime power p^k
- φ is multiplicative: gcd(m,n)=1 implies φ(mn) = φ(m)φ(n)
- Σ_{d|n} φ(d) = n

### 4.2 The Number and Sum of Divisors

τ(n) = number of divisors of n, σ(n) = sum of divisors of n. Both are multiplicative. For prime power p^k: τ(p^k) = k+1, σ(p^k) = (p^{k+1}-1)/(p-1).

### 4.3 Mobius Function and Inversion

The Möbius function: μ(1) = 1, μ(n) = (-1)^k if n is a product of k distinct primes, μ(n) = 0 if p² | n for some prime p.

**Möbius inversion formula:** If f(n) = Σ_{d|n} g(d) then g(n) = Σ_{d|n} μ(n/d) f(d).

---

## Part V: Prime Distribution and Dirichlet's Theorem

### 5.1 Dirichlet's Theorem on Primes in Arithmetic Progressions

For gcd(a,d) = 1, the arithmetic progression {a, a+d, a+2d, ...} contains infinitely many primes. Moreover, the primes are equidistributed among the φ(d) coprime residue classes modulo d.

**Consequence:** If a property holds for all primes p > N, and it is asserted that only finitely many primes can satisfy a given fixed congruence condition, this requires careful use of Dirichlet's theorem or direct analysis of the fixed integer whose prime factors are at issue.

**Key application:** If D is a fixed nonzero integer and we need p | D for all primes p in some infinite set, then D must be 0. This is because any nonzero integer has finitely many prime divisors. This principle is heavily used in the polynomial-prime divisibility problems.

### 5.2 Chebyshev's Theorem

There is always a prime between n and 2n for n ≥ 1. This is weaker than PNT but sufficient for many olympiad applications.

---

## Part VI: Common Proof Structures in Number Theory Problems

### 6.1 Infinite Descent

Used to show Diophantine equations have no positive integer solutions. Assume a minimal positive solution exists and derive a smaller solution, contradicting minimality.

**Evaluation criterion:** The descent step must produce a strictly smaller (by well-ordering) solution. A proof that claims "we can repeat this process" without explicit minimality or termination is incomplete.

### 6.2 Polynomial Congruences

For a polynomial f(x) ∈ Z[x] of degree d, the number of roots modulo prime p is at most d (by Lagrange's theorem). This is used to analyze when a polynomial vanishes at many primes.

**Key lemma:** If f(p) ≡ 0 (mod p) for all primes p in an infinite set, and f has degree d < p for large p, then either f ≡ 0 or p | leading coefficient for infinitely many p (both impossible if leading coefficient is fixed nonzero). Hence f ≡ 0.

**Stronger result:** If D(r) = 2(-1)^{r+1} + r! is a fixed integer and D(r) ≡ 0 (mod p) for all primes p > r, then D(r) = 0 (since only finitely many primes divide a fixed nonzero integer).

### 6.3 Divisibility Chains

When establishing p | f(n) for a prime p and fixed polynomial f, a common technique is:
1. Write f(n) in terms of (n-1)! using Wilson's theorem
2. Compute (n-r)! in terms of (n-1)! using the factorial identity
3. Derive a fixed constant that must be ≡ 0 (mod p) for all large primes p
4. Conclude the constant is 0

**Evaluation criterion:** Step 4 requires the explicit argument that a fixed nonzero integer cannot be divisible by all sufficiently large primes. This is often stated as "the only way infinitely many primes can divide a fixed integer is if that integer is zero." This argument is valid and may be stated briefly in a competition proof.

### 6.4 Parameterization of Divisors

When p^k | f(a,b) and p ∤ a and p ∤ b, we can sometimes factor f and analyze which prime power divides each factor separately. This often involves writing f(a,b) = g(a,b) · h(a,b) and showing gcd(g,h) | m for some explicit m.

---

## Part VII: Standard Techniques Specific to the Proofs in This Audit

### 7.1 Polynomial Divisibility and Wilson's Theorem (proof_01 type)

**Problem type:** Find all monic polynomials f ∈ Z[x] such that p | 2(f(p))!+1 for all large primes p.

**Standard approach:**
1. **Degree bound:** For deg f ≥ 2, f(p) ≥ p for large p, so p | (f(p))! and thus 2(f(p))!+1 ≡ 1 (mod p) ≠ 0. Eliminates deg ≥ 2.
2. **Constant polynomials:** f ≡ 1 (monic degree 0) gives 2·1!+1 = 3, only finitely many primes divide 3. Contradiction.
3. **Linear case:** f(x) = x+b. Positive b gives f(p) ≥ p → contradiction (same as deg ≥ 2). So b < 0, write b = -r, r > 0.
4. **Wilson application:** (p-1)! = (p-1)(p-2)···(p-r)·(p-r-1)! ≡ (-1)^r r! · (p-r-1)! (mod p). Combined with (p-1)! ≡ -1: get (p-r-1)! ≡ (-1)^{r+1}/(r!) (mod p).
5. **Fixed integer condition:** 2(p-r-1)!+1 ≡ 0 (mod p) translates to the fixed integer D_r = 2(-1)^{r+1} + r! ≡ 0 (mod p) for all large p. Hence D_r = 0.
6. **Find r:** Check small r until D_r = 0. Only r = 3 works: 2(-1)^4 + 3! = 2+6? No wait, let me recheck.

Actually for D_r = 2(-1)^{r+1} + r! (before the multiply through by r!), the condition after multiplying is: r! · 2(-1)^{r+1} + (r!)² = 0, or ... let me be careful. The exact form of D_r depends on the precise derivation. The proof should arrive at a specific integer that must be zero, and then check r=1,2,3,...

**Correctness check:** A correct proof must:
- Correctly derive the exact fixed integer D_r involving r
- Note that this being ≡ 0 (mod p) for all large p forces D_r = 0
- Correctly compute the specific value of r that makes D_r = 0
- Verify that this r gives a working polynomial f(x) = x - r

**First error in flawed proofs:** If the proof arrives at the wrong equation for D_r (perhaps confusing (p-r-1)! with (p-r)!), the final equation to solve will be wrong and the claimed value of r will be incorrect.

### 7.2 Gaussian Integer Factorization Problems (proof_06 type)

**Problem type:** Given a⁴+b⁴ = c⁴+d⁴ = e⁵ with distinct positive integers, show ac+bd is composite (or more generally, analyze the algebraic structure).

**Standard approach:**
1. **Reduction:** By coprimality of a,b,c,d,e (if a common factor p existed, divide through and repeat), assume gcd = 1.
2. **Factorization in Z[i]:** a⁴+b⁴ = (a²+ib²)(a²-ib²). Show these factors are coprime in Z[i].
3. **UFD consequence:** Each factor is a fifth power times a unit: a²+ib² = ε·α⁵ for some α = u+vi ∈ Z[i] and unit ε.
4. **Norm equation:** N(a²+ib²) = a⁴+b⁴ = e⁵. N(α⁵) = N(α)⁵ = (u²+v²)⁵. Hence e = u²+v².
5. **Repeat for (c,d):** c²+id² = ε'·α⁵ for some unit ε'. Since both pairs factorize in terms of the same α = u+vi...

**Critical subtlety:** At step 5, the claim that (c²+id²) must involve the SAME α as (a²+ib²) requires justification. Both (a²+ib²) and (c²+id²) equal fifth powers (times units) of Gaussian integers with norm e = u²+v². But different choices of unit ε could give genuinely different fifth-power Gaussian integers. The argument "the assignment must swap because the pairs are distinct" needs to be made rigorous.

**Evaluation criterion:** A proof that hand-waves the step "hence the two factorizations must be related by swapping u+vi and u-vi" without justifying why has a logical gap. Moreover, the conclusion c²=a², d²=-b² cannot hold for positive real a,b,c,d. If the proof DOES correctly derive a contradiction, the verdict is correct. If it makes an unjustified leap to derive this contradiction, the verdict is incorrect.

### 7.3 Divisibility Congruences and Case Analysis (proof_10 type)

**Problem type:** Prove or disprove that specific prime-power Diophantine equations have solutions.

**Common structure:** Write the equation as p · f(q,b) = g(b) for primes p and q, then case-analyze on q = 2 vs q odd.

**Evaluation criterion for case q=2:** The claim "p | 4·7^b - 1 implies p = 3" requires showing that 4·7^b ≡ 1 (mod p) has solutions only for p = 3. This requires either:
(a) Computing ord_p(7) and checking divisibility conditions, OR
(b) Direct case analysis for small primes

Simply asserting the conclusion without either computation or case analysis is an unjustified gap.

### 7.4 Algebraic Inequalities in Number Theory (proof_17 type)

**Problem type:** Use algebraic inequalities to bound prime-related quantities.

**Key principle:** When a proof uses an estimate like "Kp^a < Mp^b" for all positive p, both K and M must be explicitly computed, and the direction of the inequality must be verified for all relevant cases.

**Common error:** Writing an inequality in the wrong direction (e.g., 27p² < 9p² is false for all positive p). This immediately invalidates any argument that depends on it.

**Evaluation criterion:** Check every inequality claim. If any single inequality is in the wrong direction for the claimed values, the proof is incorrect at that step, regardless of whether the conclusion might be provable by other means.

---

## Part VIII: Evaluation Rubric Summary for Number Theory Proofs

When evaluating a number theory proof in this audit, apply the following checklist:

1. **Factual accuracy:** Are all theorems cited correctly? (Wilson, Fermat, Euler, LTE, QR)
2. **Hypothesis completeness:** Are all hypotheses of each theorem explicitly verified before application?
3. **Case completeness:** Are all cases covered? (Especially: what if q = 2? what if p = 2? what if the base case fails?)
4. **Fixed-integer arguments:** When a fixed integer must be divisible by all large primes, is the conclusion "hence the integer is 0" correctly derived?
5. **Coprimality:** When coprimality of two expressions is needed, is it proved or given?
6. **UFD consequences:** When factoring in Z[i] or other number rings, is unique factorization correctly applied?
7. **Direction of inequalities:** Are all stated inequalities in the correct direction for the claimed parameters?

A proof with ANY false claim, unjustified transition, or missing critical case at any of these points should be marked **incorrect**, and the FIRST such occurrence is the first material issue.

---

## Part IX: Extended Examples of Correct and Incorrect Number Theory Reasoning

### Example 1: Correct use of Wilson's Theorem

**Claim:** For prime p > 5, p | (p-4)! + (p-3)·(p-4)!/p + ... 

**Approach:** Start from (p-1)! = (p-1)(p-2)(p-3)(p-4)! ≡ (-1)(-2)(-3)(p-4)! = -6(p-4)! (mod p). Since (p-1)! ≡ -1 (mod p), we get -6(p-4)! ≡ -1 (mod p), so (p-4)! ≡ (6)^{-1} ≡ (6)^{-1} (mod p). **This is a correct use of Wilson's theorem**, assuming the inverses exist (which they do for p > 3).

### Example 2: Incorrect application — wrong formula

**Claim:** (p-1)! = (p-1)(p-2)···(p-r) · (p-r)! (off-by-one error in factorial)

This is FALSE: (p-1)! = (p-1)(p-2)···(p-r) · (p-r-1)!, not (p-r)!. An off-by-one error in the factorial formula would give a completely wrong value for D_r, leading to an incorrect determination of r.

### Example 3: Correct coprimality argument in Z[i]

**Claim:** gcd_{Z[i]}(a²+ib², a²-ib²) is a unit, given that a⁴+b⁴ = e⁵ and gcd(a,b) = 1.

**Proof:** Let δ = gcd(a²+ib², a²-ib²). Then δ | (a²+ib²)-(a²-ib²) = 2ib². Also δ | (a²+ib²)+(a²-ib²) = 2a². So δ | gcd(2ib², 2a²) = 2·gcd(b², a²)·i. Since gcd(a,b) = 1, gcd(a²,b²) = 1 in Z, so δ | 2i. The only Gaussian prime dividing 2i = -i(1+i)² is (1+i). If (1+i) | (a²+ib²), then N(1+i)=2 | N(a²+ib²) = a⁴+b⁴ = e⁵, so 2 | e⁵, hence 2 | e. Then 2^5 | e⁵ = a⁴+b⁴. But if a and b are both odd, a⁴+b⁴ ≡ 1+1 = 2 (mod 4), not 0 (mod 32). Careful analysis shows (1+i) ∤ (a²+ib²) under the coprimality assumptions. **This is a correct argument.**

### Example 4: Incorrect — overlooked unit ambiguity

**Claim:** Since a²+ib² = (u+vi)⁵ and c²+id² = ε'(u+vi)⁵ for unit ε', and (a²,b²) ≠ (c²,d²), the unit ε' must be i or -i, forcing c² = -a², d² = b².

**Error:** This doesn't follow. The unit ε' could be 1, -1, i, or -i. The case ε' = -1 gives c²+id² = -(u+vi)⁵ = (-u-vi)⁵... one needs to trace through each case systematically. Simply asserting "it must be i or -i" based on distinctness is an unjustified leap.

### Example 5: Correct evaluation — catch the wrong inequality

**Claim in proof:** "Since 3(k+1)p² ≤ 9p² for k ≥ 2, we have..."

**Check:** 3(k+1) ≤ 9 iff k+1 ≤ 3 iff k ≤ 2. For k ≥ 2, we have k+1 ≥ 3 so 3(k+1) ≥ 9. The inequality is BACKWARDS for k ≥ 3. This is the first material issue.

### Example 6: Correct handling of cases in divisibility

**Claim:** For the equation 4p^k = 7^m + 1, analyzing case p = 2: we get 2^{k+2} = 7^m + 1. Modulo 4: 0 ≡ 7^m + 1 ≡ 3^m + 1 (mod 4). For m even: 3^m ≡ 1 (mod 4), so 3^m+1 ≡ 2 (mod 4), but 2^{k+2} ≡ 0 (mod 4) for k ≥ 0. Contradiction unless k+2 = 1 i.e. k = -1 (not valid). For m odd: 3^m ≡ 3 (mod 4), so 3^m+1 ≡ 0 (mod 4). OK so m must be odd. Continue: 2^{k+2} = 7^m+1 and m odd... **This is a correct case analysis approach** — systematically checking mod small numbers to constrain the variables.

---

## Part X: Summary of First Material Issues Commonly Found

In number theory proofs at olympiad level, the most common first material issues are:

1. **Wrong inequality direction** — claimed "a < b" when actually a ≥ b for the values in question
2. **Missing case** — analyzed case p odd but not p = 2 (or vice versa), or analyzed cases modulo 3 but missed a residue class
3. **Unjustified divisibility claim** — said "p | N implies p = q" without showing why
4. **Incorrect application of Wilson** — used wrong factorial or wrong parity of (-1)
5. **Coprimality assumed, not proven** — applied UFD factoring without establishing coprimality
6. **Wrong final value** — computed D_r = 0 for wrong r, claiming incorrect polynomial
7. **Overlooked units in Z[i]** — in Gaussian integer arguments, forgot to account for all four units {1, -1, i, -i}
8. **Circular case elimination** — "proved" case q=2 by assuming p=3 and checking consistency, rather than deriving p=3 from q=2

Any of the above at the FIRST occurrence in a proof constitutes a material issue and should be reported as the first_material_issue_summary in your audit.

---

## Appendix A: Extended Worked Examples — Number Theory Proof Evaluation

### A.1 Wilson's Theorem Applications — 20 Evaluation Scenarios

**Scenario 1 (Correct).** Claim: "For prime p > 3, p divides (p-2)! - 1."
Proof: (p-1)! = (p-1)(p-2)! ≡ -1 (mod p). Also (p-1) ≡ -1 (mod p), so (-1)(p-2)! ≡ -1 (mod p), giving (p-2)! ≡ 1 (mod p). Hence p | (p-2)! - 1. Assessment: CORRECT. Uses Wilson properly, all steps valid.

**Scenario 2 (Incorrect — wrong case boundary).** Claim: "For prime p ≥ 2, p | (p-1)!+1."
Proof: By Wilson's theorem, (p-1)! ≡ -1 (mod p), so (p-1)!+1 ≡ 0 (mod p). Assessment: INCORRECT first material issue. For p = 2: (2-1)! = 1! = 1, and 1+1 = 2. 2|2 holds. But the proof works for all primes p ≥ 2. Actually CORRECT — Wilson holds for p=2: (2-1)! = 1 ≡ -1 ≡ 1 (mod 2), so (2-1)!+1 = 2 ≡ 0 (mod 2). So this proof is correct after all.

**Scenario 3 (Incorrect — composite modulus).** Claim: "15 | (15-1)! + 1 by Wilson's theorem."
First material issue: Wilson's theorem requires p to be prime. 15 = 3×5 is not prime. In fact (14)! = 14·13·...·1 contains factors 3, 5, 6, 10, 15... wait, 15 ∤ {1,...,14}, but 3·5 = 15 ∤ any single element yet 3 and 5 are both in {1,...,14}. So 15 | 14! and 14!+1 ≡ 1 (mod 15) ≠ 0. INCORRECT: first issue is applying Wilson to non-prime 15.

**Scenario 4 (Correct).** Claim: "For prime p, ((p-1)/2)!² ≡ (-1)^{(p+1)/2} (mod p)."
Proof: (p-1)! ≡ -1. Pair j with p-j for j=1,...,(p-1)/2. Product of each pair = j(p-j) ≡ j(-j) = -j² (mod p). Product of all pairs = Π_{j=1}^{(p-1)/2} (-j²) = (-1)^{(p-1)/2} · (((p-1)/2)!)². So (p-1)! = (-1)^{(p-1)/2} · (((p-1)/2)!)² ≡ -1. Hence (((p-1)/2)!)² ≡ (-1)^{(p+1)/2}. CORRECT.

**Scenario 5 (Incorrect — off-by-one).** Claim: "For prime p and r=3: (p-1)! = (p-1)(p-2)(p-3) · (p-3)!."
First material issue: (p-1)! = (p-1)(p-2)(p-3)(p-4)···1. Extracting the first 3 terms: (p-1)! = (p-1)(p-2)(p-3) · (p-4)!, NOT (p-3)!. The off-by-one error gives the wrong factorial: (p-3)! vs (p-4)!.

**Scenario 6 (Correct).** Claim: "Let D₃ = 2(-1)^4 + 3! = 2 + 6 = 8. Since D₃ ≠ 0, r = 3 is not a solution."
The correct formula is D_r = 2(-1)^r + (r-1)! and one checks r=3 gives D_3 = -2+2=0.

**Scenario W7 (Correct — Wilson derivation step).** "(p-1)! = product_{j=1}^{p-1} j = (product_{j=1}^{r} (p-j)) * (product_{j=1}^{p-r-1} j) = (product_{j=1}^r (-j) (mod p)) * (p-r-1)! = (-1)^r*r!*(p-r-1)! (mod p)." ✓

**Scenario W8 (Correct — fixed integer argument).** "The quantity 2(-1)^r + (r-1)! is a fixed integer independent of p. If this integer is nonzero, it has finitely many prime divisors, so only finitely many primes p can satisfy the congruence. Hence it must equal 0." ✓

**Scenario W9 (Incorrect — r=2 claimed as solution).** Suppose someone computes D_2 = 2(-1)^2 + 1! = 2+1 = 3 ≠ 0, yet claims r=2 is a solution. INCORRECT: D_2 = 3 ≠ 0 means p | 3 for all large p, which fails for p > 3. Not a solution.

**Scenario W10 (Correct — verification for r=3).** "f(x)=x-3. For prime p > 3: (p-1)! = (p-1)(p-2)(p-3)*(p-4)!... wait, (p-1)! = (p-1)(p-2)(p-3)*(p-3-1)! hmm. Let me use: (p-1)(p-2)(p-3) ≡ (-1)(-2)(-3) = -6 (mod p). And (p-1)! = (-6)*(p-4)!. But (p-1)! ≡ -1. So (-6)*(p-4)! ≡ -1, giving (p-4)! ≡ 1/6 (mod p). Hmm, this doesn't directly give 2(p-3)!+1. Better: (p-1)! = (p-1)(p-2)(p-3)*(p-3-1)! hmm again. Let me think. Actually (p-3)! * (p-2) * (p-1) = (p-1)! but that's wrong too. (p-3)! * 1 = (p-3)! and we need to get from (p-3)! to (p-1)!. 

(p-1)! = (p-3)! * (p-2) * (p-1) ≡ (p-3)! * (-2)(-1) = 2*(p-3)! (mod p). So 2*(p-3)! ≡ (p-1)! ≡ -1 (mod p). Hence 2*(p-3)!+1 ≡ 0 (mod p). ✓"

This is the cleanest verification for r=3. Note: the key step is (p-1)! = (p-3)! * (p-2) * (p-1) ≡ (p-3)! * (-2)(-1) = 2*(p-3)! (mod p). The formula is (p-r-1)! going from (p-1)! by stripping the r=3 terms: 

Actually: f(p)! = (p-3)!. And (p-1)! = (p-1)(p-2)(p-3) * (p-4)!. 
Hmm: p-3 terms from (p-1) to (p-3) are: (p-1)(p-2)(p-3). And (p-1)! = (p-1)(p-2)(p-3)(p-4)!.
But (p-3)! = (p-3)(p-4)! ... no, (p-3)! = 1*2*...*p-3 = (p-4)! * (p-3).
So (p-4)! = (p-3)! / (p-3).

(p-1)! = (p-1)(p-2)(p-3) * (p-4)! = (p-1)(p-2)(p-3) * (p-3)!/(p-3) = (p-1)(p-2) * (p-3)!.

Wait: (p-1)(p-2)(p-3) * (p-4)! = (p-1)! means (p-3)! = (p-3)(p-4)! (by definition). So (p-4)! = (p-3)!/(p-3). And (p-1)! = (p-1)(p-2)(p-3) * (p-3)!/(p-3) = (p-1)(p-2)*(p-3)!.

(p-1)(p-2) ≡ (-1)(-2) = 2 (mod p). So (p-1)! ≡ 2*(p-3)! (mod p). By Wilson: -1 ≡ 2*(p-3)! (mod p). Hence 2*(p-3)! ≡ -1, so 2*(p-3)!+1 ≡ 0 (mod p). ✓

### D.2 Gaussian Integer Arguments — 20 Additional Scenarios

**GI1 (Correct — basic arithmetic in Z[i]).** "(2+3i) * (1-i) = 2 - 2i + 3i - 3i^2 = 2 - 2i + 3i + 3 = 5 + i." N(2+3i) = 13. N(1-i) = 2. N(5+i) = 26 = 13*2. ✓

**GI2 (Correct — Gaussian prime check).** "Is 3 a Gaussian prime? 3 ≡ 3 (mod 4). Primes p ≡ 3 (mod 4) remain prime in Z[i]. So 3 is a Gaussian prime." ✓

**GI3 (Correct — Gaussian prime factorization).** "Factor 5 in Z[i]: 5 = (2+i)(2-i). N(2+i) = 5 prime in Z. 5 ≡ 1 (mod 4). So 5 splits." ✓

**GI4 (Incorrect — confusing Z and Z[i] primes).** "3 is prime in Z, so 3 is prime in Z[i]."
INCORRECT: Not all rational primes are Gaussian primes. Primes p ≡ 1 (mod 4) split in Z[i]. However, primes p ≡ 3 (mod 4) do remain prime. Since 3 ≡ 3 (mod 4), 3 IS a Gaussian prime. But the claim "Z-prime implies Z[i]-prime" is WRONG IN GENERAL (e.g., 5 = (2+i)(2-i) splits). The reasoning is wrong even though the conclusion for p=3 is correct.

**GI5 (Correct — norm multiplicativity).** "N(alpha * beta) = N(alpha) * N(beta) for all alpha, beta in Z[i]." This follows from N(a+bi) = a^2+b^2 = |a+bi|^2 and |alpha*beta| = |alpha|*|beta| (complex modulus is multiplicative). ✓

**GI6 (Correct — coprimality check).** "gcd_{Z[i]}(a^2+ib^2, a^2-ib^2) with gcd(a,b)=1: any common divisor d divides (a^2+ib^2)-(a^2-ib^2) = 2ib^2 and (a^2+ib^2)+(a^2-ib^2) = 2a^2. So d | gcd_{Z[i]}(2ib^2, 2a^2). Since 2i is a unit times (1+i)^2 and gcd(a,b)=1 gives gcd(a^2,b^2)=1: the only common Gaussian prime could be (1+i). Analysis of whether (1+i) can divide both factors requires checking if 2 | a^4+b^4. If a and b are both odd: a^4+b^4 ≡ 1+1 = 2 (mod 4), so v_2(a^4+b^4) = 1, not divisible by 4, so (1+i) divides a^2+ib^2 to a limited power. The full coprimality analysis is standard." ✓ (Correct approach, details omitted)

**GI7 (Incorrect — wrong unit count).** "The units of Z[i] form a group {1,-1} under multiplication."
INCORRECT. The units of Z[i] are {1,-1,i,-i}. The group is cyclic of order 4 generated by i. Omitting ±i is a first material issue in any proof that then says "the only units are ±1."

**GI8 (Correct — fifth power structure).** "If alpha = u+vi with N(alpha)^5 = N(e^5) = e^5, then N(alpha) = e (taking the unique positive real 5th root). So (u+vi)^5 = epsilon*(a^2+ib^2) for some unit epsilon in {1,-1,i,-i}."
CORRECT. N((u+vi)^5) = N(u+vi)^5 = (u^2+v^2)^5. Setting = N(a^2+ib^2) = a^4+b^4 = e^5 gives (u^2+v^2)^5 = e^5, so u^2+v^2 = e. ✓

**GI9 (Incorrect — missing the swap case).** "Since (c^2+id^2) = epsilon'*(u+vi)^5 with epsilon' a unit and (a^2,b^2) != (c^2,d^2), the unit epsilon' must give a DIFFERENT expression than (a^2+ib^2) = epsilon*(u+vi)^5. The only other fifth power is (u-vi)^5 (complex conjugate). So epsilon'*(u+vi)^5 = (some unit)*(u-vi)^5, giving c^2+id^2 is related to u-vi."

PARTIALLY CORRECT: (c^2+id^2) and (a^2+ib^2) are indeed fifth powers (times units) of Gaussian integers of norm e. But there are more than just (u+vi)^5 and (u-vi)^5 up to units. Specifically: {(u+vi)^5, i*(u+vi)^5, -1*(u+vi)^5, -i*(u+vi)^5, (u-vi)^5, i*(u-vi)^5, -1*(u-vi)^5, -i*(u-vi)^5} are all fifth powers of Gaussian integers of norm e. The proof must carefully enumerate which unit makes the real and imaginary parts equal to c^2 and d^2 (which must be non-negative since c,d are positive integers).

**GI10 (Correct — real and imaginary part constraints).** "From c^2+id^2 = epsilon'*(u+vi)^5 with c,d > 0:
If epsilon'=1: Re = Re((u+vi)^5) = u^5-10u^3v^2+5uv^4 = u(u^4-10u^2v^2+5v^4). Must be c^2 > 0.
If epsilon'=-1: Re = -(u^5-10u^3v^2+5uv^4) = -c^2 < 0. IMPOSSIBLE for c^2 > 0.
If epsilon'=i: Re = -Im((u+vi)^5) = -(5u^4v-10u^2v^3+v^5) = -v(5u^4-10u^2v^2+v^4). Must be c^2 > 0. Requires v(5u^4-10u^2v^2+v^4) < 0.
If epsilon'=-i: Re = Im((u+vi)^5) = v(5u^4-10u^2v^2+v^4) = c^2 > 0. Requires this to be positive." ✓

This analysis is CORRECT and shows that the unit epsilon' is constrained by sign conditions on c,d,u,v. The claim "it must swap u+vi and u-vi" is only valid after this sign analysis.

### D.3 Prime Factorization and Divisibility — 20 Scenarios

**P1 (Correct).** "v_2(2^k) = k." TRIVIALLY CORRECT.

**P2 (Correct).** "v_p(p^a * q^b) = a for prime p != q." CORRECT by unique factorization.

**P3 (Correct).** "v_p(a+b) >= min(v_p(a), v_p(b)) with equality if v_p(a) != v_p(b)." CORRECT (ultrametric property).

**P4 (Incorrect).** "v_p(a+b) = min(v_p(a), v_p(b)) always."
INCORRECT: If v_p(a) = v_p(b), equality need not hold. E.g., a=p, b=-p: a+b=0, v_p(0)=infinity > min(1,1)=1.
Or: a=p, b=p: a+b=2p, v_p(2p)=1=min(1,1) IF p!=2. But a=2, b=2: a+b=4=2^2, v_2(4)=2 > min(v_2(2),v_2(2))=min(1,1)=1.

**P5 (Correct — Legendre's formula).** "v_p(n!) = sum_{k=1}^infinity floor(n/p^k) = (n - s_p(n))/(p-1) where s_p(n) = digit sum in base p."
CORRECT. Both formulas are valid. The sum formula is direct (count multiples of p, p^2, etc.). The closed form follows from the base-p expansion.

**P6 (Correct — application).** "v_5(100!) = floor(100/5)+floor(100/25)+floor(100/125)+... = 20+4+0 = 24."
CORRECT. ✓

**P7 (Incorrect — off-by-one in Legendre).** "v_2(10!) = floor(10/2)+floor(10/4)+floor(10/8) = 5+2+1+0 = 8."
CORRECT (checking): 8 = v_2(10!) since 10! = 3628800 = 2^8 * (odd). Indeed: 2,4,6,8,10 contribute 1,2,1,3,1 factors of 2: 1+2+1+3+1=8. ✓ So this is CORRECT.

**P8 (Incorrect — wrong lower bound).** "For a,b > 0 with a+b = n: v_p(a) + v_p(b) <= v_p(n) + v_p(C(n,a))."
Actually this is v_p(C(n,a)) = v_p(n!) - v_p(a!) - v_p(b!). This is the Kummer-like formula. The inequality v_p(a)+v_p(b) <= v_p(n) + v_p(C(n,a)) rearranges to v_p(C(n,a)) >= v_p(a)+v_p(b)-v_p(n)... checking this for specific cases could verify or falsify.

**P9 (Correct — prime detection via factorial).** "If n = p is prime: v_p((p-1)!) = 0 (since all factors are 1,...,p-1, none divisible by p). And v_p(p!) = 1." ✓

**P10 (Correct — Zsygmondy application).** "For a>b>0, gcd(a,b)=1, n>=3: a^n-b^n has a primitive prime divisor q (a prime q divides a^n-b^n but does not divide a^k-b^k for k<n), with exceptions: (a,b,n)=(2,1,6)."
CORRECT (Zsygmondy's theorem). This is often used in olympiad number theory to show expressions have large prime factors.

### D.4 Modular Arithmetic Reference — 15 Scenarios

**M1 (Correct).** "7^4 ≡ 1 (mod 5). Since 4 = phi(5), this follows from Fermat." ✓

**M2 (Incorrect).** "7^5 ≡ 7 (mod 5) by Fermat's little theorem."
INCORRECT: Fermat says a^{p-1} ≡ 1 (mod p), so 7^4 ≡ 1 (mod 5). Then 7^5 ≡ 7 (mod 5). And 7 ≡ 2 (mod 5). So 7^5 ≡ 2 (mod 5). The claim "7^5 ≡ 7 (mod 5)" is CORRECT in the sense that a^p ≡ a (mod p) by Fermat (multiplying 7^{p-1} ≡ 1 by 7). And 7 ≡ 2 (mod 5), so 7^5 ≡ 7 ≡ 2 (mod 5). The claim "7^5 ≡ 7 (mod 5)" is true but might be seen as not reduced.

**M3 (Correct).** "The order of 3 modulo 7 divides phi(7) = 6. Check: 3^1=3, 3^2=2, 3^3=6, 3^4=4, 3^5=5, 3^6=1 (mod 7). Order = 6. So 3 is a primitive root mod 7." ✓

**M4 (Correct).** "For prime p ≡ 1 (mod 4), (-1/p) = 1 (i.e., -1 is a QR mod p)."
By Euler's criterion: (-1/p) ≡ (-1)^{(p-1)/2} (mod p). Since p ≡ 1 (mod 4): (p-1)/2 is even, so (-1)^{(p-1)/2} = 1. ✓

**M5 (Incorrect).** "For prime p ≡ 3 (mod 4), -1 is a QR mod p."
INCORRECT: For p ≡ 3 (mod 4), (p-1)/2 is odd, so (-1)^{(p-1)/2} = -1, meaning (-1/p) = -1, i.e., -1 is a NON-residue mod p. The claim is FALSE.

**M6 (Correct).** "Chinese Remainder Theorem: x ≡ 2 (mod 3), x ≡ 3 (mod 5). Solution: x ≡ 8 (mod 15). Check: 8 = 6+2 ≡ 2 (mod 3) ✓; 8 = 5+3 ≡ 3 (mod 5) ✓." ✓

**M7 (Correct — Hensel lifting).** "x^2 ≡ 2 (mod 7): try x=3: 9=7+2 ≡ 2. ✓ Then lift to mod 49: x = 3+7t. (3+7t)^2 = 9+42t+49t^2 ≡ 9+42t ≡ 2+42t (mod 49). Need 42t ≡ -7 ≡ 42 (mod 49). t ≡ 1 (mod 7). So x ≡ 10 (mod 49)." ✓

### D.5 Summary: Evaluation Quick Reference for Number Theory Proofs

For a number theory proof involving:
1. Wilson's theorem: check factorial identity is correct, modular reduction is valid, fixed-integer conclusion is applied.
2. Gaussian integers: check units are {1,-1,i,-i}, coprimality is established, UFD is correctly applied.
3. Divisibility: check case analysis is complete (q=2 case especially), inequalities are in correct direction.
4. Modular arithmetic: check order of a prime is correctly computed, QR symbol is applied with right version.

Common first material issues:
- Off-by-one factorial: using (p-r)! instead of (p-r-1)! (or vice versa) in Wilson application
- Missing units: using ±1 instead of {1,-1,i,-i} in Gaussian integer arguments  
- Wrong inequality direction: 27p^2 < 9p^2 is FALSE
- Incomplete case analysis: missing q=2 case or not deriving p from the equation
- Using Wilson for composite modulus: INVALID

*End of Number Theory Extended Appendix*
