#!/bin/bash
set -euo pipefail

python3 /solution/generate_oracle.py

cp /solution/oracle.json /logs/agent/output.json

cat > /logs/agent/oracle.txt << 'EOF'
Oracle Solution — First-Flaw Choice Audit
50 artifacts across BMOSL, IMOSL, and USAMO incorrect proof attempts.

The oracle reads artifact_manifest.json to determine the correct option (A/B/C/D)
for each artifact, then builds the full structured output with shard summaries
and a global summary of choice counts, competition counts, year counts, and
per-option artifact lists.

Shard layout (10 shards × 5 artifacts):
  shard_01: artifact_01 – artifact_05
  shard_02: artifact_06 – artifact_10
  shard_03: artifact_11 – artifact_15
  shard_04: artifact_16 – artifact_20
  shard_05: artifact_21 – artifact_25
  shard_06: artifact_26 – artifact_30
  shard_07: artifact_31 – artifact_35
  shard_08: artifact_36 – artifact_40
  shard_09: artifact_41 – artifact_45
  shard_10: artifact_46 – artifact_50
EOF
