# Three-largest-proper-divisor fixed points (modified IMO 2025 P4)

## Definitions

A **proper divisor** of a positive integer n is a positive divisor of n other than n itself. (So 1 counts as a proper divisor of every n > 1, but n itself never counts.)

For a positive integer n with at least three proper divisors, define
s(n) = d_1 + d_2 + d_3
where d_1 > d_2 > d_3 are the three largest proper divisors of n.

If n has fewer than three proper divisors, s(n) is **undefined** and n is **not counted** in any of the quantities below.

## Problem statement

Restrict attention to integers n with 4 ≤ n ≤ 30. Determine

    fixed_point_count = the number of integers n with 4 ≤ n ≤ 30 such
                        that n has at least three proper divisors AND
                        s(n) = n.

Report:
- `fixed_point_count`: the integer described above.

## Note on the original problem

The original IMO 2025 Problem 4 considers infinite sequences a_1, a_2, ... where a_{i+1} = s(a_i) and asks for all possible values of a_1. The modified problem above is a strictly finite, finite-range fixed-point count using the same operator s; it does not assume anything about iteration beyond one step.
