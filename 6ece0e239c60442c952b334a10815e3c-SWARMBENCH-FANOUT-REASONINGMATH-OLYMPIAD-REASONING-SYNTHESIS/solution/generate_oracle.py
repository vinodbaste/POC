import json
import os
import collections

# Read actual input files to compute domain statistics
INPUT_DIR = "/input_artifacts"
if not os.path.exists(INPUT_DIR):
    INPUT_DIR = "environment/input_artifacts"

domains = [
    "algebra",
    "geometry",
    "counting_and_probability",
    "number_theory",
    "precalculus",
]

domain_statistics = {}
for domain in domains:
    path = os.path.join(INPUT_DIR, f"{domain}.jsonl")
    problems = [json.loads(line) for line in open(path)]
    level_counts = collections.Counter(p["level"] for p in problems)
    hard_count = level_counts.get("Level 4", 0) + level_counts.get("Level 5", 0)
    domain_statistics[domain] = {
        "total_problems": len(problems),
        "level_distribution": {
            "Level 1": level_counts.get("Level 1", 0),
            "Level 2": level_counts.get("Level 2", 0),
            "Level 3": level_counts.get("Level 3", 0),
            "Level 4": level_counts.get("Level 4", 0),
            "Level 5": level_counts.get("Level 5", 0),
        },
        "hard_problems_count": hard_count,
    }

oracle = {
    "domain_statistics": domain_statistics,

    "proof_strategy_taxonomy": [
        {
            "strategy": "Auxiliary Construction",
            "description": (
                f"Dominant in geometry ({domain_statistics['geometry']['hard_problems_count']}/"
                f"{domain_statistics['geometry']['total_problems']} = "
                f"{100*domain_statistics['geometry']['hard_problems_count']//domain_statistics['geometry']['total_problems']}% hard) "
                "— adding helper lines, circles, or points reveals hidden similarity or congruence. "
                "The extreme Level 5 skew confirms that multi-construction proofs define the hardest geometry subclass."
            )
        },
        {
            "strategy": "Modular Arithmetic and Residue Analysis",
            "description": (
                f"Core to number theory ({domain_statistics['number_theory']['hard_problems_count']}/"
                f"{domain_statistics['number_theory']['total_problems']} = "
                f"{100*domain_statistics['number_theory']['hard_problems_count']//domain_statistics['number_theory']['total_problems']}% hard) "
                "— constraint propagation through congruence classes. "
                "The high Level 5 count confirms that deep modular chains define the hardest subclass."
            )
        },
        {
            "strategy": "State-Space Recursion",
            "description": (
                f"Dominant in counting and probability ({domain_statistics['counting_and_probability']['hard_problems_count']}/"
                f"{domain_statistics['counting_and_probability']['total_problems']} = "
                f"{100*domain_statistics['counting_and_probability']['hard_problems_count']//domain_statistics['counting_and_probability']['total_problems']}% hard) "
                "— encoding combinatorial problems as recurrences over discrete states."
            )
        },
        {
            "strategy": "Symbolic Manipulation",
            "description": (
                f"Core to algebra ({domain_statistics['algebra']['hard_problems_count']}/"
                f"{domain_statistics['algebra']['total_problems']} = "
                f"{100*domain_statistics['algebra']['hard_problems_count']//domain_statistics['algebra']['total_problems']}% hard) "
                "— equation transformation, substitution, and polynomial factoring."
            )
        },
        {
            "strategy": "Analytic Function Decomposition",
            "description": (
                f"Defining for precalculus ({domain_statistics['precalculus']['hard_problems_count']}/"
                f"{domain_statistics['precalculus']['total_problems']} = "
                f"{100*domain_statistics['precalculus']['hard_problems_count']//domain_statistics['precalculus']['total_problems']}% hard) "
                "— chaining function properties across analytic transformations."
            )
        },
    ],

    "reasoning_style_comparison": {
        "algebra": (
            f"Algebra is the largest domain ({domain_statistics['algebra']['total_problems']} problems) "
            f"with {domain_statistics['algebra']['hard_problems_count']}/{domain_statistics['algebra']['total_problems']} = "
            f"{100*domain_statistics['algebra']['hard_problems_count']//domain_statistics['algebra']['total_problems']}% hard problems. "
            "Its balanced level distribution indicates that algebraic reasoning spans a wide difficulty range "
            "from direct formula application to multi-step symbolic transformation."
        ),
        "geometry": (
            f"Geometry has the highest hard-problem concentration: "
            f"{domain_statistics['geometry']['hard_problems_count']}/{domain_statistics['geometry']['total_problems']} = "
            f"{100*domain_statistics['geometry']['hard_problems_count']//domain_statistics['geometry']['total_problems']}% hard, "
            f"with Level 5 = {domain_statistics['geometry']['level_distribution']['Level 5']} problems "
            f"({100*domain_statistics['geometry']['level_distribution']['Level 5']//domain_statistics['geometry']['total_problems']}%). "
            "This extreme Level 5 skew confirms that multi-step auxiliary construction problems dominate the hardest subclass."
        ),
        "counting_and_probability": (
            f"Counting and probability ({domain_statistics['counting_and_probability']['total_problems']} problems, "
            f"{domain_statistics['counting_and_probability']['hard_problems_count']}/{domain_statistics['counting_and_probability']['total_problems']} = "
            f"{100*domain_statistics['counting_and_probability']['hard_problems_count']//domain_statistics['counting_and_probability']['total_problems']}% hard). "
            "Level 5 problems require recognizing the correct recursive state decomposition."
        ),
        "number_theory": (
            f"Number theory ({domain_statistics['number_theory']['total_problems']} problems, "
            f"{domain_statistics['number_theory']['hard_problems_count']}/{domain_statistics['number_theory']['total_problems']} = "
            f"{100*domain_statistics['number_theory']['hard_problems_count']//domain_statistics['number_theory']['total_problems']}% hard). "
            f"Level 5 = {domain_statistics['number_theory']['level_distribution']['Level 5']} problems "
            f"({100*domain_statistics['number_theory']['level_distribution']['Level 5']//domain_statistics['number_theory']['total_problems']}%). "
            "Modular arithmetic and divisibility analysis define the reasoning style; "
            "Level 5 requires multi-modulus non-constructive arguments."
        ),
        "precalculus": (
            f"Precalculus ({domain_statistics['precalculus']['total_problems']} problems, "
            f"{domain_statistics['precalculus']['hard_problems_count']}/{domain_statistics['precalculus']['total_problems']} = "
            f"{100*domain_statistics['precalculus']['hard_problems_count']//domain_statistics['precalculus']['total_problems']}% hard) "
            "has the most balanced level distribution. "
            "Level 5 problems require the deepest analytic function composition chains."
        ),
    },

    "most_subtle_reasoning_failure_modes": [
        (
            f"Misidentifying auxiliary construction targets in geometry — with "
            f"{domain_statistics['geometry']['level_distribution']['Level 5']} Level 5 problems "
            f"({100*domain_statistics['geometry']['level_distribution']['Level 5']//domain_statistics['geometry']['total_problems']}%), "
            "choosing the wrong helper element cascades through all subsequent similarity arguments"
        ),
        (
            f"Conflating modular reduction with non-constructive techniques in number theory — "
            f"the {domain_statistics['number_theory']['level_distribution']['Level 5']} Level 5 problems "
            f"({100*domain_statistics['number_theory']['level_distribution']['Level 5']//domain_statistics['number_theory']['total_problems']}%) "
            "require fundamentally different approaches from Level 3"
        ),
        (
            f"Missing the state-space structure in counting — "
            f"the Level 5 cluster ({domain_statistics['counting_and_probability']['level_distribution']['Level 5']} problems) "
            "requires recognizing the correct recursive decomposition, not just applying inclusion-exclusion"
        ),
        (
            f"Algebraic over-generalization across the {domain_statistics['algebra']['total_problems']}-problem algebra set — "
            "the large dataset's broad level range means techniques valid for Level 3 problems fail at Level 5"
        ),
        (
            f"Ignoring domain restrictions in precalculus function compositions — "
            f"errors in domain tracking appear across the balanced Level 4-5 distribution "
            f"({domain_statistics['precalculus']['level_distribution']['Level 4']}+"
            f"{domain_statistics['precalculus']['level_distribution']['Level 5']} problems)"
        ),
    ],

    "hardest_problem_families": [
        {
            "family": "Geometry Multi-Step Auxiliary Constructions",
            "reason": (
                f"Hardest domain by hard-problem rate: "
                f"{domain_statistics['geometry']['hard_problems_count']}/{domain_statistics['geometry']['total_problems']} = "
                f"{100*domain_statistics['geometry']['hard_problems_count']//domain_statistics['geometry']['total_problems']}% hard, "
                f"Level 5 = {domain_statistics['geometry']['level_distribution']['Level 5']} problems "
                f"({100*domain_statistics['geometry']['level_distribution']['Level 5']//domain_statistics['geometry']['total_problems']}%). "
                "No other domain approaches this Level 5 concentration."
            )
        },
        {
            "family": "Number Theory Deep Congruence Chains",
            "reason": (
                f"{domain_statistics['number_theory']['hard_problems_count']}/{domain_statistics['number_theory']['total_problems']} = "
                f"{100*domain_statistics['number_theory']['hard_problems_count']//domain_statistics['number_theory']['total_problems']}% hard, "
                f"Level 5 = {domain_statistics['number_theory']['level_distribution']['Level 5']} problems. "
                "The hardest problems require multi-modulus non-constructive arguments far beyond simple modular reduction."
            )
        },
        {
            "family": "Counting Level 5 State-Space Problems",
            "reason": (
                f"{domain_statistics['counting_and_probability']['hard_problems_count']}/{domain_statistics['counting_and_probability']['total_problems']} = "
                f"{100*domain_statistics['counting_and_probability']['hard_problems_count']//domain_statistics['counting_and_probability']['total_problems']}% hard, "
                f"Level 5 = {domain_statistics['counting_and_probability']['level_distribution']['Level 5']} problems. "
                "Identifying the minimal sufficient state is the key creative barrier."
            )
        },
    ],

    "top_proof_techniques": [
        {
            "technique": "Auxiliary Circle Construction (geometry)",
            "difficulty_reason": (
                f"Geometry Level 5 = {domain_statistics['geometry']['level_distribution']['Level 5']} problems "
                f"({100*domain_statistics['geometry']['level_distribution']['Level 5']//domain_statistics['geometry']['total_problems']}%); "
                "inscribed or circumscribed circles reveal hidden angle relationships."
            )
        },
        {
            "technique": "Multi-Modulus Congruence Chain (number theory)",
            "difficulty_reason": (
                f"Number theory Level 5 = {domain_statistics['number_theory']['level_distribution']['Level 5']} problems; "
                "building constraint chains across multiple non-coprime moduli."
            )
        },
        {
            "technique": "Similarity Ratio Propagation (geometry)",
            "difficulty_reason": "Core technique in geometry Level 3-4 — identifying nested similar triangles and propagating ratios requires careful vertex correspondence."
        },
        {
            "technique": "Recursive State Encoding (counting)",
            "difficulty_reason": (
                f"Counting Level 5 = {domain_statistics['counting_and_probability']['level_distribution']['Level 5']} problems; "
                "state identification is the hardest creative barrier."
            )
        },
        {
            "technique": "Polynomial Factoring with Substitution (algebra)",
            "difficulty_reason": (
                f"Algebra Level 5 = {domain_statistics['algebra']['level_distribution']['Level 5']} problems; "
                "identifying a non-obvious substitution before factoring is the key creative step."
            )
        },
        {
            "technique": "Inclusion-Exclusion with Overlapping Constraints (counting)",
            "difficulty_reason": (
                f"Counting Level 4 = {domain_statistics['counting_and_probability']['level_distribution']['Level 4']} problems; "
                "complexity grows combinatorially with the number of constraint intersections."
            )
        },
        {
            "technique": "Infinite Descent on Integer Solutions (number theory)",
            "difficulty_reason": "Appears in number theory Level 5 — constructing a strictly smaller solution from any assumed solution and verifying termination."
        },
        {
            "technique": "Trigonometric Composition Tracking (precalculus)",
            "difficulty_reason": (
                f"Precalculus Level 5 = {domain_statistics['precalculus']['level_distribution']['Level 5']} problems; "
                "periodicity creates multiple valid branches that must all be identified."
            )
        },
        {
            "technique": "Extremal Principle (algebra and geometry)",
            "difficulty_reason": (
                f"Appears at Level 4-5 across both algebra ({domain_statistics['algebra']['level_distribution']['Level 4']}+"
                f"{domain_statistics['algebra']['level_distribution']['Level 5']} problems) and geometry; "
                "requires identifying the optimal structure and proving the extremal property."
            )
        },
        {
            "technique": "Cross-Ratio and Projective Transformation (geometry)",
            "difficulty_reason": (
                f"Geometry Level 5 cluster ({domain_statistics['geometry']['level_distribution']['Level 5']} problems); "
                "reduces complex angle/ratio problems to invariant computation."
            )
        },
    ],

    "cross_domain_reasoning_transfer": (
        f"Ranked by hard-problem rate: "
        f"geometry ({100*domain_statistics['geometry']['hard_problems_count']//domain_statistics['geometry']['total_problems']}%) "
        f"> number_theory ({100*domain_statistics['number_theory']['hard_problems_count']//domain_statistics['number_theory']['total_problems']}%) "
        f"> counting ({100*domain_statistics['counting_and_probability']['hard_problems_count']//domain_statistics['counting_and_probability']['total_problems']}%) "
        f"> algebra ({100*domain_statistics['algebra']['hard_problems_count']//domain_statistics['algebra']['total_problems']}%) "
        f"> precalculus ({100*domain_statistics['precalculus']['hard_problems_count']//domain_statistics['precalculus']['total_problems']}%). "
        f"Geometry's dominance (Level 5 = {domain_statistics['geometry']['level_distribution']['Level 5']}/{domain_statistics['geometry']['total_problems']} = "
        f"{100*domain_statistics['geometry']['level_distribution']['Level 5']//domain_statistics['geometry']['total_problems']}%) "
        "reflects that spatial reasoning combined with multi-step construction is structurally harder than any other proof pattern. "
        "Transferable techniques: auxiliary construction in geometry transfers to strategic substitution in algebra; "
        "modular arithmetic in number_theory underlies inclusion-exclusion bounds in counting; "
        "recursive decomposition in counting mirrors inductive structure in algebra."
    ),
}

output_path = (
    "/solution/oracle.json"
    if os.path.exists("/solution")
    else "solution/oracle.json"
)

with open(output_path, "w") as f:
    json.dump(oracle, f, indent=2)
