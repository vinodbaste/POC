#!/bin/bash
set -euo pipefail

python3 /solution/generate_oracle.py

cp /solution/oracle.json /logs/agent/output.json

cat > /logs/agent/oracle.txt << 'EOF'
Oracle Solution — Mathematical Reasoning Synthesis
Full Hendrycks MATH dataset: 4,000 problems across 5 domains (~4.3 MB, ~1.1M tokens)
  algebra: 1744 problems | geometry: 870 | counting_and_probability: 771 | number_theory: 869 | precalculus: 746

DIFFICULTY RANKING (by hard-problem rate, Level 4+5):
  1. geometry:                 598/870  = 68.7% hard  ← HARDEST, Level 5 = 421 (48.4%)
  2. number_theory:            500/869  = 57.5% hard
  3. counting_and_probability: 442/771  = 57.3% hard
  4. algebra:                  834/1744 = 47.8% hard  (largest dataset)
  5. precalculus:              352/746  = 47.2% hard  ← most balanced distribution

PROOF STRATEGY TAXONOMY (5 domain-specific strategies):
1. Auxiliary Construction (geometry, 68.7% hard) — multi-step helper elements define the hardest subclass
2. Modular Arithmetic and Residue Analysis (number_theory, 57.5% hard) — deep congruence chains
3. State-Space Recursion (counting, 57.3% hard) — recursive state encoding
4. Symbolic Manipulation (algebra, 47.8% hard) — equation transformation and substitution
5. Analytic Function Decomposition (precalculus, 47.2% hard) — function composition chains

HARDEST PROBLEM FAMILIES:
1. Geometry Multi-Step Auxiliary Constructions — 68.7% hard, Level 5 = 421/870 = 48.4%
2. Number Theory Deep Congruence Chains — 57.5% hard, Level 5 = 313/869 = 36%
3. Counting Level 5 State-Space Problems — 57.3% hard, Level 5 = 276/771 = 35.8%

TOP PROOF TECHNIQUES (10, domain-attributed):
1. Auxiliary Circle Construction (geometry) — Level 5 = 48.4% of geometry
2. Multi-Modulus Congruence Chain (number_theory) — Level 5 = 36%
3. Similarity Ratio Propagation (geometry) — Level 3-4 core
4. Recursive State Encoding (counting) — Level 5 = 35.8%
5. Polynomial Factoring with Substitution (algebra) — Level 5 = 436/1744 = 25%
6. Inclusion-Exclusion with Overlapping Constraints (counting) — Level 4 = 166
7. Infinite Descent on Integer Solutions (number_theory) — Level 5
8. Trigonometric Composition Tracking (precalculus) — Level 5 = 177
9. Extremal Principle (algebra/geometry) — Level 4-5 across both
10. Cross-Ratio and Projective Transformation (geometry) — Level 5 = 421

CROSS-DOMAIN TRANSFER:
geometry (68.7%) >> number_theory (57.5%) > counting (57.3%) > algebra (47.8%) > precalculus (47.2%)
EOF