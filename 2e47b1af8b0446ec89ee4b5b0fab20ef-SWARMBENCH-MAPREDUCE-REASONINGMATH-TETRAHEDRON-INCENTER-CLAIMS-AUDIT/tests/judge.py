import argparse
import json
import os
import re
from openai import OpenAI


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.reward_out), exist_ok=True)

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent_output = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w", encoding="utf-8"))
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}")
        return

    with open(args.oracle, "r", encoding="utf-8") as f:
        oracle = json.load(f)

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w", encoding="utf-8"))
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    client = OpenAI(
        api_key=os.environ["FIREWORKS_API_KEY"],
        base_url="https://api.fireworks.ai/inference/v1",
    )

    prompt = (
        "You are an evaluation judge grading an agent's JSON output against a gold oracle "
        "for a tetrahedron-incenter solution-audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- rejected_perpendicularity_no_counterexample\n"
        "- cascaded_rejection_of_e_from_a\n"
        "- correct_gtfa_invalid_proof_chain\n"
        "- false_universal_insphere_at_face_incenter\n"
        "- confused_centroid_and_incenter\n"
        "- self_contradictory_centroid_above\n"
        "- vague_word_salad_proofs\n"
        "- cot_trace_misses_distance_equivalence\n"
        "- repeats_false_universal_in_e\n"
        "- vague_almost_regular_nonconstruction\n"
        "- rejects_e_via_general_property_misapplied\n"
        "- false_claim_ai_equals_inradius\n"
        "- incoherent_ratio_argument_in_b\n"
        "- degenerate_counterexample_b_equals_c\n\n"
        "Field meanings:\n"
        "- gold_set: alphabetically-sorted lowercase letters a..h identifying the statements necessarily true under the two hypotheses.\n"
        "- acceptable_solution_ids: the response letters whose claimed set equals the gold set AND whose proofs have no defect.\n"
        "- final_answer_correct: whether that response's claimed SET of necessarily-true statement labels equals the gold set as a set.\n"
        "- failure_reasons: exact set of concrete reasons why the response's argument is defective. It must be empty iff the response's claimed set equals the gold AND the proof has no defect.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For gold_set, require the same set of lowercase letters as the oracle (alphabetical order; order irrelevant for matching).\n"
        "2. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        "3. per_response_assessment must contain exactly one object for each response A-I.\n"
        "4. For response_id and final_answer_correct, require exact equality.\n"
        "5. For failure_reasons, order does not matter, but the set must match exactly. Extra reasons fail. Missing reasons fail. No partial credit inside failure_reasons.\n"
        "6. A per-response audit receives credit only if response_id, final_answer_correct, and the exact failure_reasons set are all correct for that response.\n\n"
        "Scoring rubric with weighted points:\n"
        "- gold_set = 2 points.\n"
        "- acceptable_solution_ids = 2 points.\n"
        "- Each response audit A-I is all-or-nothing = 30 points. Award the 30 points only if response_id, final_answer_correct, and exact failure_reasons set all match the oracle for that response. Otherwise award 0 for that response.\n"
        "- Total = 274 points. score = passed/274.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 274, '
        '"justification": "<concise weighted field-by-field breakdown>"}'
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2p5",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    raw = response.choices[0].message.content or ""

    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w", encoding="utf-8"))
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw: {raw}")
        return

    score = max(0.0, min(1.0, float(result.get("score", 0.0))))
    json.dump({"reward": score}, open(args.reward_out, "w", encoding="utf-8"))

    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', '?')} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
