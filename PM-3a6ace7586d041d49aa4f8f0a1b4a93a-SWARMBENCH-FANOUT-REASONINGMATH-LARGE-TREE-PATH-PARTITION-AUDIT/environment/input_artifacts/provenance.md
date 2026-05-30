# Provenance of the proposed solutions

The eleven files `response_A.md` through `response_K.md` in `proposed_solutions/`
are independent draft solutions to the length-`K`-constrained tree path-
partition counting problem on the specific 44-vertex tree given in
`problem.md` (with `K = 22`). They were produced by eleven separate generations
from open-weight or weak large language models without any chain-of-thought
editing, hint injection, or post-hoc cleanup. They are intentionally a mix
of:

  * Responses that commit to one of the canonical wrong-method patterns
    (W-traps W1..W8 in `instruction.md`): spanning-tree count `N^(N-2)`,
    product of `(deg(v) - 1)!!`, product of `deg(v)!`, single-edge-only
    decomposition `= 1`, ad-hoc rooted-tree DP whose state transitions
    disagree with brute-force counts on small trees, Catalan / binary-
    tree shortcuts, the dominant trap of reporting the *unrestricted*
    total over all length values (W7 -- "length-constraint dropped"), or
    a misreading of the `K = 22` clause as something other than "array
    length is exactly `22`" (W8 -- "length-constraint reinterpreted").
  * One or two near-misses whose method genuinely reproduces the
    length-`K` path-partition count on small hand-checkable trees but
    slips in one of the multiplicative, coefficient-extraction, or
    modular-reduction steps for this `N = 44` tree.
  * One or two truncations that begin from a defensible length-`K`
    counting argument but stop before committing to a final integer
    modulo `997`.

No response was modified after generation other than to add stable line
breaks and Markdown wrapping; no numerical claims were altered. Whether each
response is correct, near-miss, or truncated is recorded in the gold oracle
at `/tests/oracle.json`. The provenance is supplied here only to confirm
that the responses are genuine independent generations and not adversarial
hand-crafted strings.

The audit task is to read the responses one at a time, classify each
independently against the four-code failure-reason vocabulary using the
W-trap method-pattern classifier and the R1..R4 audit rules in
`instruction.md`, and produce the structural per-audit fields
`primary_failure_evidence` and `alternative_codes_considered` for every
response. The deterministic judge grades each per-response audit
all-or-nothing.
