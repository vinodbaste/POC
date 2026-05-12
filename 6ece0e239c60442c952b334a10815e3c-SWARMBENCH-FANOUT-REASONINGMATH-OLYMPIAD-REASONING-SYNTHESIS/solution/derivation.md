# Oracle Derivation

Dataset source:
https://huggingface.co/datasets/EleutherAI/hendrycks_math

Full training split used across all 5 domains:
- algebra:                  1744 problems, 834 hard (Level 4+5) = 47.8%
- geometry:                 870 problems,  598 hard = 68.7% — HARDEST domain
- counting_and_probability: 771 problems,  442 hard = 57.3%
- number_theory:            869 problems,  500 hard = 57.5%
- precalculus:              746 problems,  352 hard = 47.2%
- Total:                    5000 problems, ~4.3 MB, ~1.1M tokens

---

# Difficulty Ordering (from computed statistics)

Ranked by hard-problem rate (Level 4 + Level 5):
1. geometry (68.7%) — Level 5 alone = 421/870 = 48.4%, extreme skew
2. number_theory (57.5%) — Level 5 = 313/869 = 36%
3. counting_and_probability (57.3%) — Level 5 = 276/771 = 35.8%
4. algebra (47.8%) — largest dataset, balanced distribution across Level 3-5
5. precalculus (47.2%) — most balanced distribution, Level 4-5 nearly equal (175+177)

---

# Domain-Specific Observations

## Geometry (870 problems, 68.7% hard)

Dominant patterns in solutions:
- Auxiliary line/circle/point constructions appear in the majority of Level 4-5 solutions
- Angle chasing and similar triangle identification drive Level 3-4
- Projective and cross-ratio arguments appear at Level 5 alongside advanced construction chains

The Level 5 concentration (421/870 = 48.4%) is the highest across all domains,
confirming that multi-step auxiliary construction problems define the hardest geometry subclass.

Oracle strategies derived: Auxiliary Construction, Geometric Transformation

---

## Number Theory (869 problems, 57.5% hard)

Dominant patterns:
- Modular arithmetic constraints appear in nearly all Level 3-5 solutions
- Level 5 problems (313 = 36%) require multi-modulus non-constructive arguments
- Divisibility analysis and prime factorization underlie most constraint chains

The rising difficulty curve (Level 3: 191, Level 4: 187, Level 5: 313) indicates
that the hardest problems require qualitatively different (non-constructive) techniques.

Oracle strategies derived: Modular Arithmetic and Residue Analysis, Infinite Descent

---

## Counting and Probability (771 problems, 57.3% hard)

Dominant patterns:
- Recursive state modeling appears in the majority of Level 4-5 solutions
- Inclusion-exclusion and complementary counting at Level 3-4
- Level 5 problems (276 = 35.8%) require identifying minimal sufficient state space

Oracle strategies derived: State-Space Recursion, Inclusion-Exclusion

---

## Algebra (1744 problems, 47.8% hard)

Dominant patterns:
- Symbolic manipulation and substitution chains throughout all levels
- Polynomial factoring with non-obvious substitutions at Level 4-5
- Level 5 (436 = 25%) requires creative substitution identification

Oracle strategies derived: Symbolic Manipulation, Polynomial Factoring with Substitution

---

## Precalculus (746 problems, 47.2% hard)

Dominant patterns:
- Analytic function decomposition across trigonometric, complex, and vector domains
- Most balanced level distribution (Level 3-5 nearly uniform: 168/175/177)
- Level 5 requires chaining multiple function properties with domain tracking

Oracle strategies derived: Analytic Function Decomposition, Trigonometric Composition Tracking

---

# Cross-Domain Synthesis

Difficulty ranking: geometry (68.7%) >> number_theory (57.5%) ≈ counting (57.3%) >> algebra (47.8%) ≈ precalculus (47.2%)

Geometry's dominance reflects that spatial reasoning combined with multi-step auxiliary
construction is structurally harder than any other proof pattern in this dataset.

Transferable techniques:
- Auxiliary construction in geometry → strategic substitution in algebra
- Modular arithmetic in number_theory → inclusion-exclusion bounds in counting
- Recursive decomposition in counting → inductive structure in algebra
