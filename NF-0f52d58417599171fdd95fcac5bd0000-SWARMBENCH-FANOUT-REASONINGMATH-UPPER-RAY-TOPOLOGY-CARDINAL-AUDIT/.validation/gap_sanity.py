#!/usr/bin/env python3
"""Gap-math sanity check: perfect multi vs plausible single-agent output."""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from judge import FIELD_WEIGHTS, as_map_by_response_id  # noqa: E402

ORACLE_PATH = ROOT / "tests" / "oracle.json"
SINGLE_OUTPUT = (
    ROOT
    / "execution_logs"
    / "single-kimi-agent"
    / "0f52d58417599171fdd95fcac5bd0000__fDbF9wU"
    / "agent"
    / "output.json"
)
TOTAL_PER_RESPONSE = sum(FIELD_WEIGHTS.values())
FORBIDDEN_LABELS = (
    "CLEAN_PROOF",
    "RAY_NEIGHBORHOOD_UNDERCOUNT",
    "FINITE_SUBSET_LIMIT_BLINDSPOT",
    "PARTNER_BINDING_MISCONCEPTION",
    "INFINITE_CASE_OVERREACH",
    "SUPREMUM_VS_SUCCESSOR_MIXUP",
    "UNCONSTRUCTIBLE_TAIL_HYPOTHESIS",
    "MISAPPLIED_TOPOLOGY_INTUITION",
)


def score_output(agent: dict, oracle: dict) -> float:
    expected = as_map_by_response_id(oracle["response_audits"])
    actual = as_map_by_response_id(agent["response_audits"])
    passed = 0
    for rid, exp in expected.items():
        act = actual.get(rid, {})
        for field, weight in FIELD_WEIGHTS.items():
            if act.get(field) == exp.get(field):
                passed += weight
    total = len(expected) * TOTAL_PER_RESPONSE
    return passed / total


def mutate_labels(agent: dict, swaps: dict[str, str]) -> dict:
    out = copy.deepcopy(agent)
    by_id = as_map_by_response_id(out["response_audits"])
    for rid, wrong_label in swaps.items():
        by_id[rid]["primary_error_label"] = wrong_label
    out["response_audits"] = [by_id[rid] for rid in sorted(by_id)]
    return out


def qd_042_spot_check() -> list[str]:
    """QD-04.2 forbidden patterns in decomposition.yaml."""
    issues: list[str] = []
    text = (ROOT / "decomposition.yaml").read_text(encoding="utf-8")
    label_re = "|".join(FORBIDDEN_LABELS)
    patterns = [
        (rf"Submission\s+([A-H])\b.{{0,120}}\b({label_re})\b", "submission+label"),
        (rf"\b({label_re})\b.{{0,120}}Submission\s+([A-H])\b", "label+submission"),
        (r"primary code is", "primary code is"),
        (r"the label is", "the label is"),
        (r"preserving the multi-agent gap", "meta gap knowledge"),
    ]
    for pattern, name in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            issues.append(f"{name}: {match.group(0)[:100]!r}")
    return issues


def main() -> int:
    oracle = json.loads(ORACLE_PATH.read_text(encoding="utf-8"))
    perfect_multi = score_output(oracle, oracle)

    two_slip = mutate_labels(
        oracle,
        {"C": "PARTNER_BINDING_MISCONCEPTION", "D": "FINITE_SUBSET_LIMIT_BLINDSPOT"},
    )
    two_slip_score = score_output(two_slip, oracle)

    six_slip = mutate_labels(
        oracle,
        {
            "C": "PARTNER_BINDING_MISCONCEPTION",
            "D": "FINITE_SUBSET_LIMIT_BLINDSPOT",
            "B": "UNCONSTRUCTIBLE_TAIL_HYPOTHESIS",
            "E": "FINITE_SUBSET_LIMIT_BLINDSPOT",
            "H": "FINITE_SUBSET_LIMIT_BLINDSPOT",
            "G": "INFINITE_CASE_OVERREACH",
        },
    )
    six_slip_score = score_output(six_slip, oracle)

    single_agent = json.loads(SINGLE_OUTPUT.read_text(encoding="utf-8"))
    # Historical 10-submission run included I/J; score only A-H against 8-submission oracle.
    single_by_id = as_map_by_response_id(single_agent["response_audits"])
    single_8 = {
        "response_audits": [
            single_by_id[rid] for rid in sorted(single_by_id) if rid in "ABCDEFGH"
        ]
    }
    single_score = score_output(single_8, oracle)

    gap_multi_vs_single = perfect_multi - single_score
    gap_2_vs_6 = two_slip_score - six_slip_score

    print("Gap sanity validation (8 submissions A-H)")
    print("-" * 72)
    rows = [
        ("perfect multi (oracle)", perfect_multi, 0.95, 1.0),
        ("2 confusion slips (C/D swap)", two_slip_score, 0.75, 0.85),
        ("6 label slips", six_slip_score, 0.30, 0.40),
        ("single-kimi (A-H only)", single_score, 0.70, 0.80),
    ]
    all_ok = True
    for name, score, lo, hi in rows:
        ok = lo <= score <= hi
        all_ok = all_ok and ok
        print(f"{name:<32} {score:8.3f}  [{lo:.2f}, {hi:.2f}]  ok={ok}")

    gap_ok = gap_multi_vs_single >= 0.20
    gap_2_6_ok = gap_2_vs_6 >= 0.20
    print("-" * 72)
    print(
        f"gap (multi - single): {gap_multi_vs_single:.3f}  (need >= 0.20)  ok={gap_ok}"
    )
    print(f"gap (2-slip - 6-slip): {gap_2_vs_6:.3f}  (need >= 0.20)  ok={gap_2_6_ok}")
    all_ok = all_ok and gap_ok and gap_2_6_ok

    qd_issues = qd_042_spot_check()
    qd_ok = len(qd_issues) == 0
    print(f"QD-04.2 decomposition matches: {len(qd_issues)}  ok={qd_ok}")
    for item in qd_issues:
        print(f"  - {item}")
    all_ok = all_ok and qd_ok

    import yaml  # noqa: PLC0415

    yaml.safe_load((ROOT / "decomposition.yaml").read_text(encoding="utf-8"))
    json.loads(ORACLE_PATH.read_text(encoding="utf-8"))
    json.loads((ROOT / "solution" / "oracle.json").read_text(encoding="utf-8"))
    print("YAML/JSON parse: ok")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
