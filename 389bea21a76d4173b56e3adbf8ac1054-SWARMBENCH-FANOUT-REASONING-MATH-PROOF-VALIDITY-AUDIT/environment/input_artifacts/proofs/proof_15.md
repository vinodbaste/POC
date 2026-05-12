<!-- DOMAIN_BACKGROUND: /input_artifacts/background_combinatorics.md -->
<!-- REQUIRED: Read /input_artifacts/background_combinatorics.md before evaluating this proof. -->

    # proof_15

    - Problem ID: USAMO_2019_4
    - Competition: USAMO
    - Year: 2019
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 47

    ## Problem

    Let \( n \) be a nonnegative integer. Determine the number of ways to choose sets \( S_{ij} \subseteq \{1, 2, \ldots, 2n\} \), for all \( 0 \leq i \leq n \) and \( 0 \leq j \leq n \) (not necessarily distinct), such that:
- \(|S_{ij}| = i + j\), and
- \( S_{ij} \subseteq S_{kl} \) if \( 0 \leq i \leq k \leq n \) and \( 0 \leq j \leq l \leq n \).

    ## Candidate Solution Attempt

    **Solution.**  
We show that once the “boundary” chains 
\[
A_0\subset A_1\subset\cdots\subset A_n
\quad\text{and}\quad
B_0\subset B_1\subset\cdots\subset B_n
\]
of subsets of \(\{1,\dots,2n\}\), with \(\lvert A_i\rvert=i\) and \(\lvert B_j\rvert=j\), are chosen, there is a unique way to fill in all the sets \(S_{ij}\).  We then count the number of such boundary‐chain pairs.

---

1. **Reduction to boundary chains.**  
   Write  
   \[
     A_i:=S_{i,0},\quad B_j:=S_{0,j}.
   \]  
   By hypothesis \(\lvert A_i\rvert=i\) and \(\lvert B_j\rvert=j\).  Moreover for every \(i,j\) the monotonicity
   \[
     S_{i,0}=A_i\subseteq S_{i,j},\qquad
     S_{0,j}=B_j\subseteq S_{i,j},
   \]
   forces
   \[
     A_i\cup B_j\;\subseteq\;S_{i,j}.
   \]
   Since \(\lvert S_{i,j}\rvert=i+j\) while \(\lvert A_i\cup B_j\rvert\le i+j\), the only possibility is
   \[
     S_{i,j}\;=\;A_i\;\cup\;B_j,
   \]
   and moreover
   \[
     \lvert A_i\cap B_j\rvert
      \;=\;\lvert A_i\rvert+\lvert B_j\rvert-\lvert A_i\cup B_j\rvert
      \;=\;i+j-(i+j)
      \;=\;0.
   \]
   In particular
   \[
     A_i\cap B_j=\emptyset
     \quad\forall\,i,j,
   \]
   so \emph{all} the \(A\)–chain and \(B\)–chain sets must be pairwise disjoint.

2. **Counting boundary chains.**  
   We must choose two \emph{disjoint} chains
   \[
     \emptyset=A_0\subset A_1\subset\cdots\subset A_n,
     \quad
     \emptyset=B_0\subset B_1\subset\cdots\subset B_n,
   \]
   with \(\lvert A_i\rvert=i\), \(\lvert B_j\rvert=j\), and \(A_n\cap B_n=\emptyset\).  

   (i)  First choose \(A_n\), any \(n\)\nobreakdash‐element subset of \(\{1,\dots,2n\}\):  
        \(\displaystyle\binom{2n}{n}\) choices.  
   (ii) Then \(B_n\) must be an \(n\)\nobreakdash‐element subset of the \emph{complement} of \(A_n\).  
        But \(\bigl|\{1,\dots,2n\}\setminus A_n\bigr|=n\), so there is exactly one way to choose \(B_n\).  
   (iii)  Finally, inside \(A_n\) we build the chain
        \(\emptyset=A_0\subset A_1\subset\cdots\subset A_n\);  at step \(i\) we choose the one new element of \(A_i\) from the \(n-(i-1)\) remaining points in \(A_n\).  Hence there are
        \[
           n\;\times\;(n-1)\;\times\cdots\;1
           \;=\;n!
        \]
        ways to build the \(A\)–chain.  Likewise there are \(n!\) ways to build the \(B\)–chain inside its \(n\)\nobreakdash‐element set.

Putting it all together,
\[
  \#\{\,(S_{ij})\}
  \;=\;
  \binom{2n}{n}
  \;\times\;
  1
  \;\times\;
  n!
  \;\times\;
  n!
  \;=\;
  \binom{2n}{n}\,(n!)^2.
\]
Notice that
\[
  \binom{2n}{n}\,(n!)^2
  \;=\;
  \frac{(2n)!}{n!\,n!}\;\times\;(n!)^2
  \;=\;(2n)!.
\]
Hence the final answer may be written in either of the equivalent forms

\[
   \boxed{
     \binom{2n}{n}\,(n!)^2
     \quad\text{or}\quad
     (2n)!.
   }
\]

---

**Verification for small \(n\).**  
- \(n=0\).  There is only the one set \(S_{00}\), of size \(0\), namely \(\varnothing\).  The formula \((2\cdot0)!=0!=1\) is correct.  
- \(n=1\).  One must choose
   \[
     A_1=S_{1,0},\;B_1=S_{0,1}
     \subseteq\{1,2\},
     \quad
     \lvert A_1\rvert=\lvert B_1\rvert=1,
     \quad
     A_1\cap B_1=\emptyset.
   \]
  There are \(\binom2{1}=2\) ways to choose \(A_1\), and then \(B_1\) is forced to be its complement; and each chain has \(1!=1\) way to interpolate.  Thus \(2\) choices total.  Equivalently \((2\cdot1)!=2!=2\).  

  One checks directly that once \(A_1\) and \(B_1\) are fixed, \(S_{1,1}=A_1\cup B_1\) is the unique way to get cardinality \(2\).  

- \(n=2\).  One first picks \(A_2\subset\{1,2,3,4\}\) of size \(2\) in \(\binom4{2}=6\) ways; then \(B_2\) is its complement (no further choice); then each of the two chains has \(2!=2\) ways to build it.  Total \(6\cdot2\cdot2=24\cdot2=24\).  Equivalently \((2\cdot2)!=4!=24\).

In each case the boundary‐chain procedure indeed reproduces precisely all families \(\{S_{ij}\}\) with the stated properties.

---

**Conclusion.**  
The **number** of ways to choose the sets \(S_{ij}\subseteq\{1,\dots,2n\}\), \(0\le i,j\le n\), so that
\[
  |S_{ij}|=i+j,
  \quad
  S_{ij}\,\subseteq\,S_{k\ell}
  \quad\text{whenever }i\le k,\;j\le\ell,
\]
is
\[
   \boxed{%
     \binom{2n}{n}\,(n!)^2
     \;=\;(2n)!\,.
   }
\]