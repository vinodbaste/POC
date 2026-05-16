#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier /logs/agent /logs/artifacts

echo "TEST_SH_VERSION=universal-reward-paths"

python3 /tests/judge.py \
  --agent-output /logs/agent/output.json \
  --oracle /tests/oracle.json \
  --reward-out /logs/verifier/reward.json \
  --details-out /logs/verifier/details.json \
  > /logs/verifier/test-output.log 2>&1

exit_code=$?

cat /logs/verifier/test-output.log

if [ ! -f /logs/verifier/reward.json ]; then
  printf '{"reward": 0.0}\n' > /logs/verifier/reward.json
  {
    echo "Score: 0.0"
    echo
    echo "judge.py failed before writing reward.json; exit_code=${exit_code}"
    echo
    cat /logs/verifier/test-output.log
  } > /logs/agent/judge_justification.txt
fi

python3 - <<'PY'
import json
from pathlib import Path

primary = Path("/logs/verifier/reward.json")
try:
    data = json.loads(primary.read_text(encoding="utf-8"))
    reward = float(data.get("reward", 0.0))
except Exception:
    reward = 0.0

json_payload = json.dumps({"reward": reward}) + "\n"
txt_payload = str(reward) + "\n"

paths = [
    Path("/logs/verifier/reward.json"),
    Path("/logs/verifier/reward.txt"),
    Path("/logs/verifier/score.json"),
    Path("/logs/verifier/score.txt"),
    Path("/logs/agent/reward.json"),
    Path("/logs/agent/reward.txt"),
    Path("/logs/artifacts/reward.json"),
    Path("/logs/artifacts/reward.txt"),
    Path("/logs/reward.json"),
    Path("/logs/reward.txt"),
]

for p in paths:
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix == ".json":
            p.write_text(json_payload, encoding="utf-8")
        else:
            p.write_text(txt_payload, encoding="utf-8")
    except Exception as e:
        print(f"Could not write {p}: {e}")

print(f"FINAL_REWARD={reward}")
PY

echo "=== reward files before sync/sleep ==="
find /logs -maxdepth 3 \( -name "reward.json" -o -name "reward.txt" -o -name "score.json" -o -name "score.txt" \) -print -exec ls -l {} \; -exec cat {} \; || true

sync

echo "Sleeping 5 seconds before Harbor reward collection..."
sleep 5

echo "=== reward files after sleep ==="
find /logs -maxdepth 3 \( -name "reward.json" -o -name "reward.txt" -o -name "score.json" -o -name "score.txt" \) -print -exec ls -l {} \; -exec cat {} \; || true

exit 0
