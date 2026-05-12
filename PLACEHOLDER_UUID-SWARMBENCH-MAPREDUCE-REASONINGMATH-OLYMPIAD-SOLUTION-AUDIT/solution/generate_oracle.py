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

TECHNIQUES = [
    "algebraic_manipulation",
    "combinatorial_counting",
    "induction",
    "inequality_application",
    "modular_arithmetic",
    "geometric_construction",
    "extremal_principle",
    "invariant_or_monovariant",
    "generating_function",
    "proof_by_contradiction",
]
COMPETITIONS = ["IMO", "USAMO", "IMOSL", "BMOSL"]


artifact_audits = sorted(
    [
        {
            "artifact_id":       aid,
            "problem_id":        meta[aid]["problem_id"],
            "competition":       meta[aid]["competition"],
            "year":              meta[aid]["year"],
            "central_technique": ans["central_technique"],
            "rigor_score":       ans["rigor_score"],
            "claim_audits":      ans["claim_audits"],
        }
        for aid, ans in answers.items()
    ],
    key=lambda x: x["artifact_id"],
)

audit_map = {a["artifact_id"]: a for a in artifact_audits}

# Shard layout: 5 shards × 4 artifacts. With only 3 artifacts seeded for review,
# we only emit the shards that have at least one artifact present.
SHARDS = {
    f"shard_{i:02d}": [f"artifact_{j:02d}" for j in range((i - 1) * 4 + 1, i * 4 + 1)]
    for i in range(1, 6)
}

shard_summaries = []
for shard_id in sorted(SHARDS.keys()):
    ids_present = [aid for aid in SHARDS[shard_id] if aid in audit_map]
    if not ids_present:
        continue
    tech_counts = {t: 0 for t in TECHNIQUES}
    rigor_sum = 0
    for aid in ids_present:
        tech_counts[audit_map[aid]["central_technique"]] += 1
        rigor_sum += audit_map[aid]["rigor_score"]
    mean_rigor = round(rigor_sum / len(ids_present), 2)
    shard_summaries.append({
        "shard_id":         shard_id,
        "artifact_ids":     ids_present,
        "artifact_count":   len(ids_present),
        "technique_counts": tech_counts,
        "mean_rigor":       mean_rigor,
    })

# Global aggregates
total_claims = sum(len(a["claim_audits"]) for a in artifact_audits)
claim_status_counts = {"verified": 0, "unjustified": 0, "incorrect": 0}
for a in artifact_audits:
    for c in a["claim_audits"]:
        claim_status_counts[c["status"]] += 1

global_tech_counts = {t: 0 for t in TECHNIQUES}
competition_counts = {c: 0 for c in COMPETITIONS}
year_counts = collections.Counter()
artifacts_by_technique = {t: [] for t in TECHNIQUES}
rigor_total = 0

for a in artifact_audits:
    tech = a["central_technique"]
    global_tech_counts[tech] += 1
    competition_counts[a["competition"]] += 1
    year_counts[str(a["year"])] += 1
    artifacts_by_technique[tech].append(a["artifact_id"])
    rigor_total += a["rigor_score"]

mean_rigor_global = round(rigor_total / len(artifact_audits), 2)

oracle = {
    "artifact_audits": artifact_audits,
    "shard_summaries": shard_summaries,
    "summary": {
        "total_artifacts":     len(artifact_audits),
        "total_claims":        total_claims,
        "claim_status_counts": claim_status_counts,
        "technique_counts":    global_tech_counts,
        "mean_rigor":          mean_rigor_global,
        "competition_counts":  competition_counts,
        "year_counts":         dict(sorted(year_counts.items())),
        "artifacts_by_technique": {t: sorted(ids) for t, ids in artifacts_by_technique.items()},
    },
}

output_path = (
    "/solution/oracle.json"
    if os.path.exists("/solution")
    else "solution/oracle.json"
)

with open(output_path, "w") as f:
    json.dump(oracle, f, indent=2)
