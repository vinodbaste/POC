#!/bin/bash
# Reference solver: emit the canonical oracle as the agent output.
# This documents the exact target structure scored by tests/judge.py and is used
# to confirm the verifier returns reward 1.0 on the gold answer (exact-match
# fast-path). The real gold statistics are derived in
# solution/compute_gold_stats.py from environment/input_artifacts/attitude.csv.

set -euo pipefail

mkdir -p /logs/agent

cat > /logs/agent/output.json <<'JSON'
{
  "gold_slope_x1000": 755,
  "acceptable_solution_ids": ["A", "G", "H"],
  "per_response_assessment": [
    {"response_id": "A", "final_answer_correct": true, "failure_reasons": []},
    {"response_id": "B", "final_answer_correct": true, "failure_reasons": ["F4"]},
    {"response_id": "C", "final_answer_correct": false, "failure_reasons": ["F6"]},
    {"response_id": "D", "final_answer_correct": false, "failure_reasons": ["F2", "F4"]},
    {"response_id": "E", "final_answer_correct": false, "failure_reasons": ["F3", "F4", "F5"]},
    {"response_id": "F", "final_answer_correct": false, "failure_reasons": ["F3"]},
    {"response_id": "G", "final_answer_correct": true, "failure_reasons": []},
    {"response_id": "H", "final_answer_correct": true, "failure_reasons": []},
    {"response_id": "I", "final_answer_correct": false, "failure_reasons": ["F5", "F6"]},
    {"response_id": "J", "final_answer_correct": false, "failure_reasons": ["F1", "F4"]},
    {"response_id": "K", "final_answer_correct": true, "failure_reasons": ["F5"]},
    {"response_id": "L", "final_answer_correct": false, "failure_reasons": ["F1"]}
  ]
}
JSON

echo "Wrote /logs/agent/output.json"
