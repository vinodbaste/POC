#!/bin/bash
set -euo pipefail

mkdir -p /logs/agent

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cp "$SCRIPT_DIR/oracle.json" /logs/agent/output.json

echo "Oracle solution applied."
