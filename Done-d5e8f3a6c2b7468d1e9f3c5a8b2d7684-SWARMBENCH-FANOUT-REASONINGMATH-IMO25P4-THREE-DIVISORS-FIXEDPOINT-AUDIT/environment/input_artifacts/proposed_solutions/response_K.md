# Response K

Enumerate n in [4, 30] with at least three proper divisors. (Composites with at least three proper divisors — primes have only one proper divisor 1 and are skipped, and squares of primes such as 9 and 25 have only two proper divisors.)

For each surviving n I compute s(n) = sum of the three largest proper divisors. After running through the list:
- n = 6 has proper divisors {1, 2, 3}; the three largest are {1, 2, 3} with sum 6. Fixed point.
- n = 18 has proper divisors {1, 2, 3, 6, 9}; the three largest are {3, 6, 9} with sum 18. Fixed point.
- All other surviving n give s(n) different from n (mostly close to n but off by a few).

So fixed_point_count = 2.
