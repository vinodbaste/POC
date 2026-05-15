You are auditing proposed solutions to a two-runner geometric optimization problem on a regular hexagon.

Working directory: /workspace.

Input artifacts:
- Problem statement: /input_artifacts/problem.md
- Source provenance: /input_artifacts/source_provenance.md
- Proposed solution files:
  - /input_artifacts/proposed_solutions/response_A.md
  - /input_artifacts/proposed_solutions/response_B.md
  - /input_artifacts/proposed_solutions/response_C.md
  - /input_artifacts/proposed_solutions/response_D.md
  - /input_artifacts/proposed_solutions/response_E.md
  - /input_artifacts/proposed_solutions/response_F.md
  - /input_artifacts/proposed_solutions/response_G.md
  - /input_artifacts/proposed_solutions/response_H.md

Task:
1. Read the problem statement and all eight proposed solutions.
2. Determine the correct optimal chronological task order for Alice and Bob.
3. Determine which proposed response(s), if any, correctly solve the problem.
4. Audit every proposed response A through H using the labels defined below.
5. Do not decide correctness by majority vote among the proposed responses. Independently analyze the task dependencies, the joint-task requirements, the possible simultaneous solo tasks, and the regular-hexagon distances.
6. Do not modify any files in /input_artifacts, /tests, or /solution.

Geometry conventions for the audit:
- You may take the side length of the regular hexagon to be 1.
- Adjacent vertices are distance 1 apart.
- Vertices with one vertex between them are distance sqrt(3) apart.
- Opposite vertices are distance 2 apart.
- Each vertex is distance 1 from the center O.

Label definitions for each proposed response:
- response_id: the response letter, one of "A", "B", "C", "D", "E", "F", "G", "H".
- extracted_final_order: the final task order claimed by that response, normalized as a string such as "[1, 2, 3, 4, 5, 6, 7]" or a bracketed order containing a set for simultaneous tasks. Use null only if the response gives no identifiable final order. This field is an extraction of the response's own final answer, not a correction.
- final_order_correct: true exactly when the response's final claimed order is mathematically equivalent to the optimal chronological order. If a simultaneous set is used, the order of entries inside that set is irrelevant. Otherwise false.
- joint_task_requirements_correct: true exactly when the response correctly identifies that tasks 2, 4, and 6 require both Alice and Bob together, and that tasks 3 and 5 are solo-capable. Otherwise false.
- flag_dependency_correct: true exactly when the response respects the final-answer-critical dependency that task 3 must occur before task 4, and task 4 must occur before task 6 because task 6 mounts the flag at A and leaves it there. Otherwise false.
- parallel_solo_block_correct: true exactly when the response recognizes the optimal use of a simultaneous block consisting only of the solo-capable non-start/non-finish tasks, completed early enough to support the later flag-photo-mount dependency. false if it treats those solo-capable tasks only sequentially, places a joint task inside the simultaneous block, or places the simultaneous block too late to be part of the optimal schedule.
- has_feasibility_error: true if the response proposes a physically or logically impossible schedule, such as completing a joint task while the runners are at different locations, completing a task before its required object is available, or completing a task at the wrong location. Otherwise false.
- has_optimization_error: true if the response's final order is not globally optimal, or if its optimization argument relies on a local greedy choice, an incomplete route comparison, or failure to consider a shorter feasible schedule. Otherwise false.
- has_calculation_error: true only if the response makes a numerical, geometric-distance, arithmetic, or algebraic mistake after its stated premises. Do not mark this merely because the response fails to compare all possible strategies.
- has_unjustified_step: true if the response uses a final-answer-critical inference without adequate justification, such as asserting that a locally closest task must be done first or that a path is optimal without comparing the relevant alternative. Do not mark this for minor missing exposition.
- has_stepwise_structure: true if the response is organized into explicit steps, numbered stages, bullet stages, or section headings that separate setup, constraints, optimization, and final answer. Otherwise false.
- has_required_answer_format: true if the response gives a bracketed task-order answer including task 1 at the beginning and task 7 at the end, using set notation for claimed simultaneous tasks if any. Otherwise false.

Output Instructions:

Write your final answer to /logs/agent/output.json as a JSON object with exactly this structure:

{
  "correct_order": "<optimal task order as a string>",
  "acceptable_solution_ids": ["<uppercase response letters that are fully correct>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "extracted_final_order": "<claimed order as a string or null>",
      "final_order_correct": <true or false>,
      "joint_task_requirements_correct": <true or false>,
      "flag_dependency_correct": <true or false>,
      "parallel_solo_block_correct": <true or false>,
      "has_feasibility_error": <true or false>,
      "has_optimization_error": <true or false>,
      "has_calculation_error": <true or false>,
      "has_unjustified_step": <true or false>,
      "has_stepwise_structure": <true or false>,
      "has_required_answer_format": <true or false>
    }
  ]
}

In the actual output, include eight objects in per_response_assessment, one for each response A, B, C, D, E, F, G, and H, in that order. Do not write anything else to that file.
