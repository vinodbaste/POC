# Review Rubric

You are validating multiple-choice conversions of real human flaw annotations from the Open Proof Corpus.

For each artifact:
- Read the problem and the candidate proof.
- Inspect the four candidate excerpts in proof order.
- Exactly one option contains the human-marked first unrecoverable flaw.
- Return the chosen option letter and the flaw type for each artifact.
- Do not invent new options or rewrite the excerpt text.

The reducer must also compute exact aggregate counts for each option letter, competition, and year.

## Option Selection Methodology

Read the **Full Candidate Proof** section to establish chronological step order, then map each option label (A–D) to its proof position. The earliest step that introduces an error from which the proof cannot recover is the correct answer. Option labels are shuffled and do not reflect proof sequence — the correct answer may be any letter.

## Flaw Type Classification Methodology

After identifying the flawed step, classify its flaw type using the following decision procedure in order:

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
