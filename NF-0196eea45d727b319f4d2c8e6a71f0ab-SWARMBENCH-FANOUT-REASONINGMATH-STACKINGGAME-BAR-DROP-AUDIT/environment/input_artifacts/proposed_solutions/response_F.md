To solve the problem, we will analyze the board and drop the bars sequentially while applying the rules provided.

1. **Initial Board Setup:**
   The occupied cells are as follows (rows from 1 at the bottom to 18 at the top):
   - Row 1: 1, 2, 3, 4, 5, 6, 8, 9, 10
   - Row 2: 1, 2, 3, 6, 7, 8, 9, 10
   - Row 3: 1, 2, 4, 5, 7, 8, 9
   - Row 4: 1, 2, 3, 4, 5, 7, 8, 9, 10
   - Row 5: 1, 2, 4, 5, 6, 7, 8, 9
   - Row 6: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   - Row 7: 1, 2, 4, 6, 8, 9
   - Row 8: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   - Row 9: 1, 2, 3, 5, 6, 7, 8, 9
   - Row 10: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   - Row 11: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   - Row 12: 1, 2, 3, 5, 6, 7, 8, 9
   - Row 13: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   - Row 14: 1, 3, 4, 5, 6, 7, 8, 10
   - Row 15: 1, 4, 5, 6, 7, 8
   - Row 16: 1, 6

2. **Dropping the Bars:**
   - **First bar** in column 12:
     - Drops to Row 10 (occupied), then stops at Row 11.
     - The occupied cell in Row 11 at Column 12 is now (11,12).
   - **Second bar** in column 11:
     - Drops to Row 10 (occupied), stops at Row 11.
     - Occupies (11,11).
   - **Third bar** in column 12:
     - Drops to Row 10 (occupied), then stops at Row 11 (now two bars occupy).
     - Occupies (11,12) and (11,11).

3. **Row Removal:**
   - After dropping all three bars, we look for any full rows:
     - Row 10 is full across all columns (from Row 1 to Row 12), removing it.

4. **Final Occupied Count:**
   After removing the full row and recounting the remaining occupied cells, we discover:

- There are no changes in the overall number of occupied cells except for the removal of Row 10.

In total, **the count of the remaining occupied cells** is determined:

**Result: 152**