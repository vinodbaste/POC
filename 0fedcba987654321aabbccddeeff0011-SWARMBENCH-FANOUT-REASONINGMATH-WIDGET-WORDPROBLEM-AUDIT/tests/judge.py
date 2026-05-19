import argparse
import json
import os
import re
from openai import OpenAI


def extract_json(text: str) -> str:
    text = text.strip()
    fenced = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if fenced:
        return fenced.group(1).strip()
    starts = [i for i, ch in enumerate(text) if ch == "{"]
    for s in reversed(starts):
        depth = 0
        for j in range(s, len(text)):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    snippet = text[s:j + 1]
                    try:
                        json.loads(snippet)
                        return snippet
                    except json.JSONDecodeError:
                        break
    first = re.search(r"\{[\s\S]*\}", text)
    return first.group(0) if first else text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-output")
    ap.add_argument("--oracle")
    ap.add_argument("--reward-out")
    ap.add_argument("--details-out", required=False, default=None)
    args = ap.parse_args()
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

    response_count = len(oracle.get("per_response_assessment", []))
    total_points = 4 + 30 * response_count
    response_ids = [it.get("response_id") for it in oracle.get("per_response_assessment", []) if it.get("response_id")]
    response_id_text = f"{response_ids[0]}-{response_ids[-1]}" if response_ids else "listed responses"

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
        "for a multi-step word-problem reasoning audit task.\n\n"
        "OUTPUT FORMAT REQUIREMENT (HARD): your entire response MUST be a single JSON "
        "object and NOTHING else. Begin with `{` and end with `}`. Do not narrate, do not "
        "output preamble, do not output reasoning prose, do not output markdown.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- wrong_rate_or_constant\n- wrong_arithmetic_at_specific_step\n- wrong_operation_applied\n"
        "- wrong_percentage_interpretation\n- final_answer_does_not_match_workings\n"
        "- missed_or_skipped_required_step\n- truncated_or_incomplete_answer\n"
        "- non_terminating_or_no_committed_answer\n\n"
        "Field meanings:\n"
        "- gold_final_value: the unique integer answer to the word problem.\n"
        "- acceptable_solution_ids: response letters whose final answer equals gold AND failure_reasons is empty.\n"
        "- final_value_correct: whether that response's committed final integer equals gold.\n"
        "- failure_reasons: exact set of concrete reasons why the response is defective.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For gold_final_value, require exact integer equality.\n"
        "2. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        f"3. per_response_assessment must contain exactly one object for each response {response_id_text}.\n"
        "4. For response_id and final_value_correct, require exact equality.\n"
        "5. For failure_reasons, order does not matter, but the set must match exactly. Extra codes fail. Missing codes fail. No partial credit.\n"
        "6. A per-response audit receives credit only if response_id, final_value_correct, AND exact failure_reasons set all match.\n\n"
        "Scoring (integer points):\n"
        "- gold_final_value = 2 points\n- acceptable_solution_ids = 2 points\n"
        f"- Each per-response audit {response_id_text} = 30 points all-or-nothing\n"
        f"- Total = {total_points}. score = passed / {total_points}.\n\n"
        "Output EXACTLY this JSON with the integer `passed` filled in, NOTHING else. "
        "The harness computes score from passed/total — do NOT output a 'score' field:\n"
        f'{{"passed": <int 0 to {total_points}>, "total": {total_points}, '
        '"justification": "<concise 50-300 char field-by-field breakdown>"}'
    )

    try:
        response = client.chat.completions.create(
            model="accounts/fireworks/models/kimi-k2p5",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"},
        )
    except Exception:
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
            f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw: {raw[:4000]}")
        return

    try:
        passed = int(result.get("passed", 0))
    except (TypeError, ValueError):
        passed = 0
    passed = max(0, min(total_points, passed))
    score = passed / total_points if total_points else 0.0
    score = max(0.0, min(1.0, score))
    json.dump({"reward": score}, open(args.reward_out, "w", encoding="utf-8"))
    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(f"Score: {score:.4f} ({passed}/{total_points} passed)\n\n{result.get('justification', '')}")


if __name__ == "__main__":
    main()
