#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

python3 -m pip install --no-cache-dir openai==1.99.9

python3 /tests/judge.py \
  --agent-output /logs/agent/output.json \
  --oracle /tests/oracle.json \
  --reward-out /logs/verifier/reward.json
