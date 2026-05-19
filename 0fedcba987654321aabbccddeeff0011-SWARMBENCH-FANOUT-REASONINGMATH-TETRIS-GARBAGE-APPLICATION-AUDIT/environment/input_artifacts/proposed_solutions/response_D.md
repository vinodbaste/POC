To determine the resulting board state after applying the garbage lines and processing any row-clears, follow these steps:

1. **Initial Board State:**
   
   ```
   0000000000
   0000000000
   0000000000
   0000000000
   0000000000
   0000000000
   0000000000
   0000000000
   0000010000
   0001011000
   0011111000
   1011111110
   1111111110
   1111111110
   ```

2. **Applying Each Garbage Line:**
   
   - **Garbage Line 1:** Hole at column 3
     ```
     0000000000
     0000000000
     0000000000
     0000010000
     0001011000
     0011111000
     1011111110
     1111111110
     1111111110
     0000000000
     ```

   - **Garbage Line 2:** Hole at column 5
     ```
     0000000000
     0000000000
     0000000000
     0000010000
     0001011000
     0001111100
     0011111000
     1011111110
     1111111110
     0000000000
     ```

   - **Garbage Line 3:** Hole at column 2
     ```
     0000000000
     0000000000
     0000000000
     0000010000
     0001011000
     0011111000
     1011111110
     1111111110
     1111111110
     0000000000
     ```

   - **Garbage Line 4:** Hole at column 3
     ```
     0000000000
     0000000000
     0000000000
     0000010000
     0001011000
     0011111000
     1011111110
     1111111110
     1111111110
     0000000000
     ```

3. **Processing Row-Clears:**
   
   After each garbage line is applied, the board is checked for any fully filled rows. If any row becomes entirely filled with ones, it is cleared, and the remaining rows shift downward with empty rows added at the top.

4. **Final Board State After Processing:**
   
   ```
   0000000000
   0000000000
   0000000000
   0000010000
   0001011000
   0011111000
   1011111110
   1111111110
   1111111110
   0000000000
   ```

**Final Answer:**

```
0000000000
0000000000
0000000000
0000010000
0001011000
0011111000
1011111110
1111111110
1111111110
0000000000
```