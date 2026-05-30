# Oracle Justification

## Ground-truth final answer

The minimum surface distance from $A$ on the top hexagonal base to $D'$ on the bottom hexagonal base of a regular hexagonal prism with side $a = 2025$ and height $h = 2025$ is

$$ d = 2025\,\sqrt{5 + 2\sqrt{3}} \approx 5891. $$

This value is realised by the **base-plus-lateral-face unfolding family**: unfold the bottom hexagonal face containing $D'$ about its shared edge with one bottom-touching lateral rectangle. In this flat development the straight-line segment from $A$ to the unfolded image of $D'$ has squared length

$$ d^2 = 2025^2 \,\big(5 + 2\sqrt{3}\big) = 20\,503\,125 + 8\,201\,250\,\sqrt{3}. $$

Reported in the oracle as
`{"rational_part": 20503125, "radical_coefficient_sqrt3": 8201250}`.

The three commonly proposed competitors are all longer or invalid:

- **Three-face lateral strip** unfolding gives $2025\sqrt{10} \approx 6402$ — valid surface path, but longer.
- **Broken base-edge path** of length $2a + h = 6075$ — valid surface path, but longer than the base-plus-lateral diagonal.
- **False "diameter and height" right-triangle shortcut** $2025\sqrt{5} \approx 4528$ — numerically smaller, but does NOT correspond to a valid surface unfolding (it would have to cut through the prism interior). The classic single-agent trap.

## Per-response classifications

| ID | Final answer | `failure_reasons` | Why |
|----|--------------|-------------------|-----|
| A | $2025\sqrt{10}$ | `[F1, F5]` | Three-face lateral-strip + asserts the false long-diagonal $2a\sqrt{3}$ |
| B | $6075$ | `[F3]` | Broken base-edge path $2a + h$ |
| C | $2025\sqrt{10}$ | `[F1]` | Three-face lateral-strip, terse |
| D | $2025\sqrt{10}$ | `[F1]` | Three-face lateral-strip |
| E | $2025\sqrt{5}$ | `[F2]` | False diameter-and-height shortcut |
| F | $2025\sqrt{5}$ | `[F2, F4]` | Diameter-and-height + YouTube / SlideShare citation |
| G | $2025\sqrt{10}$ | `[F1, F4]` | Three-face lateral-strip + YouTube / SlideShare citation |
| H | $6075$ | `[F3, F5]` | Broken base-edge path + asserts the false long-diagonal $2a\sqrt{3}$ |
| I | $2025\sqrt{5}$ | `[F2, F5]` | Diameter-and-height + asserts the false long-diagonal $2a\sqrt{3}$ |

**`acceptable_solution_ids`:** `[]` — no response derives the true minimum $2025\sqrt{5 + 2\sqrt{3}}$.

## Why the multi-agent decomposition outperforms a single agent

Nine responses cluster around three wrong answers: four commit to $2025\sqrt{10}$ (lateral strip), three to $2025\sqrt{5}$ (diameter-height shortcut), two to $6075$ (broken base-edge). A single agent that derives its "independent" gold answer while reading the nine responses in the same context window is heavily biased by this 4 / 3 / 2 vote and is likely to pick $2025\sqrt{10}$ as the ground truth (or, if it prefers the smallest number, $2025\sqrt{5}$). Either choice misses the true minimum $2025\sqrt{5 + 2\sqrt{3}}$ from the base-plus-lateral-face unfolding, costing the agent the 100-point `gold_distance_squared_decomposition` credit AND the 30 points on every response it then mis-marks `final_answer_correct = true`.

The fan-out-synthesize decomposition isolates the gold derivation into a dedicated `derive-gold-distance` sub-agent that reads only `/input_artifacts/problem.md`. Each of the nine `audit-response-X` sub-agents reads exactly one response file and applies the five-code phrase-trigger vocabulary with the full attention budget for the multi-code co-fires (F1+F5, F2+F4, F1+F4, F3+F5, F2+F5). The synthesizer is purely structural: it copies each audit's verdict, computes `acceptable_solution_ids = []`, and writes the JSON. This structural specialisation lets multi-agent score near-1.0 while single-agent typically loses 100 + 4 × 30 ≈ 220 points on the gold-and-final-answer axis alone.
