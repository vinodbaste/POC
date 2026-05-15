import argparse
import json
import os
import re
import urllib.error
import urllib.request


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return text[start:end + 1]
    return text


def call_fireworks(messages, max_tokens=4000, timeout=240):
    payload = {
        "model": "accounts/fireworks/models/kimi-k2p5",
        "messages": messages,
        "temperature": 0,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_object"},
    }
    request = urllib.request.Request(
        "https://api.fireworks.ai/inference/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {os.environ['FIREWORKS_API_KEY']}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = json.loads(response.read().decode("utf-8"))
    return body.get("choices", [{}])[0].get("message", {}).get("content", "") or ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    args = parser.parse_args()

    justification_path = "/logs/agent/judge_justification.txt"

    try:
        raw = open(args.agent_output).read()
        agent_output = json.loads(extract_json(raw))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid JSON: {e}")
        return

    oracle = json.load(open(args.oracle))

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    prompt = (
        "Grade the agent output against the gold oracle for this tetrahedron-incenter claim-audit task.\n"
        "Both are JSON objects following the schema described in the agent's instruction. The oracle is "
        "authoritative; the agent's output should be scored against it.\n\n"
        f"ORACLE:\n{json.dumps(oracle, separators=(',', ':'))}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, separators=(',', ':'))}\n\n"
        "Total: 100 points. Compute integer 'passed' (0-100) and float score = passed / 100.\n\n"
        "TOP-LEVEL KEY CHECK (gating):\n"
        "- The agent output MUST have exactly these three top-level keys: problem_id, gold_final_answer, "
        "solution_audits, cross_solution_summary. If any key is missing, set passed = 0 and score = 0.0 "
        "and return immediately — the structure is non-conformant.\n"
        "- solution_audits must be a list with exactly 7 entries, ordered alphabetically by solution_id "
        "(A, B, C, D, E, F, G). If not 7 entries OR not alphabetically ordered, cap per-solution scoring "
        "at half credit (multiply the per-solution points by 0.5).\n\n"
        "PER-SOLUTION SCORING (max 7 points each, 7 solutions, 49 points total):\n"
        "Match each agent solution_audits entry against the oracle entry with the same solution_id. "
        "For each solution, award:\n"
        "  - 2 points if claimed_set is exactly the oracle's claimed_set (as a set; order is required "
        "alphabetical but treat order errors as -0.5 not full loss).\n"
        "  - 1 point if verdict matches oracle.\n"
        "  - 0.5 points if final_answer_correct (bool) matches oracle.\n"
        "  - 0.5 points if contains_wrong_math_claim (bool) matches oracle.\n"
        "  - 0.5 points if logical_chain_valid matches AND 0.5 points if proof_complete matches.\n"
        "  - 1 point if repairability matches oracle exactly.\n"
        "  - 1 point if failure_labels coverage is reasonable: award 1 if the agent's labels include "
        "all the labels in the oracle's failure_labels (allow extra agent labels, just not missing ones); "
        "0.5 if a strict majority overlap; 0 otherwise.\n\n"
        "FATAL-ERROR SCORING (max 5 points per non-correct solution; 5 solutions B/C/E/F/G; 25 points; "
        "plus 2 points each for the 2 correct solutions A/D having first_fatal_error = null; 4 points; "
        "total 29 points):\n"
        "For oracle verdict = 'correct' (solutions A, D): award 2 points if agent's first_fatal_error is "
        "JSON null (or absent), 0 otherwise.\n"
        "For oracle verdict in {'incorrect', 'partially_correct'} (solutions B, C, E, F, G): award up to "
        "5 points:\n"
        "  - 2 points if agent's first_fatal_error.error_type matches oracle's (semantic match accepted: "
        "treat 'incomplete_proof' and 'underjustified_step' as substitutable; treat 'false_math_claim' "
        "and 'wrong_theorem_application' as substitutable; require an exact match otherwise).\n"
        "  - 1 point if agent's first_fatal_error.location plausibly points to the same passage as "
        "oracle's (semantic: agent should name the same statement/step being audited).\n"
        "  - 2 points if agent's first_fatal_error.explanation captures the same mathematical reason as "
        "oracle's (semantic similarity, not verbatim).\n\n"
        "CROSS-SOLUTION SUMMARY SCORING (max 18 points total):\n"
        "  - 2 points if gold_final_answer matches oracle exactly (string '{a, b, c, d, e}').\n"
        "  - 1 point if problem_id matches oracle ('cmo2026-p4-claims-audit').\n"
        "  - 3 points if cross_solution_summary.best_solution_id is 'D'.\n"
        "  - 3 points if cross_solution_summary.solutions_with_correct_gtfa_but_invalid_proof is exactly "
        "['C']. Award 1 if it contains C plus extras; 0 otherwise.\n"
        "  - 3 points if cross_solution_summary.solutions_with_valid_core_idea covers exactly "
        "{A, B, C, D} (as a set). Award 1.5 if it contains all 4 plus extras; 0.5 if it contains 3 of 4; "
        "0 otherwise.\n"
        "  - 6 points for cross_solution_summary.common_failure_modes coverage: the oracle lists 4 modes "
        "(unconstructed-counterexample-for-(a), false-insphere-touches-face-incenter-claim, "
        "missed-volume-to-distance-translation, no-explicit-use-of-acuteness). Award 1.5 points per oracle "
        "mode that is captured in any of the agent's common_failure_modes strings (semantic match, not "
        "verbatim).\n\n"
        "FORMAT BONUS (max 4 points):\n"
        "  - 1 point if every letter array (claimed_set values) uses only lowercase letters from a-h.\n"
        "  - 1 point if every claimed_set is alphabetically sorted.\n"
        "  - 1 point if solution_audits has exactly 7 entries.\n"
        "  - 1 point if first_fatal_error is JSON null exactly for verdict='correct' entries.\n\n"
        "Total maximum: 49 + 29 + 18 + 4 = 100 points.\n"
        "Compute passed = sum of points awarded (round to nearest integer 0-100), score = passed / 100.\n\n"
        "Return ONE JSON object only. Keep justification under 600 characters: list per-section subtotals "
        "(per-solution, fatal-error, cross-summary, format) and at most 3 sample sub-issues. DO NOT "
        "enumerate every field. Schema: "
        '{"score": <float 0.0-1.0>, "passed": <int>, "total": 100, "justification": "<short summary>"}'
    )

    messages = [
        {"role": "system", "content": "Respond with one valid JSON object only. Keep justification under 600 characters. No prose outside the JSON."},
        {"role": "user", "content": prompt},
    ]

    try:
        raw = call_fireworks(messages, max_tokens=4000)
    except (urllib.error.URLError, TimeoutError, KeyError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open(justification_path, "w") as f:
            f.write(f"Score: 0.0\n\nJudge request failed: {e}")
        return

    try:
        result = json.loads(extract_json(raw))
    except json.JSONDecodeError:
        repair_messages = [
            {"role": "system", "content": "Convert the user content into one valid JSON object only. Do not add commentary."},
            {"role": "user", "content": (
                "The following model output was supposed to follow this schema exactly:\n"
                '{"score": <float 0.0-1.0>, "passed": <int>, "total": 100, "justification": "<short>"}\n\n'
                "Convert it to valid JSON without changing the meaning.\n\n"
                f"MODEL OUTPUT:\n{raw[:6000]}"
            )},
        ]
        try:
            repaired_raw = call_fireworks(repair_messages, max_tokens=800, timeout=180)
            result = json.loads(extract_json(repaired_raw))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            json.dump({"reward": 0.0}, open(args.reward_out, "w"))
            with open(justification_path, "w") as f:
                f.write(f"Score: 0.0\n\nJudge parse error: {e}\nRaw: {raw[:1000]}")
            return

    score = float(result.get("score", 0.0))
    json.dump({"reward": score}, open(args.reward_out, "w"))
    with open(justification_path, "w") as f:
        f.write(
            f"Score: {score} ({result.get('passed', '?')}/{result.get('total', 100)} passed)\n\n"
            f"{result.get('justification', '')}"
        )


if __name__ == "__main__":
    main()
