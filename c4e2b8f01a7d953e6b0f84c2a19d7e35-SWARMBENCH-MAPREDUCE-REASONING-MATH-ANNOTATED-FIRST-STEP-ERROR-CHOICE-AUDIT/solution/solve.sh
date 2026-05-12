#!/bin/bash
set -euo pipefail

python3 /solution/generate_oracle.py

cp /solution/oracle.json /logs/agent/output.json

cat > /logs/agent/oracle.txt << 'ORACLE'
Oracle Solution — First-Step-Error Choice Audit
28 artifacts from OlympiadBench and OmniMath (ProcessBench dataset).

Each artifact presents a multi-step LLM-generated incorrect solution with four
candidate step excerpts (A-D). Exactly one excerpt is the step where the solution
first makes an unrecoverable error. The oracle records the correct option letter
for each artifact and assembles the full structured output with shard summaries.

Competitions: OlympiadBench (16), OmniMath (12)
Year: 2024 (ProcessBench dataset)

Shard layout:
  shard_01: artifact_01 – artifact_04
  shard_02: artifact_05 – artifact_08
  shard_03: artifact_09 – artifact_12
  shard_04: artifact_13 – artifact_16
  shard_05: artifact_17 – artifact_20
  shard_06: artifact_21 – artifact_24
  shard_07: artifact_25 – artifact_28
ORACLE
