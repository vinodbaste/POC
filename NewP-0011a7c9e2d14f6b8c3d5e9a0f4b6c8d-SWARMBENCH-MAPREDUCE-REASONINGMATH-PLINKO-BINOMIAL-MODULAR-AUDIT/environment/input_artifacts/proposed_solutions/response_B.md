Let the starting position be $(X_0, Y_0) = (1234, 2026)$. The target position is $(X_f, Y_f) = (0,0)$.
Each step changes the position from $(m, n)$ to either $(m-1, n-1)$ or $(m+1, n-1)$.
The $y$-coordinate decreases by 1 in each step. To go from $Y_0=2026$ to $Y_f=0$, the chip must take $k = Y_0 - Y_f = 2026 - 0 = 2026$ steps.

Let $N_R$ be the number of steps where the chip moves to the right (i.e., $x \to x+1$) and $N_L$ be the number of steps where the chip moves to the left (i.e., $x \to x-1$).
The total number of steps is $N_R + N_L = k = 2026$.
The net change in the $x$-coordinate is $N_R \cdot (+1) + N_L \cdot (-1) = N_R - N_L$.
This net change must be equal to $X_f - X_0 = 0 - 1234 = -1234$.

So we have a system of two linear equations:
1) $N_R + N_L = 2026$
2) $N_R - N_L = -1234$

Adding the two equations:
$2N_R = 2026 - 1234 = 792 \implies N_R = 396$.

Subtracting the second equation from the first:
$2N_L = 2026 - (-1234) = 2026 + 1234 = 3260 \implies N_L = 1630$.

We can check these values: $N_R + N_L = 396 + 1630 = 2026$ (correct) and $N_R - N_L = 396 - 1630 = -1234$ (correct).

The total number of distinct paths, $N$, is the number of ways to choose which $N_R$ of the $k$ steps are right moves. This is given by the binomial coefficient $\binom{k}{N_R}$.
$N = \binom{2026}{396}$.

We need to compute $N \pmod{1000}$. Since $1000 = 8 \cdot 125$, we can compute $N \pmod 8$ and $N \pmod{125}$ separately and then use the Chinese Remainder Theorem (CRT).

First, let's find the exponent of the highest power of 2 and 5 that divides $N$. This is denoted by $v_p(N)$.
Legendre's formula states that $v_p(n!) = \sum_{j=1}^{\infty} \lfloor n/p^j \rfloor$.
$v_p\left(\binom{n}{k}\right) = v_p(n!) - v_p(k!) - v_p((n-k)!)$.

For $p=5$:
$v_5(2026!) = \lfloor 2026/5 \rfloor + \lfloor 2026/25 \rfloor + \lfloor 2026/125 \rfloor + \lfloor 2026/625 \rfloor = 405 + 81 + 16 + 3 = 505$.
$v_5(396!) = \lfloor 396/5 \rfloor + \lfloor 396/25 \rfloor + \lfloor 396/125 \rfloor = 79 + 15 + 3 = 97$.
$v_5(1630!) = \lfloor 1630/5 \rfloor + \lfloor 1630/25 \rfloor + \lfloor 1630/125 \rfloor + \lfloor 1630/625 \rfloor = 326 + 65 + 13 + 2 = 406$.
$v_5(N) = 505 - 97 - 406 = 2$.
This means $N$ is divisible by $5^2=25$. So $N \equiv 0 \pmod{25}$.

For $p=2$:
$v_2(2026!) = \lfloor 2026/2 \rfloor + \lfloor 2026/4 \rfloor + \dots + \lfloor 2026/1024 \rfloor = 1013+506+253+126+63+31+15+7+3+1 = 2018$.
$v_2(396!) = 198+99+49+24+12+6+3+1 = 392$.
$v_2(1630!) = 815+407+203+101+50+25+12+6+3+1 = 1623$.
$v_2(N) = 2018 - 392 - 1623 = 3$.
This means $N$ is divisible by $2^3=8$. So $N \equiv 0 \pmod 8$.

Since $N \equiv 0 \pmod 8$ and $N \equiv 0 \pmod{25}$, $N$ must be a multiple of $\operatorname{lcm}(8, 25) = 200$.
Therefore, $N \pmod{1000}$ must be one of $0, 200, 400, 600, 800$.

Now we need to compute $N \pmod{125}$. Since $v_5(N)=2$, $N$ is divisible by $25$. So $N = 25M$ for some integer $M$. We want $N \pmod{125}$, which means we need to find $25M \pmod{125}$. This is $25 \cdot (M \pmod 5)$. So we need to compute $M \pmod 5$, where $M = N/25$.
We use the formula $\frac{1}{p^{v_p(\binom{n}{k})}} \binom{n}{k} \equiv \frac{\prod_{i=1, p \nmid i}^n i}{\left(\prod_{i=1, p \nmid i}^k i\right) \left(\prod_{i=1, p \nmid i}^{n-k} i\right)} \pmod p$.
Let $P_p(m) = \prod_{i=1, p \nmid i}^m i$. A useful property for this product modulo $p$ is $P_p(m) \equiv (-1)^{\lfloor m/p \rfloor} (m \pmod p)! \pmod p$.

For $n=2026$:
$P_5(2026) \equiv (-1)^{\lfloor 2026/5 \rfloor} (2026 \pmod 5)! \equiv (-1)^{405} (1)! \equiv -1 \cdot 1 = -1 \pmod 5$.

For $k=396$:
$P_5(396) \equiv (-1)^{\lfloor 396/5 \rfloor} (396 \pmod 5)! \equiv (-1)^{79} (1)! \equiv -1 \cdot 1 = -1 \pmod 5$.

For $n-k=1630$:
$P_5(1630) \equiv (-1)^{\lfloor 1630/5 \rfloor} (1630 \pmod 5)! \equiv (-1)^{326} (0)! \equiv 1 \cdot 1 = 1 \pmod 5$. (Recall $0!=1$)

Now, substitute these values into the formula for $M \pmod 5$:
$M \equiv \frac{P_5(2026)}{P_5(396) P_5(1630)} \pmod 5 \equiv \frac{-1}{(-1) \cdot 1} \pmod 5 \equiv \frac{-1}{-1} \pmod 5 \equiv 1 \pmod 5$.

So $N/25 \equiv 1 \pmod 5$.
This implies $N/25 = 5j+1$ for some integer $j$.
Then $N = 25(5j+1) = 125j + 25$.
Thus $N \equiv 25 \pmod{125}$.

We now have a system of congruences:
1) $N \equiv 0 \pmod 8$
2) $N \equiv 25 \pmod{125}$

From (1), $N = 8a$ for some integer $a$.
Substitute into (2):
$8a \equiv 25 \pmod{125}$.
To solve for $a$, we need the modular inverse of $8 \pmod{125}$. We can find this using the Extended Euclidean Algorithm:
$125 = 15 \cdot 8 + 5$
$8 = 1 \cdot 5 + 3$
$5 = 1 \cdot 3 + 2$
$3 = 1 \cdot 2 + 1$
Now, express $1$ as a linear combination of $8$ and $125$:
$1 = 3 - 2$
$1 = 3 - (5 - 3) = 2 \cdot 3 - 5$
$1 = 2 \cdot (8 - 5) - 5 = 2 \cdot 8 - 3 \cdot 5$
$1 = 2 \cdot 8 - 3 \cdot (125 - 15 \cdot 8) = 2 \cdot 8 - 3 \cdot 125 + 45 \cdot 8$
$1 = 47 \cdot 8 - 3 \cdot 125$.
So $47 \cdot 8 \equiv 1 \pmod{125}$. The inverse of $8$ is $47$.

Multiply $8a \equiv 25 \pmod{125}$ by $47$:
$47 \cdot 8a \equiv 47 \cdot 25 \pmod{125}$
$a \equiv 1175 \pmod{125}$.
To reduce $1175 \pmod{125}$: $1175 = 9 \cdot 125 + 50$.
$1175 = 1125 + 50$. So $a \equiv 50 \pmod{125}$.

Now substitute $a=50$ (or $a=125j+50$) back into $N=8a$:
$N = 8 \cdot 50 = 400$.
So $N \equiv 400 \pmod{1000}$.

The final answer is $\boxed{400}$.
