#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier /logs/agent

python3 -m pip install --quiet --no-cache-dir openai==1.93.0
python3 /tests/judge.py \
  --agent-output /logs/agent/output.json \
  --oracle /tests/oracle.json \
  --reward-out /logs/verifier/reward.json

if [ ! -f /logs/verifier/reward.json ]; then
  printf '{"reward": 0.0}\n' > /logs/verifier/reward.json
fi

exit 0
