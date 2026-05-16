# Solution

Let me work through this step-by-step.

**Step 1: Identify column 9 (rightmost column)**
Column 9 is currently empty throughout the board.

**Step 2: Place 3 vertical I-pieces in column 9**
- I-piece 1: Rows 16-19 (bottom 4 cells)
- I-piece 2: Rows 12-15 (next 4 cells up)
- I-piece 3: Rows 8-11 (next 4 cells up)

**Step 3: Identify complete rows after placement**
After placing the pieces, these rows become complete (all 10 cells filled):
- Row 9: 1111111111
- Row 11: 1111111111
- Row 12: 1111111111
- Row 14: 1111111111
- Row 19: 1111111111

**Step 4: Clear complete rows and shift**
Five rows are cleared. The remaining rows shift down, with 5 new empty rows appearing at the top.

**Final board state:**

```text
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
1000010000
1000110000
1011111011
1110111111
1101010111
1110111111
1101100111
1111101111
1110011111
0000000000
0000000000
0000000000
0000000000
0000000000
```
