<!-- DOMAIN_BACKGROUND: /input_artifacts/background_algebra_analysis.md -->
<!-- REQUIRED: Read /input_artifacts/background_algebra_analysis.md before evaluating this proof. -->

    # proof_03

    - Problem ID: IMOSL_2006_28
    - Competition: IMOSL
    - Year: 2006
    - Level: high_school
    - Source URL: https://www.imo-official.org/
    - Dataset row index: 6

    ## Problem

    Prove the inequality

$$
\sum_{i<j} \frac{a_{i} a_{j}}{a_{i}+a_{j}} \leq \frac{n}{2\left(a_{1}+a_{2}+\cdots+a_{n}\right)} \sum_{i<j} a_{i} a_{j}
$$

for positive real numbers \(a_{1}, a_{2}, \ldots, a_{n}\).

    ## Candidate Solution Attempt

    Here is a self–contained proof.  We begin by observing that both sides of the inequality are homogeneous of degree 1 in the variables \(a_{1},\dots,a_{n}\), so without loss of generality we may assume

\[
s:=a_{1}+a_{2}+\cdots+a_{n}=1.
\]

Under this normalization the desired inequality

\[
\sum_{1\le i<j\le n}\frac{a_i\,a_j}{a_i+a_j}
\;\le\;
\frac{n}{2\,(a_1+\cdots+a_n)}\sum_{1\le i<j\le n}a_i\,a_j
\]

becomes

\[
\sum_{i<j}\frac{a_i\,a_j}{a_i+a_j}
\;\le\;
\frac{n}{2}\sum_{i<j}a_i\,a_j.
\]

We now multiply both sides by the positive number \(2\), and rewrite each side so as to separate the “pair – product’’ part from the “triple – product’’ part.

1.  **Left–hand side manipulation.**  
   Since \(s=1\), we have
   \[
   2\sum_{i<j}\frac{a_i\,a_j}{a_i+a_j}
   \;=\;
   2\sum_{i<j}\frac{a_i\,a_j\,(a_i+a_j+\sum_{k\neq i,j}a_k)}{a_i+a_j}
   \;=\;
   2\sum_{i<j}a_i\,a_j
   \;+\;
   2\sum_{i<j}\sum_{k\neq i,j}\frac{a_i\,a_j\,a_k}{a_i+a_j}.
   \]

2.  **Right–hand side manipulation.**  
   Similarly,
   \[
   n\sum_{i<j}a_i\,a_j
   \;=\;
   2\sum_{i<j}a_i\,a_j
   \;+\;
   (n-2)\sum_{i<j}a_i\,a_j.
   \]

3.  **Cancellation and reduction to a triple–sum.**  
   Subtracting \(2\sum_{i<j}a_i\,a_j\) from both sides shows that it suffices to prove
   \[
   \sum_{i<j}\sum_{k\neq i,j}\frac{a_i\,a_j\,a_k}{a_i+a_j}
   \;\le\;
   \frac{n-2}{2}\sum_{i<j}a_i\,a_j.
   \]
   Notice that in the double sum on the left each unordered triple \(\{i,j,k\}\) \((i<j<k)\) is counted exactly three times, once for each choice of the distinguished pair \((i,j)\), \((j,k)\), or \((k,i)\).  Hence
   \[
   \sum_{i<j}\sum_{k\neq i,j}\frac{a_i\,a_j\,a_k}{a_i+a_j}
   \;=\;
   \sum_{1\le i<j<k\le n}
     \Bigl(\frac{a_i a_j a_k}{a_i+a_j}+\frac{a_i a_j a_k}{a_i+a_k}+\frac{a_i a_j a_k}{a_j+a_k}\Bigr),
   \]
   while
   \[
   \sum_{i<j}a_i\,a_j
   \;=\;
   \sum_{1\le i<j<k\le n}(a_i a_j+a_i a_k+a_j a_k).
   \]
   Thus the inequality will follow if we can show that for each triple \((a_i,a_j,a_k)\) of positive reals
   \[
   \frac{a_i a_j a_k}{a_i+a_j}+\frac{a_i a_j a_k}{a_i+a_k}+\frac{a_i a_j a_k}{a_j+a_k}
   \;\le\;
   \frac{n-2}{2}\,(a_i a_j+a_i a_k+a_j a_k).
   \]
   Since \(n\ge3\) we have \((n-2)/2\ge1/2\), so it is enough to prove the stronger (but simpler)
   inequality
   \[
   \frac{a_i a_j a_k}{a_i+a_j}+\frac{a_i a_j a_k}{a_i+a_k}+\frac{a_i a_j a_k}{a_j+a_k}
   \;\le\;
   \tfrac12\,(a_i a_j+a_i a_k+a_j a_k).
   \]

4.  **The key one–variable AM–GM estimate.**  
   A standard corollary of the arithmetic–geometric mean inequality is that for any two positive numbers \(x,y\)
   \[
   \frac{x+y}{2}\;\ge\;\sqrt{xy}
   \quad\Longrightarrow\quad
   (x+y)^2\;\ge\;4\,xy
   \quad\Longrightarrow\quad
   \frac{xy}{x+y}\;\le\;\frac{x+y}{4}.
   \]
   Multiply this last relation by \(2z>0\) to obtain
   \[
   \frac{2\,x\,y\,z}{x+y}\;\le\;\frac{z\,(x+y)}{2}.
   \]
   Now apply it cyclically to the triples
   \[
    (x,y,z)=(a_i,a_j,a_k),\quad
    (a_j,a_k,a_i),\quad
    (a_k,a_i,a_j).
   \]
   We get
   \[
   \frac{2\,a_i a_j a_k}{a_i+a_j}\le\frac{(a_i+a_j)a_k}{2},\quad
   \frac{2\,a_i a_j a_k}{a_i+a_k}\le\frac{(a_i+a_k)a_j}{2},\quad
   \frac{2\,a_i a_j a_k}{a_j+a_k}\le\frac{(a_j+a_k)a_i}{2}.
   \]
   Adding these three inequalities gives
   \[
   2\Bigl(\tfrac{a_i a_j a_k}{a_i+a_j}+\tfrac{a_i a_j a_k}{a_i+a_k}+\tfrac{a_i a_j a_k}{a_j+a_k}\Bigr)
   \;\le\;
   \tfrac12\bigl[(a_i+a_j)a_k+(a_i+a_k)a_j+(a_j+a_k)a_i\bigr].
   \]
   But the bracket on the right expands to
   \[
   (a_i a_k+a_j a_k)+(a_i a_j+a_i a_k)+(a_j a_i+a_j a_k)
   \;=\;
   2\,(a_i a_j+a_i a_k+a_j a_k),
   \]
   so after dividing by \(2\) we obtain exactly
   \[
   \frac{a_i a_j a_k}{a_i+a_j}+\frac{a_i a_j a_k}{a_i+a_k}+\frac{a_i a_j a_k}{a_j+a_k}
   \;\le\;
   \tfrac12\,(a_i a_j+a_i a_k+a_j a_k),
   \]
   as required.

Putting everything together, we have shown that
\[
2\sum_{i<j}\frac{a_i\,a_j}{a_i+a_j}
\;\le\;
n\sum_{i<j}a_i\,a_j,
\]
under the normalization \(a_1+\cdots+a_n=1\).  Re-introducing the factor \(s=a_1+\cdots+a_n\) restores the general case, and so the original inequality

\[
\sum_{1\le i<j\le n}\frac{a_i\,a_j}{a_i+a_j}
\;\le\;
\frac{n}{2(a_1+\cdots+a_n)}\sum_{1\le i<j\le n}a_i\,a_j
\]

holds for all positive real \(a_1,\dots,a_n\), with equality if and only if \(a_1=a_2=\cdots=a_n\).  This completes the proof.