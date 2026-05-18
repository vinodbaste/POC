import argparse
import json
import os
import re

from openai import OpenAI


JUDGE_MODEL = "accounts/fireworks/models/kimi-k2p5"

ALL_FAILURE_CODES = [
    "wrong_move_set_including_zero",
    "wrong_move_set_excluding_one",
    "incorrect_fibonacci_enumeration",
    "confused_pn_convention",
    "base_case_set_to_n",
    "treats_game_as_misere",
    "applies_nim_sprague_grundy_directly_wrong",
    "arithmetic_recursion_error",
    "claims_periodic_pattern_falsely",
    "arbitrary_pattern_heuristic",
    "truncated_or_short_string",
    "non_terminating_or_no_final_answer",
]

RESPONSE_IDS = ["A", "B", "C", "D", "E", "F", "G", "H"]


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
    return (
        "You are a strict expert judge for a SwarmBench math/reasoning audit task on the Fibonacci "
        "Subtraction Game P/N classification (positions 0-100). Score the agent output against the "
        "oracle on a multi-field weighted rubric. Apply substantive expert interpretation on "
        "per-response failure_reasons and primary_failure_code (allow plausible alternative codes "
        "that are concretely supported by the response text), but apply STRICT scoring on structural "
        "and aggregation fields (presence, minimum lengths, exact string match on the gold answer, "
        "exact sorted-list match per key of code_application_table, exact integer match per key of "
        "response_count_per_code).\n\n"
        "ORACLE (ground truth):\n"
        f"{json.dumps(oracle, indent=2)}\n\n"
        "AGENT OUTPUT (to be scored):\n"
        f"{json.dumps(agent, indent=2)}\n\n"
        "Allowed failure codes vocabulary (size 12):\n"
        + "\n".join(f"- {c}" for c in ALL_FAILURE_CODES)
        + "\n\n"
        "Weighted scoring rubric. Sum the per-field points to get total_earned. "
        "Compute total_possible by summing the max for each scored field.\n\n"
        "TOP-LEVEL FIELDS:\n"
        "1) gold_final_answer: exact 101-character string match against oracle. Award 4 if equal, else 0.\n"
        "2) acceptable_solution_ids: exact set match. Award 2 if equal, else 0.\n\n"
        "PER-RESPONSE FIELDS (apply for each of the 8 entries in per_response_assessment, A..H):\n"
        "3) final_answer_correct: exact bool match. Award 5 if equal, else 0.\n"
        "4) failure_reasons: substantive set match against the oracle's set for that response.\n"
        "   - Award 30 if EXACT set match.\n"
        "   - Award 15 if differs by at most one substantively-equivalent code that is plausibly "
        "supported by the response text.\n"
        "   - Award 8 if overlap |A intersect O| / |O| >= 0.5 but differs by more than one code.\n"
        "   - Award 0 otherwise.\n"
        "5) primary_failure_code:\n"
        "   - Award 25 if equals oracle's primary exactly.\n"
        "   - Award 10 if in oracle's failure_reasons set but not the oracle's primary.\n"
        "   - Award 0 otherwise.\n"
        "6) primary_failure_code_evidence: STRICT. Award 8 if string >=50 chars AND substantively "
        "cites response text; else 0.\n"
        "7) alternative_codes_considered: STRICT. Award 8 if list has >=2 unique well-formed entries, "
        "each with a 'code' from the controlled vocabulary or \"NONE\" that is DIFFERENT from this "
        "response's primary_failure_code and unique within the list, and a 'reason_excluded' string "
        ">=20 chars; else 0.\n"
        "8) failure_reason_evidence: For EACH code in the ORACLE's failure_reasons set for this "
        "response, check that the agent's failure_reason_evidence dict has that code as a key with a "
        "string value of >=20 characters. Award 5 per oracle-listed code if present and >=20 chars; "
        "else 0. Do not award points for keys the oracle does not have.\n"
        "9) code_application_count: STRICT integer match against oracle (oracle value = len(failure_reasons)). "
        "Award 10 if equal, else 0.\n"
        "10) primary_in_set_check: STRICT bool match against oracle. Award 5 if equal, else 0.\n"
        "11) evidence_key_completeness: STRICT integer match (oracle value = # evidence keys matching failure_reasons). "
        "Award 8 if equal, else 0.\n\n"
        "TOP-LEVEL AGGREGATION FIELDS:\n"
        "12) code_application_table: For EACH of the 12 codes (keys), STRICT sorted-list match against "
        "oracle. Award 100 per key if equal, else 0. Null or missing forfeits the full 100.\n"
        "13) response_count_per_code: For EACH of the 12 codes, STRICT integer match. Award 20 per key if equal, else 0.\n"
        "14) code_co_occurrence_count: dict over 66 unordered pairs of codes. STRICT integer match per key. "
        "Award 5 per key if equal, else 0.\n"
        "15) response_pair_shared_codes: dict over 28 unordered pairs of response_ids. STRICT sorted-list match "
        "per key. Award 8 per key if equal, else 0.\n"
        "16) response_triple_shared_codes: dict over 56 unordered triples of response_ids. STRICT sorted-list "
        "match per key. Award 5 per key if equal, else 0.\n"
        "17) cross_response_observations: Award 30 if string >=300 characters AND substantively "
        "describes shared defect patterns; 15 if >=300 chars but boilerplate; 0 if <300 chars or missing.\n\n"
        "Be strict on every structural minimum. Be substantive but fair on interpretive per-response "
        "fields. Compute the total_possible as the sum of maxima of all scored dimensions.\n\n"
        "Output JSON only, no markdown:\n"
        "{\n"
        "  \"score\": <float in [0.0, 1.0], = total_earned / total_possible>,\n"
        "  \"total_earned\": <int>,\n"
        "  \"total_possible\": <int>,\n"
        "  \"top_level\": {\"gold_final_answer\": int, \"acceptable_solution_ids\": int},\n"
        "  \"per_response\": {\"A\": int, \"B\": int, \"C\": int, \"D\": int, \"E\": int, \"F\": int, \"G\": int, \"H\": int},\n"
        "  \"code_application_table_total\": int,\n"
        "  \"response_count_per_code_total\": int,\n"
        "  \"cross_response_observations\": int,\n"
        "  \"justification\": \"<concise field-by-field reasoning, 200-600 chars>\"\n"
        "}\n"
    )


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
