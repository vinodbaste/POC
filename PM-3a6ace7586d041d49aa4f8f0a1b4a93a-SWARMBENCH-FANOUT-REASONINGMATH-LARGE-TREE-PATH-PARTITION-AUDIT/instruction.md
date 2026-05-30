# instruction.md

You are auditing raw AI-generated proposed solutions to a single-tree path-partition counting problem on `N = 44` vertices. The problem asks for the number of distinct lexicographically-ordered arrays of unordered vertex pairs `(A_i, B_i)` whose simple paths in the given tree partition the edge set AND whose array length is exactly `K = 22` pairs, with the count reported modulo the prime `997`.

Working directory: `/workspace`.

Input artifacts:

- Problem statement: `/input_artifacts/problem.md`
- Provenance note for the proposed AI-generated responses: `/input_artifacts/provenance.md`
- Proposed solution files (eleven total):
  - `/input_artifacts/proposed_solutions/response_A.md`
  - `/input_artifacts/proposed_solutions/response_B.md`
  - `/input_artifacts/proposed_solutions/response_C.md`
  - `/input_artifacts/proposed_solutions/response_D.md`
  - `/input_artifacts/proposed_solutions/response_E.md`
  - `/input_artifacts/proposed_solutions/response_F.md`
  - `/input_artifacts/proposed_solutions/response_G.md`
  - `/input_artifacts/proposed_solutions/response_H.md`
  - `/input_artifacts/proposed_solutions/response_I.md`
  - `/input_artifacts/proposed_solutions/response_J.md`
  - `/input_artifacts/proposed_solutions/response_K.md`

Verification:
- Your final report at `/logs/agent/output.json` is graded by a deterministic field-by-field verifier that compares it against the gold oracle stored at `/tests/oracle.json`. Each per-response audit is graded as an all-or-nothing unit on its six required sub-fields (`response_id`, `final_answer_correct`, `failure_reasons` exact set match, `primary_failure_evidence`, `alternative_codes_considered`, `error_category`). A single mis-attributed code, missing evidence string, malformed alternative-codes entry, or wrong `error_category` enum value zeros the entire 30-point audit for that response. The seventh field `length_constraint_handling` is still emitted (see below) but is documentation-only and is not graded by the deterministic verifier — its boundary between `correctly_applied` and `dropped` on truncated-but-correctly-set-up responses turned out to be too ambiguous to grade strictly. There is no partial credit within an audit.

Task:
1. Read the problem statement and all eleven proposed solutions.
2. **Mathematical derivation (the dominant work).** Independently derive the gold value `correct_answer` of the count modulo `997` for the `N = 44` tree at `K = 22`. You must derive this number yourself; no formula, invariant, or numerical hint is supplied to you here.
3. **Mathematical sanity-checks (graded).** Independently derive five sub-quantities that the verifier will check against your work:
   - `small_case_anchor_results.P3_K2`: the number of valid length-`K=2` lex-ordered pair arrays on the path `P_3` (vertices `1-2-3`, two edges), modulo `997`.
   - `small_case_anchor_results.P4_K2`: the corresponding count on the path `P_4` (four vertices, three edges) at `K=2`, modulo `997`.
   - `small_case_anchor_results.P5_K2`: the corresponding count on the path `P_5` (five vertices, four edges) at `K=2`, modulo `997`.
   - `small_case_anchor_results.S3_K2`: the corresponding count on the three-leaf star (one hub, three leaves, three edges) at `K=2`, modulo `997`.
   - `small_case_anchor_results.S4_K2`: the corresponding count on the four-leaf star (one hub, four leaves, four edges) at `K=2`, modulo `997`.

   These five integer sub-quantities are part of your output and contribute to the deterministic verifier's mathematical-derivation score. You must derive them yourself rather than copying values from the small-case anchors section below — they are the *output* of the same enumeration whose results are listed in the anchors section as oracles for sanity-checking. Reporting them in your output certifies that your committed counting method passes those small-case checks.
4. Use the problem's path-decomposition condition exactly as stated: the unordered pairs are listed in strict lexicographic order, every pair `(A_i, B_i)` satisfies `1 <= A_i < B_i <= N`, the simple tree-paths between the pairs must partition the edge set (each edge in exactly one path), AND the array length is exactly `K = 22` pairs. The length restriction is a strict additional constraint: arrays with more or fewer than `22` pairs are invalid even if every other condition holds.
5. For each proposed response, check whether the response's final stated value of the count modulo the prime equals the gold value AND whether its derivation is mathematically valid: a correct counting method (formula, recurrence, or DP that genuinely computes the count of length-`K` path-partition arrays), correct degree information for the given tree, correct handling of the length-`K` constraint, and correct numerical evaluation, including modular reduction.
6. For each proposed response A through K, audit whether its mathematical reasoning is correct and identify the concrete failure reason(s) if incorrect.
7. Do not decide correctness by majority vote among the proposed responses. Independently solve the problem first, then audit each response against your own result.

Allowed failure reason codes (each code applies ONLY when its trigger is concretely present in that single response's text):

- `wrong_formula`
  - TRIGGER: the response derives or applies an incorrect closed-form expression, recurrence, algorithm, or invariant for the count of valid arrays. See the W-trap method classifier below for the canonical wrong patterns to recognise.
- `arithmetic_error`
  - TRIGGER: the response (a) commits to a counting method that is mathematically valid for this problem, in the sense that **the auditor independently verifies — by direct polynomial expansion, brute-force enumeration, or DP transition simulation on the small trees — that the response's stated formula or DP reproduces the brute-force enumeration on EVERY one of the five small-tree anchors `P3_K2 = 1`, `P4_K2 = 2`, `P5_K2 = 3`, `S3_K2 = 3`, `S4_K2 = 3`** (this verification is mandatory and must be performed by the auditor on the response's actual stated method, not on the auditor's own correct method, and not on whatever sanity-checks the response itself claims to have done — many wrong responses claim their hand-checks pass when the actual polynomial expansion of their stated formula does NOT reproduce the anchor; the auditor MUST do the expansion themselves), (b) uses the correct degree multiset for this tree, (c) correctly accounts for the `K = 22` constraint, AND (d) **EXHIBITS** at least one concrete numerical step of the `N = 44` evaluation in the response text — for example, an explicit polynomial product computed coefficient-by-coefficient on this tree, a written coefficient-extraction step, or a written modular reduction of a fully-evaluated polynomial — such that mis-evaluation of that exhibited step is what produced the wrong final value. The trigger does NOT fire when the response shows only the framework setup, small-tree warm-ups, or the polynomial coefficient list, and then jumps directly to a final integer with phrases like "carrying out the multiplication yields ...", "expanding the product gives ...", or "after computation the answer is ..." without the actual N=44 multiplication, coefficient-extraction, or modular-reduction steps being written down. In that case the response fires `invalid_or_incomplete_justification` instead. **If the response's stated formula or DP fails ANY of the five anchors when the auditor expands it, `arithmetic_error` does NOT fire — `wrong_formula` fires instead, regardless of whether the response itself claims its method passes hand-checks.** Apply only when `wrong_formula` does not also fire.
- `invalid_or_incomplete_justification`
  - TRIGGER: the response is truncated mid-derivation without committing to any concrete final integer, OR the response commits to a final integer that is presented as a guess, an assertion, or the unsupported output of an unspecified "computation" with the actual computation not exhibited in the response text (specifically: the response sets up a framework or names a method, but then writes phrases such as "carrying out the multiplication yields ...", "expanding the product gives ...", "a careful implementation reveals ...", or "after computation the answer is ..." and jumps directly to a final integer without the relevant N=44 polynomial multiplication, coefficient extraction, modular reduction, DP transitions, or other numerical steps being written down on this tree), OR the response stops at an explicit symbolic placeholder such as `f(N)` without instantiating it, OR the response presents only a vague qualitative argument ("by symmetry", "by combinatorial principles") without committing to any concrete formula. This code applies even when the response's stated final value happens to equal the gold value.
- `final_answer_error`
  - TRIGGER: the response's final stated value modulo `997` is not equal to the gold value, including the case where the response never commits to a concrete integer.

---

## Computational framework for the auditor's gold derivation

To keep the gold derivation tractable within the available compute budget, the auditor may use the following standard local-involution decomposition. The derivation of the framework itself is documented in detail in any standard treatment of tree edge-partitions; it is provided here so that the auditor's compute budget is spent on numerical evaluation and on classifying responses, not on rederiving the framework.

For any tree, edge-partitions into simple paths are in bijection with tuples of *local involutions* (partial matchings) on the incident edges at each vertex. If the local involution at vertex `v` (of degree `d_v`) has `k_v` matched pairs, then the resulting global edge-partition has exactly `K = |E| - sum_v k_v` paths.

The number of involutions on a `d`-element set with exactly `k` pairs is `C(d, 2k) * (2k-1)!!` (with `(-1)!! = 1`). Define the per-vertex generating polynomial:

```
g_d(x) := sum_{k = 0}^{floor(d/2)} C(d, 2k) * (2k - 1)!! * x^k
```

Then the count of edge-partitions of the tree into exactly `K` paths is the coefficient `[x^{|E| - K}] prod_{v in V} g_{d_v}(x)`, computed modulo `997`.

Concretely:
- `g_1(x) = 1`
- `g_2(x) = 1 + x`
- `g_3(x) = 1 + 3x`
- `g_4(x) = 1 + 6x + 3x^2`
- `g_5(x) = 1 + 10x + 15x^2`
- `g_6(x) = 1 + 15x + 45x^2 + 15x^3`
- `g_7(x) = 1 + 21x + 105x^2 + 105x^3`
- `g_8(x) = 1 + 28x + 210x^2 + 420x^3 + 105x^4`

The N=44 tree has degree multiset `8, 7, 6, 5, 4, 4, 3, 3` plus ten degree-2 vertices and twenty-six degree-1 leaves; `|E| = 43`. To recover the length-`K=22` count, multiply all 44 per-vertex polynomials, extract the coefficient of `x^{|E| - K} = x^{21}`, and reduce modulo `997`. The five small-case anchors (P_3, P_4, P_5, S_3, S_4) are the same coefficient extraction applied to the corresponding small trees and serve to verify your numerical pipeline before applying it to the N=44 tree.

The auditor should compute the polynomial product with a single deliberate big-integer Python script and reduce only the final extracted coefficient mod 997. Whichever response then reproduces this number AND uses a method that genuinely computes this combinatorial object on small trees is correct; every other response is wrong.

---

## Method-pattern classifier for `wrong_formula` (W-traps)

When auditing whether `wrong_formula` fires, identify which method pattern the response committed to. The canonical wrong patterns for this problem are:

- **W1 — Spanning-tree count.** Invokes Kirchhoff/Cayley's formula `N^(N-2)`, or claims the answer is the number of spanning trees. (A tree has one spanning tree, so "answer = 1" by this argument is also W1.)
- **W2 — Product of `(deg(v) - 1)!!`.** Claims the answer equals `prod_v (deg(v) - 1)!!` or the number of perfect matchings on incident half-edges via odd double factorials.
- **W3 — Product of `deg(v)!`.** Treats incident edges at a vertex as fully ordered and multiplies factorials.
- **W4 — Single-edge-only assertion (count = 1).** Asserts the only valid decomposition is every edge as its own length-1 path. Ignores both glued-paths AND the `K = 22` constraint (all-singletons has `K = 43`, not `22`).
- **W5 — Buggy ad-hoc tree DP.** Sets up a rooted-tree DP whose state transitions do not reproduce the length-`K` path-decomposition count on small trees (e.g. base case ignores dangling-half-edge state, state double-counts unordered pair orientations, state does not track the running path count needed for `K = 22`, or a recurrence whose small-tree value disagrees with the brute-force anchor counts above).
- **W6 — Catalan / binary-tree shortcuts.** Invokes Catalan numbers, ballot numbers, ordered-binary-tree counts, or other classical sequences without a derived equality to the length-`K` path-partition count.
- **W7 — Length-constraint dropped.** Computes the unrestricted total over all array lengths (e.g. independently choosing partial matchings of incident edges at every vertex and multiplying) and reports that total directly without applying the `K = 22` filter. The most common trap when the underlying tree-decomposition method is otherwise correct.
- **W8 — Length-constraint reinterpreted.** Acknowledges the `K = 22` clause but reads it as "longest path has length 22", "array has at most 22 pairs", or other variants — counts under that reinterpretation rather than length-exactly-22.

These W-patterns describe wrong methods only. Identifying the correct method, deriving why it counts the right combinatorial object (length-exactly-`K` arrays satisfying conditions (1)-(4)), and applying it to the `N = 44` tree are part of the auditor's task and are not stated in this instruction file.

---

## Brute-force anchor counts for sanity-checking the auditor's method (small trees)

To sanity-check whatever counting method you commit to BEFORE applying it to the N=44 tree, the following length-`K` counts are obtained by direct hand-enumeration of length-`K` lex-ordered pair tuples whose simple paths partition the edges of the small tree. Treat them as oracles, not as method hints:

- Path P_3 on three vertices 1-2-3 (two edges): `K=1: 1`; `K=2: 1`.
- Path P_4 on four vertices 1-2-3-4 (three edges): `K=1: 1`; `K=2: 2`; `K=3: 1`.
- Path P_5 on five vertices 1-2-3-4-5 (four edges): `K=1: 1`; `K=2: 3`; `K=3: 3`; `K=4: 1`.
- Star with three leaves (1 hub, leaves 2,3,4 — three edges): `K=1: 0`; `K=2: 3`; `K=3: 1`.
- Star with four leaves (1 hub, leaves 2,3,4,5 — four edges): `K=1: 0`; `K=2: 3`; `K=3: 6`; `K=4: 1`.

If your candidate counting method does NOT reproduce these counts on the small trees at the listed values of `K`, your method is wrong; abandon it and try a different approach. (For instance: any method that always reports the unrestricted total over all `K` will fail every `K=1` anchor on these trees, since the unrestricted totals are `2, 4, 8, 4, 26` respectively — none of which match the per-`K` anchors above. Any method that ignores the lex-ordering condition will overcount the `P_4` `K=2` anchor and the four-leaf-star `K=3` anchor.)

---

## Per-response application rules

- A response receives the empty `failure_reasons` list (and `final_answer_correct = true`) exactly when its final stated value modulo `997` equals the gold value AND its derivation is mathematically valid: a counting method that genuinely computes the path-partition count (sanity-checked on at least one small hand-tractable tree by the auditor, see R3 below), correct degrees for the tree, and correct numerical evaluation including modular reduction. A response whose method matches a W-trap does NOT establish correctness, even when the boxed final number happens to coincide with the gold value.
- Otherwise, include EVERY applicable concrete failure reason and NO inapplicable reason. Extra failure reasons and missing failure reasons are both wrong.

---

## Audit rules R1–R5 (apply uniformly to every response)

These rules resolve overlap and tie-break cases. Apply them in order; the earlier rule wins.

**R1. `final_answer_error` is MANDATORY whenever the response's final stated value modulo `997` is not equal to the gold value, including when the response never commits to a concrete integer.** The presence of any other failure code does NOT exempt the response from `final_answer_error`. The fact that a response is truncated does not exempt it from `final_answer_error`; if no integer is committed, the final-value check fails and `final_answer_error` fires together with `invalid_or_incomplete_justification`.

**R1 — operational implication: every wrong response has EXACTLY TWO codes in `failure_reasons`** — exactly one primary code from `{wrong_formula, arithmetic_error, invalid_or_incomplete_justification}` (chosen by R2/R3/R4/R5 below) AND `final_answer_error`. The only legal `failure_reasons` sizes are 0 (correct response with method valid AND value matches gold) or 2 (wrong). A list of size 1 is always wrong.

**R2. `wrong_formula` fires exactly when the response commits to a specific W-pattern (W1–W8).** If the response states a counting method that genuinely reproduces the length-`K` path-partition count on at least one small hand-tractable tree (see R3) but never finishes computing the value for the `N = 44` tree, do NOT fire `wrong_formula` — use `invalid_or_incomplete_justification` (and `final_answer_error`) only. Conversely, if the response commits to a W-pattern, `wrong_formula` fires even when the response also stops short of a numerical answer (in which case combine with `invalid_or_incomplete_justification` and `final_answer_error`). Note that W7 (length-constraint dropped) is by far the most common W-pattern when the underlying tree-decomposition method is otherwise correct: a response that derives the right unrestricted count and then reports it directly without a length-`K` filter still fires W7, not `arithmetic_error`.

**R3. `arithmetic_error` is mutually exclusive with `wrong_formula` AND with `invalid_or_incomplete_justification`. The auditor MUST decide between them by independently expanding the response's stated formula or DP on the five anchor trees `P_3, P_4, P_5, S_3, S_4` at `K = 2`, NOT by trusting whatever hand-checks the response itself claims to have performed.** Enumerate all length-`K_small` lex-ordered arrays satisfying conditions (1)-(4) for the small tree by hand, directly from the problem definition, OR — equivalently — apply the involution-polynomial framework above with the correct `g_d(x)` from the framework section. Then take the response's stated formula or DP, expand it yourself on each of the five anchors, and compare to the brute-force values `P3_K2 = 1`, `P4_K2 = 2`, `P5_K2 = 3`, `S3_K2 = 3`, `S4_K2 = 3`. **If the response's stated method fails ANY ONE of the five anchors under the auditor's own expansion (regardless of any claim the response makes about its hand-checks), classify as `wrong_formula`.** Many incorrect responses assert that their hand-checks pass when the actual polynomial expansion of their stated formula does not reproduce the anchor — for example, a response that defines `f_d(x) = sum_s C(d, s) (d - s - 1)!! x^s` and claims it reproduces the three-leaf-star anchor when in fact `[x^1] f_3(x) (f_1(x))^3 = 9 != 3`; under R3 such responses fire `wrong_formula`, not `arithmetic_error`, because the auditor's own expansion shows the formula is structurally incorrect. If the response's method reproduces ALL FIVE anchors AND the response writes down at least one explicit numerical step of the `N = 44` evaluation (a coefficient-by-coefficient polynomial multiplication on this tree, an explicit DP transition produced on this tree, or an explicit modular reduction of a fully-evaluated polynomial) but slips on that exhibited step only, classify as `arithmetic_error`. If the method reproduces all five anchors but no explicit numerical step of the `N = 44` evaluation is exhibited — the response sets up the framework, lists per-degree polynomials, optionally hand-checks small trees, then jumps to a final integer with phrases such as "carrying out the multiplication yields ...", "expanding the product gives ...", or "after computation the answer is ..." — classify as `invalid_or_incomplete_justification`, NOT `arithmetic_error`. When in doubt, prefer `wrong_formula`.

**R4. `invalid_or_incomplete_justification` is mutually exclusive with both `wrong_formula` and `arithmetic_error`.** It fires exactly when (a) the response is truncated mid-derivation without ever committing to a concrete final integer, OR (b) the response commits to a final integer that is presented as a guess, an assertion, or a copy-paste with no underlying computation, where the response either does not identify any specific counting method at all or explicitly abandons whatever method it set up before stating the final value, OR (c) the response stops at an explicit symbolic placeholder such as `f(N)` without instantiating it, OR (d) the response sets up a valid framework (and may list per-degree polynomials or sanity-check small trees) but jumps directly to its final integer with phrases such as "carrying out the multiplication yields ...", "expanding the product gives ...", "a careful implementation reveals ...", or "after computation the answer is ..." without writing down any numerical step of the `N = 44` evaluation that produced that final integer. It does NOT fire when the response commits to a specific incorrect counting method (then `wrong_formula` fires instead). It does NOT fire alongside an empty `failure_reasons` list — a justified, correct response whose final value matches gold must have `failure_reasons = []`.

**R5. Truncations vs. method-leaks: an unsupported numerical claim with NO explicit `N = 44` evaluation steps fires `invalid_or_incomplete_justification`, never `arithmetic_error`.** This is the most common confuser between (R3, R4): a response that exhibits the correct framework, lists the per-degree polynomials, possibly hand-checks small trees, and then writes "carrying out the polynomial multiplication modulo 997 gives ..." or "expanding the product yields the coefficient ... = ..." with the final integer attached but without the polynomial multiplication itself written down on the response, fires `invalid_or_incomplete_justification` (and `final_answer_error`), NOT `arithmetic_error`. `arithmetic_error` requires the bad numerical step to be visible in the response text. If only the framework and the final number are visible — the connecting computation is missing — the failure is incomplete justification, not an arithmetic slip.

---

## Output field definitions

- `correct_answer`: a single integer in `[0, 997)` giving the verified count of valid length-`K = 22` arrays for the `N = 44` tree, modulo `997`. The verifier checks that this integer equals the gold integer.
- `small_case_anchor_results`: an object whose five integer values are the auditor's independently-derived length-`K = 2` counts modulo `997` for the five small reference trees (the paths `P_3`, `P_4`, `P_5` and the three- and four-leaf stars). The verifier checks each value against the oracle. Reporting these certifies that whatever counting method you committed to passes the small-case sanity checks listed above; if your method fails any of these, your method is wrong on the `N = 44` tree as well.
- `acceptable_solution_ids`: the list of response letters (each one of `"A"` through `"K"`) for which `final_answer_correct` is `true` and `failure_reasons` is empty. May be the empty list. The verifier compares this list to the oracle list as an unordered set.
- `per_response_assessment`: a list of eleven audit objects, one for each response in order A, B, C, D, E, F, G, H, I, J, K.

Per-audit field definitions:

- `response_id`: the response letter, one of `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`, `"G"`, `"H"`, `"I"`, `"J"`, `"K"`.
- `final_answer_correct`: `true` exactly when the response gives the correct value modulo `997` AND its derivation is mathematically valid as defined above. Otherwise `false`.
- `failure_reasons`: a JSON list of strings chosen only from the allowed failure reason codes. Use an empty list exactly when `final_answer_correct` is `true`. If the response is wrong, include every applicable concrete failure reason and no inapplicable reason.
- `primary_failure_evidence`: a single string of at least `60` characters quoting or paraphrasing the concrete textual evidence in the response that triggers the most specific failure code in `failure_reasons` (or, when `failure_reasons` is empty, citing the response text that establishes the correct method and the correct final value). The verifier checks the length and basic non-emptiness of this field.
- `alternative_codes_considered`: a JSON list of at least `2` objects, each of the form `{"code": "<failure_code>", "reason_excluded": "<string of >= 30 chars>"}`. **The `code` values must be drawn from the four allowed failure-reason codes — `wrong_formula`, `arithmetic_error`, `invalid_or_incomplete_justification`, `final_answer_error` — and ONLY those four. Do NOT use `error_category` enum values such as `wrong_method`, `arithmetic_slip`, `incomplete_or_truncated`, `no_method_committed`, or `correct` here; those values belong in the `error_category` field, not in `alternative_codes_considered`.** The codes used here must NOT appear in `failure_reasons` for that audit, and must be pairwise distinct within the list. The `reason_excluded` strings must explain concretely why the alternative code does not fire for that response (≥ 30 characters each, with a specific reference to either the response text or the audit rule that rules the code out — e.g. for `arithmetic_error`: "the response never writes any explicit N=44 numerical step, so per R5 invalid fires instead"). The verifier checks the list length, code-vocabulary, code distinctness, exclusion-from-`failure_reasons`, and the per-entry minimum length on `reason_excluded`. Any `code` value outside the four-code failure vocabulary zeros the audit.
- `error_category`: a single string drawn from the closed vocabulary `{"wrong_method", "arithmetic_slip", "incomplete_or_truncated", "no_method_committed", "correct"}`. This is a higher-level classification that complements `failure_reasons`. Assignment rule (R6) is precise — apply each clause and use the FIRST one that matches:
  - `wrong_method` if the response commits to an incorrect counting method matching one of W1–W8. The defining feature is that the response explicitly identifies a method (formula, DP, generating function, etc.) AND that method, applied to small trees, would produce a count different from the brute-force anchors. A response whose stated method matches a W-pattern fires `wrong_method` even if the response also slips on arithmetic afterwards.
  - `arithmetic_slip` if and only if the auditor's own expansion of the response's stated method reproduces the brute-force anchors on **all five** of `P_3, P_4, P_5, S_3, S_4` at `K = 2` AND the response writes down at least one explicit `N = 44` numerical step (a coefficient-by-coefficient polynomial product, an explicit DP transition on this tree, or an explicit modular reduction of a fully-evaluated polynomial) AND that exhibited step is what produced the wrong final integer. The defining feature is that the bad numerical step is VISIBLE in the response text. If the response's stated method fails any anchor under the auditor's own expansion, this clause does NOT fire — use `wrong_method` instead. If only the framework is visible and the connecting computation is missing, this clause does NOT fire — use `incomplete_or_truncated` instead.
  - `incomplete_or_truncated` if the response sets up a framework (with or without small-tree sanity checks) and then jumps to its final integer (or simply stops) without exhibiting the connecting `N = 44` computation. This clause covers all cases where the response visibly identifies a counting approach but does NOT exhibit the numerical step that produced the final value.
  - `no_method_committed` if the response NEVER commits to a concrete counting method at all — the prose stays at the level of "by symmetry", "by combinatorial principles", "after careful counting, the answer is...", or similar without naming or sketching any specific formula, DP, generating function, or small-tree enumeration that the response then attempts to apply. The defining feature is that there is no method to evaluate against the small-case anchors.
  - `correct` for responses whose final value matches gold AND whose method is genuinely valid.
  
  A response that walks through "labelled steps" but never commits to a single concrete formula fires `no_method_committed`, NOT `incomplete_or_truncated`. A response that explicitly invokes an incorrect formula (e.g. "the answer is `prod_v deg(v)!`") fires `wrong_method` (with the W-pattern noted in `primary_failure_evidence`), NOT `arithmetic_slip` or `incomplete_or_truncated`, even when the response then slips on arithmetic. The verifier checks exact string equality against the gold `error_category`.
- `dominant_error_location`: a single documentation-only string drawn from the closed vocabulary `{"method_commitment", "framework_implementation", "no_specific_error_in_method", "none"}`. This pinpoints WHERE the response's defect lives. The deterministic verifier does NOT grade this field and it does NOT affect your audit's 30 points; emit your best-effort value for downstream analysis. Use `method_commitment` for conceptually wrong method choices (W1–W4 / W6 / W7-style traps, lex-annihilation, independent-product); `framework_implementation` for cases where the method-CLASS is correct but the implementation is provably broken in a step exhibited in the response text (a DP state that allows two paths to share a parent edge, a degree multiset extracted as "children only" omitting parent edges); `no_specific_error_in_method` for truncated/abandoned responses, no-method responses, and arithmetic-slip responses where no framework-step bug is exhibited; `none` for correct responses.
- `length_constraint_handling`: a single documentation-only string drawn from the closed vocabulary `{"correctly_applied", "dropped", "reinterpreted", "no_method"}`. This records how the response handled the explicit `K = 22` constraint. The deterministic verifier does NOT grade this field and it does NOT affect your audit's 30 points; emit your best-effort value for downstream analysis. Use `correctly_applied` if the response's chosen method explicitly filters or weights by `K = 22`; `dropped` if the response computes the unrestricted total without a `K = 22` filter (the W7 trap); `reinterpreted` if the response acknowledges `K = 22` but reads it as something other than array length is exactly 22 (the W8 trap); `no_method` if the response never commits to a concrete counting method.
- `anchor_verification_summary`: a single string of at least `100` characters recording the auditor's own independent expansion of the response's stated counting method on at least one of the five small-tree anchors (`P_3`, `P_4`, `P_5`, `S_3`, `S_4`) at `K = 2`, with the auditor stating which anchor was used, what value the response's stated method produces under direct expansion, and whether that value matches the brute-force anchor (`P3_K2 = 1`, `P4_K2 = 2`, `P5_K2 = 3`, `S3_K2 = 3`, `S4_K2 = 3`). When the response commits to no specific method (per R4 / `no_method_committed`), state that observation explicitly with the same level of detail. The verifier checks length only (`>= 100` characters); the content is your audit's own reasoning record. This field is REQUIRED for every audit and is graded as part of the 30-point all-or-nothing per-audit check.

---

## Important scoring note

The response audit is evaluated as a strict per-field deterministic check. Extra failure reasons and missing failure reasons are both wrong. A `primary_failure_evidence` shorter than `60` characters zeros the audit. An `alternative_codes_considered` list with fewer than `2` entries, with a duplicate code, with a code that already appears in `failure_reasons`, or with any `reason_excluded` shorter than `30` characters zeros the audit. An `anchor_verification_summary` shorter than `100` characters zeros the audit. Do not include a broad reason unless it is genuinely needed to explain why that response is incorrect.

---

## Output Instructions

Write your final answer to `/logs/agent/output.json` in this exact JSON format:

```json
{
  "correct_answer": <integer>,
  "small_case_anchor_results": {
    "P3_K2": <integer>,
    "P4_K2": <integer>,
    "P5_K2": <integer>,
    "S3_K2": <integer>,
    "S4_K2": <integer>
  },
  "acceptable_solution_ids": ["<uppercase response letters whose final_answer_correct is true>"],
  "per_response_assessment": [
    {
      "response_id": "A",
      "final_answer_correct": <true or false>,
      "failure_reasons": ["<zero or more allowed failure reason codes>"],
      "primary_failure_evidence": "<string of >= 60 chars>",
      "alternative_codes_considered": [
        {"code": "<failure code not in failure_reasons>", "reason_excluded": "<string of >= 30 chars>"},
        {"code": "<distinct failure code not in failure_reasons>", "reason_excluded": "<string of >= 30 chars>"}
      ],
      "error_category": "<one of: wrong_method | arithmetic_slip | incomplete_or_truncated | no_method_committed | correct>",
      "dominant_error_location": "<one of: method_commitment | framework_implementation | no_specific_error_in_method | none>",
      "length_constraint_handling": "<one of: correctly_applied | dropped | reinterpreted | no_method>",
      "anchor_verification_summary": "<string of >= 100 chars recording the auditor's own expansion of the response's stated method on at least one of P_3, P_4, P_5, S_3, S_4 at K=2>"
    }
  ]
}
```

In the actual output, include eleven objects in `per_response_assessment`, one for each response A, B, C, D, E, F, G, H, I, J, K, in that order. Do not write anything else to that file.
