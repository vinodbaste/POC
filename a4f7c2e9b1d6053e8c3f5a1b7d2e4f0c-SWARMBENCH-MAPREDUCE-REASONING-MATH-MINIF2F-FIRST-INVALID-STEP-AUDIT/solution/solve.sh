#!/bin/bash
set -euo pipefail

python3 /solution/generate_oracle.py

cp /solution/oracle.json /logs/agent/output.json

cat > /logs/agent/oracle.txt << 'EOF'
Oracle Solution — miniF2F First-Invalid-Step Audit
28 artifacts across AIME, AMC, IMO, and MATH competition problems.

The oracle reads artifact_manifest.json for metadata and oracle_answers.json
for the correct option (A/B/C/D) for each artifact, then builds the full
structured output with shard summaries and a global summary of choice counts,
competition counts, year counts, and per-option artifact lists.

Shard layout:
  shard_01: artifact_01 – artifact_04  (AIME 1983-1986)
  shard_02: artifact_05 – artifact_08  (AIME 1987-1990)
  shard_03: artifact_09 – artifact_12  (AMC 2002-2006)
  shard_04: artifact_13 – artifact_16  (AMC 2007-2009)
  shard_05: artifact_17 – artifact_20  (IMO 1977-2001)
  shard_06: artifact_21 – artifact_24  (IMO 2003-2020)
  shard_07: artifact_25 – artifact_28  (MATH 2020)
EOF
