Let's analyze the board state and the effect of dropping the three bars.

Initial occupied cells: 159

Bar 1 (column 12):
The bar consists of cells (1,12), (2,12), (3,12), (4,12).
The occupied cells in column 12 are initially none. So the bar falls successfully to (1,12), (2,12), (3,12), (4,12).
The new board has 159 + 4 = 163 occupied cells.

Bar 2 (column 11):
The bar consists of cells (1,11), (2,11), (3,11), (4,11).
The occupied cells in column 11 are initially none. So the bar falls successfully to (1,11), (2,11), (3,11), (4,11).
The new board has 163 + 4 = 167 occupied cells.

Bar 3 (column 12):
The bar consists of cells (1,12), (2,12), (3,12), (4,12).
The cells (1,12), (2,12), (3,12), (4,12) are already occupied. So the bar will stop at the first occupied cell it encounters from the top. The bar does not fall.

Now, let's consider row clearing. We need to check if any rows are completely filled.

Row 1: (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,8), (1,9), (1,10), (1,11), (1,12) - 11 cells filled
Row 2: (2,1), (2,2), (2,3), (2,6), (2,7), (2,8), (2,9), (2,10), (2,11), (2,12) - 10 cells filled
Row 3: (3,1), (3,2), (3,4), (3,5), (3,7), (3,8), (3,9), (3,11), (3,12) - 9 cells filled
Row 4: (4,1), (4,2), (4,3), (4,4), (4,5), (4,7), (4,8), (4,9), (4,10), (4,11), (4,12) - 11 cells filled
Row 5: (5,1), (5,2), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,11), (5,12) - 10 cells filled
Row 6: (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9), (6,10), (6,11), (6,12) - 12 cells filled. Row 6 is full, so it clears.
Row 7: (7,1), (7,2), (7,4), (7,6), (7,8), (7,9), (7,11), (7,12) - 8 cells filled
Row 8: (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9), (8,10), (8,11), (8,12) - 12 cells filled. Row 8 is full, so it clears.
Row 9: (9,1), (9,2), (9,3), (9,5), (9,6), (9,7), (9,8), (9,9), (9,11), (9,12) - 10 cells filled
Row 10: (10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8), (10,9), (10,10), (10,11), (10,12) - 12 cells filled. Row 10 is full, so it clears.
Row 11: (11,1), (11,2), (11,3), (11,4), (11,5), (11,6), (11,7), (11,8), (11,9), (11,10), (11,11), (11,12) - 12 cells filled. Row 11 is full, so it clears.
Row 12: (12,1), (12,2), (12,3), (12,5), (12,6), (12,7), (12,8), (12,9), (12,11), (12,12) - 10 cells filled
Row 13: (13,1), (13,2), (13,3), (13,4), (13,5), (13,6), (13,7), (13,8), (13,9), (13,10) - 10 cells filled
Row 14: (14,1), (14,3), (14,4), (14,5), (14,6), (14,7), (14,8), (14,10) - 8 cells filled
Row 15: (15,1), (15,4), (15,5), (15,6), (15,7), (15,8) - 6 cells filled
Row 16: (16,1), (16,6) - 2 cells filled
Row 17: (empty) - 0 cells filled
Row 18: (empty) - 0 cells filled

Rows 6, 8, 10, 11 clear.
Remaining occupied cells: 167 - (12 + 12 + 12 + 12) = 167 - 48 = 119

Final Answer: The final answer is $\boxed{119}$