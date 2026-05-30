Let the starting position be $(X_0, Y_0) = (1234, 2026)$.
The chip moves from $(m, n)$ to either $(m-1, n-1)$ or $(m+1, n-1)$.
The target position is $(0,0)$.

Let $k$ be the number of steps taken. Each step decreases the y-coordinate by 1.
To reach $y=0$ from $y=Y_0$, the chip must take $Y_0$ steps. So, the total number of steps is $K = Y_0 = 2026$.

Let $k_L$ be the number of steps where the x-coordinate decreases by 1 (move to $(m-1, n-1)$).
Let $k_R$ be the number of steps where the x-coordinate increases by 1 (move to $(m+1, n-1)$).

The total number of steps is $k_L + k_R = K = 2026$.

The change in the x-coordinate is $k_R \cdot (+1) + k_L \cdot (-1)$.
The final x-coordinate is $X_0 + k_R - k_L = 0$.
So, $1234 + k_R - k_L = 0$, which means $k_L - k_R = 1234$.

We have a system of two linear equations:
1) $k_L + k_R = 2026$
2) $k_L - k_R = 1234$

Adding the two equations: $2k_L = 2026 + 1234 = 3260 \implies k_L = 1630$.
Subtracting the second equation from the first: $2k_R = 2026 - 1234 = 792 \implies k_R = 396$.

The total number of distinct paths, $N$, is the number of ways to choose $k_L$ 'L' steps (or $k_R$ 'R' steps) out of $K$ total steps. This is given by the binomial coefficient:
$N = \binom{K}{k_L} = \binom{2026}{1630}$.
Alternatively, $N = \binom{K}{k_R} = \binom{2026}{396}$.
Since $\binom{n}{k} = \binom{n}{n-k}$, both are equal: $2026 - 1630 = 396$.
We will compute $N = \binom{2026}{396}$.

We need to compute $N \pmod{1000}$. Since $1000 = 8 \times 125 = 2^3 \times 5^3$, we will compute $N \pmod 8$ and $N \pmod{125}$ separately, and then use the Chinese Remainder Theorem.

1.  **Compute $N \pmod 8$**:
    We need to find the exponent of the highest power of 2 that divides $N$, denoted as $v_2(N)$. We use Legendre's formula: $v_p(n!) = \sum_{i=1}^{\infty} \lfloor n/p^i \rfloor$.
    $v_2(N) = v_2(2026!) - v_2(396!) - v_2(1630!)$.

    $v_2(2026!) = \lfloor 2026/2 \rfloor + \lfloor 2026/4 \rfloor + \dots = 1013 + 506 + 253 + 126 + 63 + 31 + 15 + 7 + 3 + 1 = 2018$.
    $v_2(396!) = \lfloor 396/2 \rfloor + \lfloor 396/4 \rfloor + \dots = 198 + 99 + 49 + 24 + 12 + 6 + 3 + 1 = 392$.
    $v_2(1630!) = \lfloor 1630/2 \rfloor + \lfloor 1630/4 \rfloor + \dots = 815 + 407 + 203 + 101 + 50 + 25 + 12 + 6 + 3 + 1 = 1623$.

    $v_2(N) = 2018 - 392 - 1623 = 2018 - (392+1623) = 2018 - 2015 = 3$.
    Since $v_2(N)=3$, $N$ is divisible by $2^3=8$.
    Therefore, $N \equiv 0 \pmod 8$.

2.  **Compute $N \pmod{125}$**:
    First, find $v_5(N)$:
    $v_5(2026!) = \lfloor 2026/5 \rfloor + \lfloor 2026/25 \rfloor + \lfloor 2026/125 \rfloor + \lfloor 2026/625 \rfloor = 405 + 81 + 16 + 3 = 505$.
    $v_5(396!) = \lfloor 396/5 \rfloor + \lfloor 396/25 \rfloor + \lfloor 396/125 \rfloor = 79 + 15 + 3 = 97$.
    $v_5(1630!) = \lfloor 1630/5 \rfloor + \lfloor 1630/25 \rfloor + \lfloor 1630/125 \rfloor + \lfloor 1630/625 \rfloor = 326 + 65 + 13 + 2 = 406$.

    $v_5(N) = 505 - 97 - 406 = 505 - (97+406) = 505 - 503 = 2$.
    Since $v_5(N)=2$, $N$ is divisible by $5^2=25$, but not by $5^3=125$.
    This means $N$ can be written as $N = 25 \cdot M$, where $M$ is not divisible by 5.
    To find $N \pmod{125}$, we need to find $M \pmod 5$.
    We use the generalization of Lucas's Theorem for $p$-adic valuations of $n!$.
    Let $n!_p = n! / p^{v_p(n!)}$. Then $\binom{n}{k} = \frac{n!_p}{k!_p (n-k)!_p} p^{v_p(\binom{n}{k})}$.
    So, $M \equiv \frac{2026!_5}{396!_5 1630!_5} \pmod 5$.
    For $n!_p \pmod p$, the formula is $n!_p \equiv (-1)^{\lfloor n/p \rfloor} \prod_{i=0}^s n_i! \pmod p$, where $n = (n_s n_{s-1} \dots n_1 n_0)_p$.

    For $n=2026, p=5$: $2026 = 3 \cdot 5^4 + 1 \cdot 5^3 + 0 \cdot 5^2 + 0 \cdot 5^1 + 1 \cdot 5^0 = (31001)_5$.
    $\lfloor 2026/5 \rfloor = 405$.
    $2026!_5 \equiv (-1)^{405} (1! \cdot 0! \cdot 0! \cdot 1! \cdot 3!) \pmod 5 \equiv (-1) (1 \cdot 1 \cdot 1 \cdot 1 \cdot 6) \equiv -6 \equiv -1 \pmod 5$.

    For $k=396, p=5$: $396 = 3 \cdot 5^3 + 0 \cdot 5^2 + 4 \cdot 5^1 + 1 \cdot 5^0 = (3041)_5$.
    $\lfloor 396/5 \rfloor = 79$.
    $396!_5 \equiv (-1)^{79} (1! \cdot 4! \cdot 0! \cdot 3!) \pmod 5 \equiv (-1) (1 \cdot 24 \cdot 1 \cdot 6) \equiv -(1 \cdot 4 \cdot 1 \cdot 1) \equiv -4 \equiv 1 \pmod 5$.

    For $n-k=1630, p=5$: $1630 = 2 \cdot 5^4 + 3 \cdot 5^3 + 0 \cdot 5^2 + 2 \cdot 5^1 + 0 \cdot 5^0 = (23020)_5$.
    $\lfloor 1630/5 \rfloor = 326$.
    $1630!_5 \equiv (-1)^{326} (0! \cdot 2! \cdot 0! \cdot 3! \cdot 2!) \pmod 5 \equiv (1) (1 \cdot 2 \cdot 1 \cdot 6 \cdot 2) \equiv (1 \cdot 2 \cdot 1 \cdot 1 \cdot 2) \equiv 4 \pmod 5$.

    Now compute $M \pmod 5$:
    $M \equiv \frac{-1}{(1)(4)} \pmod 5 \equiv \frac{-1}{4} \pmod 5$.
    Since $4 \equiv -1 \pmod 5$, $M \equiv \frac{-1}{-1} \equiv 1 \pmod 5$.
    So $N = 25 \cdot M \equiv 25 \cdot 1 \pmod{125}$.
    Therefore, $N \equiv 25 \pmod{125}$.

3.  **Combine using Chinese Remainder Theorem**:
    We have the system of congruences:
    $N \equiv 0 \pmod 8$
    $N \equiv 25 \pmod{125}$

    From the second congruence, $N = 125k + 25$ for some integer $k$.
    Substitute this into the first congruence:
    $125k + 25 \equiv 0 \pmod 8$.
    $125 \equiv 5 \pmod 8$ and $25 \equiv 1 \pmod 8$.
    So, $5k + 1 \equiv 0 \pmod 8$.
    $5k \equiv -1 \pmod 8$.
    $5k \equiv 7 \pmod 8$.
    To find $k$, multiply by the inverse of $5 \pmod 8$. Since $5 \times 5 = 25 \equiv 1 \pmod 8$, the inverse of $5 \pmod 8$ is $5$.
    $k \equiv 7 \times 5 \pmod 8$.
    $k \equiv 35 \pmod 8$.
    $k \equiv 3 \pmod 8$.

    Substitute $k=3$ into $N = 125k + 25$:
    $N = 125(3) + 25 = 375 + 25 = 400$.

    This value satisfies both congruences: $400 \equiv 0 \pmod 8$ and $400 = 3 \times 125 + 25 \equiv 25 \pmod{125}$.
    So, $N \equiv 400 \pmod{1000}$.

The final answer is $\boxed{400}$.
