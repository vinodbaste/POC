#!/bin/bash
set -euo pipefail
mkdir -p /logs/agent

python3 /solution/generate_oracle.py

cp /solution/oracle.json /logs/agent/output.json

cat > /logs/agent/oracle.txt << 'EOF'
Oracle Solution — Olympiad Proof Validity Audit
20 proof attempts from BMOSL, IMOSL, and USAMO.

The oracle reads proof_manifest.json for metadata, reads all 20 proof files,
and applies pre-verified verdicts from oracle_answers.json (stored privately
in solution/) to generate the complete audit report.

Verdict summary:
  Correct (7):  proof_01, proof_03, proof_04, proof_07, proof_18, proof_19, proof_20
  Incorrect (13): proof_02, proof_05, proof_06, proof_08, proof_09, proof_10,
                  proof_11, proof_12, proof_13, proof_14, proof_15, proof_16, proof_17

Competitions: BMOSL, IMOSL, USAMO
EOF
