#!/bin/bash
set -euo pipefail

python /tests/judge.py \
  --agent-output /logs/agent/output.json \
  --oracle /tests/oracle.json \
  --reward-out /logs/verifier/reward.json
