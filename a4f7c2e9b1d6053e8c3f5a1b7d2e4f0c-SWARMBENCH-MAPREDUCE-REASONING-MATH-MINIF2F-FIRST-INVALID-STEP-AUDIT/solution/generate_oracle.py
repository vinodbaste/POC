import json
import os
import collections

ANSWERS_PATH = "/solution/oracle_answers.json"
if not os.path.exists(ANSWERS_PATH):
    ANSWERS_PATH = "solution/oracle_answers.json"

MANIFEST_PATH = "/input_artifacts/artifact_manifest.json"
if not os.path.exists(MANIFEST_PATH):
    MANIFEST_PATH = "environment/input_artifacts/artifact_manifest.json"

answers  = json.load(open(ANSWERS_PATH))
manifest = json.load(open(MANIFEST_PATH))

meta = {e["artifact_id"]: e for e in manifest}

artifact_audits = sorted(
    [
        {
            "artifact_id":     aid,
            "problem_id":      meta[aid]["problem_id"],
            "competition":     meta[aid]["competition"],
            "year":            meta[aid]["year"],
            "selected_option": opt,
        }
        for aid, opt in answers.items()
    ],
    key=lambda x: x["artifact_id"],
)

audit_map = {a["artifact_id"]: a for a in artifact_audits}

SHARDS = {
    "shard_01": [f"artifact_{i:02d}" for i in range(1, 5)],
    "shard_02": [f"artifact_{i:02d}" for i in range(5, 9)],
    "shard_03": [f"artifact_{i:02d}" for i in range(9, 13)],
    "shard_04": [f"artifact_{i:02d}" for i in range(13, 17)],
    "shard_05": [f"artifact_{i:02d}" for i in range(17, 21)],
    "shard_06": [f"artifact_{i:02d}" for i in range(21, 25)],
    "shard_07": [f"artifact_{i:02d}" for i in range(25, 29)],
}

shard_summaries = []
for shard_id in sorted(SHARDS.keys()):
    ids = SHARDS[shard_id]
    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for aid in ids:
        counts[audit_map[aid]["selected_option"]] += 1
    shard_summaries.append({
        "shard_id":       shard_id,
        "artifact_ids":   ids,
        "artifact_count": len(ids),
        "choice_counts":  counts,
    })

global_choice_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
competition_counts   = collections.Counter()
year_counts          = collections.Counter()
artifacts_by_option  = {"A": [], "B": [], "C": [], "D": []}

for a in artifact_audits:
    opt = a["selected_option"]
    global_choice_counts[opt] += 1
    competition_counts[a["competition"]] += 1
    year_counts[str(a["year"])] += 1
    artifacts_by_option[opt].append(a["artifact_id"])

oracle = {
    "artifact_audits": artifact_audits,
    "shard_summaries": shard_summaries,
    "summary": {
        "total_artifacts":    len(artifact_audits),
        "choice_counts":      global_choice_counts,
        "competition_counts": dict(sorted(competition_counts.items())),
        "year_counts":        dict(sorted(year_counts.items())),
        "artifacts_by_option": {k: sorted(v) for k, v in artifacts_by_option.items()},
    },
}

output_path = (
    "/solution/oracle.json"
    if os.path.exists("/solution")
    else "solution/oracle.json"
)

with open(output_path, "w") as f:
    json.dump(oracle, f, indent=2)
