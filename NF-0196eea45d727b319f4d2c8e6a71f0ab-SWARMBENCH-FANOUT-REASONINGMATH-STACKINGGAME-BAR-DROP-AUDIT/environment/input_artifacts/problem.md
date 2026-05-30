A 12-column stacking game board has height 18. Each occupied cell is represented using coordinate notation instead of a binary grid.

Rows are numbered from bottom to top starting at 1, and columns are numbered from left to right starting at 1.

The currently occupied cells are:

```text id="cps6tr"
(1,1) (1,2) (1,3) (1,4) (1,5) (1,6) (1,8) (1,9) (1,10)
(2,1) (2,2) (2,3) (2,6) (2,7) (2,8) (2,9) (2,10)
(3,1) (3,2) (3,4) (3,5) (3,7) (3,8) (3,9)
(4,1) (4,2) (4,3) (4,4) (4,5) (4,7) (4,8) (4,9) (4,10)
(5,1) (5,2) (5,4) (5,5) (5,6) (5,7) (5,8) (5,9)
(6,1) (6,2) (6,3) (6,4) (6,5) (6,6) (6,7) (6,8) (6,9) (6,10)
(7,1) (7,2) (7,4) (7,6) (7,8) (7,9)
(8,1) (8,2) (8,3) (8,4) (8,5) (8,6) (8,7) (8,8) (8,9) (8,10)
(9,1) (9,2) (9,3) (9,5) (9,6) (9,7) (9,8) (9,9)
(10,1) (10,2) (10,3) (10,4) (10,5) (10,6) (10,7) (10,8) (10,9) (10,10)
(11,1) (11,2) (11,3) (11,4) (11,5) (11,6) (11,7) (11,8) (11,9) (11,10)
(12,1) (12,2) (12,3) (12,5) (12,6) (12,7) (12,8) (12,9)
(13,1) (13,2) (13,3) (13,4) (13,5) (13,6) (13,7) (13,8) (13,9) (13,10)
(14,1) (14,3) (14,4) (14,5) (14,6) (14,7) (14,8) (14,10)
(15,1) (15,4) (15,5) (15,6) (15,7) (15,8)
(16,1) (16,6)
```

Three 4-cell bars are introduced sequentially. Each bar:

* must remain vertical,
* falls straight downward in a single column,
* cannot pass through occupied cells,
* and locks immediately upon contact.

Whenever an entire row becomes filled across all 12 columns, that row disappears and every row above it shifts downward by one.

The three bars are dropped, in order, into:

* column 12,
* column 11,
* column 12 again.

After all falling and row-removal effects are completely resolved, determine the total number of occupied cells remaining on the board.

Do not provide intermediate states. Output only a single integer.
