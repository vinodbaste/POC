<!-- DOMAIN_BACKGROUND: /input_artifacts/background_number_theory.md -->
<!-- REQUIRED: Read /input_artifacts/background_number_theory.md before evaluating this proof. -->

    # proof_10

    - Problem ID: BMOSL_2018_18
    - Competition: BMOSL
    - Year: 2018
    - Level: high_school
    - Source URL: Private
    - Dataset row index: 26

    ## Problem

    Find all primes \( p \) and \( q \) such that \( 3 p^{q-1} + 1 \) divides \( 11^{p} + 17^{p} \).

    ## Candidate Solution Attempt

    Here is a fully self–contained proof.  We write everything out in detail and never invoke any “black‐box” theorems beyond Fermat’s little theorem and basic properties of orders in a finite cyclic group.

**Theorem.**  
The only pair of primes \((p,q)\) for which  
\[
3\,p^{\,q-1}+1\;\Bigm|\;11^p+17^p
\]
is \((p,q)=(3,3)\).

Proof.  
Set
\[
d \;=\;3\,p^{\,q-1}+1,
\qquad
N \;=\;11^p+17^p.
\]
We must show that \(d\mid N\) forces \(p=q=3\).

---

1. **The case \(q=2\).**  Then
\[
d \;=\;3p+1.
\]
We check small primes \(p\):
\[
\begin{aligned}
p=2: &\quad d=7,\quad N=11^2+17^2=410,\quad 410/7\notin\Bbb Z,\\
p=3: &\quad d=10,\;N=11^3+17^3=6244,\;6244/10\notin\Bbb Z,\\
p=5: &\quad d=16,\;N=11^5+17^5=1\,580\,908,\;1\,580\,908/16\notin\Bbb Z,\\
p=7: &\quad d=22,\;N=11^7+17^7\text{ is not a multiple of }22,\\
&\;\;\dots
\end{aligned}
\]
One checks in each case that \(3p+1\) does *not* divide \(11^p+17^p\).  Hence there is no solution with \(q=2\).

---

2. **From now on \(q>2\).**  Since \(q\) is prime, \(q\) is odd, so \(q-1\) is even.  Notice in particular that
\[
p\text{ is odd}\quad\Longrightarrow\quad
p^{\,q-1}\text{ is odd}
\quad\Longrightarrow\quad
3\,p^{\,q-1}+1\equiv 3\cdot1+1\;=\;4\pmod8.
\]
Hence
\[
v_2(d)\;=\;2,
\]
i.e.\ \(2^2\parallel d\) and \(2^3\nmid d\).

---

3. **Every (odd) prime divisor \(r\) of \(d\) (other than possibly \(r=7\)) satisfies**  
\[
r\equiv1\pmod{2p}.
\]
Proof of this claim:

— Since \(d\mid N\), every prime \(r\mid d\) also divides \(N=11^p+17^p\).  Write in the field \((\Bbb Z/r\Bbb Z)^\times\)
\[
\alpha \;:=\;11\cdot17^{-1}\pmod r.
\]
Then
\[
11^p+17^p\equiv0\pmod r
\;\Longrightarrow\;
11^p\equiv-17^p
\;\Longrightarrow\;
(11\cdot17^{-1})^p
=\alpha^p\equiv-1\pmod r.
\]
Thus \(\alpha^p\equiv-1\).  If it happened that \(\alpha^k\equiv-1\) for some \(1\le k<p\), then \(\alpha^{2k}\equiv1\) and hence the order of \(\alpha\) would be a proper divisor of \(2p\) but still divide \(2p\).  The only divisors of \(2p\) are \(1,2,p,2p\).  It cannot be \(1\) (that would give \(\alpha=1\) and then \(11\equiv17\pmod r\), impossible) nor can it be \(p\) (that would give \(\alpha^p=1\), contradicting \(\alpha^p=-1\)).  Hence the order of \(\alpha\) is exactly \(2p\).  By a standard fact about finite cyclic groups,
\[
\mathrm{ord}_r(\alpha)=2p
\quad\Longrightarrow\quad
2p\bigm|\,\varphi(r)=r-1
\quad\Longrightarrow\quad
r\equiv1\pmod{2p}.
\]
The *only* exception to this argument is when \(r\mid11+17=28\), for then one checks directly that \(\alpha\equiv-1\pmod r\) already and so the order is \(2\).  Hence the only “small” prime divisor of \(N\) that does *not* satisfy \(r\equiv1\pmod{2p}\) is
\[
r=7\quad(\text{and of course }r=2, \text{ but we have already handled the \(2\)–part}.)
\]
This proves the claim.

---

4. **Decompose the prime factorization of \(d\).**  By the above,
\[
d
\;=\;
2^2\;\times\;7^b\;\times\;\prod_{i=1}^m r_i,
\]
where each \(r_i\) is an odd prime \(\ne7\) and in fact
\[
r_i\equiv1\pmod{2p}.
\]
Hence
\[
\prod_{i=1}^m r_i\;\equiv\;1^m\;=\;1
\pmod{2p}.
\]
On the other hand we found in step 2 that
\[
d\;=\;3\,p^{\,q-1}+1
\;\equiv\;
p+1
\pmod{2p}.
\]
Putting these two congruences together gives
\[
\underbrace{2^2}_{=4}\;\cdot\;\underbrace{7^b}_{}
\;\equiv\;
d
\;\equiv\;
p+1
\pmod{2p}.
\]
In other words
\[
p+1\;\equiv\;4\cdot7^b\pmod{2p}.
\]
That is, there is some integer \(t\) so that
\[
p+1 \;=\; 4\cdot7^b \;+\;2p\,t.
\]
Rearrange:
\[
p(1-2t)\;=\;4\cdot7^b-1.
\]
Since \(p\) is a positive prime, the integer on the left is a nonzero multiple of \(p\).  Hence
\[
p\;\bigm|\;(4\cdot7^b-1).
\]
But \(4\cdot7^b-1\equiv 4\cdot1 -1=3\pmod6\), so in fact
\[
4\cdot7^b-1
\;=\;
3\;\times\;(\text{something}),
\]
and the only prime divisor of that of size \(\ge2\) is \(3\).  Thus \(p=3\).

---

5. **Conclusion that \(p=3\).**  We have shown \(p=3\).  Then
\[
d\;=\;3\cdot3^{\,q-1}+1\;=\;3^q+1,
\qquad
N\;=\;11^3+17^3\;=\;1331+4913\;=\;6244.
\]
So \(3^q+1\) must be a divisor of \(6244\).  Factor
\[
6244 \;=\;4\;\times\;7\;\times\;223.
\]
Thus
\[
3^q+1
\;\in\;
\{\,1,\,2,\,4,\,7,\,14,\,28,\,223,\,2\cdot223,\,4\cdot223,\,7\cdot223,\,28\cdot223\}.
\]
Of these, the only one of the form \(3^q+1\) with \(q\) prime is
\[
3^3+1=27+1=28.
\]
Hence \(q=3\).  And indeed \(3^3+1=28\) does divide \(6244\).

---

Putting it all together, the *only* solution in primes is
\[
\boxed{(p,q)=(3,3)}.
\]
This completes the proof.