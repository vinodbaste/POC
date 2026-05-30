# Solution justification

## 1. Gold derivation (full problem, $a = h = 2025$)

Set up the regular hexagon with side $a$ and center $O$ at the origin in the
plane $z = 0$ (bottom base) and $z = h$ (top base). Label the top hex vertices
counter-clockwise so that $A, B, C, D, E, F$ are at angles
$90°, 150°, 210°, 270°, 330°, 30°$ from $O$, each at distance $a$ from $O$.
Then $A = (0, a, h)$ and $D = (0, -a, h)$ are diametrically opposite on the
top hexagon (since opposite hexagon vertices are exactly $2a$ apart), and
$D' = (0, -a, 0)$ sits directly below $D$.

Three families of surface paths from $A$ to $D'$ are candidates for the
minimum:

**Family A — three-face lateral strip.** Unfold the three consecutive lateral
rectangles between $A$'s vertical edge and $D'$'s vertical edge into a single
flat $3a \times h$ strip. Then $A$ sits at $(0, h)$ and $D'$ at $(3a, 0)$,
giving squared length $(3a)^2 + h^2 = 9a^2 + h^2$. With $a = h = 2025$ this is
$10 \cdot 2025^2$, so length $2025\sqrt{10} \approx 6402$.

**Family B — broken base-edge path.** Walk from $A$ across the top hex along
the diameter $AD$ (length $2a$), then drop along the vertical edge $DD'$
(length $h$). Total length $2a + h$, equal to $3 \cdot 2025 = 6075$ at the
full parameters. This is a *valid* surface path with a $90°$ kink at $D$ —
its length is the sum of segment lengths, not a Euclidean hypotenuse.

**Family C — top hex + one adjacent lateral rectangle (unfolded together).**
Unfold the rectangle $DD'E'E$ (or, by symmetry, $CC'D'D$) attached to the
top hexagon along its shared edge $DE$. Hinge the rectangle outward so it
lies in the plane of the top hex. With $D = (0, -a)$, $E = (a\sqrt{3}/2,
-a/2)$, the outward normal to $DE$ is $(1/2, -\sqrt{3}/2)$, so the unfolded
position of $D'$ becomes $D + h \cdot (1/2, -\sqrt{3}/2) = (h/2, -a -
h\sqrt{3}/2)$. From $A = (0, a)$, the squared straight-line distance to the
unfolded $D'$ is

$$d^2 = (h/2)^2 + \left(2a + \frac{h\sqrt{3}}{2}\right)^2 = \frac{h^2}{4} +
4a^2 + 2 a h \sqrt{3} + \frac{3 h^2}{4} = 4a^2 + h^2 + 2 a h \sqrt{3}.$$

With $a = h = 2025$, this becomes $a^2 (5 + 2\sqrt{3}) = 2025^2 \cdot (5 +
2\sqrt{3})$, i.e. $d = 2025 \sqrt{5 + 2\sqrt{3}} \approx 5891.6$.

**Validity of Family C unfolding.** Parametrize the straight line in the
unfolded plane and check it crosses the shared edge $DE$ at an interior
point. Setting $A + t (D' - A)$ equal to $D + s (E - D)$ for $s \in [0, 1]$
yields $s = 1 / (\sqrt{3} + 1) = (\sqrt{3} - 1)/2 \approx 0.366$, which is
strictly inside $[0, 1]$. The unfolded straight line is therefore a valid
surface geodesic.

**Comparison.** $5 + 2\sqrt{3} \approx 8.464 < 10$, so Family C is strictly
shorter than Family A. Family B has length $3a = 3 \cdot 2025 = 6075 >
5891.6$, so Family B is not minimal either. No other unfolding family yields
a shorter straight-line distance (one can verify by checking the 1-lateral,
2-lateral, 4-lateral, 5-lateral, top-hex + 2-lateral, etc. variants — all
produce strictly longer squared distances at $a = h = 2025$).

The full-problem squared distance therefore decomposes as

$$d^2 = 2025^2 \cdot (5 + 2\sqrt{3}) = 20503125 + 8201250 \sqrt{3}.$$

Hence `gold_distance_squared_decomposition = {"rational_part": 20503125,
"radical_coefficient_sqrt3": 8201250}` in the output schema.

## 2. Anchor derivations

The general formulas (derived above) are:

- Family A squared length: $L_A^2(a, h) = 9 a^2 + h^2$.
- Family C squared length: $L_C^2(a, h) = 4 a^2 + h^2 + 2 a h \sqrt{3}$.
- Family B length: $L_B(a, h) = 2 a + h$ (broken, not a Euclidean hypotenuse;
  square only if compared as a sum of segment lengths against the others).

For each anchor parameter pair, the minimum squared surface distance comes
from the family whose squared length is smallest:

| Anchor | $a$ | $h$ | $L_A^2 = 9a^2 + h^2$ | $L_C^2 = 4a^2 + h^2 + 2ah\sqrt{3}$ | $L_B = 2a + h$ | Min squared | Decomposition |
|---|---|---|---|---|---|---|---|
| `anchor_a1_h1` | 1 | 1 | 10 | $5 + 2\sqrt{3} \approx 8.46$ | 3 (so $L_B^2 = 9$) | $5 + 2\sqrt{3}$ | $(5, 2)$ |
| `anchor_a1_h2` | 1 | 2 | 13 | $8 + 4\sqrt{3} \approx 14.93$ | 4 (so $L_B^2 = 16$) | 13 | $(13, 0)$ |
| `anchor_a2_h1` | 2 | 1 | 37 | $17 + 4\sqrt{3} \approx 23.93$ | 5 (so $L_B^2 = 25$) | $17 + 4\sqrt{3}$ | $(17, 4)$ |
| `anchor_a2_h3` | 2 | 3 | 45 | $25 + 12\sqrt{3} \approx 45.78$ | 7 (so $L_B^2 = 49$) | 45 | $(45, 0)$ |
| `anchor_a3_h2` | 3 | 2 | 85 | $40 + 12\sqrt{3} \approx 60.78$ | 8 (so $L_B^2 = 64$) | $40 + 12\sqrt{3}$ | $(40, 12)$ |

In each case the broken-edge Family B's *segment-sum* length $L_B$ has square
$L_B^2$ as listed, but $L_B$ itself is the actual distance (no Pythagorean
combination), so the relevant comparison is between the Euclidean
$\sqrt{L_A^2}$, $\sqrt{L_C^2}$, and $L_B$. At every anchor, $L_B$ is greater
than $\min(\sqrt{L_A^2}, \sqrt{L_C^2})$, so Family B never wins; the
minimum squared distance is $\min(L_A^2, L_C^2)$.

A method that commits to Family A on every prism (the popular failure mode in
the response bundle) would produce $(10, 0), (13, 0), (37, 0), (45, 0),
(85, 0)$ — wrong on anchors `a1_h1`, `a2_h1`, and `a3_h2` (three of five). A
method that commits to the false diameter+height shortcut $(2a)^2 + h^2 =
4a^2 + h^2$ (which ignores the $2 a h \sqrt{3}$ radical contribution) would
produce $(5, 0), (8, 0), (17, 0), (25, 0), (40, 0)$ — wrong on all five
anchors. A method that always picks the broken base-edge path would produce
$L_B^2 = (2a+h)^2$ values — wrong on every anchor.

## 3. Per-response classifications and majority-vote trap

The seven proposed responses split as follows on their final stated
distance:

- $2025 \sqrt{10}$ (Family A): A, C, D, G — four of seven (majority).
- $2025 \sqrt{5}$ (false diameter + height): E, F — two of seven.
- $6075$ (Family B broken path): B — one of seven.
- $2025 \sqrt{5 + 2\sqrt{3}}$ (Family C, the true minimum): none.

No response reaches the true minimum, so `acceptable_solution_ids = []` and
every response has `final_answer_correct = false`.

The seven candidate responses sample the natural failure modes of mid-grade
model attempts on this geometry: a popular but nonminimal lateral strip
choice (Family A); a confidently asserted but invalid diameter-and-height
shortcut (the $\sqrt{5}$ family); a valid but nonminimal broken base-edge
path (Family B); some responses with external-citation crutches; one
response with a wrong-hexagon-metric assertion.

The per-response oracle assignments are:

- **A**: final stated value $2025\sqrt{10}$ (Family A) AND asserts that the
  opposite-vertex distance on the hex base is $2 \cdot \text{side length}
  \cdot \sqrt{3}$ (wrong — true is $2 a$). Codes `F1, F5`.
- **B**: final stated value $6075$ derived as $3 s = 2 a + h$ broken path.
  Code `F3`. (B does mention $s\sqrt{5}$ as a candidate but explicitly
  rejects it via an edge-crossing argument and commits to $6075$; per R3 the
  LAST boxed answer is $6075$.)
- **C**: final stated value $2025\sqrt{10}$ (Family A), no external links,
  no wrong hex metric. Code `F1`.
- **D**: final stated value $2025\sqrt{10}$ (Family A), concise, no external
  links, no wrong hex metric. Code `F1`.
- **E**: final stated value $2025\sqrt{5}$, derivation uses "diameter of the
  hexagon (4050) and height of the prism (2025)" as right-triangle legs.
  Code `F2`. (No external links, no wrong hex metric: E states "the
  diameter is 2 * 2025 = 4050" correctly, even though it then misuses that
  value in a non-surface-path geometry.)
- **F**: final stated value $2025\sqrt{5}$ (false diameter+height shortcut)
  AND cites two YouTube links as evidence. Codes `F2, F4`.
- **G**: final stated value $2025\sqrt{10}$ (Family A) AND cites two YouTube
  links and one SlideShare link as evidence. Codes `F1, F4`.

`acceptable_solution_ids = []` (no response satisfies both R5 conditions).

## 4. Why this scoring widens the single-vs-multi gap

A single agent that multiplexes derivation and seven audits in one context
is structurally biased toward majority vote — four of seven responses
commit to Family A, so a vote-following single may adopt $2025\sqrt{10}$ as
its gold and report wrong values on the gold-distance decomposition AND on
the anchor pairs where Family C is the true minimum (`a1_h1`, `a2_h1`,
`a3_h2`). Multi-agent's dedicated `derive-gold-distance` sub-agent has one
job — compare every unfolding family on every parameter pair — and its
isolated context makes the comparison much cleaner. Per-response audits are
distributed to focused sub-agents that each read exactly one response and
apply the five-code rubric without distraction.

The anchor pattern (Family C wins on 3 of 5, Family A wins on 2 of 5) is
designed so that NO single committed method matches all anchors — the agent
must consciously compare both families on each anchor, which is hard to do
under attention pressure across seven simultaneous response audits.
