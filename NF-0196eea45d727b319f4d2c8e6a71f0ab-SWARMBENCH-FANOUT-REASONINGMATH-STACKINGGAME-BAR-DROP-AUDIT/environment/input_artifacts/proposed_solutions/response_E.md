Let’s break this down carefully.  

**Step 1 – Understand current occupied cells**  
We have a 12-column board, height 18 (rows 1 to 18 from bottom to top).  
Occupied cells are given up to row 16 only (no occupied cells initially in rows 17–18).  

I’ll convert to a mental grid, column by column (from col 1 to col 12).  
From given coordinates:  

Col 1: rows 1–16 all occupied except row 15 missing, row 14 missing? Wait check:  
From data:  
Col1: (1,1) (2,1) (3,1) (4,1) (5,1) (6,1) (7,1) (8,1) (9,1) (10,1) (11,1) (12,1) (13,1) (14,1) (15,1) (16,1) → Actually row 15,1 is present (15,1 is in the list). Row 14,1 present. So col1 rows 1 to 16 all filled.  

Col2: From data:  
(1,2) (2,2) (3,2) (4,2) (5,2) (6,2) (7,2) (8,2) (9,2) (10,2) (11,2) (12,2) (13,2) — missing (14,2) (15,2) (16,2).  
So col2: rows 1–13 filled, row 14 empty, row 15 empty, row 16 empty.  

Col3: From data:  
(1,3) (2,3) (3,3) no wait (3,3) not listed — check: row3 col3 not in data.  
Row3 col4 yes, col3 no. So col3:  
(1,3) (2,3) (4,3) (6,3) (8,3) (9,3) (10,3) (11,3) (12,3) (13,3) — missing (3,3) (5,3) (7,3) (14,3) present? Yes (14,3) is listed, (15,3) no, (16,3) no.  
So col3: rows 1,2,4,6,8,9,10,11,12,13,14 occupied — gaps at rows 3,5,7,15,16,17,18.  

But easier: Let’s just note for the columns we care about (11,12 initially empty).  

Check col11: Is any (r,11) in list? No. So col11 completely empty.  
Check col12: Is any (r,12) in list? No. So col12 completely empty.  

So columns 11 and 12 have no occupied cells initially.  

**Step 2 – First bar drop (col12)**  
Bar is 4 cells tall (vertical). Falls straight down in col12 until it contacts an occupied cell or reaches bottom row. But since col12 is empty, it will fall to row 1 and lock, occupying rows 1–4 in col12.  

Now grid: col12 rows 1–4 occupied.  

**Step 3 – Check for filled rows**  
A row is filled if all 12 columns occupied in that row.  

Current before any clears:  
Row 1: all cols occupied? Check col11 empty → no.  
Row 2: col11 empty → no.  
Row 3: col11 empty → no.  
Row 4: col11 empty → no.  
So no clears yet.  

**Step 4 – Second bar drop (col11)**  
Bar 4 cells tall, falls in col11.  
Col11 empty initially, but now check if any cells from previous bar in col11? No, only col12 got bar1.  
So col11 empty, falls to row 1, occupies rows 1–4 in col11.  

Now: col11 rows 1–4 occupied, col12 rows 1–4 occupied.  

Check filled rows:  
Row 1: all 12 cols occupied? Need to verify initial data:  
From given data, row1: cols 1–10 except col7? Wait: (1,7) missing, (1,8) present. Actually row1: (1,1)–(1,6) occupied, (1,7) missing, (1,8)–(1,10) occupied. So col7 empty in row1 initially. Now after adding bars in col11,12, row1 still missing col7. So not filled.  

Row 2: from data: (2,1)–(2,10) except col4,5 missing? Actually row2: (2,1)(2,2)(2,3)(2,6)(2,7)(2,8)(2,9)(2,10) → missing col4,5, and col7? Wait (2,7) present. So row2 missing col4,5, and col11,12? Now col11,12 filled rows 1–4, so row2 col11,12 are filled now. But col4,5 empty in row2 initially. So not filled.  

So no row clears yet.  

**Step 5 – Third bar drop (col12 again)**  
Now col12 currently has rows 1–4 occupied.  
New bar 4 tall in col12 falls:  
It will stack on top of current top in col12, which is row4. So it occupies rows 5–8 in col12.  

Now col12 rows 1–8 occupied.  

**Step 6 – Check filled rows again**  

We must check all rows 1–18 for all 12 cols occupied.  

Let’s systematically check initial data plus added bars:  

Initial occupied (from given coordinates):  
Row1: col1–6,8–10 → missing col7,11,12. After bars: col11 filled row1, col12 filled row1. Still missing col7.  
So row1 not filled.  

Row2: col1–3,6–10 → missing col4,5,11,12 initially. After bars: col11,12 filled row2. Still missing col4,5.  

Row3: col1,2,4,5,7–9 → missing col3,6,10,11,12 initially. After bars: col11 filled? Wait col11 only rows 1–4 filled, so row3 col11 empty. So row3 missing col3,6,10,11,12.  

Row4: col1–5,7–10 → missing col6,11,12 initially. After bars: col11,12 filled row4. Still missing col6.  

Row5: col1,2,4–9 → missing col3,10,11,12 initially. After bars: col11,12 filled? col11 rows 1–4 only, so row5 col11 empty. So missing col3,10,11,12.  

So no row is filled even after all bars.  

**Step 7 – Total occupied cells**  

Initial count from given list: Let’s count coordinates given:  

Row1: 9 cells (col1–6,8–10)  
Row2: 8 cells (1–3,6–10)  
Row3: 7 cells (1,2,4,5,7–9)  
Row4: 9 cells (1–5,7–10)  
Row5: 8 cells (1,2,4–9)  
Row6: 10 cells (1–10)  
Row7: 6 cells (1,2,4,6,8,9)  
Row8: 10 cells (1–10)  
Row9: 8 cells (1–3,5–9)  
Row10: 10 cells (1–10)  
Row11: 10 cells (1–10)  
Row12: 8 cells (1–3,5–9)  
Row13: 10 cells (1–10)  
Row14: 7 cells (1,3–8,10)  
Row15: 5 cells (1,4–8)  
Row16: 1 cell (1,6)  

Sum: 9+8=17, +7=24, +9=33, +8=41, +10=51, +6=57, +10=67, +8=75, +10=85, +10=95, +8=103, +10=113, +7=120, +5=125, +1=126 initial occupied cells.  

Now add bars:  
Bar1: 4 cells in col12 rows1–4  
Bar2: 4 cells in col11 rows1–4  
Bar3: 4 cells in col12 rows5–8  

Total added: 4+4+4=12 cells.  

No row clears, so final occupied cells = 126 + 12 = 138.  

**Final answer:**  

138