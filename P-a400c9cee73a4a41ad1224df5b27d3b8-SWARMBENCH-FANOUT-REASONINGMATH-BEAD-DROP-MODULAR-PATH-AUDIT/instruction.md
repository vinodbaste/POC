# Bead-on-pegboard surface-path modular-residue audit

You are deriving the residue $N \bmod 1000$ of a binomial path count AND auditing thirteen raw AI-generated proposed solutions to that problem.

Working directory: `/workspace`.

Write your final answer JSON to `/logs/agent/output.json`.

## Input artefacts (read-only)

- `/input_artifacts/problem.md` — the bead-on-pegboard combinatorics / modular-arithmetic problem.
- `/input_artifacts/provenance.md` — origin and editing history of the response bundle (background only; not graded).
- `/input_artifacts/proposed_solutions/response_A.md` ... `/input_artifacts/proposed_solutions/response_M.md` — thirteen AI-generated attempts at the bead-on-pegboard problem, lettered A through M.

## Task

1. **Path-count setup.** Derive the total number of bead steps, the number of right moves, the number of left moves, and the corresponding binomial coefficient $\binom{n}{k}$. Each bead step changes $y$ by $-1$ and $x$ by $\pm 1$, so the total step count equals the starting $y$-coordinate; the right/left counts are then fixed by the net $x$-displacement. Treating "left" and "down" as independent moves and writing $\binom{1234+2026}{1234}$ is a path-model error.
2. **Modular decomposition.** Compute the 2-adic valuation $v_2$, the 5-adic valuation $v_5$, the residue modulo $8$, and the residue modulo $125$ of the binomial coefficient.
3. **CRT combination.** Combine the modulo-$8$ and modulo-$125$ residues using the Chinese Remainder Theorem to obtain the residue $N \bmod 1000$.
4. **Small-case anchor results.** Independently apply the same path-model + modular-arithmetic methodology to the five named small-case bead-on-pegboard problems listed below and report each anchor's exact path count and residue modulo $1000$.
5. **Per-response audit.** For each of the thirteen response files A through M, decide `final_answer_correct` (whether its claimed final residue equals the true $N \bmod 1000$ you derived in step 3) and the exact set of failure-mode codes `failure_reasons` whose trigger phrase is present in that response.
6. Do not decide correctness by majority vote among the proposed responses. Independently derive the gold residue first, then audit each response against that result.

## Sanity-check anchor parameter pairs

| anchor_name | start_x | start_y | right_moves | left_moves | binomial_n | binomial_k |
|---|---:|---:|---:|---:|---:|---:|
| `start_2_4_to_origin` | 2 | 4 | 1 | 3 | 4 | 1 |
| `start_4_10_to_origin` | 4 | 10 | 3 | 7 | 10 | 3 |
| `start_6_14_to_origin` | 6 | 14 | 4 | 10 | 14 | 4 |
| `start_8_20_to_origin` | 8 | 20 | 6 | 14 | 20 | 6 |
| `start_10_24_to_origin` | 10 | 24 | 7 | 17 | 24 | 7 |

For each anchor compute the exact path count $\binom{\text{binomial\_n}}{\text{binomial\_k}}$ and reduce it modulo $1000$. The anchors are deliberately small so they can be confirmed with a few-line stdlib computation. Do not infer the gold residue from these anchors — the small cases live in a different parameter regime.

## Failure-mode catalogue

Allowed failure reason codes (phrase-triggered; each code applies ONLY when its trigger phrase or its near-verbatim paraphrase is present in that single response's text):

- **F1 — path-model error.** The response uses an incorrect path model. Trigger: the response treats the bead's "down" and "left" as two independent moves and writes a total step count of `1234 + 2026 = 3260` (or any total step count other than `2026`); or it writes the binomial coefficient as $\binom{3260}{1234}$, $\binom{3260}{2026}$, or any other binomial whose top index is not `2026`; or it asserts that the bead must make exactly $1234$ steps to the left without right moves.

- **F2 — p-adic valuation error.** The response computes a wrong $v_2$ or $v_5$ of any of the three factorials $2026!$, $396!$, $1630!$, or of the binomial coefficient itself, measured against the value Legendre's formula $v_p(n!) = \sum_{j \ge 1} \lfloor n / p^j \rfloor$ yields when re-derived. Also fires when the response uses Legendre's raw digit-sum formula $v_p = s_p(k) + s_p(n-k) - s_p(n)$ for $p = 5$ without dividing by $(p-1) = 4$; or when the response treats Lucas's theorem mod $p$ as reducing the binomial-coefficient parameters modulo $1000$; or when the response wrongly concludes that no factor of $5$ remains in the binomial coefficient.

- **F3 — 5-free factorial / mod-125 shortcut error.** The response derives the correct $v_5 = 2$ but mis-applies the formula for the 5-free factorial product $n!_5 \bmod 5$ or $n!_5 \bmod 125$. Trigger: the response uses the non-recursive shortcut $P_5(n) \equiv (-1)^{\lfloor n/5\rfloor}\,(n \bmod 5)!$ without recursing into the upper digits of $n$ and arrives at $N/25 \equiv 1 \pmod 5$ (so $N \equiv 25 \pmod{125}$, $N \equiv 400 \pmod{1000}$); or the response writes the wrong base-$5$ expansion of $2026$ (e.g. as $31001_5$ instead of $31101_5$) or of $1630$ (e.g. as $23020_5$ instead of $23010_5$) and uses those wrong digit-factorials; or the response uses an incorrect block-product formula such as $g(2026!) \equiv 24^{16} \cdot \prod_{j=1}^{26}(\cdots)$ with wrong partial products and arrives at $N \equiv 25 \pmod{125}$.

- **F4 — CRT / final-residue inconsistency (INTERNAL contradiction ONLY).** Trigger: the response's stated final residue contradicts its OWN previously-stated modular results. Concretely: the response states $N \equiv 0 \pmod 8$ but its final residue is not a multiple of $8$; or the response states $N \equiv 0 \pmod{25}$ but its final residue is not a multiple of $25$; or the final residue falls outside the residue class fixed by the response's OWN mod-$8$ and mod-$125$ congruences. F4 is strictly about internal contradiction within the response itself. The phrase "final answer is wrong overall" is NEVER an F4 trigger. F4 also fires when any final answer that is not a multiple of $\operatorname{lcm}(8, 25) = 200$ follows a correct $v_2 \ge 3$ and $v_5 \ge 2$ derivation in the same response.

- **F5 — unsupported computational claim.** Trigger phrases (case-insensitive, treated as evidence the response abandoned the derivation in favour of an external computation): `known result`, `careful computation`, `systematic computation`, `computational verification`, `computational tool`, `library`, `efficient algorithm`, `Wolfram`, `Mathematica`, `Python`, `calculator`, `BinomialMod`, `standard binomial-mod libraries`, `numerical computation`, `it is known that`. F5 fires only when the assertion is final-answer-critical (the cited value is what is later boxed or returned).

## Important scoring and selection rules

- The audit is evaluated as an EXACT set match per response: `final_answer_correct` must match the oracle boolean AND `failure_reasons` must equal the oracle set (order-independent, no duplicates). Any deviation on either field scores zero for that response.
- Most responses have 3 or 4 failure reasons. Apply a code only when its trigger phrase is directly observable in the response text.
- Use an empty list `[]` for `failure_reasons` exactly when the response's final residue equals the true gold $N \bmod 1000$ AND no failure-reason trigger phrase appears in that response.
- `acceptable_solution_ids` is the uppercase, alphabetically-sorted list of `response_id` values whose `final_answer_correct` is `true` AND whose `failure_reasons` is the empty list.

## Label definitions for each proposed response

- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, ..., `"M"`.
- `final_answer_correct`: `true` exactly when the response's claimed final residue equals the true $N \bmod 1000$ you derived. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes `F1`, `F2`, `F3`, `F4`, `F5`.

---

## Verification

The verifier (`/tests/judge.py`) is a deterministic, Python-stdlib executable grader. It reads your output JSON from `/logs/agent/output.json` and grades each field against the oracle at `/tests/oracle.json` by exact integer equality and set equality. Reward is `passed / 488` clamped to `[0, 1]`; output that is byte-identical to the oracle earns reward `1.0`. It fail-closes to `0.0` on any read/JSON error or structural-gate violation. Per-field weights:

- `final_residue_mod_1000`: 30 pts (exact integer mod 1000).
- `intermediate_residues.mod_8`: 5 pts, `intermediate_residues.mod_125`: 5 pts.
- `gold_path_count_decomposition.binomial_n`: 5 pts, `gold_path_count_decomposition.binomial_k`: 5 pts.
- `gold_path_count_decomposition.v_2`: 5 pts, `gold_path_count_decomposition.v_5`: 5 pts.
- `small_case_anchor_results`: each of the five anchors is scored independently; exact match on `residue_mod_1000` earns 6 points per anchor (**30 points total**).
- `acceptable_solution_ids`: exact set match (**8 pts**, all-or-nothing).
- For each response A through M (13 responses, **30 pts per response**, **390 pts total**):
  - The response earns 30 points if and only if `response_id`, `final_answer_correct`, and the exact `failure_reasons` set all match the oracle. Otherwise 0 points.
- **Total = 30 + 5 + 5 + 5 + 5 + 5 + 5 + 30 + 8 + 390 = 488 points.**

---

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```
{
  "final_residue_mod_1000": <integer 0..999>,
  "intermediate_residues": {
    "mod_8":  <integer 0..7>,
    "mod_125": <integer 0..124>
  },
  "gold_path_count_decomposition": {
    "total_steps": <integer>,
    "right_moves": <integer>,
    "left_moves": <integer>,
    "binomial_n": <integer>,
    "binomial_k": <integer>,
    "v_2": <integer>,
    "v_5": <integer>,
    "mod_8": <integer 0..7>,
    "mod_125": <integer 0..124>
  },
  "small_case_anchor_results": [
    {"anchor_name": "<name>", "start_x": <int>, "start_y": <int>, "right_moves": <int>, "left_moves": <int>, "binomial_n": <int>, "binomial_k": <int>, "exact_path_count": <int>, "residue_mod_1000": <int 0..999>}
  ],
  "acceptable_solution_ids": ["<uppercase response letters that pass both criteria>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": <true or false>,
      "failure_reasons": ["<zero or more codes from {F1, F2, F3, F4, F5}>"]
    }
  ]
}
```

In the actual output, include thirteen objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, J, K, L, M, in that alphabetical order. Top-level keys MUST be exactly the six above with no extras. Do not write anything else to that file.
