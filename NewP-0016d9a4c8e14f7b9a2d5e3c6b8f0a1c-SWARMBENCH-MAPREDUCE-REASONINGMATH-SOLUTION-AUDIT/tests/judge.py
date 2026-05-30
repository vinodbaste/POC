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
        "for a mathematical/game-theory solution-audit task.\n\n"
        f"ORACLE:\n{json.dumps(oracle, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, indent=2)}\n\n"
        "Grade only the requested JSON fields. Do not reward prose outside the schema.\n\n"
        "Field meanings:\n"
        "- correct_seniority_order: the correct senior-to-junior ordering of all six names.\n"
        "- correct_final_allocation: the accepted six-person allocation as [Name, stacks] pairs in seniority order.\n"
        "- acceptable_solution_ids: response letters that fully solve the voting game.\n"
        "- extracted_final_allocation: the allocation claimed by each response itself, or null if no identifiable allocation exists.\n"
        "- final_answer_correct: whether the response's final allocation exactly equals the oracle final allocation.\n"
        "- seniority_order_correct: whether the response identifies Richard, Charles, Jessica, Darren, Adam, Christopher in that order.\n"
        "- uses_backward_induction: whether the response reasons from smaller remaining-player games toward the full game.\n"
        "- respects_two_player_stalemate_rule: whether the response treats the two-player continuation as equal mutual-veto bargaining with 100/100 continuation value.\n"
        "- applies_strict_majority_rule: whether the response consistently uses more-than-half vote thresholds.\n"
        "- compares_votes_against_continuation_values: whether voter acceptance is evaluated by comparison to continuation values after proposer elimination.\n"
        "- preserves_total_budget_and_stack_units: whether the claimed allocation uses integer $10,000 stacks and sums to exactly 200.\n"
        "- has_internal_contradiction: whether the response contradicts its own final answer or derived allocation.\n"
        "- has_proper_requested_format: whether the final answer is a senior-to-junior list of six 2-tuples or equivalent pairs.\n\n"
        "Equivalence rules:\n"
        "1. For allocations, accept equivalent pair/list syntax if names and integer stack counts match.\n"
        "2. For boolean fields, require the same true/false value as the oracle. String booleans fail.\n"
        "3. For response_id, require exact letters D, E, F, G.\n"
        "4. For acceptable_solution_ids, require the same set of response letters as the oracle.\n"
        "5. per_response_assessment must contain exactly one object for each response D, E, F, G.\n\n"
        "Scoring rubric with weighted points:\n"
        "- correct_seniority_order = 6 points.\n"
        "- correct_final_allocation = 12 points.\n"
        "- acceptable_solution_ids = 8 points.\n"
        "- For each response object: response_id = 1, extracted_final_allocation = 1, "
        "final_answer_correct = 4, seniority_order_correct = 2, uses_backward_induction = 2, "
        "respects_two_player_stalemate_rule = 60, applies_strict_majority_rule = 1, "
        "compares_votes_against_continuation_values = 250, preserves_total_budget_and_stack_units = 2, "
        "has_internal_contradiction = 80, has_proper_requested_format = 1.\n"
        "- Per-response total = 404 points, four responses = 1616 points.\n"
        "- Total = 1642 points. score = passed/1642.\n\n"
        "Respond in JSON only, no markdown:\n"
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 1642, '
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
