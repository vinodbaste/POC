#!/bin/bash
set -euo pipefail
# Executable verifier: Python standard library only, no third-party install.
mkdir -p /logs/verifier
python3 /tests/judge.py \
  --agent-output /logs/agent/output.json \
  --oracle /tests/oracle.json \
  --reward-out /logs/verifier/reward.json
cat /logs/verifier/reward.json
