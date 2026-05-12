#!/bin/bash
set -euo pipefail

python3 /solution/generate_oracle.py

cp /solution/oracle.json /logs/agent/output.json
