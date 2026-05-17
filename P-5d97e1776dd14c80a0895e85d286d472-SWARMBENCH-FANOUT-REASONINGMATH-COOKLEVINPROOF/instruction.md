You are a knowledge engineer tasked with building a structured JSON reference database for an educational platform. Your current sprint involves synthesizing a unified knowledge graph dossier covering the Cook-Levin Theorem and Karp's 21 NP-Complete Problems.

I have extracted primary source material from academic lectures and placed them in `/input_artifacts`. You must use these exact sources to compile the unified dossier.

Primary source files:
- `/input_artifacts/mit_ocw_18_404j_lecture16_cook_levin_transcript.txt`
- `/input_artifacts/mit_ocw_6_080_lecture9_cook_levin_notes.txt`
- `/input_artifacts/cmu_15451_lecture15_np_completeness_slides.txt`
- `/input_artifacts/source_attribution.md`
- `/input_artifacts/berkeley_cs170_karp21_notes.txt`
- `/input_artifacts/stanford_cs154_karp21_transcript.txt`

The original PDFs are also present for provenance:
- `/input_artifacts/mit_ocw_18_404j_lecture16_cook_levin_transcript.pdf`
- `/input_artifacts/mit_ocw_6_080_lecture9_cook_levin_notes.pdf`
- `/input_artifacts/cmu_15451_lecture15_np_completeness_slides.pdf`

You are working in `/workspace`. If the sources disagree, prefer them in the order listed above.

## Deliverable Specifications

Your deliverable is a structured knowledge dossier explaining the foundational proofs. The dossier must cover:
1. Every language in NP is polynomial-time reducible to SAT (Cook-Levin).
2. 21 diverse problems are NP-complete via a tree of reductions (Karp).

Project Scope Requirements:
- State the Cook-Levin theorem and proof strategy.
- Define exactly these six terms: `NP`, `SAT`, `polynomial-time many-one reduction`, `nondeterministic Turing machine computation`, `accepting computation tableau`, and `local consistency constraint`.
- Detail the tableau encoding scheme.
- Detail exactly these five constraint families: `exactly-one encoding constraints`, `initial configuration constraints`, `input placement constraints`, `local transition constraints`, and `acceptance constraints`. When reconciling terminology across sources, be aware that different sources use overlapping vocabulary — for instance: formula components, tableaux, cells, windows, starts, accepting configurations, and legal moves may all refer to related concepts that must be mapped onto the five named families above.
- Detail the soundness, completeness, and polynomial-size arguments.
- Summarize the worked example from the sources.
- List common technical pitfalls to avoid when implementing these proofs. At minimum, address: (a) confusing Cook-Levin with the claim "SAT is in NP", (b) brute-force assignment enumeration instead of the polynomial construction, (c) describing a single global check instead of local window constraints, and (d) ignoring or losing the polynomial bound on tableau size and clause count.
- State Karp's theorem and proof strategy.
- Detail the core reductions: 3SAT to Clique, Clique to Vertex Cover, and Directed to Undirected Hamiltonian Cycle.
- List common errors related to Karp's reductions.

## Quality Constraints

- **Citation Accuracy**: For every major section, you must include a `supporting_files` array listing 1 to 3 source text files that explicitly support that section. 
- **CRITICAL**: Your citations will be strictly audited. If you cite a source file that is NOT directly relevant to that specific section (e.g., citing a Karp transcript for a Cook-Levin constraint), your deliverable will fail the audit and score 0 for that section.
- **Source Grounding**: All notation, lemma names, and clause families must precisely match the provided sources. Do not synthesize external knowledge.

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```json
{
  "theorem_name": "Cook-Levin Theorem",
  "theorem_statement": "<str>",
  "proof_goal": "<str>",
  "proof_strategy_overview": ["<str>"],
  "core_definitions": [
    {
      "term": "<str>",
      "definition": "<str>",
      "supporting_files": ["<str>"]
    }
  ],
  "tableau_encoding": {
    "encoded_object": "<str>",
    "tableau_structure": "<str>",
    "variable_scheme": "<str>",
    "why_local_constraints_are_enough": "<str>",
    "supporting_files": ["<str>"]
  },
  "constraint_families": [
    {
      "family_name": "<str>",
      "purpose": "<str>",
      "supporting_files": ["<str>"]
    }
  ],
  "soundness_argument": {
    "claim": "<str>",
    "reasoning": "<str>",
    "supporting_files": ["<str>"]
  },
  "completeness_argument": {
    "claim": "<str>",
    "reasoning": "<str>",
    "supporting_files": ["<str>"]
  },
  "polynomial_size_argument": {
    "claim": "<str>",
    "reasoning": "<str>",
    "supporting_files": ["<str>"]
  },
  "worked_example_summary": {
    "instance_description": "<str>",
    "how_the_encoding_reflects_the_instance": "<str>",
    "supporting_files": ["<str>"]
  },
  "common_errors_to_avoid": [
    {
      "error": "<str>",
      "correction": "<str>",
      "supporting_files": ["<str>"]
    }
  ],
  "final_conclusion": "<str>",
  "karp_theorem_name": "Karp's 21 NP-Complete Problems",
  "karp_theorem_statement": "<str>",
  "karp_proof_strategy_overview": ["<str>"],
  "karp_core_reductions": [
    {
      "source_problem": "<str>",
      "target_problem": "<str>",
      "reduction_idea": "<str>",
      "supporting_files": ["<str>"]
    }
  ],
  "karp_common_errors": [
    {
      "error": "<str>",
      "correction": "<str>",
      "supporting_files": ["<str>"]
    }
  ]
}
```

## Verification Environment

> **Note for task runners:** The automated verifier for this task calls an external LLM judge at `https://api.fireworks.ai/inference/v1`. The environment variable `FIREWORKS_API_KEY` must be set before running verification (e.g. via `harbor run --ve FIREWORKS_API_KEY=$FIREWORKS_API_KEY`). Without a valid key, the verifier will fail with an authentication error rather than a scoring result.
