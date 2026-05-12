# Oracle Derivation — Olympiad Proof Validity Audit

Source: INSAIT-Institute/OPC (Open Proof Corpus)  
Task: Audit 20 real olympiad proof attempts for mathematical correctness. If incorrect, identify the earliest material flaw in one short sentence.

---

## Per-Proof Derivations

### proof_01 — BMOSL_2016_18 — **correct**
The proof correctly identifies and handles all cases for monic polynomials f∈Z[x] such that p|2(f(p))!+1 for all large primes p. Step 1 eliminates d≥2 by noting f(p)≥p for large p, so p|f(p)! and 2(f(p))!+1≡1 (mod p). Step 2 eliminates d=0: monic degree-0 forces f≡1, giving 2·1!+1=3, so only finitely many primes divide 3. Step 3 handles the linear case f(x)=x+b: applies Wilson's theorem as (p-1)!≡(-1)^r·r!·(p-r)! (mod p), derives the fixed integer D_r=2(-1)^(r+1)+r! must be zero for all large p, then verifies r=3 gives (r-1)!+2(-1)^r=2!-2=0. Step 4 verifies f(x)=x-3 directly: 2(p-3)!≡-1 (mod p) follows from (p-1)!=(-1)(-2)(p-3)!≡2(p-3)! (mod p) and Wilson. All steps are complete and correct. Verdict: **correct**, `first_material_issue_summary`: none.

### proof_02 — BMOSL_2018_15 — **incorrect**
The proof attempts an angle-chase but introduces incorrect angular equalities at multiple steps. The very first directed-angle equality claimed does not follow from the stated concyclicity, and subsequent steps compound this error throughout. Verdict: **incorrect**, first material issue: "The solution is an attempt for angle-chase where there is a mistake in almost every line."

### proof_03 — IMOSL_2006_28 — **correct**
The proof correctly proves the inequality sum_{i<j} a_i a_j/(a_i+a_j) ≤ n/(2s)·sum_{i<j} a_i a_j. It first normalizes to s=a_1+...+a_n=1 using homogeneity (both sides are degree 1), reducing the target to 2·sum_{i<j} a_i a_j/(a_i+a_j) ≤ n·sum_{i<j} a_i a_j. After algebraic cancellation, the inequality reduces to showing for each triple (a_i, a_j, a_k): a_i a_j a_k/(a_i+a_j)+a_i a_j a_k/(a_i+a_k)+a_i a_j a_k/(a_j+a_k) ≤ (1/2)(a_i a_j+a_i a_k+a_j a_k). The key lemma is xy/(x+y)≤(x+y)/4 from AM-GM ((x+y)²≥4xy), giving 2xyz/(x+y)≤z(x+y)/2. Applying this cyclically to (x,y,z)=(a_i,a_j,a_k), (a_j,a_k,a_i), (a_k,a_i,a_j) and adding yields 2·(LHS triple) ≤ (1/2)[(a_i+a_j)a_k+(a_i+a_k)a_j+(a_j+a_k)a_i]=a_i a_j+a_i a_k+a_j a_k, so dividing by 2 gives the required bound. No critical gaps. Verdict: **correct**, `first_material_issue_summary`: none.

### proof_04 — BMOSL_2020_13 — **correct**
The proof gives a complete coordinate proof of concurrence of ZE, CO, FM. It places A=(0,0), B=(1,0), C=(√2/2, √2/2) for the 45° isosceles triangle, computes circumcenter O=(1/2,(√2-1)/2) by intersecting perpendicular bisectors, and finds F=(( √2-1)/2,(√2-1)/2) by intersecting the small circle (center C, radius CD=√2/2) with line AC (y=x). For points E,Z on both circles, subtracting the two circle equations yields the line L: y=1/2-(√2-1)x. The intersection P of L with line CO (slope √2+1, equation y=(√2+1)x-1) is computed as P=(3√2/8,(3√2-2)/8). Finally the slopes of FP and FM are independently computed as (2-√2)/(4-√2), establishing F,M,P collinear. All numeric computations are carried through explicitly. Verdict: **correct**, `first_material_issue_summary`: none.

### proof_05 — USAMO_2013_4 — **incorrect**
The solution claims that a certain derivative is strictly negative in order to establish monotonicity, but this inequality is stated without proof and is in fact false for the function involved. This is the first material error; all subsequent monotonicity conclusions are unsupported. Verdict: **incorrect**, first material issue: "The inequality about the derivative being less than zero is wrong."

### proof_06 — USAMO_2015_5 — **incorrect**
The solution attempts to prove no quintuple of distinct positive integers satisfies a⁴+b⁴=c⁴+d⁴=e⁵, concluding the result is "vacuously true." In Step 2, the proof claims: "the assignment of which of the two irreducible factors (u+vi)^5, (u-vi)^5 goes to (a²+ib²) and which goes to (c²+id²) must swap them. But a direct check of signs then forces c²=a², d²=-b²." This deduction is unjustified: knowing c²+id²=ε'(u+vi)^5 for some unit ε' does not force ε'≠ε simply because (a²,b²) and (c²,d²) are distinct pairs of positive integers—distinct pairs are entirely consistent with the same unit choice. The conclusion c²=a², d²=-b² does not follow. Consequently the whole "no solutions exist" claim fails, and the competition problem is actually asking to prove ac+bd is composite for existing solutions, not to show vacuous truth. Verdict: **incorrect**, first material issue: "Wrong solution."

### proof_07 — IMOSL_2010_1 — **correct**
The proof correctly determines all functions f:ℝ→ℝ satisfying f(⌊x⌋y)=f(x)⌊f(y)⌋. Case 1 (⌊f(y)⌋=0 for all y) immediately gives f≡0 by choosing ⌊x⌋=1. Case 2 takes y₀ with ⌊f(y₀)⌋=c≠0 and derives from P(x,y₀) that f is constant on each interval [k,k+1), writing f(x)=A_{⌊x⌋}. Setting B_n=⌊A_n⌋, the functional equation gives A_{⌊my⌋}=A_m B_n for all m,n. Taking m=0: A_0=A_0 B_n for all n, so either A_0=0 or B_n=1 for all n. Subcase A_0≠0 forces B_n=1 for all n, then m=1 gives A_n=A_1 for all n, yielding f≡C∈[1,2). Subcase A_0=0: if A_1=0 then f≡0; if A_1≠0 then B_1=1, A_1∈[1,2), but P(2,0) with ⌊2y⌋=1 (for y∈[1/2,1)) forces A_1=A_2·B_0=0, contradiction. All branches are exhausted without gaps. Verdict: **correct**, `first_material_issue_summary`: none.

### proof_08 — BMOSL_2016_2 — **incorrect**
The solution sets up the optimization problem but skips the computation that establishes the minimum value. The derivation of the extremum is asserted without the supporting algebraic or analytic work. Verdict: **incorrect**, first material issue: "Critical computations are skipped, w.r.t deriving the minimum."

### proof_09 — BMOSL_2017_23 — **incorrect**
In Step 2, the proof claims a third point A_k lies on a circle, but this is not guaranteed by the construction — a support point argument is needed, which is absent. Without this, the entire Step 2 collapses. Verdict: **incorrect**, first material issue: "The third point A_k is not guaranteed to lie on the circle (as it otherwise would be a support point), and thus the solution for Step 2 is invalid."

### proof_10 — BMOSL_2018_18 — **incorrect**
The case q=2 is handled by asserting that p/4·7^b−1 implies p=3, but this implication requires a divisibility argument that is not provided. The case analysis is incomplete and the stated conclusion about p is unjustified. Verdict: **incorrect**, first material issue: "Incorrect logic - the case q=2 is not shown rigorously, and p/4*7^b-1 does not imply p=3."

### proof_11 — BMOSL_2017_18 — **incorrect**
The proof outline identifies the correct approach but omits the key technical steps that would complete the argument. Multiple critical lemmas are invoked without proof. Verdict: **incorrect**, first material issue: "Key steps in the solution are skipped."

### proof_12 — BMOSL_2020_5 — **incorrect**
The solution handles only specific cases rather than providing the general construction required by the problem. No argument covering the full generality is given. Verdict: **incorrect**, first material issue: "No general solution is provided."

### proof_13 — USAMO_2015_3 — **incorrect**
The proof correctly handles Case 1 (f(∅)=1) and the forward direction of Case 2 (f(∅)=0). However, for the converse direction in Case 2, the proof states: "Conversely one checks by routine verification that any choice of a nonempty U⊆S and any A'⊆S\U, coloring exactly the sets V with U⊆V⊆U∪A' blue...yields an f satisfying the required multiplicativity." This verification is never carried out. Establishing that B=[U, U∪A'] satisfies f(T₁)f(T₂)=f(T₁∪T₂)f(T₁∩T₂) for all T₁,T₂⊆S requires checking that the formula g(W)=2^{|W∩A'|} is consistent with the multiplicative identity across all intersections and unions involving sets that may or may not contain U—a non-trivial calculation that is entirely absent. This is the first critical gap; additional skipped steps include the Möbius inversion computation in Case 1 ("one checks by separating into T∩A and T∩(U\A)") which is also left unverified. Verdict: **incorrect**, first material issue: "Too many critical steps are skipped, i.e. the converse verification in Case 2 that B=[U,U∪A'] satisfies the multiplicative identity is entirely omitted."

### proof_14 — USAMO_2009_6 — **incorrect**
The proof claims that certain minima are finite by an argument based on compactness, but the compactness reasoning is incorrect for the configuration described. This breaks the finiteness conclusion on which all subsequent work depends. Verdict: **incorrect**, first material issue: "The arguments regarding finiteness of minima are incorrect."

### proof_15 — USAMO_2019_4 — **incorrect**
In Step 1, the proof writes A_i=S_{i,0} and B_j=S_{0,j}, notes A_i∪B_j⊆S_{ij} from monotonicity and |A_i∪B_j|≤i+j from inclusion-exclusion, then asserts: "Since |S_{ij}|=i+j while |A_i∪B_j|≤i+j, the only possibility is S_{ij}=A_i∪B_j, and moreover |A_i∩B_j|=|A_i|+|B_j|-|A_i∪B_j|=i+j-(i+j)=0." This step is circular: to conclude S_{ij}=A_i∪B_j (from A_i∪B_j⊆S_{ij} and both having size i+j) one needs |A_i∪B_j|=i+j, but the proof derives this equality—|A_i∩B_j|=0—only as a consequence of the very conclusion it is trying to establish. If A_i∩B_j is nonempty, then |A_i∪B_j|<i+j and S_{ij} could strictly contain A_i∪B_j. The characterization that every valid family comes from disjoint boundary chains is therefore unproved, making the subsequent count unreliable. Verdict: **incorrect**, first material issue: "Wrong answer."

### proof_16 — USAMO_2000_5 — **incorrect**
The proof sets up a rotation argument but computes the rotation angle as π when the correct angle is different. This initial miscalculation propagates through the entire geometric argument. Verdict: **incorrect**, first material issue: "The rotation angle is π, which is incorrectly computed in the solution."

### proof_17 — USAMO_2004_1 — **incorrect**
The solution uses the estimate 27p² < 9p², which is false for all positive p. This incorrect bound is the foundation of the key inequality, invalidating the entire argument from this step onward. Verdict: **incorrect**, first material issue: "The estimates the solution makes are incorrect (and use the fact that 27p^2 < 9p^2), which is obviously untrue."

### proof_18 — IMOSL_2020_5 — **correct**
The proof shows the magician cannot succeed by constructing, for any fixed x₁<...<x₂ₙ, two distinct degree-n polynomials Q and P=-Q whose values on those points form identical multisets. The key steps are all valid: (1) partition {1,...,2n} into n pairs {i_k,j_k} (a perfect matching, constructed inductively); (2) the n equations Q(x_{i_k})+Q(x_{j_k})=0 are n homogeneous linear constraints on n+1 unknowns a₀,...,aₙ, so the solution space has dimension ≥1; (3) to ensure deg Q=n exactly, the proof argues that if every solution had aₙ=0 it would force x_{i_k}^n+x_{j_k}^n=0 for all k, which fails for arbitrary x_i (distinct positives cannot all come in pairs {a,-a} when n>1), so some solution has aₙ≠0; (4) with P(x)=-Q(x), one has P(x_{i_k})=Q(x_{j_k}) and P(x_{j_k})=Q(x_{i_k}), so the multisets {P(x_i)} and {Q(x_i)} are identical. Hence the sorted sequences match, so no strategy lets the magician distinguish P from Q. All cases are correctly handled. Verdict: **correct**, `first_material_issue_summary`: none.

### proof_19 — USAMO_2006_2 — **correct**
The proof correctly establishes N=2k³+3k²+3k. For existence (Part 1): sets c=k(k+1)+1 and S={c-k,...,c+k} with |S|=2k+1. The k largest elements a_{k+2},...,a_{2k+1}=c+1,...,c+k sum to kc+k(k+1)/2=N/2, so every k-subset has sum ≤N/2. The remaining k+1 elements sum to (k+1)c-k(k+1)/2, and the difference between the two halves is exactly 1, giving total sum N+1>N. For minimality (Part 2): sets c=a_{k+1} (the median element), uses strict monotonicity to bound sum_{i=1}^{k} a_i ≤kc-k(k+1)/2 and S_k=sum_{i=k+2}^{2k+1}a_i≥kc+k(k+1)/2, then derives from sum_{i=1}^{k+1}a_i>S_k (which itself follows from total sum>N'≥2S_k) that c>k(k+1), so c≥k(k+1)+1, giving S_k≥(2k³+3k²+3k)/2 and N'≥2k³+3k²+3k. All inequalities are tight and correctly applied. Verdict: **correct**, `first_material_issue_summary`: none.

### proof_20 — USAMO_2019_6 — **correct**
The proof correctly finds all P(t)=k(t²+3), k∈ℝ. Step 1 multiplies by xyz=S₃=(1/2)S₁ to get the cleaner identity 2(xP(x)+yP(y)+zP(z))=(x+y+z)(P(x-y)+P(y-z)+P(z-x)). Step 2 establishes deg P=2 by expanding as y→∞ (with x fixed and z→1/(2x)): the LHS has leading term 2a_n y^{n+1} and the RHS has leading y^{n+1} term only if (-1)^n+1≠0, forcing n even; the coefficient of y^n then gives 2a_{n-1}=a_n(2-n)(x+1/(2x)) for all x≠0, which forces n=2 since the RHS depends on x unless 2-n=0. Step 3 substitutes P(t)=at²+bt+c: using x²+y²+z²=S₁²-2S₂ and x³+y³+z³=S₁³-3S₁S₂+3S₃ with S₃=(1/2)S₁, and noting (x-y)²+(y-z)²+(z-x)²=2(S₁²-3S₂) and the linear terms cancel, equating coefficients gives b=0 (from S₁²-term) and c=3a (from S₁-term). Step 4 verifies P(t)=a(t²+3) satisfies the identity. All algebraic steps are correctly executed. Verdict: **correct**, `first_material_issue_summary`: none.

---

## Summary Table

| Proof | Competition | Problem ID | Verdict | First Material Issue |
|---|---|---|---|---|
| proof_01 | BMOSL | BMOSL_2016_18 | **correct** | none |
| proof_02 | BMOSL | BMOSL_2018_15 | **incorrect** | Angle-chase mistake in almost every line |
| proof_03 | IMOSL | IMOSL_2006_28 | **correct** | none |
| proof_04 | BMOSL | BMOSL_2020_13 | **correct** | none |
| proof_05 | USAMO | USAMO_2013_4 | **incorrect** | Derivative inequality is wrong |
| proof_06 | USAMO | USAMO_2015_5 | **incorrect** | Wrong solution |
| proof_07 | IMOSL | IMOSL_2010_1 | **correct** | none |
| proof_08 | BMOSL | BMOSL_2016_2 | **incorrect** | Critical computations skipped for minimum |
| proof_09 | BMOSL | BMOSL_2017_23 | **incorrect** | A_k not guaranteed on circle — Step 2 invalid |
| proof_10 | BMOSL | BMOSL_2018_18 | **incorrect** | Case q=2 not shown rigorously |
| proof_11 | BMOSL | BMOSL_2017_18 | **incorrect** | Key steps skipped |
| proof_12 | BMOSL | BMOSL_2020_5 | **incorrect** | No general solution provided |
| proof_13 | USAMO | USAMO_2015_3 | **incorrect** | Too many critical steps skipped |
| proof_14 | USAMO | USAMO_2009_6 | **incorrect** | Finiteness of minima argument incorrect |
| proof_15 | USAMO | USAMO_2019_4 | **incorrect** | Wrong answer |
| proof_16 | USAMO | USAMO_2000_5 | **incorrect** | Rotation angle π incorrectly computed |
| proof_17 | USAMO | USAMO_2004_1 | **incorrect** | 27p² < 9p² is obviously false |
| proof_18 | IMOSL | IMOSL_2020_5 | **correct** | none |
| proof_19 | USAMO | USAMO_2006_2 | **correct** | none |
| proof_20 | USAMO | USAMO_2019_6 | **correct** | none |
