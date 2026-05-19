import argparse
import json
import os
import re
from openai import OpenAI


def extract_json(text: str) -> str:
    """Best-effort JSON extraction. Handles fenced blocks and 'thinking then JSON' outputs."""
    text = text.strip()
    fenced = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if fenced:
        return fenced.group(1).strip()
    candidates = list(re.finditer(r"\{[\s\S]*?\}(?=\s*(?:```|$|\Z))", text))
    for m in reversed(candidates):
        snippet = m.group(0)
        try:
            json.loads(snippet)
            return snippet
        except json.JSONDecodeError:
            continue
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
    if first:
        return first.group(0)
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    parser.add_argument("--details-out", required=False, default=None)
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

    response_count = len(oracle.get("per_response_assessment", []))
    total_points = 4 + 30 * response_count
    response_ids = [
        item.get("response_id")
        for item in oracle.get("per_response_assessment", [])
        if item.get("response_id")
    ]
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
        "for a Tetris garbage-application solution-audit task.\n\n"
        "OUTPUT FORMAT REQUIREMENT (HARD): your entire response MUST be a single JSON "
        "object and NOTHING else. Begin your response with `{` and end with `}`. "
        "Do not narrate, do not output preamble, do not output reasoning prose, do not output markdown.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- wrong_garbage_insertion_direction\n"
        "- wrong_hole_column_alignment\n"
        "- wrong_garbage_order_or_count\n"
        "- wrong_post_shift_topout_handling\n"
        "- invalid_or_incomplete_final_output\n\n"
        "Field meanings:\n"
        "- correct_final_board: the 20-row x 10-column board after the four garbage lines have been applied and any clears processed.\n"
        "- acceptable_solution_ids: the response letters whose final boards are exactly correct AND whose failure_reasons list is empty.\n"
        "- final_board_correct: whether that response's final claimed board exactly matches the correct final board.\n"
        "- failure_reasons: exact set of concrete reasons why the response's final board or reasoning is defective. Must be empty iff final_board_correct is true AND no failure-reason trigger fires on the response.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For correct_final_board, require exact row-by-row equality and exact top-to-bottom order.\n"
        "2. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        f"3. per_response_assessment must contain exactly one object for each response {response_id_text}.\n"
        "4. For response_id and final_board_correct, require exact equality.\n"
        "5. For failure_reasons, order does not matter, but the set must match exactly. Extra codes fail. Missing codes fail. No partial credit inside failure_reasons.\n"
        "6. A per-response audit receives credit only if response_id, final_board_correct, AND the exact failure_reasons set are all correct for that response.\n\n"
        "Scoring rubric with weighted integer points:\n"
        "- correct_final_board = 2 points.\n"
        "- acceptable_solution_ids = 2 points.\n"
        f"- Each per-response audit {response_id_text} is all-or-nothing = 30 points. Award the 30 points only if response_id, final_board_correct, and exact failure_reasons set all match the oracle for that response. Otherwise award 0 for that response.\n"
        f"- Total = {total_points} points. score = passed / {total_points}.\n\n"
        "Output EXACTLY this JSON object with the appropriate integer value filled in for `passed`, and NOTHING else. The harness computes score as passed/total — do NOT output a separate 'score' field:\n"
        f'{{"passed": <int from 0 to {total_points}>, "total": {total_points}, '
        '"justification": "<concise weighted field-by-field breakdown, 50-300 chars>"}'
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

    passed_raw = result.get("passed")
    try:
        passed = int(passed_raw)
    except (TypeError, ValueError):
        passed = 0
    passed = max(0, min(total_points, passed))
    score = passed / total_points if total_points else 0.0
    score = max(0.0, min(1.0, score))
    json.dump({"reward": score}, open(args.reward_out, "w", encoding="utf-8"))

    with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
        f.write(
            f"Score: {score:.4f} ({passed}/{total_points} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
