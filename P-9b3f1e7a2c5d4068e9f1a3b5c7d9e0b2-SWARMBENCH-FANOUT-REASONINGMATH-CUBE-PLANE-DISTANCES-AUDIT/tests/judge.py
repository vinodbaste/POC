import argparse
import json
import os
import re

from openai import OpenAI


JUDGE_MODEL = "accounts/fireworks/models/kimi-k2p5"

ALL_FAILURE_CODES = [
    "claims_unique_edge_length",
    "restricts_to_nonnegative_subset_sums",
    "assumes_max_distance_equals_space_diagonal",
    "assumes_plane_parallel_to_cube_face",
    "equates_max_distance_with_edge_length_directly",
    "uses_fabricated_invariant_or_invalid_derivation",
    "accepts_internal_contradictions_in_derivation",
    "assumes_zero_distance_vertex_is_axis_corner",
    "omits_sign_pattern_casework",
    "treats_one_orientation_as_proof_of_uniqueness",
    "derives_correct_partial_s2_then_discards_it",
    "non_terminating_or_no_final_answer",
]


def extract_json(text: str) -> str:
    text = text.strip()
    m = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if m:
        return m.group(1).strip()
    m = re.search(r"\{[\s\S]*\}", text)
    if m:
        return m.group(0)
    return text


def build_prompt(oracle: dict, agent: dict) -> str:
    rubric = (
        "You are a strict expert judge for a SwarmBench math/reasoning audit task. "
        "Score the agent output against the oracle on a multi-field weighted rubric. "
        "Apply substantive expert interpretation on per-response failure_reasons and primary_failure_code "
        "(allow plausible alternative codes that are concretely supported by the response text), "
        "but apply STRICT scoring on structural and aggregation fields (presence, minimum lengths, "
        "exact string match on the gold answer, exact sorted-list match per key of code_application_table).\n\n"
        "ORACLE (ground truth):\n"
        f"{json.dumps(oracle, indent=2)}\n\n"
        "AGENT OUTPUT (to be scored):\n"
        f"{json.dumps(agent, indent=2)}\n\n"
        "Allowed failure codes vocabulary (size 12):\n"
        + "\n".join(f"- {c}" for c in ALL_FAILURE_CODES)
        + "\n\n"
        "Weighted scoring rubric. Sum the per-field points to get total_earned. "
        "The maximum total possible is the sum of all the per-field weights below (compute it as you score).\n\n"
        "TOP-LEVEL FIELDS:\n"
        "1) gold_final_answer: exact string match against oracle's gold_final_answer. Award 2 if equal, else 0.\n"
        "2) gold_edge_length_squared_set: exact sorted-list match against oracle. Award 2 if equal as sorted lists, else 0.\n"
        "3) acceptable_solution_ids: exact set match against oracle. Award 2 if equal, else 0.\n\n"
        "PER-RESPONSE FIELDS (apply for each of the 9 entries in per_response_assessment, A..I):\n"
        "4) final_answer_correct: exact bool match against oracle. Award 5 if equal, else 0.\n"
        "5) failure_reasons: substantive set match against oracle's failure_reasons.\n"
        "   - Award 30 if the agent set EXACTLY equals the oracle set.\n"
        "   - Award 15 if the agent set differs from the oracle by at most one substantively-equivalent code "
        "(e.g., agent picked a near-synonymous code that is plausibly supported by the response text).\n"
        "   - Award 8 if overlap is at least half (|A intersect O| / |O| >= 0.5) but the set differs by more than one code.\n"
        "   - Award 0 otherwise.\n"
        "6) primary_failure_code: \n"
        "   - Award 25 if agent's primary equals oracle's primary exactly.\n"
        "   - Award 10 if agent's primary is in the oracle's failure_reasons set but not the oracle's primary "
        "(plausible alternative).\n"
        "   - Award 0 otherwise.\n"
        "7) primary_failure_code_evidence: STRICT structural check. Award 8 if the value is a string of "
        ">=50 characters that substantively references the response's text; otherwise award 0.\n"
        "8) alternative_codes_considered: STRICT structural check. Award 8 if the value is a list with at "
        ">=2 unique well-formed objects, each having a 'code' from the controlled vocabulary (or \"NONE\") that "
        "is DIFFERENT from this response's primary_failure_code and unique within the list, and a 'reason_excluded' "
        "string of >=20 characters; otherwise award 0.\n"
        "9) failure_reason_evidence per code: For each code in the ORACLE's failure_reasons for this response, "
        "check that the agent's failure_reason_evidence has that key with a string value of >=20 characters. "
        "Award 5 per code if present and >=20 chars, else 0. Do NOT award points for evidence keys the oracle does "
        "not have.\n"
        "10) code_application_count: STRICT integer match against oracle (oracle value = len(failure_reasons)). "
        "Award 10 if equal, else 0.\n"
        "11) primary_in_set_check: STRICT bool match against oracle (oracle: true iff primary_failure_code in failure_reasons, "
        "or primary_failure_code == 'NONE' and failure_reasons is []). Award 5 if equal, else 0.\n"
        "12) evidence_key_completeness: STRICT integer match (oracle value = # of evidence keys matching failure_reasons). "
        "Award 8 if equal, else 0.\n\n"
        "TOP-LEVEL AGGREGATION FIELDS:\n"
        "13) code_application_table: For each of the 12 codes (keys), STRICT sorted-list match against the oracle's "
        "list for that key. Award 100 per key if the agent's list (sorted) equals the oracle's list (sorted); else 0. "
        "Outputting null or omitting a key forfeits the full 100 for that key.\n"
        "14) cross_response_observations: Award 30 if the value is a single string of >=300 characters that "
        "substantively describes shared defect patterns across responses; award 15 if the string is >=300 chars but "
        "generic / boilerplate / does not reference response-specific defects; award 0 if <300 chars or missing.\n\n"
        "Be strict on every structural minimum (length, presence, list-match, integer-match). Be substantive but "
        "fair on the per-response interpretive fields (failure_reasons set match and primary_failure_code).\n\n"
        "Output JSON only, no markdown, in this exact form:\n"
        "{\n"
        "  \"score\": <float in [0.0, 1.0], computed as total_earned / total_possible>,\n"
        "  \"total_earned\": <int>,\n"
        "  \"total_possible\": <int>,\n"
        "  \"top_level\": {\"gold_final_answer\": int, \"gold_edge_length_squared_set\": int, \"acceptable_solution_ids\": int},\n"
        "  \"per_response\": {\"A\": int, \"B\": int, \"C\": int, \"D\": int, \"E\": int, \"F\": int, \"G\": int, \"H\": int, \"I\": int},\n"
        "  \"code_application_table_total\": int,\n"
        "  \"cross_response_observations\": int,\n"
        "  \"justification\": \"<concise field-by-field reasoning, 200-600 chars>\"\n"
        "}\n"
    )
    return rubric


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-output", required=True)
    ap.add_argument("--oracle", required=True)
    ap.add_argument("--reward-out", required=True)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)
    if os.path.exists("/logs"):
        os.makedirs("/logs/agent", exist_ok=True)

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent_output = json.load(f)
        with open(args.oracle, "r", encoding="utf-8") as f:
            oracle = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        with open(args.reward_out, "w", encoding="utf-8") as f:
            json.dump({"reward": 0.0}, f)
        try:
            with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
                f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}\n")
        except OSError:
            pass
        return

    if agent_output == oracle:
        with open(args.reward_out, "w", encoding="utf-8") as f:
            json.dump({"reward": 1.0}, f)
        try:
            with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
                f.write("Score: 1.0\n\nAgent output exactly matches oracle (shortcut).\n")
        except OSError:
            pass
        return

    client = OpenAI(
        api_key=os.environ["FIREWORKS_API_KEY"],
        base_url="https://api.fireworks.ai/inference/v1",
    )

    prompt = build_prompt(oracle, agent_output)

    response = client.chat.completions.create(
        model=JUDGE_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    raw = response.choices[0].message.content or ""

    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError as e:
        with open(args.reward_out, "w", encoding="utf-8") as f:
            json.dump({"reward": 0.0}, f)
        try:
            with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
                f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw:\n{raw}\n")
        except OSError:
            pass
        return

    score = max(0.0, min(1.0, float(result.get("score", 0.0))))
    with open(args.reward_out, "w", encoding="utf-8") as f:
        json.dump({"reward": score}, f)

    try:
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(
                f"Score: {score:.4f} "
                f"({result.get('total_earned', '?')}/{result.get('total_possible', '?')} weighted points)\n\n"
            )
            f.write(json.dumps(result, indent=2))
            f.write("\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
