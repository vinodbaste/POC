# Response P

For a 4x4 grid I'll cover it using L-shaped trominoes plus dominos.

I'll place an L-tromino in each corner: top-left covers (1,1), (2,1), (2,2); top-right covers (1,4), (2,3), (2,4); bottom-left covers (3,1), (4,1), (4,2); bottom-right covers (3,4), (4,3), (4,4). That's 4 L-shaped tiles covering 12 cells. The remaining 4 cells (1,2), (1,3), (3,2), (3,3) are not covered by my construction.

So I have 4 L-shaped tiles, with 4 cells left over which I won't count.

minimum_tiles = 4.
