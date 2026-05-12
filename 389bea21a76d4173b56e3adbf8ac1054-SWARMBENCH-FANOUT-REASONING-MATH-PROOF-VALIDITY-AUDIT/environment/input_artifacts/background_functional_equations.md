# Domain Background: Functional Equations Proof Evaluation

This reference covers the mathematical theory, common proof techniques, and evaluation criteria relevant to olympiad functional equation problems. Sub-agents auditing **proof_07** and **proof_11** should read this document before evaluating their assigned proof.

---

## Part I: Functional Equations Fundamentals

### 1.1 What is a Functional Equation?

A functional equation is an equation involving an unknown function f, where the unknowns are the values of f at various points. The task is typically to find all functions satisfying the equation, not just one.

**Standard notation:** P(x,y) denotes the assertion obtained by substituting (x,y) into the functional equation. E.g., if the equation is f(x+y) = f(x)+f(y), then P(0,0) means f(0) = f(0)+f(0), giving f(0) = 0.

### 1.2 Cauchy's Functional Equation

f(x+y) = f(x)+f(y) for all x,y ∈ ℝ. Solutions:
- If no regularity is assumed: any additive function (including non-measurable ones via AC)
- If f is monotone, or continuous, or bounded on an interval: f(x) = cx for some c ∈ ℝ

**Generalizations:**
- f(xy) = f(x)+f(y) (logarithmic): f(x) = c·log(x) for x > 0 under regularity
- f(xy) = f(x)f(y) (multiplicative): f(x) = x^c or f = 0 under regularity
- f(x+y) = f(x)f(y) (exponential): f(x) = e^{cx} or f = 0

### 1.3 Floor Function (Greatest Integer Function)

⌊x⌋ = greatest integer ≤ x. Properties:
- ⌊x+n⌋ = ⌊x⌋+n for n ∈ ℤ
- ⌊⌊x⌋y⌋ = ⌊xy⌋ when... not always; this requires care
- For x ∈ [k, k+1): ⌊x⌋ = k
- ⌊kx⌋ for integer k: depends on fractional part of x

### 1.4 The Functional Equation f(⌊x⌋y) = f(x)⌊f(y)⌋

The constraint is: for all real x, y, the value f at ⌊x⌋y equals f(x) times ⌊f(y)⌋.

**Key observations from substitutions:**
- P(x, y) with ⌊x⌋ = 1 (i.e., x ∈ [1,2)): f(y) = f(x)⌊f(y)⌋, so f(y) = λ·⌊f(y)⌋ where λ = f(x) for any x ∈ [1,2). This forces f(x) to be constant on [1,2).
- P(0, y): f(0) = f(0)·⌊f(y)⌋. If f(0) ≠ 0, then ⌊f(y)⌋ = 1 for all y.
- P(x, 0): f(0) = f(x)·⌊f(0)⌋.

**Structural implication:** The equation f(⌊x⌋y) = f(x)⌊f(y)⌋ with ⌊x⌋ = m (integer) says f(my) = f(x)⌊f(y)⌋ for all x with ⌊x⌋ = m. The right side is constant as x varies in [m, m+1), so f(my) is determined by m and y. This forces f to be constant on each interval [k, k+1) for k ∈ ℤ.

### 1.5 Proving Constancy on Integer Intervals

**Lemma:** Under the equation f(⌊x⌋y) = f(x)⌊f(y)⌋, if ⌊f(y₀)⌋ ≠ 0 for some y₀, then f is constant on each interval [k, k+1).

**Proof:** Fix y = y₀. The equation gives f(⌊x⌋·y₀) = f(x)·c where c = ⌊f(y₀)⌋ ≠ 0. For fixed ⌊x⌋ = k, f(k·y₀) is a specific value (fixed), so f(x) = f(k·y₀)/c is constant for all x ∈ [k, k+1). □

This argument is valid and complete. The conclusion that f(x) = A_{⌊x⌋} (a function of the floor of x) follows directly.

---

## Part II: Case Analysis in Functional Equation Proofs

### 2.1 Complete Case Enumeration

When solving f: ℝ → ℝ satisfying a functional equation, typical cases are:
1. f ≡ 0 (trivial solution)
2. f ≡ constant c for specific c
3. f = cx or f = x^c for other functional forms
4. Non-measurable/pathological solutions (usually excluded by olympiad conventions)

A complete solution must:
- Show these are the ONLY solutions (completeness)
- Show each IS a solution (verification)

**Evaluation criterion:** If a proof lists candidate solutions and verifies each, but does not show they are the ONLY solutions, the proof is incomplete. Conversely, if the proof shows "f must be one of these forms" but doesn't verify each form works, it is also incomplete.

### 2.2 Case A₀ ≠ 0 vs A₀ = 0

In the floor-function equation, A₀ = f(0) is a key parameter:
- A₀ ≠ 0: forces B_n = ⌊A_n⌋ = 1 for all n (all values in [1,2)), forcing f ≡ constant in [1,2)
- A₀ = 0: requires separate analysis

**Sub-case A₀ = 0, A₁ ≠ 0:**
From equation (*): A_n = A₁·B_n for all n. For n=1: A₁ = A₁·B₁, giving B₁ = 1, so A₁ ∈ [1,2). Then use P(2,0) with y ∈ [0,1) to get A_{⌊2y⌋} = A₂·B₀ = A₂·⌊A₀⌋ = A₂·0 = 0. For y ∈ [1/2,1): ⌊2y⌋ = 1, so A₁ = 0. Contradiction with A₁ ∈ [1,2). Hence this sub-case is impossible. □

**Evaluation criterion for this case:** The specific substitution (m=2, n=0) and the case ⌊2y⌋=1 for y ∈ [1/2,1) must be correctly used. The conclusion A₁ = 0 contradicting A₁ ≥ 1 is the crux.

### 2.3 Extracting Consequences from the Functional Equation

**General principle:** For a functional equation f(f(x)) = g(x) or similar, plug in special values:
- x = y = 0: eliminates variables, gives relations on f(0)
- y = 0: gives f(0) = f(x)·f(0), determining f(0) possibilities
- x = y: gives f(2x) in terms of f(x)
- y = x inverse: useful if the equation has a multiplicative structure

**Key technique:** Use the functional equation to reduce the unknown to finitely many parameters (e.g., f(0), f(1)) and then determine those parameters.

---

## Part III: Well-Posedness and Completeness

### 3.1 What "All Solutions" Means

For an olympiad functional equation, the task is to classify ALL functions satisfying the equation. The answer typically takes the form: "The solutions are exactly f(x) = ..., characterized by [condition]."

**A complete classification proof has:**
1. **Necessity:** Every solution is of the stated form (prove "if f is a solution then f = ...")
2. **Sufficiency:** Every function of the stated form is a solution (verify "if f = ... then f satisfies the equation")

### 3.2 Verification of Proposed Solutions

After finding the form of the solutions, each must be verified:
- For f ≡ 0: plug into LHS = f(⌊x⌋y) = f(whatever) = 0, RHS = f(x)⌊f(y)⌋ = 0·⌊0⌋ = 0·0 = 0. ✓
- For f ≡ C ∈ [1,2): LHS = C, RHS = C·⌊C⌋ = C·1 = C. ✓

**Evaluation criterion:** If the proof claims "one checks that f ≡ 0 and f ≡ C (C ∈ [1,2)) are solutions" without the verification, this is a minor omission — the verification is routine. However, if it claims non-obvious families are solutions without verifying, this is a gap.

### 3.3 Common Errors in Functional Equation Proofs

**Error 1: Not accounting for all cases.** Missing a sub-case (e.g., not handling A₁ = 0 within the A₀ = 0 branch) leads to incomplete classification.

**Error 2: Confusing necessary and sufficient conditions.** Deriving "f must satisfy property P" (necessary) does not mean "all f satisfying P are solutions" (sufficient). Both directions must be shown.

**Error 3: Substituting y for ⌊x⌋ incorrectly.** The variable ⌊x⌋ in f(⌊x⌋y) means f evaluated at the product of ⌊x⌋ (an integer) and y (any real). Not the same as f evaluated at ⌊xy⌋.

**Error 4: Domain errors.** The equation holds for all x,y ∈ ℝ. Using it only for positive integers loses information. Using it for x ∈ [1,2) (so ⌊x⌋=1) gives f(y) = f(x)⌊f(y)⌋, which must hold for ALL y, not just specific values.

### 3.4 Skipped Steps in Functional Equation Proofs

A proof of a functional equation that says "key steps are skipped" or "the argument follows by similar reasoning" without completing those steps is incomplete. The "key steps" in functional equation proofs are precisely those that:
- Eliminate impossible branches
- Determine the form of f in each branch
- Verify the proposed solutions

**Evaluation criterion for skipped-step proofs:** If a proof outline correctly identifies the approach (e.g., "consider cases based on whether f(0) = 0") but then says "the details follow" without providing them, the proof is incomplete. The verdict depends on whether the skipped details are truly routine (minor omission) or essential (critical gap).

**Key distinction:**
- Minor omission: "One checks f ≡ C satisfies the equation" (trivial verification)
- Critical gap: "One checks that the remaining sub-cases are impossible" (non-trivial, because it requires the P(2,0) argument or equivalent)

---

## Part IV: Abstract Algebraic Context

### 4.1 Groups and Homomorphisms

A group (G, ·) is a set with a binary operation satisfying: associativity, identity element e, and inverses. A **homomorphism** φ: G → H satisfies φ(ab) = φ(a)φ(b). The kernel ker(φ) = {g : φ(g) = e_H} is a normal subgroup.

### 4.2 Multiplicative Functions on ℤ/mℤ

Functions f: ℤ/mℤ → ℤ/mℤ satisfying f(ab) = f(a)f(b) are **ring homomorphisms** or **multiplicative functions** modulo m. Classification: depends on the structure of (ℤ/mℤ)*.

### 4.3 Functional Equations from Number Theory

Many number-theoretic functions satisfy functional equations:
- φ(mn) = φ(m)φ(n) for gcd(m,n) = 1 (Euler's totient is multiplicative)
- τ(mn) = τ(m)τ(n) for gcd(m,n) = 1 (number of divisors is multiplicative)
- The zeta function ζ(s) = Σn^{-s} satisfies Euler product formula

---

## Part V: Evaluation Rubric for Functional Equation Proofs

### For floor-function type (proof_07 type):

**Must verify:**
1. Case ⌊f(y)⌋ = 0 for all y → f ≡ 0 ✓ (use ⌊x⌋=1 to get f(y)=0)
2. Case ∃y₀ with ⌊f(y₀)⌋ ≠ 0 → f constant on [k,k+1) ✓ (see Lemma 1.5)
3. A₀ ≠ 0 branch → B_n=1 for all n → A_n=A₁ for all n → f≡C∈[1,2) ✓
4. A₀=0, A₁≠0 branch → contradiction via P(2,0) ✓
5. A₀=0, A₁=0 branch → A_n=A₁B_n=0 for all n → f≡0 ✓
6. Verification: f≡0 works ✓; f≡C (C∈[1,2)) works ✓

A proof that correctly executes all 6 steps is CORRECT. A proof that correctly handles steps 1-5 but fails at step 6 (doesn't verify) has a minor omission. A proof that skips any of steps 1-5 has a critical gap.

### For skipped-steps type (proof_11 type):

**Evaluate each identified "key step" in the proof:**
1. Does the proof identify the correct overall strategy?
2. For each "key step" that is claimed but not proved: is this step truly routine, or is it the critical part of the argument?
3. If multiple critical steps are simultaneously skipped, the first one is the first material issue.

**Common critical steps in abstract proofs:**
- Establishing a lemma that the whole proof depends on
- Showing a particular map is well-defined
- Showing a particular set is non-empty
- Verifying a chain of inequalities

If ALL such steps are labeled "left to the reader" or "similar to above," the proof is incomplete regardless of whether the strategy is correct.

---

## Part VI: Extended Examples

### Example 1: Complete case analysis in P(x,y) style

**Equation:** f(⌊x⌋y) = f(x)⌊f(y)⌋.

**Step 1:** P(x,y) with x ∈ [0,1): ⌊x⌋ = 0, so f(0) = f(x)·⌊f(y)⌋ for all y. If f(x) ≠ 0 for some x₀ ∈ [0,1), then ⌊f(y)⌋ = f(0)/f(x₀) = constant for all y. But ⌊f(y)⌋ is integer-valued, so this constant must be an integer. Call it B = f(0)/f(x₀). Then f(0) = B·f(x) for all x ∈ [0,1). If B ≠ 0, then f(x₀) = f(0)/B = constant for all x₀ ∈ [0,1). So f is constant on [0,1).

**Step 2:** P(x,y) with x ∈ [1,2): ⌊x⌋ = 1, so f(y) = f(x)·⌊f(y)⌋. This means f(y) = A₁·⌊f(y)⌋ where A₁ = f(x) for any x ∈ [1,2). (This is the constant from Step 1's argument applied to [1,2).) Note that ⌊f(y)⌋ is integer-valued. For f(y) = A₁·⌊f(y)⌋ to be consistent for all y, we need: ⌊A₁·⌊f(y)⌋⌋ = ⌊f(y)⌋ (taking floors of both sides). This requires A₁·n to have floor n for all integers n that appear as ⌊f(y)⌋. The condition ⌊A₁n⌋ = n for all relevant integers n requires A₁ ∈ [1/n · n, (n+1)/n) = [1, (n+1)/n), tightening to A₁ ∈ [1,2) for the condition to hold for n = 1.

**Observation:** The derivation that f is constant on [k,k+1) is correct, as shown by Lemma 1.5 above. This is a CORRECT step in a complete proof.

### Example 2: The sub-case A₀=0, A₁≠0 leads to contradiction

**Setup:** A₀ = f(0) = 0, A₁ = f(x) for x ∈ [1,2), A₁ ≠ 0.

**From A_n = A₁·B_n (equation (*) with m=1):** For n=1: A₁ = A₁·B₁, so B₁ = 1 (since A₁ ≠ 0). Hence A₁ ∈ [1,2).

**Use m=2, n=0:** For any y ∈ [0,1), ⌊2y⌋ ∈ {0,1}. Taking y ∈ [1/2,1): ⌊2y⌋ = 1, so equation (*) gives A₁ = A_{⌊2y⌋} = A₂·B₀ = A₂·⌊A₀⌋ = A₂·⌊0⌋ = A₂·0 = 0.

This contradicts A₁ ≥ 1 (since A₁ ∈ [1,2)). Hence the sub-case A₁ ≠ 0 within A₀ = 0 is impossible. ✓

This is a CORRECT and complete argument. A proof that contains exactly this reasoning is correctly completing the case analysis.

### Example 3: Proof with skipped steps

**Outline:** "We first show f is constant on each half-open interval [k,k+1). [Key step 1: not shown.] Then we analyze whether ⌊f(y)⌋ = 0 for all y or not. [Key step 2: partially shown.] In Case 1, all values are 0. [Step 3: shown.] In Case 2, f must be a constant in [1,2). [Key step 4: not shown, just asserted.] We omit the verification."

**Assessment:** This proof has key steps 1, 4 critical and unproven. Step 1 (constancy on intervals) is the foundation of the whole argument and is non-trivial (requires the Lemma argument). Step 4 (conclusion f is a constant in [1,2)) requires both the Subcase 2.1 argument and the Subcase 2.2 impossibility argument — both non-trivial. The verdict is INCORRECT with first material issue being the first skipped critical step.

### Example 4: Verification that f≡C (C∈[1,2)) satisfies the equation

**Check:** f(⌊x⌋y) = C and f(x)⌊f(y)⌋ = C·⌊C⌋. Since 1≤C<2, ⌊C⌋=1. So f(x)⌊f(y)⌋ = C·1 = C. ✓ The verification is one line.

### Example 5: What constitutes a "key step" in functional equation proofs

**Critical steps** (cannot be skipped without making the proof incomplete):
- Showing f is constant on each interval [k,k+1) [requires Lemma 1.5]
- Showing the A₀=0, A₁≠0 case is impossible [requires P(2,0) argument]
- Showing A_n = A₁·B_n for all n [requires m=1 substitution]
- Deriving B_n = 1 for all n when A₀ ≠ 0 [requires m=0 substitution]

**Minor omissions** (can be stated without proof in competition context):
- Verification that f≡0 satisfies the equation [one line]
- Verification that f≡C (C∈[1,2)) satisfies the equation [one line]
- "By induction on |T|, f(T) = Π λᵢ" [standard induction, stated without proof]


---

## Appendix A: Extended Functional Equation Proof Evaluation

### A.1 Floor Function Problems — 15 Scenarios

**Scenario FL1 (Correct — establishing f constant on intervals).** "For any y_0 with floor(f(y_0))=c!=0: applying P(x,y_0) gives f(floor(x)*y_0) = f(x)*c. For floor(x)=k: f(k*y_0) is constant (independent of x in [k,k+1)), so f(x) = f(k*y_0)/c is constant on [k,k+1)."
CORRECT. This is the key step establishing f(x)=A_{floor(x)}. ✓

**Scenario FL2 (Correct — case floor(f(y))=0 for all y).** "If floor(f(y))=0 for all y: P(x,y) gives f(floor(x)*y) = f(x)*0 = 0. Every real t = 1*t (with floor(1)=1), so f(t)=0 for all t."
CORRECT. For any t, take x=1 (floor(x)=1) and y=t: f(1*t)=f(1)*floor(f(t))=f(1)*0=0. ✓

**Scenario FL3 (Correct — A_0=0 forces B_0=0).** "A_0=f(0)=0, so floor(A_0)=floor(0)=B_0=0."
CORRECT. B_n = floor(A_n) = floor(f(x)) for x in [n,n+1). For n=0: B_0=floor(A_0)=floor(0)=0. ✓

**Scenario FL4 (Correct — A_0!=0 forces all B_n=1).** "Taking m=0 in A_{floor(m*y)} = A_m*B_n: A_0 = A_0*B_n for all n. Since A_0!=0: B_n=1 for all n."
CORRECT. floor(0*y)=floor(0)=0, so A_0 = A_0*B_n. Divide by A_0!=0: B_n=1. ✓

**Scenario FL5 (Correct — B_n=1 forces A_n in [1,2)).** "B_n=1 means floor(A_n)=1, i.e., A_n in [1,2)."
CORRECT. floor(x)=1 iff 1<=x<2. ✓

**Scenario FL6 (Correct — A_n=A_1 for all n).** "Taking m=1 in (*): A_{floor(y)}=A_1*B_n for y in [n,n+1). But floor(y)=n, so A_n=A_1*B_n. With B_n=1: A_n=A_1 for all n."
CORRECT. So f is constant: f(x)=A_1 in [1,2). ✓

**Scenario FL7 (Correct — f constant in [1,2) solutions).** "f(x) equiv C with C in [1,2) works: LHS = f(floor(x)*y) = C, RHS = f(x)*floor(f(y)) = C*1 = C. ✓"

**Scenario FL8 (Correct — A_0=0, A_1=0 case).** "If A_0=0 and A_1=0: from A_n=A_1*B_n=0 for all n. So f equiv 0."
CORRECT. ✓

**Scenario FL9 (Correct — A_0=0, A_1!=0 contradiction).** "If A_0=0, A_1!=0: then A_1 in [1,2) (from A_1=A_1*B_1 => B_1=1). Take m=2, y in [0,1), specifically y in [1/2,1). Then floor(2y)=1. From (*): A_1 = A_2*B_0 = A_2*0 = 0. Contradiction with A_1 >= 1."
CORRECT. This is the key argument. ✓

**Scenario FL10 (Correct — complete solution list).** "The complete set of solutions: f equiv 0 and f equiv C for C in [1,2)."
CORRECT. These are exactly the two types found. ✓

**Scenario FL11 (Incorrect — missing case).** "The only solution is f equiv 0."
INCORRECT. The constant solutions f equiv C for C in [1,2) are also valid. First material issue: claiming f=0 is the only solution without checking constant solutions.

**Scenario FL12 (Incorrect — wrong domain for C).** "f equiv C for any C > 0 is a solution."
INCORRECT. For C >= 2: floor(C)=2, so f(x)*floor(f(y))=C*2=2C, but f(floor(x)*y)=C. So 2C=C only if C=0. Contradiction. C must be in [1,2). First material issue: wrong domain claim.

**Scenario FL13 (Correct — negative constant).** "f equiv C for C in (-1,0): floor(C)=-1. Then f(x)*floor(f(y))=C*(-1)=-C. But f(floor(x)*y)=C. So C=-C, giving C=0. Contradiction. C=0 doesn't give f in (-1,0)."
CORRECT analysis showing C not in (-1,0). ✓

**Scenario FL14 (Correct — C=0).** "f equiv 0: floor(0)=0. f(floor(x)*y)=0=0*0=f(x)*floor(f(y)). ✓"
CORRECT. f=0 is the f(empty)=0 with no blue sets case. ✓

**Scenario FL15 (Incorrect — using wrong substitution).** "Substituting x=y=0: f(floor(0)*0) = f(0)*floor(f(0)), i.e., f(0) = f(0)*floor(f(0))."
Actually CORRECT substitution: floor(0)=0, 0*0=0, so f(0)=f(0)*floor(f(0)). This gives A_0=A_0*B_0. ✓

### A.2 Abstract Functional Equation Proofs — 12 Scenarios

**Scenario AF1 (Critical gap — key steps skipped).** "The proof identifies the correct structure but leaves multiple key steps as 'similar to the above' or 'left to the reader' without providing them."
Evaluation: Depends on which steps are skipped. If the skipped steps are:
- Routine: verification that proposed solutions work (one line each) -> minor omission
- Critical: establishing constancy on intervals, or the A_0=0,A_1!=0 contradiction -> critical gap
First material issue: the FIRST skipped critical step.

**Scenario AF2 (Correct — explicit step-by-step proof).** A proof that explicitly:
1. Handles case floor(f(y))=0 for all y
2. Establishes f constant on integer intervals  
3. Uses m=0 to get A_0=A_0*B_n
4. Case-splits A_0!=0 and A_0=0
5. In A_0!=0: gets B_n=1, A_n=A_1, f=C in [1,2)
6. In A_0=0,A_1!=0: gets contradiction from m=2
7. In A_0=0,A_1=0: gets f=0
8. Verifies both solution types
This is CORRECT and complete. ✓

**Scenario AF3 (Incorrect — claiming more solutions exist).** "The solutions are f equiv C for any constant C." 
INCORRECT: Only C=0 or C in [1,2) works (as shown above). C not in {0} cup [1,2) fails. First material issue: wrong solution set.

**Scenario AF4 (Correct — "key steps skipped" verdict).** A proof that sketches the correct strategy but leaves the critical technical steps unproven should be marked INCORRECT. Simply outlining an approach without supplying the essential steps is an incomplete proof, and incompleteness at critical points constitutes a material gap.

**Scenario AF5 (Correct — what counts as "key step").** In functional equation proofs, "key steps" (the critical non-skippable parts) include:
- Any step that changes the problem's structure substantially
- Deriving constancy of f on intervals (from the floor function)
- The contradiction argument for impossible sub-cases
- The verification that proposed solutions actually work

Minor steps that can be cited without proof:
- "floor(n)=n for integer n"
- "A_n = A_{floor(x)} for x in [n,n+1)"
- Basic arithmetic

---

## Appendix B: Functional Equations Reference

### B.1 Characterization Theorems

**Cauchy's functional equation solutions (assuming measurability or monotonicity):**
- f(x+y)=f(x)+f(y): f(x)=cx
- f(xy)=f(x)+f(y) (x,y>0): f(x)=c*log(x)
- f(xy)=f(x)*f(y) (all x): f=0 or f(x)=|x|^c*sgn(x)^k

**Key regularity conditions:** Without measurability or monotonicity, pathological solutions (not expressible in closed form) exist. Competition problems implicitly assume "nice" functions (measurable, or at least determined by their values at a dense set).

### B.2 Symmetry Arguments

If f satisfies F(x,y)=0 and F is symmetric in x,y, then F(y,x)=0. This gives: F(x,y)-F(y,x)=0, which can be used to derive additional relations.

**Anti-symmetry:** If F(x,y) = -F(y,x), then F(x,x)=0 gives information about f at f(x)=f(x) relations.

### B.3 Floor Function Properties Recap

For real x: floor(x) = greatest integer <= x.
- floor(x+n) = floor(x)+n for integer n
- floor(x) <= x < floor(x)+1
- floor(x) = n iff n <= x < n+1
- floor(n) = n for integer n
- floor(floor(x)) = floor(x)

For the equation f(floor(x)*y) = f(x)*floor(f(y)):
- Setting x in [k,k+1): floor(x)=k. Equation becomes f(k*y)=f(x)*floor(f(y)).
- RHS is constant for fixed y and varying x in [k,k+1) only if f is constant on [k,k+1) or floor(f(y))=0.
- This forces either floor(f(y))=0 for all y (Case 1), or f constant on intervals (Case 2).
