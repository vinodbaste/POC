The chip makes exactly \(2026\) moves (one for each unit descending in the \(y\)-direction).  
Let \(L\) be the number of left moves \((m-1,n-1)\) and \(R\) the number of right moves \((m+1,n-1)\).

\[
L+R=2026,\qquad 1234+(R-L)=0\;\Longrightarrow\;L-R=1234.
\]

Solving,
\[
L=\frac{2026+1234}{2}=1630,\qquad R=\frac{2026-1234}{2}=396.
\]

Thus the number of distinct paths equals the number of ways to choose the positions of the \(R=396\) right moves among the \(2026\) steps:

\[
N=\binom{2026}{396}.
\]

We need \(N \pmod{1000}\).  
Since \(1000=2^{3}\cdot5^{3}\), compute the exponents of \(2\) and \(5\) in the binomial coefficient.

---

### Exponent of \(2\)

Using the Legendre formula \(v_2\bigl(\binom{n}{k}\bigr)=s_2(k)+s_2(n-k)-s_2(n)\) where \(s_2(x)\) is the sum of binary digits:

\[
\begin{aligned}
s_2(2026)&=8,\\
s_2(396)&=4,\\
s_2(1630)&=7.
\end{aligned}
\]

Hence \(v_2(N)=4+7-8=3\). So \(N\) is divisible by \(2^3=8\) but not by \(2^4\).

---

### Exponent of \(5\)

Similarly, with base-5 digit sums:

\[
\begin{aligned}
s_5(2026)&=6,\\
s_5(396)&=8,\\
s_5(1630)&=6.
\end{aligned}
\]

Thus \(v_5(N)=8+6-6=8\). So \(N\) is divisible by \(5^8\), in particular by \(5^3=125\).

---

Since \(v_2(N)\ge3\) and \(v_5(N)\ge3\), the binomial coefficient is divisible by \(2^3\cdot5^3=1000\).

\[
N\equiv0\pmod{1000}.
\]

\[
\boxed{0}
\]
