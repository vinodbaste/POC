#!/bin/bash
set -euo pipefail

python3 /solution/generate_oracle.py

cp /solution/oracle.json /logs/agent/output.json

cat > /logs/agent/oracle.txt << 'EOF'
Oracle Solution -- IMO-GradingBench Solution-Grading Audit

150 candidate olympiad proof responses sourced from Google DeepMind's
IMO-GradingBench (gradingbench.csv). Each artifact contains a problem,
a reference solution, grading guidelines, and a candidate response.

The oracle reads /solution/oracle_answers.json (which stores the gold
predicted_grade per artifact, derived from the source CSV's Points
column mapped to the 4-class IMO-Bench convention) and the manifest
/input_artifacts/artifact_manifest.json (for grading_id, problem_id,
imo_area), then builds the full structured output with shard summaries
and a global summary of grade counts, area counts, grade-by-area
cross-tab, and per-grade artifact lists.

Grade-class mapping from source Points:
  0       -> Incorrect
  1, 2, 3 -> Partial
  4, 5, 6 -> Almost
  7       -> Correct

Shard layout (15 shards x 10 artifacts):
  shard_01: artifact_001 - artifact_010
  shard_02: artifact_011 - artifact_020
  shard_03: artifact_021 - artifact_030
  shard_04: artifact_031 - artifact_040
  shard_05: artifact_041 - artifact_050
  shard_06: artifact_051 - artifact_060
  shard_07: artifact_061 - artifact_070
  shard_08: artifact_071 - artifact_080
  shard_09: artifact_081 - artifact_090
  shard_10: artifact_091 - artifact_100
  shard_11: artifact_101 - artifact_110
  shard_12: artifact_111 - artifact_120
  shard_13: artifact_121 - artifact_130
  shard_14: artifact_131 - artifact_140
  shard_15: artifact_141 - artifact_150
EOF
