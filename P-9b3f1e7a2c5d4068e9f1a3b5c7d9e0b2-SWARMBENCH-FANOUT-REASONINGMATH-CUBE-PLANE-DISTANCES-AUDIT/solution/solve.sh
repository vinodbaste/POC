#!/bin/bash
set -euo pipefail

mkdir -p /logs/agent
cp /solution/oracle.json /logs/agent/output.json

# Keep oracle.txt non-empty for Quality Gate static checks.
# Harbor captures oracle stdout into /logs/agent/oracle.txt.
cat /logs/agent/output.json
echo "Oracle solution applied."
