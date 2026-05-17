#!/usr/bin/env python3
"""
LLM Judge for Cook-Levin Theorem proof dossier task.

Scores the agent's structured JSON output against oracle.json field by field
using Kimi K2.5 via the Fireworks API. Returns a reward in [0.0, 1.0].

Usage (called by test.sh):
    python3 /tests/judge.py \
        --agent-output /logs/agent/output.json \
        --oracle /tests/oracle.json \
        --reward-out /logs/verifier/reward.json
"""

import argparse
import json
import os
import re
import sys
import time

from openai import OpenAI


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_json(text: str) -> str:
    """Extract the first JSON object from a judge response.

    Kimi sometimes adds explanatory prose before the requested JSON. The judge
    should not turn an otherwise valid score into 0 just because of that wrapper.
    """
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()

    decoder = json.JSONDecoder()
    for json_start in (m.start() for m in re.finditer(r"{", text)):
        try:
            _, json_end = decoder.raw_decode(text[json_start:])
        except json.JSONDecodeError:
            continue
        return text[json_start:json_start + json_end]

    return text


def write_failure(reward_out: str, justification_path: str, reason: str) -> None:
    """Write reward=0.0 and a short justification for hard failures."""
    json.dump({"reward": 0.0}, open(reward_out, "w"))
    with open(justification_path, "w") as f:
        f.write(f"Score: 0.0\n\n{reason}")


def call_llm_judge(client: OpenAI, messages: list[dict], attempts: int = 6) -> dict:
    """Call the LLM judge with bounded retries for network and JSON issues."""
    last_error: Exception | None = None
    last_raw = ""

    for attempt in range(1, attempts + 1):
        for use_json_mode in (True, False):
            try:
                kwargs = {
                    "model": "accounts/fireworks/models/kimi-k2p5",
                    "messages": messages,
                    "temperature": 0,
                    "max_tokens": 2048,
                }
                if use_json_mode:
                    kwargs["response_format"] = {"type": "json_object"}

                response = client.chat.completions.create(**kwargs)
                last_raw = response.choices[0].message.content or ""
                return json.loads(extract_json(last_raw))
            except Exception as exc:
                last_error = exc

        if attempt < attempts:
            time.sleep(min(5 * attempt, 30))

    raise RuntimeError(
        f"Judge failed after {attempts} attempts. Last error: {last_error}. "
        f"Last raw response: {last_raw[:300]}"
    )


# ---------------------------------------------------------------------------
# Scoring dimensions
# The oracle has these top-level keys; each maps to a human-readable label
# and the sub-fields we care about most.  The LLM judge is asked to score
# each dimension independently.
# ---------------------------------------------------------------------------

DIMENSIONS = [
    {
        "key": "theorem_name",
        "label": "Theorem Name",
        "description": (
            "The field must equal exactly 'Cook-Levin Theorem'. "
            "Score 1 if correct, 0 otherwise."
        ),
    },
    {
        "key": "theorem_statement",
        "label": "Theorem Statement",
        "description": (
            "Must convey: every language in NP has a polynomial-time many-one "
            "reduction to SAT (i.e., a poly-time mapping f such that x ∈ L iff "
            "f(x) is satisfiable). Score 1 for full correctness, 0.5 if partially "
            "correct (e.g., missing the polynomial-time constraint or the iff), "
            "0 if wrong or missing."
        ),
    },
    {
        "key": "proof_goal",
        "label": "Proof Goal",
        "description": (
            "Must state: given an NP language and its polynomial-time NTM, "
            "construct a SAT instance that is satisfiable iff the machine accepts "
            "the input. Score 1 for full correctness, 0.5 if the NTM or "
            "polynomial-time element is mentioned but the iff is unclear, 0 if wrong."
        ),
    },
    {
        "key": "proof_strategy_overview",
        "label": "Proof Strategy Overview",
        "description": (
            "Must be a non-empty list of strings covering the key steps: "
            "(1) fix an NP language and its NTM, (2) encode an accepting run as a "
            "bounded tableau, (3) introduce Boolean variables for the tableau, "
            "(4) build constraint families, (5) establish soundness/completeness, "
            "(6) argue polynomial size. Score 1 if all major steps appear, 0.5 if "
            "two or more are missing, 0 if the overview is absent or irrelevant."
        ),
    },
    {
        "key": "core_definitions",
        "label": "Core Definitions",
        "description": (
            "Must be a list containing definitions for at least: NP, SAT, "
            "polynomial-time many-one reduction, nondeterministic Turing machine "
            "computation, accepting computation tableau, and local consistency "
            "constraint. Each entry needs a 'term', 'definition', and "
            "'supporting_files' array pointing to valid packet paths. Score 1 if "
            "all six are present with correct definitions and valid file references, "
            "deduct 0.1 per missing definition, 0.05 per missing/invalid file "
            "reference. Minimum 0."
        ),
    },
    {
        "key": "tableau_encoding",
        "label": "Tableau Encoding",
        "description": (
            "Must cover: what is encoded (a polynomially bounded accepting computation), "
            "the grid structure (rows = steps, columns = positions), the variable scheme "
            "(Booleans for symbol/state/head at each cell), and why local constraints "
            "suffice (constant-size neighborhoods). Must include a 'supporting_files' "
            "array with valid packet paths. Score 1 if all four sub-fields are correct "
            "and well-justified, 0.5 if two or more are vague or missing, 0 if absent."
        ),
    },
    {
        "key": "constraint_families",
        "label": "Constraint Families",
        "description": (
            "Must be a list covering at least five families: exactly-one encoding, "
            "initial configuration, input placement, local transition, and acceptance "
            "constraints. Each must have a 'family_name', 'purpose', and "
            "'supporting_files'. Score 1 if all five are present with correct purposes "
            "and valid file references, deduct 0.15 per missing family, 0.05 per "
            "missing/invalid file reference. Minimum 0."
        ),
    },
    {
        "key": "soundness_argument",
        "label": "Soundness Argument",
        "description": (
            "Must state: if the formula is satisfiable then the input is in the language. "
            "Reasoning must trace: satisfying assignment → valid tableau → genuine "
            "accepting computation → input accepted. Must include 'supporting_files'. "
            "Score 1 for full correct chain, 0.5 if the direction is right but "
            "reasoning is thin, 0 if wrong or missing."
        ),
    },
    {
        "key": "completeness_argument",
        "label": "Completeness Argument",
        "description": (
            "Must state: if the input is in the language then the formula is satisfiable. "
            "Reasoning must trace: accepting computation exists → tableau exists → "
            "assign variables to match tableau → all constraints satisfied. Must include "
            "'supporting_files'. Score 1 for full correct chain, 0.5 if direction is "
            "right but reasoning is thin, 0 if wrong or missing."
        ),
    },
    {
        "key": "polynomial_size_argument",
        "label": "Polynomial Size Argument",
        "description": (
            "Must argue: p(n)-step machine → polynomial rows/columns → polynomial "
            "variables → each clause family contributes polynomially many clauses → "
            "whole formula is polynomial in n and constructible in polynomial time. "
            "Must include 'supporting_files'. Score 1 for a complete quantitative "
            "argument, 0.5 if the argument is correct but vague, 0 if missing or wrong."
        ),
    },
    {
        "key": "worked_example_summary",
        "label": "Worked Example Summary",
        "description": (
            "Must describe a small NTM/input pair from the packet and explain how the "
            "encoding works concretely (rows = configurations, variables for local info, "
            "clause families rule out illegal configs). Must include 'supporting_files'. "
            "Score 1 for a clear, accurate example summary, 0.5 if vague or only "
            "partially connected to the proof, 0 if absent or unrelated."
        ),
    },
    {
        "key": "common_errors_to_avoid",
        "label": "Common Errors to Avoid",
        "description": (
            "Must be a list covering at least four errors: (1) confusing Cook-Levin "
            "with 'SAT is in NP', (2) saying the reduction enumerates all assignments, "
            "(3) describing one giant global check instead of local constraints, "
            "(4) ignoring the polynomial bound. Each entry needs 'error', 'correction', "
            "and 'supporting_files'. Score 1 if all four are present and correct, "
            "deduct 0.2 per missing error, 0.05 per missing file reference. Minimum 0."
        ),
    },
    {
        "key": "final_conclusion",
        "label": "Final Conclusion",
        "description": (
            "Must conclude that every language in NP is polynomial-time reducible to "
            "SAT, with a brief reference to the soundness/completeness of the encoding "
            "and the polynomial size of the construction. Score 1 if complete and "
            "correct, 0.5 if it reaches the right conclusion but without justification, "
            "0 if missing or wrong."
        ),
    },

    {
        "key": "karp_theorem_name",
        "label": "Karp Theorem Name",
        "description": (
            "The field must equal exactly \"Karp's 21 NP-Complete Problems\". "
            "Score 1 if correct, 0 otherwise."
        ),
    },
    {
        "key": "karp_theorem_statement",
        "label": "Karp Theorem Statement",
        "description": "Must state that 21 diverse problems are NP-complete. Score 1 for full correctness, 0 if missing."
    },
    {
        "key": "karp_proof_strategy_overview",
        "label": "Karp Proof Strategy Overview",
        "description": "Must describe starting from SAT/3SAT and building a tree of reductions. Score 1 if correct."
    },
    {
        "key": "karp_core_reductions",
        "label": "Karp Core Reductions",
        "description": "Must cover 3SAT->Clique, Clique->Vertex Cover, and Directed->Undirected HC with correct reduction ideas and valid supporting_files. Score 1 if all 3 are correct, deduct 0.33 per missing/wrong."
    },
    {
        "key": "karp_common_errors",
        "label": "Karp Common Errors",
        "description": (
            "Must list at least 3 source-grounded common errors related to Karp's "
            "reductions. Valid examples include reversing the reduction direction, "
            "forgetting the separate NP-membership argument, or wiring the 3SAT-to-"
            "Clique graph incorrectly, but other legitimate Karp-reduction mistakes "
            "also qualify. Score 1 if at least 3 valid errors are present with "
            "accurate corrections and valid supporting_files, deduct 0.33 per "
            "missing or invalid item."
        )
    },
]

# Substantive proof obligations carry most of the reward. Lightweight framing
# fields are still checked, but the benchmark signal should come from the
# sections that require coordinating definitions, tableau encoding, correctness
# directions, and polynomial-size analysis.
DIMENSION_WEIGHTS = {
    "theorem_name": 0.005,
    "theorem_statement": 0.015,
    "proof_goal": 0.015,
    "proof_strategy_overview": 0.015,
    "core_definitions": 0.120,
    "tableau_encoding": 0.180,
    "constraint_families": 0.010,
    "soundness_argument": 0.180,
    "completeness_argument": 0.180,
    "polynomial_size_argument": 0.180,
    "worked_example_summary": 0.080,
    "common_errors_to_avoid": 0.005,
    "final_conclusion": 0.015,

    "karp_theorem_name": 0.005,
    "karp_theorem_statement": 0.05,
    "karp_proof_strategy_overview": 0.05,
    "karp_core_reductions": 0.20,
    "karp_common_errors": 0.10,
}

# The supporting_files validity check: only these source text paths are allowed.
VALID_PACKET_PATHS = {
    "/input_artifacts/mit_ocw_18_404j_lecture16_cook_levin_transcript.txt",
    "/input_artifacts/mit_ocw_6_080_lecture9_cook_levin_notes.txt",
    "/input_artifacts/cmu_15451_lecture15_np_completeness_slides.txt",
    "/input_artifacts/source_attribution.md",
    "/input_artifacts/berkeley_cs170_karp21_notes.txt",
    "/input_artifacts/stanford_cs154_karp21_transcript.txt",
}

# Invalid packet paths are objective structural errors. Apply this after
# LLM scoring so path validation is deterministic and dimension-local.
INVALID_CITATION_PENALTY = 0.10
INVALID_CITATION_MAX_PENALTY = 0.60


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="LLM judge for Cook-Levin proof dossier task."
    )
    parser.add_argument("--agent-output", required=True, help="Path to agent output JSON")
    parser.add_argument("--oracle", required=True, help="Path to oracle JSON")
    parser.add_argument("--reward-out", required=True, help="Path to write reward JSON")
    args = parser.parse_args()

    justification_path = "/logs/agent/judge_justification.txt"

    # ------------------------------------------------------------------
    # 1. Load agent output
    # ------------------------------------------------------------------
    try:
        with open(args.agent_output, "r", encoding="utf-8") as fh:
            agent_output = json.load(fh)
    except FileNotFoundError:
        write_failure(
            args.reward_out,
            justification_path,
            f"Agent output file not found at {args.agent_output}. "
            "The agent likely timed out or wrote to the wrong path.",
        )
        sys.exit(0)
    except json.JSONDecodeError as exc:
        write_failure(
            args.reward_out,
            justification_path,
            f"Agent output is not valid JSON: {exc}",
        )
        sys.exit(0)

    # ------------------------------------------------------------------
    # 2. Load oracle
    # ------------------------------------------------------------------
    with open(args.oracle, "r", encoding="utf-8") as fh:
        oracle = json.load(fh)

    # ------------------------------------------------------------------
    # 3. Exact-match shortcut — oracle agent always scores 1.0
    # ------------------------------------------------------------------
    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        sys.exit(0)

    # ------------------------------------------------------------------
    # 4. Structural pre-check: verify top-level keys exist
    # ------------------------------------------------------------------
    required_keys = {d["key"] for d in DIMENSIONS}
    missing_keys = required_keys - set(agent_output.keys())
    if missing_keys:
        # Still attempt LLM scoring but flag missing keys
        missing_note = (
            f"WARNING: Agent output is missing top-level keys: "
            f"{sorted(missing_keys)}. These dimensions will score 0.\n\n"
        )
    else:
        missing_note = ""

    # ------------------------------------------------------------------
    # 5. Supporting-files validity pre-check (structural, no LLM needed)
    # ------------------------------------------------------------------
    def collect_supporting_files(obj) -> list:
        """Recursively collect all supporting_files values from the agent output."""
        found = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "supporting_files" and isinstance(v, list):
                    found.extend(v)
                else:
                    found.extend(collect_supporting_files(v))
        elif isinstance(obj, list):
            for item in obj:
                found.extend(collect_supporting_files(item))
        return found

    def invalid_supporting_files(obj) -> list:
        """Return invalid supporting_files values found in one scored dimension."""
        return [f for f in collect_supporting_files(obj) if f not in VALID_PACKET_PATHS]

    agent_files = collect_supporting_files(agent_output)
    invalid_files = [f for f in agent_files if f not in VALID_PACKET_PATHS]
    if invalid_files:
        file_warning = (
            f"NOTE: Agent cited {len(invalid_files)} invalid packet path(s): "
            f"{invalid_files[:5]}{'...' if len(invalid_files) > 5 else ''}. "
            "These will lower scores on affected dimensions.\n\n"
        )
    else:
        file_warning = ""

    # ------------------------------------------------------------------
    # 6. LLM scoring — one call per dimension for fine-grained breakdown
    # ------------------------------------------------------------------
    client = OpenAI(
        api_key=os.environ["FIREWORKS_API_KEY"],
        base_url="https://api.fireworks.ai/inference/v1",
    )

    dimension_results = {}  # key -> {"score": float, "justification": str}
    total_score = 0.0

    for dim in DIMENSIONS:
        key = dim["key"]

        oracle_value = oracle.get(key)
        agent_value = agent_output.get(key)

        if agent_value is None:
            dimension_results[key] = {
                "score": 0.0,
                "justification": f"Key '{key}' is absent from agent output.",
            }
            continue

        prompt = (
            "You are an expert evaluator judging a student's proof dossier on the "
            "Cook-Levin Theorem against a gold oracle.\n\n"
            f"DIMENSION: {dim['label']}\n"
            f"SCORING RUBRIC:\n{dim['description']}\n\n"
            f"ORACLE VALUE:\n{json.dumps(oracle_value, indent=2)}\n\n"
            f"AGENT VALUE:\n{json.dumps(agent_value, indent=2)}\n\n"
            "Instructions:\n"
            "- Compare the agent's value against the oracle and the rubric.\n"
            "- Apply the rubric scoring rules precisely.\n"
            "- Do NOT give partial credit for vague or hand-wavy content.\n"
            "- CRITICAL: Check the agent's `supporting_files` array for validity and relevance to this specific section.\n"
            "- Do NOT require an exact match with the oracle's citation list. Different valid supporting files, or a different subset of 1-3 valid supporting files, are acceptable if they directly support the section being scored.\n"
            "- If the agent cites a file path that is invalid or cites a source that is not directly relevant to this section, treat that as a citation error and score the dimension according to the rubric, including assigning 0.0 when the dimension requires citation accuracy and the citation is clearly wrong.\n"
            "- If the agent omits some oracle citations but the remaining citations are valid and directly relevant, do not fail the dimension solely for that reason; only apply the rubric's normal deductions for missing citations.\n"
            f"- Also, paths not in ({sorted(VALID_PACKET_PATHS)}) are invalid.\n"
            "- Return ONLY valid JSON (no markdown), in exactly this format:\n"
            '{"score": <float 0.0-1.0>, "justification": "<one-paragraph explanation>"}'
        )

        try:
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a strict JSON scoring service. Return exactly "
                        "one JSON object and no prose, markdown, preamble, or "
                        "analysis. The first character must be '{' and the last "
                        "character must be '}'."
                    ),
                },
                {"role": "user", "content": prompt},
            ]
            result = call_llm_judge(client, messages)
            score = max(0.0, min(1.0, float(result.get("score", 0.0))))
            justification = result.get("justification", "(no justification returned)")
        except Exception as exc:
            score = 0.0
            justification = f"Judge retry exhaustion: {exc}"

        dim_invalid_files = invalid_supporting_files(agent_value)
        if dim_invalid_files:
            raw_score = score
            penalty = min(
                INVALID_CITATION_MAX_PENALTY,
                INVALID_CITATION_PENALTY * len(dim_invalid_files),
            )
            score = max(0.0, round(score - penalty, 4))
            invalid_preview = dim_invalid_files[:5]
            suffix = "..." if len(dim_invalid_files) > 5 else ""
            justification = (
                f"{justification} Deterministic citation-path penalty: "
                f"{len(dim_invalid_files)} invalid supporting_files path(s) "
                f"{invalid_preview}{suffix}; raw score {raw_score:.2f}, "
                f"penalty {penalty:.2f}, final score {score:.2f}."
            )

        dimension_results[key] = {"score": score, "justification": justification}
        total_score += score

    # ------------------------------------------------------------------
    # 7. Aggregate score — weighted by substantive proof importance
    # ------------------------------------------------------------------
    n_dims = len(DIMENSIONS)
    weight_sum = sum(DIMENSION_WEIGHTS[d["key"]] for d in DIMENSIONS)
    final_score = round(
        sum(
            dimension_results[d["key"]]["score"] * DIMENSION_WEIGHTS[d["key"]]
            for d in DIMENSIONS
        )
        / weight_sum,
        4,
    )

    # ------------------------------------------------------------------
    # 8. Write reward
    # ------------------------------------------------------------------
    json.dump({"reward": final_score}, open(args.reward_out, "w"))

    # ------------------------------------------------------------------
    # 9. Write justification
    # ------------------------------------------------------------------
    passed = sum(1 for v in dimension_results.values() if v["score"] >= 0.9)
    partial = sum(
        1 for v in dimension_results.values() if 0.0 < v["score"] < 0.9
    )
    failed = sum(1 for v in dimension_results.values() if v["score"] == 0.0)

    lines = [
        f"Score: {final_score} ({passed}/{n_dims} full, {partial} partial, {failed} failed)\n",
        missing_note,
        file_warning,
        "=" * 70,
        "DIMENSION-BY-DIMENSION BREAKDOWN",
        "=" * 70,
    ]

    for dim in DIMENSIONS:
        key = dim["key"]
        res = dimension_results.get(key, {"score": 0.0, "justification": "Not evaluated."})
        status = (
            "PASS" if res["score"] >= 0.9
            else "PARTIAL" if res["score"] > 0.0
            else "FAIL"
        )
        lines.append(
            f"\n[{status}] {dim['label']} (score={res['score']:.2f})\n"
            f"  {res['justification']}"
        )

    with open(justification_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
