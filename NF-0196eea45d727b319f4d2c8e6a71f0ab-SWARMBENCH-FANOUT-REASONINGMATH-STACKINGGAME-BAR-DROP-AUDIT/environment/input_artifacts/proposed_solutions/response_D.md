Okay, let's simulate the stacking game with the given initial state and the sequence of bar drops.

**Initial State:** The board is 12 columns wide and 18 rows high. The occupied cells are given in the problem description.

**Bar 1: Column 12**

The first 4-cell bar is dropped into column 12. We need to find the lowest empty cell in column 12. Looking at the initial state, column 12 is empty up to row 14. Row 14 has an occupied cell at (14,1). Thus, the lowest empty cell in column 12 is row 1. So the bar will occupy cells (1,12), (2,12), (3,12), and (4,12).

**Bar 2: Column 11**

The second 4-cell bar is dropped into column 11. We need to find the lowest empty cell in column 11. Column 11 is empty up to row 18. Thus, the lowest empty cell in column 11 is row 1. So the bar will occupy cells (1,11), (2,11), (3,11), and (4,11).

**Bar 3: Column 12**

The third 4-cell bar is dropped into column 12. After the first bar, cells (1,12), (2,12), (3,12), and (4,12) are occupied. So the lowest empty cell in column 12 is row 5. The bar will occupy cells (5,12), (6,12), (7,12), and (8,12).

**Row Removal**

Now we need to check for any full rows and remove them.
*   Row 1: (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,8), (1,9), (1,10), (1,12), (1,11) - Not full.
*   Row 2: (2,1), (2,2), (2,3), (2,6), (2,7), (2,8), (2,9), (2,10), (2,12), (2,11) - Not full.
*   Row 3: (3,1), (3,2), (3,4), (3,5), (3,7), (3,8), (3,9), (3,12), (3,11) - Not full.
*   Row 4: (4,1), (4,2), (4,3), (4,4), (4,5), (4,7), (4,8), (4,9), (4,10), (4,12), (4,11) - Not full.
*   Row 5: (5,1), (5,2), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,12) - Not full.
*   Row 6: (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9), (6,10), (6,12) - Not full.
*   Row 7: (7,1), (7,2), (7,4), (7,6), (7,8), (7,9), (7,12) - Not full.
*   Row 8: (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9), (8,10), (8,12) - Not full.
*   Row 9: (9,1), (9,2), (9,3), (9,5), (9,6), (9,7), (9,8), (9,9) - Not full.
*   Row 10: (10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8), (10,9), (10,10) - Full.
*   Row 11: (11,1), (11,2), (11,3), (11,4), (11,5), (11,6), (11,7), (11,8), (11,9), (11,10) - Full.
*   Row 12: (12,1), (12,2), (12,3), (12,5), (12,6), (12,7), (12,8), (12,9) - Not full.
*   Row 13: (13,1), (13,2), (13,3), (13,4), (13,5), (13,6), (13,7), (13,8), (13,9), (13,10) - Full.
*   Row 14: (14,1), (14,3), (14,4), (14,5), (14,6), (14,7), (14,8), (14,10) - Not full.
*   Row 15: (15,1), (15,4), (15,5), (15,6), (15,7), (15,8) - Not full.
*   Row 16: (16,1), (16,6) - Not full.

Rows 10, 11, and 13 are full and will be removed. All rows above shift down.

After removing rows 10, 11, and 13, the number of occupied cells is:
Initial cells: 79
New cells: 4 + 4 + 4 = 12
Total cells before removal: 79 + 12 = 91

Full rows: 3
Cells in full rows: 12 * 3 = 36. However, we can't simply subtract 36 because the rows above shift down. We need to count the remaining cells.

Let's count the cells after the bar drops, then remove the rows.
Occupied cells:
(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,8), (1,9), (1,10), (1,12), (1,11)
(2,1), (2,2), (2,3), (2,6), (2,7), (2,8), (2,9), (2,10), (2,12), (2,11)
(3,1), (3,2), (3,4), (3,5), (3,7), (3,8), (3,9), (3,12), (3,11)
(4,1), (4,2), (4,3), (4,4), (4,5), (4,7), (4,8), (4,9), (4,10), (4,12), (4,11)
(5,1), (5,2), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,12)
(6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9), (6,10), (6,12)
(7,1), (7,2), (7,4), (7,6), (7,8), (7,9), (7,12)
(8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9), (8,10), (8,12)
(9,1), (9,2), (9,3), (9,5), (9,6), (9,7), (9,8), (9,9)
(10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8), (10,9), (10,10)
(11,1), (11,2), (11,3), (11,4), (11,5), (11,6), (11,7), (11,8), (11,9), (11,10)
(12,1), (12,2), (12,3), (12,5), (12,6), (12,7), (12,8), (12,9)
(13,1), (13,2), (13,3), (13,4), (13,5), (13,6), (13,7), (13,8), (13,9), (13,10)
(14,1), (14,3), (14,4), (14,5), (14,6), (14,7), (14,8), (14,10)
(15,1), (15,4), (15,5), (15,6), (15,7), (15,8)
(16,1), (16,6)

Rows 10, 11, 13 are removed.

The number of occupied cells is 91. Removing rows 10, 11, and 13, we have 91 - 30 = 61.
The row removal shifts the rows above down.

After row removal and shifting, count the remaining occupied cells.
After careful calculation, the total number of occupied cells remaining is 61.

```
61
```