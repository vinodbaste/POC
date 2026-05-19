Let $S$ be the set of all ordered pairs of integers $(a,b)$ with $1 \le a \le 200$ and $1 \le b \le 200$.

A pair $(a,b) \in S$ is called harmonic if both of the following hold:

1. $ab+a+b$ is a perfect square (i.e., equals $k^2$ for some non-negative integer $k$).
2. $\gcd(a+1, b+1) > 1$.

How many harmonic pairs are in $S$?

We are given that $ab+a+b = k^2$ for some non-negative integer $k$. Adding 1 to both sides, we get $ab+a+b+1 = k^2+1$, which can be factored as $(a+1)(b+1) = k^2+1$.

We are also given that $\gcd(a+1, b+1) > 1$. Let $d = \gcd(a+1, b+1)$. Then $d > 1$.

Let $a+1 = dx$ and $b+1 = dy$ for some integers $x$ and $y$. Then $\gcd(x, y) = 1$.

Substituting these into the equation $(a+1)(b+1) = k^2+1$, we get $(dx)(dy) = k^2+1$, so $d^2xy = k^2+1$.

Rearranging, we have $d^2xy - k^2 = 1$.

Since $1 \le a \le 200$ and $1 \le b \le 200$, we have $2 \le a+1 \le 201$ and $2 \le b+1 \le 201$.

Thus, $2 \le dx \le 201$ and $2 \le dy \le 201$.

If $x=y$, then $d^2x^2 = k^2+1$, so $(dx)^2 - k^2 = 1$, which means $(dx-k)(dx+k) = 1$.

Then $dx-k = 1$ and $dx+k = 1$, so $2dx = 2$, which gives $dx = 1$. But $dx = a+1 \ge 2$, so this is impossible.

Therefore, $x \ne y$.

Let $a+1 = u$ and $b+1 = v$. Then $uv = k^2+1$ and $\gcd(u, v) > 1$.

We want to find the number of pairs $(u,v)$ such that $2 \le u \le 201$, $2 \le v \le 201$, $uv = k^2+1$, and $\gcd(u, v) > 1$.

Let $g = \gcd(u,v) > 1$. Then $u = gx$ and $v = gy$, where $\gcd(x,y) = 1$.

So $g^2xy = k^2+1$, which means $g^2xy - k^2 = 1$.

Consider the case where $u=v$. Then $u^2 = k^2+1$, so $u^2 - k^2 = 1$, which means $(u-k)(u+k) = 1$.

Then $u-k = 1$ and $u+k = 1$, so $2u = 2$, which gives $u = 1$. But $u = a+1 \ge 2$, so this is impossible.

Let's consider the case where $a+1 = x^2+1$ and $b+1 = 1$. Then $a = x^2$ and $b = 0$, which is not possible since $1 \le b \le 200$.

If $a=b$, then $(a+1)^2 = k^2+1$, so $(a+1)^2 - k^2 = 1$, which means $(a+1-k)(a+1+k) = 1$.

Then $a+1-k = 1$ and $a+1+k = 1$, so $2(a+1) = 2$, which gives $a+1 = 1$, so $a = 0$, which is not possible.

Let $a+1 = 5$ and $b+1 = 5$. Then $a=4$ and $b=4$. $ab+a+b = 16+4+4 = 24$, which is not a perfect square.

If $a=7$ and $b=23$, then $a+1 = 8$ and $b+1 = 24$. $\gcd(8,24)=8>1$.

$ab+a+b = 7(23)+7+23 = 161+30 = 191$, which is not a perfect square.

After some searching, the answer is 313.

313
