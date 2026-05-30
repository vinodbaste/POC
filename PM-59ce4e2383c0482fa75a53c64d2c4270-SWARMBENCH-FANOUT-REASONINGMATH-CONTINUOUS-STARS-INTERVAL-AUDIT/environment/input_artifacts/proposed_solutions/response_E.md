# Solution

## Problem Setup

We have $N = 12$ nights with visibility counts:
$$A = [4, 1, 3, 5, 2, 2, 3, 1, 5, 6, 2, 1]$$

Total observations: $\sum_{i=1}^{12} A_i = 35$

---

## Finding Maximum $M$

**Strategy:** Minimize the duration of each star's visibility.

The optimal configuration is to have each star visible for exactly **one night**.

- On night $i$, place exactly $A_i$ distinct stars that are only visible on night $i$
- These stars don't overlap with any other stars
- This requires no conflicts and is clearly achievable

Therefore:
$$M = \sum_{i=1}^{12} A_i = 4+1+3+5+2+2+3+1+5+6+2+1 = \boxed{35}$$

---

## Finding Minimum $m$

**Strategy:** Maximize the duration of each star's visibility through continuous intervals.

**Key Insight:** Consider the "flow" of stars across consecutive nights.

Define transitions between consecutive nights:
- If $A_{i+1} > A_i$: need $(A_{i+1} - A_i)$ new stars to start on night $(i+1)$
- If $A_{i+1} < A_i$: $(A_i - A_{i+1})$ stars must end on night $i$
- If $A_{i+1} = A_i$: some stars may continue without changes

**Transitions:**
| Night | Count | Change |
|-------|-------|--------|
| 1 | 4 | Start 4 |
| 2 | 1 | End 3 |
| 3 | 3 | Start 2 |
| 4 | 5 | Start 2 |
| 5 | 2 | End 3 |
| 6 | 2 | No change |
| 7 | 3 | Start 1 |
| 8 | 1 | End 2 |
| 9 | 5 | Start 4 |
| 10 | 6 | Start 1 |
| 11 | 2 | End 4 |
| 12 | 1 | End 1 |
| After | 0 | End remaining |

**Classic Result:** The minimum number of intervals required to satisfy a sequence is equal to the **maximum value** in the sequence.

This is because:
1. We can never use fewer than $\max(A_i)$ stars, since on night $i$ we need at least $A_i$ stars visible simultaneously
2. We can always achieve exactly $\max(A_i)$ stars by carefully managing start/end points

**Maximum value:** $\max(A) = 6$ (on night 10)

Therefore:
$$m = \boxed{6}$$

**Verification:** We can construct a solution with exactly 6 stars by having some stars' intervals span multiple nights while maintaining the visibility counts at each night.

---

## Final Answer

$$m + M = 6 + 35 = \boxed{41}$$