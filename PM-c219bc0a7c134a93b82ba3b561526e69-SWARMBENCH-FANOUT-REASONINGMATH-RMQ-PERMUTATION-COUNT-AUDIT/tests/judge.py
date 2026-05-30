import argparse
import json
import os
import re
import sys
import traceback


JUSTIFICATION_PATH = "/logs/agent/judge_justification.txt"


def _write_reward(reward_out: str, reward: float) -> None:
    try:
        os.makedirs(os.path.dirname(reward_out), exist_ok=True)
        with open(reward_out, "w", encoding="utf-8") as f:
            json.dump({"reward": float(reward)}, f)
    except Exception:
        pass


def _write_justification(text: str) -> None:
    try:
        os.makedirs(os.path.dirname(JUSTIFICATION_PATH), exist_ok=True)
        with open(JUSTIFICATION_PATH, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception:
        pass


def _fail_closed(reward_out: str, message: str) -> None:
    _write_reward(reward_out, 0.0)
    _write_justification(f"Score: 0.0\n\n{message}")


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

    reward_out = args.reward_out

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent_output = json.load(f)
    except FileNotFoundError as e:
        _fail_closed(reward_out, f"Agent output missing: {e}")
        return
    except json.JSONDecodeError as e:
        _fail_closed(reward_out, f"Agent output is not valid JSON: {e}")
        return
    except Exception as e:
        _fail_closed(reward_out, f"Unable to read agent output: {e}")
        return

    try:
        with open(args.oracle, "r", encoding="utf-8") as f:
            oracle = json.load(f)
    except Exception as e:
        _fail_closed(reward_out, f"Unable to read oracle: {e}")
        return

    if agent_output == oracle:
        _write_reward(reward_out, 1.0)
        _write_justification("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    try:
        from openai import OpenAI
    except Exception as e:
        _fail_closed(reward_out, f"OpenAI client import failed: {e}")
        return

    api_key = os.environ.get("FIREWORKS_API_KEY")
    if not api_key:
        _fail_closed(reward_out, "FIREWORKS_API_KEY environment variable not set.")
        return

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.fireworks.ai/inference/v1",
        )
    except Exception as e:
        _fail_closed(reward_out, f"OpenAI client init failed: {e}")
        return

    prompt = (
        "You are an evaluation judge grading an agent's JSON output against a gold oracle "
        "for a permutation-counting-from-RMQ-table solution-audit task. The agent reports a single "
        "non-negative integer count, an acceptable_solution_ids set, and a per-response audit "
        "for nine candidate responses A through I.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Allowed failure reason codes are exactly:\n"
        "- wrong_formula\n"
        "- arithmetic_error\n"
        "- invalid_or_incomplete_justification\n"
        "- final_answer_error\n\n"
        "Field meanings:\n"
        "- correct_answer: a single non-negative integer giving the verified count of permutations "
        "consistent with the table.\n"
        "- acceptable_solution_ids: the response letters whose final stated value is correct "
        "AND whose derivation is mathematically valid.\n"
        "- final_answer_correct: whether that response gives the correct value AND its derivation is valid.\n"
        "- failure_reasons: exact set of concrete reasons why the response is wrong. It must be empty iff "
        "final_answer_correct is true.\n\n"
        "Equivalence and strictness rules:\n"
        "1. For correct_answer, require exact integer equality.\n"
        "2. For acceptable_solution_ids, require the same set of response letters as the oracle (order-insensitive).\n"
        "3. per_response_assessment must contain exactly one object for each response A through I (nine entries).\n"
        "4. For response_id and final_answer_correct, require exact equality with the oracle.\n"
        "5. For failure_reasons, order does not matter, but the set must match exactly. Extra reasons fail. "
        "Missing reasons fail. No partial credit inside failure_reasons.\n"
        "6. A per-response audit receives credit only if response_id, final_answer_correct, and the exact "
        "failure_reasons set are all correct for that response.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_answer correct = 2 points.\n"
        "- acceptable_solution_ids = 2 points.\n"
        "- Each response audit A-I is all-or-nothing = 30 points. Award the 30 points only if response_id, "
        "final_answer_correct, and the exact failure_reasons set all match the oracle for that response. "
        "Otherwise award 0 for that response.\n"
        "- Total = 274 points (4 scalar + 9 * 30). score = passed/274.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 274, '
        '"justification": "<concise weighted field-by-field breakdown>"}'
    )

    try:
        response = client.chat.completions.create(
            model="accounts/fireworks/models/kimi-k2p5",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
    except Exception as e:
        _fail_closed(reward_out, f"Judge LLM API call failed: {e}\n{traceback.format_exc()}")
        return

    try:
        raw = response.choices[0].message.content or ""
    except Exception as e:
        _fail_closed(reward_out, f"Judge LLM response malformed: {e}")
        return

    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError as e:
        _fail_closed(reward_out, f"Judge parse error: {e}\nRaw: {raw}")
        return
    except Exception as e:
        _fail_closed(reward_out, f"Judge result extraction failed: {e}\nRaw: {raw}")
        return

    try:
        raw_score = result.get("score", 0.0)
        score = max(0.0, min(1.0, float(raw_score)))
    except (TypeError, ValueError) as e:
        _fail_closed(reward_out, f"Judge score not numeric: {e}\nResult: {result}")
        return

    _write_reward(reward_out, score)
    _write_justification(
        f"Score: {score} ({result.get('passed', '?')}/{result.get('total', '?')} passed)\n\n"
        f"{result.get('justification', '')}"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        try:
            argv = sys.argv
            idx = argv.index("--reward-out") if "--reward-out" in argv else -1
            reward_out = argv[idx + 1] if 0 <= idx < len(argv) - 1 else "/logs/verifier/reward.json"
        except Exception:
            reward_out = "/logs/verifier/reward.json"
        _fail_closed(reward_out, f"Unhandled judge exception: {e}\n{traceback.format_exc()}")
