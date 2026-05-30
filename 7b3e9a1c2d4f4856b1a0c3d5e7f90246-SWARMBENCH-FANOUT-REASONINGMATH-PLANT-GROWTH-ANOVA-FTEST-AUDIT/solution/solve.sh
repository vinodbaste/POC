#!/bin/bash
set -euo pipefail
# Reference solver: emit the canonical oracle as the agent output.
mkdir -p /logs/agent
cat > /logs/agent/output.json <<'JSON'
{
  "gold_F_x1000": 4846,
  "acceptable_solution_ids": ["A", "G"],
  "per_response_assessment": [
    {"response_id": "A", "final_answer_correct": true, "failure_reasons": []},
    {"response_id": "B", "final_answer_correct": true, "failure_reasons": ["C6"]},
    {"response_id": "C", "final_answer_correct": false, "failure_reasons": ["C6"]},
    {"response_id": "D", "final_answer_correct": false, "failure_reasons": ["C2"]},
    {"response_id": "E", "final_answer_correct": false, "failure_reasons": ["C2", "C4"]},
    {"response_id": "F", "final_answer_correct": false, "failure_reasons": ["C1"]},
    {"response_id": "G", "final_answer_correct": true, "failure_reasons": []},
    {"response_id": "H", "final_answer_correct": false, "failure_reasons": ["C3"]},
    {"response_id": "I", "final_answer_correct": false, "failure_reasons": ["C5", "C6"]},
    {"response_id": "J", "final_answer_correct": false, "failure_reasons": ["C4", "C6"]}
  ]
}
JSON
cat /logs/agent/output.json
echo "Oracle solution applied."
