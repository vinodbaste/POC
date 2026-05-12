#!/usr/bin/env python3
"""Aggregate all shard results into final output JSON."""

import json

# Read artifact manifest
with open('/input_artifacts/artifact_manifest.json', 'r') as f:
    manifest = json.load(f)

# Create lookup dict by artifact_id
manifest_lookup = {item['artifact_id']: item for item in manifest}

# Shard files data
shard_files = [
    {
        "shard_id": "shard_01",
        "artifact_ids": ["artifact_001","artifact_002","artifact_003","artifact_004","artifact_005","artifact_006","artifact_007","artifact_008","artifact_009","artifact_010"],
        "artifact_audits": [
            {"artifact_id": "artifact_001", "predicted_grade": "Incorrect", "confidence_score": 5},
            {"artifact_id": "artifact_002", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_003", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_004", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_005", "predicted_grade": "Incorrect", "confidence_score": 4},
            {"artifact_id": "artifact_006", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_007", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_008", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_009", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_010", "predicted_grade": "Almost", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_02",
        "artifact_ids": ["artifact_011","artifact_012","artifact_013","artifact_014","artifact_015","artifact_016","artifact_017","artifact_018","artifact_019","artifact_020"],
        "artifact_audits": [
            {"artifact_id": "artifact_011", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_012", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_013", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_014", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_015", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_016", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_017", "predicted_grade": "Partial", "confidence_score": 2},
            {"artifact_id": "artifact_018", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_019", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_020", "predicted_grade": "Almost", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_03",
        "artifact_ids": ["artifact_021","artifact_022","artifact_023","artifact_024","artifact_025","artifact_026","artifact_027","artifact_028","artifact_029","artifact_030"],
        "artifact_audits": [
            {"artifact_id": "artifact_021", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_022", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_023", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_024", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_025", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_026", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_027", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_028", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_029", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_030", "predicted_grade": "Partial", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_04",
        "artifact_ids": ["artifact_031","artifact_032","artifact_033","artifact_034","artifact_035","artifact_036","artifact_037","artifact_038","artifact_039","artifact_040"],
        "artifact_audits": [
            {"artifact_id": "artifact_031", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_032", "predicted_grade": "Correct", "confidence_score": 4},
            {"artifact_id": "artifact_033", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_034", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_035", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_036", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_037", "predicted_grade": "Correct", "confidence_score": 4},
            {"artifact_id": "artifact_038", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_039", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_040", "predicted_grade": "Almost", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_05",
        "artifact_ids": ["artifact_041","artifact_042","artifact_043","artifact_044","artifact_045","artifact_046","artifact_047","artifact_048","artifact_049","artifact_050"],
        "artifact_audits": [
            {"artifact_id": "artifact_041", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_042", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_043", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_044", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_045", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_046", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_047", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_048", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_049", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_050", "predicted_grade": "Partial", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_06",
        "artifact_ids": ["artifact_051","artifact_052","artifact_053","artifact_054","artifact_055","artifact_056","artifact_057","artifact_058","artifact_059","artifact_060"],
        "artifact_audits": [
            {"artifact_id": "artifact_051", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_052", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_053", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_054", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_055", "predicted_grade": "Incorrect", "confidence_score": 4},
            {"artifact_id": "artifact_056", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_057", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_058", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_059", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_060", "predicted_grade": "Partial", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_07",
        "artifact_ids": ["artifact_061","artifact_062","artifact_063","artifact_064","artifact_065","artifact_066","artifact_067","artifact_068","artifact_069","artifact_070"],
        "artifact_audits": [
            {"artifact_id": "artifact_061", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_062", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_063", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_064", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_065", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_066", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_067", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_068", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_069", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_070", "predicted_grade": "Partial", "confidence_score": 3}
        ]
    },
    {
        "shard_id": "shard_08",
        "artifact_ids": ["artifact_071","artifact_072","artifact_073","artifact_074","artifact_075","artifact_076","artifact_077","artifact_078","artifact_079","artifact_080"],
        "artifact_audits": [
            {"artifact_id": "artifact_071", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_072", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_073", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_074", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_075", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_076", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_077", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_078", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_079", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_080", "predicted_grade": "Partial", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_09",
        "artifact_ids": ["artifact_081","artifact_082","artifact_083","artifact_084","artifact_085","artifact_086","artifact_087","artifact_088","artifact_089","artifact_090"],
        "artifact_audits": [
            {"artifact_id": "artifact_081", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_082", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_083", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_084", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_085", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_086", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_087", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_088", "predicted_grade": "Correct", "confidence_score": 5},
            {"artifact_id": "artifact_089", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_090", "predicted_grade": "Partial", "confidence_score": 3}
        ]
    },
    {
        "shard_id": "shard_10",
        "artifact_ids": ["artifact_091","artifact_092","artifact_093","artifact_094","artifact_095","artifact_096","artifact_097","artifact_098","artifact_099","artifact_100"],
        "artifact_audits": [
            {"artifact_id": "artifact_091", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_092", "predicted_grade": "Correct", "confidence_score": 5},
            {"artifact_id": "artifact_093", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_094", "predicted_grade": "Correct", "confidence_score": 5},
            {"artifact_id": "artifact_095", "predicted_grade": "Correct", "confidence_score": 5},
            {"artifact_id": "artifact_096", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_097", "predicted_grade": "Correct", "confidence_score": 5},
            {"artifact_id": "artifact_098", "predicted_grade": "Correct", "confidence_score": 5},
            {"artifact_id": "artifact_099", "predicted_grade": "Correct", "confidence_score": 5},
            {"artifact_id": "artifact_100", "predicted_grade": "Partial", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_11",
        "artifact_ids": ["artifact_101","artifact_102","artifact_103","artifact_104","artifact_105","artifact_106","artifact_107","artifact_108","artifact_109","artifact_110"],
        "artifact_audits": [
            {"artifact_id": "artifact_101", "predicted_grade": "Incorrect", "confidence_score": 4},
            {"artifact_id": "artifact_102", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_103", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_104", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_105", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_106", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_107", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_108", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_109", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_110", "predicted_grade": "Almost", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_12",
        "artifact_ids": ["artifact_111","artifact_112","artifact_113","artifact_114","artifact_115","artifact_116","artifact_117","artifact_118","artifact_119","artifact_120"],
        "artifact_audits": [
            {"artifact_id": "artifact_111", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_112", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_113", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_114", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_115", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_116", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_117", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_118", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_119", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_120", "predicted_grade": "Correct", "confidence_score": 5}
        ]
    },
    {
        "shard_id": "shard_13",
        "artifact_ids": ["artifact_121","artifact_122","artifact_123","artifact_124","artifact_125","artifact_126","artifact_127","artifact_128","artifact_129","artifact_130"],
        "artifact_audits": [
            {"artifact_id": "artifact_121", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_122", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_123", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_124", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_125", "predicted_grade": "Almost", "confidence_score": 4},
            {"artifact_id": "artifact_126", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_127", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_128", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_129", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_130", "predicted_grade": "Partial", "confidence_score": 3}
        ]
    },
    {
        "shard_id": "shard_14",
        "artifact_ids": ["artifact_131","artifact_132","artifact_133","artifact_134","artifact_135","artifact_136","artifact_137","artifact_138","artifact_139","artifact_140"],
        "artifact_audits": [
            {"artifact_id": "artifact_131", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_132", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_133", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_134", "predicted_grade": "Correct", "confidence_score": 5},
            {"artifact_id": "artifact_135", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_136", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_137", "predicted_grade": "Partial", "confidence_score": 2},
            {"artifact_id": "artifact_138", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_139", "predicted_grade": "Partial", "confidence_score": 3},
            {"artifact_id": "artifact_140", "predicted_grade": "Partial", "confidence_score": 4}
        ]
    },
    {
        "shard_id": "shard_15",
        "artifact_ids": ["artifact_141","artifact_142","artifact_143","artifact_144","artifact_145","artifact_146","artifact_147","artifact_148","artifact_149","artifact_150"],
        "artifact_audits": [
            {"artifact_id": "artifact_141", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_142", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_143", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_144", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_145", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_146", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_147", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_148", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_149", "predicted_grade": "Partial", "confidence_score": 4},
            {"artifact_id": "artifact_150", "predicted_grade": "Partial", "confidence_score": 4}
        ]
    }
]

# Initialize output structure
grading_audits = []
shard_summaries = []

# Summary accumulators
total_correct = 0
total_almost = 0
total_partial = 0
total_incorrect = 0
area_counts = {"Algebra": 0, "Combinatorics": 0, "Geometry": 0, "Number_Theory": 0}
grade_by_area = {
    "Algebra": {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0},
    "Combinatorics": {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0},
    "Geometry": {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0},
    "Number_Theory": {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0}
}
artifacts_by_grade = {"Correct": [], "Almost": [], "Partial": [], "Incorrect": []}
all_confidence_scores = []

# Process each shard
for shard in shard_files:
    shard_id = shard["shard_id"]
    artifact_ids = shard["artifact_ids"]
    artifact_audits = shard["artifact_audits"]
    
    # Per-shard accumulators
    shard_grade_counts = {"Correct": 0, "Almost": 0, "Partial": 0, "Incorrect": 0}
    shard_confidence_scores = []
    
    # Process each audit in the shard
    for audit in artifact_audits:
        artifact_id = audit["artifact_id"]
        predicted_grade = audit["predicted_grade"]
        confidence_score = audit["confidence_score"]
        
        # Get manifest info
        manifest_entry = manifest_lookup.get(artifact_id, {})
        grading_id = manifest_entry.get("grading_id", "")
        problem_id = manifest_entry.get("problem_id", "")
        imo_area = manifest_entry.get("imo_area", "")
        
        # Add to grading_audits
        grading_audits.append({
            "artifact_id": artifact_id,
            "grading_id": grading_id,
            "problem_id": problem_id,
            "imo_area": imo_area,
            "predicted_grade": predicted_grade,
            "confidence_score": confidence_score
        })
        
        # Update shard accumulators
        shard_grade_counts[predicted_grade] += 1
        shard_confidence_scores.append(confidence_score)
        
        # Update global accumulators
        if predicted_grade == "Correct":
            total_correct += 1
        elif predicted_grade == "Almost":
            total_almost += 1
        elif predicted_grade == "Partial":
            total_partial += 1
        elif predicted_grade == "Incorrect":
            total_incorrect += 1
        
        area_counts[imo_area] += 1
        grade_by_area[imo_area][predicted_grade] += 1
        artifacts_by_grade[predicted_grade].append(artifact_id)
        all_confidence_scores.append(confidence_score)
    
    # Calculate mean confidence for this shard
    mean_confidence = sum(shard_confidence_scores) / len(shard_confidence_scores) if shard_confidence_scores else 0
    
    # Add to shard_summaries
    shard_summaries.append({
        "shard_id": shard_id,
        "artifact_ids": artifact_ids,
        "artifact_count": len(artifact_ids),
        "grade_counts": shard_grade_counts,
        "mean_confidence": round(mean_confidence, 2)
    })

# Sort grading_audits by artifact_id (lexicographic)
grading_audits.sort(key=lambda x: x["artifact_id"])

# Sort shard_summaries by shard_id (lexicographic)
shard_summaries.sort(key=lambda x: x["shard_id"])

# Sort artifacts_by_grade lists
for grade in artifacts_by_grade:
    artifacts_by_grade[grade].sort()

# Calculate global mean confidence
global_mean_confidence = round(sum(all_confidence_scores) / len(all_confidence_scores), 2) if all_confidence_scores else 0

# Build final output
output = {
    "grading_audits": grading_audits,
    "shard_summaries": shard_summaries,
    "summary": {
        "total_artifacts": 150,
        "grade_counts": {
            "Correct": total_correct,
            "Almost": total_almost,
            "Partial": total_partial,
            "Incorrect": total_incorrect
        },
        "area_counts": area_counts,
        "grade_by_area": grade_by_area,
        "mean_confidence": global_mean_confidence,
        "artifacts_by_grade": artifacts_by_grade
    }
}

# Write output
with open('/logs/agent/output.json', 'w') as f:
    json.dump(output, f, indent=2)

print("Output written to /logs/agent/output.json")
print(f"Total grading_audits: {len(grading_audits)}")
print(f"Total shard_summaries: {len(shard_summaries)}")
print(f"Grade counts: {output['summary']['grade_counts']}")
print(f"Area counts: {output['summary']['area_counts']}")
print(f"Mean confidence: {global_mean_confidence}")
