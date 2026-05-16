#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import math
import os
import re
from pathlib import Path
from typing import Any

LETTERS = list("ABCDEFGHI")

GLOBAL_WEIGHTS = {
    "derived_final_answer": 100.0,
}

RESPONSE_WEIGHTS = {
    "final_answer_category": 6.0,
    "gtfa_correct": 10.0,
    "spatial_reasoning_error": 2.0,
    "non_spatial_reasoning_error": 1.5,
    "calculation_error": 1.5,
    "error_codes": 4.0,
    "completeness_level": 0.5,
    "efficiency_level": 0.3,
    "latex_clarity_level": 0.2,
    "brief_justification": 0.5,
}

MAX_POINTS = sum(GLOBAL_WEIGHTS.values()) + len(LETTERS) * sum(RESPONSE_WEIGHTS.values())

ANSWER_KEYS = [
    "derived_final_answer",
    "correct_final_answer",
    "correct_final_answer_latex",
    "final_answer",
    "gtfa",
]

JUSTIFICATION_KEYS = [
    "brief_justification",
    "error_analysis",
    "justification",
    "analysis",
]


def write_reward(path: str, reward: float, justification: str, details: dict[str, Any] | None = None, details_out: str | None = None) -> None:
    reward = max(0.0, min(1.0, float(reward)))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"reward": reward}, f)

    try:
        os.makedirs("/logs/agent", exist_ok=True)
        with open("/logs/agent/judge_justification.txt", "w", encoding="utf-8") as f:
            f.write(f"Score: {reward:.6f}\n\n{justification}\n")
    except OSError:
        # Local host checks may not have a writable /logs mount. Harbor verifier
        # containers do, so keep this best-effort rather than failing scoring.
        pass

    if details_out and details is not None:
        os.makedirs(os.path.dirname(details_out), exist_ok=True)
        with open(details_out, "w", encoding="utf-8") as f:
            json.dump(details, f, indent=2, ensure_ascii=False)


def canonical_math(value: Any) -> str:
    s = str(value or "").lower()
    s = s.replace("$", "")
    s = s.replace("\\", "")
    s = s.replace("{", "").replace("}", "")
    s = s.replace(" ", "")
    s = s.replace("*", "")
    s = s.replace("(", "").replace(")", "")
    s = s.replace("^", "")
    s = s.replace("·", "")
    return s


def is_gtfa_value(value: Any) -> bool:
    s = canonical_math(value)
    # Accept "69" as a clean numeric answer (the maximum s² over the set S), with
    # optional boxed/answer wrappers. canonical_math() already strips $, \, braces,
    # spaces, *, parens, ^.
    if s == "69":
        return True
    return bool(re.search(r"(?<!\d)69(?!\d)", s))


def find_submitted_gtfa(agent: dict[str, Any]) -> tuple[bool, str]:
    for key in ANSWER_KEYS:
        if key in agent and is_gtfa_value(agent.get(key)):
            return True, key

    # Compatibility: if an agent put the correct answer in a nested summary field,
    # count GTFA as mathematically found, but schema omissions still lose per-field points.
    def walk(obj: Any, path: str = ""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                yield from walk(v, f"{path}.{k}" if path else str(k))
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                yield from walk(v, f"{path}[{i}]")
        elif isinstance(obj, (str, int, float)):
            yield path, obj

    for path, value in walk(agent):
        if is_gtfa_value(value):
            return True, path

    return False, ""


def normalize_responses(responses: Any) -> dict[str, dict[str, Any]]:
    if isinstance(responses, dict):
        out = {}
        for letter in LETTERS:
            item = responses.get(letter)
            out[letter] = item if isinstance(item, dict) else {}
        return out

    if isinstance(responses, list):
        out = {}
        for i, letter in enumerate(LETTERS):
            item = responses[i] if i < len(responses) and isinstance(responses[i], dict) else {}
            out[letter] = item
        return out

    return {letter: {} for letter in LETTERS}


def exact_score(actual: Any, expected: Any, weight: float) -> tuple[float, str]:
    ok = actual == expected
    return (weight if ok else 0.0), ("ok" if ok else f"expected={expected!r}, actual={actual!r}")


def justification_score(resp: dict[str, Any], weight: float) -> tuple[float, str]:
    for key in JUSTIFICATION_KEYS:
        value = resp.get(key)
        if isinstance(value, str) and len(value.strip()) >= 20:
            return weight, f"ok via {key}"
    return 0.0, "missing or too short"


def error_code_score(actual: Any, expected: Any, weight: float) -> tuple[float, str]:
    actual_set = set(actual) if isinstance(actual, list) else set()
    expected_set = set(expected) if isinstance(expected, list) else set()

    if not expected_set and not actual_set:
        return weight, "ok"

    if not expected_set:
        return (weight if not actual_set else 0.0), f"expected empty, actual={sorted(actual_set)}"

    # Recall-heavy overlap: missing expected codes is worse than adding extras.
    tp = len(actual_set & expected_set)
    recall = tp / len(expected_set)
    precision = tp / len(actual_set) if actual_set else 0.0
    score_fraction = 0.8 * recall + 0.2 * precision
    return weight * score_fraction, f"expected={sorted(expected_set)}, actual={sorted(actual_set)}, recall={recall:.3f}, precision={precision:.3f}"


def score_response(letter: str, agent_resp: dict[str, Any], oracle_resp: dict[str, Any]) -> tuple[float, float, dict[str, Any]]:
    awarded = 0.0
    max_points = sum(RESPONSE_WEIGHTS.values())
    fields: dict[str, Any] = {}

    for field in [
        "final_answer_category",
        "gtfa_correct",
        "spatial_reasoning_error",
        "non_spatial_reasoning_error",
        "calculation_error",
        "completeness_level",
        "efficiency_level",
        "latex_clarity_level",
    ]:
        weight = RESPONSE_WEIGHTS[field]
        pts, reason = exact_score(agent_resp.get(field), oracle_resp.get(field), weight)
        awarded += pts
        fields[field] = {
            "awarded": pts,
            "max": weight,
            "reason": reason,
        }

    pts, reason = error_code_score(
        agent_resp.get("error_codes"),
        oracle_resp.get("error_codes"),
        RESPONSE_WEIGHTS["error_codes"],
    )
    awarded += pts
    fields["error_codes"] = {
        "awarded": pts,
        "max": RESPONSE_WEIGHTS["error_codes"],
        "reason": reason,
    }

    pts, reason = justification_score(agent_resp, RESPONSE_WEIGHTS["brief_justification"])
    awarded += pts
    fields["brief_justification"] = {
        "awarded": pts,
        "max": RESPONSE_WEIGHTS["brief_justification"],
        "reason": reason,
    }

    return awarded, max_points, fields


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output", required=True)
    parser.add_argument("--oracle", required=True)
    parser.add_argument("--reward-out", required=True)
    parser.add_argument("--details-out", required=False)
    args = parser.parse_args()

    try:
        with open(args.agent_output, "r", encoding="utf-8") as f:
            agent = json.load(f)
    except Exception as e:
        write_reward(args.reward_out, 0.0, f"Agent output missing or invalid JSON: {e}", details_out=args.details_out)
        return

    with open(args.oracle, "r", encoding="utf-8") as f:
        oracle = json.load(f)

    if agent == oracle:
        details = {
            "awarded_points": MAX_POINTS,
            "max_points": MAX_POINTS,
            "score": 1.0,
            "reason": "exact oracle match",
        }
        write_reward(args.reward_out, 1.0, "Agent output exactly matches oracle.", details, args.details_out)
        return

    awarded = 0.0
    details: dict[str, Any] = {
        "global": {},
        "responses": {},
    }

    gtfa_ok, gtfa_location = find_submitted_gtfa(agent)
    gtfa_weight = GLOBAL_WEIGHTS["derived_final_answer"]
    gtfa_points = gtfa_weight if gtfa_ok else 0.0
    awarded += gtfa_points
    details["global"]["derived_final_answer"] = {
        "awarded": gtfa_points,
        "max": gtfa_weight,
        "ok": gtfa_ok,
        "location": gtfa_location,
        "submitted_top_level": agent.get("derived_final_answer"),
        "oracle": oracle.get("derived_final_answer"),
    }

    agent_responses = normalize_responses(agent.get("responses"))
    oracle_responses = normalize_responses(oracle.get("responses"))

    for letter in LETTERS:
        pts, max_pts, field_details = score_response(letter, agent_responses[letter], oracle_responses[letter])
        awarded += pts
        details["responses"][letter] = {
            "awarded": pts,
            "max": max_pts,
            "fields": field_details,
        }

    score = awarded / MAX_POINTS if MAX_POINTS else 0.0
    details["awarded_points"] = awarded
    details["max_points"] = MAX_POINTS
    details["score"] = score

    lines = [
        f"Deterministic weighted score: {awarded:.4f}/{MAX_POINTS:.4f}.",
        f"Global GTFA: {'correct' if gtfa_ok else 'incorrect'}; location={gtfa_location or 'not found'}.",
        "",
        "Per-response scores:",
    ]
    for letter in LETTERS:
        rd = details["responses"][letter]
        lines.append(f"- {letter}: {rd['awarded']:.4f}/{rd['max']:.4f}")

    write_reward(args.reward_out, score, "\n".join(lines), details, args.details_out)


if __name__ == "__main__":
    main()
