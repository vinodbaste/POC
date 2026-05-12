# Oracle Derivation — miniF2F First-Invalid-Step Audit

Source: openai/miniF2F benchmark  
Task: For each of 28 incorrect proof attempts drawn from AIME, AMC, IMO, and MATH competition problems, identify the candidate excerpt (A/B/C/D) that contains the **first** invalid or unjustified reasoning step.

The candidate excerpts within each artifact are presented in randomized order. The correct option is the excerpt that first breaks valid mathematical reasoning — all subsequent steps may be conditionally correct given that flaw.

---

## Per-Artifact Derivations

### artifact_01 — aime_1983_p9 (AIME 1983) — **Option A**
**Flaw:** Claims the minimum of $\sum|x-k|$ is at the arithmetic mean. The correct theorem is that the minimum of a sum of absolute values is at the **median**, not the mean. The dataset $\{1,\ldots,10\}$ is symmetric so mean = median = 5.5, making the numerical answer coincidentally correct, but the theorem cited is wrong.

### artifact_02 — aime_1984_p1 (AIME 1984) — **Option B**
**Flaw:** Claims "by symmetry" the even- and odd-indexed subsequences must each sum to half the total (137/2). The two subsequences differ: each even term exceeds the corresponding odd term by the common difference 1, so their sums differ by 49, not 0.

### artifact_03 — aime_1985_p7 (AIME 1985) — **Option C**
**Flaw:** Incorrectly reverses the sign of the triple-intersection term in inclusion-exclusion, subtracting $|A\cap B\cap C|$ instead of adding it. Standard inclusion-exclusion: $|A\cup B\cup C| = |A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|$.

### artifact_04 — aime_1986_p3 (AIME 1986) — **Option D**
**Flaw:** Claims a geometric series "also converges for $|x|>1$ with a negative ratio." A geometric series $\sum x^n$ diverges for all $|x|\ge 1$ regardless of sign. The spurious second convergence regime is a fabricated theorem.

### artifact_05 — aime_1987_p8 (AIME 1987) — **Option A**
**Flaw:** Applies Fermat's Little Theorem to the composite modulus 15. FLT requires a **prime** modulus. The actual multiplicative order of 2 modulo 15 is 4 (since $2^4=16\equiv 1\pmod{15}$), not 14.

### artifact_06 — aime_1988_p2 (AIME 1988) — **Option B**
**Flaw:** The quadratic formula derivation introduces a sign confusion: it writes $s = (-1)\cdot 4 \pmod 7$ but the numerator should be $(1-2) = -1$, which by a different chain of errors produces the numerically correct root while disguising a sign error that would fail on non-symmetric cases.

### artifact_07 — aime_1989_p4 (AIME 1989) — **Option C**
**Flaw:** Counts forbidden (Alice, Bob, X) committees by letting X range over all 10 people including Alice and Bob themselves, giving 10 forbidden committees. In a committee of distinct people, X must be chosen from the remaining $10-2=8$ people, giving 8 forbidden committees.

### artifact_08 — aime_1990_p2 (AIME 1990) — **Option D**
**Flaw:** Overrides the correctly computed Pisano period $\pi(8)=12$ with a fabricated "standard theorem" claiming the period is $\text{lcm}(2,5)=10$. No such simple formula exists for $\pi(2^k)$.

### artifact_09 — amc12a_2002_p11 (AMC 2002) — **Option A**
**Flaw:** States that a standard six-sided die has 7 outcomes (faces 0–6). A standard die has faces 1–6, giving 6 outcomes. The resulting denominator of 49 is wrong; the correct sample space has $6\times 6 = 36$ outcomes.

### artifact_10 — amc12b_2003_p9 (AMC 2003) — **Option B**
**Flaw:** After correctly obtaining $\log_2(6/3)=\log_2(2)$, invents a rule "$\log_b(m/n)=\log_b(m)/\log_b(n)$." No such division rule exists for logarithms.

### artifact_11 — amc10a_2006_p18 (AMC 2006) — **Option C**
**Flaw:** States the divisor for repeated-letter arrangements is "$3!\cdot 2 = 12$" (describing $3!$ for A's and "2" for N's), misidentifying the factor for N as "2" rather than "$2!=2$." The formula description is wrong even though the number 12 happens to match $3!\cdot 2! = 12$.

### artifact_12 — amc12a_2006_p11 (AMC 2006) — **Option D**
**Flaw:** Claims "squaring preserves solutions," which is the opposite of truth. Squaring can introduce extraneous solutions (which is why a verification step was necessary), not preserve them exclusively.

### artifact_13 — amc10a_2007_p20 (AMC 2007) — **Option A**
**Flaw:** After showing $f(f(x))=x$ (true and valid), jumps to "therefore $f(f(f(x)))=x$ iff $f(x)=x$" without establishing that this equivalence holds — it does hold here, but the step does not show there are no additional solutions from a different reduction path; the equivalence is asserted, not proved.

### artifact_14 — amc12a_2008_p11 (AMC 2008) — **Option B**
**Flaw:** States $|z_1\cdot z_2|=|z_1|+|z_2|$ (addition). The correct rule is $|z_1\cdot z_2|=|z_1|\cdot|z_2|$ (multiplication). The addition formula belongs to the triangle inequality for sums, not products.

### artifact_15 — amc10b_2009_p15 (AMC 2009) — **Option C**
**Flaw:** In the similar-triangle argument for the altitude to the hypotenuse, writes the proportion as $AD/AC = AB/BC$. The correct corresponding proportion from $\triangle ABD \sim \triangle ABC$ is $AD/AB = AB/BC$ (altitude = $AB^2/BC$). The wrong proportion gives the right numerical answer ($12/5$) coincidentally.

### artifact_16 — amc12a_2009_p11 (AMC 2009) — **Option D**
**Flaw:** Misapplies Vieta's product formula by writing $(-1)^n\cdot(d/a)$ and obtaining $+6$, contradicting the explicit factorization $1\cdot(-3)\cdot 2=-6$. The correct formula gives $(-1)^3\cdot 6 = -6$.

### artifact_17 — imo_1977_p5 (IMO 1977) — **Option A**
**Flaw:** Claims a "contradiction" by substituting $n=0$ into a functional equation defined on $\mathbb{N}=\{1,2,\ldots\}$. Substituting an out-of-domain value does not produce a logical contradiction — it simply doesn't apply. A valid non-existence proof requires a parity argument.

### artifact_18 — imo_1988_p6 (IMO 1988) — **Option B**
**Flaw:** Invokes minimality against the companion pair $(a',b)$ before verifying that $(a',b)$ is a valid pair achieving the same ratio $k$. Using an unverified competitor in a minimality argument is the first logical gap.

### artifact_19 — imo_1990_p3 (IMO 1990) — **Option C**
**Flaw:** Dismisses the composite-$n$ case with "by a careful order argument" that is never supplied. This leaves a complete branch of the proof unjustified, constituting the first unproven claim.

### artifact_20 — imo_2001_p2 (IMO 2001) — **Option D**
**Flaw:** Claims $\sum \frac{a}{a+2b+2c}=1$ as a "Nesbitt-type identity." This is false: for $a=b=c=1$, the sum is $3/5\neq 1$. The "Nesbitt-type" label is invoked to cover an identity that does not hold.

### artifact_21 — imo_2003_p2 (IMO 2003) — **Option A**
**Flaw:** Performs a descent using the Vieta companion pair $(a',b)$ without first verifying that $(a',b)$ achieves the same ratio $k$, i.e., without showing $a'^2/(2a'b^2-b^3+1)=k$. Invoking minimality against an unverified pair is the first gap.

### artifact_22 — imo_2006_p1 (IMO 2006) — **Option B**
**Flaw:** Claims the locus of $P$ satisfying $\angle PBA+\angle PCA=\text{const}$ is a circle through $B,C$ "by the inscribed angle theorem." The inscribed angle theorem characterizes a fixed single angle $\angle BPC$, not a sum of two angles at distinct vertices.

### artifact_23 — imo_2019_p2 (IMO 2019) — **Option C**
**Flaw:** Introduces the substitution $b=a^2$ as "yielding a key constraint" but never extracts any constraint from it; the resulting divisibility condition $a+f(a^2)\mid a^2(1+f(a))$ is stated but unused. The step misrepresents a dead-end substitution as a structural result.

### artifact_24 — imo_2020_p1 (IMO 2020) — **Option D**
**Flaw:** Introduces an out-of-scope "general case" for $a_0>1$ and asserts without proof that the doubly-exponential sequence satisfies the gap-between-squares property. Both the scope extension and the unverified growth estimate constitute the first invalid reasoning after Steps 1–3 which already complete the proof.

### artifact_25 — mathd_algebra_116 (MATH 2020) — **Option A**
**Flaw:** Uses the incorrect formula $(a+b)^2=a^2+b^2$, omitting the cross term $2ab$. The correct expansion is $(a+b)^2=a^2+2ab+b^2$.

### artifact_26 — mathd_numbertheory_300 (MATH 2020) — **Option B**
**Flaw:** Computes the modular inverse $3^{-1}\equiv 4\pmod{11}$ when the goal is to evaluate $3\times(\text{known value})$ — no inverse is needed. Invoking an irrelevant algebraic operation as the first action of the step is the first invalid move.

### artifact_27 — mathd_algebra_459 (MATH 2020) — **Option C**
**Flaw:** Claims $\sqrt{4}=\pm 2$ and accepts $x=-1$ as a solution because $-2$ is "a valid square root." The principal square root $\sqrt{\cdot}$ is non-negative by definition; $\sqrt{4}=2$, never $-2$.

### artifact_28 — mathd_numbertheory_495 (MATH 2020) — **Option D**
**Flaw:** Steps 1–3 correctly enumerate **ordered** pairs (tens digit $a$, units digit $b$), giving 9 distinct numbers. Step 4 re-treats them as **unordered** pairs, double-counting each asymmetric pair and arriving at a spurious total of 17. Numbers like 19 and 91 are already both counted as separate ordered pairs; no additional doubling applies.

---

## Summary Table

| Artifact | Competition | Year | Correct Option | Flaw Type |
|---|---|---|---|---|
| 01 | AIME | 1983 | **A** | Wrong theorem (mean vs median) |
| 02 | AIME | 1984 | **B** | Unjustified symmetry assumption |
| 03 | AIME | 1985 | **C** | Inclusion-exclusion sign error |
| 04 | AIME | 1986 | **D** | False convergence regime claimed |
| 05 | AIME | 1987 | **A** | FLT applied to composite modulus |
| 06 | AIME | 1988 | **B** | Quadratic root sign confusion |
| 07 | AIME | 1989 | **C** | Wrong counting domain (10 instead of 8) |
| 08 | AIME | 1990 | **D** | Fabricated theorem overrides correct period |
| 09 | AMC | 2002 | **A** | Wrong sample space size (7 not 6) |
| 10 | AMC | 2003 | **B** | Nonexistent log division rule |
| 11 | AMC | 2006 | **C** | Wrong formula description for repeated letters |
| 12 | AMC | 2006 | **D** | Squaring "preserves" (should: may introduce) solutions |
| 13 | AMC | 2007 | **A** | Equivalence asserted without proof |
| 14 | AMC | 2008 | **B** | Modulus addition rule (should be multiplication) |
| 15 | AMC | 2009 | **C** | Wrong similar-triangle correspondence |
| 16 | AMC | 2009 | **D** | Vieta product formula sign error |
| 17 | IMO | 1977 | **A** | Out-of-domain substitution claimed as contradiction |
| 18 | IMO | 1988 | **B** | Minimality invoked before companion pair verified |
| 19 | IMO | 1990 | **C** | Composite case skipped without proof |
| 20 | IMO | 2001 | **D** | False Nesbitt-type identity asserted |
| 21 | IMO | 2003 | **A** | Descent without companion-pair verification |
| 22 | IMO | 2006 | **B** | Inscribed angle theorem misapplied to sum |
| 23 | IMO | 2019 | **C** | Dead-end substitution presented as key constraint |
| 24 | IMO | 2020 | **D** | Out-of-scope general case with unverified estimate |
| 25 | MATH | 2020 | **A** | Missing cross term in binomial expansion |
| 26 | MATH | 2020 | **B** | Irrelevant modular inverse introduced |
| 27 | MATH | 2020 | **C** | Principal square root sign error |
| 28 | MATH | 2020 | **D** | Ordered pairs re-treated as unordered (spurious ×2 doubling) |
