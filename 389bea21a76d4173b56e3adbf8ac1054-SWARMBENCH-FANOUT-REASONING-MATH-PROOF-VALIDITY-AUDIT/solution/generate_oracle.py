import json
import os
import collections

# Verdicts stored privately in solution/ — not accessible to regular agents
ANSWERS_PATH = "/solution/oracle_answers.json"
if not os.path.exists(ANSWERS_PATH):
    ANSWERS_PATH = "solution/oracle_answers.json"

# Manifest (metadata only, no verdicts) from environment/
MANIFEST_PATH = "/input_artifacts/proof_manifest.json"
if not os.path.exists(MANIFEST_PATH):
    MANIFEST_PATH = "environment/input_artifacts/proof_manifest.json"

# Proof files directory
PROOFS_DIR = "/input_artifacts/proofs"
if not os.path.exists(PROOFS_DIR):
    PROOFS_DIR = "environment/input_artifacts/proofs"

answers  = json.load(open(ANSWERS_PATH))
manifest = json.load(open(MANIFEST_PATH))

# Read each proof file to confirm it exists and gather metadata
meta = {}
for entry in manifest:
    aid = entry["artifact_id"]
    proof_path = os.path.join(PROOFS_DIR, f"{aid}.md")
    with open(proof_path) as f:
        _ = f.read()  # read the full proof (required by instruction)
    meta[aid] = {
        "problem_id":  entry["problem_id"],
        "competition": entry["competition"],
    }

# Build artifact_audits sorted by artifact_id
artifact_audits = sorted(
    [
        {
            "artifact_id": aid,
            "problem_id":  meta[aid]["problem_id"],
            "competition": meta[aid]["competition"],
            "verdict":     answers[aid]["verdict"],
            "first_material_issue_summary": answers[aid]["first_material_issue_summary"],
        }
        for aid in answers
    ],
    key=lambda x: x["artifact_id"],
)

# Compute summary fields
correct_ids   = sorted([a["problem_id"] for a in artifact_audits if a["verdict"] == "correct"])
incorrect_ids = sorted([a["problem_id"] for a in artifact_audits if a["verdict"] == "incorrect"])
competitions  = sorted(set(a["competition"] for a in artifact_audits))

oracle = {
    "artifact_audits": artifact_audits,
    "summary": {
        "correct_count":       len(correct_ids),
        "incorrect_count":     len(incorrect_ids),
        "competitions_covered": competitions,
        "correct_problem_ids":  correct_ids,
        "incorrect_problem_ids": incorrect_ids,
    },
}

output_path = (
    "/solution/oracle.json"
    if os.path.exists("/solution")
    else "solution/oracle.json"
)

with open(output_path, "w") as f:
    json.dump(oracle, f, indent=2)
