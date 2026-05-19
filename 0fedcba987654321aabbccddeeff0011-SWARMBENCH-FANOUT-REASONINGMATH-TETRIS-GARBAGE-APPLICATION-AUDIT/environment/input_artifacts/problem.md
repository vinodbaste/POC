I am playing a game of Tetris with a 10-by-20 board. The current board state is as follows, where 0s represent empty cells and 1s represent filled cells (rows are presented from the top of the board to the bottom of the board):

0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
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

I now receive 4 garbage lines from my opponent, with holes at columns [3, 3, 5, 2] (zero-indexed, applied in order — the first garbage line is the oldest and ends up highest within the garbage block; the last is the newest and ends up at the very bottom). Each garbage line is a row of nine 1s and one 0 (the hole), at the indicated zero-indexed column. The garbage rises from the bottom of the playfield, pushing the existing board content upward by 4 rows; any rows that would shift above row 0 are lost off the top of the playfield (standard "topout" behavior — but in this instance the top 4 rows of the existing board are all empty so nothing meaningful tops out). After the garbage is applied, standard row-clearing mechanics fire: any row that becomes entirely filled with 1s is cleared and remaining rows shift down with empty rows added at the top.

What is the board state after the 4 garbage lines have been applied and any resulting clears have been processed? Please format your answer using exactly 20 lines, each line containing exactly 10 digits, each digit being either 0 or 1, where a 0 represents an empty cell and a 1 represents a filled cell.
