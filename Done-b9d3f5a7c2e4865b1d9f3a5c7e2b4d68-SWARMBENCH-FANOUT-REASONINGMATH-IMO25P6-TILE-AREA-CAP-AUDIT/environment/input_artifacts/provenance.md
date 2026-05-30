# Provenance

The sixteen files under `proposed_solutions/response_*.md` are raw outputs
from small/weak language models given the problem in `problem.md`. They
were collected with no rerolls or edits: misreadings of the area cap,
floor-vs-ceiling slips, miscounted grid sizes, and partition mistakes are
preserved verbatim so the audit can score whether each response respects
the (C2) partition and (C3) area cap constraints and arrives at the
correct minimum_tiles for the 4 × 4 grid.

No response was hand-engineered to fire a specific failure code. The five
codes in `instruction.md` are post-hoc trigger phrases capturing the
mistakes the models actually made.
