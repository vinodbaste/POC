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
        "Grade the agent output against the gold oracle for this OlymMATH combinatorics-audit task.\n"
        "Both are JSON objects. The oracle is authoritative; the agent's output should be scored against it.\n\n"
        f"ORACLE:\n{json.dumps(oracle, separators=(',', ':'))}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_output, separators=(',', ':'))}\n\n"
        "Total: 100 points. Compute integer 'passed' (0-100) and float score = passed / 100.\n\n"
        "TOP-LEVEL KEY CHECK (gating):\n"
        "- The agent output MUST have exactly these four top-level keys: problem_id, gold_final_answer, "
        "solution_audits, cross_solution_summary. If any key is missing, set passed = 0 and score = 0.0 "
        "and return immediately.\n"
        "- solution_audits must be a list with exactly 15 entries, ordered alphabetically by solution_id "
        "(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O). If not 15 entries OR not alphabetically ordered, "
        "cap per-solution scoring at half credit (multiply per-solution points by 0.5).\n\n"
        "PER-SOLUTION SCORING (max 4 points each, 15 solutions, 60 points total):\n"
        "Match each agent solution_audits entry against the oracle entry with the same solution_id.\n"
        "  - 1 point if extracted_answer matches oracle's extracted_answer (literal string compare; allow "
        "minor whitespace differences). For oracle entry with extracted_answer='2^{44}', accept variants "
        "like '2^44', '2^{44}', '17592186044416'. For empty string entries, require empty or close.\n"
        "  - 1 point if final_answer_correct (bool) matches oracle.\n"
        "  - 1 point if verdict matches oracle exactly.\n"
        "  - 1 point if at least 3 of the 4 booleans (logical_chain_valid, proof_complete, "
        "contains_wrong_math_claim, repairability matches 'n/a' iff verdict='correct') agree with oracle.\n\n"
        "FATAL-ERROR SCORING (max 24 points; 2 points each for the 11 non-correct solutions; "
        "1 point each for the 4 correct solutions having first_fatal_error = null and repairability = 'n/a'):\n"
        "For oracle verdict = 'correct' (solutions D, F, K, N): award 1 point if agent's first_fatal_error "
        "is JSON null AND repairability is 'n/a', 0 otherwise.\n"
        "For oracle verdict in {'incorrect', 'partially_correct'} (B, A, C, E, G, H, I, J, L, M, O — 11 "
        "solutions): award up to 2 points:\n"
        "  - 1 point if agent's first_fatal_error.error_type matches oracle's (semantic match accepted: "
        "treat 'arithmetic_error' and 'invalid_logical_step' as substitutable for solutions G, J, M; "
        "treat 'pattern_extrapolation_unsupported' and 'false_math_claim' as substitutable for H and O).\n"
        "  - 1 point if agent's first_fatal_error.explanation captures the same mathematical reason as "
        "oracle's (semantic similarity, not verbatim).\n\n"
        "LABEL SCORING (max 9 points; 0.5 points each for failure_labels coverage + 0.1 each for "
        "domain_specific_labels coverage per solution, summed):\n"
        "For each non-correct solution, award 0.6 points if the agent's failure_labels include the "
        "primary oracle label (the one most central to the error: 'arithmetic_error' for G/J/M, "
        "'pattern_extrapolation_unsupported' for H/O, 'inconsistent_boxing' for I, 'repetition_loop' for "
        "B/C, 'false_math_claim' for A/E/L). Allow agent to include extra labels. For solutions D/F/K/N "
        "(correct), award 0.6 points if failure_labels and domain_specific_labels are both empty lists.\n"
        "Award up to 9 points total proportionally across all 15 solutions.\n\n"
        "CROSS-SOLUTION SUMMARY SCORING (max 7 points):\n"
        "  - 1 point if gold_final_answer = '948' exactly.\n"
        "  - 1 point if problem_id = 'olymmath-easy-0-en-combinatorics-audit'.\n"
        "  - 1 point if cross_solution_summary.best_solution_id is in {'N', 'F', 'K', 'D'} (any of the 4 "
        "correct solutions is acceptable; prefer N or F).\n"
        "  - 1 point if cross_solution_summary.solutions_with_correct_recurrence_wrong_arithmetic covers "
        "{G, J, M} as a set (allow up to 2 extras for partial credit 0.5).\n"
        "  - 1 point if cross_solution_summary.solutions_with_incoherent_or_truncated_reasoning includes "
        "B (and at most 1 other; B alone is canonical).\n"
        "  - 1 point if cross_solution_summary.solutions_relying_on_unsupported_pattern_extrapolation "
        "covers {H, I, O} as a set.\n"
        "  - 1 point for common_failure_modes coverage: the oracle names 4 modes (power-of-two leaps, "
        "correct-recurrence-wrong-arithmetic, deterministic-chain misconception, incoherent/truncated). "
        "Award 0.25 per mode that is captured semantically in any of the agent's common_failure_modes "
        "strings.\n\n"
        "Total maximum: 60 + 24 + 9 + 7 = 100 points.\n"
        "Compute passed = sum of points awarded (round to nearest integer 0-100), score = passed / 100.\n\n"
        "Return ONE JSON object only. Keep justification under 600 characters: list per-section subtotals "
        "(per-solution, fatal-error, label, cross-summary) and at most 3 sample sub-issues (e.g. 'A "
        "verdict=incorrect agrees, but failure_labels missing pattern_extrapolation_unsupported'). DO NOT "
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
