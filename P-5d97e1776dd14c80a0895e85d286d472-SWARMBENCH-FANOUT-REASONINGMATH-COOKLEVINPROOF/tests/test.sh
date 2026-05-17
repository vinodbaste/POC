#!/bin/bash
set -euo pipefail
mkdir -p /logs/verifier
python3 -m pip install --no-cache-dir openai==2.32.0 >/tmp/openai-install.log 2>&1 || {
  cat /tmp/openai-install.log
  exit 1
}
python3 /tests/judge.py \
  --agent-output /logs/agent/output.json \
  --oracle /tests/oracle.json \
  --reward-out /logs/verifier/reward.json
python3 - <<'PY'
import json
from pathlib import Path

reward = json.loads(Path("/logs/verifier/reward.json").read_text())["reward"]
Path("/logs/verifier/reward.txt").write_text(str(reward))
PY
