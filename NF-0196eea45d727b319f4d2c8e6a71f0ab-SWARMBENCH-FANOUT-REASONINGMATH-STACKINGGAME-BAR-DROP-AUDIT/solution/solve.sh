#!/bin/bash
set -euo pipefail

mkdir -p /logs/agent
python3 /solution/compute_oracle.py

cat /logs/agent/output.json
