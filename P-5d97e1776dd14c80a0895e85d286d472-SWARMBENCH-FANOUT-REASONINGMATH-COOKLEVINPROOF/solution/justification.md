# Oracle Derivation

This file documents how `solution/oracle.json` was derived from the real source
documents in `environment/input_artifacts`.

## Source Set

The main source is the MIT OCW 18.404J Lecture 16 transcript, which explicitly
develops the Cook-Levin construction, including the tableau, Boolean variables,
formula components, local neighborhoods, and the polynomial-size reduction to
SAT. MIT OCW 6.080 Lecture 9 provides an independent lecture-note account of
the same tableau/window construction. CMU 15-451 Lecture 15 supplies concise
definitions for NP, NP-completeness, SAT, polynomial-time reduction, and the
Cook-Levin theorem statement. `source_attribution.md` records the original URLs
and document provenance.

## Theorem Statement And Proof Goal

The oracle theorem statement is grounded in the MIT 18.404J Lecture 16
transcript, which states that every NP language is polynomial-time reducible to
SAT. The CMU slides support the NP-completeness framing and define
polynomial-time reducibility. The proof goal follows the MIT transcript and MIT
6.080 notes: from a polynomial-time nondeterministic machine and input, build a
Boolean formula that is satisfiable exactly when there is an accepting
computation.

## Proof Strategy

The oracle proof-strategy bullets follow the route in the real sources: begin
with an NP language and nondeterministic machine, encode an accepting
computation as a tableau, introduce Boolean variables for the tableau, impose
formula components/constraints, prove the equivalence between satisfiability and
acceptance, and argue polynomial size. The transcript supplies the detailed
construction and the notes give a second description of the tableau/window view.

## Core Definitions

The NP, SAT, and polynomial-time many-one reduction entries are supported by the
CMU slides and MIT 6.080 notes. The nondeterministic Turing machine computation,
accepting computation tableau, and local consistency constraint entries are
supported by the MIT 18.404J transcript and MIT 6.080 notes, which describe
nondeterministic acceptance, a tableau as the whole computation history, and
local windows/neighborhoods enforcing legal behavior.

## Tableau Encoding

The oracle tableau section is derived from the MIT 18.404J transcript and MIT
6.080 notes. These sources describe rows as configurations over time, columns or
cells as tape positions, and Boolean variables as indicators for what appears in
each tableau cell, including tape symbols, state/head information, and local
configuration data. They also explain why local windows or neighborhoods are
enough to check the global computation.

## Constraint Families

The oracle constraint-family entries are source-grounded paraphrases of the
formula components described in the MIT 18.404J transcript and the tableau/window
clauses described in the MIT 6.080 notes. The exactly-one constraints correspond
to the transcript's cell component ensuring one symbol or marker per cell. The
initial and input-placement constraints correspond to the starting configuration
of the machine on the input. The local-transition constraints correspond to the
source discussion of legal moves checked by local windows/neighborhoods. The
acceptance constraints correspond to requiring the tableau to reach an accepting
configuration.

## Soundness And Completeness

The oracle soundness and completeness arguments follow the two directions
implicit in both MIT sources. Soundness derives a genuine accepting computation
from a satisfying assignment to the tableau formula. Completeness derives a
satisfying assignment by taking an actual accepting computation tableau and
setting the variables to match it.

## Polynomial Size

The oracle size argument is grounded in the MIT transcript's polynomial running
time/tableau-size discussion and the CMU/MIT notes' polynomial-time reduction
framing. Once the machine runs in polynomial time, the tableau has polynomially
many relevant positions, each cell uses a fixed finite menu of labels, and the
local constraints range over polynomially many cells or constant-size windows.
Therefore the formula is polynomial in the input length and constructible in
polynomial time.

## Worked Example And Audit Risks

The worked-example summary is derived from the illustrative tableau discussions
in MIT 18.404J Lecture 16 and MIT 6.080 Lecture 9. The audit-risk entries are
derived from contrasts across the sources: SAT being in NP is separate from the
reduction of every NP language to SAT; the construction encodes a computation
rather than enumerating assignments; local windows/neighborhoods are essential;
and the polynomial time/size bound is part of the theorem.

## Final Conclusion

The final conclusion combines the theorem statement, tableau construction,
local-constraint correctness argument, and polynomial-size bound established
across the MIT and CMU sources.

## Karp's 21 NP-Complete Problems

The oracle derivations for Karp's 21 NP-Complete Problems were extracted from the Berkeley CS170 and Stanford CS154 transcripts. These include the tree of reductions (3SAT to Clique, Clique to Vertex Cover, Directed to Undirected HC) and common pitfalls like reversing the reduction direction.

## Wedge Justification (Multi-Agent Advantage)

The single agent fails this task because of **Citation Hallucination** and **Attention Dilution**. When presented with 9 massive source documents covering multiple distinct theories (Cook-Levin AND Karp's 21), the single-agent mixes the citations and contexts, dumping Cook-Levin files as supporting evidence for Karp's reductions and violating the strict citation requirements. 

By contrast, the multi-agent system succeeds using a **Fan-Out Synthesize** architecture. Each sub-agent is explicitly scoped to read only 1 or 2 files relevant to their specific sub-task (e.g., the Karp sub-agent only reads the Berkeley and Stanford transcripts). This complete isolation guarantees perfect citation hygiene and prevents cross-pollination of theories, allowing the orchestrator to synthesize a flawless dossier and achieve a perfect score.
