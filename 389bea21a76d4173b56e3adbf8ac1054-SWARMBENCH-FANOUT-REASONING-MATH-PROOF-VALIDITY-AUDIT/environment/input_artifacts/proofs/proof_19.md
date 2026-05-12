<!-- DOMAIN_BACKGROUND: /input_artifacts/background_combinatorics.md -->
<!-- REQUIRED: Read /input_artifacts/background_combinatorics.md before evaluating this proof. -->

    # proof_19

    - Problem ID: USAMO_2006_2
    - Competition: USAMO
    - Year: 2006
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 79

    ## Problem

    Let \( k > 0 \) be a fixed integer. Compute the minimum integer \( N \) (in terms of \( k \)) for which there exists a set of \( 2k+1 \) distinct positive integers that has a sum greater than \( N \), but for which every subset of size \( k \) has a sum at most \( N/2 \).

    ## Candidate Solution Attempt

    Proof.  Fix an integer \(k\ge1\).  We will show that the least integer \(N\) with the desired property is
\[
  N \;=\;2k^3+3k^2+3k \;=\;k\,(2k^2+3k+3)\,.
\]
Our proof has two parts: (i) for this value of \(N\) one can exhibit a suitable set of \(2k+1\) distinct positive integers, and (ii) no smaller \(N\) can work.

1.  Construction for \(N=2k^3+3k^2+3k\).

Let
\[
   c \;=\;k(k+1)+1,
\]
and consider the set
\[
   S \;=\;\{\,c-k,\;c-k+1,\;\dots,\;c-1,\;c,\;c+1,\;\dots,\;c+k\}.
\]
Since there are \((c+k)-(c-k)+1=2k+1\) integers here, \(|S|=2k+1\), and they are clearly distinct and positive.  We claim that with
\[
   N \;=\;2k^3+3k^2+3k
   \;=\;2\sum_{j=1}^k\bigl(c+j\bigr),
\]
this set \(S\) satisfies
(a) every \(k\)-element subset of \(S\) has sum \(\le N/2\), and
(b) the total sum of \(S\) is \(>N\).

Let us index the elements in increasing order:
\[
   a_i \;=\; c-k-1+i,
   \qquad i=1,2,\dots,2k+1,
\]
so \(a_1=c-k,a_2=c-k+1,\dots,a_{2k+1}=c+k\).  Then the largest \(k\) of them are
\[
   a_{k+2},a_{k+3},\dots,a_{2k+1}
   \;=\;
   c+1,\;c+2,\;\dots,\;c+k,
\]
and
\[
   \sum_{i=k+2}^{2k+1}a_i
   \;=\;\sum_{j=1}^k(c+j)
   \;=\;kc \;+\;\frac{k(k+1)}2
   \;=\;\frac N2.
\]
Hence the maximum sum of any \(k\)-subset of \(S\) is \(\sum_{i=k+2}^{2k+1}a_i = N/2\), so every \(k\)-subset has sum \(\le N/2\).  

On the other hand, the complement of that \(k\)-subset has size \(k+1\) and sum
\[
   \sum_{i=1}^{k+1}a_i
   \;=\;\sum_{j=0}^k\bigl(c-j\bigr)
   \;=\;(k+1)c \;-\;\frac{k(k+1)}2.
\]
A direct calculation shows
\[
   \sum_{i=1}^{k+1}a_i
   \;-\;\sum_{i=k+2}^{2k+1}a_i
   \;=\;1,
\]
so
\[
   \sum_{i=1}^{2k+1}a_i
   \;=\;
   \sum_{i=1}^{k+1}a_i \;+\;\sum_{i=k+2}^{2k+1}a_i
   \;=\;\frac N2+\Bigl(\frac N2+1\Bigr)
   \;=\;N+1
   \;>\;N.
\]
Thus \(S\) has total sum \(N+1\), while every \(k\)-subset has sum \(\le N/2\).  This proves existence of a suitable set when \(N=2k^3+3k^2+3k\).

2.  Minimality: no smaller \(N\) can work.

Suppose for some integer \(N'\) there is a set of \(2k+1\) distinct positive integers
\[
   a_1<a_2<\cdots<a_{2k+1}
\]
with
(i) every \(k\)-subset summing to at most \(N'/2\), and
(ii) total sum \(\sum_{i=1}^{2k+1}a_i > N'\).

Because among all \(k\)-subsets the one of largest sum is
\(\{a_{k+2},\dots,a_{2k+1}\}\), condition (i) gives
\[
   S_k \;:=\;\sum_{i=k+2}^{2k+1}a_i
   \;\le\; \frac{N'}2
   \quad\Longrightarrow\quad
   N'\;\ge\;2\,S_k.
\]
Meanwhile
\[
   \sum_{i=1}^{k+1}a_i
   \;=\;\sum_{i=1}^{2k+1}a_i \;-\;S_k
   \;>\;N' \;-\;S_k
   \;\ge\;2S_k -S_k
   \;=\;S_k,
\]
so
\[
   \sum_{i=1}^{k+1}a_i
   \;>\;
   \sum_{i=k+2}^{2k+1}a_i.
\]
We now bound \(S_k\) below in terms of \(k\).  Set
\(\;c = a_{k+1}.\)  Since the \(a_i\) are strictly increasing integers,
for \(1\le i\le k\) we have
\[
   a_i \;\le\; c-1,\;c-2,\;\dots,\;c-k
   \quad\Longrightarrow\quad
   \sum_{i=1}^k a_i
   \;\le\;
   (c-1)+(c-2)+\cdots+(c-k)
   \;=\;kc\;-\;\frac{k(k+1)}2.
\]
Also for \(1\le j\le k\),
\[
   a_{k+1+j}\;\ge\;c+j,
\]
so
\[
   S_k \;=\;\sum_{i=k+2}^{2k+1}a_i
   \;\ge\;\sum_{j=1}^k(c+j)
   \;=\;kc\;+\;\frac{k(k+1)}2.
\]
The strict inequality
\(\sum_{i=1}^{k+1}a_i > S_k\)
becomes
\[
   \Bigl(\sum_{i=1}^k a_i\Bigr)+c
   \;>\;
   \Bigl(kc + \tfrac{k(k+1)}2\Bigr),
\]
so
\[
   \sum_{i=1}^k a_i
   \;>\;
   (k-1)c \;+\;\frac{k(k+1)}2.
\]
Combining with the upper bound
\(\sum_{i=1}^k a_i \le kc - \tfrac{k(k+1)}2\)
yields
\[
   kc - \frac{k(k+1)}2
   \;>\;
   (k-1)c + \frac{k(k+1)}2
   \;\Longrightarrow\;
   c \;>\; k(k+1).
\]
Since \(c\) is an integer, \(c\ge k(k+1)+1\).  Hence
\[
   S_k \;\ge\; kc + \frac{k(k+1)}2
   \;\ge\;
   k\bigl(k(k+1)+1\bigr)\;+\;\frac{k(k+1)}2
   \;=\;\frac{2k^3+3k^2+3k}2.
\]
Therefore
\[
   N' \;\ge\;2\,S_k
   \;\ge\;2\cdot\frac{2k^3+3k^2+3k}2
   \;=\;2k^3+3k^2+3k.
\]
This shows no integer \(N'<2k^3+3k^2+3k\) can admit a valid set of size \(2k+1\).  Together with the construction in part 1, we conclude that the minimal such \(N\) is
\[
   \boxed{\,2k^3+3k^2+3k\,}
   \;=\;
   \boxed{\,k(2k^2+3k+3)\,}.
\]  ∎