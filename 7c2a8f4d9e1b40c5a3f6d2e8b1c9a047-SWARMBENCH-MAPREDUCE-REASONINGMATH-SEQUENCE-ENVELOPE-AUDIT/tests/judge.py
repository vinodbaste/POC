import argparse
import json
import os
import re

from openai import OpenAI


JUDGE_MODEL = "accounts/fireworks/models/kimi-k2p5"

ALL_FAILURE_CODES = [
    "contradictory_final_answer",
    "fatal_wrong_claim",
    "invalid_one_draw_inference",
    "invalid_upper_bound",
    "missing_lower_bound",
    "no_concrete_strategy",
    "non_terminating_or_no_final_answer",
    "not_worst_case",
    "unnecessary_mixed_pair_requirement",
    "wrong_final_number",
]


def extract_json(text):
    text = text.strip()
    m = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if m:
        return m.group(1).strip()
    m = re.search(r"\{[\s\S]*\}", text)
    return m.group(0) if m else text


def build_prompt(oracle, agent):
    return (
        "You are a strict expert judge for a SwarmBench math/reasoning audit task on the Sequence-Envelope "
        "puzzle (four mislabeled envelopes of monotonic sequences). Score the agent output against the oracle "
        "on a multi-field weighted rubric. Apply substantive expert interpretation on per-response "
        "failure_reasons and primary_failure_code (allow plausible alternative codes that are concretely "
        "supported by the response text), but apply STRICT scoring on structural and aggregation fields.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent, indent=2)}\n\n"
        "Allowed failure codes vocabulary (size 10):\n"
        + "\n".join(f"- {c}" for c in ALL_FAILURE_CODES)
        + "\n\nRubric:\n"
        "1) gold_final_answer (string match): 4 if equal, else 0.\n"
        "2) acceptable_solution_ids (set match): 2 if equal, else 0.\n\n"
        "PER-RESPONSE (8 entries, A..H):\n"
        "3) final_answer_correct (exact bool): 5 / 0.\n"
        "4) failure_reasons: 30 exact set, 15 off-by-one substantively-equivalent, 8 overlap>=50% with more "
        "divergence, else 0.\n"
        "5) primary_failure_code: 25 exact; 10 if in oracle's failure_reasons set but not primary; else 0.\n"
        "6) primary_failure_code_evidence: 8 if >=50 chars and substantive; else 0.\n"
        "7) alternative_codes_considered: 8 if >=2 unique well-formed entries (code from vocab or \"NONE\", "
        "different from primary, unique, reason_excluded >=20 chars); else 0.\n"
        "8) failure_reason_evidence: 5 per oracle-listed code if present and >=20 chars; else 0.\n"
        "9) code_application_count (integer match = len(failure_reasons)): 10 / 0.\n"
        "10) primary_in_set_check (bool match): 5 / 0.\n"
        "11) evidence_key_completeness (integer match): 8 / 0.\n\n"
        "TOP-LEVEL AGGREGATION:\n"
        "12) code_application_table: 10 keys, STRICT sorted-list match per key. Award 100 per key if equal, "
        "else 0. Null/missing forfeits the full 100.\n"
        "13) response_count_per_code: 10 keys, integer match. Award 20 per key if equal, else 0.\n"
        "14) cross_response_observations: 30 if >=300 chars substantive; 15 if >=300 chars boilerplate; "
        "0 otherwise.\n\n"
        "Be strict on every structural minimum. Be substantive but fair on interpretive per-response fields.\n\n"
        "Output JSON only:\n"
        "{\n"
        "  \"score\": <float 0.0-1.0 = total_earned/total_possible>,\n"
        "  \"total_earned\": <int>, \"total_possible\": <int>,\n"
        "  \"top_level\": {\"gold_final_answer\": int, \"acceptable_solution_ids\": int},\n"
        "  \"per_response\": {\"A\": int, \"B\": int, \"C\": int, \"D\": int, \"E\": int, \"F\": int, \"G\": int, \"H\": int},\n"
        "  \"code_application_table_total\": int, \"response_count_per_code_total\": int,\n"
        "  \"code_co_occurrence_total\": int, \"response_pair_total\": int, \"response_triple_total\": int,\n"
        "  \"cross_response_observations\": int, \"justification\": \"<200-600 chars>\"\n"
        "}\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-output", required=True)
    ap.add_argument("--oracle", required=True)
    ap.add_argument("--reward-out", required=True)
    ap.add_argument("--details-out", default=None)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)
    if os.path.exists("/logs"):
        os.makedirs("/logs/agent", exist_ok=True)

    try:
        agent_output = json.load(open(args.agent_output, "r", encoding="utf-8"))
        oracle = json.load(open(args.oracle, "r", encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w", encoding="utf-8"))
        try:
            with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
                f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}\n")
        except OSError:
            pass
        return

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w", encoding="utf-8"))
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
    response = client.chat.completions.create(
        model=JUDGE_MODEL,
        messages=[{"role": "user", "content": build_prompt(oracle, agent_output)}],
        temperature=0,
    )
    raw = response.choices[0].message.content or ""
    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w", encoding="utf-8"))
        try:
            with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
                f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw:\n{raw}\n")
        except OSError:
            pass
        return

    score = max(0.0, min(1.0, float(result.get("score", 0.0))))
    json.dump({"reward": score}, open(args.reward_out, "w", encoding="utf-8"))
    try:
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: {score:.4f} ({result.get('total_earned', '?')}/{result.get('total_possible', '?')} pts)\n\n")
            f.write(json.dumps(result, indent=2))
            f.write("\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
