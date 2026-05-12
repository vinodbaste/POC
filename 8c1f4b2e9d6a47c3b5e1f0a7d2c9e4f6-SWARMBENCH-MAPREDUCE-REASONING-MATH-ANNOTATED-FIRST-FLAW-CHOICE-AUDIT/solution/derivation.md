# Oracle Derivation — First-Flaw Choice Audit

Source: INSAIT-Institute/OPC (Open Proof Corpus)  
Task: For each of 75 incorrect olympiad proof attempts, identify the candidate excerpt (A/B/C/D) that contains the **first** unrecoverable logical flaw.

The candidate excerpts within each artifact are presented in randomized order. The correct option is the excerpt that contains the first claim that is false, unjustified, or logically breaks the argument — all subsequent steps may be conditionally correct given that flaw.

---

## Per-Artifact Derivations

### artifact_01 — BMOSL_2018_15 (2018) — **Option B**
The correct excerpt (now labeled Option B) opens with the concyclicity claim: "On the circle ω₁ the points A,D,E,G,J,N,O are concyclic."  
**Flaw:** J and N have not been shown to lie on ω₁ at this stage of the proof, making the concyclicity claim unjustified. All subsequent angle-chasing steps depend on this unproven concyclicity.

### artifact_02 — IMOSL_2010_1 (2010) — **Option D**
The correct excerpt (Option D) introduces an induction step extending a vanishing claim.  
**Flaw:** The inductive hypothesis is applied beyond its established scope — the base case and inductive structure have not been properly grounded at this point, making the extension to the integer-part a non-sequitur.

### artifact_03 — BMOSL_2018_12 (2018) — **Option A**
The correct excerpt (Option A) introduces the contradiction assumption "x/α > 2/√3."  
**Flaw:** This assumption is inconsistent with constraints already established earlier in the proof. The inequality direction reversal constitutes the first unrecoverable logical error.

### artifact_04 — BMOSL_2018_12 (2018) — **Option C**
The correct excerpt (Option C) assumes PA > k·x, PB > k·y, PC > k·z simultaneously.  
**Flaw:** These strict inequalities cannot simultaneously hold under the given triangle constraints — the configuration assumed for contradiction is itself impossible under the hypotheses.

### artifact_05 — BMOSL_2019_9 (2019) — **Option C**
The correct excerpt (Option C) applies the Tangent–Chord Theorem at a configuration where the chord and tangent do not share the point of tangency.  
**Flaw:** The Tangent–Chord angle equality is only valid at the tangency point; the proof applies it at a different point, invalidating the angular relationship.

### artifact_06 — BMOSL_2019_9 (2019) — **Option A**
The correct excerpt (Option A) computes tangent–chord angles at X and Y.  
**Flaw:** The claimed angle equality at X does not follow from the theorem as applied — AX is not established to be tangent at the relevant arc, making the angle computation unjustified.

### artifact_07 — BMOSL_2019_9 (2019) — **Option B**
The correct excerpt (Option B) applies the tangent–chord theorem in Γ.  
**Flaw:** The direction of the angle equality is reversed relative to the inscribed arc. The directed angle sign is wrong at this step, breaking the subsequent angle chase.

### artifact_08 — BMOSL_2017_5 (2017) — **Option D**
The correct excerpt (Option D) chooses exponents A_k by factorizing and assuming independence of prime factors.  
**Flaw:** The independence of the prime factors has not been established at this stage. The factorization step conflates two distinct divisibility conditions.

### artifact_09 — BMOSL_2017_5 (2017) — **Option D**
The correct excerpt (Option D) claims a Lagrange-interpolation polynomial of exact degree n with the stated properties.  
**Flaw:** The degree bound is off by one: Lagrange interpolation through n+1 points yields degree at most n, yet the proof requires degree exactly n-1. The construction does not achieve the required degree.

### artifact_10 — USAMO_2015_5 (2015) — **Option C**
The correct excerpt (Option C) claims δ yields a nontrivial rational divisor of ac+bd.  
**Flaw:** The construction of δ in the preceding step does not guarantee rationality in the relevant field extension. The assertion of "nontrivial rational divisor" is the first unjustified claim.

### artifact_11 — USAMO_2015_5 (2015) — **Option A**
The correct excerpt (Option A) asserts that α and ᾱ are coprime in ℤ[i].  
**Flaw:** The preceding argument does not establish gcd(α, ᾱ) = 1 in ℤ[i]. The coprimality claim is introduced without proof and is the first gap.

### artifact_12 — USAMO_2023_6 (2023) — **Option B**
The correct excerpt (Option B) claims F is the center of a unique orientation-preserving isometry.  
**Flaw:** The uniqueness argument relies on a compactness property that has not been established for the configuration. Without uniqueness, the identification of F fails.

### artifact_13 — USAMO_2023_6 (2023) — **Option C**
The correct excerpt (Option C) claims ω₁ = (DI I_a) carries diameter II_a because ∠IDI_a = 90°.  
**Flaw:** ∠IDI_a = 90° has not been proved at this point — it is asserted without justification. This is the first unproven geometric claim.

### artifact_14 — USAMO_2023_6 (2023) — **Option D**
The correct excerpt (Option D) cites a radical axis property for the nine-point circle.  
**Flaw:** The cited property applies to the circumcircle, not the nine-point circle. The theorem is misattributed to the wrong circle, making the radical axis argument invalid from this step onward.

### artifact_15 — USAMO_2023_6 (2023) — **Option B**
The correct excerpt (Option B) claims F coincides with a specific triangle center in the orthocentric triangle I_aI_bI_c.  
**Flaw:** The identification is incorrect — F is the wrong orthocentric analog at this stage. The center claimed does not match F's actual position.

### artifact_16 — IMOSL_2013_4 (2013) — **Option A**
The correct excerpt (Option A) introduces the bound i + j − 1 ≤ 2n−1.  
**Flaw:** The inequality conflates two different index ranges. The sharper check cited does not validate the stated bound, making the counting argument incorrect from this step.

### artifact_17 — IMOSL_2022_3 (2022) — **Option D**
The correct excerpt (Option D) defines a set for fixed x > 0 and makes a measurability claim.  
**Flaw:** The measurability requires σ-algebra stability that has not been established in the setup. A non-trivial measurability argument is simply asserted without proof.

### artifact_18 — IMOSL_2022_24 (2022) — **Option A**
The correct excerpt (Option A) claims the perpendicular bisector of AA' passes through both O and H.  
**Flaw:** While the perpendicular bisector passes through O (by the midpoint argument), the claim that it also passes through H conflates the circumcenter and orthocenter, which coincide only for equilateral triangles.

### artifact_19 — IMOSL_2022_24 (2022) — **Option C**
The correct excerpt (Option C) asserts H has equal power with respect to ω and to ω'.  
**Flaw:** The equal-power claim for H requires a specific collinearity that has not been established at this point. Without this collinearity, the power equality is unjustified.

### artifact_20 — IMOSL_2007_13 (2007) — **Option B**
The correct excerpt (Option B) fixes n ∈ ℕ and applies a prime-set result from a prior step.  
**Flaw:** The prior result was established only for a subsequence, not for all n ∈ ℕ. Applying it universally overstates its scope and is unjustified.

### artifact_21 — IMOSL_2007_13 (2007) — **Option C**
The correct excerpt (Option C) attempts to show f(1) = 1 using surjectivity.  
**Flaw:** The argument applies the functional equation before establishing that k = 1, creating a circularity. The conclusion f(1) = 1 is not validly derived.

### artifact_22 — IMOSL_2020_11 (2020) — **Option B**
The correct excerpt (Option B) introduces connectivity partitions and "cut-points" for interval families.  
**Flaw:** A structural lemma about interval connectivity is stated without proof at this step. All subsequent connectivity arguments depend on this unproven lemma.

### artifact_23 — BMOSL_2017_22 (2017) — **Option D**
The correct excerpt (Option D) claims a uniform bound N_P ≤ n−1.  
**Flaw:** The counting argument double-counts a subset of point pairs, leading to a bound that is off by one. Options that follow propagate this error.

### artifact_24 — BMOSL_2017_22 (2017) — **Option A**
The correct excerpt (Option A) introduces a binomial sum inequality.  
**Flaw:** The inequality direction is reversed — the argument requires ≥ where ≤ is written. This makes the step logically invalid and the conclusion unsupported.

### artifact_25 — BMOSL_2017_22 (2017) — **Option B**
The correct excerpt (Option B) establishes a first-pass bound K ≤ n(n−1)/4.  
**Flaw:** The counting used to derive this bound omits a class of configurations, making the bound incorrect. The true worst case exceeds n(n−1)/4.

### artifact_26 — BMOSL_2018_2 (2018) — **Option C**
The correct excerpt (Option C) handles Case q=2 with a weight-sum condition.  
**Flaw:** The summation index runs from 1 to n but the bit-weight model requires starting from 0 (the constant term). The sum is missing the leading term, making the case analysis incomplete.

### artifact_27 — USAMO_2016_3 (2016) — **Option A**
The correct excerpt (Option A) states that F lies on ω (the circumcircle), making its power with respect to ω equal to zero.  
**Flaw:** F lying on ω is asserted without proof and is false in general. All subsequent equal-power reasoning inherits from this unproven claim.

### artifact_28 — USAMO_2016_3 (2016) — **Option D**
The correct excerpt (Option D) computes slopes and verifies perpendicularity by direct algebra.  
**Flaw:** The coordinate assignment used implicitly assumes a special case rather than the general position. The "direct algebra" check is valid only for the special case, not the general configuration.

---

### artifact_29 — BMOSL_2021_3 (2021) — **Option A**
The correct excerpt (Option A) bounds \(a\) by arguing \(3/a\ge1\), concluding \(a\le 2\).  
**Flaw:** The correct bound is \(a\le 3\) (since \(a=3\) yields the valid solution \((3,3,3)\)). The excerpt asserts \(a\le 2\) with no justification for excluding \(a=3\), silently discarding the third solution.

### artifact_30 — IMOSL_2019_7 (2019) — **Option B**
The correct excerpt (Option B) derives \(f(3m)=f(m)+c\) by substituting \(n=-f(m)\).  
**Flaw:** When combining \(f(-f(m))=f(m)+c-f(3m)-2014\) with \(f(-f(m)+c)=f(-f(m))+2014\), the excerpt drops the term \(-f(3m)\) in the final cancellation, concluding \(f(3m)=f(m)+c\) where the correct result involves an additional unknown quantity.

### artifact_31 — USAMO_2018_4 (2018) — **Option C**
The correct excerpt (Option C) computes \(\sum_{j=0}^{p-1}r_j\) using the quadratic residue structure.  
**Flaw:** The sum formula \(\sum r_j=p(p^2-1)/12\) uses the Gauss sum for QRs incorrectly: it counts each nonzero residue twice but the formula \(\frac{(p-1)/2\cdot(p+1)/2\cdot p}{3}\) for \(\sum_{k=1}^{(p-1)/2}k^2\) uses the wrong closed form (missing the factor of 2 correctly but applying the sum-of-squares formula with shifted upper limit).

### artifact_32 — BMOSL_2016_11 (2016) — **Option D**
The correct excerpt (Option D) attempts to re-derive the carry count via a different method.  
**Flaw:** The excerpt conflates the total number of carries in base-2 addition of \(n+n\) with the number of \(1\)-bits plus an "adjacent-pair count." In fact, Kummer's theorem gives the carry count as exactly the number of \(1\)-bits in \(n\) (digit sum \(s_2(n)\)), with no extra adjacent-pair term. The proposed formula \(s_2(n)+\text{(adjacent pairs)}\) is incorrect.

### artifact_33 — IMOSL_2021_9 (2021) — **Option A**
The correct excerpt (Option A) uses log-convexity to bound the partial sums, obtaining \((\sum a_k)^2\le n^2\max_{i,j}(a_ia_j)\).  
**Flaw:** This bound is weaker than the claimed Cauchy-Schwarz inequality and does not imply it. The excerpt presents the log-convex bound as a stepping stone to Cauchy-Schwarz without establishing the connection; the two bounds are independent.

### artifact_34 — USAMO_2014_3 (2014) — **Option B**
The correct excerpt (Option B) substitutes \(b=1-a\) to extract a recurrence.  
**Flaw:** The resulting expression \((2a-1)[f(2-2a)-f(2a-1)]=f(1)\) is simplification of the original equation only when \(a+b=1\). The excerpt applies this identity as if it holds for general \(a\) (beyond the substitution), making subsequent deductions circular.

### artifact_35 — BMOSL_2015_8 (2015) — **Option C**
The correct excerpt (Option C) asserts nontriviality of the map using an unstated assumption.  
**Flaw:** The excerpt writes "since \(k<p-1\) is assumed," but no such assumption appears in the problem statement. The problem only gives \(\gcd(k,p-1)=1\), which does not imply \(k<p-1\). The claim of nontriviality from \(k\bmod(p-1)\ne 0\) requires knowing \(k\not\equiv 0\pmod{p-1}\), which follows from \(\gcd(k,p-1)=1\) alone without the false assumption.

### artifact_36 — IMOSL_2016_5 (2016) — **Option D**
The correct excerpt (Option D) applies pigeonhole to bound \(d(r,pq)\).  
**Flaw:** The pigeonhole is applied to "perpendicular strips of width \(D/n\)," claiming the farthest point lies in a strip at distance \(\le D/n\). This confuses the number of points (\(n\)) with the strip width: \(n\) strips of width \(D/n\) cover \([0,D]\), but the maximum distance from a chord to a point is bounded by the strip's diameter, not its width. The bound \(d(r,pq)\le D/n\) is unjustified.

### artifact_37 — USAMO_2021_2 (2021) — **Option A**
The correct excerpt (Option A) applies Nesbitt's inequality to the rewritten sum.  
**Flaw:** After rewriting \(\frac{a}{1-a^2}=\frac{a}{(b+c)(1+a)}\), the excerpt claims "the sum \(\ge9/8\) follows from Nesbitt's inequality." Nesbitt's inequality states \(\frac{a}{b+c}+\frac{b}{a+c}+\frac{c}{a+b}\ge3/2\); the denominators here are \((b+c)(1+a)\ne b+c\), so Nesbitt does not directly apply.

### artifact_38 — BMOSL_2020_6 (2020) — **Option B**
The correct excerpt (Option B) computes the altitude foot \(D\) and the angle \(\angle DAC\).  
**Flaw:** The inscribed angle theorem is applied to compute \(\angle BAM=90°-\frac{B+C}{2}\), but the correct value for the angle bisector from \(A\) to the midpoint of arc \(BC\) is \(\angle BAM=\frac{B-C}{2}\) (for \(B\ne C\)). The mistake conflates \(\angle BAM\) (half the arc difference) with a symmetric expression, leading to the wrong angle value.

### artifact_39 — IMOSL_2018_8 (2018) — **Option C**
The correct excerpt (Option C) counts ordered pairs with \(\gcd(a,n)=1\).  
**Flaw:** The argument writes "the factor of 2 and division by 2 cancel," then separately handles odd \(n\) using "\(2\cdot(\phi(n)/2)=\phi(n)\)." This implicitly assumes \(\phi(n)\) is even, but \(\phi(1)=1\) and \(\phi(2)=1\) are odd. For \(n\ge3\), \(\phi(n)\) is indeed even, but the argument applies the formula without this restriction.

### artifact_40 — USAMO_2017_6 (2017) — **Option D**
The correct excerpt (Option D) invokes the DAG structure to claim a unique sink.  
**Flaw:** A DAG can have multiple sinks (multiple vertices with no outgoing edges). The excerpt asserts "a DAG has a unique sink" without proof. The monovariant \(\Phi\) shows the process terminates and the graph is acyclic, but acyclicity alone does not give a unique final state — that requires an additional argument (e.g., showing different move sequences reach the same configuration).

### artifact_41 — BMOSL_2022_4 (2022) — **Option A**
The correct excerpt (Option A) applies Cauchy-Schwarz in Engel/Titu form.  
**Flaw:** The Engel form states \(\sum\frac{x_i^2}{y_i}\ge\frac{(\sum x_i)^2}{\sum y_i}\). The excerpt writes \(\frac{1}{\sqrt{a}}+\cdots\ge\frac{(\sqrt[4]{a}+\cdots)^2}{\sqrt{a}+\cdots}\), which would require \(x_i=\sqrt[4]{a_i}\) and \(y_i=\sqrt{a_i}\), giving \(x_i^2/y_i=\sqrt{a_i}/\sqrt{a_i}=1\ne1/\sqrt{a_i}\). The numerators and denominators are misassigned.

### artifact_42 — IMOSL_2020_6 (2020) — **Option B**
The correct excerpt (Option B) states that the circumcircle of the contact triangle has center at the midpoint of \(OI\).  
**Flaw:** This is not a standard result and is incorrect for general triangles. The circumcenter of the contact triangle (intouch triangle) \(DEF\) does not generally coincide with the midpoint of \(OI\); the nine-point center \(N_9\) lies at the midpoint of \(OH\) (not \(OI\)). The claim introduces a false geometric fact as a stepping stone.

### artifact_43 — USAMO_2019_4 (2019) — **Option C**
The correct excerpt (Option C) analyzes the parity of the correction terms.  
**Flaw:** The parity analysis states "in both cases \(p\equiv1,3\pmod4\) the parities cancel," but the argument for \(p\equiv1\pmod4\) uses different parity assignments than for \(p\equiv3\pmod4\) without showing the cancellation explicitly in each case. The conclusion is asserted rather than derived: "the total is even" is stated as obvious when it requires a direct verification for each residue class.

### artifact_44 — BMOSL_2023_7 (2023) — **Option C**
The correct excerpt (Option C) performs a consistency check on the companion tangent length \(CD\).  
**Flaw:** Option C claims \(AE = s - b\), but \(s - b\) is the tangent length from vertex \(B\) (i.e., \(BD = BF = s - b\)), not from vertex \(A\). The tangent from \(A\) has length \(AE = AF = s - a\). Assigning \(s - b\) to \(AE\) conflates the tangent lengths of two different vertices, making the consistency check \(AE + EC = (s-b)+(s-c)\) meaningless — it cannot verify \(AE + EC = b = CA\).

### artifact_45 — IMOSL_2014_2 (2014) — **Option A**
The correct excerpt (Option A) sets up the difference \(f(n)-f(n-1)\) and simplifies.  
**Flaw:** After computing \(f(n)-f(n-1)=\frac{a_n}{n}-\frac{S_{n-1}}{n(n-1)}-(a_n-a_{n-1})\), the excerpt bounds this by \(\frac{a_n}{n}\) and concludes \(f\) is strictly decreasing. The bound only says \(f(n)-f(n-1)<\frac{a_n}{n}\), which does not establish negativity. Without knowing the sign of the increment, strict decrease cannot be claimed.

### artifact_46 — USAMO_2022_3 (2022) — **Option C**
The correct excerpt (Option C) finds the intersection \(T\) of the two tangents.  
**Flaw:** The orthocenter formula \(\vec{OH}=\vec{OA}+\vec{OB}+\vec{OC}\) is applied after setting up coordinates centred at \(M\) (not at \(O\)). In coordinates centred at \(M\), the formula gives the wrong result because the formula holds only when position vectors are taken from \(O\). The computation of \(H=(p,-2d)\) is therefore incorrect.

### artifact_47 — BMOSL_2019_17 (2019) — **Option A**
The correct excerpt (Option A) deduces \(f(1)=1\) and \(1+f(n)\mid 1+n\).  
**Flaw:** From \(m=1\), \(f(1)+f(n)\mid 1+n\). Since \(f(1)\mid 1\), one concludes \(f(1)=1\). But the deduction \(f(1)\mid 1\) comes from setting \(m=n=1\) in \(f(m)\mid m\), giving \(f(1)\mid 1\). The excerpt presents this as "since \(f(1)\mid 1\), we get \(f(1)=1\)" as if no argument is needed, but the step from \(m=1\) in \(f(m)+f(n)\mid m+n\) to \(f(1)+f(n)\mid 1+n\) requires that \(f(1)\mid 1\) is already established, creating a circularity in the order of the argument.

### artifact_48 — IMOSL_2015_6 (2015) — **Option A**
The correct excerpt (Option A) states the inclusion-exclusion formula for derangements.  
**Flaw:** Option A writes the formula \(D(n)=\sum_{k=0}^n(-1)^k\binom{n}{k}(n-k)!\) and invokes inclusion-exclusion, but does not verify the key intermediate fact \(\bigl|\bigcap_{i\in S}A_i\bigr|=(n-k)!\) for any \(k\)-element subset \(S\). This is the essential step — that fixing the \(k\) elements of \(S\) leaves exactly \((n-k)!\) permutations of the rest — and it is simply asserted without proof. All subsequent simplifications build on this unverified claim.

### artifact_49 — USAMO_2020_5 (2020) — **Option A**
The correct excerpt (Option A) establishes the intersection size for the inclusion-exclusion argument.  
**Flaw:** Option A states \(\bigl|\bigcap_{i\in S}A_i\bigr|=(n-k)!\) for any \(k\)-element set \(S\subseteq\{1,\ldots,n\}\) without justification. This is the foundational claim of the entire inclusion-exclusion argument: that fixing the \(k\) specified elements leaves \((n-k)!\) free permutations of the remaining elements. Asserting it without proof is the first unrecoverable gap; Options B and C are correct given this fact, but the fact itself is never established.

### artifact_50 — BMOSL_2018_9 (2018) — **Option D**
The correct excerpt (Option D) uses directed angles to prove \(F\in\Omega\).  
**Flaw:** The step \(\angle BED=\angle BAD\) (as inscribed angles) is incorrect. Inscribed angles subtend the same arc only when both vertices lie on the circle. \(E=AC\cap BD\) is generically interior to \(\Omega\), not on \(\Omega\), so \(\angle BED\) is not an inscribed angle in \(\Omega\). The angle equality requires a different justification (e.g., using the cyclic quadrilateral property directly), not the inscribed angle theorem.

### artifact_51 — IMOSL_2011_5 (2011) — **Option A**
The correct excerpt (Option A) invokes Fermat's Little Theorem to claim divisibility lifts.  
**Flaw (misapplied_theorem):** Fermat's Little Theorem governs modular exponentiation modulo a prime; it has nothing to do with the divisibility identity \(f(m-n)\mid f(m)-f(n)\). The theorem's preconditions (prime modulus and base coprime to it) are not even named here, so the citation is unsupported. All subsequent claims (\(f(m-n)\mid\gcd(f(m),f(n))\)) rest on this misapplied citation.

### artifact_52 — USAMO_2013_4 (2013) — **Option B**
The correct excerpt (Option B) assumes WLOG \(x=y=z\) by symmetry of the equation.  
**Flaw (false_assumption):** The minimum function on the LHS is not symmetric in the same way that a sum or product is — it picks out one specific argument. The reduction to \(x=y=z\) discards asymmetric solutions and is therefore an invalid simplification, not a "WLOG" move.

### artifact_53 — BMOSL_2020_11 (2020) — **Option C**
The correct excerpt (Option C) computes the homothety image \(h(O)\) and asserts it equals the nine-point center.  
**Flaw (unjustified_claim):** The identification \(h(O)=\) midpoint of \(HO\) is asserted without derivation. While the conclusion is correct, the step from "homothety at \(H\) with ratio \(1/2\)" to "image of \(O\) is the midpoint of \(HO\)" is exactly the key fact needed and is left unproven. The cited "standard result" linking reflections of \(H\) to altitude feet is also unjustified.

### artifact_54 — IMOSL_2016_3 (2016) — **Option D**
The correct excerpt (Option D) verifies \(n=3\) works using the arithmetic \(1/3+2/9+3/9=9/9=1\).  
**Flaw (algebraic_error):** \(1/3=3/9\), so the correct sum is \(3/9+2/9+3/9=8/9\), not \(9/9\). The claim that \(n=3\) is a solution rests on this incorrect arithmetic.

### artifact_55 — USAMO_2018_2 (2018) — **Option A**
The correct excerpt (Option A) takes \(y\to\infty\) and uses boundedness of \(f\) to conclude \(f\equiv 2\).  
**Flaw (scope_violation):** The limit argument is valid only for bounded continuous functions, but the problem permits unbounded \(f:(0,\infty)\to(0,\infty)\). Applying the bounded-class result to the unrestricted class is a scope violation; the "uniqueness" conclusion does not generalize.

### artifact_56 — BMOSL_2014_7 (2014) — **Option B**
The correct excerpt (Option B) applies Lifting the Exponent without checking \(p\mid a-1\).  
**Flaw (misapplied_theorem):** The LTE formula \(v_p(a^n-1)=v_p(n)+v_p(a-1)\) for odd primes \(p\) requires \(p\mid a-1\) as a precondition. The proof writes "for any \(a\)" and so applies the lemma where its hypothesis fails — the contradiction in Step 4 confirms the misapplication.

### artifact_57 — IMOSL_2015_2 (2015) — **Option C**
The correct excerpt (Option C) descends from \((a,b,c)\) to \((a',b',c')\) and applies the same conditions.  
**Flaw (false_assumption):** The new triple's "differences" \(2a'b'-c'\) etc. are not guaranteed to be positive powers of 2 — when the original \(ab-c=2\), the new difference is 1, which only sometimes works; in other cases it can be zero or negative. The premise that \((a',b',c')\) satisfies the analogous conditions is false in general.

### artifact_58 — USAMO_2009_2 (2009) — **Option B**
The correct excerpt (Option B) claims the odd integers in \(\{-n,\ldots,n\}\) have size \(n\).  
**Flaw (algebraic_error):** For odd \(n\) (e.g., \(n=5\)) the odd integers are \(\{-5,-3,-1,1,3,5\}\), which has size 6, not \(n=5\). The construction does not give exactly \(n\) elements as claimed, breaking the lower-bound argument.

### artifact_59 — BMOSL_2016_4 (2016) — **Option C**
The correct excerpt (Option C) sums the tangent-line inequality cyclically.  
**Flaw (algebraic_error):** The pointwise tangent-line inequality \(a^2/(a+b^2)\ge(2a-b)/2\) is itself false at certain configurations (e.g., \(a=0.5,b=2\) gives LHS \(\approx 0.056\) and RHS \(=-0.5\); the inequality reverses for less extreme cases). The cyclic sum cancellation is also evaluated incorrectly — the proof's manipulation of \(\sum_{cyc}(2a-b)\) misuses the symmetry and produces \(3/2\) only by accident.

### artifact_60 — IMOSL_2017_8 (2017) — **Option B**
The correct excerpt (Option B) claims the infimum of \(E\) is 0 via \(x_i=r^i\) with large \(r\).  
**Flaw (scope_violation):** The construction \(x_i=r^i\) was designed for a linear (open) sequence, but the problem's sum is cyclic with wrap-around. The wrap-around term \(x_n^2/(x_n^2+x_1^2)\) tends to 1 (not \(1/(1+r^2)\)) for large \(r\), so the sum does not tend to 0. Applying the linear-case scaling to the cyclic case is an invalid scope extension.

### artifact_61 — USAMO_2020_4 (2020) — **Option C**
The correct excerpt (Option C) uses Pick's Theorem on the triangle \((0,0),v_i,v_j\) to conclude \(I=0,B=3\).  
**Flaw (misapplied_theorem):** Pick's Theorem gives \(A=I+B/2-1\), but area \(=1/2\) alone does not force \(I=0\) and \(B=3\); these require additionally that no lattice point lies in the interior or on the edges. The proof asserts the conclusion as if forced by area, omitting the precondition check.

### artifact_62 — BMOSL_2019_18 (2019) — **Option D**
The correct excerpt (Option D) replaces "angle bisector from \(A\)" with "perpendicular bisector of \(AI\)".  
**Flaw (false_assumption):** The proof silently changes the problem to one where \(P\) lies on the perpendicular bisector of \(AI\), under which the conclusion \(PA=PI\) is trivial. The original setup (P on the angle bisector from \(A\)) is replaced by a false premise about \(P\)'s definition.

### artifact_63 — IMOSL_2009_11 (2009) — **Option A**
The correct excerpt (Option A) rearranges the inequality and claims this reformulation is equivalent.  
**Flaw (unjustified_claim):** The leap from the rearranged inequality \(K(abc-1)\ge 2(ab+bc+ca)-6\) to "we seek the largest \(K\)" is asserted without addressing the case where \(abc<1\), where the inequality direction reverses upon dividing by \(abc-1\). The proof states the equivalence as obvious when sign analysis is required.

### artifact_64 — USAMO_2019_3 (2019) — **Option B**
The correct excerpt (Option B) counts length-3 walks from \(v\) as \(5\cdot4\cdot4=80\).  
**Flaw (algebraic_error):** This count conflates walks with simple paths. A walk that returns to a previously visited vertex is excluded from a simple path; on the icosahedron, triangle faces create cycles that the count over-includes. The number 80 is the count of length-3 walks with no immediate back-edge, not the count of simple paths to \(v'\).

### artifact_65 — BMOSL_2021_19 (2021) — **Option C**
The correct excerpt (Option C) writes \(H_p=\sum_{j=1}^{p}1/j\) and applies Wolstenholme's classical lemma.  
**Flaw (scope_violation):** Wolstenholme's classical lemma states \(\sum_{j=1}^{p-1}1/j\equiv 0\pmod{p^2}\); the sum range is \(1\) to \(p-1\), not \(1\) to \(p\), because \(1/p\) is not invertible mod \(p^k\). The proof extends the result to a range where the lemma's hypothesis (\(j\) coprime to \(p\)) fails, introducing a spurious factor that yields the wrong final congruence.

### artifact_66 — IMOSL_2012_6 (2012) — **Option B**
The correct excerpt (Option B) applies the Inscribed Angle Theorem without tracking which arc \(M\) is on.  
**Flaw (misapplied_theorem):** The theorem requires specifying whether the inscribed and central angles subtend the same or opposite arcs. The proof oscillates among "\(\angle BMC=\angle BAC\)", "\(=2\angle BAC\)", and "\(=180°-\angle BAC\)" without consistently establishing \(M\)'s arc location. The precondition (M's arc) is never rigorously verified.

### artifact_67 — USAMO_2012_5 (2012) — **Option D**
The correct excerpt (Option D) applies Desargues' theorem, claiming \(ABC\) and \(A'B'C'\) are in perspective from \(P\).  
**Flaw (false_assumption):** \(A'\) is on line \(PA^*\) (the reflected line), not on line \(PA\). Hence the triangles are NOT in perspective from \(P\) — the premise needed to apply Desargues is false in general.

### artifact_68 — BMOSL_2017_14 (2017) — **Option A**
The correct excerpt (Option A) concludes "Hence \(n=1\)" from \(n\le 1\).  
**Flaw (unjustified_claim):** The reduction "n ≤ 1 for positive integer n implies n = 1" is asserted as obvious without explicit derivation. While the conclusion is true, the inferential step that excludes \(n=0\) by the positive-integer constraint is left implicit.

### artifact_69 — IMOSL_2008_4 (2008) — **Option C**
The correct excerpt (Option C) matches coefficients of \(f(x)=ax+b/x+c\) and concludes \(c=2,b=1,a=0\) as the unique solution.  
**Flaw (algebraic_error):** Case B (\(f(1)=-2\)) yields another valid family of solutions, but the proof omits it entirely by failing to track both branches of the quadratic \(f(1)^2-f(1)-6=0\). The "uniqueness" claim is the result of incomplete case enumeration — an arithmetic/algebraic oversight in the coefficient matching.

### artifact_70 — USAMO_2011_3 (2011) — **Option D**
The correct excerpt (Option D) deduces equilateral triangle from equal arc-differences.  
**Flaw (scope_violation):** The criterion "equal arc-differences ⇒ equilateral inscribed triangle" applies only to triangles whose vertices lie on the circle. The midpoints \(M_1,M_2,M_3\) lie strictly inside the circle (on a smaller concentric circle), so the criterion is applied outside its valid scope.

### artifact_71 — BMOSL_2015_13 (2015) — **Option A**
The correct excerpt (Option A) invokes Chebyshev's sum inequality.  
**Flaw (misapplied_theorem):** Chebyshev's inequality requires both sequences to be similarly sorted. The sequence \((a^2/(b^2+c^2),\ldots)\) is not automatically sorted in the same order as \((a,b,c)\), and the proof assumes "(similarly sorted)" without verifying it.

### artifact_72 — IMOSL_2013_2 (2013) — **Option B**
The correct excerpt (Option B) uses symmetry to argue \(P(h>t)=P(t>h)\) and concludes \(1/2\).  
**Flaw (false_assumption):** The symmetry \(P(h>t)=P(t>h)\) silently assumes a fair coin (\(P(\text{heads})=1/2\)). The problem says "a coin is tossed" without specifying fairness — the proof relies on fairness as an unstated premise.

### artifact_73 — USAMO_2014_5 (2014) — **Option D**
The correct excerpt (Option D) concludes \(XY=R\) "by a lengthy angle-chasing argument (omitted for brevity)".  
**Flaw (unjustified_claim):** The omitted argument is the entire content of the problem. Asserting the conclusion without supplying any of the angle-chasing is the canonical unjustified claim.

### artifact_74 — BMOSL_2022_8 (2022) — **Option D**
The correct excerpt (Option D) verifies the formula on small cases via specific pair enumerations.  
**Flaw (algebraic_error):** The verification conflates ordered and unordered pair counts inconsistently across the small-\(n\) cases, and the implicit conversion via \(\varphi\) double-counts certain pairs. The arithmetic confirmation of the closed form is therefore tainted by a counting/arithmetic mistake.

### artifact_75 — IMOSL_2018_4 (2018) — **Option A**
The correct excerpt (Option A) claims a knight move changes parity in BOTH coordinates.  
**Flaw (algebraic_error):** A knight move changes one coordinate by \(\pm 1\) (odd, parity flips) and the other by \(\pm 2\) (even, parity stays). Hence knight moves change parity in exactly ONE coordinate, not both. The parity arithmetic is computed incorrectly, breaking the Mantel-coloring bipartition argument that follows.

## Summary Table

| Artifact | Competition | Year | Correct Option | Type of First Flaw |
|---|---|---|---|---|
| 01 | BMOSL | 2018 | **B** | Unjustified concyclicity claim |
| 02 | IMOSL | 2010 | **D** | Induction applied beyond established scope |
| 03 | BMOSL | 2018 | **A** | Contradiction assumption inconsistent with constraints |
| 04 | BMOSL | 2018 | **C** | Impossible simultaneous strict inequalities |
| 05 | BMOSL | 2019 | **C** | Tangent–Chord theorem misapplied at wrong point |
| 06 | BMOSL | 2019 | **A** | Tangent direction error in angle equality |
| 07 | BMOSL | 2019 | **B** | Directed angle sign error |
| 08 | BMOSL | 2017 | **D** | Independence of prime factors assumed without proof |
| 09 | BMOSL | 2017 | **D** | Lagrange interpolation degree off-by-one |
| 10 | USAMO | 2015 | **C** | Rationality of divisor not guaranteed by construction |
| 11 | USAMO | 2015 | **A** | Coprimality in ℤ[i] asserted without proof |
| 12 | USAMO | 2023 | **B** | Uniqueness of isometry not established |
| 13 | USAMO | 2023 | **C** | ∠IDI_a = 90° asserted without justification |
| 14 | USAMO | 2023 | **D** | Nine-point circle property misattributed |
| 15 | USAMO | 2023 | **B** | Wrong orthocentric analog identified |
| 16 | IMOSL | 2013 | **A** | Index bound conflates two different ranges |
| 17 | IMOSL | 2022 | **D** | Measurability asserted without σ-algebra argument |
| 18 | IMOSL | 2022 | **A** | Circumcenter/orthocenter conflation |
| 19 | IMOSL | 2022 | **C** | Equal-power claim for H unproven |
| 20 | IMOSL | 2007 | **B** | Subsequence result applied universally |
| 21 | IMOSL | 2007 | **C** | Circularity in f(1)=1 argument |
| 22 | IMOSL | 2020 | **B** | Connectivity lemma stated without proof |
| 23 | BMOSL | 2017 | **D** | Off-by-one in pair counting |
| 24 | BMOSL | 2017 | **A** | Binomial inequality direction reversed |
| 25 | BMOSL | 2017 | **B** | First-pass bound omits a configuration class |
| 26 | BMOSL | 2018 | **C** | Sum missing leading term (index off by 1) |
| 27 | USAMO | 2016 | **A** | F on ω asserted without proof |
| 28 | USAMO | 2016 | **D** | Coordinate argument not general (special case assumed) |
| 29 | BMOSL | 2021 | **A** | Bound a≤2 derived instead of correct a≤3, missing (3,3,3) |
| 30 | IMOSL | 2019 | **B** | Algebraic term silently dropped when eliminating f(−f(m)) |
| 31 | USAMO | 2018 | **C** | Sum of quadratic residues computed with wrong multiplicity |
| 32 | BMOSL | 2016 | **D** | Kummer carry count conflated with binary digit-sum |
| 33 | IMOSL | 2021 | **A** | Log-convex interpolation bound cited before Cauchy-Schwarz without connection |
| 34 | USAMO | 2014 | **B** | Substitution collapses two sides under unverified symmetry |
| 35 | BMOSL | 2015 | **C** | Unintroduced assumption k<p−1 used to claim non-triviality |
| 36 | IMOSL | 2016 | **D** | Pigeonhole strip bound on perpendicular distance is unjustified |
| 37 | USAMO | 2021 | **A** | Nesbitt's inequality invoked with mismatched denominator form |
| 38 | BMOSL | 2020 | **B** | Inscribed angle computes ∠BAM = 90°−(B+C)/2, wrong for non-isosceles |
| 39 | IMOSL | 2018 | **C** | Ordered-pair count uses φ(n)/2 assuming φ(n) always even |
| 40 | USAMO | 2017 | **D** | DAG uniqueness of sink asserted without showing all paths converge |
| 41 | BMOSL | 2022 | **A** | Cauchy-Schwarz Engel form has numerators and denominators swapped |
| 42 | IMOSL | 2020 | **B** | Circumcircle of contact triangle center incorrectly stated as midpoint of OI |
| 43 | USAMO | 2019 | **C** | Parity cancellation asserted without verifying each case separately |
| 44 | BMOSL | 2023 | **C** | Consistency check assigns s-b to AE (tangent from A), but AE = s-a |
| 45 | IMOSL | 2014 | **A** | Upper bound on f(n) increment does not establish strict decrease of f |
| 46 | USAMO | 2022 | **C** | Orthocenter formula OH=OA+OB+OC applied in M-centred coordinates |
| 47 | BMOSL | 2019 | **A** | Divisibility case f(n)≤(n−1)/2 not eliminated before concluding f=id |
| 48 | IMOSL | 2015 | **A** | Intersection size |∩A_i|=(n-k)! stated without proof (key inclusion-exclusion fact) |
| 49 | USAMO | 2020 | **A** | Intersection size |∩A_i|=(n-k)! stated without proof (foundational claim unverified) |
| 50 | BMOSL | 2018 | **D** | ∠BED=∠BAD cited as inscribed angles but E is not on Ω |
| 51 | IMOSL | 2011 | **A** | Fermat's Little Theorem misapplied to a non-modular-exponentiation identity |
| 52 | USAMO | 2013 | **B** | WLOG x=y=z exploits a symmetry the minimum function does not preserve |
| 53 | BMOSL | 2020 | **C** | Homothety image h(O)=midpoint of HO asserted without derivation |
| 54 | IMOSL | 2016 | **D** | Arithmetic error: 1/3+2/9+3/9 = 8/9, not 9/9 |
| 55 | USAMO | 2018 | **A** | Bounded-function limit argument applied to unrestricted function class |
| 56 | BMOSL | 2014 | **B** | LTE applied without verifying p \| a−1 precondition |
| 57 | IMOSL | 2015 | **C** | Descent assumes new triple satisfies same conditions when it need not |
| 58 | USAMO | 2009 | **B** | Count of odd integers in {−n,…,n} is n+1 for odd n, not n |
| 59 | BMOSL | 2016 | **C** | Tangent-line inequality fails pointwise; cyclic sum cancellation is invalid |
| 60 | IMOSL | 2017 | **B** | Geometric scaling x_i=r^i ignores cyclic wrap-around boundary |
| 61 | USAMO | 2020 | **C** | Pick's theorem misapplied — interior/boundary conditions not verified |
| 62 | BMOSL | 2019 | **D** | Silently replaces "angle bisector" with "perpendicular bisector of AI" |
| 63 | IMOSL | 2009 | **A** | Sign analysis for abc<1 case omitted in rearrangement |
| 64 | USAMO | 2019 | **B** | Count of walks (80) conflated with count of simple paths |
| 65 | BMOSL | 2021 | **C** | Sum range extended to j=p where 1/p is non-invertible |
| 66 | IMOSL | 2012 | **B** | Inscribed Angle Theorem applied without tracking arc position of M |
| 67 | USAMO | 2012 | **D** | Desargues applied assuming false perspective from P |
| 68 | BMOSL | 2017 | **A** | "Hence n=1" reduction left implicit |
| 69 | IMOSL | 2008 | **C** | Case B (f(1)=−2) branch omitted in coefficient matching |
| 70 | USAMO | 2011 | **D** | Equal-arc criterion applied to points not on the original circle |
| 71 | BMOSL | 2015 | **A** | Chebyshev applied without verifying both sequences are similarly sorted |
| 72 | IMOSL | 2013 | **B** | Implicit fairness assumption for the coin |
| 73 | USAMO | 2014 | **D** | "By a lengthy angle-chasing argument (omitted)" — content of the problem unproven |
| 74 | BMOSL | 2022 | **D** | Ordered vs unordered pair count conflated; small-case verification arithmetic flawed |
| 75 | IMOSL | 2018 | **A** | Knight move changes parity in exactly one coordinate, not both |
