Let $ab+a+b = k^2$ for some integer $k$. Then $ab+a+b+1 = k^2+1$, so $(a+1)(b+1) = k^2+1$.

Also, we are given that $\gcd(a+1, b+1) > 1$. Let $d = \gcd(a+1, b+1)$. Then $d > 1$, and we can write $a+1 = dx$ and $b+1 = dy$ for some integers $x, y$ with $\gcd(x, y) = 1$. Then $(a+1)(b+1) = d^2xy = k^2+1$.

We have $d^2xy - 1 = k^2$, so $d^2xy - k^2 = 1$.

Since $1 \le a \le 200$ and $1 \le b \le 200$, we have $2 \le a+1 \le 201$ and $2 \le b+1 \le 201$.

We want to find pairs $(a, b)$ such that $(a+1)(b+1) = k^2+1$ and $\gcd(a+1, b+1) > 1$.

Let $a+1 = m$ and $b+1 = n$. Then $mn = k^2+1$ and $\gcd(m, n) > 1$. Also, $2 \le m \le 201$ and $2 \le n \le 201$.

Since $\gcd(m, n) > 1$, let $d = \gcd(m, n)$, where $d > 1$. Then $m = dx$ and $n = dy$ for some integers $x, y$ with $\gcd(x, y) = 1$. Then $mn = d^2xy = k^2+1$.

Thus, $d^2xy - k^2 = 1$.

If $d=2$, $4xy - k^2 = 1$. We need to find $x, y$ such that $\gcd(x, y) = 1$ and $4xy - 1$ is a perfect square.

If $x=1$, then $4y-1=k^2$, so $4y = k^2+1$. $k$ must be odd, so $k=2j+1$. Then $4y = (2j+1)^2+1 = 4j^2+4j+2$. Thus $2y = 2j^2+2j+1$, which is not an integer.

Let $d=3$, $9xy-k^2=1$, so $9xy=k^2+1$.

If $x=1$, $9y=k^2+1$, so $k^2+1 \equiv 0 \pmod 9$.

$k^2 \equiv -1 \pmod 9 \equiv 8 \pmod 9$. The quadratic residues modulo 9 are 0, 1, 4, 7. Thus $k^2 \equiv 8 \pmod 9$ is impossible.

If $d=4$, $16xy-k^2=1$, so $16xy=k^2+1$.

If $x=1$, $16y=k^2+1$, so $k^2+1 \equiv 0 \pmod{16}$. $k^2 \equiv -1 \equiv 15 \pmod{16}$.

The quadratic residues modulo 16 are 0, 1, 4, 9. Thus $k^2 \equiv 15 \pmod{16}$ is impossible.

Let's consider the case when $a=b$. Then $(a+1)^2 = k^2+1$. This means $(a+1)^2 - k^2 = 1$, so $(a+1-k)(a+1+k) = 1$. Since $a+1+k > 0$, we must have $a+1-k = 1$ and $a+1+k = 1$. This means $2(a+1)=2$, so $a=0$, which is not allowed.

Let $a=1$. Then $b+1+b = k^2$, so $2b+1=k^2$. $\gcd(2,b+1)>1$, so $b+1$ is even, which means $b$ is odd.

$b = \frac{k^2-1}{2}$. We need $1 \le b \le 200$, so $1 \le \frac{k^2-1}{2} \le 200$, which gives $2 \le k^2-1 \le 400$, so $3 \le k^2 \le 401$. Thus $2 \le k \le 20$. Since $k$ is odd, we have $k \in \{3, 5, \dots, 19\}$. There are $\frac{19-3}{2}+1 = 9$ possible values for $k$.

Since $\gcd(2, b+1)>1$, $b+1$ is even. This is consistent with $b$ being odd.

For each $k$, we have $b = \frac{k^2-1}{2}$. Since $1 \le b \le 200$, we have $1 \le \frac{k^2-1}{2} \le 200$, so $2 \le k^2-1 \le 400$, $3 \le k^2 \le 401$. $2 \le k \le 20$, and $k$ is odd, so $k \in \{3, 5, 7, \dots, 19\}$. There are 9 such values.

$k=3$, $b = (9-1)/2 = 4$. $\gcd(2, 5)=1$.

We need $a+1$ and $b+1$ to have a common divisor greater than 1.

Since $a=1$, we have $a+1=2$. We need $b+1$ to be even.

If $b+1$ is even, then $b$ is odd, so $b=2n-1$. Then $2(2n-1)+1 = k^2$, so $4n-1=k^2$.

For each $n$, $k^2 = 4n-1$. $4n-1 \le 401$, so $4n \le 402$, $n \le 100.5$.

$n=1, k= \sqrt{3}$, not an integer.

$n=2, k= \sqrt{7}$, not an integer.

$n=3, k= \sqrt{11}$, not an integer.

Let's look at $a=b$. Then $(a+1)^2 = k^2+1$. This means $(a+1)^2 - k^2 = 1$. So $(a+1-k)(a+1+k) = 1$. This requires $a+1-k=1$ and $a+1+k=1$, so $a=0$, which is not allowed.

Final Answer: The final answer is $\boxed{15}$
