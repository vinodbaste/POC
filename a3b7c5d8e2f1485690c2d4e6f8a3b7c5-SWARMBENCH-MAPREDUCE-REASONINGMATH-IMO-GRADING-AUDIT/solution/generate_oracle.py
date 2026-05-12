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

GRADE_CLASSES = ["Correct", "Almost", "Partial", "Incorrect"]
AREAS = ["Algebra", "Combinatorics", "Geometry", "Number_Theory"]

grading_audits = []
for aid in sorted(answers.keys()):
    ans = answers[aid]
    m = meta[aid]
    grading_audits.append({
        "artifact_id":     aid,
        "grading_id":      m["grading_id"],
        "problem_id":      m["problem_id"],
        "imo_area":        m["imo_area"],
        "predicted_grade": ans["predicted_grade"],
    })

audit_map = {a["artifact_id"]: a for a in grading_audits}

SHARDS = {
    f"shard_{i:02d}": [f"artifact_{j:03d}" for j in range((i - 1) * 10 + 1, i * 10 + 1)]
    for i in range(1, 16)
}

shard_summaries = []
for shard_id in sorted(SHARDS.keys()):
    ids = SHARDS[shard_id]
    grade_counts = {g: 0 for g in GRADE_CLASSES}
    for aid in ids:
        grade_counts[audit_map[aid]["predicted_grade"]] += 1
    shard_summaries.append({
        "shard_id":       shard_id,
        "artifact_ids":   ids,
        "artifact_count": len(ids),
        "grade_counts":   grade_counts,
    })

total = len(grading_audits)
global_grade_counts = {g: 0 for g in GRADE_CLASSES}
global_area_counts = {a: 0 for a in AREAS}
grade_by_area = {a: {g: 0 for g in GRADE_CLASSES} for a in AREAS}
artifacts_by_grade = {g: [] for g in GRADE_CLASSES}

for a in grading_audits:
    g = a["predicted_grade"]
    area = a["imo_area"]
    global_grade_counts[g] += 1
    global_area_counts[area] += 1
    grade_by_area[area][g] += 1
    artifacts_by_grade[g].append(a["artifact_id"])

oracle = {
    "grading_audits": grading_audits,
    "shard_summaries": shard_summaries,
    "summary": {
        "total_artifacts":    total,
        "grade_counts":       global_grade_counts,
        "area_counts":        global_area_counts,
        "grade_by_area":      grade_by_area,
        "artifacts_by_grade": {g: sorted(ids) for g, ids in artifacts_by_grade.items()},
    },
}

output_path = (
    "/solution/oracle.json"
    if os.path.exists("/solution")
    else "solution/oracle.json"
)

with open(output_path, "w") as f:
    json.dump(oracle, f, indent=2)
