**400**

The number of distinct paths \(N\) from \((1234, 2026)\) to \((0, 0)\) is the binomial coefficient \(\dbinom{2026}{396}\), since it requires 2026 moves downward, with 396 right moves (+1 in \(x\)) and 1630 left moves (-1 in \(x\)) to achieve a net \(x\)-displacement of -1234.[[1]](https://cp-algorithms.com/combinatorics/binomial-coefficients.html)[[2]](https://www.redcrab-software.com/en/Calculator/Binomial-Coefficient)

To compute \(N \mod 1000\), factor \(1000 = 8 \times 125\) and use the Chinese Remainder Theorem.

- The 2-adic valuation \(v_2(N) = 3 \geq 3\), so \(N \equiv 0 \pmod{8}\).
- For mod 125, compute the 5-free factorial parts \(g(x!) = \prod_{j=1}^x (j / 5^{v_5(j)})\) modulo 125:
  - The product over each block of 125 consecutive integers is \(24 \pmod{125}\).
  - \(g(2026!) \equiv 24^{16} \times \prod_{j=1}^{26} (j / 5^{v_5(j)}) \equiv 101 \times 1 \equiv 101 \pmod{125}\).
  - \(g(396!) \equiv 24^3 \times \prod_{j=1}^{21} (j / 5^{v_5(j)}) \equiv 74 \times 104 \equiv 71 \pmod{125}\).
  - \(g(1630!) \equiv 24^{13} \times \prod_{j=1}^5 (j / 5^{v_5(j)}) \equiv 74 \times 24 \equiv 26 \pmod{125}\).
  - Free part: \(101 \times 71^{-1} \times 26^{-1} \equiv 101 / 96 \equiv 31 \pmod{125}\).
  - With \(v_5(N) = 2\), \(N \equiv 25 \times 31 = 25 \pmod{125}\).[[1]](https://cp-algorithms.com/combinatorics/binomial-coefficients.html)

Solve \(x \equiv 0 \pmod{8}\), \(x \equiv 25 \pmod{125}\): \(x = 125k + 25\), \(125k + 25 \equiv 0 \pmod{8}\) yields \(k \equiv 3 \pmod{8}\), so \(x \equiv 400 \pmod{1000}\).[[1]](https://cp-algorithms.com/combinatorics/binomial-coefficients.html)

