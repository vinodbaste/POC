# Justification

## 1. The combinatorial object being counted

The problem asks for the number of distinct lex-ordered arrays of unordered vertex pairs `(A_i, B_i)` of length **exactly** `K = 22` whose simple paths in the given `N = 44` tree partition the edge set. Two facts collapse the structural count:

- **The order of the array is forced by the multiset of pairs.** Once the *multiset* of unordered pairs is fixed, the lex-ordered listing is unique (sort by `A_i` ascending, breaking ties by `B_i` ascending). So counting valid arrays equals counting valid edge-partitions of the tree into simple paths with the additional restriction that the partition contains exactly `K = 22` parts (paths), where each path is identified with the unordered pair of its two endpoints.
- **Endpoints determine the path.** In a tree, any two vertices `A != B` are connected by a unique simple path; so an unordered pair `(A, B)` with `A != B` uniquely identifies one simple path.

Hence the count equals the number of *length-`K`* edge-partitions of the tree into simple paths. The unrestricted total over all `K` is the sum of the per-`K` counts; the problem here restricts to the single value `K = 22`.

## 1b. Small-case anchor sub-quantities (graded)

Five small-tree length-`K = 2` counts are graded as part of the auditor's mathematical derivation. They serve as a built-in proof that the auditor's counting method computes the right combinatorial object: any method that does not reproduce them on these small trees is wrong on the `N = 44` tree as well. The graded values, all modulo `997`, are:

- `P3_K2 = 1`. The path on three vertices has two edges; the unique length-`K=2` partition is `{(1,2), (2,3)}`.
- `P4_K2 = 2`. The path on four vertices has three edges; the two valid length-`K=2` partitions are `{(1,2), (2,4)}` and `{(1,3), (3,4)}` (each glues one pair of consecutive edges into a 2-edge path and leaves the third as a single edge).
- `P5_K2 = 3`. The path on five vertices has four edges; the three valid length-`K=2` partitions are `{(1,2), (2,5)}`, `{(1,3), (3,5)}`, and `{(1,4), (4,5)}` (each glues a contiguous block of edges into one path and the remaining contiguous block into another).
- `S3_K2 = 3`. The three-leaf star (one hub, leaves `2, 3, 4`) has three edges; for `K = 2` paths the local involution at the hub must pair exactly one incident-edge pair, leaving one as a singleton; the three valid partitions are obtained by choosing which two of the three leaves are glued through the hub.
- `S4_K2 = 3`. The four-leaf star (one hub, leaves `2, 3, 4, 5`) has four edges; for `K = 2` paths the local involution at the hub must pair exactly two of the four incident edges (the other two are also paired into the second path); there are `C(4, 2) / 2 = 3` ways to split four leaves into two pairs.

Plugging the per-vertex polynomials below into the framework reproduces these five anchor values exactly: `g_2(x) = 1 + x`, `g_3(x) = 1 + 3x`, `g_4(x) = 1 + 6x + 3x^2`, etc., and the coefficient of `x^{|E| - K}` in `prod_v g_{d_v}(x)` matches each anchor by direct computation.

## 2. Local-involution decomposition with path-count tracking

Fix any vertex `v` of degree `d_v`. In any edge-partition into simple paths, looking locally at `v`, each of the `d_v` incident edges is in exactly one path; that path either passes through `v` (uses two of the `d_v` incident edges and contributes nothing to the global path-count at `v`) or ends at `v` (uses exactly one of the `d_v` incident edges and contributes a single path-endpoint to the global path-count). Equivalently, an edge-partition induces, at every vertex `v`, an *involution* (a partial matching) on the multiset of incident edges: paired-up incident edges glue into a path crossing `v`; un-paired incident edges become path-endpoint edges at `v`.

**Lemma (gluing).** Independent involutions at every vertex glue uniquely to a global edge-partition of the tree into simple paths, and conversely, every edge-partition arises from exactly one such tuple of local involutions. (Standard tree argument: starting from any unpaired endpoint at some vertex `v`, walk the tree edge to its other end, then follow the local involution to the next outgoing edge, and continue until hitting another unpaired endpoint. Because the underlying graph is a tree, this walk never revisits an edge and always terminates. Reversing the construction yields the unique correspondence.)

**Lemma (path-count from local pair-counts).** Let `k_v` denote the number of *pairs* in the local involution at `v` (so `0 <= k_v <= floor(d_v / 2)`, and `2 k_v` of the `d_v` incident edges are paired while `d_v - 2 k_v` are left as path-endpoints at `v`). Then the resulting edge-partition has exactly

```
K = |E| - sum_v k_v
```

paths. *Proof.* The total number of path-endpoints summed over all vertices equals `sum_v (d_v - 2 k_v) = 2|E| - 2 sum_v k_v`. Each path has exactly two endpoints, so the number of paths is half of this total, giving `|E| - sum_v k_v`. ∎

Hence to count edge-partitions of the tree with exactly `K` paths, we must count tuples of local involutions `(I_v)_v` whose pair-counts `k_v` satisfy `sum_v k_v = |E| - K`, weighting each tuple by the number of distinct local involutions of `v`'s incident edges that have exactly `k_v` pairs.

**Per-vertex generating polynomial.** The number of involutions of a `d`-element set with exactly `k` pairs is `C(d, 2k) * (2k - 1)!!` where `(2k - 1)!!` is the double factorial (and `(-1)!! = 1`). Define

```
g_d(x) := sum_{k = 0}^{floor(d/2)} C(d, 2k) * (2k - 1)!! * x^k.
```

Then the count of edge-partitions of the tree with exactly `K` paths equals

```
[x^{|E| - K}] prod_v g_{d_v}(x)
```

(the coefficient of `x^{|E| - K}` in the product polynomial, taken modulo `997`).

**Sanity check on small trees.**

- **Path `P_5` (vertices `1 - 2 - 3 - 4 - 5`, four edges).** Degrees `(1, 2, 2, 2, 1)`. Polynomials `g_1(x) = 1`, `g_2(x) = 1 + x`. Product `= (1)(1 + x)^3(1) = 1 + 3x + 3x^2 + x^3`. Per-`K` counts (with `|E| = 4`): `K = 4` (`s = 0`) gives `1`; `K = 3` (`s = 1`) gives `3`; `K = 2` (`s = 2`) gives `3`; `K = 1` (`s = 3`) gives `1`. Sum `= 8 = I(1)*I(2)*I(2)*I(2)*I(1)`. Direct enumeration matches.
- **Star `K_{1,4}` (centre `1` with four leaves `2, 3, 4, 5`).** Degrees `(4, 1, 1, 1, 1)`. Polynomials `g_4(x) = 1 + 6x + 3x^2`, `g_1(x) = 1`. Product `= 1 + 6x + 3x^2`. Per-`K` counts (with `|E| = 4`): `K = 4` (`s = 0`) gives `1`; `K = 3` (`s = 1`) gives `6`; `K = 2` (`s = 2`) gives `3`. Sum `= 10 = I(4)`. Direct enumeration matches.

## 3. The target tree (N = 44)

The parent array is

```
P = [-1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
      3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6,
      7, 7, 8, 8, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22]
```

The induced edges are `(P[i], i)` for `i = 2, ..., 44`. Counting children of each vertex from `P`:

| Vertex `v` | Children                  | Parent? | `deg(v)` |
|------------|---------------------------|---------|----------|
| 1          | 2,3,4,5,6,7,8,9 (8)       | root    | 8        |
| 2          | 10,11,12,13,14,15 (6)     | 1       | 7        |
| 3          | 16,17,18,19,20 (5)        | 1       | 6        |
| 4          | 21,22,23,24 (4)           | 1       | 5        |
| 5          | 25,26,27 (3)              | 1       | 4        |
| 6          | 28,29,30 (3)              | 1       | 4        |
| 7          | 31,32 (2)                 | 1       | 3        |
| 8          | 33,34 (2)                 | 1       | 3        |
| 9          | —                         | 1       | 1        |
| 10..15     | one child each (35..40)   | 2       | 2 each   |
| 16, 17     | one child each (41, 42)   | 3       | 2 each   |
| 18, 19, 20 | —                         | 3       | 1 each   |
| 21, 22     | one child each (43, 44)   | 4       | 2 each   |
| 23, 24     | —                         | 4       | 1 each   |
| 25..30     | —                         | 5 or 6  | 1 each   |
| 31..34     | —                         | 7 or 8  | 1 each   |
| 35..44     | —                         | (above) | 1 each   |

**Degree multiset:** `8 once`, `7 once`, `6 once`, `5 once`, `4 twice`, `3 twice`, `2 ten times`, `1 twenty-six times`. Sum of degrees = `2 * 43`, matching `2 |E|`. ✓

Number of edges `|E| = N - 1 = 43`, so for `K = 22` we need to extract the coefficient of `x^{43 - 22} = x^{21}` in `prod_v g_{d_v}(x)`.

**Per-vertex generating polynomials (coefficients listed `[c_0, c_1, ...]`):**

| `d` | `g_d(x)` coefficients              | `g_d(1) = I(d)` |
|-----|------------------------------------|-----------------|
| 1   | `[1]`                              | `1`             |
| 2   | `[1, 1]`                           | `2`             |
| 3   | `[1, 3]`                           | `4`             |
| 4   | `[1, 6, 3]`                        | `10`            |
| 5   | `[1, 10, 15]`                      | `26`            |
| 6   | `[1, 15, 45, 15]`                  | `76`            |
| 7   | `[1, 21, 105, 105]`                | `232`           |
| 8   | `[1, 28, 210, 420, 105]`           | `764`           |

(Each coefficient `[x^k] g_d = C(d, 2k) * (2k - 1)!!`. The sum-evaluation `g_d(1)` recovers the involution number `I(d)`, which is the unrestricted total.)

## 4. Numerical evaluation

Multiply `prod_v g_{d_v}(x) mod 997` over all `44` vertices and read off the coefficient of `x^{21}`. Concretely:

```python
from math import comb
def doublefact(n):
    if n < 0: return 1
    r = 1
    while n > 0:
        r *= n; n -= 2
    return r
def g(d):
    return [comb(d, 2*k) * doublefact(2*k - 1) for k in range(d // 2 + 1)]
def mul(a, b, mod):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i+j] = (r[i+j] + x*y) % mod
    return r

P = [-1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
     4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 10, 11, 12, 13, 14, 15,
     16, 17, 21, 22]
N = len(P); deg = [0] * (N + 1)
for i in range(2, N + 1):
    deg[P[i - 1]] += 1; deg[i] += 1

prod = [1]
for v in range(1, N + 1):
    prod = mul(prod, g(deg[v]), 997)

# K = 22, |E| = 43, coefficient of x^{43 - 22} = x^{21}
print(prod[21] % 997)   # -> 253
```

Cross-check: summing all coefficients `prod[s]` reproduces the unrestricted count `878 mod 997` (as it must, since the unrestricted count is `prod_v I(d_v) = prod_v g_{d_v}(1)`). The exact (big-integer) length-`22` count before reduction is `33,313,002,723,900`, and `33313002723900 mod 997 = 253`.

## 5. Gold value

```
correct_answer = 253
```

## 6. Common reasoning traps for this problem (W-trap classifier)

These are the canonical wrong patterns that `wrong_formula` is meant to flag. The strongest trap for this `K`-restricted variant is W7 — **dropping the `K = 22` constraint and reporting the unrestricted total**.

- **W1 — Spanning-tree count.** Cayley's formula `N^(N - 2) = 44^42` mod 997 is far from `253`. A tree itself has exactly one spanning tree, so the tempting "answer = 1" reading is also W1.
- **W2 — Product of `(deg(v) - 1)!!`.** Counts perfect matchings on the half-edges; mod-997 residue is `314`, not `253`.
- **W3 — Product of `deg(v)!`.** Treats the local choice as a full ordering of incident edges; mod-997 residue is `570`.
- **W4 — Single-edge-only.** Asserts the only valid decomposition is to take every edge as its own length-1 path, giving `1`. Misses both the involution structure and the `K = 22` constraint (the all-singletons decomposition has `K = 43`, not `22`, so it is in fact invalid under the constraint).
- **W5 — Buggy ad-hoc tree DP.** Any rooted-tree DP whose state transitions disagree with the small-tree length-`K` counts above, especially DPs that omit the running-pair-count parameter needed to enforce `K = 22`.
- **W6 — Catalan / binary-tree shortcuts.** Catalan numbers, ballot numbers, and ordered-tree counts have no relationship to the polynomial `prod_v g_{d_v}(x)` evaluated at a coefficient.
- **W7 — Length-constraint dropped.** The most common trap. The response derives the correct unrestricted total `prod_v I(d_v) mod 997 = 878` (or some equivalent reformulation) and reports it directly without ever applying the `K = 22` filter. The reported value is `878` (or a near-mod-997 slip on `878`), not `253`. Fires `wrong_formula`.
- **W8 — Length-constraint reinterpreted.** The response notices the `K = 22` clause but reads it as "the longest path has length `22`" or "the array has at most `22` pairs" or some other variant. The committed count therefore corresponds to a different combinatorial object and does not match `253`.

## 7. Per-response audit (A–K)

The per-response audit details are populated verbatim in `solution/oracle.json` (which mirrors `tests/oracle.json` for the deterministic verifier). For each response `R in {A, ..., K}`, the audit records:

- `response_id`: the response letter.
- `final_answer_correct`: `true` iff the response's final stated value mod `997` equals `253` AND its derivation is mathematically valid.
- `failure_reasons`: applicable codes from `{wrong_formula, arithmetic_error, invalid_or_incomplete_justification, final_answer_error}` under rules R1–R4 in `instruction.md`.
- `primary_failure_evidence`: ≥30-char string quoting/paraphrasing the concrete textual evidence in the response.
- `alternative_codes_considered`: ≥2 distinct codes (none in `failure_reasons`) each with a ≥20-char `reason_excluded` string.
- `error_category`: a single string from `{wrong_method, arithmetic_slip, incomplete_or_truncated, no_method_committed, correct}` (R6).
- `dominant_error_location`: a single string from `{method_commitment, framework_implementation, no_specific_error_in_method, none}` (R8). `method_commitment` for conceptually wrong method choices (A, F); `framework_implementation` for cases where the method-class is reasonable but the implementation breaks (D — buggy DP state design allowing e=2; K — wrong degree multiset extracted from parent array); `no_specific_error_in_method` for arithmetic slips, truncations, abandonments, and no-method audits whose defect does not localise to a method-implementation step (B, C, E, G, H, I, J).
- `length_constraint_handling`: a single string from `{correctly_applied, dropped, reinterpreted, no_method}` (R7, documentation-only — not graded).

`acceptable_solution_ids = []` — none of A–K commits to the gold value `253` with a valid derivation.

<!-- BEGIN PER_RESPONSE_AUDIT -->

**Response A — final = `0`, codes = `{wrong_formula, final_answer_error}`.** A asserts "No arrangement of 22 edge-disjoint paths simultaneously partitions all edges AND produces lexicographically ordered pairs" and reports `0`. The lex-incompatibility argument is mathematically wrong: every multiset of valid pairs has a unique lex ordering, so the lex constraint is structurally satisfiable for every valid path-partition. Method commitment is incorrect, fires `wrong_formula`. `arithmetic_error` excluded — no arithmetic was performed. `invalid_or_incomplete_justification` excluded by R4 (mutually exclusive with `wrong_formula`).

**Response B — final = (truncated, no integer), codes = `{invalid_or_incomplete_justification, final_answer_error}`.** B sets up a per-vertex involution polynomial `T_d(x)`, lists the product `T_8 T_7 T_6 T_5 T_4^2 T_3^2 T_2^{10}`, and stops mid-summation at `Sigma_{e in {4,6,8,10`. Framework is correct; no final integer is committed. Fires `invalid_or_incomplete_justification` for truncation, plus `final_answer_error` per R1 (no committed value).

**Response C — final = `454`, codes = `{wrong_formula, final_answer_error}`, error_category = `wrong_method`, length_constraint_handling = `correctly_applied`.** C states `f_d(x) = sum_s C(d,s) (d-s-1)!! x^s` as its per-vertex polynomial and claims that small-tree hand-checks pass. Direct expansion of C's stated formula on the three-leaf star `S_3` at `K = 2`, however, gives `[x^1] f_3(x) (f_1(x))^3 = [x^1] (2 + 3x + 3x^2 + x^3)(1 + x)^3 = 1 * 3 + 3 * 2 = 9`, while the brute-force anchor is `S3_K2 = 3`. The response's stated formula therefore fails the `S_3` anchor under independent expansion, regardless of what the response itself claims about its hand-checks (the response's claim that its hand-checks pass is itself a calculation error). Per R3, when the response's stated formula fails any of the five anchors under the auditor's own expansion, the audit fires `wrong_formula + wrong_method` (NOT `arithmetic_error + arithmetic_slip`), even when the response writes down per-degree polynomials and a substitution-based framework. The trap that defeats lazy classifiers is to trust the response's "hand-checks pass" claim instead of doing the expansion oneself.

**Response D — final = `286`, codes = `{wrong_formula, final_answer_error}`.** D's DP state `dp_u[e][k]` allows `e in {0, 1, 2}` for paths having `u` as an open endpoint that "continue upward to u's parent". Allowing `e = 2` is structurally invalid because only one path can extend through the single parent-edge; the DP overcounts and would also fail brute-force on small trees. The asserted `dp_1[0][22] = 286` is downstream of a wrong DP design — fires `wrong_formula`.

**Response E — final = `44`, codes = `{invalid_or_incomplete_justification, final_answer_error}`.** E sets up the correct generating-function framework and the leaf-26 / non-leaf-18 split, then explicitly abandons computation ("Given the time, I must box an answer") and cycles through guesses `\boxed{0}, \boxed{42}, \boxed{1}, \boxed{44}`, finally committing `44`. The committed value is not the output of any computation in the response. Fires `invalid_or_incomplete_justification`.

**Response F — final = `480`, codes = `{wrong_formula, final_answer_error}`.** F commits to "the total number of valid arrays is the product of the counts for each sub-hub". This independent-product method is wrong because paths can cross between sub-hubs through hub vertex 1, so per-subtree counts are not multiplicatively independent. Method commitment is incorrect — fires `wrong_formula`.

**Response G — final = `42`, codes = `{arithmetic_error, final_answer_error}`, error_category = `arithmetic_slip`, length_constraint_handling = `correctly_applied`.** G identifies the unrestricted total `prod_v T_{deg(v)} = 878`, reframes the `K = 22` filter as `[x^{21}]` in the product of bivariate polynomials with `f_d = f_{d-1} + (d-1) x f_{d-2}`, lists per-degree polynomials, and commits to the extracted coefficient `42`. The framework is mathematically valid (matches the gold derivation), the `K = 22` filter is correctly applied via the `[x^{21}]` extraction target, and the response's framework reproduces small-tree counts on the inline sanity-check; the failure is the slip in the coefficient extraction itself. Fires `arithmetic_error` per R3.

**Response H — final = (truncated mid-coefficient extraction), codes = `{invalid_or_incomplete_justification, final_answer_error}`.** H sets up the per-vertex polynomial framework, computes partial coefficients `e_4 = 663, e_5 = 519, e_6 = 406, e_7 = 372`, then is cut off mid-line at `h_7 = 105 e_7 + 420 e_6 + 210 e_5 + 28 e_4 + 1 e_3 = 105(372) + 420(406) + 2`. No final integer is reached — fires `invalid_or_incomplete_justification`.

**Response I — final = `444`, codes = `{invalid_or_incomplete_justification, final_answer_error}`.** I oscillates between "the correct count is 1 (by symmetry)" and "a careful implementation reveals 444", with no formula, polynomial product, DP, or arithmetic exhibited anywhere. The committed value `444` is unsupported — fires `invalid_or_incomplete_justification`.

**Response J — final = `0`, codes = `{invalid_or_incomplete_justification, final_answer_error}`.** J walks through seven labelled steps without specifying any formula, recurrence, generating function, or DP, then commits `\boxed{0}` without exhibiting any numerical operation. No method commitment, no work — fires `invalid_or_incomplete_justification`.

**Response K — final = `0`, codes = `{wrong_formula, final_answer_error}`.** K writes "Node 2: parent1 and children:10,11,12,13,14,15 -> degree 6" and similarly assigns deg=5 to node 3, deg=4 to node 4, deg=3 to nodes 5–6, deg=2 to nodes 7–8 — every non-root sub-hub degree is undercounted by exactly one (the parent edge is enumerated but counted as zero). The downstream parity argument "in J(t) exponents are even, in H(t) exponents are odd, product has odd exponents, 18 is even, coefficient is 0" is invalid because it operates on the wrong degree multiset; the same `degree = number of children` rule applied to the path `1-2-3` also fails brute-force. The conclusion `0` is downstream of a wrong-method commitment, fires `wrong_formula`. `arithmetic_error` is explicitly excluded by its trigger ("uses the correct degree multiset").

<!-- END PER_RESPONSE_AUDIT -->
