You are auditing candidate submissions to a set-theoretic topology problem. Your job is to act as a mathematical referee.

The full problem statement and eight candidate submissions are in:

/input_artifacts/candidate_solutions.md

You must independently determine the correct solution, then audit each candidate submission A through H.

Important mathematical reminders:
- Neighborhoods in this topology are global right rays (r, infinity), not small Euclidean intervals.
- A submission with the correct final numeric answer can still have an invalid proof.
- Do not merely report the final numeric answer.

Write your final answer to:

/logs/agent/output.json

Use exactly this JSON schema and do not include extra top-level keys:

{
  "response_audits": [
    {
      "response_id": <str>,
      "final_answer_correct": <bool>,
      "proof_valid": <bool>,
      "verdict": <str>,
      "primary_error_label": <str>,
      "required_evidence_label": <str>
    }
  ]
}

Include exactly one audit object for each response A, B, C, D, E, F, G, and H.

Allowed values for verdict:
- correct
- incorrect
- correct_final_answer_but_invalid_proof

Use:
- correct only when both final_answer_correct and proof_valid are true.
- incorrect when the final answer is wrong.
- correct_final_answer_but_invalid_proof when the final answer is right but the proof is not logically valid.

Allowed values for primary_error_label:
- NO_ERROR
- GLOBAL_NEIGHBORHOOD_MISCOUNT
- FINITE_CASE_LIMIT_POINT_ERROR
- LOCAL_PAIRING_MODEL_ERROR
- OVERGENERALIZED_INFINITE_CASE
- SUPREMUM_DEFINITION_ERROR
- IMPOSSIBLE_TAIL_CONSTRUCTION
- WRONG_TOPOLOGY_TRANSFER

Allowed values for required_evidence_label:
- NO_ERROR
- GLOBAL_RAY_CARDINALITY_CHECK
- FINITE_NEIGHBORHOOD_CHECK
- PAIRING_GLOBALITY_CHECK
- COUNTABLE_COUNTEREXAMPLE_CHECK
- SUPREMUM_LEAST_UPPER_BOUND_CHECK
- COUNTABLE_COVERING_CHECK

Meaning of primary_error_label:
- NO_ERROR: no fatal error; the final answer and proof are both correct.
- GLOBAL_NEIGHBORHOOD_MISCOUNT: the argument miscounts how many points are seen by global right-ray neighborhoods.
- FINITE_CASE_LIMIT_POINT_ERROR: the argument makes a false claim about limit points of nonempty finite sets in this topology.
- LOCAL_PAIRING_MODEL_ERROR: the argument treats a paired or assigned local construction as if neighborhoods only see the assigned partner.
- OVERGENERALIZED_INFINITE_CASE: the argument makes a universal claim about all infinite bounded or unbounded sets that is not justified.
- SUPREMUM_DEFINITION_ERROR: the argument uses the wrong definition of supremum for a set of cardinals.
- IMPOSSIBLE_TAIL_CONSTRUCTION: the argument assumes a large subset of R can have finite right-ray tails in a way incompatible with countable covering by bounded intervals.
- WRONG_TOPOLOGY_TRANSFER: the argument transfers intuition from another topology into the topology stated in the problem.

Meaning of required_evidence_label:
- NO_ERROR: no error evidence is needed.
- GLOBAL_RAY_CARDINALITY_CHECK: check what a right ray contains globally, not only locally near one chosen point.
- FINITE_NEIGHBORHOOD_CHECK: check neighborhoods around points relative to a finite set.
- PAIRING_GLOBALITY_CHECK: check whether a paired construction remains valid when neighborhoods see all points above the cutoff.
- COUNTABLE_COUNTEREXAMPLE_CHECK: use or analyze a countable set that is bounded above and unbounded below.
- SUPREMUM_LEAST_UPPER_BOUND_CHECK: check the least-upper-bound definition of supremum.
- COUNTABLE_COVERING_CHECK: use or analyze the fact that R is the countable union of bounded intervals.

For each response, choose exactly one primary_error_label and exactly one required_evidence_label from the lists above.
