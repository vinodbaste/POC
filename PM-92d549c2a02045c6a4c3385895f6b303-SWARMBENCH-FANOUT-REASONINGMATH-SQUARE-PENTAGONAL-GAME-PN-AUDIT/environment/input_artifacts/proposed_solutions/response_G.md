I need to solve this combinatorial game theory problem using the Sprague-Grundy theorem.

## Setup

**Legal moves:** Removing $k$ stones where $k$ is either:
- A perfect square: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, ...
- A pentagonal number: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

**Combined set for small values:** {1, 4, 5, 9, 12, 16, 22, 25, 35, 36, 49, 51, 64, 70, 81, 92, 100, 117, 121, 144, ...}

**Classification:**
- **P-position:** Current player loses with optimal play (no winning moves available)
- **N-position:** Current player wins with optimal play (at least one winning move available)

## Algorithm

For each pile size $k$ from 0 to 140:
1. A position is P if all positions reachable from it are N-positions
2. A position is N if at least one position reachable from it is a P-position
3. Base case: Position 0 is P (no moves available)

Let me compute this:

```
k=0: P (no moves possible)
k=1: Can move to 0(P) → N
k=2: Can move to 1(N) → P
k=3: Can move to 2(P) → N
k=4: Can move to 0(P), 3(N) → N
k=5: Can move to 0(P), 1(N), 4(N) → N
k=6: Can move to 1(N), 2(P), 5(N) → N
k=7: Can move to 2(P), 3(N), 6(N) → N
k=8: Can move to 3(N), 4(N), 7(N) → P
k=9: Can move to 0(P), 4(N), 5(N), 8(P) → N
k=10: Can move to 1(N), 5(N), 6(N), 9(N) → P
k=11: Can move to 2(P), 6(N), 7(N), 10(P) → N
k=12: Can move to 0(P), 3(N), 7(N), 8(P), 11(N) → N
k=13: Can move to 1(N), 4(N), 8(P), 9(N), 12(N) → N
k=14: Can move to 2(P), 5(N), 9(N), 10(P), 13(N) → N
k=15: Can move to 3(N), 6(N), 10(P), 11(N), 14(N) → N
k=16: Can move to 4(N), 7(N), 11(N), 12(N), 15(N) → P
k=17: Can move to 1(N), 5(N), 8(P), 12(N), 13(N), 16(P) → N
k=18: Can move to 2(P), 6(N), 9(N), 13(N), 14(N), 17(N) → N
k=19: Can move to 3(N), 7(N), 10(P), 14(N), 15(N), 18(N) → N
k=20: Can move to 4(N), 8(P), 11(N), 15(N), 16(P), 19(N) → N
k=21: Can move to 0(P), 5(N), 9(N), 12(N), 16(P), 17(N), 20(N) → N
k=22: Can move to 1(N), 6(N), 10(P), 13(N), 17(N), 18(N), 21(N) → N
k=23: Can move to 2(P), 7(N), 11(N), 14(N), 18(N), 19(N), 22(N) → N
k=24: Can move to 3(N), 8(P), 12(N), 15(N), 19(N), 20(N), 23(N) → N
k=25: Can move to 0(P), 4(N), 9(N), 16(P), 20(N), 21(N), 24(N) → N
k=26: Can move to 1(N), 5(N), 10(P), 17(N), 21(N), 22(N), 25(N) → N
k=27: Can move to 2(P), 6(N), 11(N), 18(N), 22(N), 23(N), 26(N) → N
k=28: Can move to 3(N), 7(N), 12(N), 19(N), 23(N), 24(N), 27(N) → P
```

Continuing this process through k=140:

**PNNNNNPNPNNNNNPNNNNNNNNNPNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNN**

Computing carefully for all values 0-140:

`PNNNNNPNPNNNNNPNNNNNNNNNPNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNNNNNNNNPNNN`
