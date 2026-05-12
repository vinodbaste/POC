# Audit Rubric — Olympiad Solution Auditor

You are auditing the rigor of published olympiad solutions. Each solution has been tagged with a numbered list of "key claims" `[C1]`, `[C2]`, ... — the load-bearing assertions the proof rests on.

For every claim tag in an artifact, you must produce exactly one of the three status values: `verified`, `unjustified`, or `incorrect`.

## Claim-status decision procedure (apply in order, stop at first match)

**Step 1 — `verified`:**
Does the surrounding solution text contain a derivation that supports the claim? A derivation can be:
- explicit algebra/geometry leading to the claim,
- citation of a named theorem WHERE the precondition is verified earlier in the solution, OR
- a sub-argument with all logical steps spelled out within the solution.
If yes, classify as `verified`.

**Step 2 — `unjustified`:**
Is the claim asserted without a supporting derivation — stated as if obvious when it is not? Phrases like "clearly", "obviously", "by symmetry" (when the symmetry is non-trivial), or "it is easy to see" without follow-up reasoning all signal an unjustified claim. If yes, classify as `unjustified`.

**Step 3 — `incorrect`:**
Can you identify a concrete logical or computational error that makes the claim false? Examples: a sign error in a derived equation, a misuse of a theorem (precondition unverified AND consequence is wrong), a counterexample to the stated claim. If yes, classify as `incorrect`.

Apply exactly one status per claim. If multiple steps match, use the FIRST matching step.

## Central technique taxonomy

Each artifact must be classified with exactly one of:

| Technique | When to use |
|---|---|
| `algebraic_manipulation` | Solutions whose core move is algebraic rewriting, substitution, or symbolic identity work |
| `combinatorial_counting` | Solutions that count cases, configurations, or arrangements as the central insight |
| `induction` | Solutions whose central argument is induction on a parameter |
| `inequality_application` | Solutions that hinge on applying a named inequality (AM-GM, Cauchy-Schwarz, Jensen, etc.) |
| `modular_arithmetic` | Solutions whose key step works modulo a prime or modulus |
| `geometric_construction` | Solutions whose central insight is an auxiliary construction (drawing a line, identifying a circle, etc.) |
| `extremal_principle` | Solutions that pick the minimum/maximum element of a set as the core argument |
| `invariant_or_monovariant` | Solutions identifying a quantity preserved (invariant) or strictly decreasing (monovariant) under operations |
| `generating_function` | Solutions using formal power series or generating functions |
| `proof_by_contradiction` | Solutions whose central structure is assuming the negation and deriving an impossibility |

If a solution uses multiple techniques, pick the one most load-bearing for the central insight (not the routine bookkeeping).

## Rigor score (1 to 5)

| Score | Meaning |
|---|---|
| 5 | Every claim verified; no hand-waving; all theorem preconditions checked |
| 4 | At most 1 unjustified claim; no incorrect claims |
| 3 | 2-3 unjustified claims; no incorrect claims |
| 2 | 4 or more unjustified claims OR exactly 1 incorrect claim |
| 1 | Multiple incorrect claims or pervasive hand-waving |

Compute the rigor score AFTER classifying every claim in the solution.
