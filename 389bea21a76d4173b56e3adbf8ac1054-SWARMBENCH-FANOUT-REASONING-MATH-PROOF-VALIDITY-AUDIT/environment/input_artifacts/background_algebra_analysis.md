# Domain Background: Algebra and Analysis Proof Evaluation

This reference covers the mathematical theory, common proof techniques, and evaluation criteria relevant to olympiad algebra, inequalities, polynomial theory, and real analysis problems. Sub-agents auditing **proof_03**, **proof_05**, **proof_08**, **proof_14**, **proof_18**, and **proof_20** should read this document before evaluating their assigned proof.

---

## Part I: Inequalities

### 1.1 AM-GM and Related Inequalities

**Arithmetic-Geometric Mean Inequality:** For positive reals a₁,...,aₙ:
(a₁+a₂+...+aₙ)/n ≥ (a₁a₂...aₙ)^{1/n}
with equality iff a₁ = a₂ = ... = aₙ.

**Corollaries:**
- For two positives: (a+b)/2 ≥ √(ab), equivalently (a+b)² ≥ 4ab, equivalently ab/(a+b) ≤ (a+b)/4.
- Multiplying by 2c > 0: 2abc/(a+b) ≤ c(a+b)/2.
- More generally: for positive x,y with constraint: xy ≤ ((x+y)/2)² by AM-GM.

**Cauchy-Schwarz:** (Σaᵢbᵢ)² ≤ (Σaᵢ²)(Σbᵢ²) with equality iff aᵢ/bᵢ is constant.

**Engel form (Sedrakyan/Titu):** Σ(aᵢ²/bᵢ) ≥ (Σaᵢ)²/(Σbᵢ) for positive bᵢ.

**Power Mean Inequality:** For 0 < r < s:
M_r = ((Σaᵢʳ)/n)^{1/r} ≤ M_s = ((Σaᵢˢ)/n)^{1/s}

**Jensen's Inequality:** For a convex function φ: φ(Σλᵢxᵢ) ≤ Σλᵢφ(xᵢ) where λᵢ > 0 and Σλᵢ = 1. Reversed for concave functions.

### 1.2 Symmetric Inequalities

**SOS (Sum of Squares) method:** Express a non-negative quantity as a sum of squares. Useful for polynomials: if f(a,b,c) ≥ 0 for all positive reals, try to write f as a sum of squares of polynomials in a,b,c, possibly after normalization.

**Schur's inequality:** For a,b,c > 0 and t > 0:
aᵗ(a-b)(a-c) + bᵗ(b-a)(b-c) + cᵗ(c-a)(c-b) ≥ 0

**Muirhead's inequality:** For symmetric sums, the notation [α,β,γ] ≥ [α',β',γ'] (Muirhead's) applies when (α,β,γ) majorizes (α',β',γ').

### 1.3 Evaluation Criteria for Inequality Proofs

**Homogeneity normalization:** Many symmetric inequalities are homogeneous. If both sides have the same degree, one may normalize (e.g., set a+b+c = 1 or a₁+...+aₙ = 1). The normalization must preserve all constraints.

**Correct degree check:** Verify the degrees of both sides of the inequality. If degrees differ, the inequality is NOT homogeneous and normalization changes the problem.

**Monotonicity via derivative:** The claim "f'(x) < 0 for all x in domain" implies f is strictly decreasing on that domain. This claim is a FACTUAL assertion that must be verified — either by explicit computation of f' and showing f' < 0, or by citing a known result.

**First material issue for inequality proofs:** 
- If a derivative or convexity argument is used, verify the sign of f' or f'' explicitly for the relevant domain.
- If an AM-GM application is made, verify that all quantities are positive.
- If Cauchy-Schwarz is applied, verify the correct form is used.

---

## Part II: Polynomials

### 2.1 Basic Polynomial Theory

**Degree:** The degree of a polynomial f(x) = aₙxⁿ + ... + a₀ (aₙ ≠ 0) is n. Leading coefficient is aₙ.

**Roots:** By the fundamental theorem of algebra, a degree-n polynomial has exactly n roots (counting multiplicity) in ℂ.

**Lagrange interpolation:** Given n+1 points (x₀,y₀),...,(xₙ,yₙ) with distinct xᵢ, there is a unique polynomial of degree ≤ n passing through all of them:
P(x) = Σᵢ yᵢ · Π_{j≠i} (x-xⱼ)/(xᵢ-xⱼ)

**Consequence:** A polynomial of degree ≤ n is uniquely determined by its values at n+1 distinct points.

**Degree bound lemma:** A polynomial of degree ≤ n that evaluates to 0 at n+1 distinct points must be identically 0.

### 2.2 Polynomials with Symmetric Conditions

**Symmetric polynomials:** A polynomial f(x₁,...,xₙ) is symmetric if it is invariant under all permutations of variables. The fundamental theorem of symmetric polynomials: every symmetric polynomial is a polynomial in the elementary symmetric polynomials e₁,...,eₙ:
- e₁ = Σxᵢ
- e₂ = Σᵢ<ⱼ xᵢxⱼ
- e₃ = Σᵢ<ⱼ<ₖ xᵢxⱼxₖ
- ...
- eₙ = x₁x₂···xₙ

**Newton's power sum identities:** If pₖ = Σxᵢᵏ, then:
p₁ = e₁
p₂ = e₁p₁ - 2e₂
p₃ = e₁p₂ - e₂p₁ + 3e₃
...

**For three variables (x,y,z):**
x²+y²+z² = e₁² - 2e₂ = (x+y+z)² - 2(xy+yz+zx)
x³+y³+z³ = e₁³ - 3e₁e₂ + 3e₃ = (x+y+z)³ - 3(x+y+z)(xy+yz+zx) + 3xyz

Also: (x-y)²+(y-z)²+(z-x)² = 2(x²+y²+z²) - 2(xy+yz+zx) = 2(e₁² - 2e₂) - 2e₂ = 2(e₁² - 3e₂) = 2(S₁² - 3S₂).

### 2.3 Polynomial Functional Equations

**Method:** To find all polynomials P satisfying an identity F(P) = 0 or F(P, Q) = 0:
1. **Degree bound:** Compare degrees of both sides; the leading terms must match, giving a constraint on deg P.
2. **Coefficient matching:** After establishing deg P = d, substitute P(t) = aₐtᵈ + ... and match coefficients.
3. **Verification:** Plug the candidate polynomial back into the original identity to confirm.

**Degree comparison in asymptotics:** To compare degrees, take a variable to infinity and expand both sides in a power series. The leading terms must agree.

**Example:** If the identity equates two expressions, both expanded to order y^{n+1} and y^n, the coefficients of y^{n+1} give a constraint (often automatically satisfied) and the coefficients of y^n give a non-trivial constraint on the degree n.

### 2.4 Evaluation Criteria for Polynomial Proofs

**Degree bound:** The argument that "deg P ≤ n" based on asymptotic expansion must correctly identify the leading terms of both sides. An error in which power of y dominates (e.g., confusing y^n with y^{n+1}) would give the wrong degree constraint.

**Even/odd degree:** The claim "n must be even" based on cancellation of certain terms: if the coefficient of y^{n+1} on the RHS has a factor ((-1)^n + 1), then this vanishes only when n is odd. The correct conclusion is n must be EVEN (for non-vanishing leading term). An off-by-one error here changes the conclusion.

**Coefficient matching:** After establishing the degree, the system of linear equations from coefficient matching must be set up correctly. Common errors: sign errors, wrong expansion of symmetric sum identities, applying Vieta's formulas to the wrong polynomial.

---

## Part III: Real Analysis and Calculus in Olympiad Proofs

### 3.1 Monotonicity via Derivatives

A differentiable function f: (a,b) → ℝ is strictly increasing if f'(x) > 0 for all x ∈ (a,b), and strictly decreasing if f'(x) < 0 for all x ∈ (a,b).

**Verification requirement:** If a proof asserts f'(x) < 0 to establish monotonicity, it must explicitly compute f'(x) and show it is negative. The assertion "f'(x) < 0" is NOT self-evident.

**First material issue:** If f'(x) < 0 is claimed but either:
(a) f'(x) is not computed, or
(b) f'(x) is computed but the inequality f'(x) < 0 does not hold for the relevant x,

then the proof is incorrect at this step.

**Common errors with derivatives:**
- Differentiating incorrectly (product rule, chain rule errors)
- Stating the wrong derivative formula
- Claiming the derivative is negative when it could be zero or positive for some values in the domain

### 3.2 Compactness and Existence of Minima

**Weierstrass extreme value theorem:** A continuous function on a compact (closed and bounded) set in ℝⁿ attains its minimum and maximum.

**Non-compact case:** If the domain is not compact (e.g., all of ℝⁿ, or an open set, or unbounded), the function may not attain its minimum. To establish existence of a minimum, one of the following is needed:
- Show the domain IS compact
- Show the function is coercive (f(x) → ∞ as |x| → ∞), reducing to a compact sublevel set
- Direct construction of the minimum

**Evaluation criterion for analysis proofs:** If a proof claims "the minimum is attained" by a compactness argument, verify:
- The domain is indeed compact (closed and bounded), OR
- The specific compact set used in the argument is correctly identified and the function's behavior at the boundary/infinity justifies restriction to this compact set

If the domain is not compact and no coercivity argument is given, the existence of the minimum is not established.

### 3.3 Continuity and Limit Arguments

**Sequential continuity:** f is continuous at a if for every sequence xₙ → a, f(xₙ) → f(a).

**Polynomial continuation:** A polynomial identity that holds for all x ≠ c (where c is a single excluded point) also holds at x = c by continuity. More generally, a polynomial identity that holds on a dense set holds everywhere.

**Extension by continuity:** If F(x,y) = G(x,y) for all (x,y) avoiding the set {2xy=1} (which is a curve in ℝ²), then by continuity it holds everywhere. This is valid for continuous functions. For polynomials, a stronger argument: if P = Q at infinitely many points, then P ≡ Q as polynomials.

---

## Part IV: Polynomial Interpolation and Linear Algebra

### 4.1 Vandermonde Matrices

The Vandermonde matrix V = (xᵢʲ⁻¹)_{i,j=1,...,n} for distinct points x₁,...,xₙ has determinant Π_{1≤i<j≤n}(xⱼ-xᵢ) ≠ 0. Hence it is invertible.

**Consequence:** The system of n equations P(xᵢ) = yᵢ (i=1,...,n) for a polynomial of degree ≤ n-1 has a unique solution given distinct xᵢ.

### 4.2 Linear Spaces of Polynomials

The space of polynomials of degree ≤ n over ℝ is an (n+1)-dimensional vector space. Linear constraints (each of the form "the value at a specific point equals something") reduce the dimension by 1 per independent constraint.

**Evaluation criterion for interpolation proofs:** 
- A proof that "the solution space has dimension ≥ 1" from n constraints in n+1 unknowns is correct (the system is underdetermined).
- The claim "a nonzero polynomial exists of degree AT MOST n satisfying n homogeneous linear conditions" follows from the dimension count: at most n conditions can reduce (n+1)-dimensional space by at most n, leaving dimension ≥ 1.
- The argument "a solution of degree EXACTLY n exists" requires showing the solution space is not entirely in the subspace {aₙ = 0}. This needs additional reasoning.

### 4.3 Ensuring Exact Degree

**Method 1:** If any of the n conditions involves the coefficient aₙ with a nonzero coefficient, then aₙ is not forced to be 0 by the conditions.

**Method 2:** If all conditions happen to set xᵢₙ + xⱼₙ = 0 for all pairs, then aₙ = 0 is forced; but this occurs only in special configurations (symmetric about 0 with odd degree).

**Evaluation criterion:** The argument "we can choose a solution with aₙ ≠ 0" needs to explicitly handle the case where all n conditions have zero coefficient of aₙ (e.g., when all pairs satisfy xᵢₙ + xⱼₙ = 0 for the specific matching chosen). If this case is handled (even briefly), the proof is valid on this point.

### 4.4 Matching Construction in Interpolation Problems

**Context:** For 2n distinct points x₁,...,x_{2n}, pair them as {i_k, j_k} (k=1,...,n) and require Q(x_{iₖ})+Q(x_{jₖ}) = 0 for each pair.

**Homogeneity:** These are n homogeneous linear equations in the n+1 coefficients a₀,...,aₙ. The system always has a nonzero solution (kernel has dimension ≥ 1).

**Evaluation criterion:** The pairing ({i_k, j_k}) is a perfect matching on {1,...,2n}. Such a matching exists for any 2n elements (pair them up sequentially or in any bijective way). This is valid — a perfect matching always exists for an even number of elements. An incorrect claim would be that a specific type of matching (e.g., "adjacent" pairs) is required; any matching works.

---

## Part V: Symmetric Sums and Competition Algebra

### 5.1 Elementary Symmetric Polynomials

For x, y, z with constraint 2xyz = x+y+z (equivalently 2S₃ = S₁ in terms of elementary symmetric polynomials):
- S₁ = x+y+z
- S₂ = xy+yz+zx
- S₃ = xyz = S₁/2

Standard substitutions:
- x³+y³+z³ = S₁³-3S₁S₂+3S₃ = S₁³-3S₁S₂+3S₁/2
- xP(x)+yP(y)+zP(z) for P(t) = at²+bt+c: = a(x³+y³+z³)+b(x²+y²+z²)+c(x+y+z) = a(S₁³-3S₁S₂+3S₁/2)+b(S₁²-2S₂)+cS₁

### 5.2 Generating the Degree Bound

For the functional equation P(x)/yz + P(y)/zx + P(z)/xy = P(x-y)+P(y-z)+P(z-x):

After multiplying by xyz = S₃ = S₁/2, the equation becomes:
2(xP(x)+yP(y)+zP(z)) = S₁(P(x-y)+P(y-z)+P(z-x)) ... (*)

To determine deg P, fix x and let y → ∞ with z determined by 2xyz = x+y+z:
z = (x+y)/(2xy-1) ≈ 1/(2x) as y → ∞

LHS of (*): 2(xP(x)+yP(y)+zP(z)) ≈ 2yP(y) for large y; if deg P = n, this is ≈ 2aₙy^{n+1}.

RHS of (*): S₁ = x+y+z ≈ y; P(x-y) ≈ aₙ(-y)^n = aₙ(-1)^n y^n; P(y-z) ≈ aₙy^n; P(z-x) = O(1).
So P(x-y)+P(y-z)+P(z-x) ≈ aₙ((-1)^n+1)y^n.
RHS ≈ y · aₙ((-1)^n+1)y^n = aₙ((-1)^n+1)y^{n+1}.

Matching y^{n+1} coefficients: 2aₙ = aₙ((-1)^n+1).
If n is odd: (-1)^n = -1, so (-1)^n+1 = 0, giving 2aₙ = 0 → aₙ = 0. Contradiction.
If n is even: (-1)^n = 1, so (-1)^n+1 = 2, giving 2aₙ = 2aₙ. ✓ No constraint.

Matching y^n coefficients (with n even, (-1)^n = 1):
LHS y^n: 2aₙ₋₁ (from 2yP(y) expanded to next order)
RHS y^n: complex expression involving n and x. For the equality to hold for all x, the dependence on x must vanish. This gives n = 2.

**Evaluation criterion for degree bound argument:** The key steps are:
1. Correctly expand both sides in powers of y
2. Correctly identify the leading coefficient of y^{n+1} on both sides
3. Determine that n must be even (odd n gives 0 = 2aₙ)
4. Expand to next order (y^n) and show n = 2

An error in step 2 or 3 (e.g., claiming n must be odd, or wrong leading coefficient) is a material issue.

### 5.3 Completing the Coefficient Matching

For P(t) = at²+bt+c with the constraint 2xyz = x+y+z (so 2S₃ = S₁):

LHS: 2(xP(x)+yP(y)+zP(z)) = 2[a(S₁³-3S₁S₂+3S₁/2)+b(S₁²-2S₂)+cS₁]
    = 2aS₁³-6aS₁S₂+3aS₁+2bS₁²-4bS₂+2cS₁

RHS: S₁[P(x-y)+P(y-z)+P(z-x)]
   = S₁[a·2(S₁²-3S₂)+b·0+3c]     (using (x-y)²+(y-z)²+(z-x)² = 2(S₁²-3S₂) and linear terms cancel)
   = 2aS₁³-6aS₁S₂+3cS₁

Setting LHS = RHS:
2aS₁³-6aS₁S₂+3aS₁+2bS₁²-4bS₂+2cS₁ = 2aS₁³-6aS₁S₂+3cS₁

Cancel 2aS₁³-6aS₁S₂:
3aS₁+2bS₁²-4bS₂+2cS₁ = 3cS₁

Since S₁ and S₂ are "essentially independent" (they can vary independently for appropriate x,y,z):
- Coefficient of S₁²: 2b = 0 → b = 0
- Coefficient of S₂: -4b = 0 ✓ (consistent)
- Coefficient of S₁: 3a+2c = 3c → 3a = c → c = 3a

Hence P(t) = a(t²+3). ✓

**Evaluation criterion:** Check each algebraic step:
- Is (x-y)²+(y-z)²+(z-x)² = 2(S₁²-3S₂) correct? 
  LHS = 2(x²+y²+z²)-2(xy+yz+zx) = 2(S₁²-2S₂)-2S₂ = 2S₁²-4S₂-2S₂ = 2S₁²-6S₂. So 2(S₁²-3S₂). ✓
- Are the symmetric sum identities applied correctly?

---

## Part VI: Optimization Theory

### 6.1 Existence of Extrema

**Necessary condition:** A local extremum of f at x₀ (assuming f differentiable) requires f'(x₀) = 0 or x₀ is a boundary point.

**Critical points:** Points where f'(x) = 0 are candidates for extrema. One must still verify it's an actual extremum (not just a stationary point) using the second derivative test or other criteria.

**Global vs local:** A local minimum may not be the global minimum. To establish global minimum, either:
- Show there's only one critical point and it's a minimum
- Compare values at all critical points and boundary points
- Use convexity/concavity to ensure uniqueness

### 6.2 Convex Optimization

A function f is convex if f(λx+(1-λ)y) ≤ λf(x)+(1-λ)f(y) for all x,y in the domain and λ ∈ [0,1]. For differentiable f, convexity is equivalent to f'' ≥ 0 everywhere.

**For convex functions:** Any local minimum is a global minimum. If f is strictly convex, the minimum is unique.

**Common error in optimization proofs:** Claiming a minimum is achieved without either:
(a) Using Weierstrass (requires compact domain)
(b) Using coercivity (f → ∞ at infinity)
(c) Showing the infimum is attained by direct construction

If neither is provided, existence of the minimum is not established.

### 6.3 Lagrange Multipliers

For minimizing f(x) subject to g(x) = c, at a local extremum: ∇f = λ∇g (if ∇g ≠ 0).

**Evaluation criterion:** A proof using Lagrange multipliers must:
- Verify the constraint qualification (∇g ≠ 0 at the critical point)
- Find all critical points
- Check that the minimum is among the critical points (not on the boundary or at infinity)

### 6.4 Skipped Computations in Optimization

**Common gap:** An optimization proof sets up the problem (writes down the function to minimize, identifies what the minimum "should be") but then skips the actual computation that finds the minimum value. Claims like "it can be computed that the minimum is..." without computation are incomplete.

**Evaluation criterion:** The computation of the minimum must be explicit. If the minimum is found by AM-GM or Cauchy-Schwarz, the specific application must be shown. If it's found by derivatives, the computation of the critical point must be shown.

---

## Part VII: Analysis and Compactness

### 7.1 Compact Sets in ℝⁿ

A subset K ⊆ ℝⁿ is compact if and only if it is closed and bounded (Heine-Borel theorem).

**Sequences:** Every sequence in a compact set has a convergent subsequence (limit in the same set).

**Application:** If the domain of an optimization problem is compact, continuous functions attain their minimum and maximum. This is the key theorem behind existence of optimal solutions.

### 7.2 Non-Compact Domains

**Half-spaces, hyperplanes, cones:** These are typically closed but not bounded, hence not compact.

**Sets defined by infinite constraints:** The intersection of infinitely many closed sets is closed (hence potentially non-compact). The intersection of finitely many closed sets is closed.

**Common error:** Claiming a set is compact when it is only closed (but not bounded), or only bounded (but not closed). In ℝⁿ, both conditions are needed.

**Specific non-compact example:** For a problem where the variables can take arbitrarily large values subject to given constraints, the feasible region is typically non-compact. The minimum may or may not exist and requires separate analysis.

### 7.3 The Brouwer Fixed Point Theorem

Every continuous map from a compact convex set K ⊆ ℝⁿ to itself has a fixed point.

**Application in geometry:** For finding specific points (circumcenters, incenters, etc.) as fixed points of maps related to the figure.

### 7.4 Evaluation Criteria for Analysis Proofs

**Existence of minimum:** Must establish via compactness (domain is compact + Weierstrass) or via direct construction.

**Finiteness claims:** "The infimum is finite" is usually clear if the problem has any constraint (e.g., a,b,c are bounded below by 0). But attainment of the infimum requires compactness or direct construction.

**Limit arguments:** "As xₙ → x₀, f(xₙ) → f(x₀)" requires continuity of f. This is automatic for polynomials and rational functions (away from poles), but must be verified for general f.

---

## Part VIII: Polynomial Interpolation in Functional Settings

### 8.1 The Magician Trick Problem Type

**Setup:** n points x₁,...,x_{2n} are fixed. A degree-n polynomial P is chosen secretly. The sorted tuple of values (P(x₁),...,P(x_{2n})) (sorted in non-decreasing order) is revealed. Can the polynomial be uniquely recovered?

**Answer structure:** If YES, one must show the map P ↦ sorted(P(x₁),...,P(x_{2n})) is injective on degree-n polynomials. If NO, one must exhibit two distinct degree-n polynomials with the same sorted tuple of values.

**For NO:** The approach is to find Q ≠ P of degree n with {Q(xᵢ)} = {P(xᵢ)} as multisets (values up to permutation). Taking P = -Q works if Q(xσ(i)) = -Q(xᵢ) for some permutation σ, which is possible if we can find Q with paired values: Q(xᵢ) + Q(xⱼ) = 0 for some perfect matching {i,j}.

**Evaluation criterion:** The argument must:
1. Construct a valid degree-n polynomial Q with the pairing property (not just degree ≤ n)
2. Show Q ≠ 0 (so P = -Q ≠ Q in general)
3. Show the multisets {Q(xᵢ)} and {-Q(xᵢ)} = {P(xᵢ)} are equal

The critical step is ensuring deg Q = n exactly (not just ≤ n). This requires showing the degree-n coefficient can be made nonzero, which is the nontrivial part of the argument.

### 8.2 Linear Algebra over ℝ

**Dimension of kernel:** If A is an m×n matrix with m ≤ n, the kernel of A has dimension ≥ n-m. For m = n, the kernel is trivial iff A is invertible.

**Nonzero solutions:** The homogeneous system Ax = 0 (m equations, n unknowns, m < n) always has a nonzero solution.

**Subspace inclusion:** The kernel of a linear functional L: V → ℝ (where V is a vector space and L ≠ 0) is a hyperplane (codimension 1 subspace). The kernel of A consists of all vectors orthogonal to the row space of A.

**Evaluation criterion:** The claim "the solution space is not contained in {aₙ = 0}" must be supported by showing that the n constraints do not all kill the aₙ component. This requires either:
- Direct: the column of A corresponding to aₙ is not in the row space of the constraint matrix restricted to other variables
- Indirect: at least one constraint has nonzero coefficient for aₙ, AND there's at least one solution with aₙ ≠ 0

---

## Part IX: Summary of Evaluation Criteria

### 9.1 For Inequality Proofs (proof_03 type)

1. Is the normalization valid (degrees match, constraints preserved)?
2. Is the AM-GM application correct (positive quantities, correct form)?
3. Is the algebraic manipulation correct (expanding products, collecting terms)?
4. Is the final inequality direction correct?

### 9.2 For Monotonicity Proofs (proof_05 type)

1. Is f'(x) correctly computed?
2. Is the sign of f'(x) correctly determined for the relevant domain?
3. If f'(x) < 0 is claimed but actually f'(x) ≥ 0 for some x in the domain, this is the first material issue.

### 9.3 For Optimization Proofs (proof_08 type)

1. Is existence of the minimum established (compactness or direct construction)?
2. Is the critical point computation explicit?
3. Is the minimum value correctly computed?
4. Are all cases (boundaries, infinity) handled?

### 9.4 For Compactness/Analysis Proofs (proof_14 type)

1. Is the domain closed and bounded (compact)?
2. Is the function continuous?
3. Is Weierstrass correctly applied?
4. If compactness fails, is an alternative existence argument given?

### 9.5 For Polynomial Interpolation Proofs (proof_18 type)

1. Is the perfect matching well-defined and explicitly constructed?
2. Are the linear constraints correctly formulated?
3. Is the dimension count correct (n homogeneous equations in n+1 unknowns)?
4. Is the degree-exactly-n argument sound?
5. Is the multiset equality correctly verified?

### 9.6 For Polynomial Functional Equation Proofs (proof_20 type)

1. Is the degree bound correctly derived (matching of leading coefficients)?
2. Is the substitution correct (z expressed in terms of x,y)?
3. Are the symmetric sum identities applied correctly?
4. Is the coefficient matching system correct?
5. Is the verification (plugging back) performed?

---

## Part X: Extended Examples

### Example 1: Correct inequality reduction

**Claim:** The inequality Σᵢ<ⱼ aᵢaⱼ/(aᵢ+aⱼ) ≤ n/(2s) · Σᵢ<ⱼ aᵢaⱼ reduces to the per-triple inequality aᵢaⱼaₖ/(aᵢ+aⱼ)+aᵢaⱼaₖ/(aᵢ+aₖ)+aᵢaⱼaₖ/(aⱼ+aₖ) ≤ (n-2)/2·(aᵢaⱼ+aᵢaₖ+aⱼaₖ).

**Analysis:** This is correct. The double sum Σᵢ<ⱼ Σₖ≠ᵢ,ⱼ aᵢaⱼaₖ/(aᵢ+aⱼ) counts each triple {i,j,k} exactly three times (once for each distinguished pair). The reduction to the per-triple inequality is valid. Then the use of AM-GM to bound each term is:
2aᵢaⱼaₖ/(aᵢ+aⱼ) ≤ aₖ(aᵢ+aⱼ)/2 [from xy/(x+y) ≤ (x+y)/4 with z = aₖ]

Adding cyclically: ≤ ½(aₖ(aᵢ+aⱼ)+aⱼ(aᵢ+aₖ)+aᵢ(aⱼ+aₖ)) = aᵢaⱼ+aᵢaₖ+aⱼaₖ.
Dividing by 2: LHS ≤ (aᵢaⱼ+aᵢaₖ+aⱼaₖ)/2.

This is stronger than the ≤ (n-2)/2·(aᵢaⱼ+aᵢaₖ+aⱼaₖ) claim for n ≥ 3. ✓

### Example 2: Incorrect derivative claim

**Claim:** "Let f(x) = x ln x - x. Then f'(x) = ln x, and since f'(x) < 0 for x < 1, f is decreasing on (0,1)."

**Analysis:** f'(x) = ln x + x·(1/x) - 1 = ln x + 1 - 1 = ln x. This is CORRECT. And ln x < 0 for 0 < x < 1. So the claim is correct. ✓

**Example of incorrect derivative claim:** "Let g(x) = x/(1+x²). Then g'(x) = 1/(1+x²)², and g is increasing." But actually g'(x) = (1+x²-x·2x)/(1+x²)² = (1-x²)/(1+x²)², which is negative for |x| > 1. The claimed formula for g'(x) is wrong, and the monotonicity conclusion is wrong for |x| > 1.

### Example 3: Missing compactness in optimization

**Claim:** "The minimum of f(a,b,c) subject to a+b+c = 1, a,b,c > 0 is attained at a = b = c = 1/3."

**Analysis:** The domain {(a,b,c) : a+b+c=1, a,b,c > 0} is NOT compact (it's open — the corners where some variable = 0 are excluded). However, as any variable approaches 0, f may diverge or approach a boundary value. For this specific claim to be valid, one needs to also check f(a,b,c) → ∞ or ≥ value at (1/3,1/3,1/3) as any variable → 0.

If the proof just claims "the minimum is at a=b=c=1/3 by symmetry and AM-GM" without discussing the boundary behavior, it is missing the existence argument.

### Example 4: Circular reasoning in set characterization

**Claim:** "Since A_i ∪ B_j ⊆ S_{ij} and |A_i∪B_j| ≤ |S_{ij}| = i+j, the only possibility is S_{ij} = A_i∪B_j."

**Analysis:** INCORRECT. The fact that A_i∪B_j ⊆ S_{ij} and |A_i∪B_j| ≤ i+j does not imply equality S_{ij} = A_i∪B_j. What's needed is |A_i∪B_j| = i+j, which would then force A_i∪B_j = S_{ij} (as a subset of S_{ij} with the same cardinality). But |A_i∪B_j| = i+j requires A_i∩B_j = ∅. So this argument is circular if it later derives A_i∩B_j = ∅ from S_{ij} = A_i∪B_j. ✗

### Example 5: Correct handling of the degree-n condition in interpolation

**Claim:** "The solution space of n homogeneous equations in n+1 unknowns has dimension ≥ 1. To ensure a solution with aₙ ≠ 0 exists: if every solution had aₙ = 0, then the solution space would lie in the hyperplane {aₙ = 0}. But the constraint equations are: for each pair {iₖ,jₖ}: Σₘ aₘ(xᵢₖᵐ + xⱼₖᵐ) = 0. The coefficient of aₙ in the k-th equation is xᵢₖⁿ + xⱼₖⁿ. If all these were 0, then xᵢₖⁿ = -xⱼₖⁿ for all k, requiring xᵢₖ = -xⱼₖ (for n odd) or |xᵢₖ| = |xⱼₖ| (for n even). Since our points are arbitrary, this is generically not the case; and even when it happens for some pair, at least one equation has nonzero coefficient of aₙ, giving a solution with aₙ free. In any specific case, one verifies directly."

**Analysis:** This argument correctly handles the degree-n condition, noting that the case xᵢₖⁿ+xⱼₖⁿ=0 for all k corresponds to very special configurations, and in general (or by choosing an appropriate matching) at least one equation has nonzero coefficient of aₙ. ✓

### Example 6: Symmetric sum identity verification

**Claim:** (x-y)²+(y-z)²+(z-x)² = 2(S₁²-3S₂) where S₁ = x+y+z and S₂ = xy+yz+zx.

**Verification:** LHS = (x²-2xy+y²)+(y²-2yz+z²)+(z²-2zx+x²)
= 2(x²+y²+z²) - 2(xy+yz+zx)
= 2(S₁²-2S₂) - 2S₂
= 2S₁²-4S₂-2S₂
= 2S₁²-6S₂
= 2(S₁²-3S₂) ✓

This computation is simple and should not be "skipped" in a proof without verification. A proof that states this identity as "one checks" is acceptable since the calculation is brief. ✓


---

## Appendix A: Extended Examples for Algebra and Analysis Proof Evaluation

### A.1 Inequality Proofs — 20 Scenarios

**Scenario I1 (Correct — AM-GM cascade).** "sum_{i<j} a_i*a_j/(a_i+a_j) <= n/(2s) * sum_{i<j} a_i*a_j."
Proof: Normalize s=1. Then need 2*sum_{i<j} a_i*a_j/(a_i+a_j) <= n*sum_{i<j} a_i*a_j.
Rewrite LHS: 2*sum_{i<j} a_i*a_j/(a_i+a_j) = 2*sum_{i<j} a_i*a_j*(1-sum_{k!=i,j}a_k)/(a_i+a_j) [using s=1]
= 2*sum_{i<j} a_i*a_j/(a_i+a_j) + 2*sum_{i<j} sum_{k!=i,j} a_i*a_j*a_k/(a_i+a_j) [expand: 2*a_i*a_j = 2*a_i*a_j*(a_i+a_j+rest)/(a_i+a_j)]
Actually: a_i+a_j+sum_{k!=i,j}a_k = s = 1, so a_i*a_j = a_i*a_j*(a_i+a_j)/(a_i+a_j) + ...
Better: 2*sum_{i<j} a_i*a_j/(a_i+a_j) = 2*sum_{i<j} a_i*a_j/1 - 2*sum_{i<j} a_i*a_j*(s-(a_i+a_j))/(a_i+a_j)
= 2*sum_{i<j} a_i*a_j - 2*sum_{i<j} sum_{k!=i,j} a_i*a_j*a_k/(a_i+a_j).
RHS n*sum a_i*a_j = 2*sum a_i*a_j + (n-2)*sum a_i*a_j.
So need: 2*sum a_i*a_j*a_k/(a_i+a_j) <= (n-2)/2 * sum a_i*a_j.
Then sum_{i<j} sum_{k!=i,j} = sum_{i<j<k} (sum over 3 pairs) = 3*sum_{i<j<k}.
Key inequality (per triple): a_i*a_j*a_k/(a_i+a_j) + cyclic <= (1/2)*(a_i*a_j+a_i*a_k+a_j*a_k).
By AM-GM: 2*a_i*a_j*a_k/(a_i+a_j) <= a_k*(a_i+a_j)/2. Apply cyclically and add. ✓

**Scenario I2 (Correct — normalization valid).** "Since both sides of the inequality are homogeneous degree 1 in a_1,...,a_n, we may WLOG normalize sum a_i = 1."
CORRECT if both LHS and RHS are degree 1. LHS = sum a_i*a_j/(a_i+a_j): degree 2-1=1. ✓ RHS = n/(2s)*sum a_i*a_j: degree -1+0+2=1. ✓ Normalization is valid. ✓

**Scenario I3 (Incorrect — wrong degree).** "Both sides are degree 2 so normalize a_1+...+a_n=1."
INCORRECT: As verified above, both sides are degree 1, not 2. A degree-2 homogeneous inequality would normalize differently (e.g., sum a_i^2=1 or max a_i=1). Using sum=1 with degree 1 is correct, but the stated "degree 2" is wrong. First material issue: wrong degree claim.

**Scenario I4 (Correct — per-triple AM-GM).** "For any triple (a,b,c): 2abc/(a+b) <= c(a+b)/2."
Proof: From AM-GM: (a+b)^2 >= 4ab, so ab/(a+b) <= (a+b)/4. Multiply by 2c: 2abc/(a+b) <= c(a+b)/2. ✓

**Scenario I5 (Correct — cyclic sum).** "Adding 2abc/(a+b) <= c(a+b)/2 and the two cyclic permutations:
2abc/(a+b)+2abc/(a+c)+2abc/(b+c) <= c(a+b)/2 + b(a+c)/2 + a(b+c)/2."
RHS = (c*a+c*b+b*a+b*c+a*b+a*c)/2 = (2ab+2bc+2ca)/2 = ab+bc+ca.
LHS/2 = abc/(a+b)+abc/(a+c)+abc/(b+c) <= (ab+bc+ca)/2. ✓

**Scenario I6 (Incorrect — wrong cycle).** "Cycle (a,b,c) -> (b,c,a) -> (c,a,b) gives same inequality thrice."
NOT the same inequality: applying to (a,b,c): 2abc/(a+b) term. Applying to (b,c,a): 2bca/(b+c) term. These are DIFFERENT terms. The cyclic sum gives THREE distinct terms, not the same one thrice. Minor error if it leads to correct final sum, major if used as justification for tripling a single term.

**Scenario I7 (Correct — degree bound check).** "For P(t) = a_n*t^n + ..., as y -> infinity with z = (x+y)/(2xy-1) -> 1/(2x):
LHS of (*) = 2(x*P(x) + y*P(y) + z*P(z)) ~ 2*y*a_n*y^n = 2*a_n*y^{n+1}.
RHS of (*) = (x+y+z)*(P(x-y)+P(y-z)+P(z-x)) ~ y*(a_n*(-y)^n + a_n*y^n + O(1)) = a_n*((-1)^n+1)*y^{n+1}."
CORRECT computation. Leading terms match when 2a_n = a_n*((-1)^n+1), i.e., 2 = (-1)^n+1. So (-1)^n = 1, n even. ✓

**Scenario I8 (Incorrect — wrong parity conclusion).** "From 2a_n = a_n*((-1)^n+1): if n is odd, (-1)^n=-1, so (-1)^n+1=0, giving 2a_n=0, so a_n=0. Hence n is ODD."
INCORRECT: n is odd gives a_n=0, contradiction (a_n != 0). So n must be EVEN, not odd. The conclusion "n is odd" is backwards from the correct conclusion "n is even (or a_n=0)."

**Scenario I9 (Correct — coefficient of y^n).** "After establishing n=2 (from y^{n+1} matching), the coefficient of y^n gives 2*a_{n-1} = a_n*(2-n)*(x+1/(2x)) for all x. Since RHS depends on x but LHS doesn't, the coefficient of x and 1/x must vanish. This forces 2-n=0, giving n=2."
CORRECT. The constraint 2a_1 = a_2*(2-n)*(x+1/(2x)) for all x != 0 requires a_2*(2-n) = 0. Since a_2 != 0, 2-n = 0, so n=2. ✓

**Scenario I10 (Correct — full degree bound argument).** The complete argument:
1. P has degree n with leading coefficient a_n != 0.
2. Expand both sides of (*) as y -> infinity, z -> 1/(2x).
3. Coefficient of y^{n+1}: 2a_n = a_n*((-1)^n+1). This requires (-1)^n = 1, so n even.
4. Coefficient of y^n: 2a_{n-1} = a_n*(2-n)*(x+1/(2x)) for all x.
5. RHS depends on x unless a_n*(2-n) = 0. Since a_n != 0, 2-n=0, n=2.
CORRECT and complete. ✓

### A.2 Polynomial Functional Equations — 15 Scenarios

**Scenario P1 (Correct — substitution for degree bound).** "Set y -> infinity, x fixed, z=(x+y)/(2xy-1) -> 1/(2x). Expand both sides of 2(xP(x)+yP(y)+zP(z)) = S_1*(P(x-y)+P(y-z)+P(z-x))."
CORRECT setup. z -> 1/(2x) as y -> infinity (since z=(x+y)/(2xy-1)=(1/y+1)/(2x-1/y) -> 1/(2x)). ✓

**Scenario P2 (Correct — symmetric sum identity).** "(x-y)^2+(y-z)^2+(z-x)^2 = 2(x^2+y^2+z^2) - 2(xy+yz+zx) = 2(S_1^2-3S_2)."
Expand: (x-y)^2+(y-z)^2+(z-x)^2 = 2x^2+2y^2+2z^2-2xy-2yz-2zx = 2(S_1^2-2S_2)-2S_2 = 2S_1^2-6S_2 = 2(S_1^2-3S_2). ✓

**Scenario P3 (Correct — linear term vanishes).** "(x-y)+(y-z)+(z-x) = 0."
Trivially: x-y+y-z+z-x = 0. ✓ So the linear terms of P(x-y)+P(y-z)+P(z-x) always vanish.

**Scenario P4 (Correct — coefficient extraction).** "Setting P(t)=at^2+bt+c, LHS:
2(xP(x)+yP(y)+zP(z)) = 2[a(x^3+y^3+z^3)+b(x^2+y^2+z^2)+c(x+y+z)]
= 2a(S_1^3-3S_1S_2+3S_3)+2b(S_1^2-2S_2)+2cS_1."
CORRECT using standard symmetric sum identities. With S_3=S_1/2:
= 2aS_1^3-6aS_1S_2+3aS_1+2bS_1^2-4bS_2+2cS_1. ✓

**Scenario P5 (Correct — RHS computation).** "RHS = S_1[2a(S_1^2-3S_2)+0+3c] = 2aS_1^3-6aS_1S_2+3cS_1."
Since P(x-y)+P(y-z)+P(z-x) = a*2(S_1^2-3S_2)+b*0+3c = 2a(S_1^2-3S_2)+3c.
Multiply by S_1: 2aS_1^3-6aS_1S_2+3cS_1. ✓

**Scenario P6 (Correct — coefficient matching).** "LHS=RHS:
2aS_1^3-6aS_1S_2+3aS_1+2bS_1^2-4bS_2+2cS_1 = 2aS_1^3-6aS_1S_2+3cS_1.
Cancel 2aS_1^3-6aS_1S_2:
3aS_1+2bS_1^2-4bS_2+2cS_1 = 3cS_1.
Coefficient of S_1^2: 2b=0, so b=0.
Coefficient of S_2: -4b=0. ✓ (consistent)
Coefficient of S_1: 3a+2c=3c, so 3a=c, c=3a."
CORRECT. ✓

**Scenario P7 (Incorrect — wrong identity).** "x^3+y^3+z^3 = (x+y+z)^3 - 3(x+y+z)(xy+yz+zx)."
INCORRECT: x^3+y^3+z^3 = S_1^3-3S_1S_2+3S_3, not S_1^3-3S_1S_2 (missing 3S_3). First material issue.

**Scenario P8 (Correct — verification).** "P(t)=a(t^2+3): verify the original equation.
LHS: P(x)/yz+P(y)/zx+P(z)/xy = a[(x^2+3)/yz+(y^2+3)/zx+(z^2+3)/xy].
Multiply by xyz=S_3=S_1/2: a[x(x^2+3)+y(y^2+3)+z(z^2+3)] = a[x^3+y^3+z^3+3(x+y+z)] = a(S_1^3-3S_1S_2+3S_1/2+3S_1).
RHS: P(x-y)+P(y-z)+P(z-x) = a[(x-y)^2+3+(y-z)^2+3+(z-x)^2+3] = a[2(S_1^2-3S_2)+9].
Multiply by xyz=S_1/2: a*S_1/2*[2(S_1^2-3S_2)+9] = a(S_1^3-3S_1S_2+9S_1/2).
Do these match? LHS gives a(S_1^3-3S_1S_2+3S_1/2+3S_1) = a(S_1^3-3S_1S_2+9S_1/2). ✓"

**Scenario P9 (Correct — degree 0 and 1 solutions).** "P=0 (k=0) is a solution: 0/yz+0/zx+0/xy = 0+0+0. ✓ This corresponds to a=0."
CORRECT. P=0 is the k=0 case of P(t)=k(t^2+3). ✓

### A.3 Optimization and Analysis — 12 Scenarios

**Scenario OA1 (Incorrect — missing existence proof).** "The minimum of f over domain D is attained at the critical point x_0."
MISSING: Must verify D is compact (Weierstrass) or that f is coercive (f -> infinity as |x| -> infinity in D) to guarantee the minimum is attained.

**Scenario OA2 (Correct — compact domain).** "The domain D = {(a,b,c) : a+b+c=1, a,b,c>=0} is compact (closed and bounded in R^3). By Weierstrass, any continuous f attains its minimum on D."
CORRECT. D is the simplex, which is compact. ✓

**Scenario OA3 (Incorrect — wrong critical point).** "Setting f'(x)=0 gives x^2=1, so x=1."
INCORRECT: x^2=1 has two solutions, x=1 and x=-1. Both must be checked to find the minimum. Missing x=-1 is a gap.

**Scenario OA4 (Correct — second derivative test).** "f''(x_0)>0 implies x_0 is a local minimum."
CORRECT. For twice-differentiable f, f''(x_0)>0 implies x_0 is a strict local minimum. ✓

**Scenario OA5 (Incorrect — skipped computation).** "Critical computations are skipped, w.r.t. deriving the minimum value."
This is an example of the first material issue in optimization proofs where critical computations are skipped. The minimum value must be derived explicitly, not just stated. ✓

**Scenario OA6 (Correct — coercivity argument).** "As any variable tends to 0 or infinity with the constraint a+b+c=1, f(a,b,c) tends to +infinity. Therefore the minimum of f is attained in the interior of D."
CORRECT structure. Must verify the claimed coercivity for the specific f in question.

**Scenario OA7 (Correct — compactness argument variant).** "Since f is continuous and D_R = {x in D : f(x) <= R} is compact for any R, the infimum is attained on D_R, hence globally."
CORRECT if D_R is indeed compact for some R (compact sublevel sets). This is equivalent to coercivity.

**Scenario OA8 (Incorrect — non-compact domain used as compact).** "The set {(x,y) : x>=0, y>=0, xy=1} is compact."
INCORRECT: this hyperbola is closed and unbounded, hence not compact. Claiming it's compact is the first material issue.

**Scenario OA9 (Correct — finiteness of infimum).** "Since f(x,y) >= 0 for x,y in D (trivially, as f is a sum of squares), the infimum is >= 0. Since f(0,0)=0, the infimum is 0 and is attained."
CORRECT. Infimum >= 0 (bounded below) + attained at (0,0) = minimum = 0. ✓

**Scenario OA10 (Incorrect — wrong argument regarding minima).** "The arguments regarding finiteness of minima are incorrect." (a common first material issue in analysis proofs involving incorrect compactness reasoning)
This is a description of a first material issue: a proof that claims certain minima are finite using incorrect compactness reasoning would fail here.

### A.4 Polynomial Interpolation — 8 Scenarios

**Scenario PI1 (Correct — dimension count).** "n homogeneous equations in n+1 unknowns (a_0,...,a_n) have a nonzero solution by rank-nullity."
CORRECT: rank of n x (n+1) system is at most n, so null space has dimension >= 1, giving a nonzero solution. ✓

**Scenario PI2 (Correct — degree exactly n).** "To find solution with a_n != 0: if all solutions had a_n=0, the constraint vectors would all be orthogonal to e_{n+1}. This would mean x_{i_k}^n + x_{j_k}^n = 0 for all k, forcing |x_{i_k}| = |x_{j_k}| for n even, or x_{i_k} = -x_{j_k} for n odd. In general position this fails, so a solution with a_n != 0 exists."
CORRECT in general. ✓

**Scenario PI3 (Correct — multiset equality check).** "With Q(x_{i_k})+Q(x_{j_k})=0: P(x_{i_k}) = -Q(x_{i_k}) = Q(x_{j_k}) and P(x_{j_k}) = -Q(x_{j_k}) = Q(x_{i_k}). So {P(x_i)} = {Q(x_i)} as multisets."
For each pair {i_k,j_k}: P takes values -Q(x_{i_k}) and -Q(x_{j_k}) = Q(x_{i_k}) and Q(x_{j_k}) respectively... wait.
P(x_{i_k}) = -Q(x_{i_k}) = Q(x_{j_k}) (using Q(x_{i_k})+Q(x_{j_k})=0).
P(x_{j_k}) = -Q(x_{j_k}) = Q(x_{i_k}).
So: {P(x_{i_k}), P(x_{j_k})} = {Q(x_{j_k}), Q(x_{i_k})} = {Q(x_{i_k}), Q(x_{j_k})}. ✓
Summing over all k: {P(x_i) : i} = {Q(x_i) : i} as multisets. ✓

**Scenario PI4 (Correct — perfect matching existence).** "A perfect matching on 2n points always exists (pair them arbitrarily in n pairs)."
CORRECT. For {1,...,2n}, pair (1,2), (3,4), ..., (2n-1,2n). This is an explicit construction. ✓

**Scenario PI5 (Incorrect — matching affects degree).** "The matching choice affects whether degree-n solutions exist."
PARTIALLY CORRECT: The matching does affect which specific Q exists with degree exactly n. If ALL matchings lead to all solutions having a_n=0 (impossible generically), this would be an issue. In practice, for generic points, some matching always allows a_n-nonzero solution.

**Scenario PI6 (Correct — conclusion for magician).** "Since P != Q are both degree-n polynomials with the same sorted list of values at x_1,...,x_{2n}, the magician cannot uniquely identify the secret polynomial from the sorted list. Hence the trick is impossible."
CORRECT conclusion structure. ✓

---

## Appendix B: Functional Analysis and Real Analysis Reference

### B.1 Continuous Functions on Metric Spaces

A function f: X -> R is continuous at x_0 if for all epsilon>0 there exists delta>0 such that d(x,x_0)<delta implies |f(x)-f(x_0)|<epsilon.

**Uniform continuity:** f is uniformly continuous if the delta depends only on epsilon, not on x_0.

**Lipschitz condition:** |f(x)-f(y)| <= L*d(x,y) for all x,y implies uniform continuity.

### B.2 Differentiation and Taylor's Theorem

For f differentiable n times at a: f(x) = sum_{k=0}^n f^{(k)}(a)/k! * (x-a)^k + R_n(x) where R_n(x) = o((x-a)^n).

**L'Hopital's rule:** If lim_{x->a} f(x) = lim_{x->a} g(x) = 0 or +/-infinity, and g'(x)!=0 near a, then lim f(x)/g(x) = lim f'(x)/g'(x) if the latter limit exists.

### B.3 Integration Techniques

**Integration by parts:** integral u dv = uv - integral v du.

**Substitution:** integral f(g(x))g'(x)dx = integral f(u)du [u=g(x)].

**Partial fractions:** For rational P(x)/Q(x) with deg P < deg Q: decompose Q(x) into prime factors, then write P/Q as sum of terms A/(x-a)^k.

### B.4 Sequences and Series

**Cauchy sequence:** |x_m - x_n| -> 0 as m,n -> infinity. Converges in complete spaces (R, C).

**Root test:** lim sup |a_n|^{1/n} < 1 implies sum a_n converges absolutely.

**Ratio test:** lim |a_{n+1}/a_n| < 1 implies sum a_n converges absolutely.

**Power series:** sum a_n*(x-a)^n converges for |x-a| < R (radius of convergence R = 1/lim sup |a_n|^{1/n}).

---

## Appendix C: Olympiad-Level Calculus and Analysis Patterns

### C.1 Using Monotonicity to Prove Inequalities

Technique: To prove f(x) >= 0, show f(x_0)=0 at some x_0 and f is increasing on [x_0, inf) and decreasing on (-inf, x_0]. This requires computing f'.

**Evaluation criterion for derivative claims:**
If f'(x) < 0 is asserted without computation or verification, this is a gap. If f'(x) is computed but the inequality f'(x)<0 fails for some x in the domain, this is the first material issue.

Example: f(x) = x^3 - 3x on [-2,2]. f'(x) = 3x^2-3 = 3(x^2-1). f'(x)<0 iff x^2<1 iff |x|<1. So f is DECREASING on (-1,1) and INCREASING on (1,2) and (-2,-1). A proof claiming "f'(x)<0 for all x in [-2,2]" is INCORRECT at x=2 where f'(2)=9>0.

### C.2 Convexity and Jensen Applications

Jensen's inequality (convex phi): phi(E[X]) <= E[phi(X)] for random variable X.
For finite: phi((x_1+...+x_n)/n) <= (phi(x_1)+...+phi(x_n))/n.

**Standard convex functions:** x^2, e^x, x*log(x) (for x>0), 1/x (for x>0).
**Standard concave functions:** log(x), sqrt(x), x^{1/p} (for p>1, x>0).

**Olympiad applications:** To prove sum phi(a_i) >= n*phi(mean): use Jensen with concavity (or opposite direction with convexity).

### C.3 Key Metric Space Results

**Banach fixed point theorem:** If T: X->X is a contraction (d(Tx,Ty)<=L*d(x,y) with L<1) on complete metric space X, then T has a unique fixed point.

**Brouwer fixed point theorem:** Every continuous f: D^n -> D^n (closed ball to itself) has a fixed point.

**Application to existence:** Many optimization problems can be reformulated as fixed point problems, establishing existence of solutions.
