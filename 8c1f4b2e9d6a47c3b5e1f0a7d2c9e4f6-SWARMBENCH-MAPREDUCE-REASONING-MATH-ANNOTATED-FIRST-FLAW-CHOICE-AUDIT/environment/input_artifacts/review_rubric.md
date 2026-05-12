# Review Rubric

You are validating multiple-choice conversions of human flaw annotations from incorrect olympiad proof attempts.

For each artifact:
- Read the problem and the candidate proof.
- Inspect the four candidate excerpts in proof order.
- Exactly one option contains the marked first unrecoverable flaw.
- Return the chosen option letter and the flaw type for each artifact.
- Do not invent new options or rewrite the excerpt text.

The reducer must also compute exact aggregate counts for each option letter, competition, and year.

## Option Selection Methodology

Read the **Full Candidate Proof** section to establish chronological step order, then map each option label (A–D) to its proof position. The earliest step that introduces an error from which the proof cannot recover is the correct answer. Option labels are shuffled and do not reflect proof sequence — the correct answer may be any letter.

## Flaw Type Classification Methodology

After identifying the flawed step, classify its flaw type using the following decision procedure in order. **Do not skip ahead.** A common mistake is jumping straight to `algebraic_error` or `false_assumption` without first checking whether a named theorem is being misapplied.

**Step 1 — Check for misapplied_theorem:**
Does the proof invoke a named theorem, lemma, formula, or known result? If yes, verify that every precondition of that theorem is explicitly established in the proof for this specific problem. If any precondition is absent, unverified, or violated, classify as `misapplied_theorem`. Examples: applying a triangle inequality without confirming the triangle is non-degenerate; using a limit theorem without checking the convergence condition; applying AM-GM without verifying all terms are non-negative.

**Step 2 — Check for false_assumption:**
Does the proof introduce an explicit premise (e.g., "Assume X", "Let X = Y", "WLOG suppose", "Since X clearly holds") that is actually false or unjustified for the given problem? If the premise is stated as true but does not hold in the given context, classify as `false_assumption`. Examples: assuming a function is injective when it is not; assuming two quantities are equal when they differ; assuming a set is non-empty when it may be empty.

**Step 3 — Check for scope_violation:**
Does the proof apply a result, formula, or conclusion that was established only for a restricted case (e.g., a specific value, a subset, a special configuration) to a broader or different context where it was not proved? Classify as `scope_violation`. Examples: using a result proved for integers to conclude something about reals; applying a lemma proved for acute triangles to obtuse triangles; extending a finite-case result to the infinite case without justification.

**Step 4 — Check for algebraic_error:**
Does the proof perform a computation, arithmetic operation, algebraic manipulation, or combinatorial count where the result is numerically or symbolically incorrect? Classify as `algebraic_error`. Examples: incorrect expansion of a binomial; wrong simplification of a fraction; sign error in a determinant; incorrect count of cases.

**Step 5 — Default to unjustified_claim:**
If none of the above apply but the flawed step asserts a conclusion without any supporting derivation, citation, or proof — stated as if obvious when it is not — classify as `unjustified_claim`. Examples: "it follows that X ≥ Y" with no calculation; "clearly P implies Q" where the implication is non-trivial and unproved; asserting an equality holds without showing the algebra.

Apply exactly one classification per artifact. Use the decision procedure in order (misapplied_theorem → false_assumption → scope_violation → algebraic_error → unjustified_claim) and stop at the first matching category.

## Worked Examples

The five examples below illustrate exactly one flaw type each, in the same style as the artifacts you will audit. Use them as pattern-match references.

### Example A — misapplied_theorem

> *"By Fermat's Little Theorem applied to p = 7 and a = 14, we have \(a^{p-1} = 14^6 \equiv 1 \pmod{7}\)."*

Classification: **misapplied_theorem**. Fermat's Little Theorem requires \(\gcd(a, p) = 1\). Here \(a = 14 = 2 \cdot 7\) so \(7 \mid a\) and the precondition fails. The theorem's name is invoked but the precondition is not satisfied for this problem. Step 1 matches; stop.

### Example B — false_assumption

> *"WLOG assume that the function \(f\) is monotonically increasing on \([0, 1]\). Then \(f(0) \leq f(1)\) gives the desired inequality directly."*

Classification: **false_assumption**. The problem did not state monotonicity. The "WLOG" hides an unjustified premise that constrains the function class to a strict subset. The conclusion follows from a premise that does not hold in general for the problem as stated. Step 2 matches; stop. (Step 1 did NOT match because no named theorem was cited.)

### Example C — scope_violation

> *"We proved above that the inequality holds for all positive integers \(n \geq 2\). Therefore it holds for all positive reals \(x \geq 2\) by the same argument."*

Classification: **scope_violation**. A result was established only for the discrete integer case but is being applied to the broader continuous real case. The proof asserts "by the same argument" without showing the integer-specific reasoning generalizes. Step 3 matches; stop. (Steps 1 and 2 did NOT match — no theorem is named, no false premise is introduced; the issue is purely about the result's domain of validity.)

### Example D — algebraic_error

> *"We have \((x + 1)^2 = x^2 + 1\). Substituting \(x = 3\): \(16 = 10\), so the equation is consistent."*

Classification: **algebraic_error**. The binomial expansion is wrong: \((x + 1)^2 = x^2 + 2x + 1\), not \(x^2 + 1\). The arithmetic at \(x = 3\) is also wrong (\(4^2 = 16\) is correct, but \(3^2 + 1 = 10\) does not equal \(16\); the "consistency" claim relies on the bad expansion). Step 4 matches; stop. (Steps 1, 2, 3 did NOT match — no theorem misapplied, no false premise introduced, no scope extension; just bad algebra.)

### Example E — unjustified_claim

> *"Clearly the polynomial \(p(x) = x^4 + x^3 + x^2 + x + 1\) has no real roots. The result follows."*

Classification: **unjustified_claim**. The "Clearly … no real roots" assertion is non-trivial and is presented without proof, derivation, or citation. (One could prove it via \(p(x) = \frac{x^5 - 1}{x - 1}\) for \(x \neq 1\), or by computing the discriminant, or by AM-GM bounds — but the proof shows none of this.) Step 5 matches; stop. (Steps 1–4 did NOT match — no theorem invoked, no premise introduced, no scope extension, no arithmetic mistake; the issue is that an asserted fact is not justified.)

## Important reminders

- **Always start at Step 1.** Do not skip to Step 4 just because numbers appear in the proof.
- **Algebraic errors are not the default.** They require an actual numerical or symbolic computation that is wrong.
- **Unjustified claims are common.** When in doubt and Steps 1–4 do not clearly match, choose `unjustified_claim`.
- **Theorem invocations are common in olympiad proofs.** Phrases like "by Cauchy–Schwarz", "by the inscribed angle theorem", "by Pick's theorem", "by Fermat's Little Theorem" are theorem invocations — check the precondition first before classifying the error.
