#!/bin/bash
# Canonical solve.sh — copies the oracle.json to the agent output path.
# Required for verifier_type = "llm-judge" with the exact-match fast-path:
# when judge.py sees agent == oracle byte-for-byte, it returns reward 1.0
# without calling the LLM. The oracle solve.sh MUST score 1.0 for the task
# to pass SwarmBench's draft review.

set -euo pipefail

mkdir -p /logs/agent
cp /solution/oracle.json /logs/agent/output.json

cat /logs/agent/output.json
echo "Oracle solution applied."
