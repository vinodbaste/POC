You are auditing candidate submissions to a set-theoretic topology problem. Your job is to act as a mathematical referee.

The full problem statement and eight candidate submissions are in:

/input_artifacts/submission_packet.md

You must independently determine the correct solution, then audit each candidate submission A through H.

Important mathematical reminders:
- Neighborhoods in this topology are global upper rays (a, infinity), not small Euclidean intervals.
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

Include exactly one audit object for each submission A, B, C, D, E, F, G, and H.

Allowed values for verdict:
- fully_valid
- incorrect_answer
- answer_correct_proof_unsound

Use:
- fully_valid only when both final_answer_correct and proof_valid are true.
- incorrect_answer when the final answer is wrong.
- answer_correct_proof_unsound when the final answer is right but the proof is not logically valid.

Allowed values for primary_error_label:
- CLEAN_PROOF
- RAY_NEIGHBORHOOD_UNDERCOUNT
- FINITE_SUBSET_LIMIT_BLINDSPOT
- PARTNER_BINDING_MISCONCEPTION
- INFINITE_CASE_OVERREACH
- SUPREMUM_VS_SUCCESSOR_MIXUP
- UNCONSTRUCTIBLE_TAIL_HYPOTHESIS
- MISAPPLIED_TOPOLOGY_INTUITION

Allowed values for required_evidence_label:
- NO_CHECK_NEEDED
- RAY_CARDINALITY_VERIFICATION
- FINITE_SUBSET_NEIGHBORHOOD_TEST
- PAIR_GLOBALITY_AUDIT
- DECREASING_INTEGER_WITNESS
- LUB_DEFINITIONAL_TEST
- BOUNDED_INTERVAL_COVER_TEST

Meaning of primary_error_label:
- CLEAN_PROOF: no fatal error; the final answer and proof are both correct.
- RAY_NEIGHBORHOOD_UNDERCOUNT: the argument miscounts how many points are seen by global upper-ray neighborhoods.
- FINITE_SUBSET_LIMIT_BLINDSPOT: the argument makes a false claim about limit points of nonempty finite sets in this topology.
- PARTNER_BINDING_MISCONCEPTION: the argument treats a paired or assigned local construction as if neighborhoods only see the assigned partner.
- INFINITE_CASE_OVERREACH: the argument makes a universal claim about all infinite bounded or unbounded sets that is not justified.
- SUPREMUM_VS_SUCCESSOR_MIXUP: the argument uses the wrong definition of supremum for a set of cardinals.
- UNCONSTRUCTIBLE_TAIL_HYPOTHESIS: the argument assumes a large subset of R can have finite upper-ray tails in a way incompatible with countable covering by bounded intervals.
- MISAPPLIED_TOPOLOGY_INTUITION: the argument transfers intuition from another topology into the topology stated in the problem.

Meaning of required_evidence_label:
- NO_CHECK_NEEDED: no error evidence is needed.
- RAY_CARDINALITY_VERIFICATION: check what an upper ray contains globally, not only locally near one chosen point.
- FINITE_SUBSET_NEIGHBORHOOD_TEST: check neighborhoods around points relative to a finite set.
- PAIR_GLOBALITY_AUDIT: check whether a paired construction remains valid when neighborhoods see all points above the cutoff.
- DECREASING_INTEGER_WITNESS: use or analyze a countable set that is bounded above and unbounded below.
- LUB_DEFINITIONAL_TEST: check the least-upper-bound definition of supremum.
- BOUNDED_INTERVAL_COVER_TEST: use or analyze the fact that R is the countable union of bounded intervals.

For each submission, choose exactly one primary_error_label and exactly one required_evidence_label from the lists above.
