"""LLM-judge verifier for the BEETLE-PRISM hex-prism shortest-surface-path audit.

Pipeline:
  1. Fail-closed read of /logs/agent/output.json (any IO/JSON error -> 0.0).
  2. Structural hard-fail gates: top-level keys subset of allowed,
     per_response_assessment is a 9-element list in alphabetical A..I order,
     each entry has exactly the three required keys with the correct value types.
     Any violation -> reward 0.0.
  3. Exact-match fast-path: agent == oracle bit-for-bit -> reward 1.0 (no LLM call).
  4. LLM judge with the 380-point all-or-nothing rubric.  Cap at 0.99 per the
     llm-judge cap rule (only oracle copies earn 1.0).
  5. Any LLM/parse/network error -> reward 0.0 (no fail-open).
"""

from __future__ import annotations

import argparse
import json
import os
import re
from typing import Any

ALLOWED_TOP_LEVEL_KEYS = {
    "gold_distance_squared_decomposition",
    "small_case_anchor_results",
    "acceptable_solution_ids",
    "per_response_assessment",
}

REQUIRED_RESPONSE_KEYS = {
    "response_id",
    "final_answer_correct",
    "failure_reasons",
}

EXPECTED_ANCHOR_IDS = (
    "anchor_a1_h1",
    "anchor_a1_h2",
    "anchor_a2_h1",
    "anchor_a2_h3",
    "anchor_a3_h2",
)

ALLOWED_FAILURE_CODES = {"F1", "F2", "F3", "F4", "F5"}
EXPECTED_RESPONSE_IDS = list("ABCDEFGHI")
TOTAL_POINTS = 410  # 100 + 30 + 10 + 9 * 30


def _write_reward(reward_path: str, reward: float) -> None:
    os.makedirs(os.path.dirname(reward_path), exist_ok=True)
    with open(reward_path, "w", encoding="utf-8") as f:
        json.dump({"reward": float(reward)}, f)


def _write_justification(text: str) -> None:
    just_path = "/logs/agent/judge_justification.txt"
    try:
        os.makedirs(os.path.dirname(just_path), exist_ok=True)
        with open(just_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


def _structural_gate(agent: Any) -> tuple[bool, str]:
    if not isinstance(agent, dict):
        return False, "agent output is not a JSON object"
    extra = set(agent.keys()) - ALLOWED_TOP_LEVEL_KEYS
    if extra:
        return False, (
            f"forbidden extra top-level keys: {sorted(extra)}; "
            f"only {sorted(ALLOWED_TOP_LEVEL_KEYS)} are allowed"
        )
    missing = ALLOWED_TOP_LEVEL_KEYS - set(agent.keys())
    if missing:
        return False, f"missing required top-level keys: {sorted(missing)}"
    g = agent.get("gold_distance_squared_decomposition")
    if not isinstance(g, dict):
        return False, "gold_distance_squared_decomposition is not a JSON object"
    if set(g.keys()) != {"rational_part", "radical_coefficient_sqrt3"}:
        return False, (
            "gold_distance_squared_decomposition must have exactly the keys "
            "{rational_part, radical_coefficient_sqrt3}"
        )
    for k in ("rational_part", "radical_coefficient_sqrt3"):
        if not isinstance(g[k], int) or g[k] < 0:
            return False, f"gold_distance_squared_decomposition.{k} must be a non-negative integer"
    anchors = agent.get("small_case_anchor_results")
    if not isinstance(anchors, dict):
        return False, "small_case_anchor_results is not a JSON object"
    if set(anchors.keys()) != set(EXPECTED_ANCHOR_IDS):
        return False, (
            f"small_case_anchor_results keys must be exactly "
            f"{sorted(EXPECTED_ANCHOR_IDS)}; got {sorted(anchors.keys())}"
        )
    for aid, av in anchors.items():
        if not isinstance(av, dict) or set(av.keys()) != {"rational_part", "radical_coefficient_sqrt3"}:
            return False, (
                f"small_case_anchor_results[{aid}] must be an object with exactly "
                f"the keys {{rational_part, radical_coefficient_sqrt3}}"
            )
        for k in ("rational_part", "radical_coefficient_sqrt3"):
            if not isinstance(av[k], int) or av[k] < 0:
                return False, (
                    f"small_case_anchor_results[{aid}].{k} must be a non-negative integer"
                )
    ids = agent.get("acceptable_solution_ids")
    if not isinstance(ids, list) or not all(isinstance(x, str) for x in ids):
        return False, "acceptable_solution_ids must be a list of strings"
    pra = agent.get("per_response_assessment")
    if not isinstance(pra, list):
        return False, "per_response_assessment is not a JSON array"
    if len(pra) != len(EXPECTED_RESPONSE_IDS):
        return False, (
            f"per_response_assessment has {len(pra)} entries; "
            f"expected {len(EXPECTED_RESPONSE_IDS)}"
        )
    for i, (entry, expected_id) in enumerate(zip(pra, EXPECTED_RESPONSE_IDS)):
        if not isinstance(entry, dict):
            return False, f"per_response_assessment[{i}] is not a JSON object"
        if set(entry.keys()) != REQUIRED_RESPONSE_KEYS:
            extra_k = set(entry.keys()) - REQUIRED_RESPONSE_KEYS
            missing_k = REQUIRED_RESPONSE_KEYS - set(entry.keys())
            return False, (
                f"per_response_assessment[{i}] key mismatch: "
                f"extra={sorted(extra_k)}, missing={sorted(missing_k)}; required keys are "
                f"{sorted(REQUIRED_RESPONSE_KEYS)}"
            )
        if entry["response_id"] != expected_id:
            return False, (
                f"per_response_assessment[{i}].response_id = {entry['response_id']!r}; "
                f"expected {expected_id!r} (must be in alphabetical order A..I)"
            )
        if not isinstance(entry["final_answer_correct"], bool):
            return False, (
                f"per_response_assessment[{i}].final_answer_correct must be boolean"
            )
        fr = entry["failure_reasons"]
        if not isinstance(fr, list) or not all(isinstance(x, str) for x in fr):
            return False, (
                f"per_response_assessment[{i}].failure_reasons must be a list of strings"
            )
        for code in fr:
            if code not in ALLOWED_FAILURE_CODES:
                return False, (
                    f"per_response_assessment[{i}].failure_reasons contains forbidden "
                    f"code {code!r}; allowed: {sorted(ALLOWED_FAILURE_CODES)}"
                )
    return True, "structural gates passed"


def _build_judge_prompt(agent: Any, oracle: Any) -> str:
    return (
        "You are a strict deterministic grader for the BEETLE-PRISM hex-prism "
        "shortest-surface-path audit task. Apply the 410-point rubric below "
        "EXACTLY; do not invent partial credit outside the specified formulas.\n\n"
        "ORACLE (ground truth, agent-shaped):\n"
        f"{json.dumps(oracle, indent=2)}\n\n"
        "AGENT OUTPUT:\n"
        f"{json.dumps(agent, indent=2)}\n\n"
        "Scoring rubric (total 410 points; reward = passed / 410):\n"
        "  (1) gold_distance_squared_decomposition: 100 pts iff BOTH "
        "      agent['gold_distance_squared_decomposition']['rational_part'] == "
        "      oracle's rational_part AND "
        "      agent['gold_distance_squared_decomposition']['radical_coefficient_sqrt3'] == "
        "      oracle's radical_coefficient_sqrt3 (both integer-equal). Else 0.\n"
        "  (2) small_case_anchor_results: 6 pts per anchor (5 anchors, 30 pts total). "
        "      For each of the five anchor keys "
        "      (anchor_a1_h1, anchor_a1_h2, anchor_a2_h1, anchor_a2_h3, anchor_a3_h2), "
        "      award 6 pts iff BOTH rational_part AND radical_coefficient_sqrt3 are "
        "      integer-equal to the oracle's. Else 0 for that anchor.\n"
        "  (3) acceptable_solution_ids: 10 pts iff "
        "      set(agent['acceptable_solution_ids']) == "
        "      set(oracle['acceptable_solution_ids']). Else 0.\n"
        "  (4) For each of the 9 responses A-I, 30 pts ALL-OR-NOTHING per response, "
        "      awarded if and only if ALL three of the following exactly match the "
        "      oracle entry for that response_id:\n"
        "        (a) agent entry's response_id equals oracle entry's response_id (string-equal),\n"
        "        (b) agent entry's final_answer_correct equals oracle entry's final_answer_correct (boolean-equal),\n"
        "        (c) set(agent entry's failure_reasons) equals set(oracle entry's failure_reasons) (set-equal, order-insensitive, no duplicates within a single set).\n"
        "      Otherwise that response earns 0 pts (no partial credit).\n\n"
        "passed = sum of all points awarded.\n"
        "score = max(0.0, min(1.0, passed / 410)).\n\n"
        "Respond with ONLY a JSON object, no markdown, no prose:\n"
        '{"score": <float in [0,1]>, "passed": <int>, "total": 410, '
        '"justification": "<concise breakdown, <= 300 chars>"}\n'
    )


def _llm_judge(agent: Any, oracle: Any) -> tuple[float, str]:
    from openai import OpenAI

    api_key = os.environ.get("FIREWORKS_API_KEY")
    if not api_key:
        raise RuntimeError("FIREWORKS_API_KEY not set in verifier environment")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.fireworks.ai/inference/v1",
    )
    prompt = _build_judge_prompt(agent, oracle)
    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2p5",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    raw = response.choices[0].message.content or ""
    cleaned = raw.strip()
    m = re.search(r"```(?:json)?\s*([\s\S]*?)```", cleaned)
    if m:
        cleaned = m.group(1).strip()
    parsed = json.loads(cleaned)
    score = float(parsed.get("score", 0.0))
    score = max(0.0, min(1.0, score))
    just = (
        f"LLM-judge score: {score:.4f}  "
        f"({parsed.get('passed', '?')}/{parsed.get('total', '?')} pts)\n\n"
        f"{parsed.get('justification', '')}"
    )
    return score, just


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    args = parser.parse_args()

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent = json.load(f)
        with open(args.oracle, "r", encoding="utf-8") as f:
            oracle = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        _write_reward(args.reward_out, 0.0)
        _write_justification(f"Score: 0.0\n\nFail-closed (Stage 1 - file read): {e}")
        return

    ok, gate_reason = _structural_gate(agent)
    if not ok:
        _write_reward(args.reward_out, 0.0)
        _write_justification(
            f"Score: 0.0\n\nFail-closed (Stage 2 - structural gate): {gate_reason}"
        )
        return

    if agent == oracle:
        _write_reward(args.reward_out, 1.0)
        _write_justification(
            "Score: 1.0\n\nAgent output is byte-identical to the oracle "
            "(exact-match fast-path). No LLM call required."
        )
        return

    try:
        score, justification = _llm_judge(agent, oracle)
    except Exception as e:
        _write_reward(args.reward_out, 0.0)
        _write_justification(
            f"Score: 0.0\n\nFail-closed (Stage 4 - LLM judge): {type(e).__name__}: {e}"
        )
        return

    capped = min(score, 0.99)
    _write_reward(args.reward_out, capped)
    _write_justification(
        f"Score: {capped:.4f} (LLM raw {score:.4f}, capped at 0.99)\n\n{justification}"
    )


if __name__ == "__main__":
    main()
